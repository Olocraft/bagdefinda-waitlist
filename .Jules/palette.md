## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-23 - Skip Links and Smooth Scrolling
**Learning:** Generic smooth scrolling scripts (targeting `a[href^="#"]`) intercept skip links, preventing focus from moving to the content.
**Action:** When adding skip links, always exclude them from smooth scroll selectors (e.g., `:not(.skip-link)`) and ensure the target element has `tabindex="-1"`.
