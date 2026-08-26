# Custos 4.3 seed — the locator, a second identity for law

> DRAFT — repair seed for the 4.3 cycle. Unpinned until declared final. Enters the successor by succession; the ratified Custos 4.2 bytes (sha256 68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a) are untouched by this file. Discharges finding #85 only. **Executed under no numbered ruling**, and one is owed: the repair adds a definition to §5 and a reading rule to §4, which is ruling-grade. Offered to the drafting authority, which owns the wording.
>
> Adjacent, not conflicting: the covenant seal carriage seed (finding #80) repairs *where the seal's kind is written* and states that what the seal irreducibly does — name the clause set a successor is answerable to — is untouched. This seed repairs *how that clause set is named*. Neither depends on the other; both land in §10.

---

## What this seed carries

One addition, with consequences. Custos gives law exactly one identity — the self-addressing digest — and then, in three places, requires a citation the digest cannot supply. The addition is a second identity that names a *provision* rather than *bytes*, so that the two questions every legal system keeps apart can be asked separately here too.

The two identities pair rather than compete. The SAID answers which bytes. The locator answers which provision, across every version those bytes ever had. A citation carrying both is a **pinned locator**, and §4's existing two-kind pin discipline already has the vocabulary for it.

## The defect

§5's law ladder makes the clause "SAID-addressed bytes in the GEL, carrying one or more predicates and their codomain mapping — the citable atom that grounds cite and disclosure binds to" (L1198–1201). Self-addressing is the *only* identity a clause has. Three ruled or load-bearing spans then ask for something else and receive no definition.

**§8.3's defeated payload** requires "the violated or superseding clause's identifier" (L1641–1643). Under SAID-only identity there is no expressible sense in which a superseding clause supersedes a *particular provision*: amendment changes bytes, so it changes the SAID, so the amended clause and its predecessor are two unrelated digests. The defeater class **superseded** — "a later lawful act displaced the subject" (L1775) — describes a relation the record has no way to carry.

**§10's covenant seal** states that "the promise survives amendment; the seal carries the question, and the fold supplies the answer" (L2033–2034), which is true only if the sealed set names provisions. It cannot name bytes: the same section makes "a covenant seal over digest-sealable content" defective (L2040–2041), so a seal over SAIDs is a digest seal wearing the wrong label. What the text actually says is that the sealed set "names clause identifiers into the sealing domain's designated governance registry; a portable clause language — sealing a subject to another domain's law — is chartered to the encoding round and not designed here" (L2041–2045). The construct is already committed to an identifier kind the document declines to define.

**§8.3's canonical selection** orders defeats by "the lexicographic minimum of (defeater-class rank, citation identifier, subcode)" (L1767–1769). Over SAIDs that comparand is a digest sort: deterministic, and arbitrary. The subcode beneath it is "assigned by the cited clause's own committed enumeration; where the clause defines none, the subcode is empty and orders last" (L1776–1779) — a per-clause numbering scheme, optional, unnamed, and left to each domain to invent.

Three sites, one missing object. The seal case is the sharp one, because a covenant seal is a forward promise authored by a *different* domain, which cannot rewrite it when the sealing domain's law moves.

## Repair 1 — the locator

**At §5**, a new definition, sited with the law ladder:

> **Locator.** The committed name of a provision, stable across every revision of that provision's bytes: a path identifying a block of law within a corpus, assigned when the block is drafted and carried inside the block's own SAID-addressed bytes. A locator SHALL be assigned once and SHALL NOT be reused within a lineage, including after repeal — a repealed provision's locator is a tombstone, and reassignment silently retargets every citation that survives it. A locator's bytes are inside the preimage its SAID commits, so renumbering is an amendment with a new SAID and is convictable as one.

Grammar, which the document fixes for itself:

```abnf
locator = segment *( "." segment )
segment = number *( "-" number )
number  = "0" / ( %x31-39 *DIGIT )   ; no leading zeros
```

`.` descends into children. `-` inserts a sibling between two existing peers, which is the operation the child namespace cannot express: `8.3.5-1` sits between `8.3.5` and `8.3.6`, `8.3.5-1-1` between `8.3.5-1` and `8.3.5-2`, and `8.3.5-1.1` is the first child of an inserted block. The mechanism exists because non-reuse makes renumbering unavailable, not as a deferral of tidiness: there is no later pass in which suffixes are paid off, and the consecutive numbering it appears to defend is a property of a first draft only.

Ordering, which §8.3's canonical selection consumes:

> Locators compare segment-wise, left to right; a path that is a proper prefix of another sorts first, so a parent precedes its children. Within a segment the insertion list compares element-wise as integers, a proper prefix again sorting first. Two verifiers holding the same pair of locators SHALL order them identically.

Digits only, one alphabet, one comparison rule. Letter suffixes were considered and declined: byte-lexicographically `5aa` falls between `5a` and `5b` rather than after `5z`, so their reading order is not apparent on the face of the citation.

The tier is deliberately **not** encoded. Whether depth 3 is a paragraph or a subsection is a property of the block, not of its name; domains carry incompatible tier vocabularies — chapter, article, rule, canon — and baking one into the grammar forces a fork.

Every block carries a locator, not only ruled spans. A block that gains or loses a BCP 14 keyword under §4's reading rule 1 (L981–986) must not change its name, motivation is worth citing, and mechanical assignment beats judgment-laden assignment.

## Repair 2 — the pinned locator

**At §4, reading rule 2**, extending the two-kind pin discipline rather than replacing it. A locator alone does not resolve; it names a provision in whatever law is in force, and "in force" must be a committed fact rather than an ambient one.

> A **pinned locator** is a locator joined to a law head by `@` — `8.3.5@<law head>` — and it is the citation form that travels. An unpinned locator is lawful only inside the corpus that contains it, where the corpus is fixed by where the citing bytes sit. Any citation crossing a corpus boundary, and every citation carried in a finding, a receipt, or a seal, SHALL be pinned. An unpinned locator in those positions is a defect, not a shorthand: resolving it would consult the law in force at read time, which is the ambient input §8.3 forbids from reaching a finding (L1629–1631).

The clause SAID is uniquely re-derivable from a pinned locator by a fold over the GEL — no resolver, no registry, no editorial authority. That is what makes the construct admissible here, and it slots into §8.3's existing allowance for citations that are "explicit or uniquely re-derivable from a committed referent" (L1645–1646) without amending that sentence.

`@` is not a coinage. The Akoma Ntoso Naming Convention (OASIS Standard, 2019-02-21) builds an Expression IRI from a Work IRI with exactly that separator. Its unpinned form, meaning "current at access time", is the one this document must refuse.

**At §10's conviction family** (L2049–2052), which insists that "a digest mismatch, a coordinate mismatch, and a clause violation are three different refusals, and a record that blurs them is unauditable" — a fourth:

> A **locator mismatch** is the refusal a verifier emits when a pinned locator resolves, under its own law head, to a clause whose SAID is not the one the record also carries. The check is mechanical, and a record that files it as a digest mismatch is unauditable in the way this rule exists to prevent.

## Repair 3 — which identity a citation carries

The rule, and the seed's centerpiece, because it is what an implementer will otherwise get wrong:

> **Evidence cites bytes; law cites provisions.** Where a citation must be immune to amendment it SHALL name a SAID. Where a citation must survive amendment it SHALL name a locator. Where a record is simultaneously an immutable fact and an instruction to a party, it SHALL carry both.

Applied to the ratified sites:

| Site | Carries | Why |
|---|---|---|
| A finding's ground, bundle, lens, law head | SAID | A finding is an immutable fact of a closed triple (L1611–1614); if its ground named provisions, a later amendment would retroactively change what it stood on |
| §8.3 defeated payload (L1641–1646) | Both | The SAID makes replay exact; the locator lets the defeated party find the provision and argue about its current form |
| §8.3 pending requirement set (L1647–1658) | Both | The citing-clause list is a record *and* a cure instruction; a party told to satisfy a rule must be able to read it |
| §10 covenant seal's clause set (L2041–2045) | Locator | The promise is meant to survive amendment (L2033–2034); a seal over digests is a digest seal (L2040–2041) |
| A clause citing another clause | Locator, unpinned | Intra-corpus, and it should track amendment — as Akoma Ntoso puts it, acts referring to other acts do so regardless of version |
| An enactment amending law | Locator + prior-version SAID | The target provision plus the version being amended, so supersession is derived rather than declared |

That last row is Utah's bill header, which pins both: *AMENDS: 36-12-12, as last amended by Chapter 55, Laws of Utah 1993.* The form is a century old and it is the payload the **superseded** defeater class has been missing.

## Repair 4 — what a domain owes

**At §15 or §18**, wherever domain obligations sit. Custos fixes this grammar for itself; a domain conforms by satisfying the properties, not by copying the punctuation.

> A domain's law SHALL identify each provision by a locator assigned before its bytes are digested, carried inside the SAID preimage, never reused within the lineage, and admitting a total order any verifier computes identically. A domain SHOULD spell locators as this document does.

Properties are interop and bind; spelling is style and does not. A domain whose corpus is already numbered — and any domain consuming existing statutory law will be — conforms without renumbering anything. This is also what makes §10's chartered-out "portable clause language" honest: the portable part is the property set.

## Notes for the drafting authority

**A ruling is owed.** This seed inverts the usual order — it was reached by design discussion rather than by a gauntlet pass. Finding #85 was filed afterwards, against the three spans named in *The defect* rather than against the proposal, but no ruling has executed and one is needed before this can enter.

**What this seed no longer carries, and where it went.** An earlier draft bundled the carriage work in here. It is out, in three pieces. One line per block is finding #90 and its own seed, because a reflow is provable where this scheme is argued. The locator's own carriage — the bracketed token, and dropping markdown bullets from normative text so the locator carries the enumeration — is offered separately and held, because assigning permanent names to strata the clean-root decision may excise pays the whole cost of permanence for none of the benefit. `<dfn>` for defining instances is withdrawn until a term test exists: marking up whatever currently looks like a term would canonize the unearned coinages and make them harder to retire. What remains here is one normative object and should not be split further — a locator with no pinning rule does not travel, and a pinning rule with no citation discipline does not tell an implementer what to do.

**Two consequences this seed raises and does not settle.** First, §8.3's canonical selection (L1767–1769) currently takes a lexicographic minimum over a digest, which is deterministic but picks an arbitrary member of the available defeats; ordering by locator instead would select the earliest or most specific provision, which is a rule defensible to the party it defeats. That is a change of behaviour, not of notation, and it wants its own ruling. Second, the subcode at L1776–1779 is a clause-internal enumeration that locators may subsume entirely — if a clause's parts have locators, the subcode is a locator suffix, and the "where the clause defines none" branch disappears.

**§7 gains something for free.** The aggregate Constitution's per-clause sub-blocks are SAID-addressed (L1483–1485). Carrying the locator inside each sub-block upgrades what clause-selective disclosure proves: today revealing a clause against the aggregate "proves only that the clause was committed somewhere, never its membership in the law in force" (L1490–1492), and the aggregate fixes membership while the locator fixes position. A clause disclosed alone is then self-resolving, which is also why relative citation was considered and rejected — resolving a relative form requires structure the disclosure posture does not supply.

**This seed costs no citations.** Nothing here reflows or relabels anything, so no existing line citation is disturbed by it. That cost belongs to #90's seed, which states it.

## Record

| Fact | Value |
|---|---|
| Predecessor edition | Custos 4.2, sha256 `68cc5c9b7164b33dffcf7b705a0d1301fe108c647d35638fec61d52d29b2775a` |
| Executed under | No numbered ruling; one is owed (a §5 definition and a §4 reading rule are ruling-grade) |
| Finding discharged | #85 (law has one identity where three ratified spans need two) |
| Spans repaired | §5 law ladder L1195–1212 (addition); §4 reading rule 2 L993+ (extension); §8.3 payloads L1641–1658; §8.3 canonical selection L1767–1779; §10 sealed set L2041–2045; §10 conviction family L2049–2052 |
| Separated out | One line per block → #90 and its own seed; locator carriage → offered separately and held; `<dfn>` → withdrawn pending a term test |
| External citations verified | 2026-08-26 — Akoma Ntoso Naming Convention v1.0, OASIS Standard 2019-02-21, `https://docs.oasis-open.org/legaldocml/akn-nc/v1.0/akn-nc-v1.0.html`; Utah Code structure and amendatory bill form against the `bakobo/utah-id-law` corpus |
| Adjacent seed | Covenant seal carriage (finding #80) — repairs where the seal's kind is written; this repairs how its clause set is named. Neither depends on the other |
| Charter input, not designed here | The rendered-anchor transform and its id mangling |
| Re-ruling | No |
| Ratified bytes altered | None |
