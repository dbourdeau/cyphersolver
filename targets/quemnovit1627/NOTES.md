# "Quem novit": a cipher letter to Christian IV, 20 July [1627 or 1628] (Rigsarkivet, TKUA Nederlandene B.41; with catalogue 2541)

Status: **code broken, read in part**, contributed. Issue #450.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic). This folder answers Daniel Bourdeau's
note on #450 ("Checked, and held ... A pull request with the frozen transcription, dec_B.py, the key file, the two
blind transcriptions with their alignment, a corrected read-share statement and the RFC 3161 token would let us write it up").

## Read share (corrected)

**70 of the letter's 103 cipher units (67.96%) read as German words when each sign takes the value that at least two
of the three independent readers give.** Arithmetic: S 70 + E 21 + N 12 = 103; 70/103 = 67.96%. The other 33 are
3 code numbers, 7 one-sign slips that reader 1 emended, and 23 units with a sign the readers dispute (13 of them the
g/q class alone). If all three readers must agree on every sign, 47/103 = 45.63%.

The adjudicated transcription and its labelling rule were frozen (md5 in `transcriptions/ADJUDICATION_FROZEN.md5`,
13:17:09 UTC 12 Nov 2026) before it was decoded, once, at 13:17:19 UTC (`checks/adjudicated_decode_once.out`).

This sits beside the three readers' own figures and does not replace them:

| Reader | Transcription | Strict S/(S+E+N) | Shuffled keys as good (5,000; seeds 20261112 / 7) |
|---|---|---|---|
| 1, the breaker (b97) | frozen 02:18:36 UTC, md5 836d644f | 93/103 = 90.29% (**filed, withdrawn as the headline**) | 0 / 0 |
| 2, blind (b129) | frozen 09:49:43 UTC, md5 de87c01d | 62/104 = 59.62% | 0 / 0 |
| 3, blind (b137) | frozen 11:22:40 UTC, md5 6d642c8b | 49/110 = 44.55% | 0 / 0 |
| adjudicated, majority of 3 | frozen 13:17:09 UTC, md5 ec0c2427 | 70/103 = 67.96% | 0 / 0 |

Why 90.29% is withdrawn: it was one reader's count, and that reader built the key while transcribing. Two blind readers
did not reproduce it. The key itself is confirmed: all three independent transcriptions decode to German under it, far
beyond any shuffled key (counts.txt, D).

## What the document is

One page (image 443, right page), 19 lines, filed in the folder of Johann Schultetus's reports from The Hague, 1628-29
(catalogue 2541), but not in Schultetus's hand. About 100 cipher words written among clear German, three code numbers
(117 twice, 118), dated "den 20 Iulii anno currentis" and signed "Quem novit" ("whom you know") in place of a name.
Addressed to the King as "Gnädigster König" (Christian IV). Image: https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=19852699#261377,48900927

Writer: **proposed, not proved.** One article (Bohemiae Occidentalis Historica 2/2019, read through a summariser only)
puts Christian Wilhelm of Brandenburg, Administrator of Magdeburg, in Venice in early July 1627 on his way to lead
Danish forces in Silesia. A three-week wait for a galley on 20 July fits; then the date would be 20 July 1627 (Old
Style). Not tested against any dated source. The filing order (between papers of September 1628 and Schultetus's letter
after 24 July 1628) points to 1628 instead.

## The system and the key

Simple substitution, word by word, among clear German: 23 signs with a value for 21 plain letters (s and k each have two
signs; i stands for i, u and v); one sign (n, once) without a value. `key.tsv` (with shapes and counts) and `key_B.txt`
(the file the decoder reads; byte-identical to the stamped key, md5 224da5d5). Code numbers 117 and 118 are not solved.

How the key was found: the clear text continues "... lasset E. unverhalten sein", so the first two cipher words were
taken as "Gnadigster Konig"; the rest followed from word patterns, by hand. No solver. Disclosure: the letter values took
shape while reader 1 transcribed, so his "frozen before decoding" means before any scripted decode, not before any guess.

## What the letter says

