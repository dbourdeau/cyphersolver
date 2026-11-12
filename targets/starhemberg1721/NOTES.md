# Starhemberg to Giuseppe Riva, 1720-1721: three letters in a letter-number cipher (Biblioteca Estense, Autografoteca Campori, Starhemberg; lead 1568)

Status: read in part, contributed. Most of the cipher was deciphered at the time between the lines; what is new is the
part that carries no gloss. No claim of a first reading (see Prior art).

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic). Issue #432 and its comment; reviewed by
Daniel Bourdeau on 12 Nov 2026, who asked for this cipher to have its own entry, apart from the Riva table
(`targets/riva1722`).

## What the documents are

Three letters from Count Starhemberg in Vienna to Giuseppe Riva, the Duke of Modena's agent in London. Modena, Biblioteca
Estense Universitaria, Autografoteca Campori, S, "Starhemberg (von), Guido". The library files them under Guido; the
content fits Conrad Sigmund von Starhemberg ("il mio ritorno in Inghilterra ... con carattere d'Ambasciatore", 31 May
1721), which the reviewer accepts.

| id | date | leaves | cipher units | read (strict) | units with no gloss | read |
|---|---|---|---|---|---|---|
| starhemberg_1720-12-21 | 21 Dec 1720 (date not checked at full scale) | cc. 13-14, postscript on 13v | 33 | 30 = 90.91% | 13 | 10 = 76.92% |
| starhemberg_1721-05-31 | 31 May 1721 | cc. 17-18, cipher on 17r | 104 | 93 = 89.42% | 36 | 31 = 86.11% |
| starhemberg_1721-06-14 | 14 Jun 1721 | cc. 1-2 | 289 | 249 = 86.16% | 110 | 97 = 88.18% |

Sums: 30 + 93 + 249 = 372 of 33 + 104 + 289 = 426; without a gloss 10 + 31 + 97 = 138 of 13 + 36 + 110 = 159.
Per-line sums: `counts.txt`. Images: Estense IIIF, `https://edl-jarvis.cultura.gov.it/meta/iiif/<record id>/manifest`;
short record ids from our logs: ab7fcc2d (31 May 1721), 4f2940f8 (14 Jun 1721), 7667c7b4 (21 Dec 1720). Not in git.
The 14 Jun 1721 and 21 Dec 1720 records carry no cipher tag in the library's catalogue.

## The system and the key

One number per letter, separated by dots. Vowels are 1-5 (a e i o u) and again 10 20 30 40 50. Consonants run in
alphabetical order from 11: b c d f g l m n p q r s t z = 11 to 24. A double stroke after a group doubles the consonant.
Numbers from 80 up are codes for common words and names (80 questo, 84 et, 86 essere, 89 che, 94 lo, 96 di, 97 della,
98 di, 108 Hoffman, 210 Duca: all from the glosses). It is not the Riva table: K3 fails on these letters.

Key K21 (`key.tsv`): 22 letter values and 210 = Duca, every one from the contemporary gloss at the foot of c. 17r, which
covers the first half of the 31 May letter and breaks off in mid-word. Method: key from plaintext beside the ciphertext.
K21 was then applied once, unchanged, to the rest of that letter and to the other two letters.

The q question (raised by the reviewer). In K21 20 = e, and 20 also stands where q is wanted (quelli, qui, acquistati).
The order of the table explains it: 20 is the second vowel among the tens and the tenth consonant in the run from 11,
so the writer's table had 20 twice. The same order gives 11 = b and 24 = z, both confirmed by words (Borosini glossed;
ziffere, notizia, nazione). This is derived, not seen in a key sheet, and no count uses it. The reviewer notes that
`targets/selvatico1719` has 20 = qu and that this cipher resembles the 1719 table: the two share 1-4 = a e i o and
12-15 = c d f g. A full-scale recheck of every 20 was asked for and is NOT done; one crop was looked at (`holes.md`).

