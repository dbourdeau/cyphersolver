# Riva table 1721-1727: nine cipher letters to Giuseppe Riva in one syllabic table (Biblioteca Estense, Autografoteca Campori; lead 1568)

Status: read in part, contributed. No claim of a first reading (see Prior art).

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic). Issues #425, #429, #430, #432, #433;
reviewed by Daniel Bourdeau on 12 Nov 2026. This folder answers that review.

## What the documents are

Giuseppe (Gioseffo) Riva was the Duke of Modena's secretary and agent in London. His incoming letters are in Modena,
Biblioteca Estense Universitaria, Autografoteca Campori, filed by writer. Eleven letters of three writers use one number
table. Two of them carry a contemporary decipherment between the lines; nine do not, and those nine are read here.

| id | writer, place, date | leaves | units | read (strict) | issue |
|---|---|---|---|---|---|
| selvatico_1721-12-10 | Benedetto Selvatico Estense, Modena, "10 Xbre" [1721, probable] | Campori S, Selvatico Estense cc. 14-15 | 48 | 40 = 83.33% | #430 |
| selvatico_1722-01-02 | the same, Modena, "2 Genaro" [1722] | cc. 2-3 | 176 | 149 = 84.66% | #430 |
| selvatico_1722-06-10 | the same, Vienna, 10 Jun 1722 | cc. 21-22 | 150 | 128 = 85.33% | #429 |
| selvatico_1722-07-29 | the same, Vienna, 29 Jul 1722 | cc. 25-26 | 307 | 279 = 90.88% | #429 |
| selvatico_1722-08-08 | the same, Vienna, 8 Aug 1722 | cc. 35-36 | 757 | 675 = 89.17% | #429 |
| selvatico_1722-08-12 | the same, Vienna, 12 Aug 1722 | cc. 23-24 | 222 | 191 = 86.04% | #429 |
| olivazzi_1725-04-17 | Giorgio Olivazzi, Milan, 17 Apr 1725 | Campori O, Olivazzi cc. 1-2 | 377 | 278 = 73.74% | #433 |
| starhemberg_1726-03-20 | Count Starhemberg, Vienna, 20 Mar 1726 | Campori S, Starhemberg cc. 21-22 | 406 | 351 = 86.45% | #425 |
| starhemberg_1727-02-19 | his secretary, Vienna, 19 Feb 1727 | Campori S, Starhemberg cc. 23-24 | 97 | 84 = 86.60% | #432 |

Sum: 40 + 149 + 128 + 279 + 675 + 191 + 278 + 351 + 84 = 2,175 of 48 + 176 + 150 + 307 + 757 + 222 + 377 + 406 + 97 = 2,540
units (85.63%). Every letter is under the 95% bar: all nine are "read in part". Per-line sums: `counts.txt`.

The two glossed letters, which gave the key and are not read by us: Starhemberg, 27 Feb 1726 (cc. 5-8) and 6 Mar 1726
(cc. 9-10, 19-20). Images: Estense IIIF, `https://edl-jarvis.cultura.gov.it/meta/iiif/<record id>/manifest`; record ids
3e57081d-adec-4cd7-ac35-1404b389d5c9 (20 Mar 1726), c9644661-cc30-4369-bf3d-170bdc9a4a79 (27 Feb 1726),
c371348c-6a0c-4b21-ad3f-23f6f949132a (6 Mar 1726); short ids of the others as recorded in our logs: e7f7d383 (1727),
849b6bb7 (Olivazzi); the Selvatico records are those listed in `targets/selvatico1719/NOTES.md`. Images are not in git.

Writer of the Starhemberg letters: the library files them under Guido von Starhemberg. The content fits Conrad Sigmund
von Starhemberg, the Emperor's envoy in London (a household and children in London in the 1727 letter; "il mio ritorno in
Inghilterra ... con carattere d'Ambasciatore" in the letter of 31 May 1721). The reviewer accepts this; the catalogue
name is kept, with the note.

## The system

