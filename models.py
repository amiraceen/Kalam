"""
Speech models: the built-in Whisper "small" (CPU) and the optional "Extensive" model that
runs on the Mac's graphics chip (MLX). Extensive is two downloads used together: Whisper
large-v3-turbo, which picks the language and writes English, and a version of it retrained
on Arabic dialects, which writes Arabic. Downloaded once into the app's data folder, then
works offline. No AppKit here.
"""

import os
import shutil
import threading

MODELS = {
    # choice: (folder / faster-whisper name, label, download size in bytes or 0 if built in, engine)
    "small": ("small", "Whisper small", 0, "cpu"),
    "turbo": ("whisper-large-v3-turbo-mlx", "Whisper large-v3-turbo", 1_620_000_000, "mlx"),
    "dialect": ("whisper-turbo-arabic-dialects-mlx", "Whisper turbo · Arabic dialects", 3_240_000_000, "mlx"),
    "extensive": (None, "Whisper turbo + Arabic dialects", 4_860_000_000, "mlx"),
}
# A choice made of other downloads: (language detection + English, Arabic).
PARTS = {"extensive": ("turbo", "dialect")}
# Where each download comes from. "dialect" is a Transformers-format fine-tune on Gulf/Saudi,
# Egyptian, Levantine and other dialects; the app converts it to MLX after download.
REPOS = {"turbo": "mlx-community/whisper-large-v3-turbo",
         "dialect": "oddadmix/whisper-large-v3-turbo-arabic-dialectal"}
CONVERT = {"dialect"}
# CPU turbo from an earlier build (too slow) and the full large-v3 that was offered for testing.
LEGACY_FOLDERS = ("large-v3-turbo", "whisper-large-v3-mlx")
# Choices from earlier builds, now all part of Extensive.
LEGACY_CHOICES = {"turbo": "extensive", "large": "extensive", "dialect": "extensive"}
MODEL_OPTIONS = [("small", "Fast · built in"), ("extensive", "Extensive · 4.9 GB download")]
_DONE = ".complete"


def _folder_size(path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total


def _hf_download(choice, folder):
    import mlx_engine
    if choice in CONVERT:
        import tempfile
        from huggingface_hub import snapshot_download
        src = tempfile.mkdtemp(dir=folder)
        try:
            snapshot_download(REPOS[choice], local_dir=src, allow_patterns=["config.json", "*.safetensors"])
            mlx_engine.convert_hf(src, folder)
        finally:
            shutil.rmtree(src, ignore_errors=True)       # keep only the converted copy
    else:
        mlx_engine.download(folder, REPOS[choice])


class ModelStore:
    """Where each model lives and whether it's ready; downloads in the background."""

    def __init__(self, folder, builtin_path=None, downloader=_hf_download):
        self.folder = folder
        self.builtin_path = builtin_path      # bundled "small" inside the app, or None (download/cache)
        self._download = downloader
        self.downloading = None               # choice being downloaded
        self.error = None
        self._thread = None
        for name in LEGACY_FOLDERS:
            shutil.rmtree(os.path.join(folder, name), ignore_errors=True)

    def _dir(self, part):
        return os.path.join(self.folder, MODELS[part][0])

    def _parts(self, choice):
        return PARTS.get(choice, (choice,))

    def _part_ready(self, part):
        return MODELS[part][2] == 0 or os.path.exists(os.path.join(self._dir(part), _DONE))

    def label(self, choice):
        return MODELS[choice][1]

    def engine(self, choice):
        return MODELS[choice][3]

    def dialect_prompt(self, choice):
        return MODELS[choice][3] == "mlx"

    def ready(self, choice):
        return all(self._part_ready(p) for p in self._parts(choice))

    def path(self, choice):
        """What to hand to the engine: a folder, a model name faster-whisper can fetch itself,
        or for Extensive a (turbo folder, Arabic folder) pair."""
        if MODELS[choice][2] == 0:
            return self.builtin_path or MODELS[choice][0]
        if choice in PARTS:
            return tuple(self._dir(p) for p in PARTS[choice])
        return self._dir(choice)

    def progress(self):
        """0..1 for the running download, else None."""
        if not self.downloading:
            return None
        parts = self._parts(self.downloading)
        done = sum(_folder_size(self._dir(p)) for p in parts)
        return min(0.99, done / sum(MODELS[p][2] for p in parts))

    def download(self, choice, on_done):
        """Start fetching `choice` (resumes a partial download). on_done(ok) runs on the worker."""
        if self.ready(choice):
            on_done(True)
            return
        if self.downloading:
            return
        self.downloading, self.error = choice, None

        def work():
            ok = False
            try:
                for part in self._parts(choice):
                    if self._part_ready(part):
                        continue                 # e.g. Accurate was downloaded by an earlier build
                    os.makedirs(self._dir(part), exist_ok=True)
                    self._download(part, self._dir(part))
                    open(os.path.join(self._dir(part), _DONE), "w").close()
                ok = True
            except Exception as e:
                self.error = str(e) or type(e).__name__
            finally:
                self.downloading = None
            on_done(ok)

        self._thread = threading.Thread(target=work, daemon=True)
        self._thread.start()

    def remove(self, choice):
        if MODELS[choice][2] and not self.downloading:
            for part in self._parts(choice):
                shutil.rmtree(self._dir(part), ignore_errors=True)
