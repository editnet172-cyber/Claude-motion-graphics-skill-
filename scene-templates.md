# Commercial Ad Scene Templates (Remotion + TypeScript)

Use these modular scene patterns to assemble complete SaaS commercials, product promos, and social media reels.

## Scene Pattern A: Focus-Shift Value Triad ("No editor. No studio. Just one file.")

Highlights 3 sequential statements by shifting an animated arrow (`->`) and dynamically de-blurring the active line:

```tsx
import React from 'react';
import { AbsoluteFill, spring, interpolate, useCurrentFrame, useVideoConfig } from 'remotion';

const LINES = ['No editor.', 'No studio.', 'Just one file.'];

export const FocusShiftTriadScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Active index switches every 28 frames
  const activeIndex = frame < 28 ? 0 : frame < 56 ? 1 : 2;

  const arrowY = spring({
    frame: frame % 28,
    fps,
    from: ( Math.max(0, activeIndex - 1) ) * 86,
    to: activeIndex * 86,
    config: { mass: 0.7, damping: 15, stiffness: 190 },
  });

  return (
    <AbsoluteFill
      style={{
        background: 'radial-gradient(circle at 50% 30%, #F8FAFC 0%, #E2E8F0 100%)',
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: 'Inter, sans-serif',
      }}
    >
      <div style={{ position: 'relative', paddingLeft: 76 }}>
        <div
          style={{
            position: 'absolute',
            left: 0,
            top: 0,
            transform: `translateY(${arrowY}px)`,
            color: '#2563EB',
            fontSize: 54,
            fontWeight: 700,
          }}
        >
          &rarr;
        </div>
        {LINES.map((text, idx) => {
          const isActive = idx === activeIndex;
          const stepSpring = spring({
            frame: frame - idx * 28,
            fps,
            config: { mass: 0.8, damping: 16, stiffness: 180 },
          });
          const opacity = isActive ? 1 : 0.22;
          const blur = isActive ? 0 : 2.5;
          const color = idx === 2 && isActive ? '#2563EB' : '#0F172A';

          return (
            <div
              key={text}
              style={{
                height: 86,
                display: 'flex',
                alignItems: 'center',
                fontSize: 64,
                fontWeight: 800,
                letterSpacing: '-0.03em',
                color,
                opacity: interpolate(stepSpring, [0, 1], [0, opacity], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                }),
                filter: `blur(${blur}px)`,
              }}
            >
              {text}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
```

## Scene Pattern B: Interactive SaaS Terminal & Live Video Preview Split-View

Shows a left-hand command checklist with staggered green checkmarks and a right-hand video timeline player with a moving red playhead:

```tsx
import React from 'react';
import { AbsoluteFill, spring, interpolate, useCurrentFrame, useVideoConfig } from 'remotion';

const STEPS = [
  'Read SKILL.md',
  'Planned 8 scenes',
  'Animated type + glass UI',
  'Rendered 1080p video',
];

export const SaaSWorkspaceSimulationScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const windowScale = spring({
    frame,
    fps,
    config: { mass: 1.0, damping: 20, stiffness: 140 },
  });

  const playheadProgress = interpolate(frame, [15, 135], [0, 100], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        background: 'radial-gradient(120% 120% at 50% 10%, #EEF2FF 0%, #DBEAFE 100%)',
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: 'Inter, sans-serif',
      }}
    >
      <div
        style={{
          width: 1480,
          height: 780,
          borderRadius: 28,
          background: '#0B0F19',
          border: '2px solid rgba(148, 163, 184, 0.25)',
          boxShadow: '0 40px 90px -20px rgba(15, 23, 42, 0.45)',
          display: 'grid',
          gridTemplateColumns: '520px 1fr',
          overflow: 'hidden',
          transform: `scale(${interpolate(windowScale, [0, 1], [0.9, 1])})`,
        }}
      >
        {/* Left Checklist Column */}
        <div style={{ padding: 40, borderRight: '1px solid rgba(255,255,255,0.08)' }}>
          <div style={{ color: '#F8FAFC', fontSize: 24, fontWeight: 700, marginBottom: 32 }}>
            Claude Code Studio
          </div>
          {STEPS.map((step, i) => {
            const appear = spring({
              frame: frame - (20 + i * 18),
              fps,
              config: { mass: 0.6, damping: 14, stiffness: 200 },
            });
            return (
              <div
                key={step}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 16,
                  marginBottom: 22,
                  opacity: appear,
                  transform: `translateX(${interpolate(appear, [0, 1], [-20, 0])}px)`,
                }}
              >
                <div
                  style={{
                    width: 28,
                    height: 28,
                    borderRadius: '50%',
                    background: '#22C55E',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: '#052E16',
                    fontWeight: 900,
                    fontSize: 16,
                  }}
                >
                  &#10003;
                </div>
                <span style={{ color: '#E2E8F0', fontSize: 22, fontFamily: 'JetBrains Mono, monospace' }}>
                  {step}
                </span>
              </div>
            );
          })}
        </div>

        {/* Right Preview + Multi-Track Timeline */}
        <div style={{ padding: 40, display: 'flex', flexDirection: 'column', gap: 28 }}>
          <div
            style={{
              flex: 1,
              borderRadius: 20,
              background: 'linear-gradient(135deg, #F8FAFC 0%, #E0E7FF 100%)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '0 56px',
            }}
          >
            <div style={{ fontSize: 48, fontWeight: 800, color: '#0F172A', lineHeight: 1.15 }}>
              This entire
              <br />
              video...
              <br />
              is one <span style={{ color: '#2563EB' }}>file.</span>
            </div>
            <div
              style={{
                width: 180,
                height: 220,
                borderRadius: 24,
                background: '#FFFFFF',
                boxShadow: '0 20px 40px rgba(37,99,235,0.18)',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 800,
                fontSize: 26,
                color: '#1E293B',
              }}
            >
              SKILL.md
            </div>
          </div>

          {/* Timeline Tracks */}
          <div style={{ position: 'relative', height: 140, background: '#111827', borderRadius: 16, padding: 20 }}>
            <div
              style={{
                position: 'absolute',
                top: 0,
                bottom: 0,
                left: `${playheadProgress}%`,
                width: 3,
                background: '#F43F5E',
                zIndex: 10,
              }}
            />
            <div style={{ height: 22, width: '78%', background: '#3B82F6', borderRadius: 8, marginBottom: 12 }} />
            <div style={{ height: 22, width: '62%', marginLeft: '18%', background: '#A855F7', borderRadius: 8, marginBottom: 12 }} />
            <div style={{ height: 22, width: '84%', marginLeft: '8%', background: '#10B981', borderRadius: 8 }} />
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
```
