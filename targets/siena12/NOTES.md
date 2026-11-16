# Siena, Concistoro 2308 fasc. 2 no. 12 (DECODE R4790): Naples, 10 March 1413, a royal marriage offer to Sforza

Status: read (George Lasry's estimate: "more than 95 % of the text reads"); key recovered from ciphertext-only by
George Lasry with CTTS and Claude, 15-17 Oct 2026. Contributed; this project filed it and checked the record history.

Split on 18 Oct 2026 from `targets/siena1421/` (catalogue 336, the bundle) under the one-key rule. George Lasry's
consolidated report of 17 Oct 2026 groups the fascicle by key; no. 12 is the only piece under its heading ("B. A
Neapolitan court cipher of 1413"), so it is its own entry. Nos. 20 and 23 of the same spring (Ladislaus's campaign
against Paolo Orsini) are a different key, with their own page: [`targets/siena2023/`](../siena2023/NOTES.md).

Work date: 2026-10-18 (report received 17 Oct 2026).

## Credit

- **Solution: George Lasry**, "with CTTS and Claude", 15-17 October 2026, in *The cipher documents of Concistoro
  2308, fasc. 2* (consolidated report, 36 pp., 17 Oct 2026), sent by email to Daniel Bourdeau. The report's status
  line: transcription by Claude, refined by the author in CTTS; key recovered by Claude's own simulated annealing
  (865 symbols), then refined. The report does not name the Claude model.
- This project: the record history below (the DECODE "Decrypted" question), the reading and translation filed
  verbatim, the DECODE queue entry, the page.

Files: `lasry_report.md` (the report's whole section on no. 12, pp. 10-12, and its contents line, verbatim);
`reading_no12.txt`, `translation_no12.txt` (his decipherment and translation, verbatim from the appendix);
`key_lasry.jpg` (his key figure: signs cut from the manuscript, with occurrence counts). The report's PDF is not
committed. No sign-level transcription of no. 12 is in the repository (the report gives the reading, not the CTTS
transcription), so no count below is re-measured here.

## The document

ASSi, Concistoro 2308, fasc. 2 "Lettere in cifra", no. 12 (pencil number = Meister's numbering). DECODE R4790
(`Concistoro_2308_44`, created 2023-03-31, owner 32), images `IMG_R4790_I27920_P1` (verso: address, show-through),
`P2` (the letter) and `P3` (the fascicle cover "Concistoro 2308, Fasc. 2, Pezzi 25"). DECODE: dated "1500-1599" (the
placeholder of the whole fascicle), status N/A, cipher type unknown, no documents attached (checked 18 Oct 2026).
The same sheet is photographed again, rotated 180 degrees, as page 7 of DECODE R1858 "Siena keys and ciphers".

Wholly in cipher, address included. Per the report: 865 cipher symbols (822 in the 16-line letter on P2, 43 in the
3-line address on the verso) and 95 word dividers.

## The key (the report's description, verbatim)

"46 distinct signs. Homophonic substitution with word dividers: two to three signs for each vowel and for several
consonants, a crown sign for "Re" and a few name signs." The figure (`key_lasry.jpg`) shows: a 3 signs, e 3, i 4,
n 3, o 3, p 3, c 2, t 2, one sign for each of b d f g h l m q r s u/v z; nomenclature: the crown = RE (4), a sign
= "Signoria Vostra?" (2), two signs "name?" (2 and 1); nulls and separators: two signs (53 and 42 occurrences);
six signs "unknown", one occurrence each. Counted on the figure: 35 letter signs + 4 nomenclature + 2 nulls/separators + 6 unknown = 47 shapes, against the report's "46 distinct signs" (one of the unknowns may be a variant).

Not the key of nos. 20/23 (report heading A, 60 signs, nomenclator of seven name signs) and none of the 43 key
sheets of fasc. 1 (the report lists no filed key for it).

## Was no. 12 deciphered before? (the contamination question)

- **No earlier decipherment of no. 12 is known.** The project's bundle notes (`siena1421/NOTES.md`, 24 Sept 2026, now `research/siena2308/README.md`)
  "took as read" no. 12 because its second photograph sits in DECODE R1858, whose status is "Decrypted" (Daniel's
  instruction that day: trust DECODE's Decrypted status), and it was not counted as a result.
- Checked 18 Oct 2026 on DECODE (record pages fetched with the cookie): **R1858** ("Siena keys and ciphers", 8 pp.,
  created 2020-11-24 by DECODE owner 32, status Decrypted, record type ciphertext) has **no document attached**:
  no transcription, no decryption, no key file. Its 8 images are key sheets of fasc. 1 (the 1454 Milan key, "Cifra
  cum frate Bernardino", the 1475 key, R4747's slips) and, as p. 7, no. 12; that photograph shows no gloss, no
  interlinear decipherment and no note. **R4790** has status N/A and no documents. So R1858's "Decrypted" applies to
  a record that is mostly key sheets (a key is "decrypted" by nature), not to a reading of no. 12.
- Cryptoole (satoru.net) marks its row XX15XX-97 "Concistoro" (DECODE R4790, R4794) "solved/plaintext_attached"
  (`research/cryptoole/candidates.md`, 14 Oct 2026). That is a group status over the merged Concistoro records
  (the plaintext of no. 13 is no. 16, R4804, and our own ledgers are among its sources), not a decipherment of no. 12.
- Print: Meister 1902 (pp. 50-51) counts and dates the pieces but prints no reading of no. 12; the 1952 inventory
  calls the letters "solo parzialmente decifrate". Nothing found in the earlier sweeps (siena1421 Escalation).
- So George Lasry's reading (15-17 Oct 2026) is, as far as known, the first. Recorded in profile.json
  `conditions.prior_solution` as exists "no", found "not found". Asked George below whether he knows otherwise.

## Contents (the report)

From the bishop(?) of Fermo (signed "Vescovi(?) de Fermo") to Sforza Attendolo, "magnifico capitanio", Naples,
10 March 1413 ("a dì dieci de marzo, sesta indictione"; the sixth indiction with a king on the throne of Naples and
Ludovico Migliorati alive gives 1413). Carlo di Ludovico da Cesena has come to Naples and reports that the King is
willing to make a marriage alliance with Sforza. Two earlier matches fail; the King offers two girls of his house,
the daughter of Ludovico di messer Gianni de' Malatesti (eighteen, legitimate) or his niece, daughter of Niccolò
Filippo Brancaleoni of Castel Durante; Sforza may ask for whichever he prefers. The address on the verso: "[Stre]nuo
viro Sfortie [magn]ifico captaneo ...". Sforza, a widower since 1411, married Caterina Alopo in 1415, so the offer
came to nothing (report). Three weeks before no. 20 (Perugia, 30 March 1413) and the royal memoranda of no. 23.

Where Sforza was: the report cites Minuti and Pellini for Sforza at Perugia in February-March 1413; the atlas puts
the letter Naples -> Perugia on that basis.

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: the letter is Italian (Neapolitan) of 1413, not French: explicit-hole bar. reading_no12.txt (Lasry's decipherment verbatim): explicit 0.708, plain 0.25 on dialect forms. Entry language set to it and reading pointed at reading_no12.txt. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

## Remaining gaps

- the two name signs ("name?", 2 and 1 occurrences) and the "Signoria Vostra?" sign - blocker: no-key-material; each occurs once or twice, the report leaves them open
- the signer ("Vescovi(?) de Fermo") and the two girls' fathers (Ludovico di messer Gianni de' Malatesti, Niccolò Filippo Brancaleoni) - blocker: no-key-material; identification, not decipherment; the report's searches found no match
- a few words marked (?) or [?] in the reading (saviade, pigliole, pi pare, nove, deia, three [?] after "de le doe pigliole de"; six "unknown" signs of one occurrence each) - blocker: too-short; single occurrences, left open by the solver; no transcription in the repository to retry them on

## Escalation

- [x] siblings: the whole busta was opened in siena1421 (keys R4746-R4789, letters R4790-R4814, R1858); per the report no other piece is in this key; nos. 20/23 (same spring, same circle) are a different key
- [x] clear-pages: P1 (verso, address in cipher) and R1858 p. 7 (second photograph) checked 18 Oct 2026: no decipherment
- [x] known-keys: the report lists no filed key for no. 12; the fasc. 1 keys were compared with the letters by eye in siena1421
- [x] print: Meister 1902, the 1952 inventory; the report's searches (DBI Migliorati, Larousse/kleio Sforza marriages, Malatesta of Sogliano, Brancaleoni of Casteldurante)
- [n/a] key-rebuild: the key is George Lasry's; no transcription of no. 12 is in the repository to extend it on
- [n/a] retry: the same; the open words are his and are filed as he left them

## Questions for George

1. R1858 ("Siena keys and ciphers", 2020, owner 32) is marked Decrypted on DECODE with no document attached, and it
   holds a second photograph of no. 12. Is it your record, and did anyone read no. 12 before 15 Oct 2026?
2. Could you send the CTTS transcription of no. 12 (sign sequence)? With it we can measure the share read,
   validate the key statistically and show the "watch it decipher" replay on the page.
3. Which Claude model ran the annealing and the transcription (for the paper's profile)?

## 14 Nov 2026: the cipher has no transcription, and why (audit section I, "no transcription file")

- In the folder: the report's reading, translation and key figure; not the CTTS transcription.
- DECODE R4790, public record page: three images, no text attachment; full-size images need a login. No other online
  copy of Concistoro 2308 is known here.
- `outcome.texts[0].transcription_missing` replaces the empty `transcription` list. Unblocks it: George Lasry's CTTS
  transcription (question 2 above), or image P2 at full size to transcribe against `key_lasry.jpg`.
