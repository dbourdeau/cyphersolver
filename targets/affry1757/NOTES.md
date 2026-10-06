# d'Affry (The Hague) to Rouillé / Bernis, 1757-58: intercepted code letters

Status: read in part (5 Oct 2026: 0.82 of all code groups read as sense by measure_sense.py, 0.89 without R1071; the
21 Sept figure 0.86 counted groups that merely had a value; R1071 unread; write-up affry1757.html, 19 Sept 2026)

KHA The Hague, Prins Willem V, inv.nr. 192. DECODE R1052-R1076, R2067 (catalogue: d'Affry, 11 unsolved records).
Images (git-ignored, `img/`) and DECODE digit transcriptions (`decode/DOC_*.txt`) fetched 19 Sept 2026 with the
bordeaux cookie. `parse.py` reads the DOC files; `cipher_A.txt`, `cipher_B.txt`, `cipher_C.txt` hold the groups.

## Prior work

- DECODE marks R1052, R1053, R1062, R1063, R1066, R1069, R1075 "solved by Dutch codebreakers, solution on separate
  sheets". The sheets **are** among the DECODE images, as clear-text pages marked "gelcp[?] D'A. à R." with number
  and date (first missed here: they read like ordinary clear letters). Lyonet's decipherment pages: R1052 5506,
  R1053 5507-08, R1062 (see align/), R1063 (see align/), R1065 5566-68 + 5572 (cipher in numbered paragraphs P:1..),
  R1066 5578 (+5575), R1069 5589 + 5586, R1075 5604-05. Transcribed into `plain/R*.txt`.
- De Leeuw, *Cryptology and statecraft in the Dutch Republic* (thesis, UvA 2000), ch. on the Seven Years' War:
  Lyonet broke d'Affry's first code by June 1756, then "two more French ones, belonging to Bonnac and D'Affry";
  the French code used July 1757 - December 1758 "is not mentioned by Lyonet and Croiset, but was nevertheless
  solved"; d'Affry's code to Choiseul from Dec 1758 broken later.
- The contemporary decipherments survive as Nationaal Archief 1.01.50 (Stadhouderlijke Secretarie) inv. 221
  (d'Affry to R[ouillé], Dec 1755 - Jun 1757) and inv. 223 (d'Affry to B., Jul 1757 - Dec 1758), "grouped by the
  cipher used". Not digitised (empty scan ids, checked 19 Sept 2026).
- Bussemaker (ed.), 'Uittreksels uit de brieven van D'Affry aan de Fransche regeering (Dec 1755 - Mei 1762)',
  BMHG 27 (1906), DBNL `_bij005190601_01_0008`: Fruin's extracts from those decipherments, Dutch summaries with
  verbatim French sentences. Entries for 7 Jan, 1 Feb, 1 Apr, 19 Jul, 22 Jul 1757 match letters here.
  So the content of these letters was read in 1757 and summarised in print in 1906; the full text is not printed.

## Codes (group-frequency cosine between letters)

Revised: the Jan-Feb ("A") and Apr-Jul ("B") letters share their common values (de 219/1018/1138, la 583/382, que 197,
M 196, vous 569, il 1088, me 208, ne 134, faire 847, ma 6, ti 588, n 580...); the cosine split reflects homophone
habits, not two codes. `cipher_U.txt` holds both; `key_U.json` is the joint key. R1071 (C) is different.

Original split:

- **A** (Jan-Feb 1757, to Rouillé): R1052, 1053, 1062-1065, 1072, 1073, 1075, 1076. 5,011 groups, 777 distinct.
- **B** (17 Feb? / Apr 1757 - Jan 1758, to R. then "A à B" = Bernis): R1066, 1067, 1068, 1069, 1054, 1070, 1074
  (+ R2067, no transcription). 3,512 groups, 743 distinct. R1054's "to Bonnac" is DECODE reading "B"; the
  letter is Bussemaker's 19 July 1757 extract.
- **C**: R1071 (to Choiseul, 7 Aug 1757), 761 groups, unlike both.

Groups run 1-~1200; a word-and-syllable nomenclator (two-part or mostly unordered: frequent groups barely
cluster numerically).

## Code B: crib from Bussemaker's 19 July 1757 extract on R1054

The verbatim passage "Zoo het eerste het geval was, il me paroit qu'il seroit essentiel ... de la sagesse de leurs
règles" lies in R1054 positions ~200-370. Anchor: `800 698` (des précautions) at 264 and 277, 12 words apart in
the crib. See `key_B.json` for the growing key.

## Result (19 Sept 2026): key rebuilt from Lyonet's decipherments, the unread letters read

**Key.** Eight letters carry Lyonet's clear copy among the DECODE images (R1052, R1053, R1062, R1063, R1065, R1066,
R1069, R1075). Each clear copy was transcribed from the images (`plain/`) and aligned group by group with its
cipher (`align/*.tsv`, graded H/M/?; sub-agents, one letter each, cross-checked against each other). `merge.py`
votes `key_M.json` (651 groups; 56 left ambiguous in `amb_M.json`; `overrides.json` for corrections found in
reading). One code serves Jan 1757 - Jan 1758 (to Rouillé, then Bernis); only R1071 (to Stainville/Choiseul,
Vienna, 4/7 Aug 1757) is in a different code and stays unread.

