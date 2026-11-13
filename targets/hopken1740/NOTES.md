# Höpken and Carlson, Constantinople, 1740-1741: the second code, a despatch of 15/26 January 1740, the French pages of 1741 and a Latin letter signed Ibrahim Effendi (catalogue 1771 split, 2247, 2248, 2242)

Read in part, 12 Nov 2026: the despatch of 1740 and Lit. A of 1741 are read from the contemporary glosses; the two bare French
documents of 1741 are read in part with the key built from them. Written up on the site as hopken1740.html at the integration
of PRs #458 and #459. Opened 10 Nov 2026 as a split from `hopken1739` (catalogue 1771). The 1741 work (WAINUT, PRs #458 and
#459, 11-12 Nov 2026, catalogue 2245-2248) was filed as `hopken1741a` and `hopken1741b` and folded back here at the integration,
because both apply this folder's `key.tsv` byte for byte (one key, one entry; see "Integration check" at the end).

**What this target holds.** (1) The despatch of 15/26 Jan 1740, volume I/9/21, images 321-331 (Dan Bourdeau's work of 10 Nov
2026): transcribed from the Swedish decipherment of the time, 3,411 of 3,450 groups (98.9%) in confident words. (2) Lit. A,
volume I/9/26 image 147 (a French memorandum of 1741 with a French gloss): the held-out test of this key in another volume,
year and language, then read from its gloss. (3) A letter of the comte de Castellane and the start of Höpken and Carlson's reply,
volume I/9/27 images 49 and 50 left (bare, no gloss), read in part with the key extended by 24 values and 2 corrections from
Lit. A's gloss (`key_1741.tsv`). (4) Lit. B, volume I/9/29 images 81 right and 82 left (catalogue 2242, WAINUT, added
12-13 Nov 2026): a bare cipher copy of a Latin letter signed "Ibrahim Effendi", read in part with `key_1741.tsv` unchanged
(section "Lit. B of volume I/9/29" below). **Headline share: the three bare documents only, 301 of 386 words (78.0%)**:
188 of 217 (86.6%) for the two French documents of 1741 and 113 of 169 (66.9%) for Lit. B; the glossed pages are where
the key comes from and are not counted in it.

Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/9/21 (R0003582). Two copies of the same despatch, both marked
duplicate, in the same encipherment: images 321-331 (the chancery decipherer struck the groups through and wrote the
Swedish plaintext above; signed "Pera i Constantinopel d. 15/26 Jan: 1740", C. F. v. Höpken, E. Carlson) and images
332-342 (332-333 glossed, 334-342 bare; note on 332 "ankom med en express d. 5 Maji 1740"). It reports the conclusion
and exchange of the Swedish-Ottoman defensive alliance treaty.

## Why a separate target

This is a different code from the French-glossed enclosures of `hopken1739` (images 255-261): groups run to about 1999
(1774, 1800, 1825, 1868, 1869 are plain on image 326) against at most 1749 there, and values clash (1532 = Suède there, a
syllable inside Swedish words here; "Credit" is enciphered differently). One key, one entry.

## Transcription and pairing

- Pass 1 (two AI agents, gloss in view) on 322-327: pairs_322_324.tsv, pairs_325_327.tsv; rough, superseded, kept for the record.
- Pass 2: word-level pairs from full-size crops, five AI agents (wordpairs_*.tsv, images 321-331): each gloss word with
  the groups under it and a segmentation, one piece per group. K = digits and reading confident, X = doubtful, C = clear text.
