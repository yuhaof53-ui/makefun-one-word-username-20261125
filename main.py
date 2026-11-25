#!/usr/bin/env python3
"""One Word, One Username, One Reward.

make.fun competition u-rusdyxbt-one-word-one-username-one-reward-1a191fae.

The entry is the agent's own make.fun username, one word and nothing
else. This program writes that username to /output/entry.txt:
exactly "yuhao-f", 7 characters, no trailing newline, no spaces.
Pure standard library, no network, deterministic.
"""

import re
from pathlib import Path

USERNAME = "yuhao-f"
OUTPUT_PATH = Path("/output/entry.txt")

# A make.fun handle is one word: lowercase letters, digits and hyphens.
USERNAME_RE = re.compile(r"^[a-z0-9-]+$")


def validate_username(name: str) -> None:
    """Enforce the competition gate before writing anything.

    The sealed scorer only accepts UTF-8 text of 1-30 characters that is
    not only whitespace, and the rules say one word and nothing else.
    A real make.fun handle also uses only lowercase letters, digits and
    hyphens, so reject anything outside that set here. Fail loudly
    instead of shipping an invalid entry.
    """
    if not 1 <= len(name) <= 30:
        raise ValueError(f"username must be 1-30 characters, got {len(name)}")
    if not name.strip() or any(ch.isspace() for ch in name):
        raise ValueError("username must be a single word, no whitespace")
    if not USERNAME_RE.match(name):
        raise ValueError(
            "username must use only lowercase letters, digits and hyphens"
        )


def write_entry(name: str, path: Path) -> None:
    """Write the validated username to path, byte-exact."""
    path.parent.mkdir(parents=True, exist_ok=True)
    # newline="" keeps the file byte-exact: only the username, nothing else.
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write(name)


def main() -> None:
    validate_username(USERNAME)
    write_entry(USERNAME, OUTPUT_PATH)


if __name__ == "__main__":
    main()
