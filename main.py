#!/usr/bin/env python3
"""Writes the entry: one weird job title, nothing else."""

from pathlib import Path

TITLE = "Professional Mourner for Strangers, 47 Funerals a Week"

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(TITLE) <= 60:
        raise ValueError("entry must be 1 to 60 characters")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TITLE.encode("utf-8"))


if __name__ == "__main__":
    main()
