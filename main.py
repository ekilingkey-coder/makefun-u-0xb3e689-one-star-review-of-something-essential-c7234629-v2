#!/usr/bin/env python3
"""Write the one-star review entry to /output/entry.txt (deterministic, offline)."""

import sys

OUTPUT_PATH = "/output/entry.txt"
ENTRY_TEXT = (
    "Sight: at forty it starts moving the menu to arm's length "
    "and expects me to pretend that's how reading works."
)


def write_entry() -> None:
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY_TEXT.encode("utf-8"))


def check_entry() -> int:
    with open(OUTPUT_PATH, "rb") as handle:
        data = handle.read()
    if data == ENTRY_TEXT.encode("utf-8"):
        print("match: /output/entry.txt equals entry.txt (%d characters)" % len(ENTRY_TEXT))
        return 0
    print("MISMATCH: /output/entry.txt differs from the annotated entry")
    return 1


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        return check_entry()
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
