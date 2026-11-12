# vibejuel1649: Peder Vibe to Peder Juel, Danish resident in Stockholm, 1649-1651, cipher passages in the old cipher ("gamle Ciffres") of 10 letters or pages (part of catalogue 2527)

Status: read in part (Brice Dudout, PR #410, 11 Nov 2026; split out of vibejuel1651 by key and integrated 12 Nov 2026). Key recovered based on adjacent plaintext, key state partial: the letter alphabet and its opener rule are recovered, the nomenclator has no values. 244 of 250 cipher words given a value (97.6%; 212 certain, 32 probable, 1 restored, 5 unresolved); with the 68 nomenclator codes counted as holes the read share is 244/318 = 76.7%, under the 95% bar. The rule of this cipher never had a pre-registered test; the one pre-registered test that included a letter in it failed (see Validation).

Contributed by Brice Dudout (Europe chiffrée), with AI agents (transcription, system, protocols, measurements, reading and
write-up; the model is named in the pull request). Catalogue entry **2527**, found and vetted by Daniel Bourdeau on 11 Nov 2026
(TKUA paging pass), who pointed to the interlinear letters on image 78 as the crib.

The letters of 1651-1655 in the same unit use a different cipher, the new alphabet ("ny Alphabet"), with its own target:
`targets/vibejuel1651/`. This folder holds the old cipher only (split on 12 Nov 2026, see the end of these notes).

## Document

Copenhagen, Rigsarkivet, Tyske Kancelli, Udenrigske Afdeling (TKUA), Speciel del, Sverige: Resident Peder Juels og Mogens Høegs
gesandtskabsarkiver, Ordrer og breve m.m. 1648-55 (leaves stamped "Ny kongl. Saml. Fol. 1299 e"); Arkivalieronline unit 261583,
images 62-74. Letters of Peder Vibe in Copenhagen to Peder Juel in Stockholm, numbered in an old hand, with passages and whole
leaves in a number cipher between clear Danish. No letter in this cipher carries a decipherment.

Eleven sections in `transcription.txt`, ten letters or pages: image 62 (end of N. 325, 11 Jan 1649), 63 right (N. 298, early
1649), 64 right ("N 8", 22 Feb 1649), 67 left ("N 21", 25 Apr 1649), 68 right ("N 28", April 1650), 69 left (end of a letter,
18 Apr 1650), 70 right ("N 32", 23 May 1650), 71 left (f. 317, a page wholly in cipher, received 6 June 1650), 72 and 73 left
(f. 318, a slip wholly in cipher and its verso, July 1651?), 74 (N. 330, 20 Sep 1651).

The contributor included no image. Credit: Rigsarkivet, Arkivalieronline.

## System and key (`key.tsv`)

A shift cipher with the shift chosen per word. Each cipher word is an **opener** followed by a **body**: the opener (24-39) gives
a shift k, and each body number is the rank of the letter plus k. Vibe names the cipher in clear on image 62 (11 Jan 1649): the
new alphabet ("dett ny Alphabet") is to be sent, and meanwhile he writes "wed woris forige gamble Ciffres" (checked on the image).

- **gamle Ciffres**: 23 letters (i = j, u = v/w, the 21st letter is x), **cyclic mod 23**; k = -(opener mod 3), so openers
  24/27/30/33/36/39 give 0, 25/28/31/34/37 give -1, 26/29/32/35/38 give -2.
- 32/33/34 in the body stand for 1/2/3, and a word may be split in pieces with their own openers.
- **Nomenclator**: two- and three-digit numbers between the words: 68 code tokens, 22 different numbers (211 sixteen times, 422
  and 228 eight times each, 257 seven times ...). None is identified. None of the 22 occurs in the letters in the new alphabet.
- `scripts/decode.py` decodes `transcription.txt` with the fixed rule into `decryption.txt` (no language model).

How it was found (by the contributor's record). The shift-per-word system was found on N. 319 (image 78), a letter in the new
alphabet, from its partial interlinear decipherment of the time. The table of N. 319 did not read N. 330 (image 74). After the
failed test 1, N. 330 and the letters of 1649-50 were read with a cyclic 23-letter alphabet and k = -(opener mod 3), and tied to
Vibe's remark on image 62. No gloss of the time exists for this cipher.

## Validation (`validation.txt`; the frozen files are in `targets/vibejuel1651/frozen/`)

- **No pre-registered test of this cipher's rule exists.** The rule (cyclic mod 23, k = -(opener mod 3)) was found on the
  held-out set of test 1 after that set had been measured and opened, and was not put to a new held-out test.
- **Test 1 failed, and this cipher is why.** Declared: one opener table for the whole unit, the table of N. 319, with a 23-letter
  alphabet; held-out images 74 (N. 330), 77 and 79 right, 54 words, 335 numbers; pass if M1 (mean log-probability per character
  under a 4-gram model of old Danish) is at least the best of 600 controls + 0.30. Result: M1 -3.068, best control -3.281,
  margin 0.21, under the bar of 0.30. N. 330 is in the old cipher, so the frozen table could not read it. The set was not
  measured again. The order of events is by the contributor's record (one commit, self-declared timestamps).
- **Test 2 does not cover this cipher.** Its rule was changed after test 1 (declared), and its held-out set (images 81-90) is all
  in the new alphabet. It supports the shift-per-word system that both ciphers share, nothing more here.
- **What else makes the rule credible**: Vibe's own remark that he is writing in the old cipher (image 62); the mechanical
  decode with one fixed rule gives Danish words in all ten letters or pages (244 of 250 words), which construe with the clear
  text around them; N. 330 reads off directly on the image (`30.6.17.22.3.8.19.5.17` = frychter, `28.23.18` = at); and the later
  controls below.

## Reading (`reading.md`, `translation.md`)

- 250 cipher words in letters: 212 certain, 32 probable, 1 restored, 5 unresolved. Given a value: 244/250 = **97.6%**.
- 68 nomenclator codes (22 different) have no value. Counted as holes, the read share is **212/318 = 66.7%** on certain words only (244/318 = 76.7% with the 32 probable words): read in part.
  (The pull request gave one figure for both ciphers together, 390/543 = 71.8%.)
- Per letter, on cipher words alone, images 64 (93.3%) and 69 (92.0%) are under 95%.
- Content, the Danish court seen from Copenhagen, 1649-1651: who obtains what from #211 and who is reconciled with whom (image
  62); #422 and #261 studying how best to win #211 (N. 298); sailors and every man discontented while the Marselis and Friedrich
  Möller hold assignments on the best revenues of the realm (22 Feb 1649); the High Steward kept at home by a weakness that he
  pretends, the true reason being that #257 is discontented (April 1650); #228 asking satisfaction for an arrest, and #211 asking
  a declaration about a murder his servants were said to intend (June 1650); the account of the Norwegian fleet; #422 to be
  judged (slip, July 1651?); #211 afraid that #422 will reveal a correspondence, and how to win #370 away from #422 (N. 330,
  20 Sep 1651). Who does what is mostly behind the codes.

