## 2025-12-24 - Inline Validation & Accessibility
**Learning:** Browser native validation (`type="email"`) is good, but custom JS validation using `alert()` is disruptive. Users prefer inline feedback. Also, visually hidden labels are essential for inputs that rely on visual context (like placeholders) to be accessible to screen readers.
**Action:** Always check for missing `<label>` tags on inputs. If visual design prevents a visible label, use `.visually-hidden`. Replace `alert()` with inline UI feedback (`role="alert"` for a11y) whenever possible.
