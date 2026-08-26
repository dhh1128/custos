# Custos: law you can replay

Two players finish a chess game and go home. A year later a
stranger picks up the scoresheet and replays the moves. She reaches
the same board they did — not a similar board, the same one — and
she can check whether 34. Bxf7 was legal, because the rules were
fixed before the move was played and she holds them too. Nobody
testifies. The record is enough.

KERI delivers that for key state. A KEL folds identically for every
honest validator, and a forked log convicts its author for anyone
holding the pair. Then KERI stops, on purpose: an honest validator
must not trust duplicitous key state — and nothing follows.
Detection, no consequence.

That is the right place for a key management protocol to end and
the wrong place for a system to end. Everyone consuming key state
improvises what comes next: who was entitled to issue that
credential, which rules were in force when they did, what a relying
party owes once the evidence goes bad. Improvisation does not
compose.

Custos specifies the layer above that line and names the class it
defines: the GARD, a Governed Autonomic Replayable Domain. KERI
detects; a GARD adjudicates.

## Why the existing answers stop short

Governance frameworks carry real law. ICAO governs passports;
GLEIF's vLEI framework governs qualified issuers with published
criteria, annual requalification, and revocation that bites. What
prose cannot do is answer a stranger by computation: "was this
issuance proper under the law as it stood in March?" is a records
request. Prose law is read; committed law is replayed.

Blockchains supply the two things prose lacks — a total order over
rule changes and the acts they judge, and a completeness surface,
so a verifier knows it holds the whole rule set rather than the
fragment someone showed it. But governance then sits hostage to a
validator set the domain does not control, and block time displaces
the domain's own first-seen coordinate. A domain escapes its
regulator's mandate and acquires its validators'.

Underneath both failures sits one asymmetry. Integrity is
self-certifying; authority is not. A SAID is its own proof, but a
digest cannot tell you its issuer was entitled to assert a rule,
and no per-artifact mechanism can tell you that you have seen all
the rules. Completeness is a claim about a rule set, never about
one artifact, and a rule set needs a place where it is enumerable.

## The one move: a third log, a third fold

KERI already solved this shape twice. Keys get a log, the KEL, and
a fold, the Kever. Credentials get a log, the TEL, and a fold, the
Tever. Fold is Custos's word rather than KERI's, and it means what
`functools.reduce` means: walk a log's committed events in order
and accumulate the state they imply. Custos adds the third rung:
law gets the GEL, a governance event log, and the Gever that folds
it. GEL events seal into the
domain's KEL by the same anchoring discipline TELs already use — no
new wire pattern, nothing an existing verifier cannot parse. What
the KEL is to keys and the TEL is to credentials, the GEL is to
law.

A Constitution here is not a document; it is what the fold returns.
A ratified text is an event in the GEL, and the Constitution is the
computed state over all such events at a position. Two parties
holding identical committed inputs hold identical law by
computation, rather than by agreeing which PDF is current.

## The one discontinuity

Back to the board. FIDE fixes the rules of chess, and no move
amends them. That is the Kever and the Tever: their transition
rules are constants of the protocol. The Gever is the first fold
whose transition rule is committed data — the law it folds under
lives in the log it reads, enacted and amendable by the domain it
governs.

This sounds circular and is not, because it is positional. Law
never applies to itself at a coordinate, only to its successor at
the next. An amendment enters the GEL as an ordinary event, judged
under the law in force before it. Judgments after it fold under the
amended law, judgments before it under the old, and both stay
recomputable forever. Succession is never retroactive.

The base case is constructed rather than judged. A born-governed
domain computes its founding law first, seals that law's SAID into
its inception event, and takes the inception's self-addressed
prefix as its identifier — so the founding law lies inside the
bytes the identifier's digest ranges over, and the same keys under
a different founding law name a different domain. The law must not
mention the identifier; a reserved sentinel resolves at
verification, and that exclusion is what closes the cycle. A domain
may instead incept bare and anchor its law afterward: adopted
grade, lawful and confessedly weaker. GLEIF's root identifier is
adopted grade, exactly — the reading is worked out in the
[GLEIF EGF mapping](gleif-egf-mapping.md), not in the kernel.

## Seven primitives

