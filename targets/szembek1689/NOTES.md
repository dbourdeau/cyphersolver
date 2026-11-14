# Latin cipher postscript on Şerban Cantacuzino and Antide Dunod, Wallachia, after Oct. 1688 (Biblioteka Kórnicka BK 1560, "List zaszyfrowany") — NOTES

**Verdict: deciphered at the time.** Every cipher run but one carries an interlinear decipherment in a contemporary
hand. The key was rebuilt here from those glosses and every run checked against it: 22 numbers, one letter each, no
conflicts. The only unread item is one unglossed code group, `202`. Catalogue entry 348 ("Szembek papers: Latin
cipher letter", unknown → the Szembek family, early 18th c.) is resolved. The sender, recipient and date in that
entry were wrong: the letter concerns Wallachia after the death of Prince Şerban Cantacuzino (29 Oct. 1688).
Worked on 2026-09-28 in one session.

## The document

- Wielkopolska Digital Library (WBC), edition 343124, "List zaszyfrowany", publication 430427, a child of the
  structure record for PAN Biblioteka Kórnicka BK 1560 (150 leaves, "partly from the archive of Jan Szembek, Crown
  Chancellor 1700-1731"). WBC language code `lat`, rights "dla wszystkich bez ograniczeń".
- Three DjVu pages: `https://www.wbc.poznan.pl/Content/343124/DjVu/065_0001.djvu`, `066_0001`, `067_0001`. The
  site sits behind a proof-of-work "High Load" page. curl gets through once the browser pane has passed the check,
  with the browser's user agent and its `captcha_pow` cookie.
- The DjVu pages were decoded with DjVu.js (npm `djvujs-dist` 0.5.4, library sources bundled with esbuild, run in
  Node with stubbed browser globals) to 3552×4632, 3354×4185 and 3314×4571 px PNGs. The scans are kept out of the
  repository (`images/` is git-ignored material).
- Leaf foliation in the corner: "1." with "40" (f. 65 image), "2." with "41" (f. 67 image). The text starts with "P. S."
  and ends at the foot of f. 67 without a signature. It is the postscript of a letter whose main body is not in this
  item.
- In the volume, the item sits after letters to Jan Szembek of 1730-31 (Vincenti Giovanni, Mariani, Vespasiano
  Bona) and before a copy of nuncio Santini's letter of 1727. The volume is a miscellany (1694-1731), so its position
  does not date the letter.

## The cipher

- A simple substitution with two-digit numbers, 12-51, for single letters. The text is mostly clear Latin, with
  single words or phrases enciphered. Word endings and some letters inside cipher words are left in clear
  ("25 er 40 46 43 13" = perfido, "13 42 42 46 21 12 21" = occisus, "17 m 25 49 e 19 46" = amplexi).
- Key (22 numbers, all confirmed; `key.tsv`): a17 b29 c42 d43 e14 e/ae15 f40 g41 h44 i46 k48 l49 m50 n51 o13 p25
  q24 r23 s21 t20 u/v12 x19. The writer writes y in clear. 15 appears only for the ae-diphthong e (piae, memoriae,
  patriae), 14 for plain e.
- The numbers follow no alphabetical order (a17 b29 c42 d43 e14), so the table is a mixed one. No homophones and
  no nulls were seen.
- Three-digit groups are code words: `203is` is glossed *Literis* (203 = liter-), and `202` has no gloss.
- 436 two-digit cipher signs in 70 runs, plus 2 code groups (`python decode.py`). The catchword "49 46 41 eretis"
  at the top of f. 67 repeats the end of f. 66 and is counted once.

## How it was read

1. Viewed the three pages: clear Latin with struck-through number runs, and above each run a gloss in lighter
   brown ink in a different hand (the decipherer's).
2. Transcribed every run with its gloss into `runs.tsv` from 1700-px bands and native-resolution zooms of the
   doubtful signs.
3. `decode.py` aligns each run with its gloss where the lengths agree, collects number→letter pairs, and builds the
   key (22 numbers, no number with two values). It then deciphers every run with that key alone and compares the
   result with the gloss.
4. 61 of 70 runs agree letter for letter. The 9 that differ:
   - `203is` / Literis: code group, the gloss gives its value.
   - gerant (cipher) / gerent (gloss); solicitaverant / sollicitaverant; Gegenbeio, Gegenbeii / Gergenbeio,
     Gergenbeii: the cipher is right and the glosser normalised or misread.
   - functsm: the writer wrote 21 (s) for 12 (u) in de-functum.
   - pricipem: the writer left out 51 (n) in Principem.
   - defunct: the o of defuncto is not written (or the last group is 20 with a stray stroke).
   - audi2?et: a heavily struck digit (20 or 23) where r is needed; the gloss has audiret.
   None of these is a key conflict. The cipher-only reading and the contemporary gloss give the same text.
5. Identified the people: "Burgundus Antidius Dunod" is Antide Dunod SJ, Leopold I's envoy to Wallachia with
   Count Csáky in 1687-1688. "Defunctum Principem Serbanum" is Şerban Cantacuzino, who died on 29 Oct. 1688.

## Content (reading.md)

The writer, in the service of a "Celsissimus Princeps" (most likely Constantin Brâncoveanu, Şerban's successor),
thanks a "Reverendissimus Pater" for a letter in his own hand. He protests that the Wallachian side has acted
sincerely and in Christian conscience while "some Christians" (the imperial side) have not kept their promises. He
denounces Dunod as an impostor and detractor who, with a traitorous companion, misled the late Prince Şerban. The
promises Dunod carried between "that court" and Bucharest have turned out mostly false. He adds that a certain
Gegenbey was killed through a false friend's treachery and his head sent as a gift, and that his companion Gityk is
still more active "in the East".

## Independent verification by Brice Dudout (PR #565, 14 Nov 2026)

Brice Dudout (PR #565, `VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) decoded the 70 runs of `runs.tsv` from `key.tsv`
alone: 60 give the gloss letter for letter (u/v, ae/e equal), the other 10 are the two code groups and the eight slips listed above.
No key correction. Re-run here, plus a separate decoder written here: the same 60 of 70. The read share 0.986 stands. The WBC scans were
not fetched (proof-of-work page).

## Remaining gaps
- code group 202 - blocker: no-key-material; occurs once, no gloss (the contemporary decipherer left it too, and a "+" marks the line), no key table, and the clear word before it ("Damis"?) is itself unclear
## Escalation
- [x] siblings: the whole BK 1560 structure list on WBC checked (about 100 items); no other item is called cipher, and the neighbours are 1727-1731 Szembek letters in clear
- [x] clear-pages: the glosses are the decipherment; transcribed and checked run by run
- [n/a] known-keys: the key is complete from the glosses; no other key needed for the letters
- [x] print: web searches on Dunod with Gegenbey/Gityk and the letter's phrases found no edition
- [x] key-rebuild: letter key rebuilt from the glosses (22/22 numbers); 202 cannot be rebuilt from one occurrence
- [x] retry: every run redeciphered with the rebuilt key and compared with its gloss (decode.py)

## Measures

- Cipher signs 436 two-digit + 2 code groups = 438; read 437 (203 via its gloss); unread 1 (202): 99.8%.
- Cipher runs (words) 70; read 69; 98.6%.

## Files

- `runs.tsv`: transcription of every cipher run with its gloss and notes.
- `decode.py`: key rebuild and check; writes `key.tsv`.
- `key.tsv`: the rebuilt key.
- `reading.md`: the full postscript (clear + deciphered) with a translation.
