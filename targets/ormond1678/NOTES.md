# Ormond to the Earl of Arran, 24 January 1677/8: a "trial" passage in figures (Unsolved Catalogue no. 353)

Status: key identified: Tomokiyo's reconstruction of Ormond-Longford Cipher 1 shifted by +7; read in part 15/20 figures; holes kept

Attempted 26-27 Oct 2026, not solved. The 20 figures do not fit either Ormond key of these years. The passage is too
short for a ciphertext-only attack on a code of this size. The next step is the manuscript (NLI, Ormonde MSS), which
needs physical access. Cryptoole XX1678-1; Tomokiyo, "An Unidentified Cipher?" on cryptiana `charlesii2.htm`.


## Key identified, 13 Nov 2026 (files in `identification/`)

Every figure is the Ormond-Longford Cipher 1 (1680) number **plus 7**. With Tomokiyo's reconstruction of that key
(Cryptiana `charlesii2.htm`), from the glosses in HMC n.s. v pp.454 ff., the passage reads in part:

> If what he says of [445] and [342] be true, [726] and King are in a [700] [720]; but it seems to Ormond not credible.

Decryption: `[726] an d King ar e in a [700] [720]` / `to Ormond not c re di b le`. English is AI-made.

- 15/20 figures given a value (75.00%): 10 from printed glosses or the p.498 plain rendering, 4 interpolated from the
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

The record of the October attempt follows unchanged, except that "Ruled out" for Longford 1 applies to the key
**unchanged**.

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

A numeric code or nomenclator. Single letters are not among the 18 figures in the runs: no figure repeats, and
the spread runs to 732 with only five values below 91 (32, 33, 54, 55, 58). The type is the Restoration English one
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

None. HMC prints no gloss. The IA full text of vols. iv-v has no other copy of the passage. Tomokiyo lists it as
unidentified. Cryptoole XX1678-1 is open. Web search on 27 Oct 2026 (the quotation, Ormond + Arran + January 1678 +
cipher) found only the NLI catalogue records. HMC 6th Report App. p. 719 (1877) is a short descriptive list of the
Kilkenny papers and is not expected to print the letter. It was not seen; no scan was found on IA.

## Remaining gaps

- All 20 figures - blocker: too-short; 20 distinct figures of a code of about 800 entries. No repeats, so there is
  no pattern for a ciphertext-only attack, and no control at this length could succeed.
- The key - blocker: no-key-material; neither the 1678 pair code nor the 1680 Longford key fits, and no numeric
  Ormond-Arran key of 1677-78 is in print or on DECODE.
- An interlinear or marginal gloss on the sent letter or on Ormond's retained copy - blocker: needs-physical-access;
  NLI MSS 2335-2362 (Ormonde papers 1665-80), letter of 24 Jan 1677/8 in the bundle catalogued as MS UR 006261; not
  digitised. Arran's own papers (Bodleian Carte MSS, e.g. Carte 216-217, NLI microfilm MS UR 076819) may hold the
  letter as received, perhaps deciphered by Arran.

## Escalation

- [x] siblings: every Ormond-Arran letter of Jan-Feb 1678 in HMC n.s. iv read (pp. 92-107). Arran's replies of
  26 and 29 Jan and 5, 9 and 12 Feb do not repeat or answer the figures. The 5 Feb reply puts off deciphering.
- [x] clear-pages: the clear text of the same letter and of Ormond to Arran 29 Jan gives the subject (Douglas,
  Mansell, Granard), not the wording. No usable crib.
- [x] known-keys: the 1678 Ormond-Arran two-letter code is ruled out (not numeric). The Ormond-Longford 1680 key is
  ruled out (low figures fall on single consonants). Anglesey 1663 and Longford 2-3 are untested (see Key material 3).
- [x] print: HMC n.s. iv-v full text and cryptiana charlesii2.htm: nothing. HMC 6th Rept. App. not seen, and not
  expected to print the letter.
- [n/a] key-rebuild: no partial key exists to extend. 20 distinct figures give no repeats to anchor a solver.
- [n/a] retry: nothing reads yet.
- Next step: have NLI MSS 2335-62 searched for the 24 Jan 1677/8 letter (and Carte 216-217 for Arran's copy), and
  look for an interlinear decipherment. A numeric key of 1677-78 among the Ormonde papers would also do.
