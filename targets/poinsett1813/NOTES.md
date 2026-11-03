# Poinsett → Monroe, Santiago de Chile, 20 Feb 1813 (Unsolved Catalogue no. 639), with the Buenos Aires letter of 14 June 1814 (no. 651)

Status: in progress

Catalogue 639. Joel Roberts Poinsett, US special agent for Buenos Aires, Chile and Peru, to James Monroe, Secretary
of State. Manning, *Diplomatic Correspondence ... concerning the Independence of the Latin-American Nations* vol. 2
(1925), doc. 442, pp. 896-898, prints the clear text with "(undeciphered cipher)" at ten places.

## 1. The document

- NARA RG 59, Despatches from Special Agents, vol. 3 = microfilm **M37 roll 2** (catalogue naId 213803757),
  **frames 0092-0094** (folios 37, 37v-38, 38v; old foliation 41 on 0093). Images are the catalogue JPEGs
  `https://catalog.archives.gov/medialz/dc-metro/rg-059/876974/M37-02/M37-02-NNNN.jpg` (not committed).
- Frame 0092 (f. 37r, the opening) is filmed almost black with heavy show-through; even after background
  flattening only the clear words can be made out, not the code groups of passage P0 ("You will have seen a series
  of ..."). Frames 0093-0094 are good.
- Passages P1-P9 (`transcription.tsv`, one row per written line, with the clear context from Manning): **437 code
  groups, 256 distinct** (`ciphertext_1813.txt`, measured with `docs/_check_profile.py --measure --digits`).
  Manning's ten "(undeciphered cipher)" places = P0 + P1-P9 (Manning splits P2/P3 around "and dictated by the first").

## 2. The system

A numbered code of about 1,600 groups (highest group read 1589; one doubtful 1800), comma-separated. Common words
are single groups (1355 the, 1397 of, 522 and, 1348 in, 1215 / 1315 a, 1554 to), longer words are spelled from
syllable groups (409 1175 1179 765 pro-te-ti-on; 1314 413 1166 per-ma-nent). Values are not in alphabetical order
(1348 in, 1355 the, 1385 pre, 1397 of, 1399 foot, 1407 po, 1413 at): a two-part code. A small circle over a group
adds -s (971 country, 971° countries; 1116° in "sloops"); a cross under a group and a caret also occur (1115+,
694+, 264^, 961^), meaning not yet established.

It is **not** any US code table in the repo: the Department code of 1803-40 (`targets/jqa`, the = 1385), Armstrong's
THE=972, Pinckney's legation code, the 1788 legation code, Jefferson 1787, Mountflorence 1801, nor Sumter's Rio code
of 1813 (M121 vol. 1A frames 0035-0039: the = 798, of = 1399, and = 1242). `shift_test.py` also tried every constant
shift (and mod 1600/1700) of the first five against the 1813 groups: best z = 4.3 among ~9,000 settings for the JQA
table, decodes are junk; no signal. Gallatin to Madison, 15 Aug 1810 (Founders, Madison 03-02-02-0600), says
Sumter "ought to have Mr Poinsett's cypher", so a Sumter-Poinsett copy may have existed, but Sumter's despatches to
Washington are in his own code.

## 3. The 14 June 1814 sibling (Unsolved Catalogue no. 651): already deciphered, and the key source

Poinsett → Monroe, Buenos Aires 14 June 1814. Original (RC): M37 roll 2 **frames 0097-0098** (f. 39r clear, f. 39v
with both code passages and a **clerk's decode written over the groups**). **Duplicate**: frames 0099-0100 (f. 40r
headed "Duplicate", f. 40v the same code passages, no decode, line ends intact). Same code as 1813 (the = 1355, of = 1397,
"of this country" = 1397 891 971 in both letters).

**Prior art.** Manning, *Diplomatic Correspondence ... Latin-American Nations* **vol. 1 (1925), doc. 201, pp. 335-336**,
prints the whole letter with the code passages in clear, from "MS. Consular Letters, Buenos Aires, I". His text is the
clerk's decode word for word ("the utmost ship should draw", "than single Frigate"). So catalogue 651 was read in
1814 and in print since 1925; the catalogue's "OCR only, no decipherment" was wrong (found 27 Oct 2026, archive.org
djvu text of `diplomaticcorres01mann`). Method for this letter: **existing decipherment**.

**What was done here** (`transcription_1814.tsv`, `ciphertext_1814.txt`, `decode_1814.py` → `reading_1814.txt`):
both copies transcribed line by line and checked against the clerk's words and Manning. Merged text (RC, gutter
ends from the Duplicate): **123 groups, 90 distinct; 122 have a value = 0.992**. The one open group is **39** in "a ship
[39] should draw", left blank by the clerk and by Manning.

- A (after "a mission which has originated from the"): the prevailing opinion of a rupture between Great Britain and
  Spain [:] the present government of this country will endeavour to obtain the protection of the latter at any
  price; such is however the disposition of the people that the English never can gain a permanent footing in these
  countries.
- B (after "sent a prize to Rio de Janeiro"): their trade is exposed to a just retaliation of this principle, with
  seldom more than a single frigate to protect it; two sloops of war [are] better than a frigate, eighteen feet being
  the utmost a ship [39] should draw.

