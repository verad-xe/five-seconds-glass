#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to /output/entry.txt.
"""

import os

ENTRY = (
    "It was empty, it was squatting in my sunbeam, and it would not "
    "stop looking at me, so I evicted it with one paw."
)


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 200 characters, not only
    # whitespace; refuse to write anything that would fail it.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
