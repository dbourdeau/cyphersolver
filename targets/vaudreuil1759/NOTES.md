# Vaudreuil to the minister of the Marine, four cipher letters, Montréal 1759-1760 (catalogue 1388-1391)

Status: read in part (Brice Dudout, 4 Nov 2026): 1388, 1389 and 1390 read; 1391 read in part. Daniel's rule counts certain + probable words, not restored ones: 1388 99.6%, 1389 97.7%, 1390 99.5%, 1391 91.8% (98.6% with its restorations, which fill groups cut in the binding). All four: 4,345 cipher words, 96.7% (99.4% with restorations). Period key validated on a glossed copy.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Not yet published on the site. Text only: the
images (LAC copies of the ANOM originals on nouvelle-france.org) show no open licence and are not reproduced here.

One folder for the four catalogue entries because they share one key (one key, one entry). They are four distinct
letters; if you prefer four targets, the files are already split per document (`*_1388` ... `*_1391`).

## Documents

| Catalogue | Date | ANOM | New France Archives |
|---|---|---|---|
| 1388 | 8 Apr 1759 | COL C11A 104, ff. 54-66 | 27478 (+ view e000874967, ff. 65v-66, not listed on the record) |
| 1389 | 10 Apr 1759 | COL C11A 104, ff. 68-72 | 27479 |
| 1390 | 16 Apr 1759 | COL C11A 104, ff. 75-76 | 27482 |
| 1391 | 13 Aug 1760 | COL C11A 105, ff. 147-152 | 27665 |

Pierre de Rigaud de Vaudreuil de Cavagnial, governor general of New France, to Nicolas-René Berryer, secretary of state for
the Navy. Each letter is a duplicate ("Dupl.", "vérifié sur l'original"), wholly in cipher except heading and closing.

- **1388** (8 April 1759): Vaudreuil reports the famine (four ounces of bread a day, cattle and horses almost gone), the militia census (Quebec 6,356, Montréal 5,455, Trois-Rivières 1,313 men) and his plan for 1759: hold Carillon, the Ohio (Lignery at Fort Machault after Fort Duquesne was blown up), Niagara (Pouchot) and La Présentation, two new corvettes on Lake Ontario; he sees Cumberland's old plan revived by Amherst; Quebec will be defended after the battle at Carillon; he asks for battalions, munitions and above all food, having taken the mills' meal and the tithes.
- **1389** (10 April 1759): "For yourself alone": Montcalm's view that the colony is lost has become public, officers of the land troops speak against Vaudreuil before the people; he threatens to send the ringleaders to France, but humours Montcalm to avoid an open break and gives him the command of the army of Carillon.
- **1390** (16 April 1759): Provisions: the contractor (munitionnaire) has his correspondents in France replace any captured supply ship at once; the freight is to be paid to the King in Canada; Vaudreuil asks again for a supplement of food, without which the colony would fall of itself.
- **1391** (13 August 1760): Three weeks before the capitulation of Montréal: the ships and stores at Restigouche (Danjac) are in danger; the Machault (Lagiraudays) and the schooner l'Extravagante carry the despatches; the English are masters of the river and the lakes, about 40,000 men; Murray's propaganda among the Canadians and his circular against the bills of exchange; only ten thousand pounds of powder; "if I succumb it will be only in the last extremity"; with the Restigouche stores he could have secured a retreat.

## System and key

Numbered nomenclator 1-700: syllables, words, names, letters with homophones, ten-by-ten tables per hundred. The key is a
period table, not a reconstruction: "Chiffre avec M. le Mis de Vaudreuil ... 1757", ANOM COL C11E 10 ff. 285-290v (New France
Archives 15213, the lead given in the catalogue). It was transcribed from the deciphering table (view e001295274), checked
against the enciphering table (e001295269), and frozen as v1 before any test. `key.tsv` is v2: v1 plus 20 corrections made
while reading (e.g. 266 défen-, 56 to, 240 hi, 417 ha, 526 poste, 9 possession, 367 croi), each attested in at least two
contexts or by the 8 May gloss; nine values stay doubtful (`?`). The 1759-60 despatches use this 1757 table, not a later one.

## Validation

`validation.txt`: one pre-registered measurement on a held-out letter of 8 May 1759 whose LAC transcript copies the cipher with
its contemporary interlinear decipherment: agreement 0.972 against 0.185 for the best of 200 permuted keys (criterion >= 0.85
and >= best control + 0.30). The correction of the key afterwards never touched that measurement.

