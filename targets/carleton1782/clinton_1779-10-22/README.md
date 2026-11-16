# Clinton to Haldimand, New York, 22 October 1779: the all-spelled stage on the Army List title page

Added 16 Nov 2026 (Brice Dudout, with Claude, claude-opus-5-5). Lead: the peer review of this target by Andrew Beling,
who identified the Army List title page as the spelling key of the Haldimand-Clinton correspondence (`../key/`, `../KEY.md`).

## The document

LAC MG21 B.147 (copy of BL Add MS 21807, Haldimand Papers, "Correspondence with Sir H. Clinton, Sir Guy Carleton and
other officers at New York, 1777-1781"), reel H-1649 on Canadiana Héritage
(<https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649>):

| page | Canadiana frame | content |
|---|---|---|
| p. 120 (fo. 105) | [758](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/758) | cipher, "Copy", N. York Oct. 22d 1779, opening of the letter; margin "See a decyphered copy ... in p. 134 infra" |
| p. 121 (fo. 105v) | [759](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/759) | cipher, middle of the letter: **not transcribed** (about 8 columns) |
| p. 122 (fo. 106) | [760](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/760) | cipher, end of the letter and P.S., "(Signed) H. Clinton"; endorsed fo. 106v "From Sir Henry Clinton 22d Oct. 1779 Recd [20th or 24th] May 1780 by Express via Niagara" |
| pp. 134-135 (fo. 113-114v) | [772](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/772), [773](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/773) | clear copy of the whole letter; endorsed "Lettre en Chiffre du Genl Clinton reçue à Quebec par Halifax le 18 janvr 1780" |

Images are linked, not copied (Canadiana / LAC terms of service; no open licence stated). The same letter is listed in
the Carleton Papers, TNA PRO 30/55/19/98 (lead 1137), not seen.

## System

Every group `line-place` is one letter: line 1-29 of the Army List title page, letter counted from the left
(`../key/armylist_titlepage_1778.txt`). No word codes in 1779: the letter is spelled throughout, with a stroke under the
last group of each word. A doubled place (`2-99`, `6-77`, `15-55`, `2-44`) is a doubled letter (`tt`, `ll`, `pp`, `ss`).
Three lines of the page are counted differently from the 1778 lineation the 1782 letters use:

- **line 1**: two places fewer before *Honourable* (1-9 i, 1-10 o, 1-11 n, 1-13 f ... 1-27 a, 1-28 b), as if the line read
  *Permision* and lacked one more letter;
- **line 9**: one place fewer from the start (9-4 c, 9-15 v, 9-20...28 *regiments*), as if *OFICERS* (the cipher also spells
  *oficers*);
- **line 6**: 6-9 f, 6-10 i, 6-12 l (two places early) beside 6-15 d (as in 1778).

Whether this is another edition of the Army List (1779?) or the New York clerk's counting is not established.

## Test (pre-registered, one measurement)

Earlier (9 Nov 2026, issue #359) we had learned a cell table on p. 120 alone and measured it once on p. 120 columns 6-7:
0.672 against 0.276 for the best shuffled key (partial; those columns are spent). The new test (`test/`):

1. `test/frozen/PREREG_2026-11-16.md` (French, sha256 a72c2c6f...3609) written before any decoding of p. 122.
   Transcriptions are those frozen on 9 Nov before the clear copy was read (sha256 b2a4a6d4...f32d, 691d255b...fb5f).
2. Training on p. 120 only: the 1778 page as it stands gives 235 of 364 aligned letters; for each line the variant with
   0-2 letters deleted that best fits p. 120 is kept (line 1: 144 of 158; line 9: 17 of 18; other lines unchanged);
   cells seen on p. 120 take their observed letter. Key `test/frozen/key2_armylist.tsv` (645 cells, 5 unknown),
   sha256 d7618ef8...7e37, frozen before the measurement (`buildkey2.py`, `fit1778.py`).
3. Held out: p. 122 entire with its P.S., 292 groups, never aligned or scored before. Reference: the clear copy from
   "no alternative left" to "Chesapeak", then "I have received your Dispatches by the Defiance". Score: difflib matches
   over the 292 groups, an unknown cell counted wrong. Controls: 200 keys with the letters shuffled within each line.
   Bar written beforehand: at least 0.85 and at least the best control + 0.30.

**Result** (`test/frozen/mesure2_v760.txt`, `measure2.py`): **0.979** (286 of 292); best of 200 controls **0.257**; margin
0.723. Passed. 237 held-out groups fall in cells seen on p. 120 (236 right); 55 fall in cells taken from the Army List
variant alone (50 right: 6-9 twice, 6-12, 1-1 and 2-13 wrong).

Disclosure: on 9 Nov the earlier partial table was run over p. 122 to see which part of the letter it holds (no
alignment, no score); the new key uses nothing from p. 122. The reference passage is the one that run pointed to.
`test/SHA256SUMS` lists every frozen file.

## Reading

`reading.md` (sentences, with the six key misses marked) and `decryption.tsv` (every word: groups, decode). Both cipher
pages read in full against the clear copy; p. 121 is not transcribed, so the letter is read in part.
`CLEAR_COPY.md`: our reading of pp. 134-135.

## Prior reading

The clear copy filed with the cipher at Quebec is the decipherment of the time; whether the letter is printed (Brymner's calendars of the Haldimand Papers) was not checked. What is new is that this 1779 cipher is the Army List title-page spelling, with
its own count on lines 1, 6 and 9.
