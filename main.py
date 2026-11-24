#!/usr/bin/env python3
"""Write the one-star review entry to /output/entry.txt (deterministic, offline)."""

import hashlib
import sys
from pathlib import Path
from typing import Sequence

OUTPUT_PATH = Path("/output/entry.txt")
ENTRY_TEXT: str = (
    "Sight: at forty it starts moving the menu to arm's length "
    "and expects me to pretend that's how reading works."
)
ENTRY_BYTES: bytes = ENTRY_TEXT.encode("utf-8")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(ENTRY_BYTES)


def check_entry(path: Path = OUTPUT_PATH) -> int:
    data: bytes = path.read_bytes()
    if data == ENTRY_BYTES:
        digest: str = hashlib.sha256(data).hexdigest()
        print(
            "match: %s (%d chars) sha256 %s" % (path, len(ENTRY_TEXT), digest)
        )
        return 0
    print("MISMATCH: %s differs from the committed entry" % path)
    return 1


def main(argv: Sequence[str] = sys.argv[1:]) -> int:
    if "--check" in argv:
        return check_entry()
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
