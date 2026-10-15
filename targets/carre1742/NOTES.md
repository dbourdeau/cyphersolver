# Letters to Mr Carré, Pall Mall, 1742-45 (BL Add MS 32305 ff. 11-12, 14-17, 22-23; DECODE R2968, R2970, R2972)

Attempted, not solved: 0 of 1,323 code groups deciphered. A two-part code of about 800 entries, no gloss, no crib, no
key found.

Split on 14 Oct 2026 from `bl32305` under the one-key rule (George Lasry, 14 Oct 2026). Until then these three letters
were filed with the Paris letters of February 1719 (R2964, R2965) because all are intercepts in the same codebreaker's
volume; the 1719 letters are in another code and stay at [`targets/bl32305/`](../bl32305/NOTES.md) (a different cipher,
with its own page). The work below was done on 21 Sept 2026 and is carried over from the bl32305 NOTES; the `carre/`
folder (transcriptions, parser, anneal and one-part test) moved here on 14 Oct 2026. Lengths re-measured on 14 Oct 2026
with `carre/parse.py` (the bracket- and mark-aware parser): R2968 372/208, R2970 470/219, R2972 481/196, all
1,323/381, values 1-800.

Catalogue item 70 (originally R2970 alone; folded into item 78 on 21 Sept 2026, restored for this code on 14 Oct 2026).

## The volume

BL Add MS 32305 is a codebreaker's working file of intercepted letters (DECODE R2963-R2981); the record-by-record table
is in `targets/bl32305/NOTES.md`. The records in this code: R2968 (ff. 11-12), R2970 (ff. 14-17), R2972 (ff. 22-23);
R2969 (f. 13, "Carré 1742") is the decipherer's frequency count of R2968 + R2970, not a key. Images were fetched with
the DECODE cookie and are not committed.

## The attack

Attacked 21 Sept 2026 (work first done in a separate `r2970/` folder, merged into bl32305, split out here on 14 Oct 2026). **Attempted, closed**: a two-part code of about 800 three-figure groups with word-level entries; not breakable ciphertext-only from the three surviving letters.

### The documents

Three letters in one code, all in BL Add MS 32305 :

| Record | Folio | Heading | Groups | Distinct | Max |
|---|---|---|---|---|---|
| R2968 | ff. 11–12 | "Anonyme à Monsr Carré en Pellmall à Londres", Mars 1742, ΔΔΔ | 372 | 208 | 796 |
| R2970 | ff. 14–17 | "Copie d'une Lettre en Chiffre, sans date, et adressée avec ces caractères ΔΔΔ à Mr Carré en Palmal Lond. sous un couvert adressé à Mr Chevening(?), Marchand Joailier près Charing Cross"; signed "Anonyme"; endorsed "R Aug. 22 1742" | 470 | 219 | 800 |
| R2972 | ff. 22–23 | "Lond. 19 Janv. 1745" | 481 | 196 | 796 |
| all | | | 1323 | 381 | 800 |

R2969 (f. 13, "Carré 1742") is the decipherer's frequency count. Transcriptions (all in `carre/`): `transcription_R2968.txt`,
`transcription_R2970.txt`, `transcription_R2972.txt` (one line per MS line, page markers, `_` = underlined,
`?` = doubtful). Parser: `carre/parse.py`. Images are not committed (fetched with the DECODE cookie).

Notes on the copies: all three are fair copies made by the intercepting office, sheet-lettered (A–E, a–d, e–h) with
catchwords. R2968 f. 12r repeats a line (`156 106 514 512 539 279 231 686`) and brackets the first copy: a
copyist's dittography. R2972 has a later hand's underlining of repeated runs (`95 57 606 451`, `212 621 675 195`,
`9 440 144 299 86 600 707`) and faint pencil letters under a few groups (h, r?, d?, b?/e?): a decipherer's
tentative guesses, not a reading. R2970 was received 22 Aug 1742, so it is later than R2968 (March 1742).

