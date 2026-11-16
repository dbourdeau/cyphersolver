# Arabic cipher sweep 2 (16 Nov 2026)

This sweep was run by a Claude Code session (Claude Opus 5.5) for Daniel Bourdeau, in three parallel passes. It continues
`research/sweep_2026-11-15_arabic/` on the gaps that sweep left open.

**State: merged 16 Nov 2026** (owner's go-ahead) into `research/leads.json` as **2941** (row 0, Sacromonte Lead Book 17), **2942**
(row 2, Gotha) and **2943** (row 3, Sachau 218). Row 1 (Gordon's note, Durham SAD.250/1/550) was not merged: it is the same
document as catalogue 2939 and `targets/gordonmudir1884` (14 Nov 2026), so `archive_sweep_2026-10/exclude.json` leaves it out.
2941 and 2943 were vetted open (`research/vetting_2026-11-16_arabic_4/`) and promoted to the catalogue; 2942 stays a lead, unvetted
(the Gotha leaf has not been seen). The ids first given on the branch (2930-2933) were replaced by these when main's own lead ids
passed them.

| Notes | Area | Rows | Vetted |
|---|---|---|---|
| [`part_A.md`](part_A.md) | Spain, Portugal, Maghreb | 1 | 1 |
| [`part_B.md`](part_B.md) | Durham (Abbas Hilmi II HIL/64-65, Sudan Archive), Egypt-Sudan | 1 | 0 |
| [`part_C.md`](part_C.md) | Printed catalogues of Arabic manuscripts (about 60 volumes) | 2 | 0 |

## Rows

| Row | Item | Date | State |
|---|---|---|---|
| 0 | Sacromonte Lead Book 17, the "Libro mudo" (Granada) | c. 1595-97 | vetted open; plate fol. 3b seen at 1,313 x 1,317 px from the open-access edition (van Koningsveld & Wiegers 2024), which calls it undeciphered and possibly meaningless; the other cipher plates are not online |
| 1 | Durham, Sudan Archive SAD.250/1/550: Gordon to Mustafa Yawar, Mudir of Dongola, about 120 Eastern Arabic two-digit numerals | 1884 | seen; not vetted, because a possible decode (TNA PRO 30/57/4/26) could not be opened |
| 2 | Gotha, Pertsch no. 2507: an end leaf with "eine Notiz in Geheimschrift" | copy 1727, note 1764/65? | lead 2942, unvetted (Gotha viewer behind a bot check) |
| 3 | Berlin, Sachau 218, f. 231a: four lines of cipher after a Karshuni prayer | 19th c. | vetted open and promoted as catalogue 2943 (scan seen; Dudout's attempt: 59 signs, an abjad key fails, may be a reckoning table; counts only if the plaintext is Arabic) |

## Negative results

- **Durham HIL/64 and HIL/65:** all 546 canvases paged; no Arabic cipher.
- **Torre do Tombo:** all 74 units of the sixteenth-century Moroccan Arabic letters checked; all in clear.
- **BNE catalogue:** the Arabic and aljamiado manuscripts searched, through the catalogue's guest JSON API.
- ***Hespéris*:** every volume 1921-1959 read.
- **Printed catalogues:** about 60 volumes grepped.

Method note: join hyphenated line ends before grepping the djvu text of a catalogue. The Gotha hit was missed on
15 Nov for that reason.

## What is left

- **Spain:** PARES (Simancas, ACA, AHN) returned 429 and then reset the connection.
- **Blocked by bot checks or the network:** BDH, RAH, CCBAE, Hispana, BVPB, ANOM, the Moroccan national library (BNRM)
  and CSIC Simurg.
- **Other unopened items:** the TNA catalogue (Gordon's decode); the viewers at Gotha, DDB, Leiden and Qalamos; and
  Decourdemanche, Journal asiatique 1899, on the cipher of the Barbary Turks (key lead).
