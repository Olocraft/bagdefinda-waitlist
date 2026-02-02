## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-24 - Smooth Scrolling & Skip Links
**Learning:** Custom smooth scrolling scripts that intercept all hash links (`a[href^="#"]`) break native focus management for "Skip to main content" links. The script scrolls but prevents the browser from moving focus to the target.
**Action:** When implementing smooth scrolling, always exclude skip links from the selector (e.g., `a[href^="#"]:not(.skip-link)`) or ensure the script explicitly moves focus to the target element.
