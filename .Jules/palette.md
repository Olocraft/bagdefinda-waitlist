## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2026-01-15 - Skip Links and Smooth Scrolling
**Learning:** Generic smooth scrolling scripts that target all hash links (e.g., `a[href^="#"]`) often trap "Skip to content" links, preventing instant keyboard navigation and sometimes failing to move focus entirely.
**Action:** Explicitly exclude `.skip-link` class from smooth scroll selectors (e.g., `a[href^="#"]:not(.skip-link)`) and ensure the target main container has `tabindex="-1"` to guarantee focus moves correctly.
