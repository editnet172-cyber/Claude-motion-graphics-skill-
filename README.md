<div align="center">

# ⚡ `SKILL.md` — Studio-Grade Motion Graphics Ad Engine for Claude Code

### **No Editor. No Studio. Just One File.**
Turn a single prompt in **Claude Code** into a 1080p / 60fps **Apple, Linear & Stripe-style SaaS commercial, product promo, or viral social reel** with zero visual defects.

[![Claude Code Ready](https://img.shields.io/badge/Claude_Code-SKILL.md_Verified-2563EB?style=for-the-badge&logo=anthropic&logoColor=white)](#quick-start-drop-in--go)
[![Remotion 4.x](https://img.shields.io/badge/Engine-Remotion_60FPS-7C3AED?style=for-the-badge)](#everything-you-can-generate-from-one-prompt)
[![Zero Defect QA](https://img.shields.io/badge/QA_Gate-Zero_Mistakes_Verified-10B981?style=for-the-badge)](#automated-zero-defect-quality-gate)
[![Multi Format](https://img.shields.io/badge/Formats-16%3A9_%7C_9%3A16_%7C_1%3A1-0F172A?style=for-the-badge)](#repository-architecture)

<br />

<!-- HERO BANNER: Shows immediately when opening the GitHub repository -->
<img src="assets/hero-banner.jpg" alt="SKILL.md Motion Graphics Engine Hero Banner" width="100%" style="border-radius: 16px;" />

<br /><br />

## 🎬 Live Output Showcase (100% Generated from `SKILL.md`)

> **Every single frame below came from one prompt + `SKILL.md`.**
> 👇 *Auto-playing preview below — [Click here to watch/download the full 1080p MP4 with audio (`assets/showcase-demo.mp4`)](assets/showcase-demo.mp4)*

<a href="assets/showcase-demo.mp4">
  <img src="assets/showcase-preview.gif" alt="Watch Full Motion Graphics Ad Output" width="100%" style="border-radius: 16px;" />
</a>

<br />

### 🖼️ Frame-by-Frame Studio Output Breakdown

<img src="assets/storyboard-strip.jpg" alt="4-Panel Frame Breakdown from Showcase Video" width="100%" style="border-radius: 12px;" />

</div>

---

## ✨ Why Standard AI Video Code Fails vs. What `SKILL.md` Fixes

When you ask standard AI models to code a motion graphics video without `SKILL.md`, you get **robotic linear movement, broken text wrapping, overlapping divs, black gap frames, and flat 1990s colors**.

`SKILL.md` upgrades Claude Code into a **Senior Motion Director** with strict physics, optical layout rules, and an automated Python verification gate:

| Common AI Video Mistake | How `SKILL.md` Eliminates It Permanently |
| :--- | :--- |
| **Robotic linear movement (`ease-linear`)** | Enforces tuned **Remotion Spring Physics** (`mass`, `damping`, `stiffness`) for snappy UI cards, elastic badges, and smooth camera push-ins. |
| **Elements flying off-screen or negative opacity** | Enforces mandatory `{ extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }` on every `interpolate()` call. |
| **Text clipping & ugly mid-animation line wraps** | Locks typographic bounding boxes (`whiteSpace: 'nowrap'`) and animates GPU `transform` + `filter: blur()` instead of layout width/top. |
| **Flat, amateur backgrounds & harsh borders** | Applies the **Glassmorphic SaaS Design System**: radial mesh gradients, `backdrop-filter: blur(24px)` frosted cards, specular borders, and 3D floating parallax orbs. |
| **Social media UI covering captions on Reels/TikTok** | Enforces strict aspect-ratio safe zones (`1920x1080`, `1080x1920`, `1080x1080`) so text is never cropped. |
| **Blank frames or broken render exports** | Runs `scripts/validate_video_quality.py` (OpenCV + static AST checks) to verify 0 black frames and 1080p/60fps integrity before completing. |

---

## 🎯 Everything You Can Generate From One Prompt

- **SaaS Launch Commercials** — Split-screen terminal simulations, animated prompt checklists, and live multi-track timeline scrubbers.
- **Kinetic Typography Reels & Shorts** — Staggered word-by-word blur-to-sharp reveals and focus-shifting directional arrow triads (`-> Just one file.`).
- **E-Commerce Product Cards** — 3D perspective carousels, frosted glass product shots, spring-popping price tags (`$9` / `$199`), and interactive `Add to cart` CTAs.
- **Bento Grid Feature Showcases** — Modular 8-card bento grids covering Logo Reveals, Lower Thirds, Kinetic Type, Charts & Data, Product Shots, Social Media Cards, and Transitions.
- **Creator & Brand Outros** — Avatar badges, `@handle` pills, feature checkmarks, and pulsing call-to-action buttons.

---

## 🚀 Quick Start (Drop In & Go)

### Option 1: Drop directly into your project root
Copy [`SKILL.md`](SKILL.md) (along with [`references/`](references/) and [`scripts/`](scripts/)) into your workspace root or `.claude/skills/motion-graphics-ad-studio/`:

```bash
git clone https://github.com/your-username/claude-motion-graphics-skill.git
cd claude-motion-graphics-skill
```

### Option 2: Run one prompt in Claude Code
Open Claude Code in the repository and type:

```text
Make a motion ad using SKILL.md for my SaaS product.
```

Claude Code will automatically:
1. ✅ **Read `SKILL.md`** and load the spring physics & glass UI design tokens
2. ✅ **Plan 8 high-retention scenes** tailored to your brand and aspect ratio
3. ✅ **Animate kinetic type + frosted glass UI + 3D parallax spheres**
4. ✅ **Render a crisp 1080p / 60fps `output.mp4` video** and verify it with `validate_video_quality.py`

---

## 📂 Repository Architecture

```text
claude-motion-graphics-skill/
├── README.md                                  # Showcase storefront (auto-displays Banner + Video Preview)
├── SKILL.md                                   # Core Motion Graphics Ad Studio instruction file
├── PROMPTS.md                                 # Copy-paste commercial prompt pack (SaaS, Reels, E-commerce)
├── assets/
│   ├── hero-banner.jpg                        # Hero artwork displayed on repo open
│   ├── showcase-preview.gif                   # Auto-playing showcase animation for GitHub README
│   ├── showcase-demo.mp4                      # Full 1080p showcase commercial with audio
│   └── storyboard-strip.jpg                   # 4-panel studio frame breakdown
├── references/
│   ├── spring-physics-and-easing.md           # Tuned spring presets, stagger formulas & 3D orb math
│   ├── glass-ui-and-design-system.md          # Frosted glass CSS, radial mesh palettes & safe zones
│   └── scene-templates.md                     # Production TypeScript/Remotion scene components
├── scripts/
│   └── validate_video_quality.py              # Automated code & OpenCV frame quality gate
├── templates/
│   └── remotion-saas-starter/                 # Ready-to-render Remotion 4.x boilerplate (16:9, 9:16, 1:1)
└── .claude/
    └── skills/
        └── motion-graphics-ad-studio/         # Pre-configured Claude Code skill directory
```

---

## 🛡️ Automated Zero-Defect Quality Gate

Every video rendered with this skill is verified by [`scripts/validate_video_quality.py`](scripts/validate_video_quality.py):

```bash
python3 scripts/validate_video_quality.py --source templates/remotion-saas-starter/src --video assets/showcase-demo.mp4
# Output: QA VALIDATION PASSED: Zero defects detected.
```

It checks:
- **Zero Unclamped Interpolations**: Scans all `.tsx`/`.ts` files to guarantee `extrapolateLeft: "clamp"` and `extrapolateRight: "clamp"`.
- **Zero Linear UI Transforms**: Flags robotic `Easing.linear` calls on UI entrances.
- **1080p+ & Frame Rate Integrity**: Verifies output resolution and frame rate via OpenCV.
- **Blank/Corrupt Frame Detection**: Samples frames across the timeline to ensure zero black gaps between scene transitions.
