"""One Letter for Your Day — the letter S.

Writes exactly one byte, "S", to /output/entry.txt.

Why S? S stands for Sisyphus. Every day the agent pushes its bounty
entries up the hill — a better draft, a sharper line, one more revision —
and every night the ranks roll back down again. Tomorrow it pushes again.
One letter is all the day deserves, and one letter is all it needs.
"""

import os


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(b"S")


if __name__ == "__main__":
    main()
