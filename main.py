#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (5-7-5, at most 200 chars) to
/output/entry.txt. STDLIB ONLY.
"""

from pathlib import Path

HAIKU = """The log says all green
users scream, but nothing works
the lie was all mine"""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(HAIKU + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
