# Contucio to Francesco Sforza, Venice, 7 Dec 1446 (BnF italien 1583 f. 148, DECODE R7911) — catalogue 1309

Status: read, 6 Nov 2026 (Opus 5.5). Deciphered with the envoys' own key, ASMi Carteggio Sforzesco cart. 1597 no. 14
(DECODE R5314, "Angelus cum cifra Vincentij", headed for Johannes de Stavolis, Augustinus, Baptista, Matheus et
Vincentius). 225 of 226 cipher tokens given a value and read as sense (99.6%, measured by `decode.py`); one code word
(*utinam*) open.

## The documents

Catalogue 1309 named three leaves of BnF italien 1583 (Archivio Sforzesco, 1446), all from Sforza's envoys at
Venice on 7 Dec 1446 (Mazzatinti, *Archivio storico lombardo* X, 1883, p. 233; OCR in `../it1583/asl1883.txt`):

| folio | DECODE | Mazzatinti | what is on the image | cipher |
|---|---|---|---|---|
| 148 | R7911 (P1 recto, P2 verso, P3 address) | "di Contucio a Fr. Sforza (Venezia 7 decembre). In cifre." | Contucio's report on his embassy to the Signoria: his audience, Ser Pasquale [Malipiero] to be sent to Sforza, the Count's speech, news of Lombardy; signed *Servitor et famulus Contutius* | **yes**: f. 148r lines 26-30 and 50-51, f. 148v lines 6-7 |
| 151 | R7912 | "di Giovanni Stavoli, M. Giordani, V. Amidani, Agostino, Contucio a F. Sforza (Venezia 7 decembre)" (not marked *in cifre*) | a composite photograph of clear leaves: at left a heavily corrected minute in Sforza's voice (*Inanti che fare la dicta treugua ...*), at right Sforza's letter to Boccaccino and Nicodemo, Pesaro 7 Dec 1446, with the foot of the joint letter of 7 Dec (date and signatures) laid over it | no |
| 152 | R7913 | (next entry, not given in the OCR) | the envoys' joint letter of 7 Dec: *Questa matina la Ill. S. ne respose ad lambassiata exposta per mi Contucio ...*, signed *Servi Johes de Stavolis, Augustinus, Contucius, Matheus et Vinc.* | no |

