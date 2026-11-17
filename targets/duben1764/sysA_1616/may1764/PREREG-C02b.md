# PREREG-C02b — key_c02, unchanged, on the 15/4 May 1764 letter (Chiffer n:o 1, system A)

Written 17 Nov 2026 (evening), Brice Dudout's session (Claude Opus 5.5, AI agent), BEFORE any transcription in this session
of the cipher 105R-108L or of the clear 106R-107L, and before any decoding of either. Frozen by SHA-256 (`SHA256SUMS-PREREG`).
Any later change goes into a dated amendment below, never into this text.

## Why a second test
key_c02 failed its first pre-registered test (20/31 Aug 1764, `../aug1764/`): CA 0.831 at a 0.85 bar. That PREREG fixed the
binding order of the cipher pages, and the text order was different. This test uses a portion never measured, and fixes the
reading order BEFORE transcription from material evidence only (below). The August portion stays burnt.

## Key (unchanged)
`../keyc02/key_c02.json`, SHA-256 `1813621c87e836f3b20610b544239e892726b419ea5a02fc9ff71fa768b87285` (324 groups, 306 with a
value), the file frozen in `../aug1764/PREREG.md`. Nothing is added, removed or corrected. Its sources (letter 96 + 100R,
6 Mar 1764, 15 June 1764 108R-109L, 15 Nov 1765, 90R-93L) contain no group or text of images 104-107 or of 108L.

## Material
- Cipher: the number lines of the letter headed "ce 15/4 de May 1764. Mon cher Comte," (105R), on 105R, 106L, 107R and the
  first line of 108L (Riksarkivet K 259, IIIF A0073297_00105-00108). Not 104R-105L (another letter, ending on 105L with a
  Swedish clear paragraph), not the clear paragraph and signature of 108L, not 108R (15 June 1764).
- Clear: the contemporary decipherment on 106R + 107L (archival note "Till chifferbrevet av den 15/4 maj 1764"), all of its
  text as written. Extra text in the clear does not lower CA.

## Prior state (checked 17 Nov 2026 before this file)
- Repository (origin/main ae96e5159, PR branch cfa8717bc): `payne2026/may1764_cipher.txt` (Bryan Payne / Codex, 28 Oct 2026,
  PR #185) is a one-pass preliminary transcription of this cipher (870 groups, 33 doubtful). It was compared only with the
  tables 218-220 ("no accepted French"); it was never decoded with key_c01 or key_c02 and never measured against the clear.
  The clear 106R-107L has never been transcribed (Payne: "clear portions remain untranscribed"). No other PR, issue or fork
  branch (all authors) touches this letter. Our own files: no decode of 105-108L with any key (only a frequency-profile
  cosine on Payne's file, 13 Nov, to class it as system A).
- Payne's transcription is NOT used as a pass: both passes are new. (Its first 17 lines were seen in a terminal listing during
  the prior-state check; the blind pass 2 never sees it.)

## Reading order — fixed now, from material criteria only (reduced images at 500 px and crops of the cipher pages; the clear
## pages 106R and 107L were not read)
1. 105R opens the letter: date "ce 15/4 de May 1764" and salutation "Mon cher Comte," above the first number line.
2. 105R and 106L are recto and verso of ONE leaf: the header of 105R ("ce 15/4 de May 1764", "Mon cher Comte") shows through,
   mirrored, at the top of 106L.
3. 107R and 108L are recto and verso of ONE leaf: the first number line of 107R ("448.6.361...") shows through, mirrored, on 108L.
4. 108L ends the letter: one number line, then a clear paragraph in the writer's hand ending in the subscription and paraph.
5. The leaf 106R/107L between them is the decipherer's clear, in another hand (bound inside the letter).
Two cipher leaves, the first with the opening, the second with the end: the order is **105R -> 106L -> 107R -> 108L(line 1)**,
lines top to bottom on each page. No page numbers or catchwords are used or needed. Transcription files follow this order.

## Preconditions (checked on the transcription counts, no decoding)
1. The cipher has at least 300 groups of 100 or above and the clear at least 300 letters.
2. Correspondence rule (as Amendment 1 of `../aug1764/PREREG.md`): r = letters of the normalised clear / groups >= 100 of the
   cipher must lie in 1.8 <= r <= 2.8 (training letters with a complete clear: 2.17-2.37). If r is outside, the measure is NOT
   run, the portion is not burnt, and this is reported.
3. The numbers are system A (groups 1-~790, nulls below 100).

## Transcription (before decoding)
Pass 1 by this session; pass 2 by a blind sub-agent that sees neither pass 1, nor Payne's file, nor any key, nor this file.
Differences arbitrated on zooms of the full-size image; doubtful groups keep the arbitrated reading with "?". Groups are
written as the image shows (the scribe's open 3 is read as 3; no normalisation). Struck groups as [del:..]. The clear is
transcribed in two passes the same way. Both merged files are hashed in an amendment BEFORE the measure is run.

## The one measure
`scripts/measure_may.py` (frozen here; same code as `../aug1764/scripts/measure_aug.py`, seed changed, one reported-only
figure added), run ONCE:
`python3 -I scripts/measure_may.py ../keyc02/key_c02.json transcr/may1764_cipher_merged.txt transcr/may1764_clear_106R-107L.txt`
- decode every group >= 100 with the first value of key_c02 (unknown group or empty value -> nothing), in the order above;
- **CA** (decision metric) = share of the DECODED letters in difflib matching blocks of >= 4 letters between the decode and the
  normalised clear (a-z, accents stripped);
- 200 controls: random permutations of the non-empty values over the groups that have one, `random.seed(17640515)`;
- reported only, not decisive: M (share of clear letters covered) and CA_pagewise (each page aligned to the clear on its own,
  independent of page order).

## Threshold (fixed now)
**PASS** if CA >= 0.85 AND CA >= (max of the 200 controls) + 0.30. **FAIL** otherwise; a fail is reported as a fail.
Known before this file: key_c02 in-sample CA 0.83-0.97; held-out August CA 0.831 in binding order (0.938 in text order, after
the result, not a test). A pass is not assured.

## After the measure (not part of the test)
The portion (cipher 105R-108L line 1 and clear 106R-107L) is burnt for any later key test. Reading of the letter is from its
contemporary clear (existing decipherment): strict count by Daniel's rule (">= 95 % of words SURE" = read; probable words
and holes do not count as sure).
