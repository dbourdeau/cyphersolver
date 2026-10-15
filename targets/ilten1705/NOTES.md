# Heusch, Hattorf and the Elector Georg Ludwig to Jobst Hermann von Ilten, 1705-1706, code B (GWLB Hannover, Ms XXIII 1245:7)

Status: read (contemporary interlinear decipherments; transcribed and checked against the code groups)

Split on 14 Oct 2026 from `ilten1697` under the one-key rule (George Lasry, 14 Oct 2026). Until then these three
letters were filed with Hattorf's letter of 7 Nov 1697 (letter A), which is in another code (code A, groups to ~505);
it stays at [`targets/ilten1697/`](../ilten1697/NOTES.md) (a different cipher, with its own page). Code B is one code
for all three letters below. The work was done on 24 Sept 2026 in the ilten1697 session and is carried over from its
NOTES; `ciphertext_B/C/D.txt`, `letter_D_1706.txt` and the B-C part of the transcription (`letters_BC_1705_1706.txt`)
moved here on 14 Oct 2026. Access to the images (GWLB Kitodo, METS `DE-611-BF-85421`) is described in
`targets/ilten1697/NOTES.md`.

Catalogue entry 346 (with ilten1697).

## The letters

| | Date | From | Folios | Code | Groups |
|---|---|---|---|---|---|
| B | Berlin, 10 Oct 1705 | Johann Wilhelm von Heusch | 1245:7 ff. 201r-204r | B (47-1010) | 125 |
| C | Hannover, 31 Jan 1706 | Hattorf | 1245:7 ff. 288r-289r | B | 143 |
| D | Hannover, 25 May 1706 | Elector Georg Ludwig, countersigned Hattorf | 1245:7 ff. 329r-330r | B (German) | 150 |

(Group counts: `python docs/_check_profile.py --measure targets/ilten1705/ciphertext_<x>.txt --digits`; `tables.py`:
418 groups, 215 distinct, 7 unglossed.)

Transcriptions: `letters_BC_1705_1706.txt` (B, C) and `letter_D_1706.txt` (D), clear text with each code run as
`[groups = gloss]`. `tables.py` lists every group with every gloss it carries.

- Kalliope's title for D says "Herzog Georg Wilhelm"; the letter is signed **"Georg Ludwig Churfürst"** and the
  Kalliope creator field (Georg I.) agrees. The address leaf (f. 330r) names Ilten "jetzigem Envoyé extraordinaire
  am Königl. Preußischen Hoffe", at Berlin.

## Content

- **B (1705)**: Heusch reports from Berlin that the chamberlain Count Wartensleben, back from Hanover, has put the King of Prussia in good dispositions and spoken well of Sophia Dorothea ("Madame la Princesse fille de
  S.A.E."), without raising the marriage to the King but raising it with the Grand Chamberlain (Kolbe von
  Wartenberg); the minister is committed to another match; Mme de Bülow and Mlle de Pöllnitz must not appear to
  have a hand in it; it can succeed only through the Grand Chamberlain.
- **C (1706)**: Ilten's two letters to the Elector reached him privately; Ilten is to say he knows nothing if the
  marriage is raised at Berlin, since it is not the custom to offer the princesses of this house so soon; the
  Elector wants the matter insinuated gracefully. Clear postscript: Goertz, Eltz, Schönborn, the Lübeck see, and
  the threat of Charles XII coming out of Poland.
- **D (1706)**: the Elector hears from Ilten that the King in Prussia means to ask in person for his daughter's
  hand for the Crown Prince; Ilten is to head off the personal visit, discreetly, through the Ober-Cammerherr.
  (The marriage of Frederick William and Sophia Dorothea took place on 28 Nov 1706.)

## Check of the contemporary decipherment

- Code B is one code for all three letters and for both languages: 977 King of Prussia, 988 Gr.
  Chambellan / Ober-Cammerherr, 609 Princesse / Princessin, 665 Roy / König, 476 mariage, 224 de, 405.709.543
  in-si-nu- ("insinuer", "n'insinuiés", "insinuationes"). **91 is a null** (per-son-[91]-ne,
  de-man-[91]-de-r, and twice in D). The same group carries the same gloss wherever it recurs (`tables.py`).
- No gloss contradicts another occurrence of its group. The glosses read as sense throughout.

## Remaining gaps

- B f. 201v: group 419 after "à" (463 written above it) - blocker: open-codes; no gloss and no key; the sense
  ("rendu justice à Madame la Princesse") is complete without it
- C f. 288r-v: 709.276 before "juger", 78? before "trouve", 626 after "choque", 728.36? after "on" (6 tokens) -
  blocker: open-codes; unglossed by the interliner, code B has no key; each sits in a sentence that reads
- B/C/D: several groups at the right margin run into the binding (70?, 5?, 50?, 9?, 112?, 36?, 124?, 6?, 74?) -
  blocker: needs-physical-access; the glosses over them are legible, so the reading does not depend on them

## Escalation

- [x] siblings: all six Kalliope items flagged "dechiffriert" in the Ilten papers fetched; letter A of 1697 is code A
  (`targets/ilten1697/`), the two 1743 letters (Ms XXIII 1234:29,2) a later code (`targets/ilten1743/`)
- [x] clear-pages: the decipherments are interlinear on the letters themselves
- [x] known-keys: the only key sheet Kalliope lists in the Ilten papers ("Chiffre-Tabelle", 1234:31,1 pp. 386-391) is the 1740s code, not code B
- [n/a] print: not searched in depth; the letters were read at the time and the glosses leave only 7 tokens
- [n/a] key-rebuild: 7 unglossed tokens in 418; code B has ~200 distinct groups seen once or twice, too few to
  fix syllable values outside the glossed context
- [n/a] retry: nothing left that a retry could reach

## Outcome

Read from existing decipherment: the letters were deciphered in 1705-06 and the decipherments are on the pages.
Contribution here: found the images, corrected the catalogue premise and the sender of D, transcribed the three
letters with their glosses, checked every gloss against the recurrence of its groups, and identified code B (with
its null 91).
