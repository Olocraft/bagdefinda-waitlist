## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2026-01-31 - Smooth Scroll vs. Skip Links
**Learning:** Custom smooth scrolling scripts (`a[href^="#"]`) often intercept "Skip to content" links, preventing immediate focus transfer.
**Action:** Always exclude skip links from smooth scroll selectors (e.g., `:not(.skip-link)`) to ensure native browser focus behavior works correctly.
