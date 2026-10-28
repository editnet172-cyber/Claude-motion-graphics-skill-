# Glass UI and SaaS Design System Reference

This reference defines the color palettes, frosted glassmorphism surfaces, 3D spheres, and safe-zone grids used in high-converting SaaS commercials.

## 1. Signature SaaS Color Palettes

### Light Atmospheric Studio (Apple / Clean SaaS Style)
- **Canvas Background**: `radial-gradient(120% 120% at 50% 15%, #F8FAFF 0%, #E8EEFF 52%, #DCE6FF 100%)`
- **Glass Card Fill**: `rgba(255, 255, 255, 0.76)`
- **Glass Card Border**: `1.5px solid rgba(255, 255, 255, 0.88)`
- **Card Ambient Shadow**: `0 24px 60px -12px rgba(37, 99, 235, 0.16), 0 4px 16px -2px rgba(15, 23, 42, 0.06)`
- **Primary Ink**: `#0F172A`
- **Muted Ink**: `#64748B`
- **Electric Accent Blue**: `#2563EB` (`linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%)`)

### Dark Pro Editor / Terminal Window (Claude Code / Linear Style)
- **Window Surface**: `linear-gradient(180deg, #111625 0%, #0B0F19 100%)`
- **Window Border**: `1.5px solid rgba(148, 163, 184, 0.22)`
- **Inner Panel Fill**: `rgba(15, 23, 42, 0.85)`
- **Success Checkmark Green**: `#22C55E`
- **Timeline Track Accents**:
  - Track 1 (Blue): `#3B82F6`
  - Track 2 (Purple): `#A855F7`
  - Track 3 (Emerald): `#10B981`
  - Playhead Scrubber: `#F43F5E`

## 2. Frosted Glass Card Component CSS

```tsx
export const glassCardStyle: React.CSSProperties = {
  background: 'rgba(255, 255, 255, 0.76)',
  backdropFilter: 'blur(24px) saturate(180%)',
  WebkitBackdropFilter: 'blur(24px) saturate(180%)',
  borderRadius: 28,
  border: '1.5px solid rgba(255, 255, 255, 0.88)',
  boxShadow:
    '0 28px 64px -12px rgba(30, 64, 175, 0.18), inset 0 1px 0 0 rgba(255, 255, 255, 0.9)',
};
```

## 3. 3D Floating Sphere CSS

```tsx
export const createOrbStyle = (size: number): React.CSSProperties => ({
  width: size,
  height: size,
  borderRadius: '50%',
  background:
    'radial-gradient(circle at 32% 28%, #BFDBFE 0%, #60A5FA 38%, #2563EB 78%, #1E3A8A 100%)',
  boxShadow:
    '0 18px 36px -8px rgba(37, 99, 235, 0.38), inset -6px -8px 16px rgba(30, 58, 138, 0.45), inset 6px 6px 14px rgba(255, 255, 255, 0.65)',
});
```

## 4. Multi-Format Aspect Ratio Safe Zones

Always wrap foreground text and UI cards inside a safe-zone container so nothing gets cropped by video players or social media UI overlays:

| Format | Dimensions | Horizontal Safe Padding | Top/Bottom Safe Padding | Max Headline Width |
| :--- | :--- | :--- | :--- | :--- |
| **16:9 Landscape** | `1920 x 1080` | `96px` | `72px` | `1560px` |
| **9:16 Vertical Reel** | `1080 x 1920` | `72px` | `180px` | `920px` |
| **1:1 Square Feed** | `1080 x 1080` | `80px` | `80px` | `920px` |
