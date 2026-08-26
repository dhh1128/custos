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
