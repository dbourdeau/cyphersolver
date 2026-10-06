# Matignon's Cipher-3, BnF fr. 15572 f. 276 (1586): read

Catalogue item 12, the Cipher-3 leaf. `../NOTES.md` listed it as "blocker: not-attempted; not transcribed" (coverage
table: 0 / ~27 lines). This contribution is dated 6 Oct 2026.

**Result: f. 276 read.**
- **Two independent reads agree.** Two sign-by-sign readings, made separately, agree on 693 of 739 signs (93.8%,
  `scripts/compare_reads.py`).
- **Coverage.** 473 of 737 signs (64.2%) are read under this target's coverage rule (`scripts/measure.py`). The
  scrambled-key floor is ≤ 3.1%.
- **The rule is strict here.** The lexicon is modern French, while the letter uses 16th-century spellings
  (*doibuent, preiudice, escriuent, neaulmoins*). Read the 64% as a lower bound. The open spans are listed at the end.

The leaf is Gallica `btv1b9061879d`, canvas 285 (right page). It is a small slip of **22** cipher lines. The
coverage table's "~27" was an estimate. Images are not included.

## Clear text (16th-c. spelling; word division and punctuation ours; […] unread, [?] doubtful)

> La Guiolle est en doubte du Puy pour les amis de La Roussiere, [qui] sont en grand nombre avec luy, dont il y en a
> qui veullent mal a Polidor. La Saussaie a soing de qu[…] a secouru de ce qu'il a peu vos amis de la Madeleyne. [Ils]
> font courir le bruit que la Chambre et frere de la Mare ont aussi bonne intelligence qu'ils l'eurent iamais, et se
> doibuent bientost assembler au preiudice de Front[enay?]. Le procureur et son fils ont promis Aubois le remettre en
> possession du prieuré, ce que La Saussaie ne peult croire, encor qu'ils se escriuent, s'en asseurant que les sieurs
> de la Fontaine, la Chaie et Mirebeau et son procureur, ausquels il se fie, ne voudroient permettre mesmes en temps
> de […] qu'il feust depossedé du prieuré; et surtout il supplie que le Bois et l[…] aient que de se mesler ensemble
> […]. Le Puy est ennuyé de la guerre, et neaulmoins redoute la […]; quelque chose qu'il se face, il est besoing de
> le bien de maistre Iehan Durant, soit paix ou guerre, que l'on esloigne la Mar[e?], car c'est le logis que desirent
> les amis de la Mare et de la Roussiere.

**English, loosely.**
- **Factions.** La Guiolle is unsure of Le Puy because of La Roussière's friends, who are many, and some of whom wish
  Polidor harm.
- **La Saussaie.** He has taken care of […], and has helped your friends at la Madeleine as far as he could.
- **Rumour.** They are spreading word that la Chambre and la Mare's brother are as thick as ever, and will soon gather
  to the prejudice of Frontenay[?].
- **The priory.** The procureur and his son have promised Aubois to restore him to the priory. La Saussaie cannot
  believe it, even though they write to each other. He trusts that the sieurs de la Fontaine, la Chaie, Mirebeau and
  his procureur would not allow him to be dispossessed, even in time of […].
- **A request.** Above all he begs that le Bois and l[…] have nothing to do with each other […].
- **Le Puy.** He is tired of the war, yet fears […]. Whatever he does, for maistre Iehan Durant's good, in peace or
  war, la Mare should be kept away: "car c'est le logis que desirent les amis de la Mare et de la Roussiere".

**Context.** A Poitou intelligence note among the Catholic factions round La Roussière, Henri III's governor of
Fontenay(-le-Comte) 1582–87. He surrendered the town to Navarre on 1 June 1587.

## Key

S. Tomokiyo's partial Cipher-3 table (cryptiana, *Henry III's Cipher with Ambassadors*). It is a homophonic letter
substitution with word signs:
- 60 *faire*, a β-like sign *de*, 20 *la*, 18 *le*, p-with-stroke *pour*, C with n *que*, ∴ *qui*;
- v is a null.

**Checked on the deciphered sibling ff. 277r–278r → 279r–280r.** We blind-transcribed the 37 cipher lines of f. 277r
by shape only: the transcriber never saw values (`crib/BRIEF_transcriber.md`, `crib/f277r_all.txt`). A hard-EM
alignment then matched that transcription to the contemporary decipherment (`crib/plain_all.txt`):

```
python scripts/align_em.py --cipher crib/f277r_all.txt --plain crib/plain_all.txt --iters 10
```

- **Overall.** 1,271 signs align to letters and 55 word signs to their words. The table's value is the top emission
  for every frequent sign column; examples follow.

  | sign column | table value | aligned as |
  |---|---|---|
  | C05r1 | e | e 106 of 149 |
  | C16r1 | r | r 49 / 65 |
  | C17r1 | s | s 40 / 48 |
  | C19r2 | u | u 37 / 41 |
  | W02 | de | *de* 26 / 31 |
  | W03 | la | *la* 13 / 15 |

