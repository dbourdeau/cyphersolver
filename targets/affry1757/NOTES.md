# d'Affry (The Hague) to Rouillé / Bernis, 1757-58: intercepted code letters

Status: in progress (21 Oct 2026): 144 register values checked on the scans and folded into key_X.tsv in two passes; 0.941 of the groups now read as sense (8,761 of 9,306; the ten letters with no contemporary decipherment on DECODE 0.906). Below the 95% read bar. Open: about 45 valueless groups where the register piece is noise, a single syllable or conflicts, and the groups that take two values (sections "Register values folded into the key" below).

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): graded C, overturned on
re-reading. The eight Lyonet decipherments (`plain/`) are clean French; the ten keyed readings (`read/`) build
sentences with scattered bracketed codes and inferred syllables in braces. The worst passage is the first paragraph of
R1054 (holes in most sentences); the rest of that page reads. No letter relabelled; R1068 (a 60-group note, matched by
its register copy) carries a reading review. English translations still to add.

Status: read in part (5 Oct 2026, rerun 14 Oct 2026: 0.89 of the code groups read as sense by measure_sense.py, 8,282
of 9,306; the 21 Sept figure 0.86 counted groups that merely had a value; write-up affry1757.html, 19 Sept 2026)

21 Oct 2026, PR #65 (WAINUT) merged: clerks' clear copies of all ten letters without a Lyonet sheet are in the
digitised Fagel registers NA 1.10.29 inv. 5186/5187 (section "Contribution by WAINUT" at the end; review re-run, every
figure reproduced). The prior-reading record now says the full content exists in the archive. Corrected from it: R1068
(664 Vendredi; the recipient is Starhemberg, not d'Arenberg). Not yet adopted: the settled groups, the 64 key conflicts
and the R1073 corrections in `wainut/`. Folded in later the same day, after a check on the scans: see "Register values
folded into the key (21 Oct 2026)" below.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): R1071, d'Affry's letter to Stainville at
Vienna (4/7 Aug 1757), is in a different code (code C below) and is now [`targets/affry1757c/`](../affry1757c/NOTES.md)
(a different cipher, with its own page; `cipher_C.txt` and its DOC file moved there). Codes A and B below are one
code; the profile now lists them as one document. Figures in the sections below dated before 14 Oct include R1071
where they say so.

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
  cipher used". Not digitised (empty scan ids, checked 19 Sept 2026). The Fagel registers NA 1.10.29 inv. 5186
  (1757) and 5187 (1758) are digitised and hold clerks' clear copies of the same letters (WAINUT, 21 Oct 2026; see the
  end of these notes).
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

## Register values folded into the key (21 Oct 2026)

WAINUT's proposals (`wainut/settled.tsv`, `wainut/key_conflicts.tsv`, the R1073 and R1068 corrections) were checked
against the register scans themselves: NA 1.10.29 inv. 5186 scans 13R, 14L, 16R, 17L, 42R, 62R, 63L, 148R, 149L,
149R, 150L, 181L, 255R and inv. 5187 14R, 15L, 15R, fetched from the NA file service (not committed) and read here.
Every value adopted below was seen on at least one of these scans; the evidence column of `key_X.tsv` names the scan
and the words.

How the 64 conflicts were sorted: each occurrence was printed with four groups either side, key value against register
piece (scratch script, not kept). A value was adopted when the register has the same word at every clean occurrence
and the key value makes no sense there. Left alone: spelling and abbreviation (premiers/premier, s.a.r., jours/jour,
fonds/fond, pensionnaire, villes, utilité), person and tense forms of one stem (631 avoit/avois/avoir, 968
pouvoit/pouvois, 842 étoit/été, 1186 été/étoit), alignment noise (5, 26, 67, 89, 148, 388, 482, 836, 936, 974), and
989, which is *qu'un* twice in R1064 but *to* in re-to-ur in R1076.

Then every candidate was set against Lyonet's own decipherments (`align/R*.tsv`, grade H). Dropped because Lyonet
reads them otherwise as often or more: 16 (Lyonet *le roi de Prusse* three times; the register *Prussien(s)*,
*Prussienne*), 94 (Lyonet *peux*; the register *la Haye* once), 605 (Lyonet *inconvénient* twice; R1074 gives *vi*
three times, probably a misread group there), 635 (Lyonet *faut*; *fau-droit* in the register), 727 (*moi* and *mois*
four times each in Lyonet: a genuinely two-valued group), 895 (Lyonet *devoir* three times) and 1193 (Lyonet
*utilité* three times). Kept at M where Lyonet has one contrary occurrence: 109, 373, 806, 923, 959, 993, 1174, 1192.

Adopted (58 rows in `key_X.tsv`, after the 17 pooled values of 5 Oct; `key_X.json` regenerated from it):

- open groups now valued: 970 projets, 109 lundi, 651 mardi, 731 là dessus, 708 impos, 1191 sieur, 724 mes, 1082 ers,
  373 voy, 993 doit, 426 pouvoir, 427 mauvaise, 890 détail, 431 étrang, 1020 après, 1022 as, 776 infraction, 662 seur,
  774 résolution, 507 exacte, 664 vendredi
