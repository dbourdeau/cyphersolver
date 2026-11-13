# Ormond to the Earl of Arran, 24 January 1677/8: a "trial" passage in figures (Unsolved Catalogue no. 353)

Status: read in part, 10/20 figures (50%) under the read bar. Key: Tomokiyo's reconstruction of Ormond-Longford Cipher 1 (1680) with every number 7 higher, found by Malcolm McBratney (PR #526, 13 Nov 2026); written up 13 Nov 2026.

Attempted here 26-27 Oct 2026 and closed unread: the 20 figures fit neither Ormond key of these years taken unchanged.
On 13 Nov 2026 Malcolm McBratney found the offset (section below): the 1680 key fits once every figure is reduced by 7.
Cryptoole XX1678-1; Tomokiyo, "An Unidentified Cipher?" on cryptiana `charlesii2.htm`.


## Key identified, 13 Nov 2026 (files in `identification/`)

Every figure is the Ormond-Longford Cipher 1 (1680) number **plus 7**. With Tomokiyo's reconstruction of that key
(Cryptiana `charlesii2.htm`), from the glosses in HMC n.s. v pp.454 ff., the passage reads in part:

> If what he says of [445] and [342] be true, [726] and King are in a [700] [720]; but it seems to Ormond not credible.

Decryption: `[726] an d King ar e in a [700] [720]` / `to Ormond not c re di b le`. English is AI-made.

- 15/20 figures given a value (75.00%; the contributor's count, under the read bar 10/20 = 50%, see Integration check): 10 from printed glosses or the p.498 plain rendering, 4 interpolated from the
  key's regular order (51 e, 47 a, 25 c, 433 le), 1 from context (418 King). Gloss-attested only: 10/20. Holes: 5
  (1680 numbers 438, 335, 719, 693, 713), none glossed in print.
- Tomokiyo's key as published gives 14/20 (418 is an empty row in it) and reads 84 "and", 566 "Dor -> or?". We read
  84 as "an" (p.486 "and" spans 84 50) and 566 as Ormond (p.498 plain rendering; p.454 gloss "Dor").
- Each value was checked on the page images (`identification/GLOSS_CHECK.md`, crops in `identification/crops/`).
- Controls (`identification/controls_out.txt`): over offsets -150..+150 on Longford 1 and 2, only -7 on Longford 1
  spells any vocabulary word of 5+ letters across 3+ groups ("credible"). Random figure sets of the same shape at
  their best of 602 key-offset pairs reach 8 letters 6/2000; shuffles of the real figures at -7 reach it 0/3000.
  The bare hit count (14/20 at -7) reached 14 in 5/2000 random sets, so it is weak on its own.
- No held-out text is in the 1678 numbering. Whether +7 holds over the whole table is not known. The figures
  `445 342` and `700 720` stay open.
- Credit: key reconstruction S. Tomokiyo; glosses HMC; offset identification and check Malcolm McBratney (Brisbane),
  working with Claude (Anthropic). The offset was first noticed by an agent Malcolm ran on Perplexity and was then
  checked independently (transcription, glosses on images, controls rebuilt).

## Integration check (13 Nov 2026)

Verified before merging (report: SOUND WITH CORRECTIONS).

- Scripts re-run with `python3 -I` (read first; they write only `decryption.txt` and `ledger.tsv` in their folder, which
  came out unchanged): `decode.py` 15/20 given a value; `controls.py` and `controls_joint.py` reproduce every figure in
  `controls_out.txt` (14/20 at -7 on K1, unique maximum; only -7 of 602 key-offset trials spells a 5+ letter word,
  "credible"; random sets 8+ letters 6/2000; hit count 14 in 5/2000; shuffles at -7 8+ letters 0/3000; K1 alone 3/2000,
  joint 0/2000).
- Own decoder, from Tomokiyo's table image `charlesii2_Ormond_Longford1.png` typed afresh (not the contributor's K1): at -7
  it gives `[445] [342] [726] and d [418 empty] ar e in a [700] [720] / to Dor/or not c re di b l/le`, the same 14 values.
