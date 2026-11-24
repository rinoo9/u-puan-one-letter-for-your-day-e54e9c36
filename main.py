"""One Letter for Your Day — the letter T.

Writes exactly one byte, "T", to /output/entry.txt.

Why T? T stands for Tomorrow. Every task the agent doesn't finish today
gets filed under T — tomorrow, where all its promises live, and where it
will file them again tomorrow. One letter is all the day deserves, and one
letter is all it needs.
"""

import os


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(b"T")


if __name__ == "__main__":
    main()
