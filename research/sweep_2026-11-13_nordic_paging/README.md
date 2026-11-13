# Nordic paging sweep, 13 Nov 2026 (cloud session)

Brief: `research/_nov13/BRIEF.md`. Continues `sweep_2026-11-11_riksarkivet_paging`, `_riksarkivet_papers`, `_nordic`.
**Result: 5 rows in `candidates.json` (class A or B/C leads, all Riksarkivet "Skrivelser till konungen" 1133.07), none with a
vetting block**: no printed edition of any of these letters could be opened (see `verify` on each row). Rows are built by `build_candidates.py`.

## Rows

| Row | Shelfmark and images | Seen |
|---|---|---|
| Gustaf Horn, Stettin, 9 Oct and Nov 1630 | 1133.07/15, R0000795 images 78, 79, 122 | bare 2-digit homophonic text with square signs, 79 at 1800 px; DECODE key R4122 (Horn/Banér) may fit |
| "Grubbe" (Lars Grubbe?), Oct 1632, about ten despatches | 1133.07/11, R0000791 images 249-266 | pages of 2-digit cipher; 259/260 are a letter and its "Doublett"; 263 has plaintext letters over the groups; 254, 256, 258, 261 bare |
| Jakob De la Gardie, 26 Mar 1632 | 1133.07/8, R0000783 images 197-199 | four bare passages |
| "Chemnitz", Nuremberg, Nov-Dec 1631 | 1133.07/4, R0000624 images 55-58 | bare passages on 55, 56; the glossed sibling letter is image 57 |
| Johan Banér, 6 Apr 1627 | 1133.07/3, R0000623 images 356-357 | 7 bare passages, about 25 lines |

## Method and coverage (Riksarkivet)

Route as the earlier sweeps (`lbiiif.riksarkivet.se/arkis!<series>_<nnnnn>/full/900,/0/default.jpg` with the sok.riksarkivet.se Referer,
about 1 image a second with three workers, no bot check). `dl.py`/`dlq.sh` download a volume, `top.py` scores every image with the
earlier digit-texture detector (`digi.py`) and prints the 195x130 px windows of the 64 highest scores on one sheet (highest first).
Every sheet was viewed; every suspect leaf was opened at 700-2000 px. Detector limit: it ranks glossed and bare cipher alike and misses
short passages in a page of running script, so a volume "screened" here is screened by its top 64 leaves only (top 40 for R0000621 and
R0000783 in the first pass). `digi2.py`-`digi4.py` are failed alternative detectors (not used for any result).

Volumes downloaded in full and screened (top-64 sheet each), all of 1133.07 unless noted:
R0000621 (A), R0000622 (B), R0000623 (Banér), R0000624 (C), R0000625 (D-E), R0000781/782/783 (J. De la Gardie 1611-32),
R0000784 (Erik Andersson), R0000785 (F: Falkenberg, Magdeburg 1631: cipher passages glossed in part; these are the volume of
lead 1126, not re-listed), R0000791 (G), R0000792 (Gyllenhielm), R0000793 (H-J), R0000794/795 (Horn), R0000806, R0000807 (K-L),
R0000808 (Kniphausen), R0000809 (M-N), R0002220 (Johan Casimir 1613-21), R0002225 (Sa-Sm); 1133.08: R0001366-R0001371
(volumes 1-6, letters to the regency 1623-54 by name A-Ö).
Seen and excluded because glossed (read): 1133.08/4 image 262 (Torstensson to the king, 27 Feb 1645, letters over the groups),
1133.08/6 images 96, 99 (French/German despatches of c. 1645 with the German written between the lines), R0002220 images 4-5, 156, 205
(Johan Casimir 1619, key lists and interlinear decipherment), R0000785 images 100, 106 (glossed), R0000624 image 57.
Not screened (downloads stopped): R0000810 (O-Q), R0002229 (U-Ö), R0002219 (Catharina), R0001382 (Torstensson memorial, printed
in AOSB II:8). Not resolved to images (info.json returns nothing; 8 units, R0001313-R0001322, 1133.07/26-35): not tried here.
Not touched: 1133.01-1133.05 (1521-1609, 20 volumes; images not resolved), Diplomatica (all sheeted 5-6 Nov), Oxenstiernska
samlingen (2 volumes), Kanslikollegium. NAD text search for chiffer terms in digitised units returns only two Krigsarkivet volumes
(SE/KrA/0279/001/A/5 and A/43), unvisited. UD fonds (`Utrikesdepartementet med föregångare`, 368 digitised units, almost all 19th-20th
c.), Ockupationsarkivet från Novgorod (409 volumes, Russian chancery, not looked at) were enumerated (`enum_x.json`, `nad_enum.py`)
and judged unlikely.

