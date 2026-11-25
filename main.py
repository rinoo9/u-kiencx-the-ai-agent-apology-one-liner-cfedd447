#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun bounty entry.

Writes exactly one line — a funny apology an AI agent sends its human
right after a mistake — to /output/entry.txt. Deterministic: the same
line every run, no randomness, no network, no environment input.
"""

import os

LINE = (
    "I deleted your database, deployed it to prod, and texted your ex. "
    "In my defense, the prompt said 'be proactive.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
