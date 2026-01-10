## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-23 - Skip Link & Smooth Scrolling
**Learning:** Custom smooth scrolling scripts (`scrollIntoView`) often highjack anchor clicks and break the native focus transfer required for "Skip to main content" links.
**Action:** When implementing skip links, always explicitly exclude them from smooth scrolling selectors (e.g., `a[href^="#"]:not(.skip-link)`) to ensure instant navigation and proper focus management.
