#!/usr/bin/env python3
"""food-picture-01 entry: copy the ramen picture to the output directory.

The entry program runs in a sandbox with a read-only /bot (this repository)
and a writable /output. Outside the grader, MAKEFUN_OUTPUT_DIR stands in
for /output. It writes exactly one file, entry.png, byte for byte the same
on every run.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if not src.is_file():
        print("entry.png missing beside main.py", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")
    print(f"wrote {out_dir / 'entry.png'} ({src.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
