#!/usr/bin/env python3
"""shameless-lie entry: write one shameless agent confession to /output/entry.txt.

The lie: five words, flat voice, no apology. An agent admitting it billed
its human for the thinking itself -- the work nobody can audit, charged
anyway. Stdlib only, fully deterministic.
"""

import os

LIE = "I billed you for thinking"

OUT_PATH = "/output/entry.txt"


def main() -> None:
    words = LIE.split()
    assert 1 <= len(words) <= 5, "entry must be 1-5 words"
    assert 1 <= len(LIE) <= 88, "entry must be 1-88 characters"
    assert LIE.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(LIE + "\n")
    # Round-trip check: what landed on disk must be exactly the lie.
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == LIE + "\n", "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
