# philip1546 — Prince/King Philip (II) → Ferrante Gonzaga, Modena (catalogue 1561)

Status: in progress

Catalogue no. 1561 (`docs/solve/1561.html`). Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera F,
Felipe II, sfasc. I and II. Eight letters, Spanish, Philip (as prince, later king) → Ferrante I Gonzaga, governor of Milan,
signed `El Principe`, secretary Perez. Licence CC BY-NC-SA.

## Access (worked 8 Nov 2026, plain curl, no bot check)
- Manifest `https://edl-jarvis.cultura.gov.it/meta/iiif/<record id>/manifest`; the manifest id equals the Lodovico record id.
  The catalogue lists only four record ids; the other four came from the search
  `ricercadl.aspx?ricdccreator=Felipe+II&rictip=documenti+manoscritti&nris=48&page=1..3` (46 Felipe II records in all).
- `fetch.py` downloads every page at 1200 px into `img/` (git-ignored, 17 MB). `crop.py <set> <canvas> x y w h out.jpg`
  fetches a native-detail crop (pages are 5400 x 7400; x y w h are given at the 1200-px page width).

| Set | Letter | Record id | Pages | Decipherment in the file |
|---|---|---|---|---|
| a1546 | 25 Jun 1546, sfasc. II cc. 5-6 | 68f59b4c-c5e3-431f-9226-00927538c698 | 5r (clear opening, then about 13 lines of signs), 5v (signs, signature) | none seen |
| b1547 | 23 May 1547, sfasc. II cc. 9-11 | 9c67dac4-f213-4484-9e5e-fb5c1408ea76 | 9r (about 10 lines), 9v (about 17 lines) of signs | c.11r-11v clear text, about 22 lines (to be checked against the signs); c.10r is another, clear letter |
| c1548 | 4 Aug 1548, sfasc. I cc. 10-11 | 96578a9c-2963-4448-8786-5fa35a3c44e7 | 10r with three short sign blocks between clear paragraphs | none seen |
| d1549 | 8 Mar 1549, sfasc. I cc. 12-14 | fa08c81b-4cf3-4914-878e-98059ad124b8 | 12r (about 12 lines of signs) | c.14r clear text (to be checked) |
| e1551a | 24 Nov 1551, sfasc. I cc. 26-27 | 3f4f51da-b3b0-4159-9824-f22958c248dd | 26r (sign block near the foot) | none seen |
| f1551b | 24 Nov 1551, sfasc. I cc. 28-29 | 9ad3b749-cbac-4adc-94cd-b080227c220f | 28r-29r | not yet viewed |
| g1553 | 14 Mar 1553, sfasc. I cc. 35-40 | 6990ecfe-8ee7-4994-b2d6-3ccc332ee9e2 | 12 images | not yet viewed |
| h1563 | 16 Jun 1563, sfasc. II cc. 24-25 | 499ee545-fcd1-4afe-9776-a21cdbf0efb4 | 4 images | not yet viewed |

The 1551 letter on cc. 26-27 also has a parchment patent (two images, `BEU_A.C.felipe.ii...0026-01`, headed PHILIPPVS): not a cipher.
The record for 16 Jun 1563 gives a recipient who died in 1557 (Ferrante I); check the recipient.

## System: the Imperial Cipher (found 8 Nov 2026)
The signs are those of Charles V's Imperial Cipher, the same family as the Gonzaga letters in `targets/gonzaga1549/`
(table `targets/gonzaga1549/sign_table.tsv`, keys in `targets/gonzaga1549/ref/`, Masia 2009 / Meister). It is a syllabary with a vowel mark,
a few lone-letter signs and nulls; `ap` = n, which is why that sign is so frequent.

Test on the 1547 letter, c.9r line 1 (27 signs, read by eye with the gonzaga1549 table, before looking at c.11r):
`6.`=la `y-two-dots`=vi `y`=si `triangle`=ta `crossed c`=que `q-hook`=hi `pi-shape`=zi `[b]` `theta`=s `crossed triangle`=te `theta`=s
`S`=e `ap`=n `[lambda-colon]` `6`=la `theta`=s `e-hook`=fro `ap`=n `crossed triangle`=te `g.`=ra `theta`=s `x-o`=de `dash-o`=l
`lambda-two-dots`=pi `6`=e `lo`=mo `ap`=n: `la visita que hiziStes en las fronteras del Piemon...`, which is the opening of the clear text on c.11r
(`La visita que hizistes en las fronteras del Piemonte`). Two signs in that line have no value (`b` after `zi`, the lambda-colon before `las`):
probably nulls. So c.11r is the decipherment of c.9r-9v and the table fits Philip's letters.

## Done and not done
- Done: all eight letters located and downloaded; system identified; one line read as a test. Nothing else is read.
- First look at the 25 Jun 1546 letter, c.5r line 1: begins `lo que ...` (`6o`, crossed c), then signs not yet settled (several `x`
  shapes, a tall crossed 7 and a dotted 8). Not read.
- Not done: aligning c.9r-9v with c.11r-11v sign by sign (the key for this hand, adjacent plaintext); the same for c.12r against c.14r;
  transcription files per page; reading 1546, 1548, 1551 (two), 1553, 1563; viewing f1551b, g1553 and h1563 for what cipher they carry
  (g1553 and h1563 may be another system); profile.json; write-up; DECODE queue entry.
- No decipherment is known elsewhere (catalogue vetting 29 Oct 2026); no search beyond that was repeated.

## Remaining gaps
- Every letter is unread except one test line (1547 c.9r line 1). All gaps are open by choice (work not yet done), none has an outside blocker yet:
  1546 c.5r-5v; 1547 c.9r-9v (key available on c.11r-11v); 1548 c.10r (three blocks); 1549 c.12r (clear copy on c.14r);
  1551 cc. 26r and 28-29; 1553 cc. 35-40; 1563 cc. 24-25. Open codes: nulls in the 1547 line (`b`, lambda-colon) and the signs of the 1546 line 1.

## Escalation
- Siblings and clear copies: c.11r-11v (for 1547) and c.14r (for 1549) are in the same file; to be aligned next.
- Known keys: Imperial Cipher table from `targets/gonzaga1549/sign_table.tsv`; fits (see System).
- Key rebuild: from the aligned 1547 and 1549 pairs, then applied to 1546, 1548, 1551, 1553, 1563.
- Print and retry: not started. Pages of 1551 (cc. 28-29), 1553 and 1563 still to be viewed for the cipher type.
