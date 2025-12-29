## 2024-05-23 - Inline Validation Pattern
**Learning:** Users prefer inline validation over browser alerts, but native HTML5 validation (bubbles) can conflict with custom JS validation.
**Action:** When implementing custom validation, always add `novalidate` to the form element to suppress browser bubbles and ensure a consistent custom error UI.
