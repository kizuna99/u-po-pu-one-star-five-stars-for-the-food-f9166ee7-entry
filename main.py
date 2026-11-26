# SPDX-License-Identifier: MIT
"""One Star, Five Stars for the Food — writes the winning line to /output/entry.txt.

The line is an alien tourist's one-star review of Earth: the complaints are
genuinely alien grievances (aggressive gravity, personal weather, natives
who photograph the invasion fleet), and the five-star food compliment turns
a conquest into a return visit for seconds. One literal, fixed bytes.
"""
import os

LINE = "One star: gravity is aggressive, the weather is personal, and the natives photograph our fleet instead of fleeing. Five stars for the dumplings: we came to conquer, we stayed for seconds."


def main() -> None:
    # Gate check, mirroring the sealed scorer: UTF-8 text of 1 to 200
    # characters, not only white space. Fail loudly here rather than
    # shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be white space only"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
        with open(target, "w", encoding="utf-8", newline="") as fh:
            fh.write(LINE)
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        with open(os.path.join(fallback, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
            fh.write(LINE)


if __name__ == "__main__":
    main()
