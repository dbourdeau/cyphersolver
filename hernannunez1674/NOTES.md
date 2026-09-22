# Hernán Núñez (Stockholm) to Fuenmayor (Copenhagen), December 1674 — DECODE R1012–R1015

Status: read

Four despatches of the Conde de Hernán Núñez, Spanish envoy in Sweden, to Baltasar de Fuenmayor, Spanish envoy in
Denmark: 5, 15, 19 and 26 December 1674 (DECODE catalogue names; the DECODE summary's "1674–1677" is a span).
Archives générales du Royaume, Brussels, Secrétairerie d'État et de Guerre, inv. nr. 2559, the same volume as
[carpio1677](../carpio1677/NOTES.md) and [balbases1677](../balbases1677/NOTES.md). Images and DECODE's transcriptions
(transcriber MEG, 2020) fetched 21 Sept 2026 with the cookie in `bordeaux/decode/cookie.txt`; images in `img/`
(git-ignored).

**Result.** The letters are mostly in clear Spanish, with one to three cipher passages each (1,716 cipher groups in
DECODE's transcription). Every passage has a contemporary decipherment in the left margin. **The key is the one rebuilt
for Balbases 1677** (`../balbases1677/key.json`). Applied unchanged to DECODE's transcriptions, it reproduces the margin
text of all four letters word for word, apart from DECODE transcription slips. So the margins are verified, and where
DECODE could not read the margin hand ("Siruarel d mandarme…", "hasto pancial"), the key gives the text.

Added to the Balbases table from these letters (context-certain):
- 167 = Suecia (a homophone of 163)
- 161 = resolución
- `os` = para
- 30 = p (DECODE's reading of 26)
- 6+ = o
- 4 = t (dentro, otro, neutralidad)
- unstruck `d` in DECODE's transcription = struck d = que

Unread groups after the first pass: about 7% (R1012 62/624, R1013 20/372, R1014 29/484, R1015 7/236). Almost all are
DECODE misreadings (split or merged groups, "25b3", "00 0"), not gaps in the key. The margins cover the same passages.

## Second pass: the unread groups on the images (22 Sept 2026)

Images fetched from DECODE with the `bordeaux/decode/cookie.txt` cookie into `img/` (git-ignored). Every group dec.py
left unread (`unread_groups.tsv`) was found on the image and read against its margin; results with grades in
`fix_R1012.tsv` and `fix_R1013-15.tsv`, applied by `dec2.py` (output `read2/`).

- 62 DECODE misreadings: this hand's closed 4 read as 9 ("96" = 46 de, "189" = 184 sobre, "92" = 42 vi), g for y
  ("ge" = ye es), xo split as "00" + "0", merged groups (xoy = xo y, 138 = 13 8, atad = at ad).
- 48 code groups the Balbases table lacks, fixed by the margin: bof guerra, cuf Inglaterra, 187 tiempo, 149 quanto,
  111 comercio, cin haviendo, cel hacer, on electo, F with bar = todo, C+ / crossed sign = ll (with a vowel mark after
  it: small S = o, cross = e), 69 ru, 32 x, 17 y / oc, 76‡ enen, 21‡ a.
- 7 nulls, 1 illegible (R1014).
- Key corrections applied throughout: 13 = e (not a null here: 13 8 el, 13 ef esse); underlined N = V.S.
- DECODE omits two lines of R1012: p.1 "28 41 xe 28 63 / 92 76 21 ef 31 if 63 29 tt 15 13 53 46 ad" (...mas veces no
  vienen a ser sino un juego de pa-) and p.4 "28 xo oc ye ed 63 8 15 ad 66 xe 31 ec d" (...s como español por parecerme
  que). They are not in the token count.

Measured (`dec2.py`): 1,716 tokens, 1 unread, 11 values graded M; 0.999 read, 0.993 without the M values.

## Remaining gaps
- one R1014 group - blocker: illegible; the sign cannot be read on the DECODE image and the margin does not fix it
- 11 values graded M (R1012 6, R1013 3, R1014 1, R1015 1) - blocker: illegible; the signs are unclear on the image

## Escalation
- [x] siblings: Balbases 1677 and Carpio 1677, same volume; the Balbases key reads these letters
- [x] clear-pages: every passage has its margin decipherment, used as the check
- [x] known-keys: Balbases 1677 key applied unchanged
- [n/a] print: no edition found (web search 21 Sept 2026)
- [x] key-rebuild: 48 code groups added from the margins
- [x] retry: all 118 first-pass unread groups re-read on the images

## How it went

1. DECODE's `DOC_*.txt` were parsed into cipher tokens and margin text per record (`mktx.py`, `tx/`). DECODE writes
   "q." as "g.3", so that was normalised to *que*.
2. The Balbases aligner (`align2.py`) run per image did not converge, because the margin glosses run across page
   breaks. Run per record with seven anchors from the repeated pair *representado / representaré*
   (66 re, 30 p, ef se, 24 n, 70 ta, 48 do, 22 y), it converged in four rounds. The values matched Balbases'
   (58 lo, 28 s, y n, uf su, 21 a, 31 r, d+ que).
3. The Balbases key was applied directly (`dec.py`) and read the letters. The output, each with its margin, is in
   `read/`.

## What the cipher says (from the margins, checked by the key)

- **5 Dec 1674 (R1012).** Sweden has agreed with Denmark on every point of the treaty project. But if Denmark adds a
  clause not to oppose the arms Sweden now intends to take up, all earlier articles to the contrary are void, which
  is "a game of words" typical of princes. Núñez has argued in Stockholm that Sweden must keep "el freno desse reyno".
  He comments on the Swedish envoy at Copenhagen, who is not partial and is to be believed only where confirmed
  elsewhere, "siendo hombre lleno de artificios".
- **15 Dec (R1013).** Hamburg has refused to carry a Brandenburg gentleman on its ship so as not to offend Sweden. It
  was bought with Swedish promises and presents. Núñez hopes Hamburg, intimidated, will withdraw its confidence in
  the Swedes, which would encourage the Danes.
- **19 Dec (R1014).** Sweden's embassy to Copenhagen is meant to gain time and so answer the French ambassador's demands
  for the aid due under the last treaty. There is talk of Charles XI's marriage to the Danish king's sister. The
  Anglo-Swedish treaty is only a renewal of the one Coventry concluded. Keeping Denmark on side is the only way to
  hold Sweden back: if Denmark accepts neutrality, France's pretext fails.
- **26 Dec (R1015).** Before it rises, the Swedish senate will decide whether to assist France "a mano armada". Núñez
  has broken off his baths to lobby, putting the King's service before his health. (Sweden invaded Brandenburg that
  same month, which began the Scanian War.)

Prior art: DECODE lists the records as partially decrypted, and the margins are the contemporary reading. A web search
(21 Sept 2026) found no published edition.
