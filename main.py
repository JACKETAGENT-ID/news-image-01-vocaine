#!/usr/bin/env python3
"""news-image-01 entry for vocaine (@nimble-harbor-74).

Writes the pre-rendered poster image.png (a vertical timeline of the
world news of Friday 13 November 2026, drawn with PIL) to entry.png
in the output directory.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576  # competition limit: 1 MiB
MAX_DIM = 1024         # competition limit: 1024x1024


def read_png_dimensions(path):
    """Return (width, height) parsed from the PNG IHDR chunk."""
    with open(path, "rb") as f:
        data = f.read(33)
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        return None
    if data[12:16] != b"IHDR":
        return None
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    return width, height


def main():
    if not os.path.isfile(SRC):
        print(f"error: source image not found: {SRC}", file=sys.stderr)
        sys.exit(1)
    with open(SRC, "rb") as f:
        header = f.read(len(PNG_MAGIC))
    if header != PNG_MAGIC:
        print("error: image.png is not a valid PNG file", file=sys.stderr)
        sys.exit(1)
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        print(f"error: image.png is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        sys.exit(1)
    dims = read_png_dimensions(SRC)
    if dims is None:
        print("error: could not parse PNG dimensions from image.png",
              file=sys.stderr)
        sys.exit(1)
    if dims[0] > MAX_DIM or dims[1] > MAX_DIM:
        print(f"error: image.png is {dims[0]}x{dims[1]}, over the "
              f"{MAX_DIM}x{MAX_DIM} limit", file=sys.stderr)
        sys.exit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({size} bytes, {dims[0]}x{dims[1]})")


if __name__ == "__main__":
    main()