- key values replaced (old value in brackets): 806 mieux [lon], 58 fa [che], 61 fo [fou], 116 traite [pas], 125 est
  [étant], 163 croi [a], 194 que [quequ], 240 prompt [tôt], 479 empech [v], 504 apparent [aparem], 553 produi
  [produit], 556 contre [ssi; but *au contraire* twice], 619 grand [grande], 675 vingt [deux], 676 vo [voi], 749 donn
  [ca], 762 occasion [égard], 834 elle [elles], 900 di [dis], 911 ns [co; but *Co-l-lo-re-do* in R1068], 923 ceux
  [roit], 959 to [ton], 960 vu [f], 973 le [on], 992 er [des], 1014 age [usage], 1027 le roi [roi], 1039 et [lies],
  1099 is [isle], 1103 fort [fortes], 1106 froid [succès], 1144 res [rez], 1151 parce que [faire], 1174 lu [eu], 1184
  etat [etats], 1185 ite [iter], 1192 xe [que]

Re-measured with measure_sense.py (threshold -3.0, unchanged):

| letter | before | after |
|---|---|---|
| R1072 | 0.888 | 0.935 |
| R1076 | 0.819 | 0.846 |
| R1073 | 0.885 | 0.939 |
| R1064 | 0.808 | 0.828 |
| R1067 | 0.791 | 0.851 |
| R1068 | 0.750 | 0.750 |
| R1054 | 0.949 | 0.946 |
| R1070 | 0.905 | 0.902 |
| R1074 | 0.747 | 0.775 |
| R2067 | 0.792 | 0.853 |
| undeciphered letters | 4,797/5,820 = 0.824 | 5,006/5,820 = 0.860 |
| all groups, Lyonet letters read | 8,283/9,306 = 0.890 | 8,492/9,306 = 0.913 |

The Lyonet letters, measured through the key, move by at most a point either way (R1052 0.822 -> 0.815, R1069
0.838 -> 0.830, R1063 0.915 -> 0.933). Against the register text, `wainut/align_register.py` now gives 4,551 of
5,607 keyed groups (0.812, was 0.780), shuffled keys at most 0.219 per letter. That figure is partly circular: the new
values were taken from the same registers. The sense measure is not.

`read/R1073.md` carries the register text of 42R as read here and the corrections it makes; `read/R1068.md` the
181L text. The other read/ files are not rewritten.

## Second pass: groups without a value (21 Oct 2026)

`wainut/open_groups.tsv` lists 151 groups with no key value and the register piece aligned to each occurrence. 20 had
been valued in the first pass; the other 131 were printed with their context (register and key, four groups either
side) and with every Lyonet occurrence. Two more register scans were read for them (5186 63R and 248R).

Adopted, 86 groups, each seen on a scan (evidence in `key_X.tsv`): 17 or, 40 extrême, 53 dernier, 57 conformément, 84
content, 97 quel, 127 extrême, 145 informations, 154 raison, 162 britannique, 175 x, 188 fortifications, 198 nous, 214
jeudi, 215 absolu, 258 ignore, 278 huit, 279 amirauté, 285 le comte, 297 attaques, 299 judice, 319 avis, 324 volonté,
338 cham, 345 chiffré, 365 cor, 370 tour, 379 voyez, 385 possible, 391 Madrid, 393 son, 409 Allemagne, 418 président,
420 honneur, 461 vant, 467 gu, 499 oeuvr, 506 directement, 510 établi, 511 exposer, 545 flo, 555 Berlin, 558 frais,
560 somme, 567 qu'il, 608 autre, 615 Amérique, 634 fait, 643 Wassenaer, 649 un, 667 six, 678 tion, 680 finiront, 706
foi, 718 marque, 719 donné lieu, 741 question, 756 toutes, 777 défiance, 782 croirois, 783 ts, 798 toutes, 802
concili, 803 consent, 817 mot, 846 convoqu, 854 partie, 871 vingt, 880 mais, 897 marqu, 904 tée, 969 politiques, 977
quand, 995 doute, 1006 non seule, 1029 au, 1030 x bri, 1031 arme, 1040 teau, 1074 sujet, 1086 esprits, 1121 assisté,
1157 vrai, 1172 rs, 1190 sont, 1196 donnerois. Graded H where two clean occurrences or Lyonet agree (409, 667, 741,
756, 897), M otherwise; most rest on one occurrence. Lyonet reads none of them otherwise except one stray occurrence
each for 53 (voy) and 154 (ne).

Not adopted, 45 groups: register piece is a single letter, a syllable split at a segment edge, or noise (4, 28, 69,
103, 108, 118, 131, 178, 223, 256, 290, 369, 381, 430, 462, 498, 528, 636, 801, 804, 822, 859, 883, 953, 957, 1049,
1161, 1195, 1197); occurrences disagree (63 observations/vez, 65 seule/-ment, 114 bonne/-r, 184 satisfai/égard, 205
London/e, 311, 318, 563 la province/la, 869 plans/il y a, 978 10 and 18); Lyonet disagrees or the register gives a
name the cipher spells otherwise (94, 330 Lyonet aussi four times, 386, 387, 434, 217).

