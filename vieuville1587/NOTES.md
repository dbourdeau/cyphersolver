# Nevers to La Vieuville, St-Aignan, 30 September 1587 — BnF fr. 3975 fol. 101 (DECODE R4289)

Catalogue no. 184. Session of 22 September 2026. (Worked in a folder named `nevers1587/` on the unmerged `main-fresh`
branch; moved here on merge because `nevers1587/` on main is the Randan letters, R4285/R4286.)

Status: in progress

The key was found and partly confirmed; the letter is not read. See "Where it stands".

## The document

* BnF fr. 3975 item 34, ff. 101r–102v. The BnF notice (cc504266, fragment cd0e37708, cached at
  `gallica_sweep/notice_cc504266_cd0e37708.html`) says: *"Lettre avec chiffrement et déchiffrement de LOUIS DE
  GONZAGUE, duc DE NEVERS, « à Mr de La Vieville,... De St Aignen, ce 30 septembre 1587 ». Copie."* Item 35 begins
  at f. 103, so the item is these two leaves only. **There is no separate decipherment on them.**
* Gallica: fr. 3975 = ark `btv1b90605473` (396 canvases, microfilm, all labelled NP). **f. 101r = canvas 185,
  101v = 186, 102r = 187, 102v = 188** (about 4950 × 6650 px, better than the 3184 px DECODE halves). The endorsement
  on f. 102v reads "Nevers 1587 30 sept(embre) / Mr de La Vieuville".
* DECODE R4289 has 14 images (the Gallica pages cut into halves), in `img/` (git-ignored, not public domain). They
  were fetched with the `bordeaux/decode/cookie.txt` cookie.
* Three written pages (f. 101r full, 101v full, 102r full, 102v one third), about 110 lines.

## What the page is

It isn't solid cipher. Most of the text is **clear French in a very hasty hand** (probably Nevers's own), for
example "garnison", "fortune", "quelque", "possible avant", "Car", "faut avec le", "qui a guarde", "general",
"dans une", "tousjours". DECODE records "Inline cleartext: yes". Ciphered stretches are set into the clear text:
code numbers (30, 42, 43, 48, 63, 12005…) and runs of figures mixed with letter-signs, such as
`42 et 5 1 7 t ʒ r / d65 i8 th6 6725`, `1786291`, `3d 12t 5d`, `374d 6k`.

## The key: Tomokiyo's Nevers cipher no. 16 (1587)

BnF fr. 3995 f. 32v (Gallica `btv1b525085665` canvas 69, a landscape sheet), read in full and transcribed in
`key16.txt`. It has an alphabet with figure and letter homophones (a 8/9, e 7/6, i 5/4, l 3/2, m z/x, n v/t,
o r/g, s i/h, t g/f, u e/d, r ſ/k…), plain code numbers 10–100 for ranks and places (42 eschevins, 43 maire de
ville, 30 artillerie, 48 "Chau" = chasteau, 51 Mezières, 84 Paris…), and overbarred code numbers 1–81 for
provinces and persons (25 Roy, 36 Nevers, 38 Guise, 63 La Vieuville…).

Evidence that this is the Nevers–La Vieuville key of 1587:
1. **Code numbers fit the clear context.** On f. 101v, "… a 42 et 43 de …" reads "aux eschevins et maire de ville";
   48 and 30 sit in military context (chasteau, artillerie).
2. **It reads the August 1587 sibling.** Tomokiyo's hidden transcription of Nevers → La Vieuville, Paris,
   31 Aug 1587 (BnF fr. 3416 f. 53v; comment in `nevers_tomokiyo.htm` near "no.39") gives
   `… d r h f K 6 x 8 4 t non pas quil …`. Under no. 16 that is "vostre main non pas quil", and `o 8 l 3 6` gives
   "parle" (reading his `l` as a sign for r). He had tried key no. 11 on it and marked the result "NG".

Keys ruled out on this letter: no. 11 (Tomokiyo, on the sibling) and no. 12 (April 1587, fr. 3995 f. 26: a symbol
alphabet, nothing like these letter-forms).

## Where it stands

* **The figure runs in this letter do not yet decode.** A straight reading of `d65 i8 th6 6725` gives
  "ueisanseeeli", which is not French. Either the digits are misread on the microfilm, or the runs mix clear
  syllables with cipher, or Nevers used a variant of no. 16. Not settled.
