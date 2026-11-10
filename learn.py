"""
Kalam learns your words. Pure Python, so it can be tested anywhere.

Two things make Whisper write what you mean:
  - the word list (dictionary.txt) goes into Whisper's prompt, so it already leans toward
    "Higgsfield" instead of "Higgs field" while it listens;
  - fixes (fixes.json) are applied to the text afterwards, for the words Whisper still
    gets wrong your way ("Hexfield" -> "Higgsfield").

Kalam grows both by itself: after it types, it watches the text field for a minute. When
you fix a word by hand, it asks once whether to learn the fix. Fixes you turn down are
remembered too (declined.json) and never asked again.
"""

import difflib
import json
import os
import re

_WORD = re.compile(r"[\w'’\-\.@]+", re.UNICODE)
_EDGE = ".,;:!?،؛؟\"'“”()[]"
# Whisper's prompt holds about 224 tokens; past that the start is cut off. Words are written
# most important last, so this budget keeps the newest and most-used ones.
PROMPT_CHARS = 600


def load_json(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def save_json(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def apply_fixes(text, fixes):
    """Replace each misheard word or phrase (whole words, any case) with the right spelling."""
    for wrong in sorted(fixes, key=len, reverse=True):
        right = fixes[wrong]
        pattern = r"(?<![\w])" + r"\s+".join(re.escape(w) for w in wrong.split()) + r"(?![\w])"
        text = re.sub(pattern, lambda _m: right, text, flags=re.IGNORECASE)
    return text


def prompt_words(words, limit=PROMPT_CHARS):
    """The words that fit in Whisper's prompt, keeping the end of the list (the newest)."""
    out, used = [], 0
    for w in reversed(words):
        used += len(w) + 2
        if used > limit:
            break
        out.append(w)
    return out[::-1]


def _tokens(text):
    return _WORD.findall(text)


def _core(word):
    return word.strip(_EDGE).casefold()


def find_fixes(typed, field, max_words=3):
    """What the user changed by hand: [(wrong, right), ...].

    `typed` is what Kalam pasted; `field` is the whole text box afterwards (it may hold other
    text too). Only word swaps count: changes in case or punctuation, added words and deleted
    words are ignored, so ordinary editing doesn't teach Kalam anything."""
    a = _tokens(typed)
    b = _tokens(field)
    if not a or not b:
        return []
    sm = difflib.SequenceMatcher(None, [_core(w) for w in a], [_core(w) for w in b], autojunk=False)
    blocks = [m for m in sm.get_matching_blocks() if m.size]
    if not blocks:
        return []
    # The part of the field where the dictation sits.
    lo = max(0, blocks[0].b - blocks[0].a)
    hi = min(len(b), blocks[-1].b + blocks[-1].size + (len(a) - blocks[-1].a - blocks[-1].size))
    region = b[lo:hi + max_words]
    sm = difflib.SequenceMatcher(None, [_core(w) for w in a], [_core(w) for w in region], autojunk=False)
    if sm.ratio() < 0.6:
        return []                        # not the same text any more (sent, cleared, rewritten)
    fixes = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "replace" or i2 - i1 > max_words or j2 - j1 > max_words:
            continue
        wrong = " ".join(w.strip(_EDGE) for w in a[i1:i2]).strip()
        right = " ".join(w.strip(_EDGE) for w in region[j1:j2]).strip()
        if not wrong or not right or wrong.casefold() == right.casefold():
            continue
        if not re.search(r"[^\W\d_]", right):
            continue                     # numbers or symbols only: not a spelling to learn
        if difflib.SequenceMatcher(None, wrong.casefold(), right.casefold()).ratio() < 0.3 \
                and len(wrong.split()) == len(right.split()) == 1 and len(wrong) > 3:
            continue                     # a different word, not a misspelling: user rephrased
        fixes.append((wrong, right))
    return fixes


class Learner:
    """Fixes, declined fixes and the word list, kept in the app's data folder."""

    def __init__(self, folder, dictionary_file):
        self.fixes_file = os.path.join(folder, "fixes.json")
        self.declined_file = os.path.join(folder, "declined.json")
        self.dictionary_file = dictionary_file
        self.fixes = load_json(self.fixes_file, {})
        self.declined = {tuple(p) for p in load_json(self.declined_file, [])}

    def reload(self):
        self.fixes = load_json(self.fixes_file, {})

    def apply(self, text):
        return apply_fixes(text, self.fixes)

    def contains(self, typed, field):
        """True while the field still holds (an edited version of) the dictation."""
        a = [_core(w) for w in _tokens(typed)]
        b = [_core(w) for w in _tokens(field)]
        if not a or not b:
            return False
        hit = sum(m.size for m in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
        return hit / len(a) >= 0.6

    def new_fixes(self, typed, field):
        """Fixes worth asking about: not already known and not turned down before."""
        out = []
        for wrong, right in find_fixes(typed, field):
            key = (wrong.casefold(), right)
            if key in self.declined or self.fixes.get(wrong.casefold()) == right:
                continue
            out.append((wrong, right))
        return out

    def accept(self, wrong, right, words):
        """Learn a fix; returns the word list with the right spelling added (most recent last)."""
        self.fixes[wrong.casefold()] = right
        save_json(self.fixes_file, self.fixes)
        words = [w for w in words if w.casefold() != right.casefold()] + [right]
        return words

    def decline(self, wrong, right):
        self.declined.add((wrong.casefold(), right))
        save_json(self.declined_file, sorted(self.declined))

    def save_fixes(self, fixes):
        self.fixes = {str(k).casefold(): str(v) for k, v in fixes.items()}
        save_json(self.fixes_file, self.fixes)
