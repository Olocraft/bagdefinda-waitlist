## 2025-02-18 - Minimalist Forms vs Accessibility
**Learning:** "Minimalist" designs often strip away `<label>` elements in favor of `placeholder` text, which creates significant accessibility barriers. Users relying on screen readers may miss the purpose of the field, and placeholders disappear when typing, losing context.
**Action:** When encountering label-less forms, always add visually hidden labels or `aria-label` attributes to restore accessibility without compromising the visual design.
