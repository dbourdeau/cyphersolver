# A Vienna agent ("Sidon") to Baron Schenck, chamberlain of Augustus II, 1706 — DECODE R7486-R7500

Status: read in part (written up 9 Oct 2026; own entry since 14 Oct 2026)

**Split on 14 Oct 2026** from `sieniawski1708` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue entry 333
("Letters to Hetman Sieniawski and Dresden to Schenck", DECODE R7468-R7500) joined these fifteen letters with the
letters to Hetman Sieniawski only through the DECODE range; the Sieniawski letters are other correspondents in four
other keys, each with its own entry and page (a different cipher in each): [`sieniawski1708`](../sieniawski1708/NOTES.md)
(Brâncoveanu/Cantacuzino, key A), [`turculet1709`](../turculet1709/NOTES.md) (key B), [`r7475`](../r7475/NOTES.md)
(the adviser's table) and [`chomentowski1713`](../chomentowski1713/NOTES.md) (the syllabary). The work below was done
on 9 Oct 2026 in the sieniawski1708 session and is carried over from its NOTES; every file of this folder except the
Sieniawski transcriptions moved here on 14 Oct 2026 (`measure.py` rerun after the move: 865 of 1,361, unchanged).

## Records (DECODE metadata pulled 9 Oct 2026)

Archiwum Narodowe w Krakowie, owner 32 (uploaded 29 Sept 2023), private ciphertext, status 4 (N/A), cipher type 6
(unknown), symbol set numerical, no decryption or key file attached.

| Records | DECODE name | DECODE description | pages |
|---|---|---|---|
| R7486-R7500 | AKM 21 plik 30/1, items 1-15 | sender "NN z Drezna (jezuita?)", receiver "Schenck (Szench) szambelan Augusta II", 1706 | 3-8 each |

Neighbours checked: R7460-R7461 (ASang 85/3, keys, 1600-1799, other collection), R7462-R7467 (ASang 85/3 and
Krakow_UNK_1/2, unknown cipher, French), R7501-R7507 (AKPot 3227, Wąsowicz to Aleksander Lubomirski 1662-69, R7501 a
key). None of them is a key for these groups. Images: DECODE full-resolution, fetched with the session cookie
(git-ignored, not in the repository).

## First look (9 Oct 2026)

**R7486-R7500 are not from Dresden.** The first letter is headed (later hand) "Wien 7 marty 1706", docketed
"Rec. 12 aprilis 1706", numbered "N. 18", in German, signed "Votre tres humble et tres obeiss[ant]". Letter of
29 May 1706 is "N. 32". A Vienna correspondent writing to Schenck. Clear German with (a) 3-digit code numbers for
persons and words (150, 181, 187, 189, 190, 208, 258, 413, 452 ...) and (b) runs of 2-digit numbers spelling words.

## Prior work and contamination (searched 9 Oct 2026)

No edition, no key, no DECODE or literature reading found for the Vienna-Schenck letters. (Kaczka 2012 prints only
Sieniawski letters, in other keys.)

## The letters

**Documents.** Fifteen letters of 7 March - 14 July 1706, numbered by the writer (N. 15, 18, 27, 28, 31, 32, 35, 38,
39, 40, 41, 44, 47 ...), German with French and Latin, signed "Votre tres humble et tres obeiss. Serviteur" with a
cover name read "Sidon"/"Sadon". Address (R7488): "A Monsieur / Mons.r Le Baron de Schenck / Chambell. de Sa
Majesté / Le Roy de Pologne / à Cracovie". Receipt dockets "Recept. ... in Cracau", "in Lublin". A later archive hand
wrote "Seligman"/"Lehman" on two address leaves. DECODE's "NN z Drezna (jezuita?)" is wrong: every letter is dated
Vienna. Transcriptions: `transcr/R74xx.txt` (two agents from the full-resolution DECODE images, 9 Oct 2026).

**System.** Clear German with (1) a 2-digit letter cipher for single words or phrases, (2) 3-digit code numbers
(100-599) for persons, courts and things, (3) a few 1-2 digit codes outside the letter range (83, "3.", "2.") and
(4) letter signs with a dot ("o.", "b.", "L.", "d.", "e.", "f.", "g.", "c.", "m.", "p.", "oo", "ooo") standing before
codes and runs (a word code, pass 2 below).

**Key of the letter cipher, recovered ciphertext-only (9 Oct 2026).**
1. Free homophonic annealing (`solve.py`, de-1740s order 5, many-to-one, unigram prior) on 642 tokens: no sense.
2. Run statistics: runs end in 19 43, 21 45, 20 44, 19 55; 16 starts runs; the frequent numbers cluster
   (19-21, 43-45). Hypothesis: homophones are consecutive numbers in alphabetical order.
3. `monotone.py`: annealing only the 23 block boundaries over 1-84 with the de-1740s model. Best restart
   (-913 against -1212 to -1496 for the others): b from 10, c 13, d 16, e 19, f 22, g 25, h 28, i 31, k 34, l 37,
   m 40, n 43, o 46, p 49, q 52, r 54/55, s 58, t 61, u 63/64 ... i.e. **three numbers per letter, a = 7 8 9 up to
   z, alphabet without j and v** (`key.py`). Decodings: "der Baron Kleinburg alhier", "correspondenz", "seiner
   proposition", "ein rescript so ... zugleich unterschrieben", "combination", "religionis", "confidence",
   "secretarz", "introduction", "accordirten puncten", "diffidence". 79 = z (zugleich, correspondenz, abgesetzt);
   70 = w (wieder, wegen), so w and the x/y/z blocks are not exactly three wide.
4. Second pass over every run against the key (subagent, full-resolution crops, `transcr/RUNS_FINAL.txt`): 24 lines
   corrected. Traps: the scribe's 31 looks like 21 ("ʒi"), his 6 is a delta and was read as 0 or 8. 67-69 serve for
   v and w (von, Vanitäten, Avisen), 76-78 = y (Ogilvy, Convoy, Secretarÿ), 79 = z (Reichsvicecantzler). The
   recipient's superscripts over R7486 runs (s a k l a over "geschlagen", p r e t over "dessipiret", a u f) agree with
   the key: he deciphered these runs himself.
5. Readings in context include "dieser glaubet sey kein guttes omen", "Herr Senfft hat gar 181 abgesezt", "es soll
   hier viel Cabalen ...", "o. Reichsvicecantzler", "der Baron Kleinburg alhier", "aus Muscau geschrieben", "seiner
   proposition", "ein rescript, so 154 und 166 zugleich unterschrieben", "du cabinet", "Malcontenten auffs neue
   allarmiren", "die schon accordirten puncten wieder resiliren", "diffidence", "dimission", "introduction".
6. The Sieniawski keys (Kaczka's key A, the R7475 table) scored on the runs with de-1740s: -5.6 and -7.0 per character
   against -2.8 for the block key. They do not fit.

**Measure** (`measure.py`, 9 Oct 2026): 682 letter-cipher numbers, 634 in runs that give sense (93.0%). 499 code
tokens + 37 small codes; 77 distinct codes, 5 with a value (126 tokens). All cipher tokens 1218, read 760 = 62.4%.
`ciphertext_schenck.txt` (1181 numbers, measured with `_check_profile --measure --drop-first`).

## Pass 2 on the codes (9 Oct 2026, after the coordinator asked for a full reading)

- **Context pass.** Two subagents re-read at full resolution every sentence holding a code or a dotted sign
  (`transcr/CTX_R74xx.txt`, about 90 crops; corrections written back into `transcr/R74xx.txt` as "(ctx: was ...)").
  Index of every code with its sentences: `code_ctx2.txt`.
- **The recipient's gloss in R7493 P1:4-5, re-read:** "der" stands over the dotted sign "o." and "von Kayser" over
  "5 83". So **o. = der, 5 = von, 83 = der Kayser** (grade C). The first pass had put "der Kayser" on 208: wrong,
  208 is the subject of that sentence and stays open.
- **The dotted signs and small numbers are a word code, not nulls**: o. = der (C), L. = und (M: "b. 154 L. 166
  zugleich unterschrieben"), f. = bey (M: "f. 83 gar sehr wohl angesehen", "ob 189 f. 254 reussire"), b. = von dem
  (I: "b. 187 bin ersuchet worden"). d., e., g., c., m., p., oo, ooo, oj, "3." and "2." stay open.
- **The 500s are an alphabetical word list.** 509 = Friede, 513 = Ordre, 515 = Progressen, 519 = Reise, 524 = Urlaub:
  F < O < P < R < U rises with the number. Inside those bounds 502 = Abreise, 518 = Recommendation, 521 = Resolution
  fit the sentences (grade I). The other 500s (504, 508, 510, 516, 517, 520, 525-530) occur once or twice in sentences
  too damaged or too general to choose a word.
- **The 100s-200s are persons, courts and states, not in one alphabetical run.** Anchors: 100 = the imperial court
  (M), 150 = King Augustus (M), 189 = Baron Schenck (M), 204 = Schweden (M). 83 Kayser < 100 Hof < 150 König < 189
  Schenck is alphabetical, but 204 Schweden is not, so no person was valued from position.
- **190 is not Charles XII.** "König von Schweden" is in clear in the same letter; 190 is an imperial minister. Value
  withdrawn; open.
- **Persons with roles but no name:** 187 (the writer's principal in Vienna), 181 (the King's man at the imperial
  court), 166 (a minister at the King's side), 154 (co-signs a royal rescript with 166), 186, 132 and 193 (rivals for
  one post), 131, 254, 258, 529, 157, 101, 103, 183, 134, 158 (the King's banker who refuses 187's bill). The Saxon
  envoy at Vienna until 1706 was Wackerbarth and from 1706 Vesnich, but Wackerbarth is named in clear in two letters,
  and no source ties either to a code.
- **Outside material tried:** the Wiener Diarium 1706 on ANNO (dated cribs) is behind a Cloudflare Turnstile check;
  searches for a Schenck chamberlain, a "Sidon" or "Seligman" agent and a printed 1706 Saxon-Vienna correspondence
  found nothing; the Hausmann *Repertorium der diplomatischen Vertreter* is not online.
- **Measure after pass 2** (`measure.py`, counting the dotted signs and the small word codes as cipher tokens):
  letter cipher 638 of 682 (93.5%); code tokens 545, 151 with a value; dotted signs 134, 76 with a value;
  **all cipher tokens 1,361, read 865 = 63.6%**. Validation (`docs/_validate.py`, 11 Oct 2026, `validation.tsv`): pass.

## Remaining gaps
- 65 of 77 three-digit codes (394 tokens), mostly persons (187, 181, 166, 190, 254, 258, 132, 193, 186 ...) - blocker: no-key-material; roles fixed from context, names not; no key with the letters, on DECODE or in print; the 100s-200s are not alphabetical, so position gives no bound; the Saxon keys would be in the Hauptstaatsarchiv Dresden and the Wiener Diarium 1706 (dated cribs) is behind a bot check the session may not pass
- dotted signs d., e., g., c., m., p., oo, ooo, oj and small codes 3., 2. (about 90 tokens) - blocker: no-key-material; articles or pronouns, no value fits every occurrence and none is glossed
- 8 letter-cipher runs, 44 numbers, without sense (lceth, ditlan, gutswor ...) - blocker: too-short; digits confirmed twice on the images, single short runs with no second occurrence

## Escalation
- [x] siblings: R7460-R7467 and R7501-R7507 opened (other collections and correspondents); DECODE holds only AKM 21 plik 30/1 of the Schenck file
- [x] clear-pages: address leaves and dockets read (Baron de Schenck at Cracow, "Seligman", receipt dates); the recipient's own glosses used: o. = der, 5 = von, 83 = der Kayser
- [x] known-keys: Kaczka's keys A and B, the R7475 table and the Chomentowski syllabary scored on the runs: none fits
- [x] print: web searches for Schenck, "Sidon", "Seligman", Saxon envoys at Vienna 1706 (Wackerbarth, Vesnich) and printed Saxon-Vienna correspondence: no key, no edition; the Wiener Diarium on ANNO is behind a Cloudflare Turnstile check
- [x] key-rebuild: letter table complete; second context pass over every code (transcr/CTX_*); alphabetical order tested: holds in the 500s, fails for the persons
- [x] retry: every run and every code sentence re-read at full resolution
