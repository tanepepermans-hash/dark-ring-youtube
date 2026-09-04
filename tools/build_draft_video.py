#!/usr/bin/env python3
"""Build a rough, text/graphics-only draft Short from a script + narration audio.

This is a placeholder-quality proof of concept, NOT the final published video:
- Visuals here are self-generated minimalist graphic cards (no stock footage,
  no third-party images) -- zero copyright risk, but not "real" documentary
  b-roll. Swap in licensed stock per templates/... shotlist before publishing.
- Narration uses a free local model (Piper), not the channel's chosen
  ElevenLabs voice -- swap before publishing.

Usage: python3 tools/build_draft_video.py <id>
Reads voiceovers/<id>_draft.wav and a hardcoded card list per id, writes
exports/<id>_draft.mp4.
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1080, 1920
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

BG_TOP = (14, 14, 16)
BG_BOTTOM = (26, 24, 26)
ACCENT = (150, 30, 34)
TEXT = (235, 233, 230)
SUBTEXT = (150, 148, 145)

CARDS = {
    "DR-0001": [
        {"kicker": None, "lines": ["THE MOST FEARED", "HEAVYWEIGHT", "OF HIS ERA"], "dur": 3.4},
        {"kicker": "THE DARK RING", "lines": ["SONNY LISTON"], "sub": "Former World Heavyweight Champion", "dur": 4.5},
        {"kicker": None, "lines": ["JANUARY 5, 1971"], "sub": "Las Vegas, Nevada", "dur": 4.5},
        {"kicker": None, "lines": ["FOUND DEAD", "IN HIS BEDROOM"], "dur": 4.5},
        {"kicker": None, "lines": ["DEAD FOR", "NEARLY A WEEK"], "dur": 4.5},
        {"kicker": "AT THE SCENE", "lines": ["HEROIN.", "MARIJUANA."], "sub": "No syringe was found.", "dur": 4.5},
        {"kicker": "OFFICIAL RULING", "lines": ["HEART FAILURE"], "sub": "Not ruled an overdose.", "dur": 4.5},
        {"kicker": None, "lines": ["HE HAD A KNOWN", "FEAR OF NEEDLES"], "dur": 6.7},
        {"kicker": None, "lines": ["NEVER INVESTIGATED", "AS A MURDER"], "dur": 4.5},
        {"kicker": None, "lines": ["HIS WIFE.", "HIS MANAGER.", "HIS FRIENDS."], "sub": "None accepted the official story.", "dur": 4.5},
        {"kicker": None, "lines": ["STILL, OFFICIALLY,", "UNSOLVED"], "dur": 3.4},
        {"kicker": None, "lines": ["THE DARK RING"], "sub": "Real stories. Verified sources.", "dur": 2.2},
    ],
}


def make_gradient():
    img = Image.new("RGB", (W, H), BG_TOP)
    px = img.load()
    for y in range(H):
        t = y / H
        r = int(BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * t)
        g = int(BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * t)
        b = int(BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * t)
        for x in range(0, W, 4):
            for dx in range(4):
                if x + dx < W:
                    px[x + dx, y] = (r, g, b)
    return img


def wrap_center(draw, lines, font, y, fill, spacing=18):
    total_h = 0
    sizes = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        h = bbox[3] - bbox[1]
        sizes.append(h)
        total_h += h + spacing
    total_h -= spacing
    cy = y
    for line, h in zip(lines, sizes):
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        draw.text(((W - w) / 2, cy), line, font=font, fill=fill)
        cy += h + spacing
    return cy


def render_card(card, out_path):
    img = make_gradient()
    draw = ImageDraw.Draw(img)

    # subtle top/bottom accent rules
    draw.rectangle([0, 0, W, 6], fill=ACCENT)

    font_kicker = ImageFont.truetype(FONT_BOLD, 34)
    font_main = ImageFont.truetype(FONT_BOLD, 78)
    font_sub = ImageFont.truetype(FONT_REG, 36)

    cy = H * 0.38
    if card.get("kicker"):
        bbox = draw.textbbox((0, 0), card["kicker"], font=font_kicker)
        w = bbox[2] - bbox[0]
        draw.text(((W - w) / 2, cy), card["kicker"], font=font_kicker, fill=ACCENT)
        cy += (bbox[3] - bbox[1]) + 40

    cy = wrap_center(draw, card["lines"], font_main, cy, TEXT)

    if card.get("sub"):
        cy += 30
        bbox = draw.textbbox((0, 0), card["sub"], font=font_sub)
        w = bbox[2] - bbox[0]
        draw.text(((W - w) / 2, cy), card["sub"], font=font_sub, fill=SUBTEXT)

    draw.rectangle([0, H - 6, W, H], fill=ACCENT)
    img.save(out_path)


def main():
    video_id = sys.argv[1] if len(sys.argv) > 1 else "DR-0001"
    cards = CARDS[video_id]
    work = ROOT / "projects" / video_id / "_draft_frames"
    work.mkdir(parents=True, exist_ok=True)

    clips = []
    for i, card in enumerate(cards):
        png = work / f"card_{i:02d}.png"
        render_card(card, png)
        clip = work / f"clip_{i:02d}.mp4"
        dur = card["dur"]
        # slow subtle zoom (Ken Burns), 30fps
        subprocess.run([
            "ffmpeg", "-y", "-loop", "1", "-i", str(png),
            "-vf",
            f"scale=1600:-1,zoompan=z='min(zoom+0.0006,1.08)':d={int(dur*30)}:s={W}x{H}:fps=30",
            "-t", str(dur), "-pix_fmt", "yuv420p", str(clip),
        ], check=True, capture_output=True)
        clips.append(clip)

    concat_list = work / "concat.txt"
    concat_list.write_text("".join(f"file '{c.resolve()}'\n" for c in clips))

    silent_video = work / "silent.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
        "-c", "copy", str(silent_video),
    ], check=True, capture_output=True)

    audio = ROOT / "voiceovers" / f"{video_id}_draft.wav"
    out = ROOT / "exports" / f"{video_id}_draft.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "ffmpeg", "-y", "-i", str(silent_video), "-i", str(audio),
        "-c:v", "libx264", "-c:a", "aac", "-shortest", str(out),
    ], check=True, capture_output=True)

    print(f"Draft written to {out}")


if __name__ == "__main__":
    main()
