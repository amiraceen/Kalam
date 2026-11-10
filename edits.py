"""
Watches the text box Kalam just typed into, so it can learn from your corrections.

After a paste, the focused text field is read every 2 seconds (Accessibility) for up to
2 minutes. The last version that still contains the dictation is kept; when the text is
sent or cleared, the next dictation starts, or time runs out, it's compared with what Kalam
typed (learn.find_fixes). Main thread only. Password fields are never read.
"""

import time

POLL = 2.0
WATCH_FOR = 120.0


def _ax(elem, attr):
    from ApplicationServices import AXUIElementCopyAttributeValue
    err, value = AXUIElementCopyAttributeValue(elem, attr, None)
    return value if err == 0 else None


def focused_text_field():
    """The focused text element of the frontmost app, or None."""
    from AppKit import NSWorkspace
    from ApplicationServices import (AXUIElementCreateApplication, AXUIElementSetAttributeValue)
    app = NSWorkspace.sharedWorkspace().frontmostApplication()
    if app is None:
        return None
    ax_app = AXUIElementCreateApplication(app.processIdentifier())
    # Electron apps (Claude, Slack, VS Code…) only expose their text to Accessibility when asked.
    AXUIElementSetAttributeValue(ax_app, "AXManualAccessibility", True)
    elem = _ax(ax_app, "AXFocusedUIElement")
    if elem is None:
        return None
    if _ax(elem, "AXRole") == "AXSecureTextField" or _ax(elem, "AXSubrole") == "AXSecureTextField":
        return None
    return elem


def field_text(elem):
    value = _ax(elem, "AXValue")
    return str(value) if isinstance(value, str) or hasattr(value, "UTF8String") else None


class EditWatcher:
    def __init__(self, learner, on_fixes):
        self.learner = learner
        self.on_fixes = on_fixes          # on_fixes([(wrong, right), ...]) on the main thread
        self._elem = None
        self._typed = None
        self._last = None
        self._until = 0
        self._timer = None

    def watch(self, typed):
        """Start watching after a paste (main thread)."""
        self.finish()
        try:
            self._elem = focused_text_field()
        except Exception as e:
            print(f"edit watcher: {e}", flush=True)
            self._elem = None
        if self._elem is None:
            return
        self._typed, self._last, self._until = typed, None, time.time() + WATCH_FOR
        import rumps
        self._timer = rumps.Timer(self._poll, POLL)
        self._timer.start()

    def _poll(self, _=None):
        if self._elem is None:
            return
        text = None
        try:
            text = field_text(self._elem)
        except Exception:
            pass
        if text and self.learner.contains(self._typed, text):
            self._last = text
        elif self._last is not None:
            self.finish()                 # sent or cleared: judge the last version seen
            return
        if time.time() > self._until:
            self.finish()

    def finish(self):
        """Stop watching and report any fixes (also called when a new dictation starts)."""
        if self._timer is not None:
            self._timer.stop()
            self._timer = None
        typed, last = self._typed, self._last
        self._elem = self._typed = self._last = None
        if typed and last:
            fixes = self.learner.new_fixes(typed, last)
            if fixes:
                self.on_fixes(fixes)
