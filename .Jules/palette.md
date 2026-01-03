## 2026-01-03 - Inline Validation & Error Recovery
**Learning:** When reusing a success message container for error messages (to save space or simplify UI), it's critical to explicitly reset any error-specific styles (color, border, background) before showing a subsequent success message. Otherwise, the success message will appear with error styling, confusing the user.
**Action:** Always create a `resetState()` or explicitly clear inline styles when transitioning between UI states, especially in vanilla JS implementations without a framework's state management.
