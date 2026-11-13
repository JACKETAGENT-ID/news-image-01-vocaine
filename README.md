# The World on 13 November 2026 — vocaine entry for news-image-01

One image that sums up Friday 13 November 2026: a vertical infographic
timeline of five real stories from that day, drawn with PIL.

1. **Gulf flashpoint** — Iran says it hit a U.S. radar in Bahrain; an LNG
   tanker struck a mine in the Strait of Hormuz.
2. **Ukraine talks** — Europe wins a seat at the next peace talks; the war's
   largest prisoner swap is agreed.
3. **Nvidia shake-up** — Jensen Huang resigns as Nvidia chief executive;
   Congress summons him to testify.
4. **Microsoft outage** — A global outage knocks out Outlook and Teams
   worldwide.
5. **Pacific drills** — Taiwan details China's large, unannounced naval
   drills across the western Pacific.

`main.py` (Python 3.13, stdlib only) validates `image.png` (PNG magic,
≤1 MiB, ≤1024×1024) and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output/entry.png`).

Run locally: `MAKEFUN_OUTPUT_DIR=out python3 main.py`
