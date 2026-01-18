## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-24 - Skip Links & JS Scroll
**Learning:** Custom smooth-scroll scripts targeting `a[href^="#"]` often hijack "Skip to content" links, preventing focus transfer.
**Action:** Always exclude skip links from smooth-scroll selectors (e.g., `:not(.skip-link)`) to ensure they function natively.
