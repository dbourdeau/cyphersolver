# georg1643: Hesse-Darmstadt cipher letters of 1643 in D 4 Nr. 113/9 (catalogue 568: Landgrave Georg II's encrypted correspondence, 1634-1647)

Status: in progress

Catalogue **568** lists 17 files of the Hessisches Staatsarchiv Darmstadt (E 8 A Nr. 113/4, 118/3, 121/12, 142/5,
150/2, 211/9, 217/1, 221/3, 227/2, 227/9, 240/2; D 4 Nr. 7/6, 7/9, 7/12, 18/4, 23/4, 113/9) with Georg II's
partly enciphered correspondence. Of these only **D 4 Nr. 113/9** is digitised (18 images); this folder covers it.
The other 16 files have DDB records but no images (checked on the image server, 14 Nov 2026) and must be ordered.

## Access (script-friendly route, 14 Nov 2026)

Archivportal-D and the DDB viewer sit behind an Anubis bot check, and the Arcinsys Hessen search needs a session token.
The DDB API's EDM record is open and lists the scans: `https://api.deutsche-digitale-bibliothek.de/2/items/<DDB id>/edm`
gives `https://digitalisate-he.arcinsys.de/hstad/d_4/113--9/hstad_d_4_nr_113--9_0NN.jpg` (3500 x 2541 px, CC0 / CC BY
4.0). The same pattern serves D 4 Nr. 141/2 (7 images) and D 4 Nr. 239/1 (at least 41). No image is committed.

## D 4 Nr. 113/9: what it holds

"Reise des Landgrafen Johann v. Hessen-Braubach von Darmstadt nach Gießen", 18 fols., Nov 1643; "Enthält u.a.:
Teilweise chiffrierte Korrespondenz". Three cipher pieces in two systems:

| piece | image | date, parties | system | decipherment of the time |
|---|---|---|---|---|
| fol. 2 | 02 | letter of 8 Nov 1643 to a "Herr Gevatter" (signed Wolfgang? illegible), clear with cipher words | letters, digits and signs (∇, #, +) | words written over most cipher words (e.g. "reiß", "Darmstatt", "Homburg", "Schloss", "Kolsterbach"?) |
| fol. 5 | 03 | postscript of 9 Nov 1643 | same | words over the cipher words ("die convoy von", "Landgraff Johann", "Herrn Vicecantzler", "zwanzig", ...) |
| **fol. 17** | 15 | the President, Vice-Chancellor and councillors at Giessen to Georg II, Giessen, 18 Nov 1643 | **two-digit numbers** (10-39, with 5, 8+, 9 and one code sign) | two '#' notes in the left margin that paraphrase the two blocks |

Fol. 1 is a draft postscript of 22 Nov 1643 in clear, with passages underlined (perhaps those to be put in cipher in the
fair copy); no cipher on it.

## Fol. 17 (18 Nov 1643): read

- Transcription `c_f17.txt`: two blocks, 9 lines, 216 number groups (one pass, one reader).
- System: one-for-one substitution of letters by two-digit numbers, homophones for t (8+, 32) and m (22, 24), one code sign
  (a Z with a vertical stroke, probably "Landgraf Johann"). Key `key_f17.json`, 24 values, rebuilt from this letter:
  the margin notes give the sense and the groups follow it letter for letter ("und erheblichen", "persönlich",
  "communiciren"); every group then decodes to German.
- Reading `reading_f17.md`: the councillors report that "zu ewerer fürstl. gn. es sich eilends wider hinaus gen
  Darmstatt erheben und mit ihro von ainigen wichtigen und erheblichen puncten persönlich comuniciren" and that "dero herr
  bruder [?Landgraf Johann] übermorgen montags abends, gelibts gott, bey ewr fürstl. gnad. zu Darmstat anlangen werden".
  Read share 0.951 (39 words read, the code sign's two-word value counted as two holes). English translation there.
- Method: key recovered based on adjacent plaintext (the writer's own margin summaries on the same page).
- The clear text around it: the Landtag at Giessen ends well and as the Landgrave intended; the estates have written to the
  widowed Landgravine at Cassel (Amalie Elisabeth) and to the Lower Hessian estates.

## Fols. 2 and 5: symbol cipher with words of the time written over it (open)

The cipher words mix letters, digits and signs. On fol. 5 the gloss "die convoy von" over "6tzncrFctt Fcm" fits a
letter-for-letter table (6 d, t i, z e, n c, c o, r n, F v, m n), but the next glossed word ("Landgraff Johann" over
"4rr6Fmratc6rr") does not fit any single table as read here. Either the reading of similar signs (c/e, r/x, 6/b) is off,
or the system has code groups. Not transcribed in full.

Key lead: the Hausarchiv file of Landgrave Johann's correspondence with Georg II (1628-29, 1634-46) is described as
containing a "Chiffrentabelle des Landgrafen Johann" (found by web search, 14 Nov 2026, on archivportal-d.de; shelfmark
not yet identified). Fols. 2 and 5 concern Johann's journey, so his table is the first key to test.

The filed key D 4 Nr. 141/2 ("2 Alphabete einer Geheimschrift", 1652-58, Landgrave Friedrich, the Cardinal) is a later
symbol alphabet; it is not the fol. 17 system, and was not tested against fols. 2 and 5.

## Prior art

No edition or decipherment of these letters found (web search 14 Nov 2026; catalogue check of 26 Oct 2026). The catalogue's
note of Brice Dudout's email (27 Oct 2026: "key B confirmed"; two pages of Ferdinand III's war council, 31 Jan 1637,
undeciphered) concerns the E 8 A files, not D 4 113/9; nothing of it is in this repository.

## Remaining gaps

- Fols. 2 and 5 (symbol cipher) - blocker: none outside; workable. Transcribe sign by sign, rebuild the key from the
  interlinear words, test Landgrave Johann's cipher table once located.
- The code sign on fol. 17 - blocker: no key material for it beyond the margin note (probable value only).
- The 16 other files of catalogue 568 (E 8 A ..., D 4 7/6 ... 23/4) - blocker: not digitised; need a scan order.
- D 4 Nr. 239/1 ("Auflösungen", 41+ images) not looked at - workable.

## Escalation

- [x] siblings: the three pieces of D 4 113/9 compared; fol. 17's own margin notes used as cribs
- [x] clear-pages: the clear text of fol. 17 read for context; fol. 1 (draft) checked, no cipher
- [ ] known-keys: Landgrave Johann's "Chiffrentabelle" (lead) and D 4 239/1 not yet tested; D 4 141/2 checked, a later system
- [x] print: one web search, nothing
- [x] key-rebuild: fol. 17 key rebuilt (complete for the letter); fols. 2/5 not yet
- [ ] retry: fols. 2/5
