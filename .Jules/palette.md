## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-24 - Skip Links & Smooth Scroll
**Learning:** Adding a "Skip to content" link requires checking existing JavaScript smooth-scroll handlers, which often intercept all hash links (`a[href^="#"]`). This can break the native focus management required for skip links.
**Action:** Always exclude skip links from smooth-scroll selectors (e.g., `a[href^="#"]:not(.skip-link)`) to preserve native jump-to-content behavior for keyboard users.
