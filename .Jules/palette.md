## 2025-05-23 - Form Validation Patterns
**Learning:** Browser native alerts (`alert()`) are extremely disruptive and poor for accessibility. Using a dedicated message container with `role="alert"` allows for polite, inline feedback.
**Action:** When replacing alerts with inline validation, ensure to also manage `aria-invalid` states on inputs and use `novalidate` on the form to prevent conflicting browser UI. Use `.visually-hidden` labels for "clean" designs to maintain accessibility.

## 2025-05-23 - Skip Links and Smooth Scrolling
**Learning:** Custom smooth scrolling scripts (`scrollIntoView`) often don't manage focus correctly, breaking skip links. Also, broad selectors like `a[href^="#"]` inadvertently catch skip links.
**Action:** Exclude skip links from smooth scrolling scripts (`:not(.skip-link)`) to allow native browser behavior (which handles focus correctly) or explicitly manage focus in the script.