See `readings/reading_de.md` and `readings/translation_en.md` (holes marked in place). In short: H. has waited at [118]
into a third week for a galley; nobody, [117] least of all, would advise the small ones; the Signoria has assigned a
large one and he leaves today. He has borrowed another 3,000 thalers and asks the King to pay and deduct them later.
[117] has resolved nothing on his proposal; he hopes W. will declare themselves better.

## Checks (all scripts stdlib Python, run as `python3 -I`; outputs in `checks/` and `alignment/`)

- `scripts/dec_B.py` (reader 1's decoder, unchanged, stamped): rerun on the copies here, output byte-identical to the
  stamped `decode_B.out`.
- `scripts/counts.py`: every strict count above, the halves, the held-out check, and reader 2's 13 class-only units.
- `scripts/align.py`: sign agreement by the methods of readers 2 and 3 (511/565 = 90.44%; 497/564 = 88.12%; 484/564 =
  85.82%) and a three-way table in reader 1's frame (`alignment/three_way_signs.tsv`).
- `scripts/adjudicate.py`, `scripts/decode_adjudicated.py`: the adjudicated transcription and its one decode.
- `scripts/shuffle_control.py`: German 4-gram score against 5,000 shuffled keys, seeds 20261112 and 7, every reading.
  Corpus: the repository's `targets/adfgvx/corpus/de_21000, de_22367, de_2229, de_6079`, each asserted German by header.
- `scripts/holes.py`: the 33 units not read and their causes (`holes.md`).
- `scripts/decrypt_readers.py`: line-by-line decryptions of the three readers.
- Repository scripts (`docs/_check_reading.py`, `docs/_validate.py`, `docs/_check_profile.py`) were **not run**;
  `profile.json` was checked by hand against `profile.schema.json` for required keys and enums.

## Transcriptions

- `transcriptions/reader1_frozen.txt` and `reader1_units.seg`: reader 1, stamped.
- `transcriptions/reader2_blind.txt`: reader 2 as scored, after a one-character label erratum made after freezing
  (line 01, `n` to `N`); `reader2_blind_as_frozen.txt` is the file as frozen (md5 de87c01d, reconstructed and checked).
  `reader2_mapping.md` (sign classes mapped to reader 1's labels, written before decoding), `reader2_labels.txt`.
- `transcriptions/reader3_blind.txt`, `reader3_signchart.md`, `reader3_mapping.md` (frozen before decoding),
  `reader3_labels.tsv`; `decryptions/reader3_blind.json` is its decode.
- `transcriptions/adjudicated.tsv`, `adjudication_rule.md`, `s_forms.txt`, `ADJUDICATION_FROZEN.md5`.

## Prior art

CLEAR in what was checked, and thin: Danske Magazin, Kong Christian IV's egenhaendige Breve, Danske Samlinger,
Historisk Tidsskrift, the Swedish Handlingar, DECODE, Cryptiana, archive.org full-text searches. An anonymous letter
cannot be searched by name, so "not printed" cannot be proved. Not checked: Christian Wilhelm's 1627 correspondence,
Venetian state papers.

## Catalogue corrections (entry 2541)

- Image 447 (right page) is a 1628 chancery decipherment sheet ("Scultetus 17 Novemb:") for Schultetus's number code,
  so that code is not a first reading.
- Schultetus's capital-letter words are a simple substitution, read in the main (not part of this folder).
- The folder holds this second, different cipher (443), not in Schultetus's hand.

## Integration check (12 Nov 2026)

- Reproduced: key_B.txt, reader 1's transcription, the stamped files (SHA-256 equal to the manifest), the adjudication
  hashes and the counts 93/103, 62/104, 49/110, 70/103, 47/103. An independent decoder gives the same German. A
  vocabulary control of my own (words of 3+ letters found in the repository's German corpora): 60 of 100 cipher words
  for the true key, best of 3,000 shuffled keys 6.
- What the German fit shows: the key is the right key for this letter's signs. It does not test the key blind: the key
  was fitted to the whole letter by hand with the transcription (the contributor says so), so the lines 11-19 "held-out"
  figure (63/68) is not a held-out test, and the method stays "key recovered from ciphertext-only" on the strength of a
  crib and word patterns, with the language fit as confirmation.
- Order of events is by the contributor's record. The RFC 3161 reply (12 Nov 2026 02:25:10 GMT, imprint equals the
  manifest SHA-256) covers reader 1's folder only. The two blind transcriptions and the adjudication (frozen 13:17:09,
  decoded once 13:17:19 UTC, a ten-second gap) are not stamped: that the adjudication was frozen before it was decoded
  rests on the contributor's record.
- Images: image 443 (api.rigsarkivet.dk/ao/v1/images/48900927, 4473 x 3436) is a spread; the right page is the
  letter, signed "Quem novit" with a flourish, with 117, 118, 3000 and 20 as the contributor transcribes. The g/q
  signs (g before theta in "sich", "noch", "machen"; q elsewhere) look alike at the resolution used here; reader 1's
  sign list has g before theta 14 times and q never before theta, and the two word-initial c (commendiret, currentis)
  are g, which supports two signs. Not settled by eye.
- Catalogue 2541: image 447 (48900931) checked at full size: the right page is a chancery decipherment sheet headed
  "Scultetus 17 Novemb:" for the number code of the letter of 17 Nov 1628 on the left. The 2541 entry's statement that no
  decipherment was seen on any frame is corrected in catalogue.json.
- One key, one entry: no other target uses this letter-sign key (zobel1629, same collection series, uses figures).
- Write-up (page, manifest, ledgers, portraits, claims review) is not part of this commit; the writer is proposed, not proved.

## Remaining gaps

- codes 117 (twice) and 118 - blocker: no-key-material; three tokens. Corrected 14 Nov 2026: 118 also heads the sibling letter of 25 July 1627 (images 465-466), written at another place, so it is a dating word of the writer's own code, not the place of writing (M. V. Prizmic, issue #450 comment of 14 Nov 2026; doi:10.5281/zenodo.24210516). Our earlier gloss 'place of writing, Venice likely' is withdrawn.
- g/q sign class (13 units), pi/Z/n and c/e classes (7 units) - blocker: illegible; the tails of g and q cannot be told apart at the resolution available here (image 443, 4473 x 3436), three readers split; a person comparing them at full size is needed
Not unread cipher pieces, but open: the writer and the year (1627 or 1628) are not proved; the clear German was read by one
reader only, and no person has compared any transcription with the image.

## Escalation

- [x] siblings: neighbouring leaves images 426-475 of unit 261377 swept; image 447 is a chancery sheet for Schultetus's number code, a different cipher. Corrected 14 Nov 2026: our sweep missed a sibling in this key. Images 465-466 (Rigsarkivet list ids 48900949-48900950) hold a second letter in the same hand, signed 'Quem novit E.', dated in cipher 25 July 1627, found and read by Mark Vladimir Prizmic (issue #450 comment of 14 Nov 2026; preprint doi:10.5281/zenodo.24210516). We checked only that key_B reads its opening unchanged ('gnedigster konig', 'siebenden'); its transcription and reading are his and are not in this folder.
- [x] clear-pages: no decipherment on or beside the leaf (images 442-449 seen)
- [x] known-keys: zobel1629 (figures) and Schultetus's number code are different systems and do not apply; no other key of this series is a letter-sign substitution
- [x] print: Danske Magazin, Christian IV's egenhaendige Breve, Danske Samlinger, Historisk Tidsskrift, Swedish Handlingar, DECODE, Cryptiana: nothing (thin: an anonymous letter cannot be searched by name)
- [x] key-rebuild: key built by hand from a crib and word patterns; no value for the one n-form sign, none possible for the code numbers
- [x] retry: the three independent readings and their majority adjudication were each decoded with the key; the remaining 33 units are disputed signs, emendations or codes

## Files

`profile.json`, `key.tsv`, `key_B.txt`, `counts.txt`, `holes.md`, `transcriptions/`, `alignment/`, `decryptions/`,
`readings/`, `scripts/`, `checks/`, `timestamps/` (RFC 3161 `.tsq`/`.tsr`, OpenTimestamps `.ots`, manifest, `README.md`).
