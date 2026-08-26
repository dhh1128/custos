# Custos 4.3 seed — characters in the committed corpus form

> DRAFT — repair seed for the 4.3 cycle. Unpinned until declared final. Enters the successor by succession; the ratified Custos 4.2 bytes (sha256 68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a) are untouched by this file. Discharges finding #86 only. **Executed under no numbered ruling**, and one is owed: the repair adds normative content to §15's corpus form, which is ruling-grade. Offered to the drafting authority, which owns the wording.

---

## What this seed carries

One addition to a form that already exists. §15 makes "a canonical-form violation (the bytes fail the committed corpus form — ordering, corpus identity)" a conviction kind (L2777-2778), so a corpus form is already there and failing it is already convictable. The gloss names ordering and corpus identity. This seed gives the form character content, so that the shape of the deception finding #86 describes has a name and a conviction rather than passing unremarked.

## The defect, in one paragraph

Finding #86 carries the evidence. Nothing in the ratified bytes says which characters may appear in law: searched 2026-08-26, the text contains no occurrence of "unicode", "utf-8", "codepoint", "charset", or any form of "normaliz". A bidirectional override makes displayed order differ from logical order, so a clause can read one way to every reviewer and hash as something else. An invisible character makes two clauses render alike and hash differently, which matters here because under §5's ladder the digest is the whole of a clause's identity. Absent a required normalization form, one rendering has more than one byte sequence and therefore more than one SAID. And the constructions that put a verifier in front of law written by a party they are not required to trust — the covenant seal's clause set in another domain's registry (L2041-2045), and clause-selective disclosure handing over individual clauses to check in isolation (L1486-1489) — are exactly where this is not an insider problem.

## Repair — the corpus form reaches characters

**At §15**, joined to the conviction-kinds paragraph:

> **Characters.** The committed corpus form constrains the bytes of law, not only their arrangement. A domain SHALL commit the set of scripts its law is written in, and a character outside the committed set is a canonical-form violation. Independently of that set, law bytes SHALL be in Normalization Form C and SHALL NOT contain `U+202D LEFT-TO-RIGHT OVERRIDE`, `U+202E RIGHT-TO-LEFT OVERRIDE`, `U+00AD SOFT HYPHEN`, `U+2060 WORD JOINER`, `U+FEFF ZERO WIDTH NO-BREAK SPACE`, an unpaired surrogate, or a control character other than tab and newline. `U+200B ZERO WIDTH SPACE` is excluded unless the committed script set contains a script that writes without spaces between words. A frame that consumes law failing this form convicts under the canonical-form kind and does not repair it: bytes silently corrected are a clause nobody enacted.

Three things about the shape are deliberate.

The committed script set is what makes this portable. Custos cannot say which scripts are legitimate, and any list it picked would be wrong somewhere — Azerbaijani law using both Latin and Cyrillic is ordinary, and Japanese mixes three scripts inside single words. A domain commits, and departure from what it committed is derivable from bytes. That is the same move §5 makes everywhere else, and it needs no Unicode data file and no universal answer.

The unconditional exclusions are the characters that carry no meaning in any script. The two overrides instruct a rendering engine rather than describe the text, which is what makes them the mechanism of the deception. The bidirectional marks and isolates are deliberately not excluded, because they describe the text rather than override it and are ordinary parts of correct Arabic and Hebrew. `U+200B` is conditional because Thai, Lao, Khmer, Myanmar and their neighbors use it to divide words that would otherwise run together, so a blanket exclusion would merge words their readers keep apart.

Refusal rather than repair follows §15's existing shape. A canonical-form violation is already a conviction, not a cleanup, and a stripped override would produce a clause nobody wrote while leaving the record silent about it.

## Notes for the drafting authority

**The tooling exists and the corpus already passes.** `tools/check-corpus-characters.py`, added beside this seed, refuses the unconditional set and non-NFC text over every file in `spec/` and `lineage/` plus the three root documents. Measured 2026-08-26 across 748,199 characters in 30 files: no overrides, no invisibles, no stray control characters, everything already NFC. This is prevention rather than cleanup, which is the cheapest moment to adopt it.

**This document's own instance of the rule is an allowlist, and it does not generalize.** The corpus uses exactly 10 non-ASCII characters — em dash, section sign, en dash, rightwards arrow, ellipsis, prime, multiplication sign, middle dot, superset of, logical and — and not one is a letter. Since every cross-script homoglyph is a letter, listing the ten and refusing everything else defeats that whole class without naming a script or consulting Unicode data. It is stricter than comparing confusable skeletons, which only fires when a twin already exists in the corpus and misses a planted clause with no counterpart. It is also unavailable to a domain writing law in a non-Latin script, which is why the normative text above is the committed script set and the allowlist is only how this document satisfies it.

**Confusable detection is deliberately absent, and the reason is worth recording.** Per-word script mixing is the wrong test in both directions: it fires constantly on Japanese, which mixes Han, Hiragana and Katakana inside single words, and it misses a wholly Cyrillic word that renders as a Latin one, since nothing is mixed. The right test is relational — two distinct words in a corpus sharing a UTS #39 skeleton — and it needs Unicode confusables data the standard library does not carry. Bundling that data or taking a dependency is a decision this seed does not make. Latin-internal confusables (`rn` against `m`, `l` against `I`) are reachable by no character rule at all and are left to review.

**A domain's committed script set has no home yet.** The text above says a domain SHALL commit its script set and does not say where. §18's GEL grammar is the likely site, alongside the founding law's other committed placements, but that is a question for whoever draws the re-rooted structure rather than one this seed should answer.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.2, sha256 `68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a` |
| Executed under | No numbered ruling; one is owed (normative content added to §15's corpus form) |
| Finding discharged | #86 (the committed corpus form says nothing about characters) |
| Spans repaired | §15 conviction kinds L2775-2782 (addition) |
| External citations verified | 2026-08-26 — Boucher and Anderson, "Trojan Source: Invisible Vulnerabilities", arXiv 2111.00169, later USENIX Security; CVE-2021-42574 (bidirectional) and CVE-2021-42694 (homoglyph), both issued against the Unicode specification; UTS #39 skeleton and restriction-level definitions at `https://www.unicode.org/reports/tr39/`; CQT step 2 and step 5 at `https://dhh1128.github.io/canonical-quoted-text/` |
| Prior art consulted, not adopted | CQT is a lossy transform for comparing human text and folds whitespace, dashes and quote characters, which would destroy line structure and erase §4 reading rule 1's distinction between quoted and unquoted text. Its precondition steps port; the algorithm does not |
| Charter input, not designed here | Where a domain commits its script set; whether confusable detection is worth a data dependency |
| Re-ruling | No |
| Ratified bytes altered | None |
