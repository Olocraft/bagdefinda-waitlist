## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-10-26 - Smooth Scroll Accessibility
**Learning:** Custom smooth scroll scripts that intercept all hash links often break focus management, rendering skip links useless for keyboard users.
**Action:** Exclude utility links (like `.skip-link`) from smooth scroll selectors (`:not(.skip-link)`) to preserve native focus behavior.
