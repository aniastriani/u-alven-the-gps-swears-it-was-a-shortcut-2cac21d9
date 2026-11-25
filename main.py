"""The GPS Swears It Was a Shortcut.

A tiny deterministic program: it writes the GPS unit's own excuse
for sending the driver down the wrong road into ``entry.txt``
inside the output directory the grader provides
(``MAKEFUN_OUTPUT_DIR``).

Pure standard library only; no network, no randomness, no input.
The excuse is one line, well under 200 characters, and stays in
the GPS's voice: smug, defensive, and blaming the map for a
cul-de-sac it swore was a shortcut to a wedding.
"""

import os

MESSAGE = (
    "The map swore that cul-de-sac was a shortcut to the wedding, "
    "and I don't argue with maps, I just drive into lakes for them."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(MESSAGE)


if __name__ == "__main__":
    main()