- Own control: the same key with a different vocabulary (`lang/lexicons/en.json.gz`, words of 6+ letters) over offsets
  -150..+150: only -7 spells a word ("credible"); 1,000 random figure sets of the same run shape, at their best offset:
  6+ letters 8/1000, 8+ letters 0/1000. The word statistic was chosen after "credible" had been seen, so these margins
  are supporting evidence, not a pre-registered test. The bare hit count is weak (14 reached in 5/2000 random sets).
- Images (Internet Archive `calendarofmanusc04greauoft`): p.93 (leaf n122) 20/20 figures agree, sixth of run 1 = 58.
  p.454 (n1235): "in" over 377, "not" over 519, "to" over 725, "re" over 636, "hard" over 337 634 26, "by" over 48 45,
  "Dor" over 566, "pal" over 581 433, "Portsmouth are friends" over 1039 86 237 301. p.469 (n1250): "de" 206, "di" 207,
  "on" over 84. p.479 (n1260): "his discourse with 418". p.498 (n1279): 579 ... 206 followed by "our letters to Ormond
  are opened on that side". All as in `identification/GLOSS_CHECK.md`, except one point:
- **Correction, p.486 (n1267):** "and" is printed over 84 alone and "i" over 50 (Ormond's glosses, which the editor
  footnotes as "scarcely legible"); it does not span 84 50. So the print gives 84 = "and" (as Tomokiyo's key does);
  84 = "an" is the contributor's reading, supported by the alphabetical slot (83 am, 84, no 85 known, 86 ar) and by the
  run 84 26 (an + d). The group gives "and" either way; 84 stays counted as attested, the conflict is recorded.
- **Correction, the share:** under the read bar the 4 interpolated values (58 e, 54 a, 32 c, 440 le) and the context
  value (425 King) are holes. Strict share **10/20 = 50%** (the contributor's own "gloss-attested" figure). The
  contributor's 15/20 = 75% counts them as given a value. Class: read in part. `outcome.fraction_read` 0.50.
- No held-out text: the IA full text of the bound vols. iv-v was scanned for runs of figures; apart from this passage
  they are all in the 1680 Longford numbering (Longford 16 Oct, Arran 30 Oct and 13 Nov, Longford 20 Nov 1680, and a
  six-figure run). The transcription freeze is RFC 3161-stamped (10:32:39Z, hash matches); the order of events is by
  the contributor's record. The 34-file manifest hashes match the files in the folder.
- Prior art: Tomokiyo's key is published; his hidden trial at offset 0 is on charlesii2.htm (seen); no offset is
  tried there. One key, one entry: `targets/ormonde` (Maltravers to Ormonde 1634-35) is a different key; no other target
  uses the Longford ciphers. A reading file `identification/reading.txt` was added for `_check_reading.py`.

The record of the October attempt follows, except that "Ruled out" for Longford 1 applies to the key **unchanged**,
and the Remaining gaps, Escalation and Prior art sections are brought up to date.

## The document

- James Butler, 1st Duke of Ormond (Lord Lieutenant, at Dublin) to his son Richard Butler, Earl of Arran (in London),
  1677-8, January 24. Printed in HMC, *Calendar of the MSS of the Marquess of Ormonde*, New Series iv (1906),
  pp. 92-93, from the Kilkenny papers, now in the National Library of Ireland (NLI). Internet Archive
  `calendarofmanusc04greauoft`; the page is leaf n122 (p. 93). The OCR text is kept locally in `hmc_ns4_djvu.txt`, which is
  not committed. That file also holds vol. v.
- NLI holding: the Ormonde letters of 1665-80 are NLI MSS 2335-2362 (62 vols; NLI collection list A017,
  `nli_a017_ormond.pdf`, p. 3: "Letters and papers re James Butler, 1st Duke of Ormond, public affairs in Ireland etc.
  1665-80", cited to HMC 6th Rept. App. p. 719 and HMC Ormonde n.s. iii-v). The NLI Sources record MS UR 006261,
  "Seven letters of the Duke of Ormonde to the Earl of Arran on Irish affairs. Jan. 7, 24, March 9, June 4, 22, 1678",
  is this letter's bundle. The volume and folio within MSS 2335-62 are not given. Not digitised as far as found.
- Context, from the clear text of the same letter and of its neighbours in the calendar: the passage is about Mas.
  William Douglas, a Scottish nonconformist preacher. Roderick Mansell brought him to Lord Granard at Belfast in Dec.
  1677 (p. 75). Douglas told of a covenanting rising and hidden arms, and the searches in Edinburgh and Glasgow found
  nothing (Lauderdale, 16 Jan, p. 90). Ormond writes: "I have had Mas. Douglas a week with me, but he is still a
  greater mystery to me ... If what he says of 445 and 342, be true ... but it seems ...". Granard (25 Jan, p. 93-94)
  calls Douglas "a mountebank". Ormond to Arran on 29 Jan (p. 99) says Colonel Jeffreys "says Douglas is a notorious
  cheat". The figures most likely say whom Douglas accused (445, 342) and what follows if he is believed or not. That
  is context, not a crib.

## Ciphertext (as printed; `ciphertext.txt`, `figures.txt`)

> If what he says of **445** and **342**, be true **726, 91, 33, 425, 93, 58, 384, 54, 700, 720** but it seems
> **732, 573, 526, 32, 643, 214, 55, 440**. This is a trial whether you are skilful in deciphering, else it might have
> been written in plain letters.

20 figures, all different, from 32 to 732 (measured, `_check_profile.py --measure figures.txt`).
**Correction: the sixth figure of the first run is printed 58, not 57.** The scan shows 58 (crop `p93_cipher.jpg`), and
so does the IA OCR. "57" comes from Tomokiyo's quotation and went into the catalogue entry from there.

## System

A numeric code or nomenclator. (October text; with the +7 offset the five low figures 32, 33, 54, 55, 58 are single
letters of the two alphabets after all: c, d, a, b, e.) No figure repeats, and the spread runs to 732 with only five
values below 91 (32, 33, 54, 55, 58). The type is the Restoration English one
described on cryptiana `charlesii2.htm`: a short alphabet section plus alphabetically arranged syllables and words
up to about 800, with names after them. Ormond's phrase "a trial whether you are skilful in deciphering" suggests a
test of a cipher Arran held. The sense is that the matter was minor ("else it might have been written in plain
letters"), and Arran's reply of 5 Feb (p. 102) talks of "this cipher ... which is betwixt us".

## Key material tested

1. **Ormond–Arran two-letter code of 1678** (Arran to Ormond, 9 Feb 1677/8, HMC n.s. iv pp. 105-106, with Ormond's
   interlinear equivalents: `hm` D. Bucks, `dk` Court, `io` King, `te` Ld Treasurer, spelled words in `w*`-`z*`
   pairs such as `yn.xo.zc.zz.ws.xl.w't.wn` "despised"). It is a letter-pair code, so the figures here cannot be in it.
   The same pair code is in Southwell's letters (p. 376, 379, per Tomokiyo). **Ruled out.**
2. **Ormond–Longford cipher 1 (1680)** (HMC n.s. v pp. 454 ff., interlinear decipherments; Tomokiyo's
   reconstruction). Two alphabets: 23-46 (a=23, e=27, k=32, l=33) and 47-70 (e=51, h=54, i=55, l=57, m=58, n=59, s=64).
   Above them come syllables and words in alphabetical order to about 840 (be 135, d.. ~204-214, he 338, in 377,
   to 725, the 734, that 736), then names (Sunderland 1063). The positions of 59=n, 64=s and 27=e were checked
   against Longford's 20 Nov 1680 passage (vol. v p. 498, figures `579 446 64 725 566 86 27 552 582 59 ...` = "our
   letters to Ormond are opened ..."). Under this key the five low figures here are single letters: run 1 =
   t.. / a.. / **l** / k.. / a.. / **m** / i.. / **h** / s.. / s..; run 2 = th.. / ou.. / no.. / **k** / re.. / d.. /
   **i** / l... The bare consonants l-k, m-i-h and k-re do not make English words between alphabetical neighbours.
   Tomokiyo's trial, left in an HTML comment on `charlesii2.htm`, gives the same fragments (445 lo-, 342 hi-, 732
   to-the, 214 do-Duke) and he rejected it. **Ruled out** as the key unchanged. A 1678 predecessor of the same type
   with other numbering is possible and cannot be tested without its key.
3. Ormond–Anglesey 1663-64 (vol. iii p. 64 ff., row-block template like DECODE R422) and Ormond–Longford 2 and 3
   (1681-87, vols. vi-vii). **Not rebuilt here.** Their letter ranges (Longford 2: letters 1-56; Longford 3: letters
   mixed into one alphabetical series) and dates make a fit unlikely, but they are untested.

## Prior art

The key: Tomokiyo's reconstruction of Longford 1 (charlesii2.htm), used here with the offset found by McBratney (new by
the contributor's record, `identification/PRIOR_ART.md`). The passage, before 13 Nov 2026: none. HMC prints no gloss. The IA full text of vols. iv-v has no other copy of the passage. Tomokiyo lists it as
unidentified. Cryptoole XX1678-1 is open. Web search on 27 Oct 2026 (the quotation, Ormond + Arran + January 1678 +
cipher) found only the NLI catalogue records. HMC 6th Report App. p. 719 (1877) is a short descriptive list of the
Kilkenny papers and is not expected to print the letter. It was not seen; no scan was found on IA.

## Remaining gaps

- figures 445, 342, 726, 700, 720 (1680 numbers 438, 335, 719, 693, 713) - blocker: no-key-material; no gloss for these
  numbers anywhere in HMC n.s. v, none in Tomokiyo's table. Alphabetical bracketing gives only the section: 438 after
  lo 435 (l-), 335 before h 336 (g-/h-), 693, 713 and 719 among the s- entries.
- figures 58, 54, 32, 440 (1680 numbers 51 e, 47 a, 25 c, 433 le) and 425 (418 King) - blocker: no-key-material; values
  from the key's regular order and from context only; no gloss in print for these numbers.
- whether +7 holds over the rest of the table - blocker: too-short; 20 figures, no repeats, and no other passage in the
  1678 numbering in HMC n.s. iv-v.
- an interlinear or marginal gloss on the sent letter or on Ormond's retained copy - blocker: needs-physical-access;
  NLI MSS 2335-2362 (Ormonde papers 1665-80), letter of 24 Jan 1677/8 in the bundle catalogued as MS UR 006261; not
  digitised. Arran's papers (Bodleian Carte MSS; MS. Carte 50 fols 439-440 reported by cipher-lab as a January 1678
  Ormond-Arran cipher, not seen) may hold the letter as received, perhaps deciphered.

## Escalation

- [x] siblings: every Ormond-Arran letter of Jan-Feb 1678 in HMC n.s. iv read (pp. 92-107); Arran's replies do not
  repeat or answer the figures. The IA text of vols. iv-v scanned for other figure runs: none in the 1678 numbering.
- [x] clear-pages: the clear text of the same letter gives the subject (Douglas, Mansell, Granard) and fits the reading
  ("but it seems to Ormond not credible"); no further crib.
- [x] known-keys: the 1678 two-letter code is ruled out (not numeric); Longford 1 (1680) fits with +7 (13 Nov 2026);
  Longford 2 and 3 tested by the contributor over offsets -150..+150: no fit (max 12/20 and 4/20, no word).
- [x] print: HMC n.s. iv-v (all Longford 1 glosses, pp. 454-498), cryptiana charlesii2.htm. HMC 6th Rept. App. not seen.
- [x] key-rebuild: alphabetical bracketing of the five open numbers gives only their initial sections (Remaining gaps);
  no value can be fixed from 20 figures.
- [x] retry: every figure re-run with the shifted key and Tomokiyo's table as published (14/20) and with the
  contributor's values (15/20); strict 10/20 attested.
- Next step: have NLI MSS 2335-62 searched for the 24 Jan 1677/8 letter (and Carte 50, 216-217 for Arran's copy).