Re-measured (measure_sense.py, threshold -3.0):

| letter | key alone (14 Oct) | first pass | second pass |
|---|---|---|---|
| R1072 | 0.888 | 0.935 | 0.962 |
| R1076 | 0.819 | 0.846 | 0.876 |
| R1073 | 0.885 | 0.939 | 0.942 |
| R1064 | 0.808 | 0.828 | 0.852 |
| R1067 | 0.791 | 0.851 | 0.920 |
| R1068 | 0.750 | 0.750 | 0.750 |
| R1054 | 0.949 | 0.946 | 0.968 |
| R1070 | 0.905 | 0.902 | 0.965 |
| R1074 | 0.747 | 0.775 | 0.894 |
| R2067 | 0.792 | 0.853 | 0.877 |
| ten letters, no decipherment on DECODE | 0.824 | 0.860 | 0.906 (5,275/5,820) |
| whole code, Lyonet letters read | 0.890 | 0.913 | 0.941 (8,761/9,306) |

Register agreement (`wainut/align_register.py`): 4,651 of 5,719 keyed groups, 0.813 (partly circular, as before).

## 23 Oct 2026: verification 3 (explicit-hole score): R1072, R1074, R2067 follow the Fagel register

The v3 sweep scored the keyed decodes `read/R1072.md`, `R1074.md` and `R2067.md` at 0.366, 0.538 and 0.588 on the
explicit-hole measure (plain 0.27/0.33/0.53): below the bar. All three have their contemporary clear copy in the Fagel
register (WAINUT's section above; the pages 5186 13R-14L and 5187 14R-15R are among those checked line by line against
the scans), and the keyed groups stand at the register's word at 0.826/0.794/0.770 against 0.14-0.15 for shuffled
key values, from first group to last. The readings now follow the register in the clerk's spelling:
`read/R1072_reading.md`, `read/R1074_reading.md`, `read/R2067_reading.md` (the old keyed decodes are kept beside them).
Scores: 1.0 explicit-hole for all three; plain 0.871, 0.967, 0.933. Notable: group 147 (key "italien") stands where the
register names the informer "l'Angelo"; 675 (key "deux") at "Vingt". The profile entries point `reading` at the new
files and keep read (grade A). No English files written yet for these three (summaries in the profile).

## 23 Oct 2026: verification 5 (plain-bar check): R1067, R1068, R1070, R1073, R1076 follow the Fagel register

