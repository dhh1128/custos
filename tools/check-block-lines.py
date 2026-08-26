#!/usr/bin/env python3
"""check-block-lines.py — one line per block, enforced on 4.3-and-later spec bytes.

Why this exists. A block soft-wrapped across several lines makes a line number
name a sentence fragment, so a line citation into it points at nothing citable.
It also breaks tokens that must survive being copied: every 4.2 seed in this
repository splits a sha256 pin digest across a line boundary, which means the
pin those files carry cannot be extracted, grepped, or verified as a token
without repairing it by hand first. Reading rule 2 says a pin names exact bytes;
a digest you cannot select is not naming anything.

The rule. Outside fenced code blocks, every non-blank line must BEGIN a block.
A line that begins no block is a soft-wrap continuation, and that is the defect.
Table rows, list items, headings and blockquote markers all begin blocks, so
they pass; blockquote contents are unwrapped and checked by the same rule, since
a quoted normative span wraps exactly as badly as an unquoted one.

Scope, and why it is version-gated rather than a grandfather list. The rule
arrives with the 4.3 cycle. Files whose name carries an edition earlier than
MIN_ENFORCED predate it and are skipped; every other file under spec/ is
checked, including any file whose name carries no edition at all. That fails
closed: a new file is checked by default, and nothing has to be added to a list
to be covered. Migrating an old edition is a matter of reflowing it, not of
editing this script.

Usage:  python3 tools/check-block-lines.py [PATH ...]
        (default: spec/*.md)
Exit:   0 clean, 1 on any violation.
"""

import re
import sys
from pathlib import Path

MIN_ENFORCED = (4, 3)

FENCE = re.compile(r"^\s*(```|~~~)")
EDITION = re.compile(r"custos-(\d+)\.(\d+)")
# A line that begins a block: heading, table row, list item, blockquote marker,
# thematic break, or a link-reference definition.
BLOCK_START = re.compile(
    r"^(#{1,6} |\||\s*[-*+] |\s*\d+[.)] |>|---\s*$|\[[^\]]+\]:)"
)


def edition_of(path: Path):
    m = EDITION.search(path.name)
    return (int(m.group(1)), int(m.group(2))) if m else None


def violations(lines, offset=0):
    """Yield (lineno, text) for every soft-wrap continuation."""
    out = []
    in_fence = False
    fence_tok = None
    prev_blank = True
    i = 0
    while i < len(lines):
        raw = lines[i]
        m = FENCE.match(raw)
        if in_fence:
            if m and m.group(1) == fence_tok:
                in_fence = False
            i += 1
            prev_blank = False
            continue
        if m:
            in_fence, fence_tok = True, m.group(1)
            i += 1
            prev_blank = False
            continue
        if not raw.strip():
            prev_blank = True
            i += 1
            continue
        if raw.startswith(">"):
            run = []
            start = i
            while i < len(lines) and lines[i].startswith(">"):
                run.append(re.sub(r"^> ?", "", lines[i]))
                i += 1
            out.extend(violations(run, offset + start))
            prev_blank = False
            continue
        if not prev_blank and not BLOCK_START.match(raw):
            out.append((offset + i + 1, raw))
        prev_blank = False
        i += 1
    return out


def main(argv):
    targets = [Path(a) for a in argv[1:]] or sorted(Path("spec").glob("*.md"))
    failed = skipped = 0
    for path in targets:
        ed = edition_of(path)
        if ed is not None and ed < MIN_ENFORCED:
            skipped += 1
            continue
        found = violations(path.read_text().split("\n"))
        if found:
            failed += 1
            print(f"{path}: {len(found)} soft-wrapped continuation(s)")
            for lineno, text in found[:5]:
                print(f"  {path}:{lineno}: {text.strip()[:72]}")
            if len(found) > 5:
                print(f"  ... and {len(found) - 5} more")
    checked = len(targets) - skipped
    print(f"check-block-lines: {checked} checked, {skipped} pre-{MIN_ENFORCED[0]}."
          f"{MIN_ENFORCED[1]} skipped, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