A syllabic number table with a small nomenclator. Single figures 1-8 are a e i o r s t u. A ten is a consonant alone
(10 b, 20 c, 30 d, 40 f, 50 g, 60 l, 70 m, 80 n, 90 p). A two-figure group XY with Y from 1 to 5 is consonant + a e i o u;
each row has two consonants, one for the plain group and one for the underlined group (5: g / r, 6: l / s, 7: m / t,
8: n / v, 9: p / z; rows 1-4 give b c d f either way). Underlined single figures and tens are words (1_ non, 3_ in,
4_ il, 6_ che, 7_ con, 8_ per, 10_ -ment-, 40_ stato, 70_ tutto). An x-shaped sign before a vowel group adds h (x1 ha,
x4 ho). A short stroke above a group doubles the consonant or marks an accent. Numbers of 100 and over are codes for
names, titles and common words. Doubled consonants are otherwise written once. Dates are written in clear as underlined
numerals, which is how three of them were mistaken for cipher in issue #425.

## The key and how it was obtained

- K2 (11 Nov 2026): read off the contemporary interlinear decipherment of the two glossed Starhemberg letters of 1726.
  `gloss/` has the rough group reading of c. 5r with its glosses and the ten pairs that were written down. The complete
  set of pairs was not recorded and the two glossed letters are not transcribed in full: a gap, listed below.
- K3 (12 Nov 2026, `key.tsv`): K2 with 15 rows changed or added from context in the 1722 letters, each with at least
  two contexts (8_ per, 10_ -ment-, 70_ tutto, 53 gi, 54 go, 55 gu, 60_ si, 40_ stato, the sign 01 qua, and the codes
  226 quest-, 128 corte, 162 favor, 227 quel, 142 Padrone, 261 Serenissimo), and 7 unglossed rows removed. 124 rows.
  The evidence for each row is in `timestamps/selvatico1722_4letters_partial/stamped/K3_LOG.md`.
- K3 was frozen (md5 65b083be...) before the undated Selvatico letters, the 1727 letter and the Olivazzi letter were
  transcribed. Each of those was decoded once with it, unchanged. The 20 Mar 1726 letter was transcribed before any
  key for this system existed; it was first decoded with K2 and is decoded here once with K3.
- Code values are never counted as read, including the six in the key. Proposed values are listed in `holes.md` 2.
  Two of them come from the 1726 gloss on c. 5r: 288 V.S. and 214 Olanda.

Method class: key from plaintext beside the ciphertext of sibling letters, then extended. Not a ciphertext-only break.

## Corrections to our issues (reviewer's findings and our own)

1. #425 decoded the clear dates 19, 22 (Feb.) and 6 (Marzo) as cipher and counted two of them. Right: they are dates.
   Now clear text; 406 units, not 409.
2. #425 used K2 and a fallback (10_ b, 70_ m, 30_ d) that our own parser forbids. Redone with K3, no fallback:
   351/406 = 86.45%. The 84.11% is withdrawn. The 20 units downgraded on reading are listed in `overrides.tsv`;
   every unit not read is in `units.tsv` and `holes.md`, so the figure can be recomputed.
3. The #425 reading broke down in its second half. With K3 it runs to the end (see the summary below); 8 of the 20
   downgrades are a plain group where the word needs the underlined one, or the reverse (p-gi-ma for prima, da-go for
   darò, con-mo for conto). These are probably underlines missed or added in the transcription of 11 Nov. They were
   NOT re-viewed on the image for this folder; they are counted not read.
