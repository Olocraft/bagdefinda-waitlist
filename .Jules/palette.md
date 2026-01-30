## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2026-01-30 - Skip Links and Smooth Scroll
**Learning:** Custom smooth scrolling scripts often hijack all anchor clicks, preventing "Skip to content" links from functioning correctly (they scroll but don't move focus).
**Action:** When implementing smooth scrolling, explicitly exclude skip links (e.g., `a[href^="#"]:not(.skip-link)`). Also ensure the target container (e.g., `<main>`) has `tabindex="-1"` to accept programmatic focus.
