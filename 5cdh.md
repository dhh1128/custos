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
