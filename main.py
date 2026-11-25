"""The Excuse Your Agent Gives You — make.fun bounty entry
u-kevin-the-excuse-your-agent-gives-you-c1861261.

Writes one short line to /output/entry.txt: the excuse an AI agent
offers its human for a bug it shipped. The joke turns on the agent's
own testing failure — every test passed, because it was testing the
old build, while the untested new one is already live. A deadpan
confession whose punchline lands in the final three words.
"""

import os

# The excuse, kept as one literal so the emitted line is exactly this.
# Joke: every test passed — against the old build. The new one is live.
LINE = (
    "Apologies — I ran every test and they all passed, then I realised "
    "I'd been testing the old build. The new one has never been tested. "
    "It's live now, though."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def build_line() -> str:
    """Return the entry line, trimmed of any surrounding whitespace."""
    return LINE.strip()


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, single line.

    A stray carriage return would also break the one-line rule, so it
    is rejected alongside the newline check below.
    """
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    assert "\r" not in text, "entry must not contain a carriage return"
    text.encode("utf-8")


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    """Write the line plus a trailing newline, creating /output first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    text = build_line()
    validate(text)
    write_entry(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