* **The clear text is not transcribed.** At the zoom tried, the hand is about 30–40% legible to me. Reading the
  letter means transcribing roughly 110 lines of a very bad hand, then marking the cipher runs within them.

## Transcription attempt and solver run (22 Sept, second pass)

At native zoom (Gallica canvas 185) the "clear" reading falls apart. Words like "garnison", "fortune" and
"village" occur, but most of the page is regular pseudo-words with recurring forms (`buellaat`/`bucllaot`,
`alatyur`/`dealtyur`, a large looped sign `G` standing alone) and kept word spaces. That is what a
letter-substitution cipher in cursive letter-forms would look like. So the letter may be **mostly cipher**, not
mostly clear. The question stays open.

* `ct_101r.txt`: glyph-level transcription of 19 of f. 101r's ~41 lines (~900 glyphs, 28 distinct signs), about
  60% confidence per glyph (minim groups u/n/m, and e/c/r, are guesses).
* Raw text as French under `fr-1530-despatches`: −5.67 per character (shuffled control −7.86, real French about −1.5).
  So it is not clear French as transcribed.
* `solve2.py`: substitution anneal (28 signs → 23 letters, homophones allowed, unigram-KL penalty), 8 restarts:
  best −4.53, no French. `solve1.py` without the penalty collapsed to "iiii" text (degenerate LM optimum).
* Key no. 16 doesn't fit the letter-forms either: l, s, u and q are frequent here but aren't substitutes in no. 16.


**Control (`control.py`).** Real period French (the `fr-1530-despatches` corpus) enciphered with a random
27-sign homophonic key, word spaces kept, random glyph errors added, then fed to the same `solve2.py`:

| length | glyph noise | best score | outcome |
|---|---|---|---|
| 900 | 0% | −1.89 | plaintext recovered exactly |
| 900 | 20% | −3.49 | readable ("ie uous remerrie de l aduertie…") |
| 900 | 40% | −4.53 | no French |
| 4000 | 40% | −4.97 | no French: more text does not help |

The real f. 101r transcription scores −4.53, the same as the 40%-noise control. So **(a) the solver would read
this letter if it were a substitution cipher and the transcription were good**, and **(b) transcribing all ~110
lines at the current accuracy would not help**. What's needed is a transcription at about 80% or better per
glyph, which this microfilm doesn't give me.

**Key no. 16 applied to the transcription:** its substitutes cover 74% of the glyphs; the decrypt scores −7.68 per
character, worse than shuffled text. So no. 16 is not the key of the letter text, only (at most) of the code numbers.

**Confusable-class merge:** folding u/n/m/w into one class and e/c/r into another, then re-running `solve2.py`
(`ct_101r_merged.txt`): best −4.76, no French.

Conclusion: at this transcription accuracy neither reading (clear hand, or letter cipher) can be established, and
the solver can't be expected to converge on noise this high. The blocker is the legibility of the microfilm.

## Why it stops here

The cipher here is a thin layer (code numbers and short runs) inside about 110 lines of clear autograph. Reading
it at the project's 95% bar means reading that hand, and I read it only about 30–40% on the microfilm (Gallica
has only the B/W microfilm; the original needs the BnF reading room or a colour scan). Without a clear-text
transcription, the runs can't be separated or tested reliably.

## Remaining gaps

* Clear text: not transcribed (blocker: illegible on the microfilm to this reader; a colour scan or a palaeographer would unblock it).
* Cipher runs: key identified, runs not deciphered (blocker: none from outside).

## Escalation (not yet done)

1. Transcribe the clear text line by line from Gallica canvases 185–188 at native resolution, with a
   project-standard notation for the inserted runs.
2. Test each run against key16.txt. Allow clear syllables inside runs and figures read either way (6/b, 5/s, 1/7).
3. DONE 22 Sept: sibling BnF fr. 3416 = Gallica `btv1b9058240c`, ff. 52v–53r on canvas 62 (openings, 7447 px). It is
   the same hasty hand, mostly clear with code numbers (25, 63, 42 et 51, 42 et 43, 1200, 500…). What looked like
   marginal glosses are the ends of f. 52v's lines running into the gutter. **No decipherment, so no calibration.**
4. Check whether Nevers's letters of Sept–Oct 1587 are printed. Nevers's *Mémoires* (Gomberville, 1665) carries
   pieces from the fr. 3974–3995 series.
