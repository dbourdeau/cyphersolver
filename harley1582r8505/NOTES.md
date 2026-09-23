# "L'Estat du Roy de Navarre et de son party en France" (BL Harley MS 1582 ff. 263-264; DECODE R8505)

Catalogue entry 121, "Unknown sender to unknown recipient, 2 ciphertexts, BL Harley MS 1582 (R8501, R8505)".
Worked 22 September 2026.

**Outcome: broken and read (95.1% measured).** The two records of the catalogue item are different things:

- **R8501** (ff. 71-72) is one of Sir Edward Stafford's 1586 despatches and carries its own contemporary
  decipherment on f. 72r; it was already read in the sibling target `harley1582r8500/`. Nothing open there.
- **R8505** (ff. 263-264) is a French political memoir in an unknown graphic-sign cipher. It is **identified**,
  **transcribed** and **deciphered here** for the first time: the key is recovered and the text reads
  (95.1% measured - see "How much reads").

## What R8505 is

Four sides headed on f. 263r *L'Estat du Roy de Navarre & de son party en France*: a survey, for an outside
reader, of Henri de Navarre as a political asset - his two "qualitez" (first prince of the blood, chief of the
reformed churches), the places and garrisons he holds in Guyenne, Languedoc, Dauphine and Provence, the
gentlemen of his following, the Catholic, German and Swiss alliances, and the marriage question. Written after
1580 (the peace "de l'an 1577", Brouage "l'an 1580", "l'an 1576"), it belongs with Navarre's embassies to the
Protestant powers in the mid-1580s, which is how it came to sit in an English secretary's file. DECODE has no
title, no date, no author and gives the language as "English?"; the corrections are queued for DECODE.

The clear French carries the narrative; the cipher carries the sensitive clauses, written inline in the same
hand, in mid-sentence, exactly as in the Stafford letters elsewhere in the volume.

## The cipher

A **homophonic alphabet of graphic signs**, about 50 shapes, no word division, with a handful of nomenclator
numbers written between dots (6, 21, 26, 36, 51, 57, 72, 81, 99, 721 - names, still unread). Recovered key:

| letter | signs | letter | signs |
|---|---|---|---|
| a | E (lunate epsilon), psi, d, Oi, Tu | m | the **dot groups** (two, three and four dots) |
| b | phi (oval pierced by a long stem) | n | b, o |
| c | J, ti, tl, tr, + | o | Pi, PiG, sh |
| d | #, H, ne | p | hg |
| e | L, 7, Gm, I | q | cy, w0 |
| f | eq | r | w, wT |
| g | Br, Usq | s | E3 (two-bowled epsilon), n, R, U, II, Tn, bx, rho |
| h | Om | t | B, Eb, wf, F, `,` |
| i | dd, G, y, c, u, V | u | T, f, q |
| l | X, Xo | y | v |

The final key is `key.json`, letter by letter in `key_letters.txt`: three to six homophones for the frequent
letters, one sign each for the rare ones - an ordinary chancery design of the 1580s. Sign shapes are described in
`signs.md`. `v` and `j` are not distinguished from `u` and `i` (the usual 16th-century practice), and no sign for
`z` or `x` occurs.

**The dot groups are the letter m, not punctuation.** That single mistake in the first reading is why no sign
mapped to m or b, and why the first transcription could not be made to read. Controls: `7 Eb :2 psi G o B Gm b Tu
o wf` = "et maintenant"; `Xo psi :3 G B dd 7` = "l'amitie"; `:4 PiG b n c Gm q wT ne L` = "Monsieur de".
Two further pairs of shapes had been collapsed: phi (b) against f (u), and E3 (s) against E (a); and T (u)
against b (n). Controls: "de beau|caire" (Beaucaire on the Rhone), "d'une bonne armee", "estroite", "necessaire".

## How it was broken

1. First transcription of all four sides (~3,630 signs), then homophonic annealing against the shared French
   models: **failed**, in every language.
2. **Control experiment** (`control.py`): real French enciphered with a 50-sign homophonic key of the same shape
   and put through the same solver - it failed too. So the solver, not the material, was the obstacle. Two faults:
   a Sukhotin vowel/consonant constraint that was simply wrong for this key, and a temperature scale far too low
   for log-probability deltas of this size. With both fixed the control solves **100%**, and still **95.5%** with
   15% of its signs randomly corrupted, so transcription noise at the observed level is survivable.
3. The same search on the real text then produced French at once ("et qu'ils attendent", "a l'avenir", "duquel"),
   and basin-hopping plus a word-segmentation objective (`basin.py`, `word.py`, `sweep.py`) fixed the rest.
4. The recovered key had **no sign for m or b** - impossible for French. That diagnostic pointed straight at the
   transcription, and a second, reading-guided pass over the pages found the dot groups (m), phi (b), and the
   epsilon and stem-loop pairs. Every page was then re-read against the key (`ct2_p*.txt`).

