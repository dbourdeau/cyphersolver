# christianv1673: Christian V to the envoys Jens Juel and Christoffer Lindenov in Stockholm, Copenhagen, 25 May 1673, closing cipher block (catalogue 2528 = lead 2531)

Status: read in part (Brice Dudout, 11 Nov 2026; integration check 12 Nov 2026). 49 of the 68 cipher words are read with certainty = 72.1%, under the 95% bar (11 more are probable, 2 restored, 6 unresolved). Key recovered in part: six code groups of the text (seven occurrences) have no value. The key's three-digit groups were tested against the decipherment of the time of a held-out order of 6 Oct 1674: 0.849 of gloss segments exact vs at most 0.144 for 200 permuted keys. An earlier pre-registered test on the 1673 block itself failed. The values of the 1673 signs rest on the loose leaf, not on the test.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents (transcription, sign table, key, protocols,
measurement, reading and write-up). Catalogue entry **2528** (lead **2531** is the same order from the second TKUA pass), found
and vetted by Daniel Bourdeau on 11 Nov 2026 (TKUA paging pass), who pointed to the 1674 orders deciphered between the lines and
to the loose decipherment leaf.

## Document

Copenhagen, Rigsarkivet, TKUA, Speciel del, Sverige, Jens Juels gesandtskabsarkiv; Arkivalieronline unit 261588 (62 images).
Order of Christian V, countersigned Griffenfeld, "Kiøbenhavn den 25 Maji Ao 1673", to his envoys in Stockholm, Jens Juel and
Christoffer Lindenov. Two cipher blocks in a code of three-digit groups, small numbers and signs, with many Danish words left in
clear. The first block (images 8-9) is deciphered on a loose chancery leaf (image 9 right) whose filmed side ends with that block.
The **closing block** (foot of image 10 and image 11, 15 lines, 197 tokens) has no decipherment: it is the target here.
The images were used for study only; none is included, nor any crop or derivative (Rigsarkivet images are treated here as not
republishable). Credit: Rigsarkivet, Arkivalieronline.

## System and key (`key.tsv`)

A syllabic code. Three-digit groups run in alphabetical blocks: for each initial, five syllables (417-421 ba be bi bo bu, 447-451
ca ce ci co cu, 482-486 da de di do du, 530-534 fa fe fi fo fu, and the same for g, h, k, l, m, n, p, r, s, t, v), each followed
by whole words of that initial (585 haffuer, 595 hvor, 616 ingen, 648 krig, 699 med, 847 saaledes); names and countries in the
2xx-3xx range (284 Sverig, 309 Holland, 321 Franckrig); small numbers and signs stand for single letters (4 t, 5 e, 18 r, ff n,
S t, Z n). The hand of 1673 gives some signs other values than the hands of 1674 (barred m = k in 1673, u in 1674; 3 = u).

The key was rebuilt from the decipherments of the time written between the lines of two sibling orders in the same unit
(21 July 1674, images 32-37; 3 Oct 1674, images 39-41), plus the loose leaf of 1673. `key.tsv` (CC BY 4.0) has three sections:
A = the measured key exactly as frozen (KEY-v2, 222 entries); B = the values of the 1673 hand for signs and small numbers, from
the leaf; C = three values added after the measurement (486 du, 534 fu, 590 huis), not measured.

## Validation (`validation.txt`)

Two tests were declared in advance and each was run once.

**Test 1 failed.** Declared (`frozen/PROTOCOLE.md`): key v1 applied once to the closing block of 1673 itself, scored by the share
of decoded letters covered by Danish words (COV); the key passes only if COV >= 0.70, COV is at least 0.06 above the best of 200
permuted keys, and at least 0.06 above the best of 200 shuffles of the groups; "otherwise a negative result, no reading presented
as sure". Result (`frozen/scripts/mesure.out`): COV 0.722; best permuted key 0.668, so the margin is 0.054 against the 0.06
required: failed by 0.006; best shuffle 0.648 (passed). By its own rule the test is a failure, and the closing block is spent as
a test: it was not measured again. The contributor's explanation is that keys with syllables swapped still give Danish-looking
strings in a syllabic code, so a lexical score cannot separate them; that is an explanation after the result, not a test.

**Test 2 passed, on other material.** A different test was then declared (`frozen/PROTOCOLE-2.md`), on ground truth: a third
glossed order, of 6 Oct 1674 (images 42-43), was held out; the key (KEY-v2) was rebuilt without any of its pairs, then decoded
once against the glosses of the time. **0.849 of its 776 gloss segments (659) come out exactly as glossed**, against at most
0.144 for 200 permuted keys (mean 0.033) and 0.035 for 20 shifted glosses; the criteria hashed beforehand (>= 0.65, +0.40 over
each control) are all met. The held-out order was not unseen: its pairs were known in aggregate and one agent saw image 43 at
reduced size (declared in full in `validation.txt`).

