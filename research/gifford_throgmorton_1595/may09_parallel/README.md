# Two words in the Cotton copy of the 9 May 1595 Gifford letter

The alphabet marked 2 gives **SOME** and **ALL** at the positions where the Cotton copy reads *some* and *all*. Four of five eligible groups could be located by the pre-specified surrounding prose. The comparison scored two distinct exact words totalling seven letters. The success threshold required three words and twelve letters, as well as a score above all 1,000 shuffled keys. The highest control scored one. **The aggregate result is a miss.** [May 9 original, SP 12/252 f. 19r](https://link.gale.com/apps/doc/MC4304480214/SPOL) · [Cotton Caligula B VIII, f. 329r–v, Gale openings 333–334](https://link.gale.com/apps/doc/MC4318883115/SPOL)

| Original group | Agreed ciphertext | June row 2 | Cotton word | Folio, reader’s line, body token | Outcome |
|---|---|---|---|---|---|
| T02 | WRPH2 | SOME | some | 329r, 2, 23 | Exact |
| T04 | DOO2 | ALL | all | 329r, 3, 28 | Exact |
| M04 | WMX2 | SIT | — | — | No qualifying anchor |
| M12 | WHQXH2 | SENTE | sent | 329r, 24, 264 | Mismatch |
| M13 | ZYHV2 | WVER | over | 329r, 24, 265 | Mismatch |

The Cotton reader transcribed “and some / soch, had vndone them all and truly” across lines 2–3. Line 24 has “were sent over of purpose to”. Final *e* was scored, and only case, I/J and U/V were normalized. For M04 the locator required *in 102* followed by *with Sir 72*. Cotton line 21 has *si 72* in the corresponding stretch. Resemblance to the output could not supply the missing anchor. Of 1,000 shared permutations of the 24 output letters, 997 scored zero and three scored one. [Registered scoring and alignment rules](registered_plan.md)

Two earlier readers transcribed 34 cipher groups independently. Ten groups gave complete agreed ink ending in 2. T08 was the only word in the original gloss test, which scored 0/1. The previously recognized Captain White passage also excluded T09 and T10. Two more agreements, M10 and M15, covered only the ends of longer groups. The other 24 positions had disagreement, unresolved ink or a missing selector. [May ciphertext readings](../may09/) · [Historical alphabet](../june/alphabet.tsv)

**Order of work.** This is an exploratory comparison prompted by recognizing the historical May copy. The five mechanical predictions were written before the comparison plan was hashed. The investigator had seen the original interlinear annotations and knew the June alphabet. A separate reader transcribed the Cotton leaves without seeing any predictions. Their recto and verso readings were sealed at 22:37:01 and 22:38:54 UTC on 20 November 2026. The investigator froze the plan, the predictions and the scorer at 22:39:30 UTC before receiving the independent readings. The existing numerals and the previously identified passage supplied historical context and earned no points.

From this folder, `python3 -I replay.py` reconstructs the five predictions from both May readings and the June alphabet, then checks the outcome table and every control against their recorded SHA-256 digests. Add `--output <new-directory>` to save both TSVs. It uses the four located words and the one leave-out in the witness slot table. The frozen manifest, scorer, predictions, eligibility ledger and the full Cotton transcription it was scored against are in [frozen/](frozen/README.md); `python3 -I -B frozen/replay_registered.py` checks their hashes and reruns the registered scorer. The complete reference used by the registered scorer had SHA-256 `9ad617375420ceb526d90850339932370caf5d4e6751b7731bb882e62f99aaf6`. [Replay](replay.py) · [Reference positions](witness_slots.tsv)

AI agents did this work; no person has checked it.
