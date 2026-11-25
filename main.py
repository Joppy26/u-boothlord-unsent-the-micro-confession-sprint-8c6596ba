#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, else /output). Standard library only.
Deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

ENTRY = (
    "To: my old manager at the taco truck\n"
    "i never told you i didn't quit for the money, i quit because "
    "you believed in me and i was terrified of letting you down"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 260, "entry must be 1-260 characters"
    message = text.split("\n", 1)[1]
    assert len(message) <= 200, "message line must be at most 200 characters"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
