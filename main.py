"""Fridge Roast: One Line, Biggest Laugh.

Writes a single-line roast of a smart fridge to entry.txt.
The roast is a fixed string, so the output is fully deterministic.
"""

import os

ENTRY = "My smart fridge's camera caught me eating the last slice at 2 a.m. — now it locks the freezer and calls it 'accountability'."

assert 1 <= len(ENTRY) <= 200


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
