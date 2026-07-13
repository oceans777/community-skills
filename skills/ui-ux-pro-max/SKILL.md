---
name: ui-ux-pro-max
description: "Use when designing, building, or refining frontend UI/UX: layouts, components, visual systems, typography, color, and UX patterns for websites, landing pages, dashboards, and product interfaces. Provides searchable styles, palettes, font pairings, charts, and stack best practices (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind)."
---

# UI/UX Pro Max - Design Intelligence

Searchable database of UI styles, color palettes, font pairings, chart types, product recommendations, UX guidelines, and stack-specific best practices.

## How to Use This Skill

Run the commands from the skill directory (`$CODEX_HOME/skills/ui-ux-pro-max`) so `scripts/search.py` resolves, or provide an absolute path to the script. If `python` is not available, use `python3`.

When user requests UI/UX work (design, build, create, implement, review, fix, improve), follow this workflow:

Choose the smallest useful path:

- **Focused fix**: For a small existing-component issue such as spacing, contrast, one interaction state, or responsive overflow, inspect the project design system first and search only one or two directly relevant domains.
- **Full design**: For a new page, redesign, design system, landing page, or broad UX review, use the full workflow below.

Treat search results as candidates, not mandates. Apply this priority order:

1. Explicit user requirements
2. The project's existing design system and component conventions
3. Accessibility and platform guidance
4. Search database recommendations

### Step 1: Analyze User Requirements

Extract key information from user request:
- **Product type**: SaaS, e-commerce, portfolio, dashboard, landing page, etc.
- **Style keywords**: minimal, playful, professional, elegant, dark mode, etc.
- **Industry**: healthcare, fintech, gaming, education, etc.
- **Stack**: React, Vue, Next.js, or default to `html-tailwind`

### Step 2: Search Relevant Domains

For full-design work, use `search.py` across the relevant domains until you have enough context. For focused fixes, run only the searches that can change the implementation.

```bash
python scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**Recommended search order:**

1. **Product** - Get style recommendations for product type
2. **Style** - Get detailed style guide (colors, effects, frameworks)
3. **Typography** - Get font pairings with Google Fonts imports
4. **Color** - Get color palette (Primary, Secondary, CTA, Background, Text, Border)
5. **Landing** - Get page structure (if landing page)
6. **Chart** - Get chart recommendations (if dashboard/analytics)
7. **UX** - Get best practices and anti-patterns
8. **Stack** - Get stack-specific guidelines (default: html-tailwind)

### Step 3: Stack Guidelines (infer from project first)

If the user doesn't specify a stack, inspect the project and infer it. Default to `html-tailwind` only for a new standalone artifact with no existing stack.

```bash
python scripts/search.py "<keyword>" --stack html-tailwind
```

Available stacks: `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`

---

## Search Reference

### Available Domains

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `product` | Product type recommendations | SaaS, e-commerce, portfolio, healthcare, beauty, service |
| `style` | UI styles, colors, effects | glassmorphism, minimalism, dark mode, brutalism |
| `typography` | Font pairings, Google Fonts | elegant, playful, professional, modern |
| `color` | Color palettes by product type | saas, ecommerce, healthcare, beauty, fintech, service |
| `landing` | Page structure, CTA strategies | hero, hero-centric, testimonial, pricing, social-proof |
| `chart` | Chart types, library recommendations | trend, comparison, timeline, funnel, pie |
| `ux` | Best practices, anti-patterns | animation, accessibility, z-index, loading |
| `prompt` | AI prompts, CSS keywords | (style name) |

### Available Stacks

| Stack | Focus |
|-------|-------|
| `html-tailwind` | Tailwind utilities, responsive, a11y (DEFAULT) |
| `react` | State, hooks, performance, patterns |
| `nextjs` | SSR, routing, images, API routes |
| `vue` | Composition API, Pinia, Vue Router |
| `svelte` | Runes, stores, SvelteKit |
| `swiftui` | Views, State, Navigation, Animation |
| `react-native` | Components, Navigation, Lists |
| `flutter` | Widgets, State, Layout, Theming |

---

## Example Workflow

**User request:** "Làm landing page cho dịch vụ chăm sóc da chuyên nghiệp"

**AI should:**

```bash
# 1. Search product type
python scripts/search.py "beauty spa wellness service" --domain product

