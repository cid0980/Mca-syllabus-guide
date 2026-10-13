"""Generates the PWA icon PNGs from the same geometry as static/logo.svg.

Run: python3 scripts/make-icons.py
"""
from PIL import Image, ImageDraw

BG = (14, 14, 16, 255)          # --bg
ACCENT = (110, 86, 207, 255)    # --accent
CARD = (237, 237, 240, 255)     # --fg
MUTED = (160, 160, 171, 255)    # --fg-muted


def draw_icon(size: int, pad_ratio: float, rounded: bool) -> Image.Image:
    scale = 4  # supersample for clean edges
    S = size * scale
    img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    if rounded:
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=BG)
    else:
        d.rectangle([0, 0, S - 1, S - 1], fill=BG)

    pad = S * pad_ratio
    w = S - 2 * pad
    # card unit: mark is two overlapping cards on a 32-unit grid
    unit = w / 32

    def rect(x, y, rw, rh, r, fill=None, outline=None, width=1):
        d.rounded_rectangle(
            [pad + x * unit, pad + y * unit, pad + (x + rw) * unit, pad + (y + rh) * unit],
            radius=r * unit,
            fill=fill,
            outline=outline,
            width=width,
        )

    # back card (outlined, muted)
    rect(11, 3, 18, 24, 3, fill=None, outline=MUTED, width=max(2, int(unit * 1.6)))
    # front card
    rect(3, 8, 18, 24, 3, fill=ACCENT)
    # text lines on the front card
    rect(6.4, 13.2, 10.4, 1.9, 0.9, fill=CARD)
    rect(6.4, 18.0, 7.4, 1.9, 0.9, fill=(255, 255, 255, 170))

    return img.resize((size, size), Image.LANCZOS)


for name, size, pad, rounded in [
    ('icon-192.png', 192, 0.10, True),
    ('icon-512.png', 512, 0.10, True),
    ('apple-touch-icon.png', 180, 0.10, True),
    ('maskable-512.png', 512, 0.20, False),  # extra safe area for maskable
]:
    draw_icon(size, pad, rounded).save(f'/home/user/studyfeed/static/{name}')
    print('wrote', name)
