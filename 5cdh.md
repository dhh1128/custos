# Plain-english legibility pass over the spec: cut jargon that isn't earning its keep
kind: debt
tags: legibility
created: 2026-08-26T18:34Z

- 2026-08-26T18:34Z Careful terminology is for rigorously delineated concepts. Where general-purpose language is already clear, a coined term costs the reader and buys nothing. Jargon is not a virtue.

Worked example — 'species'. spec/custos-4.2.md:1552 titles a section 'Pending species and cure'; the ratified block at :1558-1567 enumerates four: absent, window-open, unresolved-conflict, expired/abandoned. 'Species' is doing the work of 'kind'. The one distinction it must preserve is that these are NOT a fifth finding value (:1563 says so; :1876-1881 guards it) — and 'kinds of pending' carries that subordination at least as well, because it names what they are kinds OF.

Note the asymmetry in the same sentence: 'expired/abandoned' IS a real term and cannot be paraphrased — it is an enumerated value that :1585 SHALLs an implementation to carry. So the pass is not de-jargoning wholesale; it is separating terms that carry a definition from labels that carry only a register.

Cost to know before starting: 'species' appears three times inside RATIFIED text at :1558-1567, so replacing it is an amendment, not an edit. The pass should triage by that boundary — free edits in ordinary prose, priced ones in ratified blocks — and probably batch the ratified changes into one amendment.

Other candidates seen while reading §8 and §14, not yet audited: 'requirement space' and 'at birth' are both used normatively and neither is defined in §5 Definitions (:1043-1286). 'ground-evaporation' is named as load-bearing at :1701 and defined nowhere in 3,940 lines.

Origin: 2026-08-26, working issue 82 with Daniel. He could not read a rewritten version of his own issue because the terminology had been layered in without the concepts being delineated.
- 2026-08-26T18:36Z COLLISION (correctness, not just legibility): 'discharge' carries two near-opposite senses, three lines apart in the same section.

  Sense 1 — a requirement is SATISFIED. :177 'the typed requirement that would discharge it'; :1656 'The fold discharges everything the law commits'; :1667/:1668 'the requirement set discharges affirmatively / by defeat'; :1741. This is the dominant sense.
  Sense 2 — machinery LETS GO of what it held. :1562 'an operational processor has discharged its retained work'; :1565 'it supplies the committed ground for the discharge' (i.e. the eviction).

Fulfilled vs abandoned. Both live in section 8.2, and sense 2 is inside the ratified block at :1558-1567, so fixing it there is an amendment. Suggest reserving 'discharge' for sense 1 throughout and using 'evict'/'drop' for sense 2 — :1586-1590 already says 'silent disposal' and 'the drop', so the plainer word is in use nearby and reads fine.

Two more from the same pass:

  'operational processor' (:1558, :1562, ratified) is opaque enough that the spec glosses its own ratified text at :1569-1573 — 'a processor is whatever machinery retains work between appraisals.' A parenthetical translating a ratified paragraph is the strongest evidence in the document that this pass is needed. Plain reading: the part of an implementation that holds work it cannot finish yet (KERI: escrow).

  'appraisal' (30 uses) is a fair word for a real concept and should probably stay — but the actor is called an 'evaluator', so the act should likely be 'evaluation'. Appraisal/evaluator is a mismatched pair. Also: section 5 Definitions uses 'appraisal' inside the definitions of law head and lens without ever defining appraisal itself.
- 2026-08-26T18:44Z CORRECTION to the previous note's 'appraisal' item — that advice was wrong, do not act on it.

I wrote that 'appraisal' is undefined in section 5 and that it should probably be renamed to 'evaluation' for consistency with 'evaluator'. Both claims are wrong.

Appraisal IS defined, at :1162-1177, inside the bolded entry 'Evaluator; constructor': "'Appraisal' names the activity and the layer — the fold-plane act of computing findings from committed evidence... appraisal is the adjudicating domain's judging half, never its acting half."

