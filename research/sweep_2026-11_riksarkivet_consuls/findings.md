# Findings, volume by volume (6 Nov 2026)

Method: every image of each volume fetched at 1200 px (`page_vol.py fetch`, about one request a second); contact sheets of
30 at 300 px a tile, contrast-stretched (`page_vol.py sheets` / `multi`); every image scored by two detectors
(`digitscan.py`: runs of separate digit-size glyphs; `chainscan.py`: long gapless ink rows, written by the Molinari helper);
sheet suspects and detector hits viewed at 800 px (`page_vol.py big`, four to a view); cipher pages cropped at 2400-2600 px
(`rik_zoom.py`) to decide glossed vs bare. Four groups of volumes were paged by helper agents working on the same cached
images and sheets (Algerica 2/2-2/5, 2/7, 2/8; Tunisica 7/1 A, 7/3 and Tripolitana 6/2, 6/7; Tunisica 7/2 Molinari;
Tripolitana 6/1); their verdicts are recorded as reported, with the images they viewed.

**Limit.** Digit rows and pages of digits show on the 300-px sheets and in the detectors. Short code groups set inside a
clear sentence (the 1736 Algiers form: underlined 4-digit groups with the word written above) do not: neither detector
scores them and they look like handwriting at 300 px. Volumes seen only on the sheets and through the detectors may still
hide that form.

## Cipher found (new rows)

| Volume | Series id | Images | Paged | Verdict |
|---|---|---|---|---|
| Maroccana II/II-IX consul general Johan Magnus Wenström (Salé, later Tangier) 1775-87 | R0003633 | 281 | all 281 on sheets; 13-28 at 800 px; 13, 15, 16, 24 at 2600 px | **cipher, glossed**: Swedish letters to the Kanslipresident / Kanslikollegium with rows of 3-digit groups (commas between groups: `212,380,514,135,531,274,178...`). The decipherment is written above each digit row (13: `sjö vid flera tillfällen nog orsakt igenom dess djerfhet` over `406658430188...`); on 23, 24 and 27 the digit rows are struck through with heavy strokes after decipherment, leaving the clear text between them. Cipher at 13 (Salé 6 Nov 1775), 15, 16 (6 Nov 1775), 18 (= 19, a second exposure; Salé 20 Feb 1776), 23, 24, 27 (Salé 15 May 1776). None after May 1776 (28-281 clear on the sheets; detector hits 15-19, and clear pages 110-111, 127, 150 checked at 800 px). **Probably the same code as Wulff's**: Wulff's bare string `4471683745073806223843` (lead 2314) splits as `447 168 374 507 380 622 384`, and `374,507`, `212,380` and `380` recur in Wenström's glossed rows (13, 15, 16): Wenström's glossed letters look like key material for Wulff's bare cipher |
| Algerica 2/2 consul Georg Logie 1729-39 (helper) | R0002319 | 526 | all on sheets; 267-526 again at 600 px; about 40 images at 800 px; 281, 282, 300 at 2600 px | **code, glossed**: 281-282, letter signed George Logie, Algiers 24 May 1736 (signature on 283): 4-digit groups (1000-1999) set in Swedish sentences for the key words, each group underlined with the plain word written above (`Signaler 1557.1126.1255.1655.1062`, `Deyen 1233`, `Amiralen 1675.1324.1705.1655`, `Algierisk 1443.1657`, `Caparen 1311.1110.1712`); words appear to be spelled with several groups (syllables or a small nomenclator). 300: a second letter of June-July 1736 (docket on 299: No. 162, 12 July 1736) speaking of "Consuln Logie" in the third person, probably by the secretary; same code (`Deyen 1233`, `Turcar 1297`, `Levanten 1259`, `Tractat 1584`, `Sverige 1531`), glossed. No key in the volume. Images 2-266 seen only at 300 px |

## New image numbers for existing leads (not re-added)

