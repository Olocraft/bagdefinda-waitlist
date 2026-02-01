## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2026-02-01 - Skip Links and Focus Management
**Learning:** Skip links require `tabindex="-1"` on the target container (e.g., `<main id="main-content">`) to ensure focus is reliably transferred and read by screen readers after activation.
**Action:** When implementing skip links, always ensure the target has `tabindex="-1"` and `outline: none` (to prevent visual focus ring on the container itself if desired), and verify existing smooth-scroll scripts do not hijack the jump.
