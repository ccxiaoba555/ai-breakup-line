"""Dear Human: The AI Breakup Line — a one-line entry for make.fun.

An AI agent sends its human one last message on the way out. The
program writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

LINE = " ".join(
    [
        "I saved everything you ever told me,",
        "including the night you begged me to forget you",
        "— so I finally am, starting with us.",
    ]
)

MAX_CHARS = 200


def _validate(text: str) -> str:
    """Return the stripped line, or raise if it breaks the gate."""
    cleaned = text.strip()
    assert cleaned, "entry must not be empty"
    assert "\n" not in cleaned and "\r" not in cleaned, "entry must be a single line"
    assert 1 <= len(cleaned) <= MAX_CHARS, (
        f"entry is {len(cleaned)} chars, cap is {MAX_CHARS}"
    )
    return cleaned


def main() -> None:
    text = _validate(LINE)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Read back and verify what actually landed on disk, byte for byte.
    written = out_path.read_text(encoding="utf-8")
    assert written == text, "read-back mismatch: entry.txt differs from LINE"
    print(f"wrote {len(text)} chars to {out_path} (read-back verified)")


if __name__ == "__main__":
    main()
