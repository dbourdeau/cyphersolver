# Isabella to the Duke of Estrada, Segovia 20 Aug 1503 (catalogue 287)

Status: read in part (22 Sept 2026). The cipher is Galende's *Cifra general de los Reyes Católicos*; the letter
survives in three ciphered copies on PARES and its content is read in outline; about half the letter-sign runs stay
unread at the resolution PARES serves.

## The target

Catalogue 287: "Isabella of Castile to the Duke of Estrada", AGS Estado, Tratados con Inglaterra leg. 4 ff. 65-67
(S.E.T.c.I. L. 4). Bergenroth, CSP Spain i no. 369 (p. 309): *"A despatch in two keys of cipher, which I have not
succeeded in deciphering. It is dated Segovia, 20th August 1503. Addressed: 'To Ferdinand the Duke.' Indorsed: 'I
received it in Richmond on the 20th of January 1504.' pp. 5, in cipher."* In his preface (p. xii) he calls it the one
cipher he could not break. Tomokiyo (cryptiana, *Spanish ciphers … Ferdinand and Isabella*) suggests trying the
Galende general cipher and separately notes that PTR leg. 53 doc. 69, an undated 1503 Isabella letter, is in that
cipher and not in Estrada's usual one.

## Where it is now

The Tratados con Inglaterra legajos were merged into **AGS Patronato Real, Capitulaciones con Inglaterra, leg. 53**.
The catalogue's "not Patronato Real" is wrong. PARES ids 2207985-2207991 are PTR 53/66-72:

| PARES | shelfmark | PARES date | what the images hold |
|---|---|---|---|
| 2207985 | PTR 53/66 | 1503-04-12 | 42 images (the 12 Apr 1503 letter and following) |
| 2207986 | PTR 53/67 | 1503-05-04 | 6 images |
| 2207987 | PTR 53/68 | 1502-07-18 | 4 images |
| **2207988** | **PTR 53/69** | "1503" | **8 images: three ciphered copies of this letter (X, Y, Z) and their dorses** |
| 2207989 | PTR 53/70 | 1503-09-24 | 8 images |
| 2207990 | PTR 53/71 | 1503-10-03 | 16 images: the 3 Oct Roussillon letter in Estrada's cipher |
| 2207991 | PTR 53/72 | 1503-10-03 | 24 images: the same, plus Bergenroth-era clear copy (pencil ff. 346-349) |

