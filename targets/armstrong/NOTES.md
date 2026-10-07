# Armstrong -> Madison, coded postscript of 30 Aug 1808 (THE=972 code) — tracker item #2

## Result: solved — 48 of 49 code groups determined, the 49th a probable slip (2026-09-15, two sessions)

    P.S. Ru-s-el ought to be the consul: he is a-n America-n by bir-th, and is much better
    qua-li-fi(ed) than any other can-di-da-te. In a word he is above men in general. Next to
    him in fit-ness is O-mea-ly, but he is like Ward-en an Ir-ish-[man].

> Russel ought to be the consul: he is an American by birth, and is much better qualified than any other
> candidate. In a word, he is above men in general. Next to him in fitness is O'Mealy, but he is, like Warden,
> an Irishman.

Reproduce: `python decode972.py ps` (grades: plain = H pencil or C known plaintext, `?` = M uncertain, `*` = inferred).
Full write-up with the group-by-group table: docs/armstrong.html (§4).

### Grades of the 49 groups

- **Pencil decodes on M34 roll 13 and/or the 4 May 1806 known plaintext (H/C), 27 distinct groups:** 1116 s, 1165 to,
  1405 be, 972 the, 1459 he, 1482 is, 1201 a, 821 n, 1429 by, 970 th, 1319 li, 584 than, 687 any, 249 other, 736 can,
  1013 di, 750 da, 967 te, 1561 men, 927 him, 1090 in, 832 ness, 934 o, 510 mea, 860 ly, 1280 en, 1216 an, 1481 ir.
  Frame 0190 (second session) also gives **1320 like** as an H reading, so it is no longer inference-only.
- **Inferred from context and checked against the alphabetical slot (I), all fit:** 1394 ru (opens a new run after
  1393 purp; reads ru in three independent places: ru-in and Dan-ish in the 22 Feb 1808 letter, Et-ru-ria on frame 0201,
  Y-ru-jo on frame 0194 — so effectively H, recorded in `pairs.txt` line 215), 1273 el (1272 eight < el < 1279 Emp),
  250 ought (249 other < ought < 252 own), 148 consul (146 confide < consul < 151 contrary), 130 America (new run after
  128 yesterday, before 137 between), 720 bir (719 Ba < bir < 723 bo), 992 qua (< 993 qui), 1048 fi(ed) (1046 fi … 1052
  fit), 1202 above (1201 a < above < 1209 Agent), 1052 fit (1050 fi < fit < 1062 fol), 384 Ward (383 w < ward < 385 was),
  1483 ish (1482 is < ish < 1484 it; Dan-ish).
- **The one doubt:** the last group is **555** in the manuscript and in Founders; 555 = re (frame 0195, sco-re), which makes
  no sense after Ir-ish, while **1555 = man** (frames 0195 and 0200, `pairs.txt` lines 119 and 457). Read as a dropped
  digit for *Irishman*; the alternative, that the postscript breaks off at "an Irish re…", is recorded for completeness.

### Corrections to the Founders Online transcription (from the LoC image, Madison Papers reel 10 frame 0521)

- Second line starts **972.** (the) in the manuscript, not Founders' "970." (th).
- Last line has **1216** (an) in the manuscript, not Founders' "1218".
- A pencil *s* under 1116 on the LoC copy: someone in Washington began and abandoned a decode.

### The people

- **Russel** = Ru-s-el: most probably Jonathan Russell of Providence, R.I. (1771–1832), whom Madison did appoint chargé
  d'affaires at Paris when Armstrong left in 1810. Inferential: no other document places him in France in 1808.