4. "K3 = the 1726 table + 56 repairs" (issues #429, #432): 56 was the number of units of the 1722 letters whose value
   changed. The key differs in 15 rows.
5. #433 printed the reading of pass A. The reading and the English here are made on the consensus of the two passes.
6. #430: three of the 179 "units" of the 2 January letter were bracket notes split by the parser. 176 units.
7. Our own: the issue for #425 said an independent decoder agreed on 407 of 409 groups; the reviewer's count from the
   stated rules is 406. His is right for the rules as stated; ours used the fallback.
8. Our own: 100_ on 21r.L10 of the 1726 letter is also a numeral in clear ("le 100 L. St."). It was never counted
   read (it is treated as a code) and is left as a unit, marked.

## What the letters say

- 10 Dec [1721]: Selvatico, from Modena, does not believe the Congress will be held and disowns Rangoni's mission to
  Paris; in cipher, someone will soon go on to Paris or to a coded place, and orders will follow from the Duke.
- 2 Jan [1722]: the Princes of Modena and Cardinal de Rohan have come from Rome; the Cardinal, laid up with gout at
  Reggio, is about to leave for France; the Duke means to post a coded person elsewhere. The Gaceta de Madrid of
  3 Feb 1722 reports the same journey, which gives the year.
- 10 Jun to 12 Aug 1722: Selvatico, now in Vienna, on Modena's claim to an indemnity for war damage, to be raised at
  the congress (Cambrai). He asks whether George I has been won for it. On 8 August the ministers in Vienna, pressed,
  admit that the Emperor will never promote the claim and would rather it were not raised, because the other side
  would then reopen other points, Mirandola among them (spelt out twice); he will support it only if the Duke or
  another power moves first. On 12 August: news of a move to have a coded place restored "to Pico"; the Emperor will
  not propose the indemnity "per non svegliare li cani che dormono" (so as not to wake sleeping dogs); this court is
  not to be trusted much.
- 17 Apr 1725: Olivazzi, in Milan, on the party working against him (the payments at issue are the excuse, the aim is
  to keep him in bad repute and from advancement; the Inquisition was used), and on three interests of the Duke, one
  of which involves a proposal "to send an Archduchess". The least secure of the nine: many coded persons.
- 20 Mar 1726: Starhemberg thanks Riva for three letters, says most of the news reached him first from others, and
  asks him to report punctually on the court and on general affairs. A yearly 100 pounds sterling is in question;
  Riva and "the friend in [Holland]" may count on at least a couple of hundred in fees between them this year, some of
  it from Starhemberg's own pocket, and for news of consequence on rewards and an Imperial favour. The Duke will find
  his account in it if he and his ministers stay "good Imperials". The middle of this letter has holes; the terms of
  the 100 pounds are not secure.
- 19 Feb 1727: French clear text about a baron's courtship as cover; the cipher begins where the lady's name should
  stand: "all of this so far is feigned"; Riva is to watch closely what passes with Palm (the Emperor's resident in
  London, expelled the next month) and what measures the British court takes.

Full Italian with holes in place: `readings/`. English: `translations/`.

## Checks

- Shuffled-key controls, 5,000 keys, Italian quadgrams (our own scripts, 11-12 Nov 2026; outputs in `timestamps/`): the
  four 1722 letters 0 of 5,000; the two undated letters together 0 of 5,000 (the 10 Dec letter alone 44 of 5,000:
  43 keyed units, too short alone); 1727 0 of 5,000; Olivazzi consensus and pass B 0 of 5,000; 20 Mar 1726 under K3 in
  the old notation 0 of 5,000 (not re-run after the date fix). The reviewer reports his own 0 of 5,000 on the filings.
- Second transcriptions: 1722 letters, a blind second transcription by a separate session (frozen before any key or
  first transcription was opened): 1,390 of 1,441 aligned groups the same (96.46%); 33 disagreements adjudicated,
  first transcription right or probably right in 29, unclear 1, blind right 3 (tick marks only). Olivazzi: pass B blind,
  349 of 379 groups the same as pass A (92.08%); 27 places adjudicated on crops (14 for A, 11 for B, 2 neither);
  that adjudication was key-aware. No second transcription: 20 Mar 1726, 19 Feb 1727, the two undated letters (for
  those two, another contributor's passes in `targets/selvatico1719/work/` agree at 159/176 and 45/48 groups).
- The reviewer's spot check of 87 groups of the 1726 letter against the image: 87 of 87, one accent tick missed.
- The repository's checker scripts were not run by us (we treat downloaded repositories as data). The checks they make
  were verified by reading them; see the pull request text.

## Remaining gaps

- Codes: 201 units, 74 different numbers; none is counted read - blocker: open-codes; `holes.md` 2 lists each with the proposed value, if any (only 288 V.S. and 214 Olanda have a gloss of the time)
- 8 plain/underlined conflicts in the 20 Mar 1726 letter, and the words "n-ma-na-r-la" (21r.L11), "di centena da" (21v.L01), "su fi" (21v.L09) - blocker: illegible; whether a stroke runs under a group is not settled on the 1,400-px images; the full-resolution crops were not re-viewed for this folder
- row 5 of the table: plain 51/52 (ra/ga? re/ge?) against plain 53/54/55 = g (K3); 5_ (chi), 30_ (esser), 50_, 0_, 9_, 9 - blocker: no-key-material; the gloss pairs recorded (`gloss/gloss_pairs.tsv`, 10 pairs) do not decide them; "ingegnarsi", "diligente" and "regenti" need plain 52 = ge
- the K2 rows read off the two glossed letters of 1726 (27 Feb, 6 Mar) - blocker: no-key-material; only 10 gloss pairs and a rough group reading of c. 5r were written down, and the two letters are not transcribed in full, so K2 itself cannot be re-derived from the files (the pair behind 8_ = E, replaced by PER in K3, is not among the ten)
- Olivazzi 17 Apr 1725: four stretches not read, the right edge of 2v under the facing leaf; 2v is decoded, not read - blocker: illegible
- Lindgren 2016 (Il Saggiatore musicale 23/2) not seen - blocker: needs-physical-access; sold by the publisher's platform, needs a library copy; the Modena-side records (Archivio di Stato, cifrari) are the other place a key may survive
- Other Riva correspondents: 398 of 535 further records viewed in full, no other letter in this table; 111 not checked - blocker: needs-physical-access; records not reachable from here

## Further work (outside this target's texts)

- Clear text of all letters: one reader (the model), abridged in places.
- Transcriptions against the images: apart from the contributor's own two passes and blind second transcriptions, the
  checks are by AI readers only (the 12 Nov reviewer: 87 of 87 groups of 20 Mar 1726; the integration check below: all 104
  groups of the 31 May 1721 letter in `targets/starhemberg1721` and all 97 groups of 19 Feb 1727). No person has compared them.

## Integration check (12 Nov 2026)

What was checked, from the files, before the page was written (full report in the integrator's verification notes):

- `scripts/build.py` rerun on a copy: every count in the table above reproduces (2,175 of 2,540; per letter as listed);
  `units.tsv` and `decryptions/` regenerate identically. `counts.txt` as filed lacked the reconciliation block that
  `build.py` appends from `counts_notes.txt`; regenerated.
- A second decoder written from `key.tsv` and the transcriptions alone: 19 Feb 1727 97 of 97 groups, 20 Mar 1726 406 of 406
  (the other letters, the same except for marks of illegibility).
- Timestamps: the RFC 3161 replies (Sectigo) of 11 Nov 2026 were read: 20 Mar 1726 pass 21:08 GMT, K3 21:30, blind second
  transcription 21:43, undated letters 21:55, 1727 22:04, Olivazzi 22:13 and 22:25. The SHA-256 of every stamped file that is
  in the repository equals its manifest line (one file, the log, changed afterwards, as declared); md5 of `KEY_K3.tsv` is
  65b083be69e3a4c6219c65566aee20fc as stated. So the order K3, then the 1727 and Olivazzi letters, is shown by the stamps;
  what they cannot show is that no one looked at those letters earlier.
- Not held out: the 15 K3 rows were made on the four 1722 letters, so their 88.65% is in-sample; 90 of the 2,175 read units
  use a row that K3 changed (2 to 30 per letter). Held out from K3: 20 Mar 1726, 19 Feb 1727, Olivazzi, the two undated letters.
- Counting: the figures count cipher units (a syllable or a word sign), the strict rule of this folder. A word with one open
  syllable still counts its other syllables as read. A rough count by words (the words inside the asterisks of
  `readings/`, a word with any bracket or `?` as open) gives about 74% for the nine letters, 60% for Olivazzi: an estimate
  made at integration, not a measurement. Neither figure is near the 95% bar.
- Images: 19 Feb 1727 c. 23r, all 97 groups and the underlines agree with the transcription on the 1,400-px image.
- Keys: K3 applied to the 31 May 1721 letter gives no language (`lm.best_language`), K21 gives Italian: the Starhemberg
  letters of 1720-21 are another key and are in `targets/starhemberg1721`. K21 is related to the 1719 table of
  `targets/selvatico1719` (b c d f g at 11-15, n at 18, q at 20) but r s t z and the vowel rows differ.
- `selvatico1719` lists the 1722 and undated Selvatico letters and the Starhemberg letters as not solved or not worked: they are here.

## Escalation

- [x] siblings: the Estense file for Starhemberg, Selvatico and Olivazzi viewed; the two glossed 1726 letters are the key source; 398 of 535 further Riva records viewed, no other letter in this table
- [x] clear-pages: no clear copy of any of the nine letters; the dates written in clear inside the cipher lines of 20 Mar 1726 taken out of the cipher
- [x] known-keys: the 1719 table of `selvatico1719` (its contributor found that it does not read the 1722 letters); K21 of `starhemberg1721` and K3 tried on each other's letters: neither fits
- [x] print: Lindgren and Timms 2003 and Stefani searched in open copies (no cipher); Lindgren 2016 not seen (paywalled), recorded as a gap
- [x] key-rebuild: K2 rebuilt to K3 from context in the 1722 letters (15 rows), 7 unglossed rows dropped; remaining values proposed in `holes.md` 2 and not counted
- [x] retry: every unit not read is listed in `units.tsv` with its reason; the underline conflicts of 20 Mar 1726 left for the full-resolution images (gap above)

## Prior art (checked 11-12 Nov 2026): priority not established

- Lowell Lindgren, "Gioseffo Riva (1682-1739), a Diplomatic Arbiter of 'buon gusto' in the London of George I",
  Il Saggiatore musicale 23/2 (2016), pp. 277-374. NOT SEEN: sold by the publisher's platform, not open; the journal's
  site and the publisher's page give the title only; a library search site refused automated access and that was not
  worked around. What is known at second hand (Stefani, "Un diplomatico a Vienna", notes 7 and 30): the article maps
  Riva's correspondence (pp. 368-373) and cites a letter of Count Starhemberg to Riva of 13 March 1726 (p. 353). So
  Lindgren used the Starhemberg file. Whether he prints or deciphers any cipher passage is not known to us. Until
  someone reads the article, every letter here is at risk of an earlier reading, the Starhemberg letters most.
- Lindgren and Timms, "The Correspondence of Agostino Steffani and Giuseppe Riva, 1720-1728", RMA Research Chronicle
  36 (2003): an open copy was searched through a fetch tool in five blocks (first 500,000 characters): no cipher, no
  Selvatico, no Olivazzi, no Mirandola; Starhemberg once, as the writer of a letter in another folder, not printed.
- Stefani, "Un diplomatico a Vienna" (Riva 1729-37): no cipher, no Selvatico or Olivazzi in the 200,000 characters read.
- This repository: `targets/selvatico1719` (another contributor) reads the 1719 table and records the 1722 letters as
  "not solved" and the Starhemberg letters as "not worked". `targets/palm1727` names Conrad Sigmund von Starhemberg.
- The two glossed 1726 letters were deciphered at the time, by the recipient's side. The nine here carry no gloss.
- Not checked: Modena-side records (Archivio di Stato di Modena, Cancelleria ducale, ambasciatori; the cifrari), where
  a key or decipherments may survive.

## Files

- `transcriptions/`: one file per letter, the lines of the frozen transcriptions unchanged (20 Mar 1726: notation v2,
  the three dates moved into clear text; the frozen pass is in `timestamps/riva1722_1726/stamped/`).
- `key.tsv`; `gloss/`; `overrides.tsv` (94 rows, downgrades only; 93 units change mark, one was already not read); `scripts/build.py` (standard library).
- `decryptions/`: line by line against the transcription. `units.tsv`: every unit with its mark. `counts.txt`.
- `readings/`, `translations/`, `holes.md`.
- `timestamps/`: seven stamps of 11 Nov 2026 with the stamped files, second transcriptions among them.
