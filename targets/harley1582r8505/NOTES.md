# "L'Estat du Roy de Navarre et de son party en France" (BL Harley MS 1582 ff. 263-264; DECODE R8505)

Status: in progress

Catalogue entry 121, "Unknown sender to unknown recipient, 2 ciphertexts, BL Harley MS 1582 (R8501, R8505)".
Worked 22 September 2026.

**22 Oct 2026, reading audit** (George Lasry's test: can a reader build coherent sentences and translate them?):
R8505 is **decoded, not read**. `reading.txt` gives the cipher clauses as strings of French word fragments with `[#]`
holes in most lines (f. 264v 3.38-3.41 almost noise); only the clear French around them reads. Class read -> not
read, method -> not solved (the ciphertext-only key kept as a part); 95.1% (characters in vocabulary words) withdrawn
as a reading figure. The outcome line below is superseded.

**23 Oct 2026, re-read (REREAD_BRIEF, batch b28)**: stays *decoded, not read*. `R8505_reading.md` (whole memoir,
holes marked) scores 0.518 clean sentences (0.613 on explicit holes; before, `reading.txt`, 0.454). f. 263r was re-read
sign by sign on the higher-resolution images of **DECODE R8010, a duplicate record of ff. 263r-264v** ("Harley_ms_1582_8")
and now reads (0.661 alone): 8 labels corrected (`R8505_corrections.tsv`); the first transcription's `d` (crossed
delta, a) also covered the crossed epsilon `Eb` (t) on the rectos ("sentent du gouvernement", "devant Espernon"); key
unchanged. `reading.py` had dropped every `#` (d) as a code marker; `b28_r8505_decode.py` fixes it. f. 264r is still the
first transcription (beam over look-alikes helps only in places). Files: `R8505_reading.md`, `R8505_en.md`,
`R8505_reread_log.md`, `R8505_transcription_f1_b28.txt`.

