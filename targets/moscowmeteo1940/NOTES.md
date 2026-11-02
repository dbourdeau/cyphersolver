# Moscow, 1940: Soviet enciphered weather broadcasts read by the Japanese Army (1938-1940)

Status: read (Brice Dudout, 28 Oct 2026; key tables reconstructed by the Japanese Army Meteorological Department in 1940, transcribed and checked, counted in figures since there are no words: June-July 1940 tables 4,796 figures, 4,793 certain, 0 probable, 3 restored from the cyclic structure, 0 unresolved; worked example of 6 July 1940 60 of 60 figures, all certain; October 1940 grids 218 figures, one figure too many in the odd-day grid not located; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 28-29 Oct 2026. Not in the catalogue: a historical codebreaking file, not an unsolved cipher. Published write-up: https://bdudout.github.io/europe-chiffree/en/meteo-urss-1940.html (site currently offline: the GitHub account is suspended; the write-up is committed and will reappear with it).

## What the documents are

Twelve top-secret reports of the Japanese Army Meteorological Department (陸軍氣象部) to the Vice-Minister and then the Minister of War (Tōjō Hideki, Itagaki Seishirō, Hata Shunroku, Tōjō again), August 1938 - October 1940, held by the National Institute for Defense Studies (防衛研究所), Tokyo, online through JACAR (Japan Center for Asian Historical Records): Ref. C01004558500, C01004559200, C04120597300, C01004559500, C01004816800, C01004816500, C01004816400, C01004816900, C01004816700, C01004832500, C01004832600, C01004818600. Each announces a Soviet key change in the enciphered weather broadcasts (Soviet Far East from 11 Aug 1938, Moscow's European-Russia section from February 1940) and gives the method and key to read it. The JACAR images are "all rights reserved" and are not included; everything here is transcribed.

The plain text under every cipher is the international synoptic report (groups of five figures: station, cloud, weather, wind, pressure, temperature...), and every system subtracts or adds a key figure by figure without carrying. Four generations follow each other (key.tsv has every key):
1. Aug 1938, Far East: groups 1<->3 and 2<->5 exchanged, +3 on every figure (+4 on the station index). Read the same day, 10 hours after it came into service. From Sept 1938 one additive group per broadcast group, changed every 2-4 weeks.
2. Feb 1940, Far East: eleven symbols (0-9 and X), group 1 substituted and then used as running key for the line.
3. Feb-June 1940, Moscow "types" 17040, 05104, 05080, 05188: one indicator figure per group is substituted and fixes the subtractor of the other four. This is the "Russian code" described from the British side by Brian Audric (Met Office IDA unit, 2000); his example deciphers by the same method (decode.py, V3).
4. June-Oct 1940, Moscow: key group aaabb sent in clear; 7 and X exchanged; a 109-figure cycle subtracted from the starting point the key group designates. Two tables at a time (odd and even days in Moscow), changed 10 June, 26 June and 12 Oct 1940. The report of 16 July 1940 encloses the four June tables complete; that of 16 Oct 1940 the two new grids.

## What we did

- Transcribed the method passages of all twelve reports and translated them (reports.md).
- Transcribed the four June-July 1940 tables cell by cell from the photographs (tables_1940.py, tables_jun1940.tsv: 4 tables x 11 rows x 109 figures = 4,796 figures) and the two October grids (tables_oct1940.py, tables_oct1940.tsv). The tables were transcribed and frozen before any check.
- Found the structure the Japanese had exploited: the eleven rows of each table are the same 109-figure cycle, shifted (cycles_109.tsv). The key group only gives a start in the cycle; every station enciphered with another key yields another overlapping fragment, which is how the tables could be rebuilt from a few days of traffic. The October grids are the same thing condensed, one figure per key, the struck-out cell being the one duplicate of 110 keys for 109 positions.
- The figure 0 almost never occurs in any Soviet key of 1938-1940 (once in table 1, consistently on its 11 rows): a 0 would let the plain figure through.

## Validation

- V0, rotation: 0 disagreements on 4,796 figures; 3 figures illegible on the photograph (table 3: row 111 col 99, 2nd figure; row XXX col 11, 11th figure; row XXX col 88, 2nd figure) restored from the structure as 4, 4, 2.
- V1, held-out example: the worked example of the report of 16 July 1940 (two stations received 6 July 1940 04:00 Japan time, key 22244, table 3) is on image 4, the tables on images 6-7. The key stream drawn from our transcribed table equals the stream printed in the report, and the decipherment gives back the report's clear text: 60 of 60 figures.
- V2: the example of Moscow type 17040 (February 1940) is reproduced, 25 of 25; it settles a figure blurred on the photograph (33556).
- V3: Audric's British example of the same system, 25 of 25 with his key.
- No 200-control statistical test is given: we recovered no key ourselves and read no language; the keys are Japanese and were only transcribed and checked against the reports' own examples. No enciphered Soviet broadcast of 1940 was found online (the British files TNA HW 54/4 and HW 40/31 are not digitised), so there is no external test.
- Targeted visual review by Brice Dudout (28 Oct 2026, shapes only): the 5th additive of 12 Nov 1938 is 34235 (first transcribed 34135); the subtractor cell for cipher figure 6 on 29 Apr 1940 is badly stamped, 8 probable, 6 possible; even-day October cells (00,111)=5 and (00,888)=8 confirmed; eight odd-day October cells read "5" all confirmed.

## Count by the 95% rule (in figures)

- June-July 1940 tables: 4,796 figures: 4,793 certain, 0 probable, 3 restored from the cyclic structure, 0 unresolved (100% read in their sense).
- Worked example of 6 July 1940: 60 cipher figures, 60 certain.
- October 1940 grids: 2 x 110 cells, 2 struck out, 218 figures. They cannot be checked by rotation (one figure per key). In the odd-day grid 2 and 5 occur 13 times and 4 only 11 times: one figure is probably misread (a 5 or a 2 for a 4); not located after the visual review. Less secure than June.
- Key list (key.tsv): one cell probable (29 Apr 1940, cipher 6 -> 8).

## Files

- `reports.md`: Japanese method passages, transcribed, with English translations.
- `key.tsv`: every key of 1938-1940 as given in the reports.
- `tables_1940.py`, `tables_jun1940.tsv`: the four June-July tables as read; `tables_oct1940.py`, `tables_oct1940.tsv`: the October grids; `cycles_109.tsv`: the six 109-figure cycles.
- `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`: the worked example of 6 July 1940; `*_17040.*`: the type 17040 example of February 1940. These are the only Soviet cipher texts in the file, deciphered and read as synoptic code. The October 1940 grids (C01004818600) are key material only.
- `decode.py`: V0-V3 above, no dependencies (`python decode.py`).

## Prior work

Searched 28 Oct 2026 (web in Japanese and English): nothing found on the Japanese Army's reading of Soviet weather ciphers, nor any publication of the Moscow tables. The Soviet system of type 3 is known from the British side only (Audric 2000, with key and example, no tables). Still to consult offline: Kotani Ken, Japanese Intelligence in World War II; the official war history (戦史叢書); CINCPAC-CINCPOA Bulletin 5-45 (1945), in which a captured Japanese meteorologist reportedly spoke of Allied weather codes broken; Miyasugi Hiroyasu, "島内志剛日記にみる対ソ通信情報活動", Intelligence 22 (Red Army ciphers, not weather).

## Sources

- JACAR (jacar.go.jp), refs above; example C01004832600 image 4, tables images 6-7 and 9-10; C01004818600 image 2.
- Brian Audric, The Meteorological Office Dunstable and the IDA Unit in World War II, Royal Meteorological Society, Occasional Papers on Meteorological History no. 2, 2000.
- The National Archives, Kew, HW 54/4 "Correspondence on Russian meteorological cyphers" (1939-1940); HW 40/31 "Exploitation of Russian meteorological communications by Axis Powers" (1944-1945) (not consulted).

## Credits

Brice Dudout (dossier, choice of the material, targeted visual review), with Claude (Anthropic) agents for transcription, checking and write-up. The British comparison rests on Brian Audric's paper.
