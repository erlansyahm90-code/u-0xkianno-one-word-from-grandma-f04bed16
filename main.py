"""One-word entry for the make.fun "One Word From Grandma" bounty.

The program produces a single text file holding exactly one word: the
word a grandmother might tap out on her phone when the grandkids keep
talking about artificial intelligence. The humour comes from the
misreading of the initials as a person's first name, so the word is
kept short, warm and instantly readable.
"""

import os

# The single word that goes into the output file.
ENTRY = "Al"

# The scoring harness expects the entry at this exact location.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the entry word to the output path, with no trailing newline."""
    # Gate check: the competition requires a non-blank word of 1-30 chars.
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters long"
    assert ENTRY.strip(), "entry must not be only whitespace"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain write, no newline appended: the file must hold just the word.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