## What the letters say

- 21 Dec 1720, postscript: "Lei continui di scrivermi in ziffere spesso" (keep writing to me in cipher, often). The
  first line is glossed; "in ziffere spesso" is not.
- 31 May 1721: his return to England is certain, as Ambassador. In cipher: the Duke of Modena does well to continue his
  devotion to the House of Austria (glossed); "those who have been faithful to it have gained very great advantages
  ... on this point" (not glossed; new).
- 14 Jun 1721: the South Sea affair; whether an opera company will be formed in London this year and what it would pay
  an excellent singer. In cipher: Borosini is in Vienna, sings tenor, has no equal in Europe, and would join if asked
  for in the name of the King or of the company; a letter of request to Starhemberg would do. A certain Colman has
  arrived to serve under St Saphorin; is he the son of "Hoffman"? And he wants the talk of court and nation in London
  about Vienna's conduct towards "Sig. Cnigt" (Robert Knight, the South Sea cashier, by sense). New, with no gloss:
  "suo parec[...]io", the proposal and "servirò ... il tenore Borosini", "il St. Saporin", "al sig. [Hoffman]",
  "toccante il sig. Cnigt", the closing words and the signature code.

## Corrections to our issue

1. The comment on #432 gave the two extra letters as figures only. Their transcriptions, decodes and readings are here.
2. 21 Dec 1720: 31/33 becomes 30/33. The 24 of "ziffere" was counted read as t.
3. The comment said the 21 Dec letter was "READ"; at 90.9% it is read in part.
4. "20 = e or a slip of the writer" (issue): replaced by the table-order explanation above, still unproved.

## Remaining gaps

- every 20 re-read at full scale (20 = e in "verso", "essempi"; q in "quelli", "qui"); "acquistati" (31 May, 17r.L6-L7), where the table-order reading of 20 as q leaves 23 to be u in one place and t in the others - blocker: illegible; the 1,400-px image shows clean figures but no separate sign for the two values of 20, and no key sheet of the writer is known
- codes 59, 9, 62, 85, 236, 301 and four places of the 14 Jun 1721 letter (`holes.md`) - blocker: open-codes; each occurs once or twice with no context that decides it
- the glosses of 14 Jun 1721 and 21 Dec 1720 are not transcribed diplomatically, and the clear text of the letters mostly not - blocker: needs-physical-access; the full record ids of these two letters are known only as short ids (4f2940f8, 7667c7b4), the short-id manifests give 404 and the library's catalogue pages were not reachable, so the images could not be fetched at integration
- Lindgren 2016 not seen - blocker: needs-physical-access; Il Saggiatore musicale 23/2, pp. 277-374, paywalled, a library copy is needed; the Borosini passage of 14 Jun 1721 is the most exposed
- cc. 3-12 and 15-16 of the Starhemberg file, not examined for more of this cipher - blocker: needs-physical-access; not reachable from here

## Further work (outside this target's texts)

- No second transcription and no second reader of the three letters. At integration all 104 groups of the 31 May 1721
  letter (c. 17r) were compared with the image by an AI reader: all agree; the 14 Jun and 21 Dec transcriptions were
  not compared with any image by anyone but their transcriber.

## Integration check (12 Nov 2026)

- `scripts/build.py` rerun on a copy: 30 of 33, 93 of 104, 249 of 289 (372 of 426 = 87.32%); unglossed 10 of 13, 31 of 36,
  97 of 110 (138 of 159 = 86.79%); `units.tsv` and `decryptions/` regenerate identically. A second decoder written from
  `key.tsv` and the transcriptions alone agrees on 33 of 33, 104 of 104 and 282 of 289 groups (the seven differences are
  trailing doubt marks and the sign for an illegible group).
