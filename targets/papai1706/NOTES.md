# János Pápai (Constantinople) to Ferenc Rákóczi II, 1706–1710, in the envoy key R580 — DECODE R740, R741, R757, R765, R784, R793–R796, R805, R823

Status: read — the eleven numeric letters read with the envoy's own key (second pass: 16,641 of 16,698 numeric
groups, 99.7%; 16,641 of ~16,739 with DECODE's '?' tokens, 99.4%); the open groups are DECODE transcription slips.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. R731 (6 Mar 1710,
Belgrade), whose six passages are in a graphic-sign alphabet, is a different cipher, with its own page
([`targets/papai1710/`](../papai1710/), docs/papai1710.html); `R731_signs.txt` and `solve731.py` moved there
(`retry_groups.py` imports `solve731.py` from there). On the eleven numeric letters alone the read bar is met, so this
entry is now read (it was read in part only because of R731).

Catalogue entry 46 (class B, scored by rule). Worked 21 Sept 2026. Archive images are not in the public domain
(DECODE: publishing only with the archive's permission); they are kept git-ignored in `img/`, and only derived text is
committed.

## The documents

| Record | Shelfmark (MNL OL G15) | Date, place | Cipher | Groups | In key |
|---|---|---|---|---|---|
| R805 | Caps. C Fasc. 33, pp. 34–37 | 1 May 1706, Constantinople (signed Pápai János, Horváth Ferenc) | numeric, R580 key | 336 | 336 (100%) |
| R795 | Caps. C Fasc. 36, pp. 18–21 (item 1) | 1 Jan 1706, Constantinople (*die prima Januarii*), signed Pápai János | numeric, R580 key, groups above 322 are nulls | 1,617 | 1,356 + 251 nulls (99.1%) |
| R796 | Caps. C Fasc. 36 (item 2) | 20 Feb 1706, Constantinople, Pápai | numeric, R580 key | 1,025 | 1,004 + 16 (99.5%) |
| R793 | Caps. C Fasc. 36 (item 2) | 1?–19 Mar 1706 (*tizen·todik Martius*), Pápai | numeric, R580 key | 1,226 | 1,194 + 24 (99.3%) |
| R794 | Caps. C Fasc. 36 (item 2) | undated, early 1706 | numeric, R580 key | 1,175 | 1,152 + 15 (99.3%) |
| R823 | Caps. C Fasc. 33, pp. 140–143 | 19 Dec 1706, Constantinople (Pápai, Horváth) | numeric, R580 key | 1,632 | 1,609 (98.6%) |
| R765 | Caps. E Fasc. 80, pp. 2–11 | 5 Jan 1707 (DECODE origin "Balar") | numeric, R580 key | 4,864 | 4,787 (98.4%) |
| R784 | Caps. D Fasc. 80, pp. 110–111 | undated (DECODE 1707), unsigned; cover note in another hand | numeric, R580 key | 594 | 587 (98.8%) |
| R757 | Caps. E Fasc. 109, pp. 85–90 | 16 May 1708 (DECODE origin "Balar") | numeric, R580 key | 2,758 | 2,695 (97.7%) |
| R740 | Caps. H Fasc. 226, pp. 85–88 | 2 Jan 1710, Constantinople | numeric, R580 key (one passage, p. 2–3) | 168 | 168 (100%) |
| R741 | Caps. H Fasc. 226, pp. 89–96 | 8 May 1710, Constantinople | numeric, R580 key | 1,466 | 1,458 (99.5%) |
| R731 | Caps. H Fasc. 226, pp. 31–33 | 6 Mar 1710, Landor Fejérvár (Belgrade), signed *Pápai János* | graphic-sign substitution, six short passages (split off 14 Oct 2026: papai1710) | — | — |

Group counts are what `decode.py` parses from the DECODE transcriptions (R740: transcribed here from the images,
`R740_transcription.txt`). "In key" groups are those with a value in the key; the rest are digit slips in the
transcription, clear numerals (R823 opens with 400–1000 figures that are sums, not cipher) or joined groups.
Total: 11,640 of 11,818 groups (98.5%).

R793–R796 (catalogue 47, "Constantinpole envoys to Ferenc Rákóczi II, 2 ciphertexts", added 21 Sept 2026): DECODE
lists them as "partially decrypted" because the transcriber copied the contemporary interlinear decipherment, which
covers only parts of the lines. They are four despatches, not two. The same key reads all four unchanged: 4,706 of
5,043 groups have a table value, 306 more are groups above 322, which the interlinear decipherer passes over
(R795: *szem* `402 499 731` *n lé-*): nulls. 31 groups are slips. With nulls, 5,012/5,043 (99.4%) read.
`decode_nulls.py` prints the readings with nulls as `·`.

## The key: DECODE R580 / R581

DECODE R580 (MNL OL G15 Caps. C Fasc. 43/39) is headed *Nemzetes Vitézlő Pápai Jánosnak adott Clavis, mássa*
("key given to the noble and valiant János Pápai, copy"). R581 (Fasc. 43/40) and R452 (Ráday Archives
C64-4d2-25/11) are further copies of the same table. It is a Hungarian syllabic nomenclator, values 10–322:

- letters, two homophones each: A 219|229, B 209|239 … Z 60|312, plus ö, ü, ny, ly, gy, ty, cz, sz, nk, rt;
- vowel-consonant and consonant-vowel syllables (11 ab, 21 ad … 192 ge … 245 va … 236 üz), laid out in columns
  ending in 1, 2, 3 … 6;
- names: 246 Király, 256 Fejedelem, 257 Fényes Porta, 267 Török Császár, 277 Vezér, 287 Bassa, 297 Bécs;
  countries 17–207; places, rivers and months 18–298.

The key was never linked to these letters on DECODE (R805 is "partially decrypted": a few interlinear syllables).
The first test on R805 read 336 of 336 groups as continuous Hungarian. `decode.py` applies the table (R581's
transcription, which is the cleanest).

## What the letters say (gist; the reading files are `*_read.txt`)

- **R805, 1 May 1706.** The envoys urge that the Porte refuse the Germans (Imperial troops) free passage across
  Ottoman ground: *az németnek szabados általmenetelt ne engedgye … az Török Országon való általmenetelt … az végbeli
  Bassák … az Aradi Bassának ordere nélkül meg ne engedgye az németnek Szegedfelé való általmenetelt*. They have
  spoken to the Vezír about their affairs and also about Muscovy.
- **R823, 19 Dec 1706.** Report of an audience at the Porte in the presence of the Imperial internuncio, partly in
  Latin: *non libenter conversatur vobiscum … Fényes Porta in praesentia internuncii … praesentia autem vestra non est
  ingrata Portae*; the argument over hereditary kingship: *legibus imperatoris hereditarii regis sunt Angliae,
  Daniae, Sveciae, et tamen legibus subsunt*, and the envoys' reply that Hungary cannot give up its old laws.
- **R765, 5 Jan 1707.** Submission to the Prince's will, the Polish situation, and approaches to the French
  ambassador (*a Francia Ország oratorához elmentünk*) on the Prince's orders.
- **R784, 1707 (added 21 Sept 2026, catalogue entry "Unknown sender to Ferenc Rákóczi II").** Unsigned, undated
  report from Constantinople in the envoy's key: *A Francia Ország orátora jelentette … hogy semmi ratiókkal nem …
  a Fényes Portát az hadakozásra*: the French ambassador reported that no arguments could bring the Porte to war;
  the grandees who fought the last war have sworn to see it through (*egyátallyában effectuállyák hogy a Török
  Császárnak hadakozásra kell resolválni magát*); the whole Turkish nation is inclined to it; France means to turn
  Turkey wholly against the Germans (*ezt a Török Országot egészen a német ellen fordítsa*), from which Hungary would
  get harm, not profit; the ambassador has written the same to the Tatar Khan; if Muscovy and Poland do not second
  it, the Germans will overrun Hungary. It ends with the writer's wish to report quickly to *Nagyságod* (the Prince).
  The DECODE transcription splits five groups (`0 79`, `221 33`, `203 273`, `92 1`, `1 00`); read as the image
  shows them, all but one decode. On p. 2 a note in another hand, upside down, asks the Prince to keep it secret and
  decipher it himself: *Mivel ez titok, méltóztassék … titokban tartani s maga decifrálni …*. Grade H.
- **R795, 1 Jan 1706 (catalogue 47).** Pápai with Ferenc Horváth (*vélem Horváth Ferenc urammal*) reports the
  Prince's discretion money handed to the Vezír's Kiaya; the Tatar Khan; the French ambassador; the Pasha of
  Temesvár; a Croatian incursion; letters to go via Moldavia (*Moldvában … folytatni az leveleket … corres-
  pondentiát*) so that the Prince's news arrives faster. Ends *Constancz die prima Januarii Ezer het szaz hat,
  Pápai János*.
- **R796, 20 Feb 1706.** The Prince's undated letter from the Tisza received; the Germans spread false news; the
  confederates are scorned; the Moldavian *kapi-kiaya* as channel; the Muscovite envoy, the Vezír and the Sultan;
  nothing resolved on the propositions. Ends *Constancz, Ezer het szaz hat, huszadik Februarii*.
- **R793, March 1706.** Secret talks with the Porte's chancellor about the Muscovite–Porte quarrel, the King of
  Sweden, a Hungarian confederation with the Porte *certis conditionibus*, the Circassians and the Black Sea; the
  Prince's manifesto translated and given to the Vezír.
- **R794, early 1706 (undated).** Propositions on recruiting horse in Wallachia (*Havasalföld … négyezer lovas*),
  the memorial on Muscovy; the (French) King's money that the ambassador will not pay without the King's order.
- **R757, 16 May 1708.** The Muscovite ambassador's message; the envoy cannot send money from Constantinople;
  Hentér.
- **R740, 2 Jan 1710.** The Kiaya's answer, in cipher: *legyen patientia, [ne] siessen, várakozzék … Bécs … a
  Vezérnek megírván … ha a Fényes Porta szívére nem veszi … ne kellyen illy haszontalan költeni s alkalmatlankodni
  Felségednek a Fényes Portán*: be patient, do not spend money and effort at the Porte in vain.
- **R741, 8 May 1710.** At the Defterdar's; the Pasha of Belgrade's letter concerned only the merchants' affairs.

The readings are run-on Hungarian as the cipher gives it (no word division); the word breaks above are editorial.
Grades: the numeric passages are H (direct table reading) except isolated groups shown as `[n]` in the reading files.

## R731

A different cipher (graphic signs), split off 14 Oct 2026: see `../papai1710/NOTES.md`.

## Prior work

- DECODE lists R805 as partially decrypted (interlinear syllables) and the others as not decrypted. No link to R580.
- Kálmán Benda edited *Pápai János törökországi naplói* (Budapest: Szépirodalmi, 1963, Magyar Századok). Whether
  it prints these ciphered despatches deciphered was not checked (not online). Contemporary decipherments may
  also exist in the Rákóczi chancery papers. Treat the readings here as new only in that they were not on DECODE.

## Files

`fetch.py` (DECODE pages, transcriptions, images via the project cookie), `decode.py` (the table decoder),
`DOC_*.txt` (DECODE transcriptions and keys), `*_read.txt` (decoded output), `R740_transcription.txt`.

## Second pass (21 Sept 2026, later session)

**Numeric residue.** `decode2.py` re-reads every DECODE transcription with four rules on top of `decode.py`:
1. run-together groups (4–6 digits, e.g. `273159`, `83193`, `20561`) are split into key values: 84 groups,
   reading *meg*, *uram*, *vol*, *azut*, *alt* and so on (grade C: a few splits, such as `109422`, give doubtful text);
2. a split group is re-joined with its neighbour when the join is a key value and the parts are not (`1 00`, `4 4`,
   `3 08`): 14 groups;
3. 3-digit groups above 322 are nulls in every letter, as the interlinear decipherer treats them in R793–R796
   (316 groups), except R823, whose 400–1000 figures are clear numerals (19);
4. **220 = a** (grade C). 220 is not on the key sheet but occurs 11 times in R765, and in context it is *a* in eight
   (*…olvan a mediatio*, *de a valóság*, *irok a Királynak*): an unlisted homophone next to A 219|229, or a slip.

Result: 16,641 of 16,698 numeric groups read (99.66%). The 57 still open are scattered single groups (0–9, 110,
120, 160, 200 …), mostly fragments of split groups; `retry_groups.py` scored every key value in context with a
4-gram model of Pápai's own text and none wins by a clear margin (`retry_groups.tsv`). About 41 more tokens are
marked with `?` by DECODE's transcribers (illegible to them). The reading files are `<record>_read2.txt`.

**R731, the graphic signs.** Transcribed and attacked in this pass; the record is now in `../papai1710/NOTES.md`.

**Print.** Benda (ed.), *Pápai János törökországi naplói* (Budapest: Szépirodalmi, 1963, Magyar Századok) is not
online (antiquarian copies only). It needs a library copy.

## Remaining gaps
- 57 numeric groups across R757, R765, R793–R796, R823 - blocker: illegible; split or slipped digits in DECODE's transcriptions that no key value fits by context (retry_groups.tsv); about 41 further tokens marked '?' by DECODE
- Benda (ed.), Pápai János törökországi naplói (1963) - blocker: needs-physical-access; not online

## Escalation
- [x] siblings: twelve Papai records (R793–R796 added from catalogue 47) plus key copies R580, R581, R452 opened
- [x] clear-pages: interlinear decipherments of R793–R796 and R805 used; R581's corner sign line checked (cipher, not an alphabet)
- [x] known-keys: R580/R581/R452 applied to all eleven numeric letters; no graphic alphabet among them
- [x] print: Benda 1963 searched for online (antikvarium.hu only); DECODE and web searched, nothing printed online
- [x] key-rebuild: numeric key extended (220 = a, splits, joins, nulls above 322, decode2.py)
- [x] retry: every off-key group rescored in context (retry_groups.py) and regraded; 57 remain
