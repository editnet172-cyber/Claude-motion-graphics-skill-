---
name: motion-graphics-ad-studio
description: Create studio-grade SaaS motion graphics videos, commercial ads, product promos, kinetic typography reels, and explainer videos with Remotion (React/TypeScript) or HTML5 Canvas. Use whenever the user asks to make a motion graphics video, SaaS launch ad, promo video, social media reel, kinetic typography animation, product commercial, or animated UI showcase.
---

# Motion Graphics Ad Studio

Generate agency-quality motion graphics videos, SaaS product launch commercials, e-commerce promos, and kinetic typography reels from a single prompt with deterministic physics, glassmorphic UI components, and automated frame-level quality verification.

## When to Use

- The user asks to create a motion graphics video, commercial ad, SaaS product launch promo, or explainer video.
- The user wants a social media video in 16:9 (YouTube/Web), 9:16 (Reels/Shorts/TikTok), or 1:1 (Feed) format.
- The user asks for Apple, Linear, Stripe, or Vercel-style glassmorphic UI animations, kinetic typography, 3D floating orbs, charts, lower thirds, or logo reveals.
- The user wants to turn a product description, landing page, or script into a rendered `.mp4` video without manual editing.

## Steps

### Step 1: Lock Composition Specs and Aspect Ratio

Select the target resolution and frame rate before writing any scene code. Always default to **60 fps** (or **30 fps** for lightweight previews) so spring animations and kinetic typography render without motion judder.

- **Landscape SaaS / Launch Ad (16:9)**: `1920x1080` at `60fps`, safe-zone padding `96px` horizontal, `72px` vertical.
- **Vertical Reel / Short / TikTok Ad (9:16)**: `1080x1920` at `60fps`, safe-zone padding `72px` horizontal, `180px` top/bottom (clears platform UI overlays).
- **Square Feed Ad (1:1)**: `1080x1080` at `60fps`, safe-zone padding `80px` all sides.

### Step 2: Plan the 8-Scene Commercial Storyboard

Never animate a single static screen for more than 3.5 seconds. Break every commercial ad into a high-retention multi-scene sequence where visual energy peaks every 60 to 120 frames:

1. **Scene 1 - Pattern-Interrupt Hook (0.0s - 2.5s)**: Atmospheric backdrop or minimal canvas with staggered word-by-word kinetic hook text and subtle camera push-in (`scale: 1.0 -> 1.06`).
2. **Scene 2 - Problem Elimination / Value Triad (2.5s - 5.0s)**: Three stacked typographic lines where inactive lines sit at `opacity: 0.22` and `filter: blur(2px)` while an animated directional arrow (`->`) snaps vertically to highlight the active line in full contrast and brand accent color.
3. **Scene 3 - Hero Asset / Brand Icon Reveal (5.0s - 6.5s)**: Split-screen or card collapse transition into the hero visual or glowing badge icon with radial light bloom and floating micro-particles.
4. **Scene 4 - Interactive SaaS UI Simulation (6.5s - 12.0s)**: Dark/light glassmorphic application window (`backdrop-filter: blur(24px)`) showing real-time prompt typing, step-by-step green checkmark completion badges, and a live timeline scrubber with multi-track colored clips.
5. **Scene 5 - Multi-Format Bento Grid Showcase (12.0s - 15.5s)**: Staggered 2-row bento grid demonstrating modular capabilities (Logo Reveals, Lower Thirds, Kinetic Type, Charts and Data, Product Shots, Social Media Cards, Smooth Transitions) with 3D floating spheres in the background.
6. **Scene 6 - 3D Carousel and Product Action Card (15.5s - 19.0s)**: Three-card perspective showcase (`rotateY` + depth blur on side cards) featuring a crisp center product card with spring-animated price counter and interactive CTA pill button.
7. **Scene 7 - Timeline Frame-Scrubbing Proof (19.0s - 22.5s)**: Fast-rewind horizontal filmstrip (`<<`) with a glowing center viewfinder frame and dynamic frame counter (`FRAME 0587 -> FRAME 0156`) proving every frame is code-generated.
8. **Scene 8 - Offer Badge and Creator CTA Outro (22.5s - 27.0s)**: Hero file/product icon with spring-popping price pill, two verification checkmarks, creator avatar with handle, and pulsing primary CTA button.

### Step 3: Enforce Physics-First Motion Rules (Zero Linear Motion)

Robotic motion is the number one sign of amateur AI video generation. Follow these strict animation rules on every property (consult `references/spring-physics-and-easing.md` for full code presets):