Custos types the whole system in seven things, then binds itself to
a rule: every construct it introduces later must be stated as a
composition of those seven. A warranty is an enactment binding its
maker to a finding's ground. An organ is a seated constructor.
Federation is a relation between domains built from seals and
enactments. A section that needs an eighth primitive has found a
gap in the ontology, repairable only by amending the typing chapter
through succession. The seven are a budget, not a glossary.

Five are nouns.

A **log** is committed evidence — an append-only record, anchored so
that KERI proves both its integrity and its authorship. A log
asserts nothing; preserving is its entire office. A domain reads
three: the KEL for keys, the TEL for credentials, the GEL for law.

A **fold** is computed judgment: the pure function from a log's
committed bytes to the state they imply. Log and fold are one
structure read twice, and no fold ever writes.

A **finding** is what a fold returns — a judgment carrying the
ground that justifies it.

A **seal** is a commitment planted in a log, the instrument by which
one committed record binds itself to another. Three kinds carry the
standard. A digest seal commits to exact bytes. An event seal
commits to the event at a log coordinate. A covenant seal commits a
subject to the domain's standing law, so that a successor failing
the sealed clauses is convictable on the seal's own bytes. Seals are
how the GEL hangs off the KEL, and how a founding law gets inside
the identifier it will govern.

**Succession** is law changing by enactment inside the very log the
fold reads — the loop of the previous section, named as a primitive
because everything reflexive in the design is built from it.

Two are verbs, and no object performs both.

To **evaluate** is the fold's verb: read committed bytes, compute
state, return findings, refuse where no committed rule makes the
question evaluable. An evaluator holds no pen, and no degree of
conviction earns it one.

To **enact** is the constructor's verb: ratify law, seat an
authority, issue or revoke, commit an act. Every enactment is a
committed event, so a constructor cannot act except by producing the
evidence of its own act.

That is KERI's controller/validator division carried up one tier —
only a controller writes a KEL, any validator verifies it, and no
validator, however convinced, may write. In Python it is two
signatures that cannot be confused:

```python
def evaluate(evidence_bundle, law_head, position) -> Finding:
    """A fold. Pure: no clock, no config, no network, no operator
    discretion. Whatever is not an argument cannot influence the
    result; it returns having written nothing."""

def enact(act, signing_keys) -> Event:
    """A constructor. The side effect is the whole point: produce a
    committed event and append it to a log. It judges nothing."""
```

Two evaluations of the same triple return equal findings — equal
under one conformance predicate, which is semantic full-payload
equality today and byte identity by construction the moment a
carriage encoding ratifies. That is the chess replayer's test,
applied to governance.

## One turn of the loop

The seven work in a cycle, and each pass leaves the record larger
than it found it.

1. Genesis (enact, seal, log). Someone writes a one-page rule-set,
   seals its SAID into an inception event, and the resulting prefix
   is the domain's identifier. One key state, one page of law, one
   log binding them.
2. Seating (enact). The domain seats an organ — an establishment act
   citing the clause that creates the role. The organ is now a
   constructor with a committed mandate.
3. Issuance (enact). The organ issues a credential. Registry state
   moves in a TEL, anchored to key state.
4. Question (evaluate). A stranger holding nothing but the logs asks
   whether that credential's holder may act in some role. The Gever
   folds the GEL, in the context of the KEL and TEL spans it cites,
   into the Constitution in force at that position, and returns a
   finding.
5. Consequence (enact). If the finding is terminal and adverse,
   someone acts on it: revoking the credential, unseating the organ.
   The act commits the finding that grounds it, so the consequence is
   checkable by the same replay that produced the judgment.
6. Amendment (enact, succession). The law itself changes. The
   amendment is an ordinary GEL event, judged under the law in force
   before it. Later folds run under the new text; earlier ones stay
   computable under the old.

Steps 5 and 6 both land in the GEL, which is the log step 4 reads.
That is what autonomic means here: the domain detects, judges, acts,
and files the act into the law it will be judged by next time, with
no external enforcer anywhere in the loop.

## What a fold returns

Take step 4's question — may this credential's holder act in role
Y? — and consider the four answers a fold can give. Each carries
its ground, and the ground is a component of the value rather than
an annotation on it. A bare verdict is not a member of the type.