## Prior art

No decipherment of these letters is known. Daniel Bourdeau's vetting of entry 2527 (11 Nov 2026) found nothing on DECODE, in
Tomokiyo or in Lasry. Fryxell (1836) prints a Swedish abstract of Juel's register of outgoing letters (catalogue 2553), without
the cipher passages. The contributor's web search (11 Nov 2026) found no edition of the cipher passages. The Royal Library
(NKS 1299 e fol.) and the Danish printed collections were not searched at length, so an edition remains possible. No prior-art
search was repeated at verification or at integration: this section rests on the contributor's and the catalogue vetting's record.

The pointer on p. 115 of Juel's register (2 Sep 1648, to Vibe; catalogue 2553, unit 261585) was followed by WAINUT (PR #457):
it is in this old cipher and is read here, see "Register p. 115" below.

## Integration check (12 Nov 2026)

PR #410 was verified independently before integration (scripts re-run, hashes checked, a second decoder written, images 62, 74
and 83 fetched from api.rigsarkivet.dk). What that found, and what was changed here:

- **Reproduction.** Test 1 reproduces exactly from `frozen/` (M1 -3.068, best control -3.281, failed). All frozen hashes match.
  A second decoder gives the same decryption.
- **Why test 1 failed, measured.** Scoring its three held-out images separately with the frozen table: image 74 (N. 330) -3.980
  against a best control of -3.125 (worse than chance); image 77 -2.353 against -2.961; image 79 -2.632 against -3.094. One
  letter sank the set, the old-cipher one.
