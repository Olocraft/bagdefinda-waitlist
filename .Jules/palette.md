## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-24 - Semantic Landmarks & Focus Management
**Learning:** Native smooth scrolling scripts often hijack focus behavior, breaking accessibility for skip links. Explicitly excluding skip links (`:not(.skip-link)`) from such scripts is crucial.
**Action:** Always verify focus destination when implementing skip links, and ensure the target has `tabindex="-1"` if it's a non-interactive element like `<main>`.
