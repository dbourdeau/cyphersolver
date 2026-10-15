# Hattorf to Jobst Hermann von Ilten, Hannover, 7 November 1697, code A (GWLB Hannover, Ms XXIII 1245:4)

Status: read (contemporary interlinear decipherment; transcribed and checked against the code groups)

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). Until then this entry held four letters to
Ilten in two codes. This entry is letter A, in code A. Letters B, C, D (1705-06) are in code B and are now
[`targets/ilten1705/`](../ilten1705/NOTES.md) (a different cipher, with its own page), with `ciphertext_B/C/D.txt`,
`letter_D_1706.txt` and the B-C transcription (`letters_BC_1705_1706.txt`). The transcription file of A is now
`letter_A_1697.txt`; `tables.py` here covers code A only.

Catalogue entry 346, "Letters to Jobst Hermann von Ilten, Hanover-Celle, catalogued as not deciphered", class C,
scored from the archive scan of 23 Sept 2026 (`research/oldest/scan_2026-09-23/hard_targets.md` item 8). Worked 24 Sept 2026.

## The premise was inverted


Kalliope's records for the four letters (DE-611-HS-4135390, -4136135, -4136176, -4136197) carry the note
**"Dechiffrierter Brief"**, which means *deciphered letter*. The scan read it as "nicht dechiffriert". The four
letters carry 492 code groups; all but 7 have a decipherment written over them in the recipient's office. Letter A's 74 groups are all glossed.

The images are online after all: the GWLB digital library (Kitodo, digitale-sammlungen.gwlb.de, public domain)
has the "Receuil de Lettres a Jobst Hermann d'Ilten", Parts I-IV, VII and VIII:
- Part IV = Ms XXIII 1245:4, METS `DE-611-BF-85418` (Kitodo id 61351); ff. 212r-213r = phys. 433-436.
- Part VII = Ms XXIII 1245:7, METS `DE-611-BF-85421` (Kitodo id 64590); ff. 201r-204r = phys. 405-411,
  ff. 288r-289r = phys. 579-581, ff. 329r-330r = phys. 661-663.
Image URL pattern: `https://digitale-sammlungen.gwlb.de/content/<METS id>/jpgs/default/<8-digit phys>.jpg`.
The Kitodo search form needs a POST with its own `tx_dlf[encrypted]` token (the plain GET returns "Keine Treffer").
Images are in `img/` (git-ignored), METS in `mets/`.

## The letter

| | Date | From | Folios | Code | Groups |
|---|---|---|---|---|---|
| A | Hannover, 7 Nov 1697 | Johann Ernst von Hattorf | 1245:4 ff. 212r-213r | A (15-505) | 74 |

(`python docs/_check_profile.py --measure targets/ilten1697/ciphertext_A.txt --digits`: 74 groups, 57 distinct.)

Transcription: `letter_A_1697.txt`, clear text with each code run as `[groups = gloss]`. `tables.py` lists every
group with every gloss it carries.

## Content

- **A (1697)**: the Elector (S.A.E., Georg Ludwig, then Elector of Hanover) thinks it would help his affairs to
  sow discord between **Kolbe** (Wartenberg) and **Barfus** at Berlin and win the friendship of one of them;
  Ilten might do it through "la femme du premier" (Kolbe's wife), with whom he is said to stand "extremement
  bien". Hattorf himself does not think it so easy.

## Check of the contemporary decipherment

- Every code run was aligned with its gloss. Code A is a small syllabary (ses = 445.71, affaires = 124.73,
  mettre = 331.107.484, Barfus = 75.256.505, vous = 500.505) with homophones (et = 237/238, la = 308/309) and
  62 as a null (`62.308... = la discorde`, `62.204... = de l'un des`, `128.445.62 = aisée`).
- No gloss contradicts another occurrence of its group (`tables.py`: 74 groups, 57 distinct, 0 unglossed).

## Remaining gaps

None: all 74 groups carry a gloss.

## Escalation

- [x] siblings: all six Kalliope items flagged "dechiffriert" in the Ilten papers fetched; letters B-D are code B
  (`targets/ilten1705/`), the two 1743 letters (Ms XXIII 1234:29,2) a later code (`targets/ilten1743/`)
- [x] clear-pages: the decipherment is interlinear on the letter itself
- [x] known-keys: the only key sheet Kalliope lists in the Ilten papers ("Chiffre-Tabelle", 1234:31,1 pp. 386-391) is the 1740s code, not code A
- [n/a] print: not searched in depth; the letter was read at the time and every group is glossed
- [n/a] key-rebuild: nothing unglossed
- [n/a] retry: nothing left

## Outcome

Read from existing decipherment: the letter was deciphered in 1697 and the decipherment is on the page.
Contribution here: found the images, corrected the catalogue premise, transcribed the letter with its glosses,
checked every gloss against the recurrence of its groups, and identified code A (with its null 62).