## The reading

`reading.txt` holds the text run by run with its clear-text context. Samples:

- f. 263r: "... et qu'ils attendent ... a l'avenir ... allie a luy ... hors le royaume ... il est bien ..." and, in
  cipher, the name **d'Espernon**.
- f. 264r: "cependant ne laissent ... qu'il n'y ait quelque gentilhomme ... les causes ... ceux de la Religion ...
  munitions qu'on a ... la guerre ... nos provinces ... quand nos ennemis ... fortes et asseurees ... pour la
  conservation ..."
- f. 264v (Languedoc): "et maintenant jouissant de l'amitie estroite de Monsieur de Mont[morenci], auquel la leur
  est necessaire ... places de toute la province de Languedoc ... estant icelui asseure de **Beaucaire sur le
  Rosne** et de la seneschaussee de **Besiers** ... **Carcassonne** ... et autres places d'importance ... a la
  devotion du Roy de Navarre."

## How much reads

**95.1% of the 3,551 deciphered characters fall inside French words** (`python evalct.py key.json 'final/f*.txt'`,
Viterbi segmentation against a 37k-word vocabulary built from the `lang/` French corpora). That is the measure
behind the read bar; it is conservative, since 16th-century spellings and proper names the vocabulary does not
hold are counted as unread.

Per side: f. 263r 0.96, f. 264r 0.95, f. 263v 0.95, f. 264v 0.95.

**Emendations.** ff. 263v and 264v were re-read sign by sign from the images against the key. ff. 263r and 264r
kept their first-pass transcription, corrected only by a constrained pass (`emend.py`, `merge_eq.py`): a token may
be swapped only between shapes the second reading proved confusable - the dot groups against `eq` (the f sign is a
stem with a dot cluster at its upper right, so a faint stem reads as a bare cluster), phi against f, the two
epsilons, the two stem-loops, chi against the hourglass, the three bar-shapes, and Pi against the bracket - and
only where the word model gains clearly. 77 tokens in all, 2% of the text; every one is logged in
`emendations_all.txt` and `merges.txt`, so any of them can be checked against the images.

## The nomenclator numbers

Ten numbers occur, written between dots, and none is fixed by the text; but three have contexts that narrow them:

| number | context in the reading | probable |
|---|---|---|
| 72 | "la guere contre ceus dela religion en **72**"; "le parti de ceus de la religion demeurera ferme en **72**" | a country - France |
| 81 | "le **81** son frere"; "les **81** **36** auront peu de moien de lui mal faire" | a person, probably the King |
| 21 | "**21** c[har]gee dela guere contre ceus dela religion" (feminine agreement) | a feminine noun - the League, or the army |

6, 26, 36, 51, 57, 99 and 721 (the last in "le sul mariage d[e] **721**") occur once or twice with nothing to fix
them. They are recorded as open codes.

## Remaining gaps

- open-codes: the ten nomenclator numbers (6, 21, 26, 36, 51, 57, 72, 81, 99, 721), 14 tokens in all, have no
  values; they are names, and nothing in the text fixes them.
- illegible: about 5% of the text does not resolve into French words. It is scattered, not concentrated: faint
  ink, and shapes ambiguous between two members of the same family. ff. 263r and 264r would gain most from the
  same sign-by-sign re-reading the two versos got; the lines f. 263v 3.38-3.46 are the weakest on the page and
  are marked provisional in `ct2_p3.txt`.

## Escalation

- [x] siblings: every DECODE record of Harley 1582 (R8498-R8502, R8504) and R8506 checked; R8501 already read.
- [x] clear-pages: no interlinear or marginal decipherment anywhere on ff. 263-264; the clear French around the
      runs was used as context throughout.
- [x] known-keys: Navarre's numeric cipher with Segur (`../segur/`) is not this key; no graphic-sign Navarre key
      is on DECODE or in Tomokiyo's tables. The key was rebuilt here from the ciphertext.
- [x] print: the memoir is not in the Calendars of State Papers Foreign 1583-86 and no printed copy was found.
- [x] key-rebuild: done - see "How it was broken".
- [~] retry: ff. 263v and 264v were re-read sign by sign against the recovered key; ff. 263r and 264r were only
      emended between the proven confusable pairs, because the session's agent capacity ran out. That second
      reading of the two remaining sides is the open task.

## Files

`img/` (git-ignored BL images), `signs.md` (sign chart, with the corrections table), `ct_p1..p4.txt` (first
transcription), `ct2_p3.txt`, `ct2_p4.txt` (second, reading-guided transcription), `final/f1..f4.txt` (the transcription the
reading uses), `emendations_all.txt`, `merges.txt` (every emendation logged), `key.json`/`key_letters.txt` (the key),
`reading.txt` (the reading), `control.py` (the control experiment), `solve*.py`, `basin.py`, `word.py`,
`sweep.py`, `split.py` (the attack), `profile.json`.
