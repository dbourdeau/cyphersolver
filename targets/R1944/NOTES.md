# DECODE R1944 — Etienne Bourdeaux (Berlin) to Maarten van der Goes, 31 January 1801

Status: read from the contemporary clear copy (misfiled under DECODE R1946); code groups not aligned.

Catalogue 228 (class C). Nationaal Archief, The Hague, 2.01.08 Ministerie van Buitenlandse Zaken 1796–1810,
inv. 257; DECODE R1944 ("Non-decrypted", 2 pp., numerical nomenclator, "likely devised by S. E. Croiset").

## Result

The clear text survives. It was imaged with the wrong DECODE record: the third image of **DECODE R1946**
(Bourdeaux's dispatch of 7 February 1801, `IMG_R1946_I13417_P3.png`) is a clear sheet headed
"Van den Chargé d'aff. Bourdeaux", numbered **N°. 16**, dated **Berlyn 31 January 1801**, and closing
"(get.) Bourdeaux". That is R1944's sender and date. The archive's stamped folio numbers are consecutive:
**294** on the cipher leaf, **295** on the clear sheet. The clear text runs to about 90 words and the cipher
to about 110 three-digit groups with superposed marks, which fits a codebook that has whole-word entries.

Found 20 Sept 2026 while viewing the neighbouring records (R1945, R1946). Checked against the scan 21 Sept 2026.

## Transcription (clear sheet, R1946 image 3, fol. 295)

> N°. 16. Berlyn 31 January 1801.
>
> De Heer van Rosencrantz verzekert de eigentlyke oorzaak van zyn renvoy te ignoreeren. Hy veronderstelt dat
> zyn Cyffer door middel van een bediende is genomen, en gecopieerd geworden, waar door dan zyne Gevoelens zyn
> bekend geworden. — Vry positiever meldt Lusy, dat het bureau, waar in zyn Cyffer was, is geforceerd
> geworden. — Het is om die reden, dat men den Heer Schuer, in N°. 13 gementionneerd, heeft willen naar
> Petersburg zenden om een nieuw Cyffer over te brengen.
>
> (get.) Bourdeaux

An earlier draft (`solution.md` in the shared checkout's `r1944/` folder) read "vertrek" for **renvoy** and
"positiver" for **positiever**. On the scan it is plainly *renvoy* (dismissal).

## Translation

Mr van Rosencrantz assures us that he does not know the real cause of his dismissal. He supposes that his
cipher was taken by a servant and copied, and that his views became known that way. Lusi reports, much more
definitely, that the desk in which his cipher was kept had been forced open. That is why they had wanted
to send Mr Schuer, mentioned in no. 13, to Petersburg to carry a new cipher.

## Context (grade C, not checked in print)

"Rosencrantz" is most likely the Danish diplomat Niels Rosenkrantz, sent away from St Petersburg by Paul I
at the end of 1800. "Lusy" is the Prussian envoy to Russia, Count Spiridon Lusi. "Schuer" is not identified.
So the letter reports a codebook compromised through a servant or a forced desk, and it does so in cipher.

## Open

- The code groups were transcribed with their marks on 14 Nov 2026 (115 groups, see below); they are not aligned
  to the clear text group by group. The key (a Croiset
  numerical nomenclator, per DECODE) is not identified among the DECODE key records.
- Dispatch no. 13, which mentions Schuer, has not been located.

## Files

- Page scans, crops and the draft `solution.md` are in the shared checkout's git-ignored `r1944/` folder.
  They are DECODE images and are not committed.
- `docs/r1944_lead.jpg` and `docs/r1944_cipher.jpg` are the site crops.

## 14 Nov 2026: the code groups transcribed (audit section I, "no transcription file")

- No transcription was in the folder, and DECODE R1944 carries none: its public record page lists two images only,
  and DECODE serves the full-size images only to a logged-in user ("Insufficient permissions").
- The Nationaal Archief publishes its own scans of inv. 257 (601 scans,
  https://www.nationaalarchief.nl/onderzoeken/archief/2.01.08/invnr/257/file ; no login). The originals are bound
  latest first. Scan 420 is no. 19 (7 Feb 1801, DECODE R1946); **scan 432, right page = fol. 294r** (stamp 294), headed
  "N. 16 ... Berlyn den 31 January 1801", seven lines of groups; **scan 433, left page = fol. 294v**, four more lines,
  then "Heil en respect / Bourdeaux"; scan 434, right page, is the clear copy of no. 16.
- Transcribed line by line from the full-size scans (5000 px wide), each group with the mark above it:
  `texts/R1944_transcription.txt`. **115 groups in 11 lines** (measured with `_check_profile.py --measure --digits
  --drop-first`; the "about 110" above was an estimate by eye). Groups are of two or three figures (31, 62, 69, 72, 79,
  97, 21, 29, 58, 61, 91 have two). Marks: double bar, single bar, tick, wavy stroke, two dots, cross, one dot; 17
  groups carry none. Five groups are marked doubtful (`?`). Two short upright strokes stand alone between groups in
  lines 10 and 11.
- A single AI transcription, not checked by a person. There is no key, so it cannot be checked by decoding. What can
  be said: the pair `237: 927+` stands twice (lines 3 and 7) and `927+` a third time at the head of line 11; the clear
  copy has "zyn Cyffer" twice and "een nieuw Cyffer" near the end, at matching places in the text (about a quarter,
  about three fifths, near the end). That makes `927+` = Cyffer and `237:` = zyn likely; no other value is proposed.
- The closing formula on fol. 294v reads "Heil en respect" on the archive's scan.