Evaluator is the ROLE; appraisal is the ACTIVITY. The spec separates them deliberately and says so in the same entry. Renaming appraisal to evaluation would collapse a distinction the document draws on purpose — the exact failure mode this tick exists to prevent.

The real finding is smaller: 'Appraisal' has no bolded entry of its own, so it cannot be found by scanning section 5's term list, and a reader who scans rather than reads the 'Evaluator; constructor' entry end to end will conclude it is undefined. That is what happened to me. Fix is to give it its own entry, not to rename it.

Method lesson for whoever runs this pass, worth more than the item: a term can be defined inside another term's entry. Scanning bolded headings is not sufficient evidence that something is undefined — grep the prose before calling anything unearned jargon. 'requirement space', 'at birth' and 'ground-evaporation' from the earlier note were flagged by the same scan-based method and MUST be re-checked the same way before anyone acts on them.
- 2026-08-26T18:47Z 'Appraisal' should become 'evaluation' — this one is checked, unlike the retracted item above.

Section 1.3 makes 'evaluate' one of the two core verbs of the whole model. 'Evaluator' and 'evaluation' are then ordinary English morphology off that verb and need no coinage. 'Appraisal' breaks the chain for no gain:

  - No name collision blocks it. The 'evaluation seal' at :1252 is the DEFERRED fourth seal kind, is 'a committed verdict' (an artifact, not an act), and the entry says 'no construct in this document uses it'. The name is free — and 'evaluation seal' actually reads as a seal over an evaluation, which presupposes the proposed usage.
  - The layer claim is empty. The section 5 entry says appraisal 'names the activity and the layer', but the layer it points at is the fold plane, which is already called the fold plane. Appraisal is only what happens there.
  - The one real distinction available is not held. If 'appraisal' meant the domain's judging OFFICE and 'evaluation' one instance, the pair would earn its keep. But 'appraisal position' (:1150, :1614) is a coordinate of a single act — instance grain. The spec uses the word at both grains, so whichever reading you take, some usage is wrong.

Related, and separable: the section 5 entry titled 'Evaluator; constructor' (:1162-1177) does not really define two words — it defines a BOUNDARY (constructor vs evaluator, the KERI controller/validator lineage, refuse-don't-legislate). That content is load-bearing and should stay; only the framing misleads. Retitle to name the separation, and give 'evaluation' its own short entry.

Scope note: ~30 uses of appraisal/appraise, and the phrase 'appraisal position' is a named member of the triple, so this rename touches the spec's most-cited vocabulary and every downstream citation of it (utina, review corpus). Not a free edit — but not a ratified-text edit either, unlike 'species' and the sense-2 'discharge'.
- 2026-08-26T18:51Z 'typed requirement set' — the adjective is redundant AND applied inconsistently.

:1647 SHALLs the four fields (requirement kind, subject identifier, citing clauses, discharge species), so a conforming requirement set cannot be untyped. There is no untyped variety anywhere in the document. The adjective distinguishes nothing.

The inconsistency is the sharper problem. Roughly half and half:
  typed: :1434, :1524, :1647, :3022
  bare:  :1667, :1668, :1968, :2411
The SHALL at :1647 says 'typed'; the transition table at :1667-1668, twenty lines later, says bare. Same object, same section, two names — which invites a reader to think the bare ones are a different thing.

Fix: drop the adjective everywhere, keep the SHALL that makes it true.

CAUTION for whoever runs this — do NOT blanket-replace 'typed'. It has a second, load-bearing use as a VERB meaning 'its type is determined by': ':1619 the bundle is typed by the law head', and :599, :782, :1421, :1583. That usage is a real claim and must stay. Only the decorative adjective goes.

Unaudited neighbours of the same shape, flagged not concluded: 'typed evidence' (:1541, :2521, :2537, :3832), 'typed seal' (:1995, :2018, :3215, :3842), 'typed slot' (:1958). Each needs the same test — is there an untyped counterpart in the document? — before anyone touches it. Do not assume they pattern with requirement set.