**What each test covers.** Test 2 validates the code as rebuilt from the 1674 glosses, that is the three-digit groups (94 of the
197 tokens of the closing block, 56 distinct groups). The other 103 tokens are small numbers and signs whose 1673 values differ in
part from 1674 (barred m = k in 1673, u in 1674; 29 = x in 1673, i in 1674); they rest on the loose leaf, with which the first
block of 1673 decodes into running text, and on no measurement. The order of events (protocols and key hashed before each run)
is by the contributor's record: the pull request is a single commit and the timestamps in the FREEZE files are his own.

## Reading (`reading.md`, `translation.md`)

68 words come from cipher groups: 49 certain, 11 probable, 2 restored, 6 unresolved. **Read share 49/68 = 72.1%**: read in
part. Only the certain words count as read (README read bar: a guessed word, a supplied word and a hole are not read; the
probable words each rest on an inferred value, a single attestation or a doubtful sign). The contributor's count in the pull
request took certain and probable together, 59/68 = 86.8%, with Exempel still among three restored words; that is his figure
and it is not used elsewhere. (His working fiche gave 46/10/3/6 of 65; three certain words were missing from its list.)

Content: the salute at sea in the Sound (Øresund). If the Swedes argue that their warships may pass "our castles" without
striking (strygen), the envoys are to answer that any such exemption is only an indulgence for a time, as others are allowed
elsewhere by an agreed signal; that it rests on no other footing than the one laid down, that other crowned heads, and the Crown
of Sweden itself, whose example they have alleged several times, show that none of them claims the salute; and that the king is
far from giving up a right that he and his ancestors have held unchallenged for so many years. The order then turns, in clear,
to the coinage.

## Prior art

No decipherment of the closing block is known. The loose leaf of the time covers the first block only, and its verso was not
filmed. Daniel Bourdeau's vetting of entry 2528 (11 Nov 2026) found nothing on DECODE, in Tomokiyo or in Lasry, and found that
Danmark-Norges Traktater vol. 6 does not print or cite this order; the second TKUA pass (lead 2531) opened Vaupell, Jørgensen,
Fryxell and Danske Samlinger without finding it. A quick web search of ours found no edition either. We have not seen the printed
volumes ourselves nor searched Rigsarkivet's inventories of the Juel and Lindenov instructions, so an edition we do not know of
remains possible.

## Remaining gaps

