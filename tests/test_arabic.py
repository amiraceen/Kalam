"""Arabic clean-up. Run: python3 -m unittest discover -s tests"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import arabic  # noqa: E402


class ArabicNormalizeTest(unittest.TestCase):

    def test_diacritics_tatweel_digits(self):
        self.assertEqual(arabic.normalize("مَرْحَباً بِكُمْ في الاجتمـــاع رقم ٣"), "مرحبا بكم في الاجتماع رقم 3")

    def test_latin_punctuation_becomes_arabic(self):
        self.assertEqual(arabic.normalize("هل ترون الشاشة ? نعم , واضحة ; شكرا"), "هل ترون الشاشة؟ نعم، واضحة؛ شكرا")
        self.assertEqual(arabic.normalize("السعر 3,500 ريال"), "السعر 3,500 ريال")     # numbers untouched
        self.assertEqual(arabic.normalize("الساعة 4.30"), "الساعة 4.30")

    def test_english_unchanged(self):
        self.assertEqual(arabic.normalize("Hi team, can we meet at 3.30?"), "Hi team, can we meet at 3.30?")

    def test_mixed_mostly_arabic(self):
        self.assertEqual(arabic.normalize("أرسل الملف على Slack , لو سمحت ?"), "أرسل الملف على Slack، لو سمحت؟")

    def test_fillers(self):
        self.assertEqual(arabic.remove_fillers("اممم أبي أحجز موعد"), "أبي أحجز موعد")
        self.assertEqual(arabic.remove_fillers("آه تمام"), "آه تمام")                   # Egyptian "yes" stays
        self.assertEqual(arabic.remove_fillers("الممثل"), "الممثل")                     # not inside words


class LanguagePickTest(unittest.TestCase):
    """Auto-detect only ever picks Arabic or English, leaning Arabic."""

    def test_pick(self):
        import speed
        self.assertEqual(speed.pick_language([("he", 0.45), ("ar", 0.2), ("en", 0.2)]), "ar")   # was Hebrew
        self.assertEqual(speed.pick_language([("en", 0.5), ("ar", 0.3)]), "ar")                # was English
        self.assertEqual(speed.pick_language([("en", 0.9), ("ar", 0.04)]), "en")
        self.assertEqual(speed.pick_language([("fr", 0.9), ("en", 0.05)]), "en")

    def test_prompt(self):
        self.assertIn("شحالش", arabic.initial_prompt("ar"))
        self.assertIn("أقولش", arabic.initial_prompt("ar"))          # Omani -ش, not "أقول ليش"
        self.assertIn("email", arabic.initial_prompt("ar"))          # English words stay in Latin
        self.assertTrue(arabic.initial_prompt("ar", ["مسقط"]).endswith("مسقط"))
        self.assertEqual(arabic.initial_prompt("en", ["Maal", "Kalam"]), "Maal, Kalam")
        self.assertIsNone(arabic.initial_prompt("en"))
        self.assertIsNone(arabic.initial_prompt("ar", dialect=False))


class ModelStoreTest(unittest.TestCase):

    def test_download_then_ready(self):
        import tempfile
        import threading
        import models
        calls, gate = [], threading.Event()

        def fake(name, folder):
            calls.append(name)
            gate.wait(2)
            with open(os.path.join(folder, "model.bin"), "wb") as f:
                f.write(b"x" * 1000)

        store = models.ModelStore(tempfile.mkdtemp(), builtin_path="/app/model", downloader=fake)
        self.assertTrue(store.ready("small"))
        self.assertEqual(store.path("small"), "/app/model")
        self.assertFalse(store.ready("extensive"))
        done = []
        store.download("extensive", done.append)
        self.assertEqual(store.downloading, "extensive")
        self.assertIsNotNone(store.progress())
        store.download("extensive", done.append)        # second click while running: ignored
        gate.set()
        store._thread.join(2)
        self.assertEqual((calls, done), (["turbo", "dialect"], [True]))   # both halves, one click
        self.assertTrue(store.ready("extensive"))
        self.assertIsNone(store.progress())
        base, ar = store.path("extensive")
        self.assertTrue(base.endswith("whisper-large-v3-turbo-mlx"))
        self.assertTrue(ar.endswith("whisper-turbo-arabic-dialects-mlx"))
        self.assertEqual(store.engine("extensive"), "mlx")
        self.assertTrue(store.dialect_prompt("extensive"))
        self.assertFalse(store.dialect_prompt("small"))

    def test_extensive_reuses_an_earlier_download(self):
        import tempfile
        import models
        folder, calls = tempfile.mkdtemp(), []
        os.makedirs(os.path.join(folder, "whisper-large-v3-turbo-mlx"))
        open(os.path.join(folder, "whisper-large-v3-turbo-mlx", ".complete"), "w").close()
        store = models.ModelStore(folder, downloader=lambda name, f: calls.append(name))
        store.download("extensive", lambda ok: None)
        store._thread.join(2)
        self.assertEqual(calls, ["dialect"])            # Accurate from before is kept
        self.assertTrue(store.ready("extensive"))

    def test_old_model_choices_become_extensive(self):
        import json
        import tempfile
        import settings
        path = os.path.join(tempfile.mkdtemp(), "settings.json")
        for old in ("turbo", "large", "dialect"):
            with open(path, "w") as f:
                json.dump({"speech_model": old}, f)
            self.assertEqual(settings.Settings(path)["speech_model"], "extensive")

    def test_removes_old_cpu_turbo_download(self):
        import tempfile
        import models
        folder = tempfile.mkdtemp()
        for name in ("large-v3-turbo", "whisper-large-v3-mlx"):
            os.makedirs(os.path.join(folder, name))
        models.ModelStore(folder)
        for name in ("large-v3-turbo", "whisper-large-v3-mlx"):
            self.assertFalse(os.path.exists(os.path.join(folder, name)))

    def test_failed_download_reports_error(self):
        import tempfile
        import models

        def fail(name, folder):
            raise OSError("no internet")

        store = models.ModelStore(tempfile.mkdtemp(), downloader=fail)
        done = []
        store.download("extensive", done.append)
        store._thread.join(2)
        self.assertEqual(done, [False])
        self.assertEqual(store.error, "no internet")
        self.assertFalse(store.ready("extensive"))


if __name__ == "__main__":
    unittest.main()
