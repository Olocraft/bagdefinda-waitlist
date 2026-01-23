## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-24 - Focus Management and Landmarks
**Learning:** Adding a "Skip to content" link requires careful management of focus targets. The target container (e.g., `<main>`) must have `tabindex="-1"` to be programmatically focusable, ensuring the user's focus actually moves there for subsequent navigation.
**Action:** Always pair internal skip links with a corresponding `tabindex="-1"` and `outline: none` (for visual polish) on the target container. Ensure smooth-scroll scripts do not hijack these functional jumps.
