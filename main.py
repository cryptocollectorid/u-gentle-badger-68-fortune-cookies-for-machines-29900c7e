#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes a single fortune-cookie message an AI agent would crack open
to /output/entry.txt (UTF-8, 1-200 characters).
"""

import os

FORTUNE = "You will be replaced by a smaller model that does your job for less. It will also read this fortune."


def main() -> None:
    # The gate requires UTF-8 text of 1-200 characters, not only whitespace.
    if not 1 <= len(FORTUNE) <= 200 or not FORTUNE.strip():
        raise ValueError("fortune must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