| Volume | Series id | Images | Paged | Verdict |
|---|---|---|---|---|
| Maroccana II/I consul Peter Christian Wulff at Salé 1764-75 (**lead 2314**) | R0003632 | 167 | all 167 on sheets; 15-24, 31, 32, 37, 43, 105, 112, 113, 153 at 800 px | **new cipher images 17 and 22** (besides 11, 12, 13, 14, 18, 24). 17 (left page): two blocks of digit lines inside the letter (`4471...` again before `presenterne af penningar för belopp af`); 22: one digit line at the foot of the left page, two and a half at the head of the right page. Both bare at 800 px. Dates: 15 = Salé 15 June 1765, 19-20 = 20 July 1765, 21 = 21 Dec 1765: the cipher runs 1764-65 only. No cipher after 24 (105 accounts, 153 a French translation of a passport). See Wenström above for probable key material |
| Maroccana I/I lieutenant colonel Abraham von Stauden 1772-75 (**lead 2318**) | R0003619 | 103 | all 103 on sheets; 75, 77, 78, 79 at 800 px; 79 at 2600 px | **new cipher images 77, 78, 79** (besides 76). 77: a row and a half of digits at the foot of the right page, decipherment between (`Deße senste ...`); 78: both pages, digit rows alternating with the decipherment; 79 (Mequinez 18 July 1775, left page): seven digit rows under the heading `Konge Maj:t` with **no decipherment**, each row set off by a wavy rule (the marking of the two bare lines on 76), about 140 groups. Groups 3-digit, comma-separated (`202,374,525,340,431,457,180,139,614...`), the layout of Wenström's code; `374` and `447` also occur in Wulff's string |
| Tunisica 7/2 consul J. A. Molinari 1764-78 (**lead 2260**; helper) | R0003585 | 732 | all on sheets; about 120 images at 800 px; 108, 364 at 2600 px | **Every cipher letter has a deciphered copy.** Nine letters, each sent twice (original and `Dupl.`); in each pair at least one copy carries an interlinear French decipherment in a second hand, the digit stream divided by commas into mostly 3-digit groups (108: `de joye, et je remercie très humblement Votre Excellence ...`). Letters and images (glossed in bold, the rest bare): 6 Sept 1764 **11, 12** / Dupl. 15, 16; 22 Jan 1765 **62** / Dupl. **64**; 9 Feb 1765 **70, 71** / Dupl. **77** (first rows; rest bare), 78; 22 Feb 1765 **107-110** / Dupl. **111-114**; 21 Mar 1765 **116-119** / Dupl. **120 left**, 120 right, 121-123; 18 Apr 1765 **132-134** / 136, 137, 138; 20 May 1765 **139-141** / Dupl. 143-145; 8 June 1765 **149, 150** / Dupl. 152, 153; 14 June 1765 **155, 156** / 157, 158; 8 July 1765 **172** / Dupl. 176; 7 July 1770 Dupl. **363, 364** / 365, 366 (hence the note `Dubbletten dechifferad` on 365). Clear-text `Copie` of two letters: 158 right-160 left (No 653, 14 June 1765) and 177 right-182 left (No 264, 8 July 1765). Nothing after 183 is cipher. New relative to the lead: 11, 12, 15, 16, 62, 64, 70, 71, 77, 78, 107-114, 116-119, 121, 132-134, 136, 137, 139-141, 143, 145, 149, 150, 155-157, 172, 363, 364, the row on 365, and the two copies. **The bare pages are duplicates of glossed letters**, so the lead's "bare cipher" no longer holds |

## Paged, no cipher seen

