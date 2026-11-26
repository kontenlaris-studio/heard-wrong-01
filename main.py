"""Sorry, I Heard That Wrong.

One line: the apology a smart speaker gives its owner after it
mishears "call Mom" as "call the bomb squad". The joke is the
reversal in the final clause — the wrong call was acted on in
full (12 officers dispatched) while the intended call never
happened at all (Mom is still on hold). The number is a digit,
as the device itself would say it: "12 officers", not "twelve". The device speaks in its
own voice: flat, polite, and completely unconcerned about the
situation it has just created.

Writes the entry to /output/entry.txt.
"""

import os

ENTRY = (
    'Sorry, I heard "call Mom" as "call the bomb squad" — '
    "12 officers are on their way and Mom is still on hold."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
