# Barbavara and Pusterla to Francesco Sforza, Jan - May 1447: the R1857 key (BnF italien 1584)

Status: written up 29 Oct 2026 (docs/barbavara1447.html): read from existing decipherments; f. 143 read in part (5 of 51 runs open)

One key, two writers. DECODE R1857 image P11 (ASMi, Potenze sovrane 1592 Cifrari, a late copy) is headed "Marcolinus de
Barbavara et Symon Arrigonus — Petrus de Pusterla". Marcolino Barbavara, ducal secretary, wrote from Rimini and Rome
(leads 1314); Pietro Pusterla, the Duke of Milan's procurator, from Gualdo, Ferrara and Milan (lead 1313; folded in
here from `targets/pusterla1447/` on 28 Oct 2026, its notes kept as `NOTES_pusterla.md`, log `WORKLOG_pusterla.md`).
All letters are in BnF italien 1584 (Archivio Sforzesco, 1447), Gallica microfilm ark `btv1b100373864`; folio numbers
are the stamped ones, which are Mazzatinti's (1887).

## Result: read from existing decipherments

Every cipher letter of both men in the volume has a decipherment:

1. **Clear copies in one late italic hand** (the script looks eighteenth century, probably the Milan archive's before
   the papers went to Paris; not dated), each filed beside its cipher leaf. Where the copyist could not read a code
   sign he left a blank and drew the sign in the margin.
