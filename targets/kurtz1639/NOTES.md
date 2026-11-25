# Kurz von Senftenau (Hamburg) to Trauttmansdorff, 1638-39

Status: in progress (all nine letters read as of 23 Oct 2026, eight of them read in part by the cipher-words-only count of 16 Nov 2026; key checked against Mírka's table; site page and ledgers still to be brought up to date)

23 Oct 2026, re-read r2c (REREAD_BRIEF, Claude Opus 5.5): **R3813 and R3814 read**; every letter now reads.
DECODE R3813 and R3814 carry Jakub Mírka's key reconstruction (an Excel sheet and a handwritten table, Nov 2022), listed
under the images and never opened before. It is a key, not a decipherment. Our key agrees with it in structure; the two
values that disagreed were checked at every occurrence and changed: k = to (was ti) and m = va (was a; 29 = qu does not
double the v, so 29 m = qua). 9v = vo holds at all 48 uses (Mírka's q). On the images the "crossed sign" of R3813 is two
shapes (tall crossed f = ta; low curled p-form = vi), the looped k-form (to) had been read d, α or x, and the x-places of
the null 4 are a crossed 4 (x, glossed so on R3811 p. 1): 32 labels in R3813, 3 in R3814, and 16 in the other letters
relabelled (read/<rec>_corrections.tsv; KEY.md "Corrections, 23 Oct 2026"). Reading bodies with conjectures counted as
holes (v2_score.py): R3813 plain 0.563, explicit holes 0.932; R3814 0.508 / 0.968 (half Latin); the sentences hold.
Sibling readings brought in line (contento, a proposito, protectorium, Salvius, extremam, perrexit). fraction_read 0.575 ->
1.0 (23,669 of 23,669 cipher tokens in letters that read). Logs: read/R3813_reread_log.md section 8, R3814_reread_log.md.

22 Oct 2026, re-read (REREAD_BRIEF, batch b06): **read** now R3811 (0.62), R3812 (0.616), R3815 (0.681), R4625 (0.603,
dated Hamburg 10 Feb 1639 on its p. 6), R4645 (0.625), R4736 (0.636), with R4734 seven of nine; **decoded, not read**
R3813 (0.531) and R3814 (0.524). Figures = clean-sentence share of the reading body (research/reading_audit/b06_body_score.py).
Key corrected for all letters after kwic checks: 38 = d (was g), Δ = nu (was e), #dot = su (was null), #s-long = ti (was t),
m = a (was null); polyphonic 9v = vo and pv = vi entered as relabelled signs (KEY.md, "Corrections, 22 Oct 2026"). About
330 label and clear-text fixes on full-resolution crops (read/<rec>_corrections.tsv); the R3811 interlinear decipherment
transcribed (read/R3811_interlinear.md). Readings, translations and logs: read/<rec>_reading.md, _en.md, _reread_log.md.
fraction_read 0.021 -> 0.575 (13,618 of 23,669 cipher tokens).

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read**: R4734 only (short
runs inside clear German). **Decoded, not read**: R3811, R3812, R3813, R3814, R3815, R4625, R4645, R4736: the clear
German reads, but the deciphered runs are unspaced and garbled every few lines (by-eye 55-80%), so sentences through the
cipher cannot be built. 99.9% (tokens with a value) is withdrawn as a reading figure; 2.1% of the cipher tokens read
(480 of 22,913).

Ferdinand Sigmund Kurz von Senftenau, imperial vice-chancellor, writing from Hamburg (one from Glückstadt) during the
preliminary peace talks with Sweden and France, to Maximilian von Trauttmansdorff (one to Ferdinand III, one a copy of a
letter to Schwarzenberg). SOA Plzeň, pracoviště Klášter u Nepomuka, RA Trauttmansdorffů, inv. č. 200, karton 9.

## Documents (DECODE, all public images, fetched to img/, git-ignored)

| DECODE | date | to | images |
|---|---|---|---|
| R3812 | 1639-02-03 (DECODE: 1638, wrong) | Trauttmansdorff | 14 |
| R3811 | 1639-01-17 | Trauttmansdorff | 6 (p.1 has interlinear decipherment) |
| R3813 | 1639-01-27 | Trauttmansdorff | 20 |
| R3814 | 1639? undated | Trauttmansdorff | 5 |
| R3815 | 1639-02-06 | Ferdinand III | 4 |
| R4625 | 1639-02-10 | Trauttmansdorff | 7 |
| R4645 | 1639-02-13 | Trauttmansdorff (with two Banér copies) | 9 |
| R4734 | 1639-04-08 | copy of letter to Schwarzenberg | 5 |
| R4736 | 1639-04-14 (Glückstadt) | Trauttmansdorff | 3 |

73 image files (many are two-page spreads). No DECODE key record and no transcription files; R3813 and R3814 carry Mírka's key reconstruction (xlsx + handwritten table, 2022) as attachments, opened only on 23 Oct 2026.

## Prior work

- Contemporary interlinear decipherment on p.1 of the 17 Jan 1639 letter (R3811).
- Jakub Mírka, "Raně novověká šifrovaná korespondence ...", Západočeské archivy 2012, 44-72; reprinted in Crypto-World
  11-12/2012 (part I, pp. 23-25, lit/crypto1112_12.pdf). He rebuilt the key from the R3811 p.1 interlinear text
  (homophonic letters, one sign for each consonant+vowel bigram ba be bi bo bu ca ... , nulls, no codes) and deciphered
  only the 17 Jan 1639 letter, summarised in Czech (Swedish/French/Dutch pressure on the Polish king, supply problems,
  Saxe-Lauenburg and Denmark, long passage on Hans Georg von Arnim denying a part in Wallenstein's treason and seeking
  pardon). The key table and plaintext are not printed. The other letters were "dosud nedešifrované" (not yet deciphered). His key table is on DECODE (R3813/R3814 attachments, Nov 2022): see the 23 Oct 2026 block.

## Method

tr/CONVENTION.md: token transcription of every image (agents, 2 at once). Key rebuilt from the R3811 glosses, then
extended by homophonic solving with a German LM and cleartext context.

## Result (19 Sept 2026)

**The key.** KEY.md / key.json. Numbers 41-100 are consonant+vowel signs in a regular table: each ten is split into two
halves, one consonant each, in reverse alphabetical order from 41 (r p n m l k h g d c b); units 1-4 of a half run o i e a
(41 ro, 42 ri, 43 re, 44 ra); the fifth place of each half is a separate consonant+u series (45 pu, 50 lu, 55 mu, 60 hu,
65 ku, 70 du, 75 gu, 80 bu, 85 cu, 95 us, 100 ru; 97 is, 98 es). Numbers 1-40 and the letter and graphic signs are
homophones for single letters, a few for pairs (9 te, 6 se, c si, n ve, d so, k ti, #l-loop tu); ψ/φ z, π/α m, 29 qu.
#s-loop, #dot, p and a few rare signs are treated as nulls (or flourishes). This is Mírka's "homophonic substitution with
bigrams and nulls", now written out.

**The reading.** read/<record>.txt (clear text in braces, decipherment in brackets); read/SUMMARIES.md in English.
22,913 cipher tokens transcribed; 98.3% get a value. The decipherment is fluent in stretches and garbled in others:
by-eye coherence 55-80% per letter (R4645 best, R4736 and R3814 weakest). The garble is mostly transcription (one pass by
agents; 1/7, 6/0/c, 9/ψ/φ, 93 vs 9 3 confusions) and Latin passages, not the key. α reads "Salv-" before l (Salvius,
salvus conductus): probably a second sign merged with α in transcription.

**Content.** Kurz's reports from Hamburg (and Glückstadt) Jan-Apr 1639: Banér's winter invasion of Lower Saxony and
Halberstadt, Duke Georg of Lüneburg's passivity and the Lower Saxon Circle's neutrality, Arnim's escape and his plea for
a protectorium, the Danish mediation of Christian IV and its expiry, distrust of Salvius and of "universal" treaties
("ein teufflisch inventum"), France's aims (Lorraine, Alsace, the imperial crown), Rákóczi and French money.

**Corrections to DECODE.** R3812 is 3 Feb 1639, not 1638 (it answers R3813 of 27 Jan 1639; postscript dated 1639).

**Open (updated 21 Sept).** The second pass is done (below). The Banér copies in R4645 (to Lüneburg, 10 Jan 1639; to the
Lower Saxon envoys, 29 Jan 1639) and the R4734 endorsement ("Copia deß Herrn Reichs Vice Canzlers schreiben Ahn Herrn
Graven von Schwartzenberg abgangen. 8. April 1639") are transcribed in read/. See Remaining gaps.

## Second pass (21 Sept 2026)

Every tr/ file was checked line by line against crops of the images (tr/PASS2.md rules, tr/PASS2_LOG.md per-file log;
check.py prints each line with its token values). About 360 tokens corrected, no lines added or removed. The recurring
misreads: `c` for `#l-loop` (tu, 27 cases, mostly R3812/R3811), bold `9` for `#sect` (w, about 30), `6`/`61` for `φ`
(z, dozens in R3813), wrong splits of two-digit groups (`63 1` = `6 31`, `9 3` = `93`, `4+ 2?` = `42`), `62`/`93` for
`6`/`9`. In R3813 a crossed ƒ-like sign had been merged with `x` (i); split out as `#f-cross` = ta (114 tokens; LM
confirms: R3813 -2.968 -> -2.935, while x = ta makes R3812 worse, so it is R3813's own sign).

A script bug was also fixed: decode.py, parse.py and check.py treated any line starting with `#` as a comment, so 56
cipher lines opening with a sign (`#4-hook`, `#z-tail` ...) had been left out of the reading and the solver.

Effect (German 5-gram, mean log-prob per char, before -> after; deciphered chars):
R3812 -3.071 -> -3.015 (6888 -> 7008); R3811 -3.036 -> -2.966; R3813 -3.084 -> -2.935 (10189 -> 10514);
R3814 -3.352 -> -3.324; R3815 -3.108 -> -2.981; R4625 -3.270 -> -3.219; R4645 -3.312 -> -3.306 (Latin-heavy);
R4734 -3.089 -> -2.989; R4736 -3.099 -> -3.113 (2060 -> 2200 chars: restored lines, e.g. "dimittiren, mal disfatti
et mal disfatti ist"). 23,699 cipher tokens, 99.9% with a value. read/*.txt regenerated.

Alpha split (21 Sept): α re-valued m -> sa (LM better on 7 of 9 letters), 28 looped tokens renamed #a-loop = m after
image check. Scores after all changes: R3812 -2.969, R3811 -2.906, R3813 -2.881, R3814 -3.260, R3815 -2.945,
R4625 -3.191, R4645 -3.306, R4734 -2.902, R4736 -3.089 (every letter better than the 19 Sept baseline).

## Log

- 2026-09-19: records, images, literature fetched; transcription started.
- 2026-09-19: all 73 images transcribed (tr/); structured solver; key rebuilt (KEY.md); all nine letters deciphered.
- 2026-09-21: checked second transcription pass on all 73 images; comment-line bug fixed (56 lines restored); #f-cross = ta split from x in R3813; read/ regenerated; α = sa and #a-loop = m split; R4645 Banér copies and R4734 endorsement transcribed (addressee Schwarzenberg).

## Read share over cipher words only (16 Nov 2026)

README Conventions now measure the read bar over the words written in cipher only. These letters mix the two, and the
readings run clear and deciphered text together unmarked. To split them, each reading body (title to `## Notes`) was
aligned character by character to `read/<rec>.txt`, where the clear text is in braces and the deciphered runs are in
brackets. Each word and each hole took the side of the stream it falls in
(`research/reading_audit/r23_kurtz_split.py`). R4734 marks its cipher runs in ⟨ ⟩ and was counted by that mark.
Holes were counted by words with the v2_score rules.

| letter | recorded | cipher words only | holes / words read | whole letter, clear included (not the measure) | state |
|---|---|---|---|---|---|
| R3811 | 0.965 | 0.939 | 24 / 369 | 0.959 | read -> read in part |
| R3812 | 0.95 | 0.901 | 121 / 1,106 | 0.946 | read -> read in part |
| R3813 | 0.966 | 0.939 | 113 / 1,731 | 0.965 | read -> read in part |
| R3814 | 0.972 | 0.943 | 28 / 463 | 0.958 | read -> read in part |
| R3815 | 0.967 | 0.918 | 24 / 270 | 0.946 | read -> read in part |
| R4625 | 0.971 | 0.922 | 40 / 475 | 0.965 | read -> read in part |
| R4645 | 0.95 | 0.945 | 18 / 309 | 0.937 | read -> read in part |
| R4734 | 0.98 | 0.958 | 5 / 113 | - | stays read |
| R4736 | 0.94 | 0.904 | 37 / 347 | 0.909 | stays read in part |

The recorded figures were taken over each whole reading file, which has no `## Reading` heading, so the Notes were
counted too. Over the reading body alone, with the clear text, R3812, R3815 and R4645 were already under 95%. The
target was already read in part (R4736) and stays so. One letter of nine (R4734) now meets the read bar. The holes are
the ones listed under Remaining gaps, and nothing new is added there.

Pooled over the nine letters, 5,183 of 5,593 cipher words read: **0.927**. This is now `fraction_read`, and the
page reads partial (93% of the cipher). The earlier 1.0 counted the tokens of letters that build sentences.

## Remaining gaps
- Residual [?] words and unread runs in the nine letters (R3813 about 20 [?] and the clerk's slips in its Notes; R3814 about 12 runs; the others in each read/<rec>_reading.md Notes) - blocker: no-key-material; checked 23 Oct 2026 against Mírka's full key table and on the images (look-alike signs split); the remaining figures are legible but spell no word under any value of either key, and no second copy of the letters exists
- All nine letters, residual garbled lines (listed per file in tr/PASS2_LOG.md; R3814 and R4645 Latin worst) - blocker: illegible; the checked second pass (21 Sept) fixed about 360 tokens; what remains is mostly ambiguous digit groupings, blots and overwritten digits where the image does not decide
- Postscripts and margin notes in Kurz's own cursive (R3811, R3814 p. 4, R4645 P6, R4736) - blocker: illegible; fast personal hand at DECODE image resolution, partly read in the Notes (the Banér copies P7+P5 and P3+P8 and the R4734 endorsement are transcribed, read/R4645_clear.md, read/R4734_endorsement.md)
- R4645: a leaf between P2 ("quae ergo") and P6 - blocker: needs-physical-access; not among the nine DECODE records

## Escalation

- [x] siblings: all nine DECODE records (73 images) transcribed; no key record or transcription files on DECODE
- [x] clear-pages: R3811 p. 1 interlinear decipherment used to seed the key; transcribed in full 22 Oct 2026 (read/R3811_interlinear.md)
- [n/a] known-keys: the key is rebuilt in full from the glosses and the regular CV table; Mirka's 2012 key is not printed
- [x] print: Mirka, Zapadoceske archivy 2012 and Crypto-World 11-12/2012: only the 17 Jan letter, summarised
- [x] key-rebuild: structured homophonic solver with a German LM; table 41-100 written out (KEY.md, key.json)
- [x] retry: checked second transcription pass on all 73 images (21 Sept 2026), decode.py rerun on all nine letters; LM score better on 8 of 9
- [x] retry (22 Oct 2026, b06): key corrected (38 = d, Δ = nu, #dot = su, #s-long = ti, m = a, 9v = vo, pv = vi), every letter re-read on crops, six more letters read; R3813/R3814 short of the bar
- [x] known-keys (23 Oct 2026, r2c): Mírka's key table (xlsx + handwritten) found attached to DECODE R3813/R3814; compared sign by sign: k = to and m = va adopted, 9v = vo confirmed
- [x] retry (23 Oct 2026, r2c): look-alike signs split on full-resolution crops (curled p = vi, looped k = to, crossed 4 = x) in R3811-R3815; R3813 and R3814 read
- [x] print (23 Oct 2026): web search for an edition of Kurz's Hamburg letters found none; Documenta Bohemica Bellum Tricennale Illustrantia VI (1979) may calendar them (regests only) and is not online