- five of the six unresolved words and the two restored ones of the closing block (groups 32, 320, 348, 384 twice, 646, 906) - blocker: open-codes; the letter reads but these code groups do not: none is glossed in images 32-43, and the syllable blocks give only the initial of 384 (a-) and 646 (k-); another order in the same code would fill them
- la·g·ge·n·s (T05): every group has a value but the word does not construe - blocker: illegible; a misread sign in our transcription is the likely cause ("Flaggens" would need an f), to be checked on the original image
- the verso of the loose decipherment leaf (image 9) - blocker: needs-physical-access; it was not filmed and might carry the decipherment of the closing block; only Rigsarkivet can say
- the overwritten group in T04 (image 11 line 1), 841 or 541 - blocker: illegible; the last digit is blotted and the first is drawn like this hand's 5 as much as its 8; the full-size online image does not decide between "Indulgencien, tid" and "indulgence for en tid"
- a blind re-reading of the other doubtful signs of the closing block (T02 Q, T07 768 lam) - blocker: illegible; seen at the resolution served online, not yet re-read blind
- the eleven probable words (Indulgencien, udstirkelse, saaledes, Sammentegn, aldre, Kronede, strygen in T12, upaakieret, huis, Fundament, Exempel) - blocker: no-key-material; each rests on a value inferred from the syllable blocks, on a single gloss or leaf attestation, or on a doubtful sign, and the unit holds no other text in the 1673 hand to confirm them
- prior art outside the repository (an edition of the order, Rigsarkivet's inventories) - blocker: needs-physical-access; the printed volumes named under Prior art were opened in Daniel Bourdeau's vetting passes, not by the contributor or at the integration check, and the inventories are not online

## Escalation

- [x] siblings: all 62 images of unit 261588 checked on contact sheets; cipher only on images 8-11 (1673) and 32-43 (1674); the three glossed orders of 1674 transcribed with their glosses and used for the key and the held-out test
- [x] clear-pages: the loose leaf at image 9 right is the chancery decipherment of the first block only (aligned group by group); no other clear copy of the order in the unit
- [x] known-keys: the only key material known for this code is in the unit itself (1674 glosses and the 1673 leaf); DECODE, Tomokiyo and Lasry have nothing (Daniel's vetting); no printed key found
- [x] print: Danmark-Norges Traktater 6, Vaupell, Jørgensen, Fryxell and Danske Samlinger (Daniel's two passes, 11 Nov 2026): the order is not printed; our web search found no edition
- [x] key-rebuild: key extended by the alphabetical syllable blocks (486 du, 534 fu inferred; 590 huis from the h block and a gloss); 384 and 646 bracketed to an initial; nothing else can be inferred for 32, 320, 348, 906
- [x] retry: every unread group searched in all glosses of images 32-43 (42-43 after the measurement) and in the leaf; the reading regraded with key v2 and the sign table (working fiches 84.6% with key v1, then 86.2% with key v2 on a list short of three certain words; recount 86.8%; all three by the contributor's count of certain + probable words, which the integration check replaced by 72.1%, certain words only)

## Integration check (12 Nov 2026)

Pull request #409 was verified independently and then integrated; this section records what was checked and what was changed.

Reproduced:
- Test 2: `mesure2.py mesure` in a scratch copy gives 0.849 (659/776), best of 200 permuted keys 0.144 (mean 0.033), best of 20
  shifts 0.035; `mesure2.py calib` gives 0.769 (536/697) and 0.706 (1224/1734). KEY-v2 rebuilt by the script without order C is
  byte-identical to the frozen file (222 entries, SHA-256 5334c7aa...). All 8 FREEZE-2 hashes match.
- Test 1: the lexicon `working/da.json.gz` named in FREEZE.sha256 is not in the pull request, but it is this repository's
  `lang/lexicons/da.json.gz` (same SHA-256, 45a7213b...). With it copied in, all 19 FREEZE hashes match and `mesure.py mesure`
  gives the filed line again: COV 0.722, best permuted key 0.668, best shuffle 0.648. The failure reproduces.
- Counts: 197 tokens (`_check_profile.py --measure`); 94 three-digit tokens, 56 distinct; 68 cipher words.
- A second decoder written from `key.tsv` and `transcription.txt` matches `decryption.txt` on 14 of 15 lines; the one difference
  was group 29 (below).
- Images 10, 11 and 43 fetched from api.rigsarkivet.dk (plain requests answer): 196 of the 197 tokens agree with the images; the
  one open place is T04. About 65 glossed groups of the held-out order on image 43 agree with the pairs file.
- The reading was read as Danish sentences against the translation: it is coherent on the salute in the Sound.

Corrected:
- **Read share.** Headline changed from 86.8% (certain + probable) to 72.1% (certain only), by the README read bar applied as
  written. The class does not change.
- **Key state.** `outcome.key` changed from "recovered" to "partial": six groups of the text have no value (32, 320, 348, 384,
  646, 906; seven tokens). `outcome.codes_open` filled.
- **Group 29.** `decryption.txt` printed 29 = i (the 1674 value) while `reading.md` used x for "Exempel" and called it restored.
  The leaf supports x in the 1673 hand: in the first block, line C14 has `5 29 860 ff` where the leaf reads "extenderes". 29 = x
  is added to `key.tsv` section B, `decryption.txt` now prints "exempel", and Exempel moves from restored to probable (one
  attestation, not measured). So the unvalued tokens are seven, not eight.
- **T04, image 11 line 1** (looked at again at full size, 4358 px wide). The group after 448 is written `.84?.` or `.54?.`: the
  last digit is a blot, overwritten. The first digit has an open hooked top like the 5 of 585 and 544 lower on the page, and
  unlike the closed two-loop 8 of the 448 beside it; but the ink is heavy and an 8 cannot be excluded. So 541 is at least as
  likely as 841 on the image. With 541 = for the line runs "at det ickun er en indulgence for en tid, som ...", which is
  regular Danish; with 841 = si it gives "Indulgencien, tid". Not established: the transcription stays as frozen (841?), the
  alternative is noted in `reading.md` and `translation.md`, and the word count is unchanged. Either way the word is among the
  probable ones (486 = du is inferred).
- **Test 1** is stated as failed, with what was declared, the score and the bar (Validation above).
- **Scope of test 2** stated: it validates the 1674 code groups; the 1673 signs rest on the leaf. Checked at verification: the
  first block (538 tokens, 38 without a value) decodes into running text that matches the leaf ("woris mening var at ...
  foretage ... amicabel interposition ... underhandling intet kunde udwirke").
- Thin support inside the validated key, for the record: 544 fra, 583 ho and 852 swar have one gloss each in 1674; 872 is
  glossed tid twice and til twice; 847 is glossed forlader four times and saaledes twice (the weighting chose saaledes, and the
  held-out order agrees once).

Not checked: prior art outside the repository (see Remaining gaps); the order of events beyond the contributor's own record.

A crop of image 11 (the closing block) was added to the site at integration, credited to Rigsarkivet; the contributor sent no
image. Credits follow the pull request: Brice Dudout (solution), the chancery decipherments of 1673-74 (key material); the
pointer to the 1674 orders and the leaf came from the project's own TKUA paging pass and catalogue entry 2528.

Claims review of the page (12 Nov 2026). No separate reviewer was available in this session, so `docs/christianv1673.html` was
re-read line by line against these notes, `profile.json`, the reading files and `validation.txt` with the checklist of
`.claude/skills/writeup/claims-review.md`. Fixed on that pass: the six unvalued groups account for five of the six unresolved
words, not all six (la·g·ge·n·s has a value for every group; the same slip was in `reading.md`); "reads as connected Danish to
the end" now says "with three holes"; the 222 entries are those of the frozen file, of which `key.tsv` lists 218; the meta
description and the index blurb now say that the first test failed; image 11 carries twelve of the fifteen lines, not all
fifteen (header of `transcription.txt`). An independent reader is still owed.