**Readings** (`read/R*.md`, inferred values with evidence in `read/R*_new.tsv`, {braces} = inferred, [n] = open):

| Record | Date, no. | Read | Content |
|---|---|---|---|
| R1072 | 6 Jan 1757, 123 | ~65% in sense | "the Italian", a spy, offers to go to England and report on forces, cabinet, campaign plans; wants pay and a pension |
| R1076 | 7 Jan 1757, 124 | ~90% | convoy and escort after the storm; navy without land increase; herring; talk in Amsterdam |
| R1073 | 25 Jan 1757, 133 | ~90% | false rumour of a memorial on the augmentation; talk with the Grand Pensionary |
| R1064 | 1 Feb 1757, 136 | ~95% | States of Holland adjourned to the 20th; taxes for the augmentation; herring favour; spies (Quintin, La Combe) |
| R1067 | 1 Apr 1757, 161 | ~88% | Steyn embarrassed; the Gouvernante: "faut-il que ce soit moi qui favorise les moyens de faire du mal à mon père?"; Maastricht convoy; Wassenaer |
| R1068 | 26 Apr 1757, 172 | 56/60 groups | courier Vienna-London; Colloredo to d'Arenberg |
| R1054 | 19 Jul 1757 (to B.) | ~92% | Gouvernante's journey; ask for a declaration of the States-General; précautions of d'Estrées |
| R1070 | 22 Jul 1757, 210 (to B.) | ~95% | Gouvernante to speak to the States of Holland; Ostend and Nieuport; trade to Amsterdam and Rotterdam |
| R1074 | 17 Jan 1758, 283 | ~90% | French loan attempted in London; Macdonald (Bulkeley regiment) suspected |
| R2067 | 17 Jan 1758, 283 (to B.) | ~91% | cover letter to the loan extract: money operations in England useless; Englishmen and Spaniards passing; transcribed from the images here |
| R1071 | 4/7 Aug 1757 (to Stainville) | not read | different code |

**Checks.** Bussemaker's verbatim sentences recur group for group: 19 Jul (R1054, groups 145-351, four small
differences where Fruin abridged), 22 Jul (R1070), 1 Apr Wassenaer sentence (R1067 piece 7); Coquelle (1904)
quotes the Gouvernante's words to d'Affry from the Paris original, found in R1067. Bussemaker's Dutch summaries
of 7 Jan, 1 Feb, 1 Apr, 19 Jul and 22 Jul agree point by point.

