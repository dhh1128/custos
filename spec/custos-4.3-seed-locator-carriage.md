# Custos 4.3 seed — how a locator is written into the bytes (HELD)

> DRAFT, and **HELD** — this seed is complete enough to read and should not be ruled on yet. It waits on the clean-root decision that issue #77 lists last "because it frames the rest." Repair seed for the 4.3 cycle, unpinned until declared final; the ratified Custos 4.2 bytes (sha256 68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a) are untouched by this file. Discharges no finding of its own; it carries the part of finding #85's repair that assignment depends on. Offered to the drafting authority, which owns the wording.

---

## Why this is held rather than proposed

A locator is the committed name of a provision, never reused within a lineage even after repeal. That permanence is the whole value and the whole cost, and it is only worth paying once the thing being named holds still.

Issue #77 records the ratifying authority's signal for this cycle: "a **cleaner root** — excising or subsuming the accumulated strata rather than another accretion pass — with full implementability as the bar," with the connectome pass over 4.2-of-record named as the instrument for deciding what is load-bearing and what is scaffolding. Assigning permanent names before that decision spends permanence on strata that may not survive, and restructuring afterwards leaves insertion suffixes threaded through a document whose purpose is to be legible.

So the convention below is written down now, because it is cheaper to settle the shape while the argument is fresh, and it is not offered for a ruling until the structure it would name is known.

## What it depends on

Finding #85 and its seed, which define the locator, the pinned locator, and the rule that evidence cites bytes while law cites provisions. Nothing here makes sense without those. Finding #90's seed, which puts one line per block, is independent of this but lands in the same neighborhood: a bracketed token at the start of a block presumes a block occupies a line.

## Repair 1 — the token

> A block's locator is written as a bracketed token at the start of the block, followed by a single space. The token is text rather than markup: locating a block is a match on line start.

Taking §8.3's required payloads as they stand, that reads:

```
[8.3.5] Required payloads.

[8.3.5.1] A defeated finding SHALL carry its defeater class and its citation: the violated or superseding clause's identifier, or, for cryptographic defeat, the identifier of the failed verification subject.

[8.3.5.2] A pending finding SHALL carry its typed requirement set: deduplicated elements, each carrying requirement kind, subject identifier, the list of citing clauses, and its discharge species, in the canonical four-field total order.

[8.3.5.3] A self-convicted finding SHALL carry the identifier of the canonical proof package for the contradictory pair.
```

Markup was considered and declined. This document's bytes are its law, so any element admitted here widens the grammar a fold must parse in order to find a clause. A bracketed token is text, and the rule for finding one is a match on line start. It also survives being quoted out of the file, which an `id` attribute does not.

Rendered anchors are generated downstream and do not appear in the bytes. The asymmetry matters: a generator upstream of ratified bytes would put an uncommitted tool inside the law's own production, while rendered HTML is not the law and its transform can be replaced or discarded freely. The transform also has to mangle the identifier, because `id="8.3.5.2"` is legal HTML5 but in CSS and `querySelector` the dots are class separators, and that escaping is a rendering concern that should not reach the law.

## Repair 2 — normative text drops markdown bullets

> Enumerated normative items are locator-labelled blocks rather than markdown list items.

This is what `(a)`, `(b)` and `(c)` are in a statute. Legal drafting has no bullets, because the number *is* the enumeration and it also has to be citable. Under this seed the locator does that work, so a bullet beside it is a second, weaker enumeration that cannot be cited.

It is the change that most visibly alters how the document reads, and it should be judged on that rather than on the mechanics.

## Notes for the drafting authority

**One known defect in this design, unresolved.** Nothing stops a block's prose from beginning with something shaped like `[8.3.5.2]`, at which point a parser reads authored text as structure. CQT names the same failure at its step 3 and answers it by building the placeholder from characters that cannot appear in the input at all. Whether the same answer is available here, and whether the exposure is exploitable or merely untidy, is not settled. It should be before this is ruled on.

**`<dfn>` is not here.** An earlier draft proposed marking defining instances of terms so that a term's address became the locator of the block containing it. That is withdrawn until a term test exists, because marking up whatever currently looks like a term would canonize the unearned coinages and make them harder to retire. The test wanted is roughly: a term survives if an implementation must emit it, or it names a distinction the document holds at every site, or it is imported from a cited external standard.

**The assignment itself is not a seed.** Once the clean-root decision is made, giving every surviving block a locator is mechanical work performed during regeneration, not text to be ruled on. What needs ruling is the convention above.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.2, sha256 `68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a` |
| Status | HELD — not offered for a ruling until the clean-root decision (#77) is made |
| Executed under | No numbered ruling; one is owed when this is taken up |
| Finding discharged | None of its own; carries part of #85's repair |
| Depends on | #85's seed (the locator, the pinned locator, the citation rule) |
| Adjacent | #90's seed (one line per block), independent but presumed by a line-start token |
| Unresolved | A block whose prose begins with something shaped like a locator token |
| Withdrawn | `<dfn>` for defining instances, pending a term test |
| Ratified bytes altered | None |