- **Warden**: David Bailie Warden (1772–1845), born in County Down, secretary of legation, got the Paris consulate;
  Armstrong removed him in 1810 and protested his reinstatement in 1811 ("without a single grain of attachment to the
  U.S.", 3 March 1811). The postscript shows the same animus three years earlier and gives its cause.
- **O'Mealy**: Michael O'Mealy, Baltimore merchant resident in France since 1793 (Papers of James Madison, Secretary of
  State Series 10:497 n. 2).

An earlier version of these notes read the subject as "S." = Skipwith and 1394 as a null; both were wrong. 1394 is *ru*
(the clerk's pencil dash over it marks a syllable continued from the word written over the preceding group), and the
subject is Ru-s-el.

## How: the codebook was reconstructed from NARA DUSMF microfilm M34 roll 13 (naId 188671172, `img13/`),
where the State Department clerk's pencil decode is written above each cipher number of Armstrong's 1806–07
despatches, above all the October 1806 political despatch on frames 0192–0201 (located by `pencil_score.py`, which
ranks frames by faint mid-grey pixels away from ink). Pairs were read frame by frame and recorded in `pairs.txt`
(584 lines, each with frame/line reference and H/M grade; about 352 read with confidence); `decode972.py` merges them
with Tomokiyo's partial table from the 4 May 1806 known-plaintext letter (`code972_partial.json`, 227 entries) and the
INFER dictionary of slot inferences, ranking H > C > M > I, into a table of ~580 distinct groups (`python decode972.py
table`; `export_key.py` writes it as `key972.js` for the site decoder). The 1808–10 roll 14 (naId 188671566) is NOT
decoded except a faint pencil line under the 22 Feb 1808 postscript.

**Control text:** the private letter of 22 February 1808 (Founders 99-01-02-2733), ~150 groups in the same code and
sharing no groups of interest with the known-plaintext letter, reads with gaps with the merged table ("The ruin of
Gustavus is at last resolved. Russia is to seize Finland, while France & Denmark take possession of Sweden…"), and
fixes ru, ish and Russia (305). Two probable single-digit slips there: Founders' 631 (wise) for 651 (plain) in
"com-plain-t-s", 916 (had) for 921 (have). One anomaly: 946 is *on* in the 4 May 1806 letter but must be *Gu* in
Gustavus (914 = gu elsewhere) — homophone or slip.

## Second session (2026-09-15): the roll-13 frames were re-fetched through the catalogue proxy
(`https://catalog.archives.gov/proxy/records/search?naId=188671172` lists the 393 object URLs, saved in `img13/objects.json`;
the images are `.../medialz/dc-metro/rg-059/603720/M34/M34-013/M34-013-NNNN.jpg`). Frame 0190 (Paris, 20 July 1806,
"A peace was signed last night between Russia and France ... this looks like peace between England and France also")
carries a full pencil decode and gives **1320 = like** (H), plus 1492 last, 835 night, 801 about, 679 look (H) and
512 media (M).

## What is left (not needed for the postscript)

- Frames downloaded but not yet read, which may turn the remaining I grades (1273, 250, 384, 1483, 992, 1048, 148, 130,
  720, 1052, 1202) into H: 0011-0012, 0016-0017, 0021, 0027, 0034-35, 0058-59, 0096-97, 0109-10, 0121-22, 0140-43,
  0150-51, 0160, 0188-89, 0191-92, 0223-25, 0232-38, 0289 (dense pages such as 0233 need 600 dpi crops line by line).
- The LoC image of the postscript (mjm015002) is still Cloudflare-blocked to scripts; it was collated by hand.
- The 20 Feb 1808 letter: see the adjudication section below (2026-09-16). Not readable with this table.
- The other coded Armstrong despatches: see "The other despatches in THE=972 (2026-10-02)" below. The "~40" was an
  overestimate: Founders' early-access texts of Sept 1807 - Feb 1809 contain eleven coded despatches, roll 14 adds three
  of 1810, and the 1804-07 ones are already printed decoded.

## The 20 February 1808 letter and the AFIO contest solution (adjudication, 2026-09-16)

**Verdict: the published solution does not hold.** It is a set of 56 word labels hung on 51 of the letter's 216 distinct
groups, and it fits its own sentence no better than a key fitted by the same procedure to a shuffled ciphertext.

The item: Armstrong to Madison, Paris, 20 Feb 1808 (Founders 99-01-02-2728; NARA M34 roll 14 images 29-32). Founders
prints 369 groups, 216 distinct, values 1 to 1900, with 35 passages in graphic symbols (shorthand-like) that no
transcription renders. Ciphertext saved as `feb20_ciphertext.txt` (Founders is now behind a CloudFront challenge for
scripts; the Wayback copy `web.archive.org/web/2025id_/https://founders.archives.gov/documents/Madison/99-01-02-2728`
works). The Association of Former Intelligence Officers announced on 27 May 2025 that Yaacov Apelbaum had decrypted it and
published a 60-word plaintext and a 56-entry key (saved as `afio_key.txt`; machine-readable form from Tomokiyo's
`madison_AFIO.txt`). Tomokiyo's article "An Outlier Code in Armstrong-Madison Correspondence (1808)" (cryptiana
`madison_armstrong.htm`, Oct 2025, rev. June 2026) already judged it unconvincing; this is the quantitative version.

### What the frames say

- Every coded despatch on the roll-13 frames read here (0034 = 18 Mar 1805 copy, 0097 = 10 Sept 1805, 0122 = 1806,
  0190-0201 = 1806, and the pencil-annotated pages generally) is in the THE=972 code, values below about 1600. No group
  in the 1700-1900 range, which the 20 Feb letter uses 49 times, was seen on any frame. The State Department clerk's
  pencil decodes therefore give the THE=972 key only; there is no pencil decode of the 20 Feb letter (Kreider: "we've
  found no evidence that it ever was decoded"), and Madison wrote to Jefferson on 15 May 1808: "The undecyphered letter
  from A. ... No such Cypher is in the office, and must be one concerted with another correspondent" (Founders
  99-01-02-3082, Kreider's identification). So "rebuild the claimed key from the frames" has a definite answer: the
  frames cannot yield it, because the key was never in Washington.
- Paired check with our table (`python decode972.py feb15` / the 20 Feb groups): the **15 Feb 1808** despatch, five days
  earlier, is in THE=972 and reads at once (176 of 243 groups H/C-known, 72 %: "with one [hand] they offer us the
  Floridas ... they do not accept this ... it is however merely an experiment; yet if it succeeds you will [see] a
  second ... In either case, do not suspend a moment the seizure of the Floridas"). The 20 Feb letter with the same
  table: 92 of 369 groups (25 %) hit, and the hits are noise ("roc de ion ... ward the native pos native like ct
  Monarch temp ..."). Two letters, one table, one reads and one does not: the 20 Feb code is a different code, as
  Kreider's team and Tomokiyo said.

### Scoring the AFIO key (`python adjudicate_feb20.py`)

| test | AFIO key | control |
|---|---|---|
| groups of the letter covered by the key | 133 of 369 (36 %); 51 of 216 distinct | |
| key numbers that never occur in the letter | 5 of 56: 6 *i*, 39 *written*, 131 *to*, 432 *its*, 1358 *that* | |
| plaintext words with no code group at all | 6 of 60: *seamen, examined, not, we, shall, receive* | |
| published text aligned in order against the key's rendering | 40 of 60 words, over groups 12-102 (page 1) | shuffled key: 18.9 mean, max 26 (passes, but trivially: the key was read off this page) |
| mapped occurrences inside that span the text does not use | 28 of 68 dropped (consistency 0.59) | key built by the same walk on a **shuffled** ciphertext: 0.70 +/- 0.18 |
| mapped occurrences over the whole letter the text does not use | 93 of 133 (share used 0.30) | same control: 0.41 +/- 0.02, min 0.36 |
| the 13 occurrences of 17 = "of", 12 of 18 = "the", 10 of 38 = "and", 8 of 14 = "this" | used 0, 1, 0, 0 times | |

Reading the first sentence with their own key gives *you the petitions your [1628] have concerning their your treatment
[symbols] have commerce been*, which they print as "The petitions of your seamen concerning their treatment have been
examined": *you*, *the*, the second *your*, one *have* and *commerce* are dropped, *of*, *seamen* and *examined* are
supplied. "I have written to you ... its ports ... that" rests on five key numbers absent from the letter. The 35
symbol passages, including two full lines, are not mentioned. The "verification methodology" on the AFIO page (grammar,
style, thematic parallels with the 1804 and 1806 letters, frequency of "the/this/have") tests the English sentence,
not the key; the frequency claim is false on its face, since the text uses the letter's commonest group once in
thirteen occurrences.

The controls: (A) shuffling the 45 words among the 56 numbers drops the in-order match from 40 to about 19, which
shows only that the key encodes the order of page 1, as any key read off page 1 must. (B) The informative control is
to build a key the same way (walk the plaintext, give each word the next free group) on a *shuffled* copy of the
ciphertext: 500 such keys fit the AFIO sentence with 60 of 60 words in order, account for 70 % of the mapped
occurrences in their span and 41 % over the letter, both better than the AFIO key's 59 % and 30 %. A key that fits
random noise better than it fits the real text carries no information about the code.

### What would settle it

A reading must render every occurrence of every mapped group, say what the symbol passages are, and be checked against
an independent source: a second letter in the same code, or the key itself. The candidates for the "other
correspondent" (Tomokiyo, from Kreider): Pinkney, Monroe, Erving, Livingston, or Armstrong's New York circle. The
Founders page for 20 Feb 1808 also opens with a clear "The", which any solution has to continue.

Not checked: the roll-14 images of the letter itself (naId 188671566, objects 29-32; not fetched), so the Founders
group list stands unverified against the manuscript; the frames 0011-0289 were skimmed for value range and pencil, not
read group by group.

## Pencil score retested over the whole roll (2026-09-16, paper preparation)

The claim above that `pencil_score.py` "located" frames 0192-0201 does not hold when the score is rerun over all
393 frames (`fetch_and_score.py`, results in `pencil_ranking.tsv`; 392 fetched, 0003 failed). The raw score is
dominated by grey blank leaves and bleed-through: 73 frames score above 0192 and 94 above 0200; the annotated
frames rank 55-110 and 286-306 of 392. Even within the 39 frames first downloaded, 0192 ranks sixth. Variants
(`score_variants.py`, `score_variants.tsv`): grey relative to page background, bright pages only, puts 0149 (the
4 May 1806 letter, which carries its own pencil decode) second and 0192 ninth; restricting to the interlinear band
within 20 px of ink puts 0192 third of 392; but 0196-0201 stay in the bottom third under every variant. So the score
can find the first, densely annotated page of a decoded despatch and nothing more. The Cryptologia draft
(`papers/cryptologia/armstrong1808.tex` section 4.2) says so; the HistoCrypt draft and `docs/armstrong.html` still
carry the older wording and need the same correction. Frames the band score ranks high and that have not been read:
0147 (a copy letter in clear with bleed-through, false positive on inspection), 0029, 0264, 0302, 0186, 0061, 0117.

## The other despatches in THE=972 (2026-10-02/03)

Status: in progress (the postscript above is finished and written up; this section extends the table to the rest of
the correspondence; on the site in docs/armstrong.html section 07, updated with the 3 Oct measures).

**Sources.** `founders_crawl.py` walked Founders' Armstrong-Madison chain through the Wayback Machine (pages in `fo/`,
index `fo/index.json`). Roll 14 (naId 188671566, 22 Jan 1808 - 14 Sept 1810) was already on disk in `img/` (665
frames; the notes above said "not fetched"). Roll 14 was paged twice: at 12 frames a sheet (`grids14/`) and by the
top fifth of every frame (`heads14/`, to read the dates), which located every coded despatch of 1808 named by Founders.
Roll 13 ends with the 15 Nov 1807 triplicate (frame 0377) and the 27/29 Dec 1807 despatch (frames 0390-0391).

Almost every manuscript carries the State Department clerk's **pencil decode** between the lines. Those decodes were
read at full frame resolution and are the main evidence now: `pencil.tsv` (about 150 group values, frame by frame).
Where Founders' group list differs from the manuscript, the manuscript is transcribed in `transcripts14.txt`
(15 Nov 1807, 27/29 Dec 1807, 5/9 Mar 1808, 6 Jun 1808, 25 Oct 1808, and the three 1810 despatches); Founders'
misreadings in the others are in `fix972.json`. `additions972.tsv` keeps the values forced by context alone (the
entries marked weak/probable/slot-misfit are not counted as sense). `sense972.json` lists, per despatch, the groups
that have a value but do not read as English. `despatches.py` measures both ways; outputs `despatches_out.txt`,
`shares.txt`, `inventory.tsv`.

**Measures.** *Known* = the group's value is attested independently of this despatch's context: the clerk's pencil
over it (in this despatch or another), Tomokiyo's 1806 known plaintext, or the 1806 pencil (`pairs.txt` H). *Reads as
sense* = has a value that is known or forced by its sentence, and the rendered word fits the English; it excludes
M-grade guesses that do not fit, additions marked weak, and the spans listed in `sense972.json`.

| despatch | groups | known: before (10-02) | known: after | sense: before | sense: after | content |
|---|---|---|---|---|---|---|
| 15 Nov 1807 (13/0377) | 58 | not in inventory | 87.9 % | - | 98.3 % | Lucien Bonaparte, "in attachment or from policy, is to marry the Queen Regent of Etruria"; "Imperial longing" for colonies "which are in its opinion necessary to France, are not on our side of the Atlantic" |
| 27/29 Dec 1807 (13/0390-91) | 243 | 69.3 % (Founders list, 225) | 86.8 % | 88.9 % given a value | 99.6 % | T[alleyran]d "dare not avow his opinion"; the Emperor "wished to get hold of the royal family of Portugal"; "a degree of wretchedness that makes even scoundrels honest", verified in the conduct of Araújo, who betrayed his master; 29 Dec: "this is mere artifice ... Russia is sincere and will be duped" |
| 15 Feb 1808 (14/0024-25) | 243 | 69.5 % | 76.1 % | 100 % given | 97.1 % | the blessings of equal alliance against Great Britain, or war; "they pick our pockets with all imaginable diligence, dexterity and impudence"; seize the Floridas |
| 22 Feb 1808 (14/0033-34) | 387 | 72.6 % | 76.5 % | 98.2 % given | 96.1 % | Gustavus; Denmark "cannot go very willingly"; Bonaparte and the crowns of Portugal and Spain; "you will have to elect between being the ally or the enemy of France"; a league of American interest, "restricted to Cuba and Mexico"; Cretet, Fouché, Talleyrand |
| 5/9 Mar 1808 (14/0039-40) | 409 | 70.8 % (Founders list, 408) | 86.6 % | 94.6 % given | 99.3 % | "Private": the letter subjoined (Lafayette's) shows the means employed for a favourable turn and the little probability they will suffice; Lafayette: Cretet obscure and contradictory, Fouché spoke well, matter adjourned; Champagny little encouragement; "Burn my scrawl ... most affectionately yours, La Fayette"; 9 Mar: the Emperor would consent to an exception to the November decree |
| 26 Mar 1808 (14/0053) | 5 | 40 % | 40 % | 100 % given | 80 % | "brigandage" (pencil) |
| 31 May 1808 (14/0083) | 4 | 75 % | 100 % | 100 % given | 100 % | "supposed to be the work of the Emperor" (Founders 472 for 972) |
| 6 Jun 1808 (14/0086) | 10 | 66.7 % (Founders, 3 groups) | 100 % | 66.7 % | 100 % | "he would become a free agent ... we can only do our duty by preparing for the worst" |
| 13 Aug 1808 (14/0120) | 27 | 70.4 % | 100 % | 92.6 % | 100 % | the moment will "enable you to do with the Floridas and your western limits whatever you please"; "no one even to ask a question on either subject" |
| 30 Aug 1808 PS (LoC) | 48 | 77.1 % | 77.1 % | 100 % given | 97.9 % | Russel, O'Mealy, Warden (the 49th group emended) |
| 25 Oct 1808 (14/0132) | 23 | 72.7 % (22) | 95.7 % | 90.9 % | 100 % | to give up Portugal "while they retain Spain"; Holland, Hanover, Brunswick "while France continues to be what it is, is not the way"; Joseph's title to the Floridas "better than none" |
| 20 Jan 1810 (14/0476) | 29 | 79.3 % | 96.6 % | 100 % given | 96.6 % | another turn; negociation with the duke of Cadore |
| 2 Feb 1810 (14/0494) | 18 | 38.9 % | 83.3 % | 100 % given | 100 % | Mr Petry; a convention on principles of reciprocal advantage |
| 17 Feb 1810 (14/0495) | 83 | 63.9 % | 79.5 % | 100 % given | 95.2 % | to justify the violence already committed on our commerce ... force or fraud |

The "before" sense column is the 10-02 "given a value" share, which was not a sense measure. Thirteen of the fourteen
items are now at or above 95 % read as sense; 26 Mar 1808 (5 groups) is at 80 %. The 20 Feb 1808 letter (369 groups)
is a different code and stays out (adjudication above).

**The five conflicts, settled by third occurrences.**
- 946: *on*. The manuscript of 22 Feb 1808 (frame 0033) writes 914 (gu) in Gu-sta-v-us; Founders' 946 is a misreading.
- 396: *while*. Pencil "while" twice on 25 Oct 1808 (frame 0132); 395 is *which*, so the 17 Feb 1810 pencil "which"
  over 396 is a slip (Armstrong's or the clerk's) one number off.
- 1260: *dou*. Pencil "doubt" over 1260.1401.578 on 27 Dec 1807 (frame 0390), as in 22 Feb 1808. The 17 Feb 1810
  "uncharitable" over 619.1260.1484.808 stays a context value of the triplicate copy only.
- 720: not settled. On 26 Mar 1808 (frame 0053) the digit is 720 or 750; the pencil "brigandage" needs *da* = 750 (H).
  Read as Armstrong's or Founders' 750; 720 = *bir* (the PS inference) is untouched.
- 1415: *ble* (pencil "blessings" on 15 Feb 1808) and *be* (1806 known plaintext); on 29 Dec 1807 the manuscript writes
  1405 (be) where Founders printed 1415, so some of the *be* readings may be Founders misreadings of 1405. Two values kept.

**Other findings.** The pencil gives 910 = *go* (twice), 240 = *master* and 1557 = *mar* in context (two values
each), 1162 = hyphen ("to-day", "to-morrow"), 896 = parenthesis, 958 and 588 = nulls (the pencil skips them), 894/959/
960/1109 = digits. Founders misreads about twenty groups in the 1807-08 lists checked here (fix972.json and the transcript
headers).

## Remaining gaps

- 22 Feb 1808, still open after the frame collation of 4 Oct 2026 (section below), each group seen once and confirmed on frame 0034: 1354 968 1494 1244 1387 (the man "of Hamburg" in the antechamber; *cou-rier* for 1244 1387 is a candidate only), 406 1216 1440 418 ("for ever the [?]-an-[?]-ose-s of Europe"; 418 *ose* is really written), 337 in "driven her [out] of her old and wise course" (the MS writes 337; a slip for 537 *out* is not supported) - blocker: too-short.
- 15 Feb 1808: the MS writes 484 and 1 where the sense needs 1484 *it* (+1116 s = *its* aggressions) and 4 *commerce*; read as Armstrong's or the copyist's slips (dropped leading 1, as 555 for 1555 in the PS), grade I - blocker: too-short.
- 15 Feb 1808: 962 inside de-x-[ter]-it-y and 1177 purp in im-pu-d-ence, both written so on frame 0024 (with 1005 *de* added above the line) - writer's slips, meanings certain.
- 5 Mar 1808: 1338 = *name* ("there are people name-d who", slot 1337 na < 1338 < 1340 native; Lafayette has named Cretet, Fouché, Champagny, Talleyrand) and 1369 = *our* ("to put our ships in requisition", adjacent homophone of 1367 or a 7/9 slip), both grade I, proposed 4 Oct 2026 - blocker: too-short.
- 26 Mar 1808: the 720/750 digit. Blocker: illegible.
- 1804-07 despatches: printed decoded in the Secretary of State Series. The group lists are on roll 13 (inventory) but
  were not transcribed in this session; they would confirm, not extend, readings for the groups above only if those
  groups occur there. Left open.
- Nothing needs physical access.

## Frame collation of 15 and 22 Feb 1808 (4 Oct 2026, contributed by Feyseel Nur, PR #21)

Frames fetched from `catalog.archives.gov/medialz/dc-metro/rg-059/603720/M34/M34-014/M34-014-00NN.jpg` (0024 = 15 Feb,
0033-0034 = 22 Feb; fair copies in a clerk's hand). Readings now attested on the frame:

| Founders | MS | reading |
|---|---|---|
| 769 **803** | 769 **805** (0034) | "stating the **dread** of his government and the means taken by it to avert the introduction into Denmark of a general army" (769 = dre, slot 765 does < dre < 771 du; 805 = ad) - closes "the dress ac[count?]" |
| 1245 | **1225** (0034; probable, the clerk loops his 2) | "consider himself **as** succeeding to dominion of her colonies" |
| 1357 755 | **1337 255** (0034; 255 probable) | **Bo-na-part-e** |
| 946 | **914** (0033) | Gu-sta-v-us (confirms the earlier correction) |
| 916 | **910** (0033) | "Denmark cannot **go** very willingly" |
| 631 (com-…-t-s) | **651** (0034) | com-**plain**-t-s; the earlier 631 in "her old and 631 course" is 631 = *wise* as written |

## 20 Feb 1808: known codes under private transforms (4 Oct 2026, contributed)

Search by OpenAI Codex, files in `feb20_known_code_search/` (REPORT.md, METHODS.md, results.json, scripts). WE028
(THE=1385; Tomokiyo's transcription) and the THE=972 table, each under direct and modular shifts, digit reversal, the
24 digit permutations, per-digit offsets, separate shifts for groups <100 and ≥100, and invertible affine maps
(19.6 M settings), scored with a character LM against 200 shuffled ciphertexts: best real z = 1.83, family-corrected
p = 0.40; no transform maps the five frequent groups (17, 18, 38, 1, 14) to the/of/and/to/a. Not the code with a
simple private transform. Digit note: groups ≥100 end in 0 (39%) and 1 (20%), 2/3/5/9 almost never (THE=972 is
uniform); a "decade-family" (inflection-digit) reading does not beat a shuffle control (45 multi-member decades
against 42.1 expected, 95% bound 47).

## Escalation

- Siblings: every coded despatch of Sept 1807 - Feb 1809 in Founders, the 15 Nov 1807 triplicate, and the three 1810
  despatches to Robert Smith were decoded.
- Clear pages / pencil: the clerk's interlinear pencil was read at full resolution on roll 13 frames 0377, 0390, 0391
  and roll 14 frames 0024-25, 0039-40, 0053, 0083, 0086, 0120, 0132, 0476, 0494, 0495 (`pencil.tsv`).
- Copies: frame 0643-44 (copy of 5 Mar) and the originals were collated against Founders.
- Known keys: decode972.py table; Tomokiyo's partial table.
- Key rebuild: `additions972.tsv` (context values) now carries only what the pencil does not cover.
- Retry: the five conflicts were retried against third occurrences (above). Not yet done: transcribe the 1804-07 group
  lists from roll 13 against their printed decodes.
