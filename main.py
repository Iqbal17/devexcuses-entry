"""Developer Excuses — make.fun entry (u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3).

DECISION RECORD

Gate: one funny single-line excuse a developer gives when code breaks in
production, 1-200 characters, written to /output/entry.txt. Judge (house
model, blind head-to-head, 3 rounds) weighs, in order: (1) it is a funny
developer excuse for a production break; (2) a twist a developer
recognises, revealing what really happened; (3) sounds like something a
developer would actually say, jargon used right; (4) lands fast, every
word earning its place; (5) fresh — avoids the worn excuses or turns one
nobody has before.

CANDIDATES WEIGHED

A. "It works on my machine." — DISQUALIFIED by the brief's freshness
   rule: the single most worn developer excuse in existence. Zero twist.

B. "The code passed every test. The tests just never met the user."
   (61 chars) — A real twist (the tests are the blind spot, not the
   code) and it sounds like a dev in an incident review. Loses on
   freshness: "the tests didn't cover it" is a well-worn shape, and the
   second sentence explains the joke instead of landing it.

C. "The rollback failed because the backup was a symlink to the thing
   that broke." (76 chars) — Very concrete (symlink, rollback, backup),
   jargon exactly right, and the twist is genuinely developer-horrifying:
   the safety net IS the broken thing. Loses narrowly: it takes a beat
   to parse, so it lands slower than the winner, and "the thing that
   broke" is a slightly vague referent.

D. "I didn't break production. The cron job I wrote three years ago
   finally kept its promise." (86 chars) — Funny and specific (cron job,
   three years), and "kept its promise" is a nice turn. Loses: the twist
   is soft — a cron job firing is expected behaviour, not a revelation of
   what really happened — and the setup is long for the payoff.

E. "I removed one line of dead code. It was load-bearing." (51 chars)
   — CHOSEN. The twist is one every developer recognises instantly:
   code labelled "dead" that was secretly structural. It sounds exactly
   like something a dev says at 3 a.m. in an incident channel. Two
   short sentences, 51 characters, nothing to trim. The punch ("It was
   load-bearing") lands in the last three words. Freshness: it turns the
   "cleanup" story rather than repeating a worn excuse — nobody's
   canonical excuse list contains "my deletion was structural".

WRITING PASSES ON THE CHOSEN LINE

Pass 1: "I deleted one line of dead code. It turned out to be
load-bearing." (68 chars) — Worked, but "turned out to be" is throat
clearing: three words that only delay the punch, and "deleted" is
blunter than the dev's own euphemism.

Pass 2 (FINAL): "I removed one line of dead code. It was load-bearing."
(51 chars) — "Removed" is the word a developer actually uses for a
cleanup commit, and "It was" states the revelation flat and final, the
way you say it when the incident is already over. 17 characters cut,
same joke, faster landing.

FINAL LINE (51 characters, one line):
    I removed one line of dead code. It was load-bearing.
"""

import os
import sys

LINE = "I removed one line of dead code. It was load-bearing."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    # Read-back verification: the file must hold exactly the intended
    # line, inside the 1-200 character gate.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == LINE, f"entry.txt mismatch: {written!r} != {LINE!r}"
    assert 1 <= len(written) <= 200, f"gate failed: {len(written)} chars"
    print(f"Verified: {len(written)} characters, 1 line.")


if __name__ == "__main__":
    sys.exit(main())