- **Ban Linear Easing**: Never use linear interpolation (`easing: Easing.linear` or CSS `linear`) for position, scale, or rotation. Linear easing is only permitted for continuous time-progress bars or constant filmstrip scrolling.
- **Use Tuned Spring Physics**: Drive all UI entrances, text reveals, and card transitions with Remotion `spring()` using purposeful physical parameters:
  - **Snappy UI & Text Reveal**: `{ mass: 0.8, damping: 16, stiffness: 180 }`
  - **Smooth Hero Card Entrance**: `{ mass: 1.1, damping: 22, stiffness: 130 }`
  - **Elastic Badge / Price Pill Pop**: `{ mass: 0.6, damping: 11, stiffness: 220 }`
  - **Camera Pan / Zoom Drift**: `{ mass: 2.0, damping: 35, stiffness: 80 }`
- **Clamp Every Interpolation**: Always pass `{ extrapolateLeft: "clamp", extrapolateRight: "clamp" }` to every `interpolate()` call so values never overshoot into negative opacity or broken coordinates outside their active frame window.
- **Layer Secondary Motion**: Combine at least 3 properties on every entrance (`translateY`, `scale`, `opacity`, and subtle `blur` clearing from `8px` to `0px` over 12 frames).
- **Stagger Sibling Elements**: Offset sibling words, checklist rows, or bento cards by `4` to `7` frames (`delay = index * 5`) so elements cascade naturally instead of appearing all at once.

### Step 4: Apply the Glassmorphic SaaS Design System

Build every scene with studio-level visual depth (consult `references/glass-ui-and-design-system.md` and `references/scene-templates.md`):

- **Atmospheric Canvas**: Never use flat `#FFFFFF` or `#000000` backgrounds. Use multi-stop radial mesh gradients (`radial-gradient(circle at 20% 20%, #EEF2FF 0%, #E0E7FF 45%, #F8FAFC 100%)` for light scenes, or `#070913` to `#0F172A` with subtle star/grid noise for dark scenes).
- **3D Parallax Spheres**: Place 4 to 6 floating 3D spheres (`radial-gradient(circle at 30% 30%, #93C5FD, #3B82F6 60%, #1D4ED8 100%)` with soft drop shadows) drifting on sine-wave trajectories (`Math.sin(frame / 25) * 14`) across foreground and background depth layers.
- **Frosted Glass Cards**: Style containers with semi-transparent fills (`rgba(255, 255, 255, 0.72)` in light mode, `rgba(15, 23, 42, 0.78)` in dark mode), `backdropFilter: "blur(20px)"`, a `1px solid rgba(255, 255, 255, 0.6)` specular border, and layered ambient shadows (`0 24px 48px -12px rgba(30, 58, 138, 0.14)`).
- **Typographic Hierarchy**: Use geometric grotesque fonts (`Inter`, `Plus Jakarta Sans`, or `SF Pro Display`) for headings with tight tracking (`letterSpacing: "-0.03em"`, `fontWeight: 800`, `lineHeight: 1.08`) and `JetBrains Mono` for code, terminal prompts, and frame counters.

### Step 5: Render and Run the Zero-Defect QA Validator

Before delivering the final video to the user, render the output and run the automated quality gate:

1. Render the composition to MP4 using H.264 (`-crf 18 -pix_fmt yuv420p` for crisp color and universal playback).
2. Run the bundled verification script to check both source code and rendered frames:

```bash
python3 scripts/validate_video_quality.py --source src/ --video output.mp4
```

3. Fix any reported violations (unclamped interpolations, text overflow outside safe zones, blank/black frames, or sub-1080p resolution) and re-render before handing off the final video.

## Gotchas

- **Unclamped `interpolate()` explosions**: Forgetting `extrapolateRight: "clamp"` causes elements to fly off-screen or opacity to exceed `1.0` after the transition ends. Always wrap or lint every `interpolate()` call.
- **Hard cuts without transition overlap**: Cutting abruptly between dark and light scenes feels jarring. Overlap adjacent `Sequence` blocks by 10 to 15 frames and cross-dissolve with a scale-through (`scale: 0.94 -> 1.0`) or whip-blur transition.
- **Text clipping and wrapping glitches**: Animating font size or container width causes text to reflow mid-animation. Lock container dimensions (`whiteSpace: "nowrap"` on kinetic headlines) and animate `transform: translateY() scale()` instead of layout properties (`width`, `height`, `top`, `left`).
- **Missing font readiness**: Rendering before web fonts finish loading causes a flash of unstyled fallback text on frame 0. Load fonts synchronously via `@remotion/google-fonts` or local `@font-face` with `continueRender()` / `delayRender()`.
