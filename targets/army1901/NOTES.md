# Japanese General Staff drafts to Fukushima, 1901: grid kana table (catalogue 715; JACAR C09122808300 ff.)

Contributed by Harumi-Matsuba (GitHub issues #371 and #374, 10 Nov 2026; repository
https://github.com/Harumi-Matsuba/kagigo1901-public, commits 7a627e4 and 9d53bd6; code MIT, documents and data CC BY 4.0).
Integrated and checked here 10 Nov 2026. Catalogue entry 715 (JACAR sweep, Oct 2026). Page: `docs/army1901.html`.
Outside the LLM paper's scope (Japanese; contributed). Sister target with a different table: `targets/army1902/`.

## The documents

Five drafts of telegrams from the Army General Staff in Tokyo (Maj.-Gen. Tamura) to Maj.-Gen. Fukushima in Peking, Feb-May 1901,
in the National Institute for Defense Studies (NIDS) file 参謀本部 雑, 自明治34年1月5日至同年6月29日 通報綴, viewed by the
contributor on JACAR:

| JACAR | frames | date | pairs | in table | counted as read |
|---|---|---|---|---|---|
| C09122808300 | 0306-0307 | Feb 1901, undated | 11 | 11 | 10 |
| C09122808400 | 0308-0309 | 14 Feb 1901, No. 21 | 15 | 15 | 15 |
| C09122809400 | 0331-0332 | 2 Mar 1901 | 59 | 52 | 48 |
| C09122810100 | 0348-0350 | 8 Mar 1901 | 42 | 40 | 37 |
| C09122812300 | 0412-0414 | 1 May 1901 | 21 | 20 | 20 |
| total | | | 148 | 138 | 130 (87.8%) |

Each draft is romanised Japanese in clear with the sensitive words in digits: two digits per kana, written in groups of five,
so the last group of a run is short. All 23 digit runs have even length (checked here). The catalogue entry took the
Latin strings for enciphered romaji; they are plain romaji, garbled in JACAR's record text (contributor, #371).

## The key (contributor, #374)

A grid: tens digit = vowel row, units digit = consonant column. Lower half 01-50 (tens 0-4 = a i u e o; units 1 vowel, 2 k,
3 g, 4 s, 5 z, 6 t, 7 d, 8 n, 9 h, 0 b with b at 10-50); upper half 51-95 (tens 5-9 = a-o; units 1 p, 2 m, 3 y, 4 r;
55 = ワ, 65 = ン). ヲ sent as オ. `texts/key.md`.

How it was found: no contemporary translation of these drafts exists in the file. From the clear romaji after the digits,
`48456 241 mitasigatasi` taken as ノゾミヲ (望ミヲ充タシ難シ) gave spacings ノ-ゾ = 3, ゾ-オ = 4; then `41411 45248 kotowa`
= オオシマノ and `64422 11493` (third pair = sixth pair) = リコウシヨウ. These three words (13 values) and the grid rule fix
the table; the rest came out of it. Method category: key recovered from ciphertext-only, with cribs guessed from the clear
romaji of the same drafts (adjacent plaintext): recorded as "key recovered based on adjacent plaintext".

Not the 1901 incoming table of issue #371 (serial 00-67, ア00 カ01 ガ02 ...; rebuilt by the contributor from five telegrams
of officers in China whose translations were filed with them, then applied to C09122796200 16/16 and in part to
C09122806100). That table was tried on these drafts: 21 of 148 pairs fall outside its range and the rest give no words
(`decode.py`, right-hand column). A different key: by the one-key rule it is not part of this target (see Remaining gaps).

## Checks made here (10 Nov 2026)