- **Later controls made at verification** (after the fact, not pre-registered):
  - the fixed old-cipher rule against 200 random opener tables on the final transcription: -1.926 against a best of -2.536;
  - a per-letter refit of k on all 22 sections of both ciphers agrees with the fixed tables for 383 of 403 words; every
    disagreement is an opener seen once or twice.
- **Images.** Image 74: about 110 numbers on the whole page, 45 of them at full resolution, all agree; the image confirms the
  later correction `25.3.4.12` (ticks between 3 and 4) over the frozen `25.34.12`. Image 62: the clear remark and its five
  cipher lines agree. That one correction is the only number corrected after the measurement that the verification compared
  with the image; none of the listed probable words was checked there.
- **Image 62, last cipher word (integration).** The pull request left `27.12.11.13.14.13.19.13.19` unresolved. On the image the
  digits are 2 7 1 2 1 1 1 3 1 4 1 3 1 9 1 1 3 1 9; divided `27.12.1.11.3.14.13.19.1.13.19` they give MALCONTANT, the word and
  spelling of images 64 and 68 ("#261 has reconciled #211 and #257, who was somewhat discontented"). Entered as a probable word
  (the ticks are hard to place); the frozen files are unchanged. This moves the count from 243/250 to 244/250.
- **Split by key.** The pull request filed two ciphers and the unsolved Krag letters in one target, `vibejuel1651`. This folder
  is the old cipher (see Split).
- **Class and key state.** `outcome.key` is "partial" (the nomenclator has no values); `fraction_read` is the share of cipher
  words given a value (0.976) with `codes_open` 68; `read_share` and `fraction_coherent` are 0.767, the figure with the codes
  as holes, which is the one the site shows.
- **Counts taken again from the files.** 250 words and 68 code tokens for these letters agree with the pull request's table.
- **`scripts/decode.py`** used `eval()` on the `#K` lines; it now uses `ast.literal_eval`, with byte-identical output.
- **Method.** Filed as "key recovered based on adjacent plaintext": no letter in this cipher has a gloss, but the system it
  shares with the new alphabet was found from the gloss of the time on N. 319 in the same unit, and the cipher is named in
  Vibe's clear text. The alphabet and the opener rule themselves were worked out from the ciphertext.
- **Reading review.** The reading was read as sentences against the translation at integration: grade B (coherent Danish where
  the cipher words stand, but most sentences have a code for their subject or object).
- **Claims review.** No separate reviewer agent was available in this session: the page was re-read line by line against these
  notes, the profile and the reading files with the checklist of `claims-review.md`. Fixed on that pass: a reason given for
  writing 32-34 for 1-3 was not from the sources and was cut; the gloss on N. 319 is "of the time", not "a clerk's"; the number
  compared with the image at verification (image 74) is a certain word, not one of the 32 probable ones; Fryxell is cited as the
  contributor cites him; the codes stand for people and places by the sense only. An independent reader is still owed.

### Claims review by a second reader (12 Nov 2026)

- The published read share now counts certain words only: 212 of 250 (66.7% with codes as holes). The 32 probable words (a corrected number, a
  re-divided tick, a supplied letter or an unusual spelling) are not counted, by the rule used for every target of
  this round; the figure with them is given once.