Corrections to the key aligned earlier (`key_1814.tsv`, now 95 values): 964 = *principle*, not "prince" (the clerk's
word runs into the gutter, Manning prints "principle"); the group for "it" is **1236** (Duplicate clear, faint 1 on the
RC; 1236 occurs three times in 1813), not 236; "two" is **1087** on both copies, not 1037; "between" reads **737** on
both copies (middle digit not certain), not 727; "protect(ion)" splits pro-te-**ct**-**ion** (409 1175 1179 765),
since "protect" is 409 1175 1179 and "frigate" ends in 1175 = te; "feet" = 108 **480** (480 from the Duplicate).
Copy differences: the Duplicate drops 337 *never* and 1506 *sloo-*, and writes 127? for the RC's 137 *war*.

## 4. The 1813 letter with that key

`decode.py` → `decode_1813.txt`: **161 of 437 groups (0.368) have a value** (158 before the 1814 corrections of 27 Oct). The decode is fragments, not yet
sentences, e.g. P1 "No dependance can be placed on the [1436] of the people the [486][1095] and li[218][1095] of
this country ..."; P4 "... of this govern-ment [901] the ..."; P6 "... re-[12]-pro-te-ti-on ..."; P7 "... in the
[428] of ... the govern-ment". No sentence reads yet, so nothing is claimed as read.

## Remaining gaps
- P0, f. 37r (frame 0092), about three lines of groups - blocker: illegible; the microfilm frame is nearly black;
  needs a new scan of the original (NARA RG 59) or the 1813 duplicate if one survives
- 276 of 437 groups in P1-P9 (210 of 256 distinct values) - blocker: no-key-material for most; the only decoded
  sibling found covers 95 values (48 of the 256 distinct 1813 groups after the 27 Oct corrections); Poinsett's own papers with his other ciphered reports (HSP, Poinsett Papers
  vol. 4, Gilpin collection) are not online
- the same groups - blocker: open-codes until the context pass below has been made
- 14 June 1814 (no. 651): group 39 in "a ship [39] should draw" - blocker: too-short; one occurrence in both letters,
  left blank by the clerk and by Manning

## Escalation
- [x] siblings: M37 roll 2 frames 0091-0102 opened; 14 June 1814 (0098, duplicate 0100) is in the same code with a
  clerk's decode, used for the key; 0462 (Jacob Lewis) is another code; Sumter's Rio code (M121) is not this one
- [x] clear-pages: Manning prints the clear text only; no clear copy of the cipher passages found
- [x] known-keys: JQA/Department 1803-40, Armstrong THE=972, Pinckney, 1788 legation, Jefferson 1787,
  Mountflorence 1801, Sumter 1813 tried directly and under shifts; none fits
- [x] print (1814): Manning vol. 1 doc. 201 (1925) prints the 14 June 1814 letter decoded (the clerk's text); vol. 1
  has no other Poinsett letter with code (the rest were returned to him in 1818), vol. 2 only the 1813 letter undecoded
- [ ] print: Manning checked (no decode of 1813); Weber 1979 not online; HSP calendar (1941) full view on HathiTrust
  mdp.39015034759822 but behind a bot check, to be searched by hand for 'cipher'
- [x] key-rebuild: context pass made 27 Oct; only 'Lima' (249 413, twice in P4) cross-checks; no new values, the
  unknown groups occur once or twice in contexts that do not fix them
- [x] siblings (2): Lowry, La Guaira 1810-12, had a cypher for Shaler and Gelston and sent the Department one
  ciphered letter (Manning vol. 2, Lowry to Graham 30 Nov 1816); M84 roll 1 frames 0014-0090 viewed: all clear, no
  code, so that letter is not in the file; Shaler's papers (M37 roll 1) have no code frames (NARA triage)
- [x] siblings (3), 28 Oct: M37 roll 1 (all 753 frames), M37 roll 2 frames 0025-1057, M70 roll 1 (Buenos Aires consular
  despatches 1811-17, 292 frames) and M77 vol. 7 (instructions 1808-15, sampled) surveyed by contact sheet: no further
  frame in this code and no key table. Morris 1813-15 (the = 285) and Lewis 1816 are other codes. Not surveyed: M78
  consular instructions 1801-17 (naId 220862827); Manning's source for 1814 (consular letters, Buenos Aires, M70 does
  not hold Apr 1814-Jan 1815)
- [n/a] retry: no new key values came from the context pass or the sibling searches, so nothing to re-run

## 5. Next steps

1. Context pass: fill recurring groups only where two or more occurrences agree; grade them I.
2. Find more decoded material in this code: Weber, *United States Diplomatic Codes and Ciphers* (1979); HSP Poinsett
   Papers vol. 4 (1811-14 reports "parts in cipher", per the HSP list filmed at M37 roll 2 frames 20-22); the
   Department's Buenos Aires consular file (M70) for any of his letters that were not returned in 1818.
3. A better image of f. 37r (frame 0092).
4. Manning took the 1814 text from "MS. Consular Letters, Buenos Aires, I" (NARA M70 roll 1): check whether that is a
   third copy of the 14 June 1814 letter, or a copy of the 1813 one, with its own decode (it might fill group 39).

Prior art (27 Oct 2026): Manning 1925 has no decode; web search found none; not in the repo before this folder.

## Contribution (Brice Dudout, 3 Nov 2026)

Poinsett's despatch of 29 June 1811 (HSP, Poinsett Papers vol. 1, folder 10) has 19 groups in this code with the plain
text written over them: four values of `key_1814.tsv` are confirmed and 13 are new (`dudout/key_1811_additions.tsv`).
With them, 170 of the 437 groups of the 1813 letter have a value (was 161); no sentence reads yet. The despatches of
20 March and 11 April 1811 are in a second code, with a "decyphered" sheet for 11 April. Details in `dudout/README.md`.