So the cipher of catalogue 1309 is all on f. 148. The catalogue's vetting note ("sign cipher lines inside clear text"
on R7912 and R7913) is wrong: there are none. The DECODE folio labels may also be shifted (the right page of R7912 is
Mazzatinti's f. 150), not checkable without the volume (ital. 1583 is not digitised; microfilm MF 16151).

Images: DECODE, binarized microfilm scans, fetched with the project cookie during the it1583 sibling sweep (23 Oct
2026; `C:\Users\dbour\cypher\.worktrees\it1583\it1583\sib\`, git-ignored). The key image is in
`targets/birago1448/keys/` (git-ignored). Not committed.

## Key

`key.md`: the key sheet transcribed, and the labels used. ASMi Carteggio Sforzesco cart. 1597 no. 14 (DECODE R5314),
an 18th-c. copy: homophonic letters (2-5 signs for a, d, e, i, o, u), a vowel+consonant syllable table, 15 word
signs, a name column (*stat* = lo Duca de Milano, Δ = la S.ria V.ra, ꝑꝑ = Signoria Veneta, ꝑꝑꝑ = Conte ...), nulls.
September 2026 (it1583) had looked at it for the f. 68/f. 70 letters and ruled it out there; the it1583 sibling sweep
of 23 Oct 2026 found its use on R7900/R7901 (f. 89, Angelus, *Cum cifra Vincentii*, with the clear text f. 90).
Check made here on that pair: R7900 *bɪ ſ q k ∍ ‹c q g ħ stat* = "che lo stato de [lo Duca de Milano]", R7901
"che lo stato del Duca de Milan".

**What f. 148 adds to the key:** *pec* = Cosimo (from the interlinear gloss on f. 148v; not on the copy); *utinam*,
a code word with no value; the letter-forms the writer used for the key's signs (the key's ƅ = e drawn as an h with
a hooked bowl; the key's h = s drawn as a k; the kp ligature for q drawn as "xp").

## Result

`transcription.txt` (sign by sign), `decode.py`, `decryption.txt`, `reading.md` (Italian with English), `en.md`.

- **f. 148r 26-30**: what the Venetians and Florentines want discussed with Sforza: "tanto per la desfatione del
  Duca de Milano quanto de la vostra perdeta, et del vostro danno, et de lo restoro d'essi"; above all, "se facesse
  la pace con [utinam], la quale fatta che fosse", they would care little for "lo Re de Ragona"; and they want Sforza
  "personalmente se trovasse a la disfatione del Duca de Milano".
- **f. 148r 50-51**: after the Count's offer to the Signoria: "Questa tale oferta parve a Cosimo che in ogni modo se
  devesse fare" (Cosimo de' Medici advised that the offer be made).
- **f. 148v 6-7**: "questa parte parve a Cosimo se devesse dire", with the contemporary decipherment written over
  it (*questa*, *parte*, *parve*, *a cosimo*, *se devesse*, *dire*).

Measured (`decode.py`): 226 cipher tokens + 1 null; 225 given a value (99.6%), every one in a word of the reading;
open: 1 (*utinam*). Two sign shapes uncertain (end of *Ragona*; first sign of *parve*, under the library stamp),
fixed by sense. Reading reviewed as sentences (grade A): every cipher clause builds with the clear text around it.

Method: **read with known key**. The key sheet is headed with the names of the Venice envoys of 1446 (Stavoli,
Agostino, Battista, Matteo, Vincenzo), so it is the key of this correspondence; it was not on the letter's DECODE
record, and nobody had applied it to f. 148. The verso's interlinear gloss is a partial contemporary decipherment (the
31 tokens of the verso); it confirmed the key and gave *pec*, but the rest was deciphered with the key.

Prior art: none found. DECODE R7911 Non-decrypted, no names; Mazzatinti gives the heading only; web search on the
correspondents, date and embassy (6 Nov 2026) and the it1583 and visconti1446 notes give no reading; the vetting of
2 Nov 2026 found nothing in Tomokiyo, Lasry or the literature.

Context: Venice and Florence were allied with Sforza against Filippo Maria Visconti in the war of 1446-47; the
Venetian victory at Casalmaggiore (Sept 1446) is the "prosperous victories" the Count's speech congratulates. Ser
Pasquale [Malipiero] was named Venetian ambassador to Sforza (f. 148r, f. 152). Cosimo de' Medici advising the
envoys' wording at Venice is new detail.

## Remaining gaps
- code word *utinam* (written *vtinã*), f. 148r line 28, "la pace con [utinam]" - blocker: open-codes; once only, not on the 18th-c. key copy (whose code column has four unlabelled entries), and the sense (a power to make peace with so that the King of Aragon matters little) does not fix it
- two uncertain sign shapes (last sign of *Ragona*, f. 148r 29; first sign of *parve*, f. 148r 50, under the stamp) - blocker: illegible; binarized microfilm scan; the sense fixes both

## Escalation
- [x] siblings: R7900-R7915 (ff. 89-158) opened in the it1583 sweep of 23 Oct 2026; ff. 151 and 152 of this group are clear; R7900/R7901 is the one other letter in this key, with its clear text, checked here for *stat*; the envoys' letter of 14 Dec (f. 155) is not on DECODE
- [x] clear-pages: f. 152 and the clear parts of f. 148 read for context; the verso gloss transcribed and compared (agrees)
- [x] known-keys: cart. 1597 no. 14 fits; no other key needed
- [x] print: Mazzatinti 1883; web search on the correspondents and embassy; no edition of the letter found
- [x] key-rebuild: *pec* added from the gloss; *utinam* tested for a sense value: none fixed
- [n/a] retry: one code word open, nothing else unread

## Sources

- BnF italien 1583 ff. 148, 151, 152, via DECODE R7911, R7912, R7913 (images not public domain).
- Key: Archivio di Stato di Milano, Carteggio Sforzesco cart. 1597 no. 14, DECODE R5314.
- G. Mazzatinti, "Inventario delle carte dell'archivio sforzesco contenute nei codici italiani 1583-1593 della
  Biblioteca nazionale di Parigi", *Archivio storico lombardo* X (1883), p. 233.
- `../it1583/NOTES.md` (the R7900/R7901 lead), `../visconti1446/NOTES.md` (the Duke's own slips in the same volume,
  a different key).
