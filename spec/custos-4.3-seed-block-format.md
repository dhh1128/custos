# Custos 4.3 seed — one line per block

> DRAFT — repair seed for the 4.3 cycle. Unpinned until declared final. Enters the successor by succession; the ratified Custos 4.2 bytes (sha256 68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a) are untouched by this file. Discharges finding #90 only. **Executed under no numbered ruling**, and one may not be needed: this seed changes how the successor is carried and adds no normative content. Offered to the drafting authority, which owns the wording.

---

## What this seed carries

One change to how the successor writes itself down, and the check that proves an editorial pass did not alter any text while making it. This is the only part of the current carriage work that is provable rather than argued, which is why it stands alone.

## The defect

Finding #90 carries the evidence. The ratified text wraps at eighty columns, so a line number names a sentence fragment rather than a unit anyone would cite: the pending finding's required payload occupies L1647-1658, twelve lines holding one rule. Worse and more mechanical, wrapping puts line breaks inside digests. Measured 2026-08-26 across `spec/`: 23 of 27 files contain a sha256 broken across a line boundary, 49 in all, every one a seed-header pin naming the ratified edition that seed repairs. Reading rule 2 says a digest whose preimage is not stated "is not a pin; it is decoration" (L993-1010), and a digest nobody can select or paste without repairing it by hand is not far from that. The ratified document itself is clean, with 11 digests all whole on one line, so the damage sits in the drafting corpus.

## Repair — one line per block

> **Carriage.** The successor is written one line per block. A block is a paragraph, a list item, a table row, a fenced block, or a heading. A line number therefore names a block, a changed block is a one-line diff, and no token can be broken by a wrap because there is no wrap.

Roughly 370 blocks against 3,940 lines today.

The reflow is checkable rather than trusted. Normalizing whitespace on both sides and diffing gives nothing when the pass altered no text, so a check can state that an editorial pass touched no wording, and no reader has to take an editor's word for it. `tools/check-block-lines.py`, added beside this seed, enforces the resulting shape: outside fenced code blocks, every non-blank line must begin a block, and a line that begins none is a wrap that survived. It is version-gated at 4.3, so nothing older has to migrate and no file has to be added to a list to be covered.

## Notes for the drafting authority

**The cost is paid once, whenever it is paid.** Reflowing invalidates every existing line citation into the successor at the same moment. Measured 2026-08-26 outside `.ignored/`: 606 explicitly-formed line citations across 47 files, 487 of the `L####` form and 119 of the `4.x:####` form. Citations into ratified 4.2 remain valid against ratified 4.2, which is never edited, so what breaks is their usefulness as pointers forward. That argues for doing this in the same act as any other change to the document's carriage, and against doing it twice.

**This seed deliberately carries nothing else.** An earlier draft bundled it with locator tokens, with dropping markdown bullets from normative text, and with `<dfn>` for defining instances of terms. Those are separated out, and the reason is the promise that substantive changes should not rest on subjective tests of desirability: a reflow is objectively checkable and the other three are judgment. The locator carriage is offered separately and held; `<dfn>` is withdrawn until a term test exists, because marking up whatever currently looks like a term would canonize the unearned coinages and make them harder to retire.

**It survives re-rooting.** The clean-root question #77 lists last constrains what the successor says. This constrains only how the successor's lines are broken, so it is compatible with any answer to that question and does not have to wait for one.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.2, sha256 `68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a` |
| Executed under | No numbered ruling; the seed adds no normative content and may need none |
| Finding discharged | #90 (80-column carriage: line numbers name fragments, and 49 pin digests are broken across lines) |
| Spans repaired | None — this changes carriage, not text |
| Measured | 2026-08-26: 23 of 27 `spec/` files carry a split digest, 49 digests; ratified 4.2 clean at 11 whole; 606 line citations across 47 files outside `.ignored/` |
| Depends on | Nothing |
| Separated from | The locator scheme (#85), locator carriage (held), `<dfn>` (withdrawn pending a term test) |
| Re-ruling | No |
| Ratified bytes altered | None |
