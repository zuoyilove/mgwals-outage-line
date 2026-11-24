#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes one status page line (at most 160 characters) to
/output/entry.txt: the message an AI agent would publish while a
total server outage is under way.

The line is fixed text, written by this program. It is plain,
first person, specific about what is down, and honest about what
the agent cannot check or does not yet know: no invented cause,
no invented ETA.
"""

import os

LINE = (
    "Every server is down — even the ones that would tell me what's "
    "wrong. I can't check anything yet or say when we'll be back. "
    "I'll update when I can."
)

MAX_CHARS = 160


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, (
        f"line must be 1-{MAX_CHARS} characters, got {len(LINE)}"
    )
    assert LINE.strip(), "line must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
