# alfonso1576: Alfonso II d'Este to the protonotary at Venice, 14 Apr 1576 (catalogue 1566)

Status: in progress. Not yet written up: no site page or README row. Classed read (narrowly), so it is ready for the /writeup skill. The status below is the contributor's.

Status: read (3 Nov 2026), by a narrow margin. Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera E, Este (d'), Alfonso II d'Este, duca di Ferrara, cc. 76-77.

Catalogue 1566 holds three letters in three systems. One key, one entry: this folder has the 1576 letter, and `targets/ercole1559` has the 1559 letter to Bentivoglio and the note on Ariosto's c. 1.

Transcription and reading were done by AI language-model agents viewing the images. No human palaeographer has checked them. An independent AI verifier checked the first version; its report is `VERIFY.md`, unchanged, and it covers both folders. This version applies its must-fix list. No independent check has been run on this final version.

| Signs | Job | Words | Reading as sense | No restored or changed letter | Status |
|---|---|---|---|---|---|
| 3,703 | ciphertext-only break; no decipherment on the leaf | 740 | 737 (99.6%) | 706 (95.4%) | read, three words above the bar of 703 |

Words are counted in the cipher only, with elided forms split. "No restored or changed letter" excludes every word with a `<x>`, `{x}` or `[?x]` mark. "Reads as sense" counts every word but the three wholly doubtful ones. `python scripts/check_marks.py 76` makes the count, and fails on any letter that departs from the decryption without a mark.

"Read" is a narrow call. The first hand alone gives 535 of 557 (96.1%), the second hand and postscript 171 of 183 (93.4%). If you want a margin of more than three words, mark the letter read in part.

## System

Simple substitution of Italian, with nulls. No word breaks, no code groups. See `key_1576.tsv`.

- 20 letters. The sign alphabet is Latin letter forms in a secretary hand, so the cipher reads like nonsense Latin script.
- Nulls: x, y, k, each used freely, often in pairs. & and 3 occur once each. x often sits between two identical signs, which hides doubled letters.
- The digit 7 stands for itself, once ("lettera vostra di 7").
- Two hands. The first runs to c. 77r l. 6: nulls 8.4% of signs. The second takes over at c. 77r l. 7 and does the postscript: nulls 1.2%, and it drops or shortens letters. Some signs there have a stroke above; these were not recorded (see open points).
- The table runs in blocks: a-d go to z u t s; e-h go to a b c d; q-t go to e f g h.

## Two q-forms: g = s, q = m

The first version said the hand writes one shape for cipher q and cipher g. That was wrong. The hand writes two signs:

- **Looped tail.** The descender sweeps left and back up in a large oval: cipher g = **s**.
- **Straight tail with a short foot:** cipher q = **m**.

Both are ordinary italic letter forms, and the split fits the block pattern of the table. The transcription, key and decryption now keep them apart, and no value in the decryption is chosen by sense.

All 339 signs were read by tail on enlarged crops, in order, one mark per sign, and saved in `q_tails.tsv` before any comparison with the values given by sense. To place the crops, each line of signs was aligned to the image by `scripts/align_signs.py`, which uses no language. 331 tails were marked at once; 8 needed a larger crop and were settled there.

| | count |
|---|---|
| looped, g = s | 227 |
| foot, q = m | 112 |
| tail agrees with the value sense had given | 338 of 339 |
| conflict | 1, c. 77r l. 9, first sign of "mostrare": a clear loop, so the signs give "sotrare". Listed in the reading |

Limits. This reader had read the decryption, and the crops carried the neighbouring signs as a label, so the reading of tails was not language-blind. The independent sealed test in `VERIFY.md` section 2 (37 of 37 on lines it chose, 17 of 17 on others) is the stronger evidence for the split, and it covers 54 signs. A simple machine feature on ink below the line gave AUC 0.58 (shuffled labels up to 0.61): the loops of neighbouring signs fall in the same box, so it is no check in either direction. The older tests with 61%, AUC 0.62 and AUC 0.47 are withdrawn: their crops did not sit on the q-forms, 4-6 signs off in the cases the verifier traced.

The merger also explains an oddity in the break: with q and g merged, the annealer had to put m somewhere, and gave it to the null y in both halves.

## How the key was obtained

Ciphertext-only. Quadgram annealing on a corpus of period Italian (Ariosto's letters, plus the 1630 readings of target 1567), 10 restarts, no crib. Eight of the ten runs landed on one solution, and the output read as Italian at once, apart from the nulls. The first working text had the nulls as letters, which told us which signs to drop.

## Held-out test

c. 76r alone (1,241 signs) was broken separately, and the rest (2,448 signs) separately, with no shared information in the code.

**This hold-out was not set up in advance.** The whole-text key dates from 21 minutes before the split. The machine check is valid. It is not a preregistered test, and whoever ran it already knew the key. The sign counts here are those of the merged first version.

- 21 signs are assigned by both breaks. 18 agree with each other, but two of those (y=m and q=s) are effects of the merged q-form: y is a null in the final key, and q=s is only half true. 16 of the 18 match the final table. The three that differ are null x, null k and b.
- Key frozen from c. 76r, applied to the rest, gives `guardoaquel...locheluisedmesisocihadetto...`. Italian at once.
- Mean quadgram score per position: real key -10.17; 200 shuffled tables, mean -15.01, best -13.38. Reproduced by the verifier with a model from Ariosto's letters only: -10.18; 500 shuffled tables, best -13.56.

## Transcription

Pass 1: straightened half-lines, read and written down before any value was known, so blind to language. One sign changed after the break without a log entry at the time: c. 76r l. 2 pos. 6, z to 7, now logged; the verifier confirms the 7. Pass 2 was not blind. The reading was walked against the signs by alignment, each of the 50 positioned disagreements viewed on a crop, and 14 signs changed. Pass 3 is the one above: q and g split, and at c. 76r l. 2 a sign read f (no bar, but f's descender and foot) where l stood, and the tall sign squeezed between a and o read as B, which gives "et il sospetto", the letter's usual spelling. The two insertions above the line now stand in the sign text at their carets, so the count is 3,703 and not 3,689.

Independent blind check: 287 signs (c. 76r ll. 1-3, c. 77r ll. 4, 10), q and g merged; 6 raw disagreements (2.1%). After settling on crops, the transcription was wrong at 2 (0.7%), the verifier at 4. This sample cannot speak for the rest.

## Departures

"11 r written without the bar" was inexact. The clerk wrote the plain tall l, stopping at the baseline, where sense wants r. Of 9 sites the verifier viewed, 8 are of this kind; the ninth is the f above. So the bar is not lost; the sign is a different one, a slip or a second value. All are listed in the reading. The silent changes the verifier found (ben, sommamente, per, and marks on the wrong letter at nostri and inquisitione) are corrected, so the text now prints the signs: bene, somamente, nostr`<i>`, inqu`<i>`sitione, pe`<r>`.

## Reading

Alfonso tells his agent, a protonotary, how to handle an unnamed man (*incognito*) who fears stricter proceedings against him. The man is to be told that nothing from Ferrara can harm him, that he was never in Este pay, only rewarded at times, and that Ferrara's interest in news of "those lords" was friendly. If he came to Ferrara he would have to be handed over under the conventions with "that Dominion", all the more for a crime of *lese maestatis*. The duke privately believes the story is invented, and the man is more likely hiding from debts. He is someone "to take from what one can, but not to open oneself to". The agent is to find out quietly whether any inquiry exists, to give the man fifty scudi, and to learn from Tassone what was promised him. The second hand turns to oils and almonds, Doctor Panino sent by the merchants, a Roman complaint, and in the postscript the prisoners of Rovigo, whose status as Este subjects has been proved. Clear note: Montecatino will write about Albano.

The recipient is at Venice. A note at the foot of c. 77r, in a later hand, reads *A Monsig.r Ariosti Ambasciatore / Venezia*. That is later testimony, not the writer's, but it stands on the leaf and agrees with the catalogue. The text points the same way: "dominio", "signori", *lese maestatis*, Rovigo, plague deputies, and a docket that reads *Inquisitori* in our first reading. The plague of 1575-77 would fit, from general knowledge. A British Library record has Claudio Ariosto as Ferrarese ambassador at Venice in 1592 (https://searcharchives.bl.uk/catalog/032-002021330). If the reading holds, the letter shows the duke disowning a paid informant inside Venetian territory. A historian should check all this.

## Prior art and collision (2-3 Nov 2026): open

- Collision: rechecked at upstream head 3c777efd5, and on 3 Nov against the open pull requests and head d06538173. No target folder, no commit, no pull request for this letter.
- Web searches on Claudio Ariosto and Alfonso II 1576 found no edition or decipherment. Search results do not settle that.
- The key-bearing archive is unopened: ASMo, Cancelleria ducale, Cifrario, 8 buste (https://www.filodiritto.com/la-parola-incognita-cifre-e-cifrari-alla-corte-estense). So is the ASMo ambassadors' series, where a minute or Ariosto's replies for April 1576 may stand. We do not claim that the reading is new. We say only that no decipherment stands on the leaf and that we found none.
- The docket of c. 77v shows that the letter was read in its own day, as one would expect.

## Remaining gaps

- [?puntino]; "a [?ti]", where sense wants the Pope; [?gagliarde], whose first sign and b are not explained; "cha", read as a dialect che - blocker: too-short; each occurs once or twice.
- The docket of c. 77v - blocker: illegible; partly lost in the fold.
- Prior art: ASMo Cifrario and ambassadors' series - blocker: needs-physical-access.

## Open checks

These are checks not done, not unread pieces of the cipher, so they do not stand as gaps above. They bear on the narrow "read": if you count them against the bar, the letter is read in part.

- Second-hand strokes above signs: not recorded sign by sign. If they mark doubling, spellings such as *fato* and *Quato* change, and the departures table shrinks.
- No fresh key-free copy of the whole text: 287 signs had a blind second reader. The q/g reads rest on one reader who knew the text, plus the verifier's sealed 54.
- The end of the clear text and the signature are a first reading from images.

## Escalation

Third pass: all q-forms read by tail, c. 76r l. 2 corrected, marks rebuilt and enforced by script.

## Image sources (links only; no scans in git; licence CC BY-NC-SA)

Lodovico IIIF manifest `https://edl-jarvis.cultura.gov.it/meta/iiif/898fdfe5-96b1-4b6f-bdc2-a71cd72af1f6/manifest`.

## Files

`transcription_cc76-77_1576-04-14.txt`, `decryption_cc76-77_1576-04-14.txt`, `reading_cc76-77_1576-04-14.md` (Italian with English, sentence by sentence), `key_1576.tsv`, `q_tails.tsv`, `sign_changes_cc76-77.tsv`; `VERIFY.md`, the independent report, unchanged; `scripts/`.

`python scripts/check_decryption.py` reruns the key over the transcription. `python scripts/check_marks.py 76` counts the words and enforces the marks. Both need only the standard library. The other scripts need the images and are there as a record of the method; they use a `scans/` and a `work/` folder that are not in the repository.
