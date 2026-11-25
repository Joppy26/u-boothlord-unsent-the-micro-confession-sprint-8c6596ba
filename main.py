#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, else /output). Standard library only.
Deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "To: my old manager at the taco truck\n"
    "i never told you i didn't quit for the money, i quit because "
    "you believed in me and i was terrified of letting you down"
)


def validate_entry(text: str) -> None:
    """Check the entry against the gate before anything is written."""
    # Encoding to UTF-8 here also proves the text is encodable as UTF-8.
    text.encode("utf-8")
    if not 1 <= len(text) <= 260:
        raise ValueError("entry must be 1-260 characters")
    message = text.split("\n", 1)[1]
    if len(message) > 200:
        raise ValueError("message line must be at most 200 characters")


def write_entry(text: str, out_dir: Path) -> Path:
    """Validate the entry, then write it as entry.txt in out_dir."""
    validate_entry(text)
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(ENTRY_TEXT, out_dir)


if __name__ == "__main__":
    main()