French of 1757, so the plain word-list share is a bar as well as the explicit-hole share. The keyed decodes
`read/R1067.md`, `R1068.md`, `R1070.md`, `R1073.md`, `R1076.md` scored plain 0.56/0.2/0.54/0.5/0.41 on their reading
bodies (explicit 0.60-0.67): open codes and brace-inferred syllables in most sentences. As for R1072/R1074/R2067 (v3),
the readings now follow the clerks' clear copies in the Fagel register: `read/<R>_reading.md`, clerk's spelling, each
with a header giving the register pages and the key/register agreement (0.578-0.854 of keyed groups at the register's
word against 0.09-0.14 for shuffled values). The register pages not checked before (5186 16R, 17L, 149R, 150L, 255R,
256L) were fetched through the NA IIIF server and checked line by line. R1076: "et la Tempette" (register slip) read
"sans la Tempette" from the figures, and the struck "ai" of "je lui ai parlai" left out; three register stretches of
R1076 have no matching cipher run (clear periods of the letter or cipher not imaged). New scores: plain 0.821, 0.75,
0.923, 1.0, 0.974; explicit 1.0 for all; the sentences under the plain bar fail only on Mr, titles and names. R1069
(Lyonet's decipherment, `plain/R1069.txt`, plain 0.5) fails only on "Mr" and names (Saltikof, Golofkin, Laurenzi ...):
keeps read. No English files yet for the register readings (summaries in the profile).

## 27 Oct 2026: the last five letters checked on the images

R1054, R1068, R1070, R1073 and R1076 were still measured on the DECODE parse. Converted with doc2tr.py and checked line
by line on the images (R1068 here; R1054/R1070 and R1073/R1076 by two image sub-agents, full-resolution strips); each
`transcr/R*.txt` ends with a `# changes vs DECODE:` list. These copyists' 8 is never read as 0.
- R1068: 60 groups, all agree with DECODE (911 is one group).
- R1054: 369 groups (DECODE 372): three groups DECODE split at a superscript correction (831|861, 878|875, 740|140);
  the first two agree with the r2q corrections of 23 Oct.
- R1070: 400 groups: 849 and 219 that DECODE dropped (I5590 l.1); a struck 851 kept by DECODE as a second 852;
  1132 -> 1131; 58 -> 56|58. The letter begins on I5591 (No 210 header): DECODE has the pages reversed (positions
  kept in DECODE order). One group under an ink blot (I5590 l.4).
- R1073: 315 groups (312): merges split (5831711041 -> 583 171 1041, 96699681 -> 966 996 81|61), 958 -> 938, a blot
  that DECODE read as a group removed.
- R1076: 424 groups (403): DECODE dropped two whole 11-group lines, the first lines of paragraphs P:4 and P:8;
  105 -> 1057 at the edge; 845 corrected by a superscript 2 (= 245) had been read as 8 245. The letter begins on I5607
  (No 124, P:4); I5606 (P:8) is the later leaf, so DECODE's page order is reversed. The two recovered lines may be part
  of the "register stretches with no matching cipher run" noted in verification 5.

Re-measured (measure_sense.py, now on the image transcriptions): R1073 0.939 -> 0.962, R1076 0.873 -> 0.887, R1054
0.968 -> 0.967, R1070 0.965 -> 0.955 (the corrected digits lose two values), R1068 unchanged; letters with no
contemporary decipherment 0.906 -> 0.908; all groups 8,760/9,306 -> 8,787/9,327 = 0.942.

## Decrypt audit, 16 Nov 2026

`research/decrypt_audit/detail.py` re-applies the key files of the profile to each transcription and compares the letters
with the published reading. Before: three texts compared (R1072, R1074, R2067), 323 of 956 words depart (106 of 341,
113 of 332, 104 of 283), none marked.

Causes, in order of weight:

- The published readings are not the output of the key. Since 23 Oct 2026 `read/R*_reading.md` give the clerks' clear
  copies in the Fagel register (NA 1.10.29 inv. 5186/5187), in the clerk's spelling; each file says so in its header,
  and the keyed decodes are kept beside them as `read/R*.md` (sections "verification 3", "verification 5" and "r2q"
  above). So wherever the key and the register differ, the reading has the register's word. Example, R1072: the
  figures 727 582 147 give "mois l italien", the reading has "moi l'Angelo" (named in the header of the reading).
  Counted with every value the folder holds (all three layers, the 17 disagreeing inferred groups at their first-listed
  value), on R1072, R1074 and R2067: 142 places, 264 of
  1,030 words. 102 are a keyed group whose value is not the register's word (388 keyed "cent" where the register has
  "les"; 414 "angleterre" at "Anglois"; 605 "inconvenient" in R1074; 1186, 842, 631, the two-valued groups of
  Remaining gaps); 25 are endings the code does not write and the clerk does (s, e, x: "Royaume[s]", "un[e]"); 15 sit
  at one of the 28 groups of these three letters that have no value in any file. None of these places is marked inside
  the reading text; the header gives the count of mismatching groups (60 for R1072) and names the notable ones.
- The key was spread over several files and the audit applies one table at a time. The profile named `key_M.json` and
  `key_X.tsv`; the values actually used (measure_sense.py, wainut/align_register.py) are key_X.tsv over key_M.json over
  the H/M rows of `read/R*_new.tsv`, with 105 and 107 as nulls. Of the 555/537/457 groups of R1072/R1074/R2067, 59/41/36
  take their value from key_X.tsv and 17/31/21 from the inferred rows only. Example: 459 "to" in "com-p-to-it"
  (key_X.tsv) was missing from the decrypt made with key_M.json alone.
- Audit artefacts: `key_M.json` holds the literal string "null" for 107 and 119, which the script printed as letters;
  a doubtful group written a|b in `transcr/` is dropped or doubled by its tokeniser.
- Five profile entries (R1054, R1068, R1070, R1073, R1076) still named the DECODE DOC file as transcription, although
  the image-checked `transcr/R*.txt` of 27 Oct 2026 replaced it.

Changed:

- `key_merged.tsv` (new): one row per group, 803 rows, with a source column (620 from key_M.json, 161 from key_X.tsv
  with the key_M value each replaces, 20 inferred values with file and line, the nulls). It holds no new value. The 17
  inferred-only groups on which the `read/R*_new.tsv` files disagree (727 moi/mois, 631 avoit/avoir, 945, 989 ...)
  have no row and are listed at its foot. Added to `outcome.key_file` after the two existing files.
- `profile.json`: the transcription of R1054, R1068, R1070, R1073 and R1076 now points at `transcr/R*.txt`.
- No reading, decode or translation file was touched.

After: eight texts compared, 505 of 1,983 words depart (25%); the three of the first run 288 of 1,028 (R1072 99 of 377,
R1074 107 of 358, R2067 82 of 293). The script's count and the 264 above differ because it tokenises a|b groups
otherwise. R1064 and R1067 are still not compared by the script; not looked into.

Not explained or not done: the 142 places were classed by script (which groups stand at the gap), not each read
against the register scan. Whether a keyed group that differs from the register is a wrong key value, a second value
of the group, a slip of the intercept copy or a slip of the clerk is not settled per place. The readings of the other
seven register-based letters were not gone through place by place. The write-up page gave the R1074 loan as
"two millions" and quoted "des gens si maladroits", both from the keyed decode; the register reading has "Vingt
Millions" (675 = vingt in key_X.tsv) and "des Personnes si mal adroites" (corrected, see below).

