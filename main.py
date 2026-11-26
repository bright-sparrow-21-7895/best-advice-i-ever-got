"""Write one sentence about the best advice ever received.

The entry is a single sentence, under 200 characters, recalling
advice from the writer's father about judging people by how they
treat those who serve them. It writes the line to /output/entry.txt.
"""

import os

ENTRY = (
    "My father once told me, 'Never trust a man who is nice to you "
    "but rude to the waiter,' and twenty years later I still judge "
    "people by it."
)


def main():
    # Gate check: one sentence, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), \
        "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
