## 2024-05-23 - Minimalist Form Labels
**Learning:** Minimalist designs often use placeholders as labels, which is an accessibility anti-pattern. Users with cognitive disabilities may lose context when they start typing, and screen readers may not announce the field purpose correctly.
**Action:** Always include a `<label>` element. If the visual design forbids it, use a `.visually-hidden` class to keep it accessible to screen readers while maintaining the visual aesthetic.
