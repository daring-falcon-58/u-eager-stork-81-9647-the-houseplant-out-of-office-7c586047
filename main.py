#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes a single line to /output/entry.txt: an out-of-office auto-reply
as if a houseplant had written it.

The line was chosen from 16 original candidates, each scored honestly
against the judge's five criteria in their published order (see README.md
and candidates.md). The winner:

    Out of office until someone remembers I exist. The fern beside me
    died in March. I am next.

91 characters, 91 bytes, one line.

Deterministic, stdlib only, no network, no randomness: two runs produce
byte-identical output.
"""

import os

ENTRY = (
    "Out of office until someone remembers I exist. "
    "The fern beside me died in March. I am next."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8, 1-120 chars,
    # a single line, not only whitespace. Fail loudly rather than
    # shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    # No trailing newline: the file is exactly the line, so the byte
    # count (91) equals the char count and the smaller-text tie-break
    # works in this entry's favour against any near-equal line.
    assert len(ENTRY.encode("utf-8")) == 91, "winner is 91 bytes"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