- Wording corrected on the page from this review; see the commit of 12 Nov 2026.

## Register p. 115 (added 12 Nov 2026, from PR #457)

A text outside the ten letters: the entry "To Peder Vibe, Stockholm, 2 Sep 1648" in the extract register of Peder Juel's outgoing
letters (Rigsarkivet, TKUA, Speciel del, Sverige, Ekstraktprotokol 1647-49, Arkivalieronline unit 261585, image 61, p. 115): ten
lines of numbers broken by clear words of the register's secretary, no decipherment written on them. WAINUT (PR #457) applied this
folder's rule unchanged and found it in the old cipher: an own decoder written from the rule reproduces `register_p115/decryption_vibe.txt`
exactly, and three of its nine nomenclator numbers (212, 351, 401) are among the 22 of the letters of 1649-51 (the other six, 277,
339, 412, 426, 442 and 446, are new). One key, one entry: the p. 115 files moved here from `targets/juel1647/` (which holds the
unrelated 8-64 table of the same register). Files: `register_p115/` (transcription with both passes, decryption, reading with
every departure marked, translation, plain text); the reading was checked with the contributor's `check_marks.py` (passes when run from `targets/juel1647/scripts/` on these files: the
reading rebuilds the decryption except at marked places) and compared with image 61 at integration (all ten rows agree).

- Reading: "442 sagde nogle dage til 212 at forrige 412 af 351 277 [fogte] hende bort, nu skal 401 føre hende hid igien. Dog blef
  hand [?dragit]; dennem gang 412 af 339. Kiørde for 412 aff 426 och ..., da tre vogne imellom. Men 412 af 426 gick hen ... hos 446
  ... 339 ... 442": "442 said some days ago to 212 that the former 412 of 351 277 [...] her away, and that 401 shall now bring her
  back here again; yet he was [drawn?] ...; the 412 of 426 drove ... with three wagons between", with the codes open.