- Timestamps: RFC 3161 replies (Sectigo) of 11 Nov 2026: 31 May 1721 22:07:00 GMT (it holds `KEY_K21.tsv`, md5
  0bbf709160237928df5c7390547d7183), 21 Dec 1720 23:09:47, 14 Jun 1721 23:29:11. The key file is byte-identical in the
  three stamps and the SHA-256 of every stamped file in the repository equals its manifest line, so the key was fixed before
  the other two letters were transcribed. The glossed units of 31 May (68 of 104) are the key's own source and prove nothing;
  the glossed units of 14 Jun (179) are a check that was not used to build the key but is not counted as a test either.
- Image: c. 17r of 31 May 1721, all eight cipher lines, 104 groups: the transcription agrees throughout, and the foot gloss
  ends "mostrano che [struck] e vel:" as quoted.
- The Riva table K3 applied to the 31 May letter gives no language; K21 gives Italian. Two keys, two folders: the Riva table
  is in `targets/riva1722`. K21 is related to the 1719 table of `targets/selvatico1719` (b c d f g at 11-15, n at 18, q or qu
  at 20) but r s t z (21-24 here, 25-27 and 29 there) differ.
- Counting: the figures count cipher units under the strict rule of this folder (codes, the doubling mark, doubts and emended
  units are not read). A rough count by words, from the asterisk spans of `readings/` (a word with a bracket or `?` as
  open), gives about 57% for the three letters (14 Jun 1721 54%): an estimate, not a measurement. Neither is near 95%.

## Escalation

- [x] siblings: the Estense Starhemberg file swept; two more letters in this cipher found (14 Jun 1721, 21 Dec 1720); the other letters of the file are in the Riva table (`targets/riva1722`)
- [x] clear-pages: the foot gloss of c. 17r is the contemporary decipherment of the first half of the 31 May letter and the key's only source; the glosses of 14 Jun and 21 Dec read between the lines
- [x] known-keys: the Riva table K3 (597 and 3,435 of 5,000 shuffled keys as good: it does not read these letters) and the 1719 table of `selvatico1719` (r s t z differ) tried
- [x] print: Lindgren and Timms 2003 searched in an open copy (no cipher); Lindgren 2016 not seen (paywalled), recorded as a gap
- [x] key-rebuild: K21 is the gloss values only (22 letters, one code); the table-order structure (b c d f g l m n p q r s t z from 11, vowels again at 10 to 50) explains the second value of 20 and is not used for any count
- [x] retry: every unit not read is in `units.tsv` with its reason; the places of the 14 Jun letter and the 20s are listed in `holes.md`

## Prior art (checked 11-12 Nov 2026): priority not established

- The contemporary glosses: 234 of the 426 units were deciphered at the time on the letters themselves. Not ours.
- Lowell Lindgren, "Gioseffo Riva (1682-1739), a Diplomatic Arbiter of 'buon gusto' in the London of George I",
  Il Saggiatore musicale 23/2 (2016), 277-374: NOT SEEN (not open access). It uses this Starhemberg file (a letter of
  13 March 1726 is cited at p. 353, per Stefani) and treats Riva's recruiting of singers for the Royal Academy
  (pp. 300-307, 336-343, per Stefani). The Borosini passage of 14 Jun 1721 is exactly its subject and is mostly
  glossed on the page, so it is likely to be quoted there. Treat this letter as probably known until the article is read.
- Lindgren and Timms, RMA Research Chronicle 36 (2003), open copy searched through a fetch tool (first 500,000
  characters): no cipher; Borosini appears in notes on Steffani's letters of 1724, not from this letter; Starhemberg
  once, as the writer of an unprinted letter.
- This repository: `targets/selvatico1719/NOTES.md` lists the Starhemberg letters as "not worked".

## Files

`transcriptions/` (the frozen files, unchanged), `key.tsv`, `overrides.tsv`, `unglossed.tsv`, `scripts/build.py`,
`decryptions/`, `units.tsv`, `counts.txt`, `readings/`, `translations/`, `holes.md`, `timestamps/`.