PTR 53/69, images (dbCode 12534514; each record must be opened with `catalogo/show/<id>` in the same cookie session
before `ViewImage.do`, or PARES serves the previous record's images):

* images 1-2, pencil f. 322r-v, **copy X**: 46 + 11 lines, closing "en madri[d]? a [..] de setiembre", then Estrada's
  endorsement of receipt (below).
* images 3-4, pencil f. 323r-v, **copy Y**: 47 + 10 lines, closing **"en Segovia a xx de agosto de diii"**; the
  endorsement on the dorse carries Bergenroth's-era reference "Leg. 4 f. 65 y 66". This is Bergenroth's no. 369.
* images 5-6: dorses (address leaves) with archival marks "T.c.Y.4" and 19th-century pencil notes; no cipher.
* images 7-8, **copy Z** (marked "T.c.Y.4", "PR 53-69"): closing **"en Segovia a tres de otubre de diii"**; at the
  foot of the recto Estrada's endorsement of receipt (below).

So PTR 53/69 is Bergenroth's L. 4 ff. 65-69, and the endorsements identify the leaves:

| copy | closing | endorsement (Estrada's hand) | Bergenroth |
|---|---|---|---|
| Y | "en Segovia a xx de agosto de diii" | dorse "Leg. 4 f. 65" | **no. 369** (ff. 65-67), "not succeeded in deciphering" |
| X | "en madri[d]? a [..] de setiembre" | "…dia de todos santos del suso dicho año en la casa de Dur[ham] … Martin Sanches de … [nao] Jorja" | **no. 380** (f. 68): "Received at Durham House on the day of All Saints … It came in the ship 'George'" |
| Z | "en Segovia a tres de otubre de diii" | "en la casa de Durã[m] a ocho de março de diiii. Recebida de uno de Salusbery" | **no. 381** (f. 69): "Received at Durham House on the 8th of March 1504, by a messenger from Salisbury" |

The three copies open with the same words and carry the same text line for line (different line breaks). X and
Z are the duplicates of the August letter that the monarchs kept sending: Isabella's letter of 3 Oct (no. 385,
L. 4 f. 70 = PTR 53/71-72, Estrada's cipher, deciphered by Bergenroth) says *"In case you may not have received
[our letters of 20 August], I have ordered that the duplicate of it should be sent to you along with this
letter"*. Z is that duplicate, dated the same day.

**Bergenroth mis-filed X and Z.** He calendared no. 380 (f. 68) as Isabella's 3 Oct letter on the marriage treaty
and its ratification, "deciphered by the editor", and no. 381 (f. 69) as "the same despatch"; nos. 382-384
(ff. 74, 75, 77) are further copies. But ff. 68 and 69 carry the Galende-cipher text of the August letter, not the
ratification letter: he evidently deciphered the ratification letter from the Estrada-cipher copies and gave
ff. 68-69 the same summary because they carry the same date and endorsement style. So the letter he could not
read (no. 369) is also what stands on the leaves of nos. 380 and 381. This probably explains the catalogue's
"why" (the marriage) too. It also means catalogue **288** ("Isabella to Estrada, [3 Oct] 1503, PTR 53/69",
closed in SOLVED_CATALOGUE as deciphered by Bergenroth, CSP 385) is this same letter, copy Z. CSP 385 is PTR
53/71-72, not 53/69.

## The key

Galende Díaz 1994, app. doc. 1 (`esp318/keys/cifra_general.txt`, 683 groups): the *Cifra general de los Reyes
Católicos*, homophonic sign alphabet + two-to-four letter code groups with initials v-, x-, y-, z-, b-, c-. It fits
at once: the first line of all three copies reads **`cog` Ya SABEYS [co]MO `xix` el `bof` rey de Francia `zok` nos
RONPIO `yiz` los DIAS PASSADOS `yaz` la `yui` guerra `xuy` en `zin` Napoles**. Every code group met so far takes a
value that fits its context (about 480 group tokens; `zer`, `zeg`, `boe`/`bue` twice each are the only ones read
with doubt). Bergenroth's "two keys" is the code/letter mixture; nothing in the text needs a second key.

Two writing habits: the v- codes are written with a b-like v (`vib` Aragon, `vud` agora, `vek` aquello, `vil`
ayuda), and code-final *z* is written like a 3 (`yiz`, `yaz`, `zez`, `ziz`, `biz`).

## What the letter says

(Reading in `reading_X.md`, copy X's line numbers.) The King of France broke the peace in Naples without cause,
though "we gave him all the justification in the world, seeking every means" to avoid war; not content with that,
he has now sent all his power by sea and land to the frontiers, most of it to Roussillon and the rest to the
Fuenterrabía frontier, and has already opened war in Aragon, in Guipúzcoa, and in Galicia with a fleet. "The flower
of the people of France" and the greatest army he could raise are gathered in Languedoc to enter Roussillon. Lines 19-26
turn to the Spanish response (grandees, troops, the Navarre frontier), too broken to paraphrase. The King of England "our
brother is bound, by virtue of [the treaties] between us and him, to help us defend what is ours"; so far they have
not wished to press him to declare himself until the French actually entered their kingdoms, "and now only" — the
verso — Estrada is to ask for **two thousand English foot (`xik zod` PEONES, three times)**, with ships, and to send
the answer. This is the letter that the 3 Oct letter (PTR 53/72, clear copy f. 346) summarises: *"Por otras nuestras
cartas de veinte de agosto … habreis visto como el Rey de Francia habia comenzado a nos romper la guerra … y como
por entonces no queriamos afrontar al Rey de Inglaterra nuestro hermano a que se declarase por nos … hasta ver que
los franceses entraban en nuestros reynos"*, and whose request for "dos mil peones ingleses escogidos" it repeats.
The marriage of Catherine and Henry is not the subject of this letter.

## Remaining gaps

- Letter-sign runs, about half of the cipher tokens of each copy (154 [..] stretches in reading_X.md) - blocker: illegible; PARES serves only 988x1310 px, a sign is 8-10 px high and the alphabet has several homophones per letter; three copies collated; needs the AGS originals or a high-resolution reproduction from Simancas
- X's day of the month and place ("en madri[d]?") and a few words of its endorsement - blocker: illegible; small cursive at 988 px

## Escalation

- [x] siblings: PTR 53/66-72 all opened; 53/69 holds three copies of the one letter (collated), 53/72 holds the
  clear copy of the 3 Oct letter that summarises it (used as a crib for sense and vocabulary).
- [x] clear-pages: no decipherment of the Galende-cipher letter on any image of 53/66-72; the clear copy on
  53/72 ff. 346-349 is of the 3 Oct Estrada-cipher letter only.
- [x] known-keys: Galende's Cifra general fits (every code group consistent); Tomokiyo's "Estrada cipher" (cab, cev,
  gam, gep … raf, ru) does not occur.
- [x] print: CSP Spain i 369 (unread), Tomokiyo spanish.htm (no reading), Galende 1994 (key only); no edition found.
- [n/a] key-rebuild: the key is complete in print; the open runs are unread signs, not unknown values.
- [x] retry (image enhancement, 22 Sept): every PARES route re-tested (zoom 10/20/100, print view, quality flags): max 997x1396, no IIIF or tiles. Strips at 4-6x with unsharp masking, read against Galende's plate (p. 167) of sign forms: adds isolated words (l. 12 *cud* una, l. 13 *tal resistencia … en ninguna dellas*) but the open runs stay ambiguous between two or three sign forms. A reading past ~50% is not possible from these images; the push to 95% is closed as impossible until Simancas supplies high-resolution photographs.
- [x] retry: X was read with Y (all 47 lines) and Z (first lines and closing) beside it; runs that read in one copy
  were carried over. A further sign-by-sign pass at this resolution would add little; better images are the step.

## Files

* `reading_X.md` — the reading, line by line, codes with values, [..] for unread runs.
* `work_Y.md` — first working transcription of copy Y lines 1-10 (sign notation).
* `img69/`, `img71/`, `img72/` … — PARES images (git-ignored), `lines/` line strips (git-ignored).
* `strips.py`, `halves.py`, `stack.py`, `zoom.py`, `contact.py` — image cutting helpers.