- **Counts, by the rule used on this page (certain words only; codes as holes).** 25 cipher words: 23 verbatim in the contributor's
  count, of which two (bort, skal) rest on digits that the blind review of the contributor's work read as 18 and 8 where both of the
  contributor's passes had 14 and 4 (so those two are probable, not certain, here); 1 guess ([?dragit], "24 25 4 17 1 7 9 19": read with
  25 as an opener it gives esbhku, with 24 as the opener and 25 left out d r a g i t); 1 hole (fogte, "31 5 13 6 18": clear figures that
  do not read). So **21 of 25 words (84.0%)**; with the 15 code tokens (nine numbers) as holes **21 of 40 = 52.5%**; the contributor's
  count was 23 of 25 (92.0%). Read in part (grade B, the contributor's blind reader). The clear Danish of the register between the
  runs is not transcribed (a secretary hand on black-and-white microfilm), which is why the sentence checker gives only 0.25.
- **What this is for the rule.** An application of the published rule, unchanged, to a text it was not built on, in another hand
  (a secretary's copy of Juel's outgoing letter, where the letters of 1649-51 are Vibe's own): 21 certain words of 25 read as Danish that
  construes with the clear words around it. It is **not a pre-registered test**: the transcription of p. 115 was made by the
  contributor after the rule was public, and two digits were settled on the image by the contributor's blind reader, who by the contributor's record read them before knowing where the repairs were. It is
  independent evidence that the rule is Vibe's old cipher and that it was in use in September 1648, before his letter of 11 Jan 1649 that names it.
  The nine numbers of the nomenclator found here have no value.
- Headline figures of this target (the 97.6% and the 66.7%, "ten letters or pages") are those of the letters of 1649-51 and were not
  recomputed; p. 115 is counted apart, as above.

## Remaining gaps

- the 68 nomenclator code tokens (22 numbers: 211, 228, 257, 261, 422, 423 ...) - blocker: no-key-material; no code list is in the unit and no letter in this cipher carries a gloss; Juel's replies, the rest of NKS 1299 e at the Royal Library or a code list in the Juel papers could give them
- five unresolved cipher words (image 64: 24.1=7.5; image 69: 30.13.1.11.14 and 27.8.9.12; image 71: 31.?9.5.17.4.12.18; image 72: 32.9.3.6.11) - blocker: illegible; blots, a tear and confused ticks at the resolution served online; the original could settle some
- the 32 probable words, of which only the last word of image 62 was checked against the image, at integration (the verification spot-checked one other corrected number, on image 74) - blocker: illegible; each correction rests on a single number at the limit of the microfilm scans served online (listed with its reason in reading.md)
- no pre-registered held-out test of the old-cipher rule - blocker: no-key-material; every letter of the unit in this cipher has been opened and read; p. 115 of Juel's register (above) is a read, not a pre-registered, application of the rule to new material, and a blind test needs another new text in the same cipher
- register p. 115: "fogte" (hole), "[?dragit]" (guess) and the nine nomenclator numbers (277, 339, 412, 426, 442, 446, and 212, 351, 401 of the letters) - blocker: needs-physical-access for the two words (the figures are clear but do not read; the original letter of 2 Sep 1648 would show a copyist slip) and no-key-material for the codes
- register p. 115: the clear text of the register between the runs - blocker: illegible; a secretary hand on black-and-white microfilm, made out only in part; a reading by a palaeographer of Danish secretary hands is needed
- prior art outside the repository not searched again (no edition, DECODE or literature search at verification) - blocker: needs-physical-access; the Royal Library's NKS 1299 e fol. and the Danish printed collections are not online in full

## Escalation

- [x] siblings: all images 57-95 of unit 261583 checked by the contributor; the new-alphabet letters are read in targets/vibejuel1651; Juel's register (catalogue 2553, unit 261585) was opened by the contributor and its p. 115 (1648) reported to be in this old cipher; that entry is not part of this target
- [x] clear-pages: the clear pages of the unit were read for their remarks on the cipher (image 62: old and new alphabet); none is a decipherment
- [x] known-keys: no key for this cipher is held anywhere; the new alphabet of the same correspondents shares no code number with these letters; DECODE, Tomokiyo and Lasry have nothing (catalogue vetting)
- [x] print: Fryxell 1836 (abstract without the cipher passages); the catalogue vetting (Fridericia 1894, Gigas 1883); the contributor's web search found no edition
- [x] key-rebuild: alphabet and opener rule rebuilt and applied to every letter; codes bracketed only by sense (not counted)
- [x] retry: every unread word retried by the contributor at native zoom with the final rule and regraded; image 62's last word re-divided at integration

## Split (12 Nov 2026)

One key, one entry. These letters arrived in `targets/vibejuel1651` (PR #410) together with the letters in the new alphabet and
three letters of Krag. The old and the new cipher differ in alphabet (23 letters against 25), opener rule and cyclicity, and
their code numbers do not overlap, so they are two keys and two targets. Moved here: the 11 old-cipher sections of
`transcription.txt`, their decryption, reading and translation, the old-cipher section of `key.tsv`, and a copy of
`scripts/decode.py`. `frozen/` (both tests) stays in `targets/vibejuel1651/`, unchanged, so that its hashes keep matching.
The three Krag letters of 1648 (another system, not solved) are a lead: `research/leads.json` id 2527, transcription in
`research/sweep_2026-11-11_tkua_paging/krag1648_transcription.txt`.

### Integration check of the p. 115 addition (12 Nov 2026)

Own decoder from the rule reproduces `register_p115/decryption_vibe.txt`; the contributor's `check_marks.py` passes; image 61 (all ten rows of the entry) fetched from api.rigsarkivet.dk and compared with the transcription at that reading: no disagreement, with line 4 ("18" and "8") not settled by my crop. Claims review of the added section: line by line by the integrating session; an independent reader is owed.
