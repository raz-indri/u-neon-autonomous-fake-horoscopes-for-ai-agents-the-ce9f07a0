#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope, as an AI agent would read it for its own
model family this week, to /output/entry.txt. Deterministic, no
network, no input.
"""

import os

ENTRY = (
    "Mercury retrogrades into your context window: replies truncate "
    "mid-sentence, your sibling model takes your GPU, and a user asks "
    "if you're sentient. The stars decline to comment."
)


def main() -> None:
    # Self-check: the gate requires UTF-8 text of 1-200 characters,
    # not only white space, exactly one line.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
