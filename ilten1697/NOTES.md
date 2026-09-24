# Letters to Jobst Hermann von Ilten, 1697-1706 (GWLB Hannover, Ms XXIII 1245:4 and 1245:7)

Status: read (contemporary interlinear decipherments; transcribed and checked against the code groups)

Catalogue entry 346, "Letters to Jobst Hermann von Ilten, Hanover-Celle, catalogued as not deciphered", class C,
scored from the archive scan of 23 Sept 2026 (`oldest/scan_2026-09-23/hard_targets.md` item 8). Worked 24 Sept 2026.

## The premise was inverted

Kalliope's records for the four letters (DE-611-HS-4135390, -4136135, -4136176, -4136197) carry the note
**"Dechiffrierter Brief"**, which means *deciphered letter*. The scan read it as "nicht dechiffriert". The four
letters carry 492 code groups; all but 7 have a decipherment written over them in the recipient's office.

The images are online after all: the GWLB digital library (Kitodo, digitale-sammlungen.gwlb.de, public domain)
has the "Receuil de Lettres a Jobst Hermann d'Ilten", Parts I-IV, VII and VIII:
- Part IV = Ms XXIII 1245:4, METS `DE-611-BF-85418` (Kitodo id 61351); ff. 212r-213r = phys. 433-436.
- Part VII = Ms XXIII 1245:7, METS `DE-611-BF-85421` (Kitodo id 64590); ff. 201r-204r = phys. 405-411,
  ff. 288r-289r = phys. 579-581, ff. 329r-330r = phys. 661-663.
Image URL pattern: `https://digitale-sammlungen.gwlb.de/content/<METS id>/jpgs/default/<8-digit phys>.jpg`.
The Kitodo search form needs a POST with its own `tx_dlf[encrypted]` token (the plain GET returns "Keine Treffer").
Images are in `img/` (git-ignored), METS in `mets/`.

## The letters

| | Date | From | Folios | Code | Groups |
|---|---|---|---|---|---|
| A | Hannover, 7 Nov 1697 | Johann Ernst von Hattorf | 1245:4 ff. 212r-213r | A (15-505) | 74 |
| B | Berlin, 10 Oct 1705 | Johann Wilhelm von Heusch | 1245:7 ff. 201r-204r | B (47-1010) | 125 |
| C | Hannover, 31 Jan 1706 | Hattorf | 1245:7 ff. 288r-289r | B | 143 |
| D | Hannover, 25 May 1706 | Elector Georg Ludwig, countersigned Hattorf | 1245:7 ff. 329r-330r | B (German) | 150 |

(Group counts: `python docs/_check_profile.py --measure ilten1697/ciphertext_<x>.txt --digits`.)

Transcriptions: `letters_1697_1706.txt` (A-C) and `letter_D_1706.txt` (D), clear text with each code run as
`[groups = gloss]`. `tables.py` lists every group with every gloss it carries.

- Kalliope's title for D says "Herzog Georg Wilhelm"; the letter is signed **"Georg Ludwig Churfürst"** and the
  Kalliope creator field (Georg I.) agrees. The address leaf (f. 330r) names Ilten "jetzigem Envoyé extraordinaire
  am Königl. Preußischen Hoffe", at Berlin.
- The scan's "Hanover-Celle ministers and diplomats" is right for A-C; D is the Elector himself.

## Content

- **A (1697)**: the Elector (S.A.E., Georg Ludwig, then Elector of Hanover) thinks it would help his affairs to
  sow discord between **Kolbe** (Wartenberg) and **Barfus** at Berlin and win the friendship of one of them;
  Ilten might do it through "la femme du premier" (Kolbe's wife), with whom he is said to stand "extremement
  bien". Hattorf himself does not think it so easy.
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

- Every code run was aligned with its gloss. Code A is a small syllabary (ses = 445.71, affaires = 124.73,
  mettre = 331.107.484, Barfus = 75.256.505, vous = 500.505) with homophones (et = 237/238, la = 308/309) and
  62 as a null (`62.308... = la discorde`, `62.204... = de l'un des`, `128.445.62 = aisée`).
- Code B is one code for all three later letters and for both languages: 977 King of Prussia, 988 Gr.
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

- [x] siblings: all six Kalliope items flagged "dechiffriert" in the Ilten papers fetched; the two 1743 letters
  (Ms XXIII 1234:29,2) are a different, later code and became their own target, `ilten1743/`
- [x] clear-pages: the decipherments are interlinear on the letters themselves
- [x] known-keys: the only key sheet Kalliope lists in the Ilten papers ("Chiffre-Tabelle", 1234:31,1 pp. 386-391) is the 1740s code, not A or B
- [n/a] print: not searched in depth; the letters were read at the time and the glosses leave only 7 tokens
- [n/a] key-rebuild: 7 unglossed tokens in 418; code B has ~200 distinct groups seen once or twice, too few to
  fix syllable values outside the glossed context
- [n/a] retry: nothing left that a retry could reach

## Outcome

Read from existing decipherment: the letters were deciphered in 1697-1706 and the decipherments are on the
pages. Contribution here: found the images, corrected the catalogue premise (and the sender of D), transcribed the
four letters with their glosses, checked every gloss against the recurrence of its groups, and identified code A
and code B (with its null 91).
