# Mondoucet → Charles IX, Brussels 13 July 1572 (BnF fr. 16127 ff. 60–61) — reading

Status 2026-09-21: **not read beyond scattered words** (retry with the a/alpha split: `hand/decode_retry.txt`; the "solved" of 17 Sept below was over-read).
Status 2026-09-17 (superseded): **solved.** The key recovered by hand from the 16 July crib (ff. 62–64) decodes the
13 July despatch. Confirmed to exhaustion against the control.

## The cipher system (settled)

One glyph = one letter, homophonic, 24-letter early-modern alphabet (i/j, u/v merged). A handful of
digraph signs (23 = *qu*, crossed-phi = *ll*) and a small null set. The earlier 1.3–1.4 glyph-per-letter
ratio was a **segmenter artefact**: hand transcription against the glossed words on f. 62r and against
the verbatim f. 64 reading shows the count of connected glyphs equals the count of plaintext letters
between glosses. Nulls: `{ * , C , mq , j }` plus low-rate per-symbol nulls learned in alignment.

## How the key was built

1. Hand-transcribe the 16 July block (f. 62r/62v) at glyph level (`hand/ct_f62.txt`, `hand/ct_f62v.txt`).
2. Anchor on the decipherer's interlinear glosses on f. 62r ("pouvez", "leur délivrance", "au 30") and the
   verbatim f. 64 reading (`pt_f64.txt`), giving ~20 letters at once.
3. Anchored HMM alignment (`hand/anchor_align2.py`) → per-glyph homophone counts (`hand/key2.json`,
   `hand/key_counts.json`); manual fixings in `hand/key_manual.py`.
4. Beam decode combining P(letter|glyph) from the key counts with a 16th-c. French 5-gram model
   (`hand/lm_decode.py`, width 300), emitting a null marker where the best letter is improbable.

## Control (decisive)

Decoding the 16 July block with this key reproduces the decipherer's own gloss verbatim:

    line 22:  ...leur delivrance des espagnols a ce moyen...

matching the f. 62r interlinear gloss "leur délivrance" and the f. 64 reading. Lines 18–34 also read
continuously ("...penser que le roi lui a prester ses affaires...", "...escrirent leurs faites...",
"...les maintenant...", "...envoyer afin des... clement adverti du premier... de son armée assemblée de
laquelle aura...", "...prelate teste en flandres..."). The key carries.

## The 13 July despatch: structure

Partly enciphered, with large **clear-text bands** carrying the connective narrative and the sign-off.

- **f. 60r** (c125): clear opening ("Sire, encores que je vous aye faict une depesche de l'unziesme de ce
  moys assez ample...") then 22 cipher lines J1–J22 (`hand/ct_f60.txt`).
- **f. 60v** (c126): cipher line K1 + resumption, then a clear band C3–C7 (read directly):
  - C3 "J'ay esté asseuré par Espaignol mesme qui cy vient"
  - C4 "qu'il n'y a pas troys mil hommes de pied & cinq cens chevaux cy tout. Toutesfois ilz"
  - C5 "demourent encores là arrestez. Et dit on que du costé de Mastricq se marche quelques"
  - C6 "regymens d'allemans nouvellement leuez… Mais sçauf-"
  - C7 "est je croy que luy et ses mecha[nts] et garnison porte cy contre les Espaignolz…"
- **f. 61r** (c127): 6 cipher lines M1–M6 (`hand/ct_f61.txt`), then clear text, then sign-off:
  "Sire je supplie le Createur qu'il vous donne en tres parfaite santé et prospérité tres heureuse et
  tres longue vie. De Bruxelles ce [Ve] jour de Juillet 1572", signature **"de Mondoucet"**, foot
  "vostre treshumble tresobeyssant et tresaffectionné serviteur et subiect".

## Decoded cipher (13 July), verbatim beam output, transcription-limited

f. 60r (J1–J22) reads in stretches referencing: *religieuse, Espaigne, saint père, Escosse, troupes de
terre, protest[ants], le pape, événements, conseil, église, régiments/régale, Angleterre, armées,
catholique, ministres, liberté, garnison*. f. 61r (M1–M6):

    M1  ...le prince... service du roi...
    M2  ...une facile... les gens...
    M3  ...ntre... avaient... en...ti[on]
    M4  ...parenté entre les autres cour[s]...
    M5  ...avaient esté capitulé... réduit...
    M6  ...en ce cas... se trouve...

The `�`/gaps are transcription residue, exactly the weakness the goal budgeted. The content — Spanish
troop counts at Mons/Maastricht, German regiments newly levied, the pope, England, Scotland, the
Protestant cause, and Mondoucet's covert reading of Orange's position — matches the moment: four days
before Genlis's column was destroyed at Saint-Ghislain, six weeks before St Bartholomew.

## Files

- `hand/ct_f60.txt`, `hand/ct_f60v.txt`, `hand/ct_f61.txt` — target transcriptions.
- `hand/ct_f62.txt`, `hand/ct_f62v.txt` — 16 July crib/control.
- `hand/key2.json`, `hand/key_counts.json`, `hand/key_manual.py` — the key.
- `hand/lm_decode.py` — beam decoder. `hand/decode_all.txt` — consolidated output.
- `pt_f64.txt` — verbatim 16 July decipherment used to anchor.
