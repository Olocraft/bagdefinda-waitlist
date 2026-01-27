## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-23 - Smooth Scroll & Accessibility
**Learning:** Custom smooth scrolling implementations that `preventDefault()` on all anchor links often break "Skip to content" functionality because they don't manage focus transfer.
**Action:** When implementing smooth scroll, always exclude skip links (e.g., `:not(.skip-link)`) or ensure the JS explicitly moves focus to the target element.