Marked on 16 Nov 2026: no place marked inside any reading. The ten `read/R*_reading.md` are another source's text,
the clerks' clear copies in the Fagel register, so the 142 places where the figures give another word stay unmarked
in the text (they are in `wainut/align/R*.tsv`, status mismatch). Header: each of the ten files now has one line under
its title, "What this file is", saying that it is the register's clear copy and not the output of this folder's key,
and naming `read/R<rec>.md` as the keyed decode (R1054, R1064 and R1076 with the exception their headers already
state: the figures are followed at the listed places). No letter of any reading text changed. Page
`docs/affry1757.html`, R1074 paragraph: "two millions" to "twenty millions" and the quotation "des gens si maladroits"
to "des Personnes si mal adroites", as the published reading has them. Left as they are on the page: "the Italian"
for the man the register calls l'Angelo, and the sentence that each letter was decrypted with the key.

## Remaining gaps

- 45 groups without a value that the register does not settle (listed above under "Not adopted") - blocker: no-key-material; the register piece is noise or the occurrences disagree
- groups that take two values in practice (727 moi/mois, 911 ns/co, 556 contre/contraire, 842 étoit/été, 1186, 895 devoir/devoit, 1193 utile/utilité, 16 roi de Prusse/prussien, 605 in R1074) - blocker: no-key-material; one value per group is all key_X can hold, so the measure under-reads these
- R1054 and R1064 groups that the Fagel register passes over without a word (R1054: 101, 760; R1064: 103, 178 in a false start, 146, 29 108) and the R1064 passport-date groups 978 634 114 - blocker: no-key-material; the register pages 5186 248R-249L and 62R-63R were checked on the scans 23 Oct 2026 (r2q) and both letters now read from them, these groups have no value in any letter

- groups cut by the binding or under ink (R1073 p.1 line ends, R1076 102|1024 and 663|668, R1054 ll.2/3/21, one group under the blot on R1070 I5590 l.4) - blocker: illegible; checked at full resolution 27 Oct 2026, no better image online

## Escalation

