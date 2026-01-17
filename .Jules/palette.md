## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-24 - Smooth Scrolling & Accessibility
**Learning:** Custom smooth scrolling implementations often hijack native anchor behavior, breaking accessibility features like "Skip to main content".
**Action:** Always exclude accessibility bypass links from smooth scroll selectors (e.g., `a[href^="#"]:not(.skip-link)`) and ensure the target container (e.g., `<main id="main-content">`) has `tabindex="-1"` so it receives focus after the jump.
