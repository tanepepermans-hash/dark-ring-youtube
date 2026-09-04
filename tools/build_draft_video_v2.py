#!/usr/bin/env python3
"""Draft v2: flat-icon "motion graphics" style, closer to what the user pictured
as "cartoon/animation" while staying free/local (no paid AI video tool).

Icons are generic silhouettes/symbols (boxer stance, house, evidence bag,
question mark, ring logo) -- not depictions of a specific real person, which
also keeps portrait-right risk low. Real character animation (faces, motion)
needs a paid AI video tool (Runway/Pika/Kling) or an animation subscription
(e.g. Vyond) -- not wired up here, see notes to the user.

Usage: python3 tools/build_draft_video_v2.py <id>
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1080, 1920
FPS = 24
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

BG_TOP = (16, 15, 18)
BG_BOTTOM = (28, 22, 24)
ACCENT = (168, 38, 42)
TEXT = (238, 236, 233)
ICON = (210, 205, 198)

SCENES = {
    "DR-0001": [
        {"icon": "boxer", "text": "THE MOST FEARED MAN IN BOXING", "dur": 3.4},
        {"icon": "house", "text": "FOUND DEAD IN HIS HOME, 1971", "dur": 3.4},
        {"icon": "bag", "text": "HEROIN. NO SYRINGE.", "dur": 2.6},
        {"icon": "question", "text": "RULED NATURAL CAUSES.\nALMOST NO ONE BELIEVED IT.", "dur": 3.0},
        {"icon": "ring", "text": "STILL, OFFICIALLY, UNSOLVED", "dur": 1.9},
    ],
}


def ease_out_back(t, overshoot=1.6):
    t = max(0.0, min(1.0, t))
    c = overshoot
    t -= 1
    return 1 + (c + 1) * (t ** 3) + c * (t ** 2)


def gradient_bg():
    img = Image.new("RGB", (W, H), BG_TOP)
    px = img.load()
    for y in range(H):
        t = y / H
        row = tuple(int(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3))
        for x in range(W):
            px[x, y] = row
    return img


def draw_icon(draw, name, cx, cy, scale, color):
    s = scale
    if name == "boxer":
        # head
        draw.ellipse([cx - 40 * s, cy - 220 * s, cx + 40 * s, cy - 140 * s], fill=color)
        # torso
        draw.polygon([
            (cx - 70 * s, cy - 140 * s), (cx + 70 * s, cy - 140 * s),
            (cx + 55 * s, cy + 80 * s), (cx - 55 * s, cy + 80 * s),
        ], fill=color)
        # raised arms (fighting stance)
        draw.polygon([(cx - 70 * s, cy - 120 * s), (cx - 150 * s, cy - 200 * s),
                       (cx - 120 * s, cy - 220 * s), (cx - 50 * s, cy - 90 * s)], fill=color)
        draw.polygon([(cx + 70 * s, cy - 120 * s), (cx + 150 * s, cy - 200 * s),
                       (cx + 120 * s, cy - 220 * s), (cx + 50 * s, cy - 90 * s)], fill=color)
        draw.ellipse([cx - 175 * s, cy - 235 * s, cx - 105 * s, cy - 165 * s], fill=ACCENT)
        draw.ellipse([cx + 105 * s, cy - 235 * s, cx + 175 * s, cy - 165 * s], fill=ACCENT)
        # legs
        draw.polygon([(cx - 55 * s, cy + 80 * s), (cx - 15 * s, cy + 80 * s),
                       (cx - 25 * s, cy + 220 * s), (cx - 65 * s, cy + 220 * s)], fill=color)
        draw.polygon([(cx + 55 * s, cy + 80 * s), (cx + 15 * s, cy + 80 * s),
                       (cx + 25 * s, cy + 220 * s), (cx + 65 * s, cy + 220 * s)], fill=color)
    elif name == "house":
        draw.polygon([(cx, cy - 180 * s), (cx - 180 * s, cy - 20 * s), (cx + 180 * s, cy - 20 * s)], fill=color)
        draw.rectangle([cx - 130 * s, cy - 30 * s, cx + 130 * s, cy + 200 * s], fill=color)
        draw.rectangle([cx - 30 * s, cy + 80 * s, cx + 30 * s, cy + 200 * s], fill=BG_TOP)
    elif name == "bag":
        draw.rounded_rectangle([cx - 90 * s, cy - 60 * s, cx + 90 * s, cy + 140 * s], radius=24 * s, fill=color)
        draw.line([cx - 40 * s, cy - 60 * s, cx - 10 * s, cy - 120 * s], fill=color, width=int(14 * s))
        draw.line([cx + 40 * s, cy - 60 * s, cx + 10 * s, cy - 120 * s], fill=color, width=int(14 * s))
        draw.ellipse([cx - 12 * s, cy - 135 * s, cx + 12 * s, cy - 111 * s], fill=color)
    elif name == "question":
        font = ImageFont.truetype(FONT_BOLD, max(1, int(320 * s)))
        bbox = draw.textbbox((0, 0), "?", font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text((cx - w / 2, cy - h / 2 - bbox[1]), "?", font=font, fill=color)
    elif name == "ring":
        draw.ellipse([cx - 150 * s, cy - 150 * s, cx + 150 * s, cy + 150 * s], outline=color, width=int(16 * s))
        draw.ellipse([cx - 90 * s, cy - 90 * s, cx + 90 * s, cy + 90 * s], outline=ACCENT, width=int(10 * s))


def wrap_lines(text):
    return text.split("\n")


def render_frame(bg, scene, local_t, scene_dur):
    img = bg.copy()
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 6], fill=ACCENT)
    draw.rectangle([0, H - 6, W, H], fill=ACCENT)

    pop_dur = 0.5
    icon_t = min(1.0, local_t / pop_dur)
    scale = ease_out_back(icon_t) * 0.9
    scale = max(0.0, scale)
    draw_icon(draw, scene["icon"], W / 2, H * 0.42, scale, ICON)

    text_t = min(1.0, max(0.0, (local_t - pop_dur * 0.6) / 0.4))
    if text_t > 0:
        font = ImageFont.truetype(FONT_BOLD, 66)
        lines = wrap_lines(scene["text"])
        y = H * 0.66
        alpha = int(255 * text_t)
        overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        odraw = ImageDraw.Draw(overlay)
        for line in lines:
            bbox = odraw.textbbox((0, 0), line, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
            odraw.text(((W - w) / 2, y), line, font=font, fill=(*TEXT, alpha))
            y += h + 24
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    return img


def main():
    video_id = sys.argv[1] if len(sys.argv) > 1 else "DR-0001"
    scenes = SCENES[video_id]
    work = ROOT / "projects" / video_id / "_draft_v2_frames"
    work.mkdir(parents=True, exist_ok=True)
    bg = gradient_bg()

    frame_idx = 0
    for scene in scenes:
        n_frames = int(scene["dur"] * FPS)
        for f in range(n_frames):
            local_t = f / FPS
            img = render_frame(bg, scene, local_t, scene["dur"])
            img.save(work / f"f_{frame_idx:05d}.png")
            frame_idx += 1

    silent = work / "silent.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-framerate", str(FPS), "-i", str(work / "f_%05d.png"),
        "-pix_fmt", "yuv420p", str(silent),
    ], check=True, capture_output=True)

    audio = ROOT / "voiceovers" / f"{video_id}_draft_v2.wav"
    out = ROOT / "exports" / f"{video_id}_draft_v2.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-i", str(silent), "-i", str(audio),
        "-c:v", "libx264", "-c:a", "aac", "-shortest", str(out),
    ], check=True, capture_output=True)

    print(f"Draft v2 written to {out}")


if __name__ == "__main__":
    main()
