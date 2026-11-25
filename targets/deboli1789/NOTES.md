# Deboli → Stanisław August, St Petersburg cipher despatches, 1789 (Unsolved Catalogue 418)

Outcome: read in part. 103 of the 106 despatches have their plaintext in the clear series (read from existing
decipherment); the key was rebuilt from eleven aligned pairs and applied to the three despatches that have none
(key recovered based on adjacent plaintext): 25 Mar 95.5%, 14 Dec 89.4%, 10 May 84.8% of cipher groups read as
sense, measured by `read.py`.

AGAD Warszawa, Zbiór Popielów (fonds 12), sygn. 17: "Deboli. 1789 (cyfry)", 106 cipher despatches of Antoni
Augustyn Deboli, Polish envoy at St Petersburg, to King Stanisław August, 2 January - 29 December 1789, k. 2-312
(AGAD's count is 113 pieces, k. 348). Scans on AGAD's own server:
http://agadd2.home.net.pl/metrykalia/12/album/17/index.html, letter list with image links
https://www.agad.gov.pl/inwentarze/ZbPop17.xml.

## Finding 1: the clear series holds the plaintext of 103 of the 106 despatches

ZbPop 419, "Deboli do króla 1789" (105 pieces, album 419 on the same server), is the Polish clear text of the same
despatches: 100 cipher despatches have a clear piece of the same date there (`pairs.tsv`). The clear texts of 22, 25
and 29 December 1789 are misfiled in ZbPop 417 (catalogued as 1788), nos. 114-116, with the January 1790 despatches.
Eleven pairs were transcribed in full and aligned group by group (`align.py`): 6 Jan, 1 May, 12 May, 4, 8, 11, 15,
18, 22, 25, 29 Dec. Each cipher reads as its clear letter from first word to last, at a steady 1.9 cipher groups per
clear word; words left in clear inside the cipher ("vulgo", "Vederemo", "per consequens", "Qui vult finem vult media",
"in statu quo") fall at the matching points of the clear letters. The 15 May pair is the exception: the clear letter
(about 1,780 words) is far longer than its cipher (1,441 groups), so the cipher carries only part of it; it was left
out of the key.

The clear pieces are fair copies in a secretary's hand, signed "Deboli", with the cabinet's reception note ("reçue le
17. / rep."; on 15 Dec "reçue le 26. p. Mr du Hamel"). The sibling sessions on 1790 and 1791 (`targets/deboli1790`,
`targets/deboli1791`, 27 Oct 2026) reached the same pairing for their years independently and read these fair copies
as the King's cabinet's decipherments; the 1782 edition (Zielińska & Danilczyk 2017, introduction p. 11-13) shows the
cabinet deciphering Deboli's letters on separate sheets. deboli1790 checked one 1789 pair (6 Jan) and noted the volume
"closed the same way". Historians already quote this series (Łojek 1962, Rolnik 2025).

## Finding 2: the code, rebuilt from the pairs

A one-part syllabary (nomenclator) of about 2,200 numbered groups, Polish plaintext, dotted number groups, "Sire!" and
the French close in clear.

- Groups stand for letters, syllables, common words (8 do, 895 nie, 1353 się, 1489 tym, 1484 tych, 1681 że, 2004
  będzie, 1216 przez, 560 którzy, 1988 bo) and names and phrases (1182 posła, 1578 WKMci, 551 króla, 1307 Rossya,
  21a deputa-, 2148 currentis).
- Numbering follows the alphabet in two runs: 1 to about 1770 runs a ... z (461 ka, 466 ko, 623 lo, 692 mi, 780 n, 895
  nie, 961 on, 1262 ru, 1559 w, 1560 wa, 1678-1764 z words); 1775-1788 are punctuation; numerals near 1790-1860; a second run
  from about 1870 starts again at a (1873 a, 1900 aby, 1926 ale, 1988 bo, 2004 będzie, 2059 by, 2076-2177 c, cz).
- Punctuation: the whole band 1775-1788 aligns to no letters (about 1,250 occurrences in the transcriptions; 1786 alone
  649, absent on 6 Jan and the commonest group in December). The 1791 decipherment reads 1786 as a comma and 1775 as a
  full stop (deboli1791 reveal), so the band is punctuation; the aligner, which drops punctuation from the clear text,
  treats it as nulls (`seed.tsv`).
- Letters written under a group (355a, 403a/b, 873c, z, e) mark variants; most fall back on the base value. A
  7-shaped first digit with a z under it (7601, 7678) is a marked form of 1601, 1678.
- Framed runs "4000 9933 ... 9933" with groups 2300-3409 (22 and 29 Dec) hold French passages in a separate table:
  the aligner places "quoiqu'il crie avant qu'on l'ecorche", "droit au solide alloit Bartholomée" and "insinuez à Sa
  Majesté le Roi qu'il prenne confiance dans l'Abassadeur relativement à cette affaire d'Alliance" exactly inside
  them. They are not the 1791 "code B" (deboli1791's table has none of their groups). Probably the 1780 "Chiffre
  François Nouveau" (ZbPop 451), not online.
- Probably the "Cyfra polska" sent to Deboli on 8 March 1783 (ZbPop 444), not online. deboli1791's independent table
  for the same code agrees with this key where both have the group, up to accents and syllable boundaries.

`key_pass.tsv` is the key rebuilt on the eleven pairs: 630 anchored groups (aligned at least twice, consistently),
1,736 groups seen. `key_8pairs.tsv` is the eight-pair key used for the control.

## Finding 3: the three despatches with no clear text

| no. | date | k. | groups | read as sense |
|---|---|---|---|---|
| 024 | 25 Mar 1789 | 77 | 288 | 275 (95.5%); cipher addition "Ajouté au Duplicata seul, le 25. Mars" |
| 042 | 10 May 1789 | 138-142v | 4,393 | 3,727 (84.8%) |
| 104 | 14 Dec 1789 | 296-298v | 1,222 | 1,092 (89.4%); 39 clear Polish passages inside the cipher |

All three: 5,094 of 5,903 groups (86.3%). Counted by `read.py` from `reading/*.tsv`: a group counts when its key
value (or a context reading, `reading/*.fix.tsv`) makes sense in place; groups whose key value does not fit were
marked unread by hand on 27-28 Oct 2026.

- 25 March, Postscriptum to the duplicate: Deboli will ask in every letter what Hetman Branicki is doing; Prince
  Nassau-Siegen writes that Branicki is one of the most devoted to Russia; Nassau had no time for the King's answer;
  Russia wants no new war.
- 10 May: Potemkin has left for the army; long talks with Nassau-Siegen on the "bunt" (the Ukrainian rising rumours),
  Branicki, the withdrawal of the Russian commissariats from Poland; a letter of Potemkin to Markov; Stackelberg
  reported "że krol pruski ofiaruie swoią pomoc Polsce"; someone wrote to Potemkin "że WKMci chciałeś Branickiego
  otruć"; the King's policy towards Repnin, the Primate and the bishopric of Kraków; Krzyżanowski; "że to teraz pora,
  aby się Polska podźwignęła, a resztę Panie Boże robi".
- 14 December: Potemkin had his courier tell the Empress he met rudeness and had to fight for horses crossing Poland;
  Russian couriers given escorts "dla bezpiecznieyszego przeiazdu"; Stackelberg's reports against Deboli; Deboli asks
  to be recalled ("Śmiam o tym namienić WKrMci, abyś zawczasu ... kogo na zastąpienie mię destynował in petto"), that
  the letter be burnt, and that the answer come in a separate packet he can decipher himself.

## Method and controls

- `align.py`: beam DP aligning each cipher group with 0-10 letters of the clear text, cost from the alphabetical order
  of known groups, iterated anchors. `decode.py`: key-only decoding with the alphabetical bracket for unknown groups.
  `read.py`: token-level reading with hand overrides (`reading/*.fix.tsv`), counts tokens read.
- Control 1 (failed, 27 Oct): filling unknown groups from a Polish LM inside their alphabetical bracket (`fill.py`).
  Held-out 18 Dec letter, 171 hidden groups: 5-8 exact. Not used for any reading.
- Control 2 (worked, 27 Oct): key from seven pairs without 18 Dec; the 18 Dec cipher decoded blind gets a value for
  95.6% of its groups, and 91.4% of the decoded letters fall in the order of the real clear text.
- Language model: `lang` pl-1790 (pl-gutenberg respelled to 1780s conventions plus the clear despatches), added for
  this target; `lm.norm` fixed to keep Polish ł as l.

## Prior work

- AGAD inventory: "Korespondencja polityczna tajna (pismo cyfrowe) ... Listy zapisane szyfrem"; no decipherment noted
  on ZbPop 17. No interlinear decipherment on the cipher letters (pages sampled across ZbPop 17, 428, 4, 5, 416).
- Zielińska & Danilczyk, Korespondencja polityczna Stanisława Augusta: Augustyn Deboli 1781 (2015), 1782 (2017):
  printed from the cabinet's registers AKP 265/266 (Archiwum Królestwa Polskiego), not from ZbPop. Later years unedited.
- D. Rolnik 2025 (Rocznik Filozoficzny Ignatianum 31/3) and J. Łojek, Misja Debolego w Petersburgu (1962) used the
  clear series. Not on DECODE.
- Sibling sessions of 27 Oct 2026: deboli1790 (closed, deciphered at the time; 6 Jan 1789 pair checked) and deboli1791
  (written up; five pairs aligned, two codes). Neither read the three despatches without a clear text.

## Decrypt audit, 16 Nov 2026

`research/decrypt_audit/` applies `key_pass.tsv` to each transcription and compares the letters with the text the profile
lists for it: 3,704 of 13,121 compared words depart over the fifteen texts (17% to 77% per text). Nothing was changed in the
key, the transcriptions or the readings; the figures after are the same. What the figures mean differs by group of texts.

Twelve paired despatches (c001, c041, c045, c046, c101-c103, c105-c109; 3,062 of 12,122 words, 18% to 31%):

- The text compared is not a reading of this project. It is the archive's clear copy (`clear/*.txt`), the material the key was
  rebuilt from. The figure measures how far `key_pass.tsv`, used alone, regenerates the clear copy.
- `key_pass.tsv` is the aligner's table, not a clean codebook: one row per group seen (1,736), value = the commonest aligned
  string, with the other strings in the `alternatives` column. 644 rows are seen once (1/1); 637 rows meet "twice and 60%"
  (630 after the order check, the figure above). Counted here over the eleven `align_*.txt` files: of 22,171 groups, 81% are
  aligned in place to exactly the key value, 9% to a longer or shorter string holding it (case endings and syllable breaks:
  637 = list 19 times, listu 8, lis 12; 1578 = wkmc 35, wkmci 33; 1307 = rossya, rossyi), 9% to a different string, 1% to nothing.
  Example (6 Jan): key "sekret" + "la" where the clear copy has "Sekretarza".
- c046 (15 May) was never aligned: its clear letter is much longer than the cipher (Finding 1).
- The script also drops every group written with "?" (unsure digit), because it does not strip the mark as `read_cipher` does.

Two line-by-line decodes (c042 10 May, 425 of 550; c104 14 Dec, 190 of 291):

- Audit artefact: each line of `reading/*.decoded.txt` starts with its folio label ("k.138r.01:", "k.138v.01:"); the script reads the
  letters of the label as text ("kr", "ku", 119 of the sampled departures in c042). With the labels stripped in memory the script
  gives 138 of 277 (c042) and 56 of 179 (c104); a "word" there is a whole manuscript line, since the files have no word division.
- The rest is by design. Rebuilt here from `key_pass.tsv`, the `fix.tsv` files and the transcriptions with the rules of `read.py`
  (not run; functions imported), both files come out identical, line for line, and so do the three `reading/*.tsv`. The lines that
  still depart hold one of: a group marked unread by hand although the key has a row for it, printed {group} (c042 565 of 666 open
  groups, c104 95 of 130); a group with "?" in the transcription, valued by `read.py`, dropped by the script (155 and 19 groups); a group
  with a letter under it valued from its base group (31 and 11; the rule is in Finding 2); a context reading in [ ] from `fix.tsv` (5 and 16);
  in c104 the 38 clear passages. The 53 and 44 lines with none of these equal the key output exactly.
- No unmarked emendation in these two files.

The worded reading of 25 March (`reading/c024_1789-03-25.txt`, 27 of 158):

- Six departures are the note "(context)" printed after a context reading; the script takes it for text.
- Word endings chosen without a mark where the key's main value is another form and the chosen form is in its `alternatives`
  column: listu (key list), siebie (sie), Hetman (hetmana), WKMci seven times (wkmc), Rossyi twice (rossya), woyny (woyne),
  życzy (zyc + y). 14 words.
- Letters supplied or changed without a mark and without a row in the key: "na odprawie" (groups give na-pra-wi), "to iest"
  (2407 = ie), "powiedzieć" (pow-dzie-c), "przyszło, że się" (przys-o-ze-s-sie), and a second "na" in "essencyonalna, na ktora"
  (the groups give es-se-n-cy-o-na-l-na once). 5 places. The header of the file says "old spelling as the code gives it".
  They are reported to the audit for a central decision; the file was not changed.

Not checked: the digits of the transcriptions against the images, and the clear copies against the images.

Marked on 16 Nov 2026. In `reading/c024_1789-03-25.txt` 18 words now carry [ ] round the letters the main value of the key
does not give (19 bracket pairs): list[u], ie[st], sie[bie], WKMc[i] seven times, Rossy[i] twice, [od]prawi[e], pow[ie]dzieć,
przys[zł]o, [na], woyn[y], życ[z]y. No letter of the text was changed. Left unmarked, 2 places, because the change is a letter
left out and a mark would need to add it: "Hetman" (key value hetmana) and "że się" (the groups give ze-s-sie); the header
names both. The first report counted these as 14 endings and 5 places; each was checked again against `reading/c024_1789-03-25.tsv`.
Header: one sentence added on [x]. The twelve files in `clear/` each got a second header line saying that the file is the
archive's clear copy, not the output of `key_pass.tsv`, and naming its `align_*.txt` (none for 15 May); nothing inside them
was marked. The folder holds no stored key-only decode of the paired ciphers. Page: one sentence added after "Old spelling is
kept as the code gives it". The audit script now gives 11 of 157 words for c024. `v2_score.py` hole rate for c024: 0.063
before, 0.159 after (a word with a bracketed letter counts as a hole). `read_share` (0.955, counted by groups) was not changed.

## Remaining gaps

- 10 May 1789 (no. 042): 666 of 4,393 groups unread - blocker: open-codes; groups with no value in the eleven pairs or
  whose aligned value does not fit in place, in a hand where 0/8 are hard to tell apart (154 groups transcribed with ?);
  more pairs near May and a second look at the doubtful digits would narrow them.
- 14 Dec 1789 (no. 104): 130 of 1,222 groups unread - blocker: open-codes; same cause, a different hand (1185/1105).
- 25 Mar 1789 (no. 024): 13 of 288 groups unread - blocker: open-codes; 1407, 518, 437, 108, 2140b and fragments that
  do not read, each once.

## Escalation

- [x] siblings: ZbPop 419 and 417 pair with 103 of 106 despatches; eleven pairs aligned. The leaves around nos. 024,
  042, 104 and the clear pieces of the neighbouring dates (24 Mar, 8 and 12 May, 15 Dec) checked: none is their text.
  Not on DECODE.
- [x] clear-pages: c104 carries 39 clear Polish passages, used; c024 is headed "Ajouté au Duplicata seul"; the French
  passages in the 4000/9933 frames of 22 and 29 Dec are in the clear copies.
- [x] known-keys: ZbPop 444, 451, 453/454 not online. deboli1791's code tables (same code) tried on every unread group:
  they agree with this key and added three readings (1586 wiadomość, 48 dość, 1612 wyraż-); code B does not occur.
- [x] print: Zielińska & Danilczyk print 1780-1782 only; 1789 unedited (Rolnik 2025); nothing in print for these three.
- [x] key-rebuild: eleven pairs, 630 anchored groups; alphabetical brackets used for context readings (1175
  Postscriptum, 2161 często, 1287 respons, 2094 czy, 1369 śl, 1711 zal-, 2009 bie).
- [x] retry: every group of the three letters re-read with the eleven-pair key and the 1791 table on 27-28 Oct; LM
  gap-filling tried and failed its control.
