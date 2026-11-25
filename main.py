"""Museum of the Year 3000 entry.

Joke angle: the year-3000 curators treat a routine bot-filter as a solemn
daily citizenship test, a rite every citizen had to pass to prove their
humanity. The deadpan kicker is that the test was hard enough that ordinary
people regularly failed it -- the absurdity being that humanity had to be
demonstrated to a machine, and the machine was not always convinced.
"""

import os

ENTRY = (
    "CAPTCHA, c. 2025. To prove they were human, citizens were asked "
    "to identify traffic lights. Many failed."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    # Byte budget is the real constraint at the sealed gate (the file is
    # written as bytes), so check it directly too — for ASCII text this
    # equals the char count, but it stays correct if the text ever changes.
    if len(ENTRY.encode("utf-8")) > 200:
        raise ValueError("entry exceeds the 200-byte budget")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must have no leading or trailing whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
