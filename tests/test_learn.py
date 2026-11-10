import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import learn


def test_apply_fixes_whole_words_any_case():
    fixes = {"hexfield": "Higgsfield", "higgs field": "Higgsfield"}
    assert learn.apply_fixes("the Hexfield shot, higgs  field too.", fixes) == "the Higgsfield shot, Higgsfield too."
    assert learn.apply_fixes("hexfields", fixes) == "hexfields"


def test_find_fixes_inside_a_longer_field():
    typed = "Can you write the Sedan prompt for the Hexfield shot?"
    field = "Hi. Can you write the Seedance prompt for the Higgsfield shot? thanks"
    assert learn.find_fixes(typed, field) == [("Sedan", "Seedance"), ("Hexfield", "Higgsfield")]


def test_find_fixes_ignores_punctuation_case_rephrasing_and_other_text():
    assert learn.find_fixes("open the folder for", "Open the folder for.") == []
    assert learn.find_fixes("I like the blue one", "I like the red one") == []
    assert learn.find_fixes("hello world how are you", "totally different message now") == []


def test_learner_remembers_accepted_and_declined(tmp_path):
    d = str(tmp_path)
    lr = learn.Learner(d, os.path.join(d, "dictionary.txt"))
    words = lr.accept("Hexfield", "Higgsfield", ["Kalam"])
    assert words == ["Kalam", "Higgsfield"]
    lr.decline("disdash", "dish")
    lr = learn.Learner(d, os.path.join(d, "dictionary.txt"))
    assert lr.apply("in Hexfield") == "in Higgsfield"
    assert lr.new_fixes("a disdash and Hexfield", "a dish and Higgsfield") == []
    assert lr.contains("one two three four", "x one two three four y")
    assert not lr.contains("one two three four", "")


def test_prompt_words_keep_newest():
    words = [f"w{i:03d}" for i in range(300)]
    kept = learn.prompt_words(words)
    assert kept[-1] == "w299" and len(", ".join(kept)) <= learn.PROMPT_CHARS
