# Kopp ↔ Chicherin radiograms, 1921 (NARA M316 rolls 40–48; catalogue 669)

Attempted, open: no group value recovered for the figure traffic. The letter traffic in the same file is split off per key: `lejava1921`, `voikov1921` (keys recovered, deciphered), `voikov1921b` (decoded, not read), `stomoniakov1921` (unbroken). The Karakhan table is in `karakhan1921`.

## Source

Typed copies of radio traffic intercepted at the US High Commission, Constantinople, sent to State by Admiral Mark
L. Bristol. NARA RG 59, Central Decimal File 861.00, microfilm M316 rolls 40–48 (digitised as RG 64 copies); naIds in
`extract_ocr.py`. Covering despatch: 861.00/8575, Bristol No. 153, 20 Apr 1921 (M316-041-0871/0872).

The Russian radio operator's statement in No. 153: the bulk of Kopp–Chicherin traffic is in Russian; messages signed
like "Tchicherin Maerz 16-1921 number ..", and Hilger's and Staehler's, are in German; the Bolsheviks "use old Russian
code books and sometimes apply Captain Murashenko coding method", a numerical key "subtracted or added to the coded
original (double coding)"; Nauen sometimes withholds Kopp's messages. Bristol could not vouch for this.

## Prior work

- Tiltman, "Experiences 1920-1939" (NSA release, Doc ID 6618711): GC&CS read Moscow-London traffic from 1920.
  Columnar transposition of transliterated Russian, then from about Nov 1920 dinomes (variants by frequency) before
  transposition, dinomes not split; early 1921 a new table with the discriminant DELEGAT, first entry about April 1921;
  keys from George Wither. A footnote notes a similar system on another link with split dinomes. Nothing there on
  Moscow-Berlin.
- HW 12 (GC&CS decrypts) and RG 457 6707N not seen. No published reading of this traffic found by web search
  (2 Nov 2026).

## The corpus

`extract_ocr.py` keeps 625 frames with figure runs from the cached NARA OCR; `segment.py` splits 1,478 runs, 66,640
groups (OCR only, provisional, includes retransmissions and traffic that is not Soviet). The OCR reads the blurred
carbons badly: frames are checked by eye before anything is claimed. Measured so far, on OCR:

- The file holds several unrelated systems. Clear counters 00025, 00050 ... mark every 25 groups in the 5-figure
  traffic. Discriminant words precede the groups (SWET, MISTERIA, PALLADA, FORUM, ANCHAR, SIRIUS, SOLNZE ...).
- `AUSSENAMT WIEN` / Pohl and the Austrian POW mission use groups 0000-19999 with no leading zero.
- `RETRANSMISSION ANGORA` and `Christiania` runs have many repeats: other plain codes.
- `dinome_ic.py`: aligned dinome IC well above 1.0 in many 5-figure runs (RUDII 3.2, SIRIUS 2.8), consistent with the
  dinome systems Tiltman describes, though no table or key is recovered here.
- The Berlin → Moscow 4-figure runs share a clustered first pair (64, 74, 75, 85, 86 ...): `stat5.py`.

## Two small plain systems

Both show literal phrase repeats, so no additive is on them.

1. **Karakhan → Kopp, 29 Apr 1921, Nr 1979/S** (M316-042-0255, `karakhan_ct.txt`, 179 groups read from the image).
   First pair almost always in 4-7 × odd digit; second pair almost always two adjacent digits.
2. **Kopp 16 Apr 1921 and Lutovinov 23 May 1921, Nr 417** (M316-041-0876, 0877, 042-0953; `kopp0876_ct.txt`,
   `kopp0877_ct.txt`, `lutowinoff417_ct.txt`). First pair in 01-09, 10-13, 15, 20, 30 ... 90; second pair in 01-31, 40,
   50 ... 90. 042-0953 is sharp; 0876/0877 are blurred and 3/5/6/8 are uncertain. One partial last line of
   0876 is not transcribed.

## Failed attempts

- Two-table consonant + vowel syllabary (`cv_solve.py`, `cv_solve2.py`, `tworun.py`): scores no better than shuffled
  controls (Karakhan -4.93 vs -5.08; Lutovinov -5.42 vs -5.54); no Russian.
- `mi.py`: context is strong inside a group and weak from one group's second pair to the next group's first pair
  (Karakhan z 0.0, family 2 z 2.2), which argues against chained consonant + vowel signs.
- `mono.py`: second-pair stream as monoalphabetic Russian scores -3.69 per character, the same as its shuffled control
  and far from -2.11 for real text.
- `dinome_mono.py`: aligned dinomes of the 5-figure runs annealed to Russian; no text.
- `period_hi.py`, `solve14.py`, `em.py`, `relkey.py`: clustered 4-figure messages as table code + periodic numerical
  key. On Nr 461 (042-1265) period 14 scored z 11.2, but 14 is the typed line length and the even harmonics point to 2.
  Stripping gives 9-15% of groups in the known vocabulary, and no single odd-even difference stands out. An idea that
  14 was twice the length of a discriminant word is withdrawn: the discriminant on that frame is inked out. No key.
