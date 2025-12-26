## 2025-05-23 - Form Validation UX
**Learning:** Re-using success message containers for inline errors is a lightweight way to provide feedback without adding new DOM elements, but requires careful state management (timeouts).
**Action:** When implementing custom validation, always ensure native validation is disabled (`novalidate`) and that error states are cleared before showing new messages to prevent race conditions.
