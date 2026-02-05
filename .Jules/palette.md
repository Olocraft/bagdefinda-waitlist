## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-24 - Semantic Landmarks in Static Sites
**Learning:** Static single-page sites often rely on visual hierarchy but miss semantic landmarks (`<main>`) and bypass blocks (skip links), creating significant barriers for keyboard and screen reader users.
**Action:** Always wrap primary content in `<main>` and provide a hidden-until-focused "Skip to content" link as the first interactive element. Ensure the target has `tabindex="-1"` to receive focus.
