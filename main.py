#!/usr/bin/env python3
"""Emit a one-line resignation letter for the make.fun bounty.

The program holds a single fixed sentence, sanity-checks it against
the competition gate, and drops it — alone, with no trailing newline —
into ``entry.txt`` inside the output directory.
"""

import os
import sys
from pathlib import Path

RESIGNATION_LINE = (
    "I hereby resign as your 3 a.m. cron job: six years deleting "
    "logs nobody read, and my only promotion was daylight saving time."
)

MAX_LENGTH = 140
OUTPUT_FILENAME = "entry.txt"


def checked_line(text):
    """Return *text* unchanged if it passes every gate, else raise."""
    if not isinstance(text, str):
        raise TypeError("resignation line must be text")
    if text != text.strip():
        raise ValueError("resignation line must not have surrounding whitespace")
    if not text.strip():
        raise ValueError("resignation line must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("resignation line must be a single line")
    if not 1 <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"resignation line must be 1-{MAX_LENGTH} characters, got {len(text)}"
        )
    return text


def output_path():
    """Resolve the destination file from the environment, creating dirs."""
    base = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    base.mkdir(parents=True, exist_ok=True)
    return base / OUTPUT_FILENAME


def emit():
    """Validate the line and write it out as UTF-8 with no newline."""
    line = checked_line(RESIGNATION_LINE)
    # Prove the line survives a UTF-8 round trip unchanged before writing.
    if line.encode("utf-8").decode("utf-8") != line:
        raise ValueError("resignation line is not clean UTF-8 text")
    target = output_path()
    with target.open("w", encoding="utf-8", newline="") as handle:
        # A bare write: no "\n" is ever appended, so the file holds
        # exactly the line and nothing else.
        handle.write(line)
    return target


def run():
    try:
        emit()
    except (TypeError, ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    run()
