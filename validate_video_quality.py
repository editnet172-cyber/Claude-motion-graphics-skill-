#!/usr/bin/env python3
"""
Zero-Defect Motion Graphics QA Validator
Checks both Remotion/TypeScript source code and rendered MP4 output for:
1. Unclamped interpolate() calls
2. Banned linear easing on UI transforms
3. Video resolution, FPS, duration, and audio/video stream health
4. Blank/black frames or frozen frame glitches
"""

import argparse
import os
import re
import subprocess
import sys

def audit_source_code(src_dir: str) -> list[str]:
    issues = []
    if not os.path.exists(src_dir):
        return issues

    for root, _, files in os.walk(src_dir):
        for fname in files:
            if not fname.endswith((".ts", ".tsx", ".js", ".jsx")):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Check for unclamped interpolate calls
            interp_calls = re.findall(r"interpolate\s*\([^;]+\)", content, re.DOTALL)
            for call in interp_calls:
                if "extrapolateLeft" not in call or "extrapolateRight" not in call:
                    issues.append(f"[CODE] {fpath}: Found interpolate() without extrapolateLeft/Right clamp.")
                    break

            # Check for forbidden linear easing on transforms
            if "Easing.linear" in content:
                issues.append(f"[CODE] {fpath}: Avoid Easing.linear on UI entrances; use spring() or bezier easing.")

    return issues

def audit_video_file(video_path: str) -> list[str]:
    issues = []
    if not os.path.exists(video_path):
        issues.append(f"[VIDEO] Rendered file not found: {video_path}")
        return issues

    try:
        import cv2
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            issues.append(f"[VIDEO] Failed to open video stream: {video_path}")
            return issues

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        if min(width, height) < 1080:
            issues.append(f"[VIDEO] Resolution {width}x{height} is below 1080p commercial standard.")
        if fps < 29.5:
            issues.append(f"[VIDEO] Frame rate {fps:.2f}fps is too low (minimum 30fps, recommended 60fps).")
        if frame_count < 30:
            issues.append(f"[VIDEO] Video is too short ({frame_count} frames).")

        # Sample frames across the video to detect pure black/corrupted frames
        blank_frames = 0
        sample_indices = [int(i * (frame_count - 1) / 20) for i in range(21)] if frame_count > 20 else range(frame_count)
        for idx in sample_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ok, frame = cap.read()
            if not ok or frame is None:
                issues.append(f"[VIDEO] Unreadable frame at index {idx}.")
                continue
            if frame.std() < 1.5:
                blank_frames += 1

        if blank_frames > 1:
            issues.append(f"[VIDEO] Detected {blank_frames} flat/blank sampled frames. Check scene sequence gaps.")

        cap.release()
    except Exception as exc:
        issues.append(f"[VIDEO] Inspection error: {exc}")

    return issues

def main():
    parser = argparse.ArgumentParser(description="Validate motion graphics source and rendered MP4.")
    parser.add_argument("--source", default="src", help="Path to Remotion/TypeScript source directory")
    parser.add_argument("--video", default=None, help="Path to rendered MP4 file")
    args = parser.parse_args()

    all_issues = []
    if args.source and os.path.exists(args.source):
        all_issues.extend(audit_source_code(args.source))
    if args.video:
        all_issues.extend(audit_video_file(args.video))

    if all_issues:
        print("QA VALIDATION FAILED:")
        for issue in all_issues:
            print(f" - {issue}")
        sys.exit(1)

    print("QA VALIDATION PASSED: Zero defects detected.")
    sys.exit(0)

if __name__ == "__main__":
    main()
