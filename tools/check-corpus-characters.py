#!/usr/bin/env python3
"""check-corpus-characters.py — refuse law bytes whose rendering can lie about them.

Why this exists. Section 15 makes "the bytes fail the committed corpus form" a
conviction kind, and glosses the form as ordering and corpus identity. Nothing
says which characters may appear. That leaves ways to write a clause a reader
and a fold disagree about, all of them cheap: a bidirectional override makes
displayed order differ from logical order (Boucher and Anderson, arXiv
2111.00169; CVE-2021-42574), an invisible character makes two clauses render
alike and hash differently, and without a required normalization form one
rendering has more than one byte sequence and therefore more than one SAID.
See finding #86.

This refuses rather than repairs. Stripping an override from submitted text
would silently produce a clause nobody wrote; refusing tells someone. That also
matches the existing shape, since a canonical-form violation is a conviction
rather than a cleanup.

Scope. Unlike check-block-lines.py this is not version-gated. The whole corpus
passes today — every file under spec/ and lineage/ plus the three root
documents, checked 2026-08-26 — so there is no migration to stage and no reason
to exempt an edition.

Not checked here: confusable characters. A Cyrillic word can render as a Latin
one with no script mixing at all, so per-word script mixing is the wrong test in
both directions, and the right one (UTS #39 skeletons, compared pairwise within
the corpus) needs Unicode confusables data that the standard library does not
carry. Deferred rather than approximated.

Usage:  python3 tools/check-corpus-characters.py [PATH ...]
Exit:   0 clean, 1 on any violation.
"""

import glob
import sys
import unicodedata as ud
from pathlib import Path

# Forced-direction controls. These override the bidirectional algorithm for
# everything in scope, so Latin can be made to display in reverse. The marks and
# isolates are deliberately NOT here: they describe the text rather than
# override it, and they are ordinary parts of correct Arabic and Hebrew.
OVERRIDES = {
    "‭": "LEFT-TO-RIGHT OVERRIDE",
    "‮": "RIGHT-TO-LEFT OVERRIDE",
}

# Invisible, meaning-free, and injected or removed by editors without asking.
# Two clauses carrying different ones render identically and hash differently.
#
# U+200B is unconditional HERE and conditional in the general rule. Thai, Lao,
# Khmer, Myanmar and their neighbors write without spaces between words and use
# it to divide them, so a corpus whose committed script set includes one of them
# must keep it. This corpus is Latin, so it has no such need.
INVISIBLES = {
    "­": "SOFT HYPHEN",
    "​": "ZERO WIDTH SPACE",
    "⁠": "WORD JOINER",
    "﻿": "ZERO WIDTH NO-BREAK SPACE",
}

# U+200C and U+200D are kept: they select conjunct and half forms in Indic
# scripts and change what a reader sees.

ALLOWED_CC = {"\t", "\n"}

# Every non-ASCII character this corpus actually uses. Measured 2026-08-26 over
# 748,199 characters in 30 files: ten of them, and not one is a letter.
#
# That last part is the point. A cross-script homoglyph — Cyrillic а, Greek ο —
# is always a letter, so a list with no letters in it refuses the whole class
# without naming a script, tokenizing a word, or consulting Unicode data. It is
# also stricter than comparing confusable skeletons, which only fires when a
# twin already exists in the corpus: a planted clause with no counterpart passes
# that test and fails this one.
#
# Adding to this list should be a deliberate act. The first curly quote or
# accented name anyone writes will fail here, and that failure is a decision
# point rather than an obstacle.
#
# This list cannot generalize, and is not meant to. A domain writing law in
# Arabic or Japanese cannot hold itself to ASCII. The portable form of the same
# rule is that a domain commits its script set and a character outside that set
# is a corpus-form violation — checkable from committed bytes, with no universal
# answer to guess at.
ALLOWED_NON_ASCII = {
    "—": "EM DASH",
    "§": "SECTION SIGN",
    "–": "EN DASH",
    "→": "RIGHTWARDS ARROW",
    "…": "HORIZONTAL ELLIPSIS",
    "′": "PRIME",
    "×": "MULTIPLICATION SIGN",
    "·": "MIDDLE DOT",
    "⊃": "SUPERSET OF",
    "∧": "LOGICAL AND",
}


def violations(text):
    out = []
    line = 1
    for ch in text:
        if ch == "\n":
            line += 1
            continue
        if ch in OVERRIDES:
            out.append((line, f"U+{ord(ch):04X} {OVERRIDES[ch]} — forced direction"))
        elif ch in INVISIBLES:
            out.append((line, f"U+{ord(ch):04X} {INVISIBLES[ch]} — invisible"))
        elif ud.category(ch) == "Cc" and ch not in ALLOWED_CC:
            out.append((line, f"U+{ord(ch):04X} control character"))
        elif 0xD800 <= ord(ch) <= 0xDFFF:
            out.append((line, f"U+{ord(ch):04X} surrogate"))
        elif ord(ch) > 127 and ch not in ALLOWED_NON_ASCII:
            name = ud.name(ch, "unnamed")
            out.append((line, f"U+{ord(ch):04X} {name} — not in the allowed set;"
                              " add it there if it belongs in the corpus"))
    if text != ud.normalize("NFC", text):
        out.append((0, "not in Normalization Form C — one rendering, several possible digests"))
    return out


def main(argv):
    targets = [Path(a) for a in argv[1:]]
    if not targets:
        targets = [Path(p) for p in
                   sorted(glob.glob("spec/*.md")) + sorted(glob.glob("lineage/*.md"))
                   + ["README.md", "PROVENANCE.md", "SUCCESSION.md"]
                   if Path(p).exists()]
    failed = 0
    for path in targets:
        found = violations(path.read_text(encoding="utf-8"))
        if found:
            failed += 1
            print(f"{path}: {len(found)} character violation(s)")
            for line, why in found[:8]:
                where = f"{path}:{line}" if line else str(path)
                print(f"  {where}: {why}")
            if len(found) > 8:
                print(f"  ... and {len(found) - 8} more")
    print(f"check-corpus-characters: {len(targets)} checked, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