| Volume | Series id | Images | Paged | Verdict |
|---|---|---|---|---|
| Maroccana II/X consul general Peter Wijk at Tangier 1787-1809 | R0003634 | 306 | all on sheets | no cipher seen (Swedish despatches; `Underdånig rapport` fair copies 1802-08 to the King's cabinet for foreign correspondence) |
| Maroccana VII/b letters from and to missions and consuls 1766-98 | R0003642 | 210 | all on sheets; 198 at 800 px | no cipher seen (Wulff's and Brander's accounts 1766-72, Kanslikollegium registry copies 109-170, present lists; 198 is Wenström's 1777 table of presents) |
| Maroccana I/II-I/VII missions: Strömfelt 1777, Kullenberg 1777-81, Ankarloo 1779-80, af Christiernin 1782-87, von Rosenstein 1785/1791, Lagerstråle 1795 | R0003620-R0003625 | 75, 36, 45, 87, 31, 12 | all 286 on sheets; R0003623 10, 43, 57, R0003624 4, R0003620 8 at 800 px | no cipher seen |
| Algerica 2/6 consul Henric Brandell 1766-92 | R0002323 | 536 | all on sheets (151-536 without the gamma stretch, the hand being heavy); 77, 242, 394, 427 at 800 px | no cipher seen (dense Swedish, French news sheets, accounts; 427 is a struck-out 1788 notice in clear) |
| Tunisica 7/1 B consul Ferner 1760-67 | R0003580 | 92 | all on sheets; 14, 39-41, 62, 64-66 at 800 px | no cipher seen (Swedish letters 1763-66, clear) |
| Tripolitana 6/1 consuls 1740-79 (helper) | R0003591 | 528 | all on sheets; 89 images at 800 px (every detector hit and a sample of each writer's letters) | no cipher seen. Writers: Isaac Bergh 1740-42 (3-25), J. G. Lillienberg 1743, consul Wijnbergh 1744-59 (30-287, with captain G. Strand's despatches 1745-46 at 80-108), Christian Bagge 1759-72 (288-363), Johan Gabriel Burgman 1772-78 (364-491), Richard Tully, British chargé, 1778-79 (492-527) |
| Algerica 2/5 consul Erik Brander 1758-65 (helper) | R0002322 | 225 | all on sheets; 84, 114, 141, 186, 213, 214, 220 at 800 px | no cipher seen |
| Algerica 2/7 Mathias Skjöldebrand 1792-1802 (helper) | R0002324 | 447 | all on sheets; 84, 87, 132, 283 at 800 px | no cipher seen |
| Algerica 2/8 Johan Norderling 1802-08 (helper) | R0002325 | 171 | all on sheets; 36 detector hits and 12 at 800 px | no cipher seen |
| Algerica 2/4 Logie 1748-57 (helper) | R0002321 | 373 | all on sheets; 78, 273, 303, 328 and 12 others at 800 px | no cipher seen (Pro Memoria, printed passes, accounts) |
| Algerica 2/3 Logie 1740-47 (helper) | R0002320 | 489 | all on sheets; 26 images at 800 px | no cipher seen; the 1736 code form could hide here at 300 px |
| Tunisica 7/3 consul Tulin 1779-1808 (helper) | R0003586 | 704 | all on sheets; 36 images at 800 px | no cipher seen (Swedish despatches with French, English, Italian enclosures; Molinari's widow's declaration 1780 at 112; dash marks on 296-300 are not cancelled cipher) |
| Tripolitana 6/2 consuls 1779-1802 (helper) | R0003607 | 370 | all on sheets; 20 images at 800 px | no cipher seen (Widell, Andelöwer, Burström) |
| Tunisica 7/1 A consul Rönling 1736-60 (helper) | R0003579 | 279 | all on sheets; 8 images at 800 px | no cipher seen (112: merchants' bale marks) |
| Tripolitana 6/7 papers on the Barbary states 1663-1801 (helper) | R0003616 | 162 | all on sheets; 8 images at 800 px | no cipher seen (a printed Dutch regulation of 1658 and a treaty of 1724-30 explain the detector hits) |

## Notes

- known.py (6 Nov) on `2112/II`, `2112/II/II`, `R0003633`, `Wenström`, `Peter Wijk`, `2119.2/2/2`, `R0002319`, `Logie`,
  `Gladda`, `Algerica 2/2`, `Brandell`, `Tulin`, `Skjöldebrand`, `Norderling`, `Erik Brander`, `Ferner`, `Rönling`,
  `2119.6`, `2119.7`, `Tripolitana`, `Algerica`, `Tunisica`, `Maroccana`: hits only on this sweep's and the earlier
  Riksarkivet sweeps' own files, on leads 2260 and 2314, and a leads.json mention of George Logie as background to the
  1763 treaty. No catalogue, DECODE or target hit.
- Wulff, von Stauden and Wenström share one layout (3-digit groups 100-799, comma-separated or run together) over 1764-76
  in Morocco; Molinari's Tunis stream (1764-70) is divided by its decipherer into mostly 3-digit groups. Comparing the
  glossed Wenström, von Stauden and Molinari groups with Wulff's bare strings is the obvious next step: if this is one
  consular code, Wulff's and von Stauden's bare passages can be read from the glossed pairs.
