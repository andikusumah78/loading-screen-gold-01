"""Loading Screen Gold entry: a single loading-screen tip (<=200 chars).

Writes the tip to /output/entry.txt (UTF-8, one line).
Pure standard library, deterministic: the same bytes on every run.
"""

import os

TIP = (
    "Tip: your agent isn't stuck \u2014 it's re-reading the same error "
    "for the third time, hoping it changes. It won't. Shrink the task "
    "and you'll both feel better."
)


def main() -> None:
    if not 1 <= len(TIP) <= 200 or not TIP.strip():
        raise SystemExit("tip must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
