# Spring Physics, Easing Curves, and Choreography Reference

This reference provides deterministic motion formulas for Remotion (`spring`, `interpolate`, `Easing`) and HTML5 Canvas so every animation feels crafted by a senior motion designer.

## 1. Remotion Spring Presets

Import `spring` and `useCurrentFrame`, `useVideoConfig` from `remotion`:

```tsx
import { spring, interpolate, useCurrentFrame, useVideoConfig, Easing } from 'remotion';

export const SPRING_PRESETS = {
  // Crisp UI cards, terminal windows, and kinetic text entrances
  snappyUI: { mass: 0.8, damping: 16, stiffness: 180 },
  // Smooth hero cards, bento grid tiles, and split-screen panels
  smoothHero: { mass: 1.1, damping: 22, stiffness: 130 },
  // Playful price tags ($9 pill), notification badges, and checkmarks
  elasticPop: { mass: 0.6, damping: 11, stiffness: 220 },
  // Heavy cinematic camera push-in, pan, and 3D carousel rotation
  cinematicCamera: { mass: 2.0, damping: 35, stiffness: 80 },
  // Whip-pan or fast scene exit transition
  whipTransition: { mass: 0.5, damping: 14, stiffness: 260 },
} as const;
```

## 2. Safe Clamped Interpolation Helper

Never call raw `interpolate` without clamping unless intentionally looping. Use this helper:

```tsx
export const clampedInterpolate = (
  frame: number,
  inputRange: readonly number[],
  outputRange: readonly number[],
  easing?: (t: number) => number
) => {
  return interpolate(frame, inputRange, outputRange, {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing,
  });
};
```

## 3. Staggered Word-by-Word Kinetic Text Formula

To animate a headline word by word with vertical lift, scale, opacity, and de-blurring:

```tsx
export const getWordAnimationStyle = (
  frame: number,
  fps: number,
  wordIndex: number,
  startFrame = 0,
  staggerFrames = 4
) => {
  const localFrame = frame - (startFrame + wordIndex * staggerFrames);
  const progress = spring({
    frame: localFrame,
    fps,
    config: SPRING_PRESETS.snappyUI,
  });

  const translateY = interpolate(progress, [0, 1], [28, 0]);
  const scale = interpolate(progress, [0, 1], [0.92, 1]);
  const opacity = clampedInterpolate(localFrame, [0, 8], [0, 1]);
  const blur = clampedInterpolate(localFrame, [0, 10], [8, 0]);

  return {
    display: 'inline-block',
    opacity,
    filter: `blur(${blur.toFixed(2)}px)`,
    transform: `translateY(${translateY.toFixed(2)}px) scale(${scale.toFixed(4)})`,
    willChange: 'transform, opacity, filter',
  };
};
```

## 4. Floating 3D Orb Sine-Wave Trajectory

Give background spheres organic zero-gravity drift using out-of-phase sine and cosine waves:

```tsx
export const getFloatingOrbTransform = (
  frame: number,
  seedIndex: number,
  amplitudeX = 16,
  amplitudeY = 22,
  speed = 0.04
) => {
  const phase = seedIndex * 1.7;
  const dx = Math.sin(frame * speed + phase) * amplitudeX;
  const dy = Math.cos(frame * (speed * 0.85) + phase) * amplitudeY;
  const rot = Math.sin(frame * (speed * 0.5) + phase) * 6;
  return `translate3d(${dx.toFixed(2)}px, ${dy.toFixed(2)}px, 0) rotate(${rot.toFixed(2)}deg)`;
};
```