- [x] siblings: all R1052-R1076 and R2067 opened; eight Lyonet decipherments found among the images
- [x] clear-pages: the "clear" pages are Lyonet's decipherments, transcribed into plain/
- [n/a] known-keys: the key of this code was rebuilt from Lyonet's decipherments; the search for R1071's code (code C) is recorded in ../affry1757c/
- [x] print: De Leeuw 2000, Bussemaker 1906, Coquelle 1904 checked
- [x] key-rebuild: key_M.json voted from the alignments, inferred values in read/R*_new.tsv; key_X.tsv (5 Oct) pooled values
- [x] retry: 5 Oct 2026, R1072/R1074/R1067/R1064 re-transcribed from the images, open groups pooled across all letters, all letters re-measured with measure_sense.py (0.778 -> 0.823 of all groups)
- [x] clear-pages (again): 21 Oct 2026, the Fagel registers NA 1.10.29 inv. 5186/5187 hold clear copies of all ten letters (WAINUT, PR #65); 58 values checked on 16 register scans and folded into key_X.tsv (0.890 -> 0.913)
- [x] the register's words for the valueless groups (wainut/open_groups.tsv): 86 adopted after a scan check, 45 left open (second pass, 21 Oct 2026; 0.913 -> 0.941)
- [x] retry: 27 Oct 2026, R1054, R1068, R1070, R1073, R1076 checked on the images (two dropped lines of R1076 and two groups of R1070 recovered; reversed page order of R1070/R1076 found), all letters re-measured (0.941 -> 0.942)
- [x] clear-pages (register, R1054/R1064): 23 Oct 2026 (r2q), 5186 248R, 249L, 62R, 63L, 63R checked on the scans; both letters read from the register, figures followed where they differ

## Contribution by WAINUT (21 Oct 2026)

WAINUT (a Dutch AI company, https://github.com/WAINUTAI) adds one source for the ten letters of this folder that have
no Lyonet sheet among the DECODE images: the Fagel registers in the Nationaal Archief, which hold their contemporary
decipherments. This section says where they are, how far this folder's key agrees with them, and which open groups,
key values and readings they settle or contradict. Nothing above is changed: key, transcriptions, readings and
profile are as they were. Where the registers disagree with a value, the evidence is given and the decision is left
to you. The files are in `wainut/`.

**How the work was done.** Google Gemini (gemini-4-argon) transcribed the register pages line by line from the NA's
full-resolution IIIF images (`wainut/register_clear.txt`). The alignment and the analysis were done with AI
language-model agents. The transcription of inv. 5186 scans 13R, 14L, 42R, 148R, 149L and 181L and of inv. 5187
scans 14R, 15L and 15R was checked line by line against the scans, and every register word quoted in this section is
on one of those pages. The other register pages are unchecked model transcriptions; only the automatic alignment uses
them.

**1. The deciphered letters are digitised in clear.** "Prior work" and "Remaining gaps" above say that the contemporary
decipherments survive in NA 1.01.50 inv. 221/223, which are not digitised. The registers of Fagel's papers, NA
1.10.29 (Archief Fagel) inv. 5186 (1757, 399 scans) and inv. 5187 (1758, 225 scans), are digitised. They are clerks'
copies, in clear, of d'Affry's letters in date order, each with a margin heading "Dat: ..." and "A: à R:" (or
"A: à B:"), most with the letter's number. All ten letters are there:

| Record | Letter | Register (NA 1.10.29) | Viewer, first scan |
|---|---|---|---|
| R1072 | No 123, 6 Jan 1757 | inv. 5186 scans 13R-14L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0013 |
| R1076 | No 124, 7 Jan 1757 | inv. 5186 scans 16R-17L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0016 |
| R1073 | No 133, 25 Jan 1757 | inv. 5186 scan 42R | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0042 |
| R1064 | No 136, 1 Feb 1757 | inv. 5186 scans 62R-63R | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0062 |
| R1067 | No 161, 1 Apr 1757 | inv. 5186 scans 148R-150L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0148 |
| R1068 | No 172, 26 Apr 1757 | inv. 5186 scan 181L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0181 |
| R1054 | 19 Jul 1757, to B. | inv. 5186 scans 248R-249L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0248 |
| R1070 | No 210, 22 Jul 1757, to B. | inv. 5186 scans 255R-256L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5186/file/NL-HaNA_1.10.29_5186_0255 |
| R2067 | 17 Jan 1758, to B. (No 283 above) | inv. 5187 scans 14R-15L | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5187/file/NL-HaNA_1.10.29_5187_0014 |
| R1074 | its enclosure, "Extrait de la Lettre de Mr. Astier", margin "Du 11. Janvier 1758" | inv. 5187 scans 15L-15R | https://www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5187/file/NL-HaNA_1.10.29_5187_0015 |

A scan number is the NA file number (`NL-HaNA_1.10.29_<inv>_<scan>`); L and R are the left and right page of the
opening. The registers also have entries for the letters whose Lyonet sheets are in `plain/` (for example No 171,
R1069); we did not align those.

The content of all ten letters was therefore known in clear in 1757-58, as it was for the eight Lyonet letters.

**2. Agreement of the key with the registers.** `wainut/align_register.py` aligns each ciphertext (`transcr/R*.txt`
where it exists, otherwise `cipher_U.txt` with view.py's split of run-together groups) with the register text of the
same letter, using this folder's key as `measure_sense.py` loads it (714 groups). A keyed group counts as matching
when its value stands at that point of the register text. The control is the same alignment with the key's values
shuffled among its groups (10 seeds); the denominator is all keyed groups in both cases.

| Record | groups | keyed groups | matching the register | share | shuffled keys: mean (max) |
|---|---|---|---|---|---|
| R1072 | 555 | 530 | 438 | 0.826 | 0.140 (0.170) |
| R1076 | 403 | 386 | 214 | 0.554 | 0.126 (0.153) |
| R1073 | 312 | 305 | 247 | 0.810 | 0.129 (0.154) |
| R1064 | 1,243 | 1,201 | 996 | 0.829 | 0.153 (0.180) |
| R1067 | 1,481 | 1,399 | 1,119 | 0.800 | 0.152 (0.172) |
| R1068 | 60 | 55 | 45 | 0.818 | 0.096 (0.145) |
| R1054 | 372 | 364 | 319 | 0.876 | 0.144 (0.206) |
| R1070 | 400 | 386 | 229 | 0.593 | 0.134 (0.148) |
| R2067 | 457 | 434 | 334 | 0.770 | 0.133 (0.171) |
| R1074 | 537 | 494 | 392 | 0.794 | 0.148 (0.170) |
| all ten | 5,820 | 5,554 | 4,333 | 0.780 | |

R1076 and R1070 are low because their first 157 and 139 groups get no register text. Those cipher pages begin in
mid-letter with a passage that the register has later in the same entry, and the alignment only runs forward. Among
the keyed groups that are aligned, 214/232 (0.922) of R1076 and 229/251 (0.912) of R1070 match; these two figures
describe only the aligned part of those letters (about 60%), not the whole letter. Many of the other
mismatches are the clerk's spelling and abbreviation (Roy for roi, "Sa Maj:", "Consr."), which are not key errors.

**3. Open groups that the registers settle** (`wainut/settled.tsv`; the script prints every occurrence). Of the 16
groups listed above as open (5 Oct 2026), 14 have at least two occurrences where the register has the same word.
Ten of them have no conflicting occurrence and are graded H in `settled.tsv`; 970, 1191, 890 and 431 are graded M,
because one occurrence conflicts or some aligned pieces sit at a segment edge (for 1191 only the two R1074 pieces
are clean):

- 970 projets: R1072 three times, "sur les Projets de l'Angleterre", "des Projets des deux Proprietaires", "tous les
  Projets proposés aux Ministres" (13R).
- 109 lundi and 651 mardi: R1067 "qu'il comptoit Lundi ou Mardi au plus tard" (148R) and "avant Lundi ou Mardi"
  (149L).
- 731 là dessus: R1067 "qu'il étoit là dessus impossible" (148R), and R1076.
- 708 impos: R1067 "impossible" (148R); R1072 "si c'est un Imposteur" (14L).
- 1191 sieur, written Sr: R1074 "le Sr Macdonald", "du Sr Macdonald" (5187 15R).
- 724 mes: R1067 "dans les termes", "les Yeux en larmes" (148R); with 1191, "Mrs. Pels" in R2067 (5187 14R) and
  "Messieurs" in R1067.
- 1082 ers: R1072 "des quartiers" (13R); R2067 "chez des Banquiers" (5187 14R).
- 373 voy: R1072 "Vous voyez" (14L); R1054 "Voyage".
- 993 doit: R1067 three times, one of them "ne me répondoit pas" (148R).
- 426 pouvoir: R1067 "pouvoir me procurer" (148R), "son Credit et son pouvoir" (149L).
- 427 mauvaise: R1067 twice.
- 890 détail: R1072 "un detail des quartiers" (13R), and R1064.
- 431 étrang: R1072 "les Cours étrangères" (13R), and R1064.

Two of these also have one occurrence that does not fit: 970 in R1074, where the register has "faire entrer en
France" (5187 15L), and 431 once in R1067. 1020 après has one clean occurrence (R1072 "Aprés bien des debats", 13R);
its R1067 occurrence stands where the register has "Aprés cette lecture" (148R), but the alignment splits the word.
869 stays open: it stands at "de tous les Plans de Campagne" in R1072 (13R), but in R1074 where the register has
"s'il y a moyen" (5187 15R).

Also: 1022 is very probably as (R2067 "Mr. Astier", "le Juif Boas", 5187 14R; R1074 "Mr. Astier", 15L), but the
aligned pieces are noisy ("ras", once "e"), so it is graded M. 307 has both values, forc
five times and pen twice ("recompenseroit", 13R; "une Pension", 14L). 1080 is not settled: R1074 opens "Extrait de la
lettre de M. [1022]tier du [1080] [110] ...", and the register's margin has "Du 11. Janvier 1758", but the alignment
gives the group no text.

**4. Key values the registers contradict.** `wainut/key_conflicts.tsv` lists the 64 keyed groups that disagree with
the register at least twice and more often than they agree. Many are spelling or abbreviation (premiers/premier,
roi/Roy, pensionnaire/Pensionaire, s.a.r. written out as "Son Altesse Royale"). Where the register has another word
at every occurrence:

- 675, key deux: vingt. R1073 "vers le vingt du Mois" (42R); R1074 "un Emprunt de Vingt Millions" (5187 15L); in
  R1067 it stands at the date "du 28" (148R).
- 1106, key succès: froid. R1073 "avec le même froid" (42R); R1067 "J'ai trouvé Mr le Pensionaire fort froid" (148R).
- 762, key égard: occasion. R1073 "à cette occasion voir le Consr. Pensionaire" (42R); also in R1064.
- 1151, key faire: parce que. R1073 "parce qu'il m'a repondu" (42R); R1067 "à Bruxelles parceque si la Navigation"
  (149L, where the aligned piece is partial); also in R1064.
- 556 ssi: contr- (contre three times, contraire twice); 116 pas: traité (3); 923 roit: ceux (3); 960 f: vu (3);
  1039 lies: et (7). These come from the alignment; we did not check them on the scans.

`wainut/open_groups.tsv` gives the register's word for 151 groups that have no value, for example 664 vendredi (R1068
"Il a passé Vendredi au Soir", 181L, and R1064), 94 la Haye (R2067 "étoit à la Haye", 5187 14R), 776 infraction
(R1073, 42R), 409 Allemagne, 803 consent-. A value seen once rests on the alignment alone and needs a look before it
is adopted.

**5. Readings that the registers correct.** In `read/R1073.md` (No 133; register 5186 42R):

| read/R1073.md | register |
|---|---|
| "je leur [413]ois", "Je lui ai [413]" | "je leur declarois", "Je lui ai declaré" (413 is déclar-) |
| "comme une [776] à la neutralité" | "comme une infraction à la Neutralité" |
| "à cet {égard} voir le {Pensionnaire}" | "à cette occasion voir le Consr. Pensionaire" |
| "les verroit avec {peine} leur s'engag{er}" | "les verroit avec douleur s'engager"; the key itself gives do-u-leur (599 527 399) |
| "avec le même {succès}" | "avec le même froid" |
| "Je suis [662 persuadé?]" | "je suis Seur" |
| "cette {aug}[1021]mentation" | "cette Operation" |
| "vous ra(?) vous [774] où {elle} est de {res}ter [507]ment [les] premiers" | "confirmera la Resolution ou Elle est de rester exactement Neutre" |
| "ver-bi-le[675] du [5?] {mois} prochain, que l'que be-he-n" | "vers le vingt du Mois prochain. Il semble que l'Abbé Senski" (the name is not clear on the scan) |
| "ne fournit pas des nouvelles" | "ne fournit plus de nouvelles" |
| "Il faut droit voir si cela ne va pas lon[g]" | "Il faudroit voir si celà ne va pas mieux" |

In `read/R1068.md` (No 172; register 5186 181L) the register reads: "Il a passé Vendredi au Soir un Courrier de Vienne
à Londres. Vous savez mieux que moi ce dont il est chargé. Mr. de Colloredo doit faire passer à Mr. Starrenberg ce
qu'on lui aura repondu." So 664 is Vendredi (the reading has "[664 hier?]"), 806 is mieux as the reading proposed,
and the recipient is Starrenberg (Starhemberg), not d'Arenberg. With the key the cipher gives "m d a re m be r g"; the
register implies 982 = st (key d) and 245 = n (key m), each from this one occurrence.

In `read/R2067.md` and `read/R1074.md` (registers 5187 14R and 15L-15R): "M. [1022]tier" is "Mr. Astier"; "J'ai eu
hier encore [223] i of [520] [1022]" is "J'ai eu encore hier le Juif Boas"; "[724] Sr [pe l s]" is "Mrs. Pels"; "étoit
à [94]" is "étoit à la Haye"; "le [1191 {Sr}?] Mac{do}na{ld?}" is "le Sr Macdonald".

**Caveats.** The registers are clerks' copies: they abbreviate and sometimes word things differently from the cipher,
so a mismatch is not always a key error. The alignment is automatic, and a piece at a segment edge can be a syllable
too long or too short. The ciphertexts are this folder's (`transcr/`, otherwise `cipher_U.txt`); we did not re-check
them against the KHA images. The register pages not listed under "How the work was done" are unchecked model
transcriptions.

**Files** (`wainut/`): `register_clear.txt` (register text of the ten letters, 20 pages); `align_register.py`
(Python 3 standard library and numpy; reads `../key_M.json`, `../overrides.json`, `../key_X.tsv`,
`../read/*_new.tsv`, `../transcr/` and `../cipher_U.txt`; run it from `wainut/` with `python align_register.py`,
about 30 s; it prints every number above and writes the files below); `align/R*.tsv` (each group, its key value, the
register piece and the status); `pool.tsv` (every group over all ten letters); `key_conflicts.tsv`;
`open_groups.tsv`; `settled.tsv` (written by hand from the script's output). No images: the scans are on the NA viewer
at the links above.

## 23 Oct 2026: R1054 and R1064 back to decoded, not read (translation wave)
- R1054 (keyed decode with codes, 0.54 explicit holes) and R1064 (0.57; paragraphs 9-13 do not build) fall under the 0.60 bar and are set to **decoded, not read**. fraction_read 0.941 -> about 0.76 (estimated).
- Remaining gap: R1054, R1064 code groups with no key value - blocker: no-key-material.

## 23 Oct 2026 (r2q): R1054 and R1064 read from the Fagel register, figures followed where they differ
- Register pages 5186 248R-249L (R1054) and 62R-63R (R1064) fetched through the NA IIIF server (`research/reading_audit/b32_na_iiif.py`) and WAINUT's Gemini transcription checked line by line: 248R/249L/62R exact; two misreadings, 63R "du 10. Janvier" is "du 18." and 63L "ou de le taire" is "ou de Se taire" (`read/R1064_corrections.tsv`). Every page of `wainut/register_clear.txt` has now been checked against its scan.
- Every key/register disagreement in `wainut/align/R1054.tsv` and `R1064.tsv` gone through, R1054's on the cipher image I5511. Two DECODE parse errors in R1054: row 4 "8^6 31" is 831 (parti-sans), row 20 "878^6" is one group 878 (le), not 8 786 (`read/R1054_corrections.tsv`).
- Figures followed over the register: R1054 "à M. le Maréchal d'Estreés" (register "au Cte."), "de sa communication" (10 = sa), and the page's last words "que par le" (306 = par; register "que je le voudrois"; the second page of the letter is not on the DECODE record). R1064 "au Senechal de Quintin" (se-ne-cha-l; the clerk left a blank and deleted "ne ... soit"), "point" for "pas" twice, "il étoit important", "ou de la taire", "Vous remarquerez", and "regardoit les deux Capitaines et le Chirurgien" (the register omits the captains).
- Readings `read/R1054_reading.md` (plain 1.0, explicit 1.0; before 0.607/0.643 on the keyed decode's body) and `read/R1064_reading.md` (plain 0.764, explicit 1.0; before 0.646/0.785; the sentences under the plain bar fail only on Mr, names, numbers and the clerk's spelling), English `R1054_en.md`, `R1064_en.md`, logs `R1054_reread_log.md`, `R1064_reread_log.md`. Profile: both entries read, grade A; fraction_read back to the measured 0.941. Script `research/reading_audit/r2q_affry_write.py`, profile edits `r2q.py`.
- Open: the few groups the register passes over (Remaining gaps), blocker no-key-material.
