## 2025-10-26 - Inline Validation Pattern
**Learning:** Native `alert()` is disruptive and `input type="email"` validation can block custom JS handlers unless `novalidate` is used on the form.
**Action:** Always use `novalidate` on forms when implementing custom inline validation to ensure a consistent, accessible UI experience. Replace alerts with inline messages reusing existing success/notification containers styled for errors.