**DECODE transcription slips** found on the way: in two hands a looped 8 was read as 0 (R1072, R1075, also R1064,
R1067: 056=856, 099=899 ...); groups run together (58291 = 582 91) or dropped; superscript corrections (8^578).
`view.py` splits merged groups; the reading agents re-parsed from the DOC files where needed.

**Open:** ~5-12% of groups per letter (listed as [n] in each reading), the weak stretches of R1072, R1071 entirely.

## Push towards 95% (5 Oct 2026): image re-transcription and a sense measure

**The old measure did not count sense.** The 0.86 of 21 Sept counted a group as read when it had any key or inferred
value, '?' values included, whatever the text around it said; by that rule the undeciphered letters now stand at 0.96.
It also ran on `cipher_U.txt`, the DECODE digits parsed by `parse.py`, which (a) keeps DECODE's 8-read-as-0 slips
(the reading agents corrected them only in their prose readings), and (b) drops every DECODE line that starts with a
paragraph tag (`<CLEARTEXT FR B:3.> 676 . 996 ...`): 7 lines of R1064 and 12 of R1065 were missing from the counts.

**New measure, `measure_sense.py`.** A group counts as read only if it has a value (key_M, H/M rows of read/*_new.tsv,
or `key_X.tsv`; '?' rows do not count) and the 9-group window round it scores as French under
`lang` model `fr-modern` (no spaces, per-char log-prob > -3.0) with at most one valueless group in the window. Proper
names spelt in syllables (Maham/Mahom, Baltimore, Macdonald) cannot pass an LM, so the ranges in `sense_names.tsv`
count when every group has a value. Image re-transcriptions in `transcr/R*.txt` replace the DECODE parse.
Calibration: the same test applied to the eight Lyonet letters, along their aligned (known-sense) group sequences,
passes 0.876 of groups, so the measure under-counts real sense by roughly an eighth; the figures below are the raw
measured ones. The Lyonet letters count as read (contemporary decipherment); R1071 counts as unread.

**Image re-transcription** (all from the DECODE images in img/, rotated -90, read strip by strip at full resolution):
- R1072: re-transcribed here (`transcr/R1072.txt`, 555 groups); the copyist's two looped forms of 8 were read as 0 by
  DECODE nearly everywhere (849, 898, 984, 878, 1018, 1088, 868, 885, 828 ...). Text now reads as a whole
  (comptoit, gratification de cent louis, d'Écosse et d'Irlande, Baltimore, remplit ses engagements, assez tôt).
- R1074: re-transcribed here (`transcr/R1074.txt`, 537 groups; DECODE's 564 included split/merged junk [1] [0] [21]).
- R1067: re-transcribed by an image sub-agent (`transcr/R1067.txt`, 1,481 groups; ~133 positions differ from DECODE:
  ~20 run-together groups, ~6 dropped, 3 added, one struck group kept by DECODE, the rest mostly the 8 trap; three
  copyist hands; paragraph numbers No 2-13 spread over the pages).
- R1064: converted with `doc2tr.py` (keeps the tagged lines) and then checked line by line on the images by a
  sub-agent (`transcr/R1064.txt`, 1,243 groups; ~48 8/0 fixes, one whole line DECODE dropped on p. 5, 2 splits,
  ~10 other digits; a second hand on pp. 3-4 writes 8 as a w-shaped double loop and 3 as a reversed c).
- R2067: the 19 Sept hand transcription reformatted (`transcr/R2067.txt`); R1065 converted with doc2tr.py for the
  denominator only.

**Pooled open codes** (`pool.py` lists every occurrence across all letters; only values that every occurrence forces
went into `key_X.tsv`, with evidence): 1096 ir, 823 gra, 630 lui, 990 dit, 336 facil, 520 faire (H); 1102 Écosse,
597 et, 459 to, 363 conven, 240 tôt, 686 pli, 458 en, 212 plus, 840 cli, 514 ld, 303 la Gouvernante (name code),
485 vous (M). Left open because more than one word fits: 970 (projets/desseins/plans, 6 occurrences), 869
(opérations/plans), 109/651 (two days: "avant [109] ou [651]"), 731/708, 1191 (le/du [1191] Macdonald), 1020, 1082,
890, 431, 373, 724, 993, 426, 427.

**Result, sense measure (threshold -3.0), before -> after:**

| Letter | groups | 5 Oct before | 5 Oct after | what moved it |
|---|---|---|---|---|
| R1072 | 555 | 0.661 | 0.888 | image re-transcription; 8 pooled values |
| R1067 | 1,481 (was 1,471) | 0.661 | 0.791 | image re-transcription; lui, dit, facil, faire, la Gouvernante |
| R1074 | 537 (was 564) | 0.702 | 0.747 | re-transcription; faire, Écosse, ld; names |
| R1064 | 1,243 (was 1,108) | 0.766 | 0.808 | 135 groups DECODE/parse.py had lost; image check |
| R2067 | 457 | 0.761 (not in cipher_U; counted from transcr) | 0.792 | lui, dit |
| R1054 / R1070 / R1073 / R1076 / R1068 | 372/400/312/403/60 | 0.925/0.885/0.885/0.819/0.667 | 0.949/0.905/0.885/0.819/0.750 | pooled values |
| undeciphered letters | 5,820 | 0.749 (of 5,245) | 0.824 | |
| all groups (Lyonet letters read, R1071 unread) | 10,067 | 0.778 (of 9,363) | 0.823 | |
| without R1071 | 9,306 | 0.847 | 0.890 | |

At threshold -3.4 the totals are 0.848 overall, 0.917 without R1071; at -2.6, 0.773 / 0.837.

**Why 95% is out of reach here.** R1071 is 761 of 10,067 groups (7.6%) in another code with no key material, so the
target cannot pass 0.924 even if every other group read. Within the readable letters the remaining failures are
(i) open codes where several words fit (listed above), (ii) key values that make nonsense in place (homophone
clashes the 651-group vote did not settle, e.g. 1080 pêche in the date of R1074, 307 forc/pen), and (iii) the
measure's own under-count of about an eighth.

## Remaining gaps

- R1071 (to Stainville/Choiseul, 4/7 Aug 1757), 761 groups - blocker: no-key-material; a different code; no decipherment among the images and the Nationaal Archief 1.01.50 inv. 221/223 decipherments are not digitised
- open code groups where more than one word fits (970, 869, 109/651, 731/708, 1191, 1020, 1082, 890, 431, 373, 724, 993, 426, 427 and single groups listed as [n] in read/) - blocker: open-codes; pooled over all letters 5 Oct 2026 (pool.py), no occurrence forces one value; the decipherments NA 1.01.50 inv. 221/223 would settle them (not digitised)
- key values that read as nonsense in place (homophone clashes in key_M, e.g. 307, 1080), most in R1074 (0.75) and R1067 (0.79) - blocker: open-codes; would need the Lyonet key sheet or NA inv. 223 decipherments
- R1054, R1068, R1070, R1073, R1076 not re-transcribed from the images (DECODE parse with view.fix splits) - blocker: none external; lower yield, they already measure 0.75-0.95

## Escalation

- [x] siblings: all R1052-R1076 and R2067 opened; eight Lyonet decipherments found among the images
- [x] clear-pages: the "clear" pages are Lyonet's decipherments, transcribed into plain/
- [ ] known-keys: other d'Affry codes (1755-56, and to Choiseul from Dec 1758) not sought for R1071
- [x] print: De Leeuw 2000, Bussemaker 1906, Coquelle 1904 checked
- [x] key-rebuild: key_M.json voted from the alignments, inferred values in read/R*_new.tsv; key_X.tsv (5 Oct) pooled values
- [x] retry: 5 Oct 2026, R1072/R1074/R1067/R1064 re-transcribed from the images, open groups pooled across all letters, all letters re-measured with measure_sense.py (0.778 -> 0.823 of all groups)