- affirmed: the committed evidence discharges the clause. Its
  ground is the evidence bundle and the clause set it was appraised
  under.
- defeated: something committed defeats it. The credential was
  revoked, the issuer was never seated, a signature failed. Its
  ground is the citation of the defeating clause or superseding
  act, plus the defeat's class — crypto, authority, merit, or
  superseded. Where several defeats are available at once, the
  finding cites the lexicographic minimum, so two verifiers
  holding the same evidence emit the same defeat down to the byte.
- pending: the evidence so far neither affirms nor defeats. Its
  ground is a typed requirement set naming exactly what would
  settle it — this schema, from that issuer, not yet present.
  Pending is a cure path, not a shrug.
- self-convicted: the subject's own committed bytes contradict each
  other. Its ground is the proof — the contradictory pair. This one
  is terminal. The question is poisoned, and no later evidence
  rehabilitates it. At the key tier, whether a pair bears is decided
  by KERI's own superseding-recovery rules, and a lawfully
  superseding event reconciles rather than convicts.

The ground requirement is the load-bearing decision of the whole
design. Because every finding carries its ground, every finding is
checkable by replay; because every finding is checkable by replay,
judgment composes across parties that share evidence but share no
authority.

A fifth outcome is pointedly not a value. Where no committed rule
makes the question evaluable — a missing rule, not missing evidence
— the evaluator refuses, and the refusal is an operational fact
rather than a finding. An evaluator that invents an ordering to
avoid refusing has legislated, and one that legislates is a
constructor wearing the wrong name.

Transitions run only toward evidence growth. No backward edge
exists, so affirmed never becomes defeated; fresh defeating
evidence yields a new finding at a new position. Affirmed and
defeated are final except for one event: a contradictory pair
bearing on the same question moves either to self-convicted.

## Standing, and consequence that checks out

Registry state is evidence, standing is judgment, and the committed
covenant set is the function between them. A TEL says whether a
credential is issued or revoked. It never says whether the holder
may act. That answer exists only under a committed covenant naming
which schemas, from which registries, confer which powers. A
relying party that reads authority off the registry has skipped the
law and trusted the ledger.

Recourse is where a governed domain becomes autonomic. A grounded
enactment commits, inside its own bytes, the evidence bundle it
rests on, the law head it invokes, the position it speaks at, and
the terminal finding it claims — asserting that the fold over
exactly these inputs returns exactly this finding. Any holder of
the logs checks it twice: the ground replays, and the enactor held
the invoked power at that position. An enactment whose ground fails
replay is defeated on its own bytes, by a stranger, with citation.
Revocation stops being an event you observe and becomes a
computation you check.

## Many frames, no referee

Judgment never crosses a frame boundary; evidence does. When one
domain's act arrives at another, four steps run: authenticate and
resolve belong to the medium and compute identically everywhere,
while appraise and confer belong to the receiving domain alone,
under its own law. The same act is lawfully judged differently by
every frame that judges it, at the same time.

So there is no super-frame and no root registry. Domains compose
the way local charts compose an atlas. Consumption is unilateral: B
commits an event recognizing what of A's regime it consumes, and A
need not know of it. Federation is bilateral — two anchors in two
logs citing one shared rule object, either side exiting by its own
act. A joint multi-signature identifier would be simpler and is
rejected on principle: it manufactures an authority above both
parties.

Replay costs real cycles. Warranties amortize it: a signed
attestation that a finding was computed under a pinned lens. A
warranty is evidence about a judgment, never the judgment, and it
is replay-falsifiable by construction — one honest
verifier recomputing from committed bytes convicts the warrantor on
its own signature. Judgment stays cheap to verify because it is
expensive to fake.

## What it refuses to claim

The most instructive section of Custos 4.2 draws the boundary of
its own design. Seven commitments are fixed; the interior they
bound — evaluator scheduling, seating procedure, constructor
architecture — is confessed undesigned. Every executable claim was
exercised against one implementation at one pinned checkout, and
agreement between independent implementations is an open debt
stated on the record.

The repository holding the text says the same of itself: it is a
projection, never an authority, because which bytes are law is
computed from the governance log and never read off any mirror.

A standard whose central claim is replay would refute itself by
asking you to take anything on faith. So it hands you the move
list.
