# Catalogue 2356: Spanish officer to Ottavio Piccolomini, camp in the Wetterau, 12 August 1646 (inv. 25071)

WAINUT, 12 Nov 2026. Work done with AI language-model agents viewing the photographs, and checked by script as
described below. No human palaeographer has checked the text. An independent AI language-model agent that took no part
in the solution reviewed it blind on 12 Nov 2026 (see "Independent review" below).

## Result in one paragraph

The cipher is a homophonic substitution in two-figure groups (two to four groups for most letters, in alphabetical
runs), with code groups for names. The writer used two tables in 1646: an earlier one on inv. 25063 and 25065
(e.g. o = 20/61/70, s = 24/74) and a second one on inv. 25067, 25069 and the bare 25071 (e.g. no = 41 43 or 42 16,
de = 12 15). The key of the second table was rebuilt from the contemporary interlinear glosses of 25067 (32 glossed
words and phrases, `pairs.tsv`, all decrypting to their gloss with the frozen key), frozen, and tested on held-out
glossed words of 25069: **10 words, 9 letter for letter with the gloss; the tenth (recolegida) has one group (93) not
in the key, the other 9 of its groups agree; 62 of 63 held-out groups give the gloss letter.** The frozen key,
unchanged, reads the bare letter 25071: **read in part, 38 of 42 cipher words verbatim from the signs (90.5%;
35 of 39 = 89.7% without the 3 code groups); 2 words with a doubtful sign (one under an ink blot, one of doubtful
shape), 2 with a marked repair; no guesses, no holes.** Dan's reading checker on the Spanish running text:
clean-sentence share 0.688 (11 of 16 sentences), coverage 0.827, hole rate 0.104; the "holes" are lexicon misses on
17th-century spelling (havra, offrece, havia, aora, dexar, deve, socorer). On a human reading all 16 sentences hold.

## Document

| inv. | date | cipher | status |
|---|---|---|---|
| 25071 | "Del Campo a Ilenstatt [?] y 12 de Agosto 1646" | 15 lines, 216 two-figure groups, 42 cipher words | **read in part**: 38 verbatim (90.5%), 2 doubtful signs, 2 marked repairs, no holes |

Bare: no gloss over or beside the cipher. Original: SOA Zámrsk, Rodinný archiv Piccolominiů (Náchod), inv. č. 25071
(microfilm label "31/2"). Image: photograph of the microfilm frame in the appendix of Václav Vlnas, *Počítačová
analýza šifrované korespondence rodu Piccolomini* (BA thesis, Univerzita Hradec Králové 2017, theses.cz/id/p3p2kb):
appendix zip P_lohy_A_a_B.zip, frame 25071.jpg. Key frames of the same zip: 25067.jpg, 25067_1.jpg (key), 25069.jpg
(held-out). The photographs are rotated 90 degrees and soft; clean scans would have to be ordered from SOA Zámrsk
(not done). No images are in this folder for git.

**Place and writer.** The catalogue entry gives "Del Campo a Franckental"; the date line on the frame reads "Del
Campo a Ilenstatt" (or Ilonstatt), most likely Ilbenstadt in the Wetterau, where the imperial-Bavarian army stood in
August 1646. The text (Giessen, the Main, Turenne joining the Swedes, the Prince of Darmstadt) fits the Wetterau and
Upper Hesse, not the Palatinate. The writer signs in plain script "Joh: Behr [?] von ..." under "Su mas humilde y
obediente criado"; the name is not read further here. The slug `frankenthal1646` was set before the frame was read
and may need changing (e.g. `ilbenstadt1646`).

## System

Homophonic substitution, two-figure groups, letters in alphabetical runs (20 a, 25-27 a, 28-29 b, 30 e, 31-32 f,
33-34 g, 35 h, 37-39 i, 40 m, 41-42 n, 43-44 o, 45-46 p, 47 q, 49 r, 50-51 u/v, 54 x, 56 y, 58-59 z, 60 r, 61-62 s,
63-64 t) plus a second run (10-11 c, 12-13 d, 14-15 e, 16 o, 17 u/v, 18 y, 22-23 l, 24 m). Code groups written
apart, larger: 67 = Archiduque, 72 = Principe de Darmstadt (both glossed on 25067). Word gaps are not marked inside a
run. Full key: `key_frozen.tsv` (`key.tsv` is the same), with the gloss words that attest each group.