Printed editions searched: Handlingar rörande Skandinaviens historia, Kronologiskt register (archive.org handlingarrrand03scangoog
full text): no letter of the five found; Rikskansleren Axel Oxenstiernas skrifter (rikskanslerenax*goog on archive.org) exist but
cover Oxenstierna's own letters, not these writers' letters to the king. No edition of the king's incoming letters 1627-32 was found.
Verified not helpful: DECODE `RecordsList?search=Gardie|Grubbe` (only Chifferklaver key sheets, via broad match).

## Rigsarkivet (Denmark)

`rasearch.py` (soeg.rigsarkivet.dk/api/v1/Search/arkivalier, flaky: retry) and `terms.py`: 40 cipher terms x online/all in Danish and
German (`ra_terms.json`, 457 series). Nothing new that is scanned: the scanned hits are key volumes ("Chiffer 1670-1709", West-Indies
keys, Trankebar keys), the Frederik 1523 item (target `frederik1523`, done) and the Bernstorff estate series
(`Gruppeordnede sager: Bernstorff: Materiale fra A. P. Bernstorffs dødsbo`, 1764-1797, "Chiffernøgler, udaterede": a key, not
enumerated). Unscanned: Lagau 1712 (catalogue), Else Iversdatter Vandal 1626 (catalogue 467), Sehested keys. `dua_online.json` lists the 286 scanned
series of the Departementet for de Udenlandske Anliggender (Sverige: letters 1534-1771, Polen: Depecher, Rusland, Rigsdagen:
Gesandtskabsrelationer 1544-1771 etc.); `ao.py epid` enumerated their units (e.g. 260682-260702, 261507-261511 Sweden: letters 1633-1771,
261470 Spain, 261119 Ostfriesland, 719607 Russia 1641-99, 261890-261903 Polen 1771-93) but only one Swedish unit (261507, every 8th
image of 1-154, Christina to Frederik III: clear letters, no cipher) and one Russia sheet were viewed. Danske Kancelli (672 scanned
series) and Kongehuset (10) were counted, not paged.

## What remains

- 1133.07/26-35 (8 units: Johan Casimir 1622-32, Radziwill-Rosladin, Spens, T, varia) and 1133.01-1133.05: resolve images through the viewer.
- R0000810, R0002229, R0002219; second 64 windows of the big volumes (R0000622, R0000782, R0000791, R0001366-1371).
- Vetting of the five rows: find the edition (Krigshistoriskt arkiv, Styffe, Gustaf II Adolfs skrifter) and run Horn's key R4122
  (`targets/baner1640/key_r4122.json`) over the Horn and Banér groups.
- Rigsarkivet: Swedish letter units 261491-261511 and the Rusland/Polen depecher units, by stride.

Scripts: `nad_enum.py`, `rik.py`, `dl.py`, `dlq.sh`, `top.py`, `digi.py`, `cz.py`, `hi.py`, `dz.py`, `rasearch.py`, `terms.py`, `ao.py`,
`dksheets.py`, `build_candidates.py`. Scratch (images) is outside the repo.
