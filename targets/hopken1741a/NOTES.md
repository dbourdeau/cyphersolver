# Catalogue 2245-2248: Höpken and Carlson, Constantinople, to the chancery president, 1735-1741

Work of 11-12 Nov 2026, contributed by WAINUT (AI language-model agents; no human palaeographer). Four Riksarkivet
volumes of Diplomatica Turcica were paged from the images the catalogue names, and two documents were worked in full:

| Sub-folder | Volume | Images | Document | Groups | Proposed state |
|---|---|---|---|---|---|
| `hopken1741a/` | I/9/26 (R0003635), catalogue 2247 | 147 | "Lit. A", French memorandum on the last Russo-Ottoman treaty, enclosure to the despatch of 24 Feb / 4 Mar 1741; glossed | 282 | read (contemporary gloss, checked against the frozen key) |
| `hopken1741b/` | I/9/27 (R0003636), catalogue 2248 | 49, 50 (left page) | Cipher copy of a letter of the comte de Castellane, French ambassador, and the start of Höpken and Carlson's reply; received 2 Oct 1741; **bare, no gloss** | 205 + 269 | letter: read in part; reply (to the foot of 50 left): read in part |

Both are in the **second code** of `hopken1740` (four-digit groups 1006-1915, a syllabary built for Swedish, with word
codes). No new key was built: the hopken1740 `key.tsv` on origin/main was frozen unchanged (`key_frozen.tsv`,
sha256 in `FROZEN.sha256`) and applied. These are the first French texts read in that code and the first bare
passages read with it outside volume I/9/21.

Status: in progress (not yet written up). Lit. A (image 147) read, 12 Nov 2026; other glossed runs and the rest of
the volumes are open (see Remaining gaps and Escalation).

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
  runs (second code). Image 147: Lit. A, worked (hopken1741a).
- **I/9/27 (R0003636, Jul-Dec 1741, catalogue 2248).** Image 8: glossed Swedish runs. Images 49-52: the bare French
  copy of the exchange with Castellane, about 2,000 groups over seven pages; 49 and the left page of 50 worked
  (hopken1741b). Image 93: bare pages. Image 135: partly glossed.
- Catalogue 2241, 2242, 2244 (volumes I/9/23, I/9/29, I/9/28) were not opened.

## Method

1. Sign conventions (SIGN_CONVENTIONS.md) set in the pass-file headers before any decoding.
2. Two passes per page: pass 1 from bands at 0.6-0.75x of the full-size image, pass 2 from fresh crops at 0.9-1.0x
   (quadrants or halves), disagreements settled on 2x crops. Image 49: 3 disagreements (1638/1688, 1840/1340,
   1583/1505), settled 1688, 1840? and 1585. Image 50: 2 (1670/1678 and a blotted third digit), kept doubtful as 1678?
   and 1613?. Image 147: no digit disagreement; pass 2 added two strokes over 1500 (à); one group kept as 1678?, one
   as 1442?. Honest caveat: on image 147 the gloss is written between the rows and was in view; the digits were read
   before any decoding, and no digit was changed toward the gloss. Images 49-50 have no gloss. One agent did both
   passes (a second agent was not available in this run), so the passes are not fully independent.
3. Key: key_frozen.tsv = the hopken1740 key on origin/main (329 groups; 235 confirmed), unchanged.
4. **Held-out test (scripts/heldout.py) on Lit. A**, a page from another volume and in another language than any page
   the key was built on: each run of groups is aligned to its gloss by dynamic programming. **222 of 282 groups (79%)
   give exactly the letters of the gloss at their place; 242 groups are in the key, so 92% of those known.** With the
   key's values shuffled among its groups: mean 33.4, maximum 51 over 200 shuffles. Word codes were compared through a
   fixed list of equivalents stated in the script (tractat=traité, ottporten=Porte, ...); letters normalised (j=i,
   u=v=w, accents dropped).
5. key.tsv (working key) = key_frozen.tsv + 24 values read from the Lit. A gloss (status gloss_1741a: 1741 u, 1718 ir,
   1529 che, 1521 y, 1703 va, 1702 us, 1527 qu', 1789 tra, 1769 eur, 1566 plu, 1797 vre, 1283 lu, 1652 ix, 1043 cle,
   1175 qui, 1423 sui, 1712 ir, 1877 fro, 1027 oient, 1442 é, 1439 glé, 1183 ég, 1824 is, 1832 prince) + 2 frozen
   single values corrected on the same gloss (1504 r -> vo, three places; 1840 a -> au/av, two places).
6. The bare letter (hopken1741b) was decrypted mechanically with key.tsv (scripts/decrypt.py) and read in French;
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
| Castellane letter (key.tsv) | 94 | 79 (84.0%) | 2 | 13 | 0 |
| Reply, to foot of 50 left (key.tsv) | 123 | 109 (88.6%) | 3 | 10 | 1 |