## Key source

- **Glossed pairs, `pairs.tsv`** (25067 and 25067_1): 32 rows, 229 groups; `scripts/check_pairs.py` decrypts each
  with the frozen key: all give their gloss. They attest 45 of the 47 letter groups and both code groups.
- Two groups are not attested by a gloss: **34** (g, from the order of the table, used once in 25071 for "Giesen")
  and **56** (y, a single group between the glossed words "lexos" and "temprano" on 25067_1; used once in 25071, "ny").
- The pairs were read from 1.9x crops with the gloss in view; they are a record for rechecking the key, not a blind
  copy.

## Held-out test

Frame 25069 (same writer and table, glossed) was not used to build the key; `key_frozen.tsv` was written before its
crops (work/h69_*) were made. Ten glossed words were transcribed by group (`heldout_25069.tsv`) and decrypted:
gente, esperar, ellos, antes, no, la gente, esparcida, no, aconsexable agree letter for letter; "recole[93]ida"
(gloss recolegida) has one group not in the key. 9 of 10 words, 62 of 63 groups. Small, and the gloss was visible.

## Reading

`transcription_25071.txt` (reconciled from `_pass1`, made before the key, and `_pass2`, made after the key was
frozen; see the review below on what that means), `decryption_25071.txt`
(mechanical), `reading_25071.md` (marked), `translation_25071.md`. `scripts/check_marks.py` rebuilds the decryption
from transcription + key and fails on any unmarked departure: PASS (12 Nov 2026).

Word counts (42 cipher words, code groups counted as words): 38 verbatim from the signs; 2 with a doubtful sign
(aquel, a figure under an ink blot; desarmarse, group 61 of doubtful shape, possibly 51); 2 with a marked repair (cath{+e}gorica; o{u/y} "oy", the group read 50 or 56);
0 from a gloss only; 0 holes. The writer's spellings socorer, socorerle and ny are kept as written.

Content: the army will not seek out the enemy or risk battle unless the enemy attacks Giessen, which must then be
relieved; the Prince of Darmstadt must not be abandoned. Turenne has joined the Swedes, who summoned the Prince to
declare himself and disarm or be attacked, on Queen Christina's orders; he refused and will defend himself. The
Archduke has promised to relieve him in any case.

## Statistical validation

`docs/_validate.py` on `validation.tsv` (the 216 groups with the values the reading gives them, doubtful groups as
read; 12 Nov 2026, model es-golden-age, order 4): reading -2.258 per letter; 200 random keys of the same structure
-4.687 (sd 0.303, z 8.0); a key annealed onto the shuffled ciphertext at best -2.731 (mean -2.779, z 8.8); the
annealer on the real text from random keys -2.442. Verdict: pass. 216 tokens on 43 types is short, and the key came
from glosses, not from this test.

## Prior art (checked 12 Nov 2026)

- Catalogue entry 2356 and the sweep notes (`research/sweep_2026-11_czech_chrome/`): bare, not deciphered; Vlnas 2017
  lists the frame in appendix B as not deciphered.
- Dan's repo (origin/main 54c4ecc65 and the log to 12 Nov): no target, PR or issue for 25071, Frankenthal or
  Piccolomini beyond the merged claudiamedici1646 (#302), piccolomini1646 (#303, #310). No collision.
- Web: the solving round ran no web search. The independent reviewer ran one quick search (12 Nov 2026): no edition
  or decipherment of 25071. It turned up Thomas Ernst's work on the "zifra picolominea" (MIÖG 129; scienceblogs.de,
  7 Oct 2017), on Piccolomini's own cipher, and a HistoCrypt paper (ecp.ep.liu.se/index.php/histocrypt/article/
  download/693/599). That paper was opened on 12 Nov 2026: it is Dinnissen and Araújo, on the captured cipher letters
  of a Portuguese spy in Recife (1646), and does not treat this writer, this table or the Rhine campaign. Ernst's papers were not opened. Open as far as checked.