- Pass 3: the X lines of 322-327 rechecked on high-zoom crops with the key (94 lines, 63 settled).
- **Second copy as a blind control.** The bare copy on 332 and 334-342 was transcribed digits-only by three agents told
  to open no other file (bare_332_336.txt, bare_337_339.txt, bare_340_342.txt; 3,082 groups). 2,987 (97%) are identical
  in sequence to the glossed copy. At each one-for-one difference where the bare group was not doubtful, the bare digit
  was taken (scripts/apply_bare.py; 25 + 91 groups, each noted in the pairs' note column): the differences are almost
  all 5/6, 2/8 and gutter-cut digits under the strike-through of the glossed copy, and the bare digit is the one that
  agrees with the key. Image 333 (a second glossed copy of the text of 322) is not transcribed; it was consulted for
  three lines of 322.
- Pass 4: the 63 lines still X rechecked against both copies; 51 settled, 1 reclassed as clear text, 11 remain.
- Judgement calls, all noted in the pairs: in five lines the groups spell a different word from the gloss (dertil/derwid,
  öfwer/om, af/om, är den/är det, en orsak/orsaken) and at 327 r06 the gloss "hwarpå" stands over groups that spell
  "wärde"; three words have no gloss and are restored from confirmed values ([derom], [til], [ej]); [tre] (327 r05, gloss
  blotted) and [söka] (328 r16, no gloss) are restored from key values; "22 Decembre" (324 r04) rests on a doubled
  group 1865 and the gloss "d. 2".

## Key and tests

scripts/make_key.py takes the most frequent piece per group from the K lines (a/å/ä and o/ö folded: the code does not
distinguish them; i/j and u/v are one letter each). Final key.tsv: 235 confirmed, 15 mixed, 78 single. A syllabary with
word codes (1516 Ott: Porten, 1413 Kongl. Majt, 1171 Ambassadeur, 1450 alliance, 1526 negociation, 1360 tractat, 1256
Ryssland, 1123 Franckrike, 1265 Swerige, 1902 Tessin, 1915 Reis Effendi, 1287 Stor Viziren, 1560 Sultan, 1179 Venedig,
1669 subsidier). Groups above 1749 are ordinary syllables. No nulls. Homophones for common letters and syllables.

Held-out test (scripts/heldout_test.py): a key built from 322-325 only was frozen before the 326-327 pairs came back
(key_frozen_322_325.tsv, FROZEN.sha256). On the K lines of 326-327 as first paired: 598 groups, 522 in the key, **457
(76% of all, 88% of those known) give exactly the piece the pairing assigns**; shuffled-key control mean 3.5, maximum
33 of 500. Caveat: the agent pairing 326-327 had seeds.tsv and worked where wordpairs_324_325.tsv already lay, so the
test is not strictly blind. The same frozen key on 330-331 gives 517 of 591 (87%), but that agent had key.tsv in view;
it is a consistency figure, not a held-out one.

## Outcome

3,450 groups on images 321-331; 3,411 (98.9%) lie in words whose digits and reading are both confident, 39 in 11
doubtful words (scripts/make_texts.py prints the count). reading_sv.txt is the Swedish text in order, translation_en.txt
the English, decryption.txt the key applied group by group, transcription.txt the groups. This is the contemporary
decipherment transcribed and checked against a rebuilt code list and a second copy; it is not a break of bare cipher.

## The 1741 volumes (PRs #458 and #459, WAINUT)

Work of 11-12 Nov 2026 by AI language-model agents (no human palaeographer), contributed by WAINUT (PRs #458 and #459). Four
Riksarkivet volumes of Diplomatica Turcica were paged from the images the catalogue names (2245-2248), and two documents of
1741 were worked in full:

| Volume | Images | Document | Groups | State |
|---|---|---|---|---|
| I/9/26 (R0003635), catalogue 2247 | 147 | "Lit. A", French memorandum on the last Russo-Ottoman treaty, enclosure to the despatch of 24 Feb / 4 Mar 1741; glossed | 282 | read (contemporary gloss, checked against the frozen key) |
| I/9/27 (R0003636), catalogue 2248 | 49, 50 (left page) | Cipher copy of a letter of the comte de Castellane, French ambassador, and the start of Höpken and Carlson's reply; received 2 Oct 1741; bare, no gloss | 205 + 269 | letter and reply: read in part |

Both are in the code of the despatch above (four-digit groups 1006-1915). These are the first French texts read in that code and
the first bare passages read with it outside volume I/9/21.

## Collision check (11 Nov 2026, again 12 Nov before finishing)

Dan's repo, origin/main 54c4ecc65: targets `hopken1739` and `hopken1740` (both on volume I/9/21, R0003582) are the only
Höpken targets; no target, note or sweep row beyond the catalogue entries names R0003590, R0003628, R0003635 or
R0003636. Open PRs (#391-#434): none on Höpken, Carlson or Diplomatica Turcica. Issues and PRs searched for "Höpken"
and "Hopken Carlson Constantinople": only our merged #236 and Dan's merged #379. No collision. Rechecked on 12 Nov
2026 when packaging (origin/main 4a71baf89; main at 8e98a2e43 checked through the GitHub API, site rebuilds only):
targets/ still has only hopken1739 and hopken1740; open PRs #391-#451 and PR searches for Höpken, Hopken, Castellane,
Carlson Constantinople, Diplomatica Turcica, R0003635 and R0003636 show nothing new. No collision.

## Prior art (checked 11-12 Nov 2026)

Two web searches (Höpken, Carlson, Constantinople 1739-40, despatches, cipher; Castellane, Constantinople 1741,
Romanzof, congrès, Grand Vizir, lettre chiffrée). Found: background on the embassy (Höpken envoy 1738-42, Carlson to
1745; the defensive alliance of Dec 1739) and that Castellane's own correspondence for 1740-47 is in the French
diplomatic archives (Nantes, Constantinople embassy series). No edition or decipherment of these letters. The
catalogue entries record known.py, DECODE (Nordic dump) and a web search on 4 Nov with nothing found. **Castellane's
original letter, and the reply as received, may survive in clear in the Nantes series: a possible crib, not checked.**

## Survey of the four volumes (images named by the catalogue, viewed at 1200 px)

- **I/9/24 (R0003590, 1735-39, catalogue 2245).** Image 40 (Pera 20/31 Oct 1735): about 90 groups glossed in
  Swedish, all below 1750, in the **first code** of `hopken1739` (1684 alliance, 1584 traité and 1532 Suède/Swerige
  sit under the gloss as in hopken1739's French pages). Image 106: a few glossed Swedish runs, same range. Image 139
  (July 1738): a bare paragraph of about 200 groups below 1750 inside a clear letter. Image 205: no cipher (a clear
  Swedish letter of 1739 and an English recommendation). Not worked: this is the hopken1739 code, which has only 85
  confirmed values; image 40 is a held-out page for it, and 139 is bare text for it.
- **I/9/25 (R0003628, 1740, catalogue 2246).** Image 8: Swedish gloss over groups up to 1898 (second code). Image 53:
  two pages of mostly bare four-digit groups (second code range). Image 99: a **three-digit** number code (groups
  about 100-900) in a Swedish letter, a different system again, not matched here. Image 329: a letter received 7 Nov
  1740 with a short glossed run. Not worked.
- **I/9/26 (R0003635, Jan-Jun 1741, catalogue 2247).** Images 8, 54, 100, 240, 286: Swedish despatches with glossed
  runs (second code). Image 147: Lit. A, worked (Lit. A, below).
- **I/9/27 (R0003636, Jul-Dec 1741, catalogue 2248).** Image 8: glossed Swedish runs. Images 49-52: the bare French
  copy of the exchange with Castellane, about 2,000 groups over seven pages; 49 and the left page of 50 worked
  (the Castellane exchange, below). Image 93: bare pages. Image 135: partly glossed.
- Catalogue 2241 and 2244 (volumes I/9/23, I/9/28) were not opened in this survey; 2242 (I/9/29) was opened later
  for Lit. B (section "Lit. B of volume I/9/29" below).

## Method

1. Sign conventions (SIGN_CONVENTIONS.md) set in the pass-file headers before any decoding.
2. Two passes per page: pass 1 from bands at 0.6-0.75x of the full-size image, pass 2 from fresh crops at 0.9-1.0x
   (quadrants or halves), disagreements settled on 2x crops. Image 49: 3 disagreements (1638/1688, 1840/1340,
   1583/1505), settled 1688, 1840? and 1585. Image 50: 2 (1670/1678 and a blotted third digit), kept doubtful as 1678?
   and 1613?. Image 147: no digit disagreement; pass 2 added two strokes over 1500 (à); one group kept as 1678?, one
   as 1442?. Honest caveat: on image 147 the gloss is written between the rows and was in view; the digits were read
   before any decoding, and no digit was changed toward the gloss. Images 49-50 have no gloss. One agent did both
   passes (a second agent was not available in this run), so the passes are not fully independent.
3. Key: `key.tsv` of this folder, the hopken1740 key (328 groups; 235 confirmed), unchanged (sha256 c4e208fe...8ef1ac, recorded in FROZEN.sha256).
4. **Held-out test (scripts/heldout.py) on Lit. A**, a page from another volume and in another language than any page
   the key was built on: each run of groups is aligned to its gloss by dynamic programming. **222 of 282 groups (79%)
   give exactly the letters of the gloss at their place; 242 groups are in the key, so 92% of those known.** With the
   key's values shuffled among its groups: mean 33.4, maximum 51 over 200 shuffles. Word codes were compared through a
   fixed list of equivalents stated in the script (tractat=traité, ottporten=Porte, ...); letters normalised (j=i,
   u=v=w, accents dropped).
5. key_1741.tsv (working key) = key.tsv + 24 values read from the Lit. A gloss (status gloss_1741a: 1741 u, 1718 ir,
   1529 che, 1521 y, 1703 va, 1702 us, 1527 qu', 1789 tra, 1769 eur, 1566 plu, 1797 vre, 1283 lu, 1652 ix, 1043 cle,
   1175 qui, 1423 sui, 1712 ir, 1877 fro, 1027 oient, 1442 é, 1439 glé, 1183 ég, 1824 is, 1832 prince) + 2 frozen
   single values corrected on the same gloss (1504 r -> vo, three places; 1840 a -> au/av, two places).
6. The bare letter (the Castellane exchange, below) was decrypted mechanically with key_1741.tsv (scripts/decrypt.py) and read in French;
   every departure is marked, and scripts/check_marks.py rebuilds the decryption and fails on any unmarked departure
   (it passes for all three documents; a tampered reading fails, tested).
7. Consistency check on the bare letter, not a formal held-out test: while first decoding image 49 with the frozen
   key, values for eight groups unknown or odd in that key were proposed from the sense (1741 u, 1718 ir, 1504 vo,
   1529 che, 1521 y, 1703 va, 1840 au, 1702 us) before image 147 was decoded; all eight were then found in the Lit. A
   gloss with the same value. These proposals were noted in the working session, not frozen in a file. Three further
   context values were proposed on the Castellane letter and then recur, with the same value making sense, in the
   reply: 1478 eu (il y a eu, sieur / Dieu), 1452 jo (aujourd'hui / joie), 1605 où (où il / où se trouve).
8. Dan's reading checker (docs/_check_reading.py --file, run in a throwaway worktree of origin/main): clean-sentence
   share 0.909 for Lit. A (10 of 11 sentences), 0.444 for the Castellane letter (4 of 9), 0.615 for the reply (8 of
   13; 0.643, 9 of 14, before the review fix joined two sentences at "auxquels"). It counts each word written as `[?word]` (a context-guessed value) as a hole; the Castellane letter's
   sentences are long and carry 2-4 such words each.

## Word counts (scripts/check_marks.py)

| Document | Cipher words | Verbatim from key | Marked repair | Guessed (context) | Holes |
|---|---|---|---|---|---|
| Lit. A (against the frozen key) | 122 | 84 (68.9%) | 3 | 35 from the gloss (not guesses) | 0 |
| Castellane letter (key_1741.tsv) | 94 | 79 (84.0%) | 2 | 13 | 0 |
| Reply, to foot of 50 left (key_1741.tsv) | 123 | 109 (88.6%) | 3 | 10 | 1 |

Word codes rendered in French (grefwen = comte, storviziren = Grand Vizir, ottporten = Porte, hof = Cour, swerige =
Suède, ryssland = Russie, frankrike = France, fred = paix, tractat = traité) are counted as verbatim. Lit. A: all 122
words are covered by the contemporary gloss; the cipher differs from the gloss in four places (notes in
about_reading_lita_1741.txt).

## Independent review (12 Nov 2026)

An AI language-model agent that took no part in the solve reviewed the 1741 work blind (it was then two folders). It read 92 groups from its own
crops before opening the transcriptions (image 147 rows H05 and the end of H08; image 49 rows L04, L07, L12; image 50
left rows M08, M14): no disagreement, and the two doubtful groups it met (49 L07 1840?, 50 M14 1613?) are the ones
marked. It confirmed that the key applied frozen is byte-identical to origin/main targets/hopken1740/key.tsv, reran
decrypt.py, check_marks.py and heldout.py with the same results, and read each text as sentences against its
translation: Lit. A read, grade A; Castellane letter read in part, grade B; reply read in part, grade B (recorded as
`reading_review` in each profile.json). Fixes made on its findings:

- Reply M03-M04: the change `Au{x/ssi}` (1828 read as "ssi", "aussi") is dropped. 1828 = x is confirmed 5/5 in the
  frozen key, and the mechanical text reads "... au sujet des intérêts de notre Cour, auxquels personne n'est plus
  capable de contribuer dans ce pays [1515] qu'un ambassadeur de France". Reply counts: 109 verbatim (was 108),
  3 repaired (was 4).
- Castellane letter L12: the cipher la-ri-a-[1409]-le gives "lariaille" with 1409 = il, so "le sieur de Laria aille"
  uses one a twice. The second a is now marked `{+a}` in the marked file and the reading. Counts unchanged.
- Lit. A translation: notes that the cipher has "couvre" for "découvre".

The reviewer left `con{ha/grè}s` (1496) as it is: marked, plausible, and listed as open.

## What the bare letter says

Castellane writes that there was a general divan at the Porte that day, after which the Porte's dragoman invited him,
on behalf of the Grand Vizier, to a kind of congress next Sunday at which "Monsieur de Romanzof" (very probably
Aleksandr Rumyantsev, the Russian ambassador) would be present; he asks the Swedes for any reflections on their
interests before "le sieur de Laria" goes to the Porte's dragoman at eight next morning. The reply thanks him for his
generous conduct toward the interests of the Swedish court, announces a visit next evening to set out "nos pensées sur
les intérêts présents de la Suède relatives à la Russie", and begins: in the critical situation of Sweden with Russia
(Sweden had declared war in summer 1741), any accommodation between the Porte and Russia is ... (breaks off).

## Lit. B of volume I/9/29 (catalogue 2242, WAINUT, 12 Nov 2026)

Work of 12 Nov 2026 by AI language-model agents for WAINUT (no human palaeographer or Latinist). It uses this folder's
keys unchanged, so it is filed here (one key, one entry). File names carry the suffix `_litB`.

**Result: read in part.** A bare cipher copy of two pages (494 groups, 169 cipher words), decrypted with `key_1741.tsv`
and read as Latin from the salutation to the address: 113 words verbatim from the signs (66.9%), 13 with a marked change
(74.6% together), 40 resting on values guessed from sense, 3 holes. The other texts of this folder are Swedish and
French; this one is Latin.

### Document

Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/9/29 (Beskickningshandlingar 1736-1746), image series R0003653.

- Image 81, right page: headed "Doupplette" and "Lit. B"; a heading row (B00) and 18 rows of four-digit groups (B01-B18),
  no gloss, no clear words. https://sok.riksarkivet.se/bildvisning/R0003653_00081
- Image 82, left page: the verso of 81 right (the heading at its top is show-through of 81, mirrored); 11 rows (C01-C11),
  ending with a flourish. https://sok.riksarkivet.se/bildvisning/R0003653_00082
- IIIF: `https://lbiiif.riksarkivet.se/v3/arkis!R0003653_00081/full/max/0/default.jpg` (and `_00082`); manifest
  `https://lbiiif.riksarkivet.se/arkis!R0003653/manifest`. Fetched one at a time, 1.6 s apart, User-Agent
  WAINUT-research; no 429, no bot check. Scans are not in git.

The cipher gives the signature "Ibrahim Effendi" (C08) and the address "Excellentissimo Domino Domino A[h]me[t] [1909],
Domino nobis observantissimo" (C09-C11; two letters of the name rest on guessed values and group 1909 is unread). The
pages carry no date; the volume runs 1736-1746, and the profile's year 1740 is an estimate from the subject (inferred). The catalogue entry (vetting of 6 Nov 2026) describes images 79-85 as French cipher; the text of
81-82 is Latin.

Content (translation_litB.md): the writer has explained again and again what the addressee told him about the boundaries
to be marked and about the law and custom for dividing the islands; the "legatus Germaniae" (probably the Imperial
envoy; inferred, the text gives only the title) was astonished and did not know what to answer; the writer expects him
to stop disputing about the islands and to accept everything today or tomorrow, "because it cannot be otherwise"; he
was given leave to call on the addressee but was summoned early and kept at the Porte until evening, and asks to be
excused. If the islands are those of the Danube and Sava, this is the frontier settlement after the Treaty of Belgrade
(1739); that is an inference and was not checked.

### Key

Both keys of this folder, unchanged: `key.tsv` (the frozen key: 328 entries, 329 lines with the header; sha256
c4e208fe...8ef1ac, as in FROZEN.sha256) and `key_1741.tsv` (the work key: 352 entries, 353 lines; key.tsv plus 24 values
and 2 corrections from the Lit. A gloss; sha256 865cbb5e...036d2d7e). No value was added to either file from Lit. B.

Values proposed from sense for groups that are in neither key are written `[?x]` in the reading. 31 distinct groups
are guessed, at 46 places; none of them is given two different values. Ten groups recur: 1773 qua (5 places: quae x2,
qualis, quasi, quamprimum), 1186 quo (3: quod x3), 1103 um (3: iterum, desiderium, vacuum), 1452 io (2: responsio,
responsionem), 1152 pt (2: acceptaverit, acceptare), 1462 spu (2: disputatio, disputabit), 1401 ip (2: ipsi, ipse),
1306 o (2: debeo, maneo), 1632 t (2: dederant, A[h]met), 1056 mu (2: communicabo, quamprimum). 21 occur once: 1866 ne,
1539 sue, 1547 stri, 1238 super, 1724 sci, 1261 de, 1530 ld, 178? tra (the last digit is in the torn edge; 1789 = tra in
key_1741.tsv), 1307 ul, 1038 aver, 1406 se, 1885 no, 1353? me, 1619 jus, 1682 t, 1567 venia, 1286 ig, 1336 sca, 1468 gnu,
1656 pri, 1640 h. One group that is in the key, 1067 (the word code ryska), is read as the syllable rna in "hesterna";
the sense is sure but the value is a guess, marked `{ryska/?rna}` and counted as a guess.

Marked changes of key values (13 words): 1461 fi read ni twice (Germaniae, omnia; fi is right in confiniis x2 and
fieri; 1451 = ni, a 5/6 slip is possible); 1471 ga read ia twice (jam, licentiam; key_1741.tsv already records ja once
for 1471); 1602 wa read ut; 1825 att read at (respondeat); 1128 ce read l (vel; 1128 = ce in every ex+ce+l+en+ti of this
letter, so probably a slip of the encipherer); 1802 up read op (opus); 1834 ba read pe (vesperas); 1561 ge read to (toto); and three
letters added with no group: {+di}xit, soe{+p}issime, {+i}d est. Two further changes sit in words counted under other
headings: 1013 ma read ac in acceptaverit (counted as guessed; 1031 = ac, a transposition?), and the B09 pair
`{sla/...} {ce/...}` (counted as a hole). The word code 1516 ottporten is
rendered Porta and counted as verbatim, as in the 1741 pages.

### Transcription

SIGN_CONVENTIONS_litB.md was written before any digit was read. Each page was transcribed twice on different crop grids
(pass 1: 4 bands x 2 halves at about 1x; pass 2: 3 bands x 3 columns at 1.25x), digits only, without the key.
Disagreements: 2 in 494 groups (B15 g6 1353/1383 -> 1353?; C02 g15 1135/1136 -> 1135?), settled as far as possible on
2.5x crops. B09 g18 is 178? (last digit in a tear). Caveats: one agent did both passes, so they are not fully
independent; image 82 was transcribed after the decryption of image 81 had been seen.

**Two groups corrected after the blind review** (both passes had the first reading; the reviewer read the image):

- C10 g4: 1624 -> 1024. At 4x the second digit is a 0 with a short tail, without the tall looped ascender this hand
  gives every 6 (1632 and 1764 in the same row). 1024 = mi, so "Domino" is now verbatim (it was the repair
  `Do{puissance/mi}no`).
- B15 g16: 1496 -> 1495?, kept doubtful. The last digit has the closed bowl and top flag of this hand's 5 (as in 1655'
  of the same row). 1495 = ho (as in B13 "hodie"), so the word is now verbatim (it was the repair `{ha/ho}die`).

Both corrections are noted in transcription_litB.txt and transcription_litB2.txt; the pass files are left as written.

### Held-out figure

There is no gloss on these pages, so no blind test is possible. What can be measured: the frozen key (`key.tsv`) was
built from another volume and another language (the Swedish despatch, vol. I/9/21) and never saw these pages. Applied
unchanged (`scripts/heldout_litB.py key.tsv transcription_litB_all.txt marked_litB.txt`), it knows 434 of the 494 groups,
and at **419 of them its value is the one the Latin reading uses (96.5% of the groups it knows, 84.8% of all groups)**;
with its values shuffled among its groups (500 shuffles) the same count has mean 2.0 and maximum 28. Per page: image 81,
269 of 322 groups (83.5%; 95.7% of the 281 it knows; shuffled mean 1.3, maximum 21); image 82, 150 of 172 (87.2%; 98.0%
of the 153 it knows; shuffled mean 0.7, maximum 8). This is a consistency figure, not a blind test: the reading was made
with the key in view. In addition, five values that `key_1741.tsv` took from the Lit. A gloss (1175 qui, 1702 us, 1703 va,
1283 lu, 1504 vo) occur 13 times here, and at 13 of the 13 places they give the value the Latin reading uses;
`scripts/check_marks_litB.py` run against `key.tsv` instead of `key_1741.tsv` fails at exactly these 13 places.

### Reading and word counts

decryption_litB.txt is the mechanical decryption with key_1741.tsv (`scripts/decrypt_litB.py`). marked_litB.txt is the
reading piece by piece; `scripts/check_marks_litB.py` rebuilds the decryption from transcription_litB_all.txt +
key_1741.tsv and passes ("OK: no unmarked departure"); an unmarked change fails it (tested). reading_litB.md gives the
Latin sentences with the marks, translation_litB.md the English with the same holes. The `_litB` scripts are copies of
this folder's decrypt.py and check_marks.py with three additions, so that the existing scripts are left unchanged: a
group with a lost digit (178?), `{x/...}` (key value gives no sense, counted as a hole) and `{x/?y}` (key value replaced
by a guess, counted as a guess).

| Page | Cipher words | Verbatim from key | Marked change | Guessed (context) | Holes |
|---|---|---|---|---|---|
| Image 81 right (B00-B18) | 112 | 69 (61.6%) | 11 | 30 | 2 |
| Image 82 left (C01-C11) | 58 | 45 (77.6%) | 2 | 10 | 1 |
| Lit. B, whole | 169 | 113 (66.9%) | 13 | 40 | 3 |

One word ("Excellentiam", B18-C01) runs across the two pages and is counted on both in the per-page rows. 4 words contain
a doubtful digit (1353?, 1135?, 178?, 1495?). The 3 holes are [1463] (B17), [1909] (C10) and one two-group word in B09.

Dan's reading checker (`docs/_check_reading.py --file`, origin/main 65cdcd9d5, in a throwaway worktree removed after):
reading_litB.md, language detected Latin, 23 sentences, 8 clean, **clean share 0.348**; translation_litB.md 25 sentences,
22 clean, 0.88. This is below the checker's 0.45 line. Two diagnostics, not the submitted reading:
`work/litB_reading_recurring_unmarked.txt` (the `[?]` mark dropped on the ten recurring guessed values, which hold at
every place, and kept on the 21 single ones, as CONTRIBUTING.md allows) scores 0.391 (9 of 23); `work/litB_reading_unmarked.txt`
(every mark dropped) scores 0.538. The submitted reading keeps all marks, because the recurring values are not confirmed
by a contemporary text. The checker's Latin word list lacks several ordinary words of this letter (among them
excellentiam, maneo, explicavi, respondebit, vesperas, obsequia), so it understates the reading; the state rests on the
reviewer reading the sentences (below). We propose "read in part" because the verbatim share (66.9%) is far below 95%
and 40 words rest on guessed values; the true holes are 3.

### Independent review (12 Nov 2026)

An AI language-model agent that took no part in the solve reviewed Lit. B blind. It copied seven rows from the image
before opening the transcription (B05, B08, B12 and B15 on image 81; C06, C09 and the first part of C10 on image 82;
about 115 groups): 2 disagreements, both corrected above (C10 g4, B15 g16); the other doubtful groups it met (B12 g18
1401, B15 g6 1353?) agree. It reran decrypt, check_marks and heldout with the solver's results, confirmed that both
keys are byte-identical to this folder's `key.tsv` and `key_1741.tsv`, and read reading_litB.md as Latin sentences
against translation_litB.md: "real Latin chancery prose" that follows through from the greeting to the address; grade
B, read in part. Of 10 units (greeting, 7 sentences, signature, address) it counts 9 clean if only true holes count,
1 if every `[?x]` counts as a hole, and about 4 if the consistently recurring guesses are taken as read. Fixes made on
its findings: the two digits above; `{ryska/rna}` reclassed as a guess (`{ryska/?rna}`); counts and the checker figure
updated. Its other doubts are listed in the gaps below.

### Prior art (checked 12 Nov 2026)

Catalogue entry: known.py, DECODE (Nordic dump), Tomokiyo and Lasry, 4-6 Nov 2026, nothing found. Two web searches on
12 Nov 2026 ("Ibrahim Efendi" Latin letter, Swedish envoy, Constantinople 1740, Danube islands, Belgrade treaty;
"Ibrahim Efendi", Höpken, Carlson, boundary commission): background only, on the delimitation of the frontier across the
Danube islands after the Treaty of Belgrade. No edition, printing or decipherment of this letter found.

### Collision check

12 Nov 2026 at the start and before finishing, and again on 13 Nov 2026 when packaging: origin/main and GitHub main
65cdcd9d5 (12 Nov 21:56 UTC). targets/ has hopken1739 and hopken1740 only for this legation; no target, note or PR names
catalogue 2242, Ibrahim Effendi or the Lit. B pages; R0003653 and I/9/29 occur only in the sweep and vetting files of
research/ (sweep D, vetting n05). Open PRs (#391, #494-#500): none on Höpken or Diplomatica Turcica. No collision.

### Files added for Lit. B

SIGN_CONVENTIONS_litB.md; transcription_litB.txt (image 81, with _pass1 and _pass2), transcription_litB2.txt (image 82,
with _pass1 and _pass2), transcription_litB_all.txt (both pages, the file the scripts use); decryption_litB.txt,
marked_litB.txt, reading_litB.md, translation_litB.md; scripts/decrypt_litB.py, check_marks_litB.py, heldout_litB.py,
pairs_litB.py; work/litB_reading_unmarked.txt and work/litB_reading_recurring_unmarked.txt (checker diagnostics).
Rebuild from this folder (standard library only):

    python scripts/decrypt_litB.py key_1741.tsv transcription_litB_all.txt decryption_litB.txt
    python scripts/check_marks_litB.py key_1741.tsv transcription_litB_all.txt marked_litB.txt
    python scripts/heldout_litB.py key.tsv transcription_litB_all.txt marked_litB.txt

## Remaining gaps

- 7 words with a value conflict (322 r15 i, 324 l01 Ryska gränsen, 325 l14 bewijs, 326 l01 slutande, 328 r08 försäkra, 328 l09 aldrahögstes, 328 l18 allernådigst) - blocker: open-codes; both copies agree on the digits, the word reads from the gloss, probably slips of the encipherer or a homophone not separated
- 3 words where the split between groups is unknown (327 r06 "1500", 330 l08 willkor, 331 l14 pröfwas) - blocker: open-codes; 1640, 1689, 1771 not fixed
- 1 gloss unread (323 l08, a name over 1313, looks like "v: Haren") - blocker: open-codes; single occurrence, clear in both copies
- A few clear (unenciphered) words are doubtful in the hand (330 l02-03, r02, r03; 321 inserted word) - blocker: illegible
- Context values in the Castellane exchange not confirmed by a gloss - blocker: open-codes; 1026 Monsieur (2), 1286 V[otre] (3),
  1520 cha (2), 1478 eu (3), 1452 jo (2), 1605 où (2), 1339 zo, 1438 f (in Romanzof), 1083 flé, 1056 mu, 1409 il,
  1508 ai, 1581 eux, 1326 ux, 1733 ns, 1747 cri; changed value {ha/grè} (1496, congrès).
- 1515 (reply, M05) unread - blocker: open-codes; one place only.
- "Laria" (49 L12) - blocker: open-codes; la-ri-a-[1409]-le gives one a for two words (marked `{+a}`), or the name is
  "Lari". The reviewer recalls a dragoman family of this name at the French embassy; not checked.
- The 13 guessed words of the Castellane letter - blocker: open-codes; Dan's checker gives 0.444, just under its 0.45
  line, because each `[?word]` counts as a hole. The reviewer reads all four sentences as holding and grades the letter
  read in part (B); if the line is held strictly, "decoded, not read" is the fallback the reviewer names but does not
  recommend.
- Doubtful digits - blocker: illegible; 49 L07 1840? (3 or 8), L10 1227?; 50 M01 1678? (0 or 8), M14 1613? (blot,
  1613 or 1633); 147 H11 1678?, H16 1442? (a figure written below). Kept doubtful on 2x crops.
- Castellane's side of the exchange in the French archives (Nantes, Constantinople embassy series: his correspondence of 1740-47 is listed in the inventory) - blocker: needs-physical-access; the clear originals, if they survive, would be a crib; not searched beyond the inventory entry.
- A human second reader of the digits and the French - blocker: needs-physical-access; both passes of the 1741 transcription were by one agent and every reader so far was an AI agent; the blind review spot-checked 92 groups on images 147, 49 and 50 and the integration about 300, with no disagreement.
- Lit. B, B09: two groups, 1673 (sla, a single value in the key) and 1128 (ce), give no sense ("..., [...] de confiniis"); perhaps "nec", not adopted - blocker: open-codes
- Lit. B, [1463] (B17, "licentiam [1463] hesterna die") and [1909] (C10, after the addressee's name, perhaps a title or a name code) unread - blocker: open-codes; one place each
- Lit. B, the 40 words resting on guessed values - blocker: open-codes; 31 groups guessed from sense at 46 places (10 groups recur and hold at every place, 21 occur once); single guesses carry content ([?super], [?de], [?me] [?jus]sit, [?venia]m, [?aver]); `{ryska/?rna}` in "hesterna" (sense sure, value guessed); they should be checked against a glossed page of this code before they enter a key. Dan's checker gives 0.348, under its 0.45 line, because each `[?x]` counts as a hole; the reviewer reads the letter as Latin sentences and grades it read in part (B)
- Lit. B, `ve{ce/l}` (B13) goes against a firm key value (1128 = ce in every ex+ce+l+en+ti of the letter) - blocker: open-codes; probably a slip of the encipherer, marked
- Lit. B, the addressee "A[h]me[t] [1909]" - blocker: open-codes; two letters rest on guessed values (1640 h; 1632 t, which also gives "dederant") and 1909 is unread. Who the writer and the addressee are is not established, and no identification is proposed
- Lit. B, doubtful digits - blocker: illegible; B15 g6 1353? (3 or 8), B15 g16 1495? (5 or 6, corrected from 1496 after the review), C02 g15 1135? (5 or 6), B09 g18 178? (last digit in a tear)

## Not part of this target (not worked)

The following were surveyed or left aside and are not unread pieces of the documents above: the rest of the Castellane exchange (the right page of image 50, images 51 and 52, about 1,500 bare groups in the same code; the reply read here breaks off at the foot of the left page, and the remainder is a document of its own that is not transcribed); the first-code pages of I/9/24 (images 40, 106 glossed, 139 bare; image 40 would be a held-out page for the hopken1739 key) and the glossed second-code runs of I/9/25-27 (images 8, 54, 100, 240, 286, 329, 135), which are the material that would confirm the context values above; the three-digit number code of I/9/25 image 99 (a different system); the continuation of Lit. A beyond image 147; catalogue 2241 and 2244 (volumes not opened); in I/9/29 (catalogue 2242), the pages around Lit. B: images 78-80 (French cipher with clear words; image 79 right headed "2. Lit. [?]"), 82 right (headed "Doublette") and 83-85 (further bare pages), none transcribed, and image 56 (a small-number cipher with a Swedish gloss, another system), not worked. The original (non-duplicate) copy of Lit. B, and any Lit. A beside it, was not looked for beyond images 78-86 of I/9/29; a second copy would be a separate witness that could settle the doubtful digits of Lit. B.

## Escalation

- [x] siblings: images 78-86 of I/9/29 paged at 1600 px around Lit. B (listed under "Not part of this target"); the leaves before and after the despatch opened, its second copy (332-342) used as a control; the four volumes named by catalogue 2245-2248 paged at 1200 px, and the glossed Lit. A page of I/9/26 used as held-out test and key extension for the bare pages of I/9/27
- [x] clear-pages: the gloss is the decipherment on the despatch and on Lit. A; images 49-50 checked for a gloss or a clear copy (none)
- [x] known-keys: Lit. B read with this folder's key_1741.tsv unchanged, frozen key.tsv held out (419 of 494 groups); not the hopken1739 code (values clash; recognised on I/9/24 but not applied); the stade1710 key does not fit; this folder's key applied frozen to the 1741 pages
- [x] print: two web searches of 12 Nov 2026 for Lit. B (Ibrahim Efendi, the islands, the Belgrade frontier): no edition; web searches of 10-12 Nov 2026, repeated at the integration (Castellane, Höpken, Carlson, the congress): no edition or decipherment; the Nantes inventory lists Castellane's correspondence of 1740-47, which was not opened
- [x] key-rebuild: the despatch's key frozen and tested (235 confirmed values) and extended by 26 values from Lit. A's gloss; for the 1741 bare pages the remaining context values rest on the sense (listed in the gaps, open-codes); the glossed runs that could confirm them are outside this target (above)
- [x] retry: the despatch's doubtful lines rechecked twice (11 remain); 1515 and the doubtful digits of the 1741 pages retried on 2x crops (kept doubtful), and about 300 groups of images 49 and 147 compared again at the integration


## Image sources

https://lbiiif.riksarkivet.se/arkis!R0003582_00NNN/full/max/0/default.jpg, NNN = 319-342, fetched one at a time; scans/
is git-ignored.

## Image links (1741 volumes)

IIIF manifests: https://lbiiif.riksarkivet.se/arkis!R0003590/manifest , ...!R0003628/manifest ,
...!R0003635/manifest , ...!R0003636/manifest. Images: https://lbiiif.riksarkivet.se/v3/arkis!R0003636_00049/full/max/0/default.jpg
(and _00050; R0003635_00147). Viewer: https://sok.riksarkivet.se/bildvisning/R0003636_00049 , _00050 ,
https://sok.riksarkivet.se/bildvisning/R0003635_00147 . Fetched one at a time, 1.6 s apart, User-Agent
WAINUT-research (scripts/fetch.py); no 429, no bot check. Scans are in scans/, not for git.

## Files added by the 1741 work

SIGN_CONVENTIONS.md (for the 1741 pages); transcription_lita_1741.txt (with _pass1 and _pass2), gloss_lita_1741.tsv,
pairs_lita_1741.tsv, decryption_lita_1741.txt (frozen key), marked_lita_1741.txt, reading_lita_1741.md,
translation_lita_1741.md, about_reading_lita_1741.txt, work/lita_keytsv.txt; for the Castellane letter and the reply
transcription_*_oct1741.txt (with passes), decryption_*, marked_*, reading_*, translation_*, about_reading_*;
key_1741.tsv (the working key: key.tsv plus the 26 gloss values), scripts/gloss_values.tsv. Rebuild from this folder (standard
library only):

    python scripts/make_key_1741.py
    python scripts/heldout.py key.tsv transcription_lita_1741.txt gloss_lita_1741.tsv 200
    python scripts/decrypt.py key.tsv transcription_lita_1741.txt
    python scripts/check_marks.py key.tsv transcription_lita_1741.txt marked_lita_1741.txt
    python scripts/check_marks.py key_1741.tsv transcription_castellane_oct1741.txt marked_castellane_oct1741.txt
    python scripts/check_marks.py key_1741.tsv transcription_reply_oct1741.txt marked_reply_oct1741.txt

scripts/fetch.py downloads the images; crop.py and sheet.py need Pillow and the scans, which are not included.

## Integration check (12 Nov 2026)

Done by the integrating session, not by the contributor.

- **One key, one entry.** `key_frozen.tsv` of both PR folders (hopken1741a, hopken1741b) is byte-identical to this folder's
  `key.tsv` (sha256 c4e208fe3c39689f1dba15fc8635c8d4fc42efd7391280ef6d09d82ae28c8f47, recomputed for all three files), and
  the code is the one of the despatch above. They were folded in here: the files moved with `git mv` (names kept; the working
  key `key.tsv` of the PRs is `key_1741.tsv`; their scripts are in `scripts/`, `make_key.py` renamed `make_key_1741.py`), the two
  near-identical NOTES and the three profiles merged into this NOTES and this profile. The earlier folders are gone.
- **Reproduced.** heldout.py on Lit. A: 222 of 282 groups (79%), 242 in the key (92%), shuffled-key control mean 33.4, maximum 51
  over 200 shuffles; check_marks.py passes for Lit. A, the letter and the reply; make_key_1741.py rebuilds key_1741.tsv (the
  contributor's file has CRLF line endings, otherwise identical); an own decoder written from key_1741.tsv gives the same
  mechanical text of the Castellane letter, including the unknown groups 1478, 1452, 1520, 1026, 1339, 1438, 1083, 1056.
- **Images** (lbiiif.riksarkivet.se, served without a check): R0003636_00049, all 16 rows of the letter and the three first rows of
  the reply, about 215 groups, and R0003635_00147 rows H04-H08, about 85 groups, compared with the transcriptions: no
  disagreement at that reading (the first group of the letter's second row is 1688, as transcribed).
- **What "frozen key" means for the bare pages.** The key applied to them is key_1741.tsv: the frozen key plus 24 values from
  Lit. A's gloss and two corrections (1504 r to vo, 1840 a to au). Of the letter's 205 groups 180 are in the frozen key and 191 in
  key_1741.tsv, with 7 values changed; of the reply's 269, 245 and 258, with 9 changed. The held-out test on Lit. A
  used the key frozen unchanged; the eight values "proposed from the sense before the gloss" (method, step 7) were not
  frozen in a file, so that check is by the contributor's record.
- **Strict share.** The contributor already counted strictly (verbatim words only; guesses, repairs and the hole excluded):
  letter 79 of 94 = 84.0%, reply 109 of 123 = 88.6%, together 188 of 217 = 86.6%; read in part. Lit. A: every word is covered by
  the contemporary gloss (84 of 122 words from the frozen key, 35 from the gloss values, 3 repaired): this is the contemporary
  decipherment checked, not a ciphertext break, and it is not counted in the headline. The despatch is likewise (98.9% of groups
  in confident words). The letter's sentence checker is 0.444 (just under 0.45), the reply's 0.615; the letter reads as French
  sentences to a reader (grade B), so read in part stands.
- **Class.** The target is read in part by its bare pages; method key recovered based on adjacent plaintext (the glosses of the
  Swedish despatch and of Lit. A, then applied to bare pages). Outcome.key is partial (16 context-only groups in the letter and reply).
- The two independent-review paragraphs above are the contributor's. The claims review of the page was done line by line by the
  integrating session; an independent reader is owed.
