## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-23 - Skip Links & Smooth Scrolling
**Learning:** Custom smooth scrolling scripts (`preventDefault()` on `click`) often break accessible "Skip to Content" links by preventing the native focus jump.
**Action:** Always exclude skip links from smooth scrolling selectors (e.g., `:not(.skip-link)`) and ensure the target element has `tabindex="-1"` to receive programmatic focus reliably.
