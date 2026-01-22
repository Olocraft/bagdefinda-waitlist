## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-24 - Skip Links & Focus Management
**Learning:** Adding a "Skip to main content" link requires careful interaction with custom smooth-scrolling scripts. Native jump-to-ID behavior is preferred for accessibility (instant focus transfer), so skip links should be excluded from smooth scroll interceptors.
**Action:** When implementing skip links, ensure the target element (e.g., `<main>`) has `tabindex="-1"` and `outline: none` to receive focus without a visual ring, and explicitly exclude `.skip-link` from global smooth-scroll selectors.