**Check against R2969.** R2969's tallies are of R2968 + R2970 together (the two 1742 letters), counting the
bracketed dittography. With that line included my transcription gives exactly R2969's figure for 686 (20), 212 (19),
106 (18), 121 (14), 12 (14), 707 (12), 781 (11), 539 (10), 621 (10), 518, 330, 610 (9), 66, 232 (8), 44, 98, 231,
283, 476, 551, 611, 771 (7); it differs by one for 573 (12 v 11), 27 (9 v 8, one doubtful 27 at a page edge),
772 (7 v 8). R2969's second column lists 610 with 19, apparently a slip. So the transcription is sound to about one
group in 300.

### Statistics

- 1323 groups, 381 distinct, 147 seen once; values 1–800 (one 800, none above). Each hundred has 36–62 distinct
  values: the whole range 1–800 is in use. Flat profile: the top value (212) is 2.3 % of the text, then 12, 106, 686
  (1.8–2.0 %), 707, 66, 121, 283, 621, 75.
- No separators, no nulls detectable: groups are separated by points (R2968, R2972) or spaces (R2970) only.
- Repeats are short: 94 repeated bigrams, 24 trigrams, 8 four-grams, one five-gram (`151 521 330 621 212`, in
  R2968 and R2970); `95 57 606 451` ×3 and `75 95 57 606` in 1745 (a name or title spelled in groups, underlined).
- The 1742 and 1745 letters share the code: 73 % of the 1745 tokens use a value seen in 1742 (68 % of R2970's use a
  value seen in R2968), and the top values recur (12, 212, 106, 66, 283).
- Underlined single groups (R2970: 73, 218, 349, 7, 211, 587, 204, 319, 307, 785, 328, 80, 143, 135, 685, 383,
  235; R2968: 356, 196, 365, 135, 549, 631, 204, 785, 287, 585, 80) are the intercepting clerk's marks, probably for
  proper names; 135, 204, 785, 80 are underlined in both 1742 letters.

### What the system is

1. **Not a letter-level homophonic cipher.** Annealing a letter-per-group assignment against the French 4-gram model
   (`carre/anneal_letters.py`, `lang` model `fr-modern`) reaches −2.09/−2.11 per char on the real text and −2.12/−2.17 on
   the same groups in shuffled order: no difference, and the output is gibberish (`carre/anneal_letters.out`). With 381
   types for 1323 tokens a letter homophonic would be overfitted anyway; the type/token ratio and the Zipf-like
   profile are those of a word code.
2. **Not a one-part code.** In a one-part French code, le/la/les (l-), que/qui (q-), et/en (e-) would pile the token
   mass into their alphabetical bands. `carre/onepart_test.py` compares the observed token mass per 50-value bin with what an
   alphabetical list of the 700 commonest French words (fr-gutenberg) predicts: Pearson r = −0.26. Placing the top 30
   values at their proportional alphabetical positions scores worse than random values (86 % of 2000 random
   placements do as well). The contemporary tentative identification (686/106 = de, 121 = la) also assigns
   non-adjacent values to de.
3. **So: a two-part code** of about 800 entries (words, and presumably syllables/letters for spelling names such as
   the underlined 1745 run), the same type as the Paris 1719 code in this volume (`targets/bl32305/`), whose glosses prove two-part order.

Language: French is assumed from the headings (French clerk's heading, "Anonyme", the writer's ΔΔΔ address mark);
nothing in the figures confirms it.

### Is it breakable?

Not ciphertext-only. 1323 tokens for an ~800-entry random-order code give at most a handful of reliable
identifications (the few frequent function words) and no way to verify them; the decipherer of the time stopped at
the same place (R2969, pencil guesses on R2972). No crib is available: the letters are undated/anonymous and the
contents unknown; a guessed crib (Walpole, Carteret, the Pragmatic Army, the Pretender) cannot be placed without a
known sequence, and the only repeated long run (`95 57 606 451`) is too short to test a name against.

