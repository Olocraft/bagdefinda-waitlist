## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-24 - Smooth Scrolling vs. Skip Links
**Learning:** Custom smooth scrolling scripts that intercept `click` events and call `preventDefault()` often break "Skip to Content" links by preventing the browser from moving focus to the target element.
**Action:** When implementing smooth scrolling, explicitly exclude `.skip-link` elements from the selector (e.g., `a[href^="#"]:not(.skip-link)`) to ensure native focus management works for keyboard navigation.
