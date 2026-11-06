# Riksarkivet consular volumes, full paging (6 Nov 2026)

Source key `riksarkivet_consuls`. Goal: page **every image** of the Swedish consular volumes of Diplomatica Maroccana and
Turcica bihang (Algerica, Tunisica, Tripolitana), which the west sweep (`sweep_2026-11_riksarkivet_west`) and the Turcica
sweep (`sweep_2026-11_riksarkivet_turcica`) had sampled at 15-24 images each, after both found bare digit-string cipher of the
1760s there (Wulff, Salé, lead 2314; Molinari, Tunis, lead 2260). **2 rows** in `candidates.json` (`make_candidates.py`);
the per-volume record is `findings.md`.

## Method

1. `units.json`: 25 volumes, 6,987 images (series ids from the two earlier sweeps' `units.json`): Maroccana II/I-II/X
   (consuls Wulff, Wenström, Wijk), I/I-I/VII (missions 1772-95), VII/b; Algerica 2/2-2/8 (consuls Logie, Brander, Brandell,
   Skjöldebrand, Norderling); Tunisica 7/1 A, 7/1 B, 7/2, 7/3 (Rönling, Ferner, Molinari, Tulin); Tripolitana 6/1, 6/2, 6/7.
   Left out: the Algerian deputation volumes 3/9-3/15, the Tripoli prize commission 6/4-6/6 and the beys' letters 7/4
   (not consular despatches; sheeted by the Turcica sweep).
2. `page_vol.py fetch`: every image at 1200 px into the session scratchpad, one request a second
   (lbiiif with `Referer: https://sok.riksarkivet.se/`; no bot check, no Chrome).
3. `page_vol.py sheets` / `multi`: contact sheets of 30 images at 300 px a tile, contrast-stretched; every sheet viewed.
4. Two detectors on every image, because a few digit lines inside a clear letter do not show at 300 px (Wulff 14, 17, 18,
   22, 24 look like handwriting there): `digitscan.py` (chains of separate digit-size glyphs at an even pitch) and
   `chainscan.py` (long gapless ink rows; written by the Molinari helper). `process.py` runs digitscan; chainscan runs on a folder of cached images.
5. Suspects and detector hits at 800 px (`page_vol.py big`, four to a view); cipher pages cropped at 2400-2600 px
   (`rik_zoom.py`) to look for interlinear decipherment; neighbouring images checked for deciphered copies.
6. Helper agents paged four groups (Algerica 2/2-2/5, 2/7, 2/8; Tunisica 7/1 A, 7/3 and Tripolitana 6/2, 6/7; Molinari's
   Tunisica 7/2; Tripolitana 6/1) from the same cached images and sheets; their image lists are in `findings.md`.
7. `known.py` on every shelfmark and consul: no prior record beyond the sweeps' own files and leads 2260, 2314.

**Limit.** Code groups set singly inside clear sentences (the Algiers 1736 form: underlined 4-digit groups with the word
written above) neither show at 300 px nor trigger the detectors; they were found only on an 800-px view. Volumes seen at
300 px plus detectors (most of them) are clean of digit rows and pages, not proven clean of that form.

## Results

All 25 volumes paged in full. Cipher in five volumes:

| Row | Volume | Images | Decipherment |
|---|---|---|---|
| **new**: consul J. M. Wenström, Salé 1775-76, 3-digit consular code | Maroccana II/II-IX (R0003633) | 13, 15, 16, 18 (= 19), 23, 24, 27 | glossed (class A); groups shared with Wulff's bare string: probable key to lead 2314 |
| **new**: consul George Logie, Algiers 1736, 4-digit code words | Algerica 2/2 (R0002319) | 281, 282, 300 | glossed (class A) |
| lead 2314 (not re-added): consul P. C. Wulff, Salé 1764-65 | Maroccana II/I (R0003632) | new: 17, 22 (bare); known 11-14, 18, 24 | bare |
| lead 2318 (not re-added): A. von Stauden, Morocco 1775 | Maroccana I/I (R0003619) | new: 77, 78 (glossed), **79 (bare block, about 140 groups)**; known 76 | mostly glossed, 79 bare |
| lead 2260 (not re-added): consul J. A. Molinari, Tunis 1764-70 | Tunisica 7/2 (R0003585) | nine letters in 11-176 and 363-366, each in two copies | **every letter has a glossed copy**; two clear-text copies (158r-160l, 177r-182l): the bare pages are duplicates |

What this changes for the existing leads:

- **2260 Molinari**: no longer ciphertext-only. Each of the nine cipher letters survives in an original and a duplicate,
  and at least one copy of each carries an interlinear French decipherment (32 newly found glossed pages); the bare pages
  (120 right-123, 136-138, 143-145, 152-153, 157-158, 176, 365-366 ...) are the undeciphered twins.
- **2314 Wulff**: still bare (17 and 22 added), but Wenström's glossed letters of 1775-76 from the same consulate share
  groups with Wulff's string (`374 507`, `380`) and von Stauden's 1775 rows share the layout: probably one consular code.
- **2318 von Stauden**: image 79 adds a bare block of seven rows to the two bare lines on 76.

## Paged, no cipher seen

Wijk 1787-1809, Maroccana VII/b, the six Moroccan missions 1777-95, Algerica 2/3-2/8 (Logie 1740-57, Brander, Brandell,
Skjöldebrand, Norderling), Tunisica 7/1 A, 7/1 B, 7/3 (Rönling, Ferner, Tulin), Tripolitana 6/1, 6/2, 6/7. Details and the
images viewed at 800 px are in `findings.md`.

## Not reached

- Comparing the glossed Wenström, von Stauden and Molinari group/plaintext pairs with Wulff's bare strings (the test of the
  one-code hypothesis), and reading von Stauden 79.
- Algerica 2/2 images 2-266 and Algerica 2/3-2/4 at 600 px for more of Logie's 1736 code.
- DECODE, Tomokiyo, Lasry and the editions (Jerad's Molinari edition, 2015) were not searched for the two new rows.

## Files

`units.json` (the 25 volumes), `page_vol.py` (fetch, sheets, multi, big), `digitscan.py`, `chainscan.py`, `process.py`
(sheets + digitscan scores per volume), `rik_common.py`, `rik_pick.py`, `rik_zoom.py` (from the west sweep, scratch dir
changed), `make_candidates.py` -> `candidates.json`, `findings.md`. Images and sheets stay in the session scratchpad.