What would break it:
- the key itself, or another letter in the code with an interlinear decipherment. Places to look: the rest of BL Add
  MS 32305 and neighbouring codebreaker volumes (Add MS 32258–32310, the Newcastle/Secret Office papers), SP 107
  (intercepted letters), SP 36 1742 (Carré as an addressee), and the Secret Office decipherers' letter-books
  (Willes family) for "Carré" or "Carre, Pall Mall";
- a clear copy or summary of any of the three letters (e.g. in the Newcastle papers, Add MS 32699–32700 for Aug 1742);
- the identity of Carré and of "Chevening" the jeweller, which would suggest names for the underlined groups and a
  crib for the opening (R2970 and R2968 both open without a salutation run in common).

### Log

- 21 Sept 2026: fetched R2968, R2969, R2972 images (R2970 already in `decode/`); transcribed the three letters from
  the full-resolution images; checked against R2969; statistics; letter-homophonic anneal + shuffled control
  (no signal); one-part test (no signal). Conclusion above.

### Key hunt (21 Sept 2026): negative

- **R2975–R2981** (the rest of the volume; R2982 on is Add MS 4136): all 1749–59, letter ciphers or 4-figure codes, deciphered. None in the Carré code; no key, table or clear copy.
- **R2971** (pencil "Carré 1742"): a French despatch from London to "V.A.S." (a prince), 1742, 4-figure syllabic code deciphered interlinear (448 = de, 745 = que, 693 = les, 4209 = la). Not to Carré, not the same code: 448 and 745 never occur in the 1323 Carré groups. The pencil heading is an archivist's.
- **R2972's marks under groups** ("h", "e", "r?/d?", "b?") are the decipherer's cross-references to the sheet (e–h) where the same run recurs (`9 440` → h, `95 57 606 451` on f → e and on e → f, `600 707` → g), not plaintext guesses. R2972 carries no decipherment.
- **Web search** (Carré Pall Mall 1742 cipher/Jacobite; "Add MS 32305"; Mr Carré 1742–45; the jeweller "Chevening"): nothing.
- Still to try, offline: the Willes decipherers' letter-books, Newcastle papers Add MS 32699–32700 (Aug 1742, Jan 1745), SP 36 / SP 107 for "Carré, Pall Mall".

## Prior art

Checked 21 Sept 2026: the BL catalogue description (unidentified cipher keys) and a web search for the shelfmark, Carré,
Pall Mall 1742, the jeweller "Chevening": no edition or study found. DECODE has no transcription files for these records.

## Remaining gaps
- R2968, R2970, R2972, the whole of the three letters (1,323 groups) - blocker: no-key-material; a two-part code of ~800 entries with no gloss, crib or key in the volume, on DECODE or in print; 1,323 tokens of a random-order code cannot be rebuilt ciphertext-only

## Escalation
- [x] siblings: all of Add MS 32305 on DECODE viewed (R2963-R2981); R2969 is a frequency count, R2971 (pencil "Carré 1742") is a different 4-figure code to a prince (its de=448/que=745 never occur here), R2975-R2981 are 1749-59 letter ciphers/codes
- [x] clear-pages: none; the three letters are entirely in figures, and R2972's small marks are the decipherer's cross-references to recurring runs, not a reading
- [x] known-keys: no key in the volume: R2971 is a different code (de=448/que=745 absent here), the Paris 1719 code is another two-part code (its glosses were not applied here), and no key of this code was found on DECODE or on the web
- [x] print: BL catalogue, web search for Carré / Pall Mall / Chevening / Add MS 32305: nothing
- [n/a] key-rebuild: nothing reads; a letter-homophonic anneal is no better than its shuffled control and a one-part order is ruled out (r = -0.26), so there is no seed for a two-part code
- [n/a] retry: nothing was read to retry

Leads offline (not done): the Willes decipherers' letter-books; Newcastle papers Add MS 32699-32700 (Aug 1742, Jan 1745);
SP 36 / SP 107 for "Carré, Pall Mall".