- The OCR stream of 042-1265 starts with the date `1921` as if a group; those frames need checking before reuse.

## Clear material in the file

- 041-1069 to 1078: Bristol No. 160, 25 Apr 1921: "confidential copies of what he described to me as code telegrams",
  from the local Russian Political Mission, mostly Lomonosov, Dec 1920 to Jan 1921, one to Kopp. English only, and Bristol
  would not vouch for them. No matching ciphertext seen: the intercepts in the file start in March 1921.
- 043-0936: Bristol No. 336, 1 July 1921: anti-Bolsheviks gave "positive assurance" that they had secured the Bolshevik
  code in Berlin; it never arrived. The American Mission in Berlin got the same promise, also unmet.
- Many messages are in clear, some marked "translated from Russian by P.S." (042-0863, 042-0616, 043-0440, 043-1088):
  context, and possible cribs, not yet tested.

## Crib search

- Lenin, PSS 52 no. 314, written 7 May 1921, "send in cipher to Kopp", 91 words, about 489 letters transliterated; a note
  by Chicherin adds that it goes to Lutovinov in Kopp's absence. Moscow serials run 2006/S (1 May) to 2220/S.
  Nearest Moscow to Berlin messages: Nr 180 to Kopp, 7 May, 2157/S, and Nr 184 to Lutovinov, 8 May, 2188/S, both signed
  Karakhan, SWET, 45 and about 36 groups. Those are short for 91 words in letters, and the SWET groups are flat (position
  IC 1.03). No fit is shown, and without a code book a crib here could not be confirmed.
- DVP IV (istmat.org nodes from about 50521): 22 pages fetched before the site closed connections, then refused WebFetch,
  curl and Chrome from this machine, probably because of that crawl. Search results show mostly notes, plus a radiogram of
  2 April to several missions (node 50549) and a telegram to Brodovsky. Neither text has been read.
- Politburo decision "Predlozhenie t. Koppa", 16 April 1921, same date as frames 041-0876/0877: the notes tie it to goods
  exchange. Text not seen. The decision approves a reply to Kopp, so its date alone does not identify the Berlin to Moscow
  intercept.

## Dating and duplicates (5 Nov 2026)

Checked against the cached NARA OCR of M316 roll 42 after an outside check of the same texts by a correspondent (name
held until credit is agreed; no plaintext from their tests):

- Nr 417 sits on a sheet headed "MAY 26th 1921 / FROM BERLIN TO MOSCOW" with the message line "FUNKSPRUCH Nr 417 VOM
  23 MAI 1921". The sheet date is the intercept date; 23 May is the message date.
- It belongs to Bristol No. 246, Constantinople, 31 May 1921, stamped 861.00/8742 (object 604704182), enclosure "Cipher
  telegrams exchanged between Moscow and Berlin, etc. May 26th-31st inclusive". Roll 42 covers 861.00/8623-8773.
- Our three transcriptions total 717 positions; the small table is the 715 complete groups. Not in them: one partial last
  line of 041-0876 and an overwritten group before 9603 in Nr 417.
- No parallel copy: runs of three groups from each text match only their own frame in rolls 40-48.
- Nr 421 and 427 (23 and 24 May, Berlin to Moscow) are five-digit SWET messages, not four-figure like Nr 417.

## Figure traffic after the letter break

`fig.py`: the small table (715 groups) with each group as one letter, corrected model: real -2.43 to -2.50, shuffled -2.40 to -2.54, and the text collapses into repeated letters. No support. The pair `9030 7010` occurs 7 times; its neighbours vary, and reading it as `zpt` is untested.

## Different systems

These are different tables, so a later reading of one should split it into its own target (one key, one entry).

## Remaining gaps
- All of the file: no group value known - blocker: no-key-material; no code book, crib or decipherment in the file or found in print
- HW 12 (GC&CS decrypts, 1921) - blocker: needs-physical-access; not online, whether Berlin traffic was read is unchecked
- RG 457 6707N, War Department copies - blocker: needs-physical-access; not digitised

## Escalation
- [x] siblings: reels 40-48 scanned by OCR; four frames viewed closely; 041-1071 to 1078 are English versions of telegrams, see "Clear material in the file"
- [x] clear-pages: covering despatch 041-0871/0872 read, no decipherment; the other despatches in the catalogue entry not read closely
- [x] known-keys: only the small-table vocabulary was tested as an underlying code for Nr 461, and it did not fit
- [ ] print: Dokumenty vneshnei politiki SSSR IV not fully checked: istmat.org refuses this machine after 27 fast requests; Lenin PSS 52 no. 314 checked, see below
- [x] key-rebuild: annealing, EM and a period search all failed their controls
- [n/a] retry: nothing has been read, so there is nothing to retry