- `decode.py` written from the stated rule only (does not import the contributor's code). Over the first transcription
  `ct_outgoing1901.txt` (copied from the contributor's `data/outgoing1901.txt`): 23 runs, 0 odd, 148 pairs, 136 in the
  table (`decode_out.txt`). The contributor's four re-read digits bring it to 138 in the table with 29->21 and 27->21,
  both also read so by the blind second reader; 96->16 and 98->93 are not confirmed and give 〔チ〕 and 〔ヨ〕 only. Every
  kana string agrees with the contributor's `outgoing1901.tsv`.
- The names that come out unforced are historical and fit the dates: リコウシヨウ (Li Hongzhang), テウシドウ (Zhang Zhidong),
  セイアン (Xi'an), コウシウワン (Kiaochow Bay), ゲンスイ (the Field Marshal), ヒメジ, クスノセ, シバ, オオシマ, カミオ. Against
  Fukushima's own telegrams read with the #371 table (C09122801000, 22 Apr 1901: the Field Marshal permitted to go to Japan;
  C09122805900, 25 Feb: Shiba to leave early next month), per the contributor; not re-checked here.
- JACAR could not be reached from this session (proxy refused www.jacar.archives.go.jp), so no digit was checked against the
  images here, and no crop is shown. The contributor's figures: second reader (OpenAI Codex, blind, from images) digit
  agreement 285/296; C09122809400 by pairs 53/59. Control (contributor): kana covered by JMdict words of 3+ kana, real
  table 58, 1,000 permuted grids max 37, 1,000 random reassignments max 36. Not re-run here (no Japanese word list in lang/).
- Prior work: contributor's search of 10 Nov 2026 (Cryptiana meijiarmy.htm, meijiarmy2.htm, unsolved.htm and blog; this
  repository; GitHub; web, Japanese and English) found none. Not checked: NDL Search, CiNii, J-STAGE, 日本外交文書 vol. 34.
  No human has compared the images with the transcription (contributor).

## Reading (contributor's, kana reproduced here)

Per document in `texts/<JACAR>_reading.md` and `_en.md`. C09122808400 and C09122812300 read in full; C09122808300,
C09122809400 and C09122810100 in part. In brief: Kamio is not permitted (something) and will be sent to Himeji; Ōshima under
discussion, otherwise Kusunose, Shiba to be sent back; Li Hongzhang's reply to Japanese advice against a secret agreement,
Zhang Zhidong's request that the treaty not come into being, a telegram from Xi'an; the Field Marshal (Waldersee, per the
contributor) wishes to visit Japan from Kiaochow Bay; someone to return home, the number of relief troops undecided.

## Remaining gaps
- values 59, 60, 80, 89, 99 (ten occurrences in C09122809400, C09122810100, C09122812300) - blocker: no-key-material; outside the grid, apparently word codes; no code list found, and contexts only suggest (Russia, China, Germany, minister) without confirming
- C09122809400 first group (99506 or 77306), 22652 (マ vs ヤ for 密約), re-read digits 43962/43162 and 16598/16593 - blocker: illegible; the blind second reader and the first transcription disagree, and JACAR was not reachable from this session to look again
- C09122810100 09626 (ミ vs マ for 漫遊) and 〔モチ〕 (92 16); C09122808300 〔ケ〕コウ (32) - blocker: illegible; the images, per the contributor, show these digits; drafter's slip or misreading cannot be settled without the originals at NIDS
- the rest of the 通報綴 after C09122810000 (only C09122810100 and C09122812300 viewed) - blocker: needs-physical-access; JACAR unreachable from this session (proxy), so the sibling items could not be opened here
- C09122806100 (18 Feb 1901, incoming) values 69 and 91 - blocker: no-key-material; outside the #371 incoming table, which reads the rest of it; a different key from this target's, to go with a separate #371 target not created in this session

## Escalation
- [x] siblings: contributor viewed C09122807700-C09122809900 (22 items, 53 frames) of the same file; only 808300 and 808400 carry digits; the incoming telegrams of the same months use the #371 table
- [x] clear-pages: no Japanese draft or translation of the five found in the viewed items; the clear romaji around the digits supplied the cribs
- [x] known-keys: the #371 incoming table and the 1902-04 table of army1902 tried; neither reads these drafts (decode.py)
- [x] print: contributor's prior-work list (PRIOR_CHECK.en.md); Cryptiana pages; nothing found
- [x] key-rebuild: table fixed by the grid rule from 13 cribbed values; the five off-grid values tried against context only
- [x] retry: every doubtful digit re-read by the contributor and judged blind by Codex; the four re-reads kept apart, two confirmed

## Files
- `ct_outgoing1901.txt`: first transcription, digits and romaji (contributor's `data/outgoing1901.txt`, CC BY 4.0)
- `decode.py`, `decode_out.txt`: independent decoder and its output (grid table; #371 table beside it)
- `texts/<JACAR>_reading.md`, `_en.md`, `texts/key.md`