Word codes rendered in French (grefwen = comte, storviziren = Grand Vizir, ottporten = Porte, hof = Cour, swerige =
Suède, ryssland = Russie, frankrike = France, fred = paix, tractat = traité) are counted as verbatim. Lit. A: all 122
words are covered by the contemporary gloss; the cipher differs from the gloss in four places (notes in
hopken1741a/about_reading_lita_1741.txt).

## Independent review (12 Nov 2026)

An AI language-model agent that took no part in the solve reviewed both folders blind. It read 92 groups from its own
crops before opening the transcriptions (image 147 rows H05 and the end of H08; image 49 rows L04, L07, L12; image 50
left rows M08, M14): no disagreement, and the two doubtful groups it met (49 L07 1840?, 50 M14 1613?) are the ones
marked. It confirmed that key_frozen.tsv is byte-identical to origin/main targets/hopken1740/key.tsv, reran
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

## Remaining gaps

- The rest of the Castellane exchange (image 50 right page, 51, 52; about 1,500 bare groups) - blocker: not-attempted;
  same code, the key reads it; it needs two transcription passes and a reading.
- Context values in hopken1741b not confirmed by a gloss - blocker: open-codes; 1026 Monsieur (2), 1286 V[otre] (3),
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
- Other code pages of I/9/24-27 - blocker: not-attempted; the first-code pages of I/9/24 (images 40, 106 glossed;
  139 bare) and the second-code glossed runs of I/9/25-27 (images 8, 54, 100, 240, 286, 329, 135). The glossed runs
  are the material to confirm the context values above; image 40 is a held-out page for the hopken1739 key.
- The three-digit code of I/9/25 image 99 - blocker: not-attempted; a different system.
- Catalogue 2241, 2242, 2244 - blocker: not-attempted; not opened.
- Castellane's side of the exchange in the French archives (possible clear text) - blocker: not-attempted; a crib for
  the whole exchange if it survives.
- A full independent second reader - blocker: not-attempted; both passes were by one agent; the blind review
  spot-checked 92 groups on images 147, 49 and 50, with no disagreement.

## Escalation

- [x] siblings: the four volumes named by catalogue 2245-2248 paged at 1200 px (survey above); the glossed Lit. A page
  of I/9/26 used as held-out test and key extension for the bare pages of I/9/27
- [x] clear-pages: images 49-50 checked for a gloss or a clear copy on the page (none); Lit. A is glossed
- [x] known-keys: the hopken1740 key (second code) applied frozen; the hopken1739 key (first code) recognised on
  I/9/24 but not applied
- [ ] print: two web searches only; the Nantes Constantinople series (Castellane's own correspondence) not checked
- [ ] key-rebuild: context values proposed from the sense only (listed above); the glossed runs of I/9/25-27 that
  would confirm them are not worked
- [ ] retry: 1515 and the doubtful digits not retried beyond 2x crops; images 50 right, 51 and 52 not transcribed

## Image links

IIIF manifests: https://lbiiif.riksarkivet.se/arkis!R0003590/manifest , ...!R0003628/manifest ,
...!R0003635/manifest , ...!R0003636/manifest. Images: https://lbiiif.riksarkivet.se/v3/arkis!R0003636_00049/full/max/0/default.jpg
(and _00050; R0003635_00147). Viewer: https://sok.riksarkivet.se/bildvisning/R0003636_00049 , _00050 ,
https://sok.riksarkivet.se/bildvisning/R0003635_00147 . Fetched one at a time, 1.6 s apart, User-Agent
WAINUT-research (scripts/fetch.py); no 429, no bot check. Scans are in scans/, not for git.

## Files (targets/hopken1741a/)

The notes above cover both targets of this round; this folder holds Lit. A, and `targets/hopken1741b/` holds the
Castellane exchange. Here: SIGN_CONVENTIONS.md; transcription_lita_1741.txt (with _pass1 and _pass2);
gloss_lita_1741.tsv (the contemporary gloss, by row); pairs_lita_1741.tsv; decryption_lita_1741.txt (frozen key);
marked_lita_1741.txt; reading_lita_1741.md; translation_lita_1741.md; about_reading_lita_1741.txt; key_frozen.tsv (the
hopken1740 key.tsv, unchanged; sha256 in FROZEN.sha256); key.tsv (working key, key_frozen.tsv + the 26 gloss values,
built by scripts/make_key.py from scripts/gloss_values.tsv); work/lita_keytsv.txt (Lit. A decrypted with key.tsv);
profile.json. scripts/: decrypt, make_key, heldout,
pairs and check_marks use the standard library; fetch downloads the images, and crop and sheet need Pillow and the
scans, which are not included. Rebuild from this folder:

    python scripts/make_key.py
    python scripts/heldout.py key_frozen.tsv transcription_lita_1741.txt gloss_lita_1741.tsv 200
    python scripts/decrypt.py key_frozen.tsv transcription_lita_1741.txt
    python scripts/check_marks.py key_frozen.tsv transcription_lita_1741.txt marked_lita_1741.txt