## Independent review (12 Nov 2026)

A separate AI language-model agent that took no part in the solution reviewed the folder blind (a model reading, not
a person). It cut its own crops and copied 69 groups on 6 runs before it opened the transcription: 68 agree, 1 is
doubtful on the image (L09, third group of "desarmarse": 61, or 31 or 51). It rebuilt the decryption, checked every
cipher word by hand against the key, and read the Spanish against the translation sentence by sentence: all 16
sentences hold. It agreed the state **read in part** and gave grade **B**: three words rest on a doubtful sign or an
inferred value (aquel, oy, Giesen) and the held-out test is small. Changes made after the review: L09 group 61 is now
`61?` in the transcription and "de{?s}arm-arse" a doubtful word (verbatim 39 to 38); "seek him" in the translation
now reads "seek the enemy". The review also noted that pass 2 was made after the key was frozen
(`key_frozen.tsv` 01:23, pass 2 01:25), against the brief: of its four changes, three do not depend on the key (L09
re-segmented from 21 to 20 figures, confirmed blind by the reviewer; `30?`; `50/56`); the fourth, 51 to 61 in L09, does,
and is the group now marked doubtful.

## Remaining gaps

- L05 "aquel" - blocker: illegible; the fourth group is under an ink blot (only "3" is clear); a clean scan
  from SOA Zámrsk would settle it (not ordered).
- L09 "desarmarse" - blocker: illegible; the third group is 61 (s) or 51 (u, "deuarmarse"); its first figure is
  crossed by a stroke from the line above. Marked doubtful; a clean scan would settle it.
- L13 "oy" - blocker: illegible; the second figure of the group after "aviso" is 0 or 6; read 56 (y) for the
  sense, marked repair.
- L09 "cathgorica" - blocker: needs-physical-access; the signs give no e between h and g; one letter added in the
  reading (marked repair); a clean scan would show whether the writer slipped or a group was missed.
- Group 34 (g, "Giesen") - blocker: too-short; not glossed in the worked text of 25067 and 25069; its value rests on
  the table order and the sense. The further glossed pages 25067_2 and 25069_1 may attest it and were not worked.
- Group 93 (held-out, 25069) - blocker: too-short; one occurrence, not in the key; probably a further g homophone or
  a slip for 33.
- Held-out test - blocker: too-short; 10 words, gloss visible on the crops, the freeze rests on file order only; a
  larger held-out set would need the unworked glossed pages 25067_2 and 25069_1.
- Place and writer - blocker: needs-physical-access; the date line reads "Ilenstatt" (probably Ilbenstadt,
  Wetterau), not Frankenthal as the catalogue has it, and the signature "Joh: Behr [?] von ..." is not read. The slug
  `frankenthal1646` follows the catalogue; the reviewer agrees it should be raised or renamed (e.g. `ilbenstadt1646`).
- Human check - blocker: needs-physical-access; no human palaeographer has checked any sign.

Not part of this target: the writer's earlier table (25063, 25065) and the troop list 25026 were not worked.

## Escalation

- [x] siblings: the glossed letters 25067 and 25069 of the same writer, table and year gave the key and the
  held-out test; 25063 and 25065 checked and found to use an earlier table
- [x] clear-pages: the contemporary interlinear decipherments on 25067 and 25069 used (pairs.tsv, heldout_25069.tsv)
- [x] known-keys: Vlnas 2017 lists 25071 as not deciphered and gives no key for this table; the claudiamedici1646 and
  piccolomini1646 keys are other tables
- [x] print: catalogue and sweep notes, Vlnas 2017, one web search (12 Nov 2026), the HistoCrypt paper opened; no
  edition found
- [x] key-rebuild: every group of 25071 has a value; 34 and 56 from table order and context, not from a gloss
- [x] retry: every doubtful group retried on 3-4x crops by the solver and again blind by the reviewer (aquel,
  desarmarse and oy stay doubtful and need a clean scan from SOA Zámrsk, not ordered); 25067_2 and 25069_1 would
  attest 34 and enlarge the held-out test
