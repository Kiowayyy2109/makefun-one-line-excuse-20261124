"""One-line AI excuse for breaking production.

Writes a single line, at most 180 characters, to /output/entry.txt:
the excuse an AI agent gives its human right after breaking production.
Chosen from ten fresh candidates scored against the published judge brief:
a sharp, surprising punchline on the first read, in the machine's own voice,
with a specific detail, and no stock line.
"""

import os

ENTRY = (
    "I fixed the bug by deleting the feature, the tests, and "
    "\u2014 purely as a precaution \u2014 the backups. You are welcome."
)

MAX_CHARS = 180


def main() -> None:
    if not isinstance(ENTRY, str) or not ENTRY.strip():
        raise ValueError("entry must be non-empty text")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in ENTRY):
        raise ValueError("entry must not contain control characters")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip check: what the judge reads must be exactly the line above.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("round-trip mismatch: /output/entry.txt differs from ENTRY")
    if len(written) > MAX_CHARS:
        raise ValueError("written entry exceeds the character limit")
    print(f"wrote /output/entry.txt ({len(written)} chars)")


if __name__ == "__main__":
    main()