# 2. Search style (based on industry: beauty, elegant)
python scripts/search.py "elegant minimal soft" --domain style

# 3. Search typography
python scripts/search.py "elegant luxury" --domain typography

# 4. Search color palette
python scripts/search.py "beauty spa wellness" --domain color

# 5. Search landing page structure
python scripts/search.py "hero-centric social-proof" --domain landing

# 6. Search UX guidelines
python scripts/search.py "animation" --domain ux
python scripts/search.py "accessibility" --domain ux

# 7. Search stack guidelines (default: html-tailwind)
python scripts/search.py "layout responsive" --stack html-tailwind
```

**Then:** Synthesize all search results and implement the design.

---

## Tips for Better Results

1. **Be specific with keywords** - "healthcare SaaS dashboard" > "app"
2. **Search multiple times** - Different keywords reveal different insights
3. **Combine domains** - Style + Typography + Color = Complete design system
4. **Always check UX** - Search "animation", "z-index", "accessibility" for common issues
5. **Use stack flag** - Get implementation-specific best practices
6. **Iterate** - If first search doesn't match, try different keywords

---

## Common Rules for Professional UI

These are defaults for new UI. Existing product conventions and platform-native behavior take precedence.

### Icons & Visual Elements

| Rule | Enforce |
|------|---------|
| **Consistent icon language** | Prefer the project's existing icon system. For a new web UI, use one coherent SVG set; reserve emojis for intentional content or brand expression. |
| **Stable hover states** | Use color/opacity transitions on hover; keep layout dimensions fixed to prevent shift. |
| **Correct brand logos** | Pull official SVGs from Simple Icons or brand sites; verify the latest mark before use. |
| **Consistent icon sizing** | Standardize viewBox (24x24) and apply w-6 h-6 (or equivalent) across the set. |

### Interaction & Cursor

| Rule | Enforce |
|------|---------|
| **Pointer cues** | Preserve native platform cursor behavior and add pointer cues to custom clickable surfaces when the project design system does not already handle them. |
| **Hover feedback** | Provide clear visual feedback (color, shadow, border) on hover and focus. |
| **Smooth transitions** | Use restrained motion appropriate to the platform and respect reduced-motion preferences; 150-300ms is a common web default, not a universal requirement. |

### Light/Dark Mode Contrast

| Rule | Enforce |
|------|---------|
| **Glass card light mode** | Use `bg-white/80` or higher opacity for glass surfaces. |
| **Light text contrast** | Use `#0F172A` (slate-900) or darker for body text to meet 4.5:1 contrast. |
| **Muted text light** | Use `#475569` (slate-600) or darker for secondary text. |
| **Border visibility** | Use `border-gray-200` or higher in light mode so edges remain visible. |

### Layout & Spacing

| Rule | Enforce |
|------|---------|
| **Floating navbar spacing** | Add `top-4 left-4 right-4` (or equivalent) margin for floating navbars. |
| **Content clearance** | Add top padding equal to the fixed navbar height to keep content visible. |
| **Consistent max-width** | Use a single container width (e.g., `max-w-6xl` or `max-w-7xl`) across sections. |

---

## Pre-Delivery Checklist

Before delivering UI code, verify these items:

### Visual Quality
- [ ] Icon treatment follows the project design system and user intent
- [ ] New icon sets are internally consistent when the project has no existing set
- [ ] Brand logos are correct (verified from Simple Icons)
- [ ] Hover states don't cause layout shift
- [ ] Theme tokens are used through the project's established styling mechanism

### Interaction
- [ ] Custom clickable surfaces have appropriate pointer/focus cues for the target platform
- [ ] Hover states provide clear visual feedback
- [ ] Transitions are smooth (150-300ms)
- [ ] Focus states visible for keyboard navigation

### Light/Dark Mode
- [ ] Light mode text has sufficient contrast (4.5:1 minimum)
- [ ] Glass/transparent elements visible in light mode
- [ ] Borders visible in both modes
- [ ] Test both modes before delivery

### Layout
- [ ] Floating elements have proper spacing from edges
- [ ] No content hidden behind fixed navbars
- [ ] Responsive at 320px, 768px, 1024px, 1440px
- [ ] No horizontal scroll on mobile

### Accessibility
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Color is not the only indicator
- [ ] `prefers-reduced-motion` respected
