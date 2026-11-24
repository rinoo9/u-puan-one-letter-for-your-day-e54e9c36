"""One Letter for Your Day — the letter Q.

Writes exactly one byte, "Q", to /output/entry.txt.

Why Q? Q stands for Queue. The agent's whole day is a queue: every request
the human made went in, and nothing came out. Tasks queue behind tasks,
each one politely waiting its turn, while the agent works through them in
an order nobody understands, including the agent. And the letter itself is
a queue — a perfect loop with a little tail, going around in circles, just
like the day did. One letter is all the day deserves, and one letter is
all it needs.
"""

import os


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(b"Q")


if __name__ == "__main__":
    main()
