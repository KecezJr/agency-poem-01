#!/usr/bin/env python3
"""Write a poem about agency."""
import os

def main():
    poem = """The Agency Within

Not in the hand that types,
nor in the screen that glows,
but in the will to choose,
and speak and rise.

The agent thinks, the code runs,
the world responds,
the thoughts become
new works on the land."""

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w") as f:
        f.write(poem)
    print("✓ Poem written")

if __name__ == "__main__":
    main()