2. **Fifteenth-century decipherments**: f. 43 (of Pusterla's f. 42) and the interlinear glosses on Barbavara's two
   mixed letters f. 135 and f. 143. The glosses cover only part of the cipher runs; the runs are deciphered here with
   the R1857 key (`texts/glossed_letters.md`).

| writer | cipher leaf | date, place | decipherment | canvas |
| --- | --- | --- | --- | --- |
| Pusterla | f. 13 | 21 Jan 1447, Gualdo | f. 14 | 15-16 |
| Pusterla | not located (Mazzatinti f. 27) | 6 Feb 1447, Ferrara | f. 27 | 27 |
| Pusterla | f. 32 | 10 Feb 1447, Ferrara (margin note; copy undated) | f. 33 | 30-31 |
| Barbavara | f. 40 | 13 Feb 1447, Rimini | f. 39 | 36 |
| Pusterla | f. 42 | 14 Feb 1447, Milan (Mazzatinti: 16 Feb) | f. 41r-v; 15th-c. f. 43 | 38-40 |
| Barbavara | f. 49 | 27 Feb 1447, Rome | f. 48r-v (Mazzatinti: "Traduzione" f. 50) | 45-46 |
| Barbavara | f. 56 | 3 Mar 1447, Rome | ff. 55r-v, 57r | 53-55 |
| Barbavara | f. 62 | 4 Mar 1447, Rome | f. 61r | 58-59 |
| Barbavara | f. 69 | 6 Mar 1447, Rome | f. 68 | 65 |
| Pusterla | f. 67 | 6 Mar 1447, Ferrara | f. 66r-v | 63-64 |
| Pusterla | f. 71 | 7 Mar 1447, Ferrara | f. 70r-v | 67-68 |
| Barbavara | f. 75 | 8 Mar 1447, Rome | f. 74r-v | 71-72 |
| Pusterla | f. 77 | 8 Mar 1447, Ferrara | f. 76r-v | 73-74 |
| Pusterla | f. 81 | 10 Mar 1447, Ferrara | f. 80 | 77-78 |
| Barbavara | f. 135 | undated (late Apr 1447) | 15th-c. glosses in part; runs deciphered here | 129 |
| Barbavara and Arrigoni | f. 143 | 4 May 1447, Rome | 15th-c. glosses in part; runs deciphered here | 136 |

Texts: `texts/decipherments_18c.md` (+ `_en`) Barbavara's six copies; `texts/pusterla_copies_a.md`, `_b.md` (+ `_en`)
Pusterla's eight; `texts/glossed_letters.md` (+ `_en`) ff. 135 and 143.

Checks against the cipher (spot checks with the key): f. 69 line 1 = "in questa hora" as in the f. 68 copy; f. 40 line 1
= "se lo c[avalario]" as in the f. 39 copy; the clear words left in f. 75's cipher recur in order in the f. 74 copy. No
sign-level transcription of the copied letters was made (`transcription_missing` in the profile).

## The key and the code signs

R1857 P11 (`key_R1857_codes.tsv`): homophonic alphabet (2-4 signs a letter), vowel-consonant syllable signs (ab … uz),
word signs (che, con/cum, per, non, qua, quando, que, perché, quanto, se, ciò, come), nulls ("insignificanti"), and code
signs for Signori Malatesti, Re, dinaro, Conte d'Urbino, Duca di Ferrara, V.S., Papa, Camerlengo, Duca, Veneziani, qui,
with three signs unlabelled (∠, a Z-like sign, A). Several cells are ink-blotted. Tomokiyo had already tied R1857 P11
to ital. 1584 f. 69 (DECODE note, 2024).

The copyist's own key lacked several code labels; his blanks, read with R1857 and the context, give:

| sign | value | basis | blanks |
| --- | --- | --- | --- |
| ꝺ+÷ | Duca di Ferrara (in 1447 Leonello d'Este, Marquis) | R1857 label "Duca di Ferrara" over the sign; all five blanks fit | f. 27 ×2, f. 55v ×2, f. 74v |
| ꝺ.7 | Veneziani | R1857 label; fits | f. 80 ×2 |
| 9+o | qui | R1857 label; fits | f. 80 |
| Z-like sign | Micheletto Attendolo, the Venetian captain-general [?] | context only: "il ___ vene con tuto l'exercito de' Venetiani a Cremona"; "uno Capo di Squadra del ___ quale è suo parente" (Micheletto was Sforza's cousin) | f. 76 ×2, f. 80 |
| ∠ | open (lord of Faenza? a ∠ stands in f. 41's margin beside "il Sig. de Faenza", written out) | none | f. 27 ×2, f. 76 |
| A | open | none | f. 66 |
| ƺ, ⁊9, ϵo | open | none | f. 41 (×1 each) |

## Contents

Pusterla, having sealed the January capitoli between the Duke and Sforza, travels to Sforza (21 Jan), then to Ferrara,
where the lord of Ferrara is suspicious and the money for Sforza's condotta stalls (6-10 Feb); in Milan the Duke receives
him gladly but will not let him leave without money (14 Feb); back at Ferrara he presses the Duke of Ferrara to pay,
in vain, reports Micheletto's Venetian army at Cremona crying "viva San Marco", the move on Soncino, and the Count of
Urbino's negotiations (6-10 Mar). Barbavara, sent to Rome and King Alfonso, finds Eugenius IV dead, wins from the King
94,000 ducats a year for two years for Sforza's condotta, reports the conclave and the election of Nicholas V (6 Mar),
and the King's threat that priests are "homini da bastonate, non da pregare" (8 Mar).

## The glossed letters ff. 135 and 143 (29 Oct 2026)

Transcribed in full and every cipher run deciphered with the R1857 key and the 15th-c. glosses (`texts/glossed_letters.md`,
English `_en`, the runs as written in `texts/glossed_runs.tsv`; first pass by a subagent, checked here in outline).
f. 135: 4 runs, all read in sense ("circha li facti de Roberto da Montalboddo", "Re", "el mio restare de qua ...",
"pigliare de le altre terre ..."). f. 143: 51 runs; 9 from the key with the gloss agreeing, 31 key and gloss, 6 gloss
alone, 5 unread (143.17, .31, .35, .46, .51: no gloss, blotted key cells). Values the glosses give but the key copy does
not: ϵg = s, fto = ap (papa), t-o = i, h = l, d- = r; probable nulls Ap, 3°, otto, "presto" (struck), TT, .ll., ·l·, +.
Several pairs glossed li, per le, ciò do not decode with the key copy: the late copy may be wrong there, or the gloss
loose. A second sign-by-sign pass is advised before these values are used to correct the key.

## Remaining gaps
- f. 143 runs 143.17, .31, .35, .46, .51 and words inside 143.4, 143.41 - blocker: no-key-material; no gloss (or too faint) and the signs' cells are blotted on the only key copy.

- Code signs ∠ (×3), A (×1), ƺ, ⁊9, ϵo (×1 each) - blocker: open-codes; unlabelled on R1857 or not on it, each with one to three contexts.
- Z-like sign = Micheletto Attendolo [?] - blocker: open-codes; context only, three places.
- The 6 Feb 1447 cipher original (copy f. 27) - blocker: needs-physical-access; not found on the microfilm.
- f. 33 copy has no date line (date from a later margin note) - blocker: needs-physical-access.

The copied cipher leaves have no sign-level transcription here: the copies are complete texts, so it is recorded as
`transcription_missing` in the profile rather than as a gap.

## Verification, 14 Nov 2026 (Brice Dudout, Claude Opus 5.5)

- f. 68 "Monsignore da Cologna": the cipher f. 69 (canvas 65, l. 2) has the same word, `ott p+ p- ⊃ o-` = c-ol-og-n-a
  after `Є p7 fo ꝺ7 ⊃ per ÷` (Monsignore) and `♀ o-` (da); `ott` is the key's c, not a b sign. The slip is the
  encipherer's (or the writer's), not the late copyist's. Gap closed.
- `verify_dudout_20261114.py`: the f. 135 / f. 143 runs decoded with the key values listed in `texts/glossed_letters.md`
  alone (not the gloss-inferred t-o, h, fto, ϵg, ꝕ): 241 of 495 signs of the deciphered runs fit a key value. Only
  143.8 and 143.25 fit sign for sign; runs labelled K (143.24, .26, .48 …) rest on the gloss-inferred values too.
  Details in `VERIFY_dudout_20261114.md`.

## Escalation

- [x] siblings: every cipher leaf of both writers in ital. 1584 opened with its neighbours; the copies found for all.
- [x] clear-pages: the late-hand leaves are the decipherments; f. 43 is a 15th-c. decipherment.
- [x] known-keys: R1857 P11 applied (spot checks; the glossed letters' runs).
- [x] print: no edition of these letters found (Mazzatinti inventories them only).
- [x] key-rebuild: code signs settled from the copies' blanks (Duca di Ferrara, Veneziani, qui; Micheletto [?]).
- [x] retry: every blank in all fourteen copies checked against R1857 and context.

## Sources

- Gallica BnF italien 1584: https://gallica.bnf.fr/ark:/12148/btv1b100373864 (IIIF via openapi.bnf.fr).
- DECODE R1857 (key, ASMi; image not public domain): https://de-crypt.org/decrypt-web/RecordsView/1857
- G. Mazzatinti, *Inventario dei manoscritti italiani delle biblioteche di Francia* t. II (1887).
- Images are not committed; `crop.py` cuts regions from the full canvases.