**23 Oct 2026, second pass (b28)**: f. 264r's 25 cipher lines compared with R8010 P3 (9 label corrections,
`R8505_transcription_f2_b28.txt`); f. 264v ll. 3.38-3.46 re-transcribed on R8010 P4 (`R8505_transcription_f3_b28.txt`):
it reads in part ("ni selon sa qualite ni selon la leur, les a abandonnees en besoin ... en risee et en proie a leurs
ennemis"), so it is not illegible. **The versos were labelled the wrong way round: `final/f3.txt` is f. 264v,
`final/f4.txt` is f. 263v** (R8010 P2 = 263v holds Languedoc; P4 = 264v; P3 carries the folio number 264); every folio reference in this file now follows the corrected labels (3.xx lines = f. 264v, 4.xx lines = f. 263v). Clear French of f. 263r's lower half and of f. 264r transcribed. Score
0.530 (0.650 explicit holes; f. 263r 0.691, f. 264r 0.351, f. 264v 0.407): stays *decoded, not read*.

**23 Oct 2026, third pass (b28)**: f. 263v's clear French transcribed in full from R8010 P2 and set around its
cipher runs (4.1-4.11). Whole reading body 0.529 clean sentences (0.691 explicit holes); by side f. 263r 0.691,
f. 263v 0.519, f. 264r 0.351, f. 264v 0.407. Still *decoded, not read*: the cipher clauses of ff. 264r and 264v do not
build. Folio references in this file and in profile.json checked against the corrected leaf order.

**DECODE note (for decode_updates)**: R8010 duplicates R8505 (same leaves, better images); R8009 is an empty record of
the same name; R8505's language should be French, title "L'Estat du Roy de Navarre & de son party en France".

**Outcome: broken and read (95.1% measured).** The two records of the catalogue item are different things:

- **R8501** (ff. 71-72) is one of Sir Edward Stafford's 1586 despatches and carries its own contemporary
  decipherment on f. 72r; it was already read in the sibling target `targets/harley1582r8500/`. Nothing open there.
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
- f. 263v (Languedoc): "et maintenant jouissant de l'amitie estroite de Monsieur de Mont[morenci], auquel la leur
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

## Corrections

- **30 Sept 2026 (filling the gaps in the quotation for Lasry's list).** f. 264v lines 3.18-3.24 re-read on the image
  (`img/p3.jpg`) and re-decoded sign by sign with `key.json`, so that one run reads continuously with its clear
  context (normalised text at the end of `reading.txt`): "... Et je scay que des l'an passé le Roy d'Espagne faisoit
  traicter a la soubz main avec luy par un certain italien qui sert d'ingenieur a Lisbone, dont les letres me sont
  venues es mains. Maintenant aussi la Roine sa mere va traicter avec luy le mariage de sa fille [de] Lorraine, pour
  le rejoindre avec [c]este maison ennemie de la chrestienté e[t] particulierement de l'estat d'Angleterre, a quoi,
  veu les pratiques ordinaires de ceu[s] de Guise en Escosse, [6] doit remedier." Changes: 3.21 re-segmented ("les
  letres me sont venues es mains", no sign changed); 3.22 "[c]este" (one c for "avec ceste") and "e[t]" (the sign
  after e reads u, a slip); 3.23 the sign after "ce" is T (u), the shape of the u in "Guise" on the same line and the
  second transcription's reading, so `final/f3.txt` changes b -> T there; the next sign is the o-sign where s is
  wanted: "ceu[s] de Guise en Escosse" replaces "C en o deguisee nes C o". Clear words re-read: "des l'an passé"
  (was "des lan- / part"), "faisoit traicter" (was "faisons traictes"), "sa fille [de]" (was "&"). The key is
  unchanged. `evalct.py` in this checkout gives 0.911 over all four sides both before and after the change (f. 264v
  0.905 -> 0.906); the 95.1% above was measured in the main checkout with its vocabulary build.

## Remaining gaps

- the cipher clauses of f. 264r (2.5-2.7, 2.16-2.25) and f. 264v (3.1-3.5, 3.39-3.47) that do not build - blocker: no-key-material; tokens confirmed on the R8010 images, the key (rebuilt from this text alone) gives no French there, and no second text in the same key is known
- doubtful names and words in the clear text of all four sides, marked [?…] - blocker: illegible; fine secretary hand at the photograph's resolution
- the ten nomenclator numbers (6, 21, 26, 36, 51, 57, 72, 81, 99, 721), 14 tokens - blocker: no-key-material; names, nothing in the text fixes them

## Escalation

- [x] siblings: every DECODE record of Harley 1582 (R8498-R8502, R8504) and R8506 checked; R8501 already read.
- [x] clear-pages: no interlinear or marginal decipherment anywhere on ff. 263-264; the clear French around the
      runs was used as context throughout.
- [x] known-keys: Navarre's numeric cipher with Segur (`../segur/`) is not this key; no graphic-sign Navarre key
      is on DECODE or in Tomokiyo's tables. The key was rebuilt here from the ciphertext.
- [x] print: the memoir is not in the Calendars of State Papers Foreign 1583-86 and no printed copy was found.
- [x] key-rebuild: done - see "How it was broken".
- [x] retry: the versos re-read sign by sign (Sept); f. 263r re-read sign by sign and f. 264r compared line by
      line with the image, f. 264v 3.38-3.46 re-transcribed, 23 Oct 2026 (b28, R8010 images).

## Files

`img/` (git-ignored BL images), `signs.md` (sign chart, with the corrections table), `ct_p1..p4.txt` (first
transcription), `ct2_p3.txt`, `ct2_p4.txt` (second, reading-guided transcription), `final/f1..f4.txt` (the transcription the
reading uses), `emendations_all.txt`, `merges.txt` (every emendation logged), `key.json`/`key_letters.txt` (the key),
`reading.txt` (the reading), `control.py` (the control experiment), `solve*.py`, `basin.py`, `word.py`,
`sweep.py`, `split.py` (the attack), `profile.json`.

## fols. 264r-264v read, Brice Dudout (29 Oct 2026)

With key.json unchanged, and after a blind check on the two last cipher lines of 264v (absent from b28: coverage 0.886, rank 1/201 against 200 permuted keys), the cipher lines of 264r and 264v were re-transcribed on DECODE R8010 P3/P4. b28 confused o/u, b/T, E/E3, d/Eb, X/hg, and filed several shapes under `Tu` (a lying T = c, J, a rounded U = h, a lead-in stroke); b28's 3.47 is the rising end of 3.48. The passages now read: 666 words, 95.3% in their sense (31 unresolved), e.g. "ele n'a pas despende un denier pour eu" (264v) and "ne peut desguiser ce faict d'Anuers", which dates the memoir to c. 1583 (hypothesis: the French Fury, 17 Jan 1583). See `dudout/README.md`.
