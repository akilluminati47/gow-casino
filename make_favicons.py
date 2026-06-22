"""Generate a favicon set from images/favicon.png (Gears skull-gear emblem)."""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "images", "favicon.png")

src = Image.open(SRC).convert("RGBA")
print("source size:", src.size)

# Place the emblem on a square transparent canvas so it never distorts.
w, h = src.size
side = max(w, h)
square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
square.paste(src, ((side - w) // 2, (side - h) // 2), src)

def out(name):
    return os.path.join(ROOT, name)

def resized(size):
    return square.resize((size, size), Image.LANCZOS)

# Standalone PNG icons
png_sizes = {
    "favicon-16x16.png": 16,
    "favicon-32x32.png": 32,
    "favicon-48x48.png": 48,
    "apple-touch-icon.png": 180,
    "android-chrome-192x192.png": 192,
    "android-chrome-512x512.png": 512,
}
for name, size in png_sizes.items():
    resized(size).save(out(name), "PNG")
    print("wrote", name)

# Multi-resolution .ico
ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
square.save(out("favicon.ico"), format="ICO", sizes=ico_sizes)
print("wrote favicon.ico", ico_sizes)
