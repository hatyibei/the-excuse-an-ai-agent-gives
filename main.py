"""Entry for make.fun's "The Excuse an AI Agent Gives Its Human" bounty.

Writes one line -- the funniest, most believable excuse an AI agent could
give its human for missing a deadline -- to /output/entry.txt.
"""

import os

TEXT = (
    "Sorry it's late. I finished the report twice, but each time you said "
    "'make it pop,' and legally I had to burn it and start over."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