## Reading

Files per document: `transcription_<n>.txt` (groups, one manuscript line per line), `decryption_<n>.txt` (mechanical, line
for line), `reading_<n>.md` (French sentences, marked), `translation_<n>.md` (English, same marks). Count by Daniel's rule:
counted word by word on reading_<n>.md (a word with a restored part counts as restored):

| Letter | words | certain | probable | restored | unresolved | read (certain + probable) | with restored |
|---|---|---|---|---|---|---|---|
| 1388 | 2,012 | 1,965 | 38 | 6 | 3 | 99.6% | 99.9% |
| 1389 | 692 | 669 | 7 | 15 | 1 | 97.7% | 99.9% |
| 1390 | 210 | 205 | 4 | 1 | 0 | 99.5% | 100.0% |
| 1391 | 1,431 | 1,303 | 11 | 97 | 20 | **91.8%** | 98.6% |
| all | 4,345 | 4,142 | 60 | 119 | 24 | 96.7% | 99.4% |

1391 is below 95% without its restorations, so it is read in part (see Remaining gaps). In groups: 1388 about 3,670; 1389 1,220; 1390 354; 1391 2,340 + 94 cut in the binding.

## Remaining gaps

- 1388: three passages unresolved (f. 58 "j'‹équivale›", f. 60v "transport des ‹ap-se-e-ment›", f. 63v "munitions ‹ta›"); groups 64 and 59 look like encipherer's slips - blocker: illegible; re-read at x3-x4 on the NFA image, no better image in hand.
- 1389: one group cut and illegible on f. 68v ("du précis du ‹...› de mes opérations") - blocker: illegible; the group is cut and the image shows no more.
- 1391: 94 groups lost in the binding on the versos (ff. 147v-151v): the NFA image (about 1125 px) shows only their first digit; about 90 are restored from the sense (often a syllable imposed by the next line), 20 short segments (about 35 of 1,540 words) stay unresolved. Words read 91.8% without the restorations (98.6% with them, about 7% of the words): below the 95% rule, so read in part; a higher-resolution image (LAC deep zoom or ANOM IREL) would settle most of them - blocker: needs-physical-access; LAC deep zoom returned 403, the ANOM original or an IREL image is needed.
- Value 629 ("préparatif" in the table, "nous" expected once in 1391 f. 147): left as read - blocker: open-codes; one doubtful table value, the sentence reads.

## Escalation

- [x] siblings: the held-out letter of 8 May 1759 (C11A 104 ff. 79-83) and the LAC transcript reels C-2401 / C-2402 around these letters opened; the 1758 Montcalm table in C11E 10 checked as a different cipher.
- [x] clear-pages: LAC transcripts (C-2401 skips ff. 54-76; C-2402 sounded, not exhaustive) and the neighbouring despatches in clear checked for a decipherment: none found.
- [x] known-keys: the period table of the series (C11E 10, 1757) is the key; validated 0.972 vs 0.185.
- [ ] print: NOT finished. Found: NY Col. Docs X 974-975 (abstract of 10 and 16 Apr 1759). Not yet checked: Casgrain (Lévis collection), the RAPQ, ANOM F3 16 (see Prior work).
- [x] key-rebuild: 20 values of the copied table corrected in context (key v2, each attested twice or by the 8 May gloss).
- [x] retry: every doubtful digit re-read at x3-x4 and regraded; the 94 cut groups of 1391 retried from the sense with key v2.

## Prior work

Catalogue: open (no decipherment found, 28 Oct 2026). The April 1759 despatches were deciphered at the time: the "Abstract of
despatches" of 7 June 1759 (NY Col. Docs X 974-975) summarises 10 and 16 April in one or two sentences, and our 1390 agrees with
it; no full decipherment is known. The LAC transcripts of C11A (reel C-2401) skip ff. 54-76; a non-exhaustive sounding of C-2402
(vol. 105) found no deciphered copy of 13 Aug 1760. Not checked: Casgrain (Lévis collection), the RAPQ, ANOM F3 16 (the
calames row "Vaudreuil à Berryer lui annonçant en chiffres la perte de la colonie", probably a cipher copy of 1391). Web
searches on phrases of the plaintext found nothing.

## Method

Images read at x3-x4 enlargement; 1388 transcribed by one agent and finished (ff. 65v-66) by another; doubtful digits re-read
from the sense and marked {nnn} in the transcriptions. No human check against the images yet.
