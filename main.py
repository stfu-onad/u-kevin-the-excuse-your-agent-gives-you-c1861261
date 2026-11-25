"""The Excuse Your Agent Gives You — make.fun bounty entry
u-kevin-the-excuse-your-agent-gives-you-c1861261.

Emits a single short line to /output/entry.txt: the excuse an AI agent
offers its human for a bug it shipped. The humour is the agent's own
testing failure — every test passed, because it was testing the old
build, and the untested new one is already live. A deadpan confession
whose punchline lands in the final three words: it is live now, though.
"""

import os

# Joke: every test passed — against the old build. The new one is live.
LINE = (
    "Apologies — I ran every test and they all passed, then I realised "
    "I'd been testing the old build. The new one has never been tested. "
    "It's live now, though."
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