- **Agreement with the table.** 58% of all aligned events carry exactly the table value. The rest are mostly
  transcription noise between similar rows (the blind transcriber's row ids are inconsistent), not key errors.

**Additions to the table, found on f. 276 and checked on the image:**
- **`###`** (three crossed strokes) = **et**.
  - It occurs 8 times, always between words, and "et" fits every place: *la Chambre et frere*, *le procureur et son
    fils*, *la Chaie et Mirebeau et son procureur*, *prieuré et surtout*, *guerre et neaulmoins*, *la Mare et de la
    Roussiere*.
  - Tomokiyo has a # in his r column, which this leaf does not support.
- **Split columns:** ζ (z-topped hook) = i but ɤ (reversed hook) = o; ꝫ (9 with a bar) = u but ʒ (closed 9) = t.
- **Other signs:** a small o with a diagonal tail = y; the crossed-A / ※ sign = i (L04, L16).
- **The f column's ∂ is f**, not o: *de Front…* in L08, against δ = o elsewhere.

## Method

1. **Line crops.** The slip was deskewed (−5.25°). We cut 22 lines at a 134-px pitch into three overlapping crops
   each.
2. **Read 1 and read 2.** Read 1 was done by hand for L01–02 and by two agents for L03–22. Read 2 was done by a third
   agent that never saw read 1.
   - Both used `BRIEF_reader.md`: the table, sign conventions verified on this hand, and the L01–02 worked example,
     which matches Tomokiyo's published opening.
   - Output is one letter per sign, with no smoothing into French.
   - Files: `read1.txt`, `read2.txt`.
3. **Comparing the reads.** `scripts/compare_reads.py` gives the letter-level agreement and lists every disagreeing
   span (44). We checked the spans that change the sense against the deskewed image:
   - *et* (8 places);
   - *sont en grand nombre* (y = n), not *et grand*;
   - L03–04 *a soing de* (hook = o, ※ = i, y = n, 23 = g);
   - L08 *Front…* (∂ f, ⊥ r, hooked o, y n, a t, then null v and *que*).

## Checks (`scripts/`, standalone, Python 3)

| check | real key | shuffled keys |
|---|---|---|
| `measure.py read1.txt 20`: signs read (the `../measure.py` rule: run of ≥ 3 lexicon words, ≥ 10 letters) | **64.2%** (read 2: 51.7%) | median 0.7%, max 3.1% |
| `control_shuffle.py read1.txt 50`: letters inside lexicon words of ≥ 3 letters | **62.9%** (read 2: 53.7%) | median 7.3%, max 17.2% |
| `compare_reads.py read1.txt read2.txt`: two independent reads | **93.8%** of signs agree | – |

The shuffles permute the letter values among the signs. The word signs stay as they are, which is conservative.

**External agreement:**
- **Tomokiyo's opening.** The L01–02 opening matches his published opening (*La Guiolle est en doubte du pu pour
  les amis de la Roussiere…*).
- **Interlinear glosses.** The contemporary glosses over L11 and L13 agree where they are legible.
- **People and places.**
  - La Roussière was governor of Fontenay.
  - Frontenay (Frontenay-Rohan-Rohan, near Niort) and Mirebeau are Poitou places.
  - La Saussaie, la Mare, Aubois, La Guiolle, la Chaie, Polidor and Iehan Durant were not found online. They are
    presumably local gentry and officers, for the Vendée or Deux-Sèvres archives or the *Archives historiques du
    Poitou*.

## Open

- **Lines with doubtful spans:**
  - L04: a blot after *qu*;
  - L14: *en temps de* [one sign not in the table: a C with o inside; context wants *paix* or *guerre*];
  - L16: *et l[…] aient*, and the end of the line;
  - L18: *redoute la ?euel*;
  - L20: *la Mar[e?]*, or Mareuil;
  - L22: the closing flourish.
- **Next target:** fr. 15571 f. 179, the other Cipher-3 leaf. The same table and conventions should read it, and
  Tomokiyo's image carries an interlinear decipherment to check against.

## Files

- **Root:**
  - `read1.txt`, `read2.txt`: the two sign-by-sign readings, one letter per sign.
  - `BRIEF_reader.md`: the brief both reads used.
- **`crib/`:**
  - `f277r_all.txt`: value-blind transcription of f. 277r.
  - `plain_all.txt`: ff. 279r–280r transcribed.
  - `key_em_all.tsv`: the alignment's key.
  - `chart_values.tsv`: the chart-id → value map, which the transcriber never saw.
  - `BRIEF_transcriber.md`.
- **`scripts/`:**
  - `align_em.py`, `compare_reads.py`, `measure.py`, `control_shuffle.py`;
  - `segment.py`: lexicon Viterbi, shared with the `dinteville1592` contribution.
- **`data/`:** `fr_words.tsv`, the lexicon.
