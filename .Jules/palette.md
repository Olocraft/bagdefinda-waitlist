## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-23 - Skip Link & Smooth Scroll Interaction
**Learning:** Custom smooth scrolling scripts that intercept all hash links (`a[href^="#"]`) break accessibility features like "Skip to main content" links, preventing them from moving keyboard focus.
**Action:** Always exclude skip links from smooth scrolling selectors (e.g., `a[href^="#"]:not(.skip-link)`) to preserve native focus behavior.
