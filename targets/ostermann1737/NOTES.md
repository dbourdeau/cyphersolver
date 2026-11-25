# ostermann1737: A. I. Ostermann in the Empress's name to I. P. Kalushkin, Russian resident in Persia, 17 April 1737 (O.S.), GAAO Astrakhan f. 394 op. 1 dop. d. 11 l. 21 (catalogue 1247)

Status: in progress. Contributed by pull request, not yet written up: the key was recovered from cipher lines 1-16 alone, frozen, and used for one decode of all 20 cipher lines (strict judge 760 of 770 letters, 98.7%; held-out lines 17-20 147 of 148, 99.3%). By the README read bar, counted in words, 140 of 152 words read as sense (0.921) with the one-letter slips counted as holes, so the target is filed read in part. The page, ledgers, DECODE queue and catalogue edit are left to the maintainers (24 Nov 2026: the DECODE queue entry, a held skip, and the catalogue 1247 edit are done; the page and ledgers wait for the write-up).

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic): Claude Fable 5.2 the solver session, Claude Opus 5.5 the strict judge and the assembly of this folder.

Provenance tags: [measured] = counted or hashed from the files in this folder; [derived] = worked out from them; [sourced] = from a named source; [stated] = given by the contributor's working session, not checked here; [unverified] = a reading of the text not checked by anyone else.

## The source

GKUAO GAAO (State Archive of Astrakhan Oblast), f. 394, op. 1 dop., d. 11, l. 21. The Commons file page describes it as "Рескрипт вице-канцлера ... Остермана русскому резиденту в Персии И. П. Калушкину, 17 апреля 1737 г." and gives the Astrakhan archive's virtual exhibition as its source [sourced: Commons file page, PRIOR_ART.md 4]. The catalogue dates it 28 April 1737 N.S. [sourced: catalogue.json 1247]. The rescript speaks in the Empress's voice ("по указу нашему", "нашего вице канцлера") [derived: the decode].

One leaf: a clear opening, then 20 lines of cipher (the clear words "Въ цѣлости" stand before the cipher in line 1). Line 20 breaks off in mid-sentence ("тебе всячески"); the text goes on on a leaf that was not imaged [derived: DECODE.txt].

Image: **none is committed.** Wikimedia Commons, https://commons.wikimedia.org/wiki/File:Шифрованное_письмо_вице-канцлера_Остермана_резиденту_в_Персии_Калушкину,_1737.jpg (714x1021). The original file returned HTTP 429 four times and the 500px thumb 429; the working image is the rendering from `https://commons.wikimedia.org/w/thumb.php?f=<file>&w=713`, 713x1020, md5 992c3531700364eeca36943e86b9d1a1, a re-encoded thumbnail one pixel short of the original. The archive's own PNG (archive.astrobl.ru/.../f-394-op-1-dop-d-11-l-21.png) and exhibition page were unreachable (proxy tunnel closed) (`FETCH_LOG.txt`) [measured]. Licence: the Commons page tags the file PD-Art (PD-old-100-expired), public domain [sourced: the saved copy of the file page in the working folder, 24 Nov 2026; not re-checked].

Length [measured]: `python docs/_check_profile.py --measure transcription_l21.txt --drop-first` gives 896 whitespace tokens = 787 sign tokens + 101 group gaps (`|`) + 1 illegible sign `[...]` + 7 tokens of clear text and marks in braces. Of the 787 signs, 17 are the divider S26 (12) and the flourish S33 (5), leaving 770 letter signs (`shuffle_out.txt`, `judge/judge.tsv`). 33 sign labels (`SIGNS.md`).

## The system (`KEY.tsv`)

One-to-one substitution of 31 signs for Russian letters. The signs are Cyrillic letters, digits and marks given other values [measured: KEY.tsv]:

| sign (mnemonic) | value | sign | value | sign | value | sign | value |
|---|---|---|---|---|---|---|---|
| S01 (В) | к | S09 (8) | и | S17 (а) | л | S25 (є) | х |
| S02 (б) | п | S10 (4) | д | S18 (п) | в | S27 (ψ) | я |
| S03 (ш) | о | S11 (2) | с | S19 (n) | у | S28 (У) | **от** (ligature ѿ) |
| S04 (two minims) | е | S12 (ӡ) | б | S20 (р) | г | S29 (o) | ф |
| S05 (ц) | р | S13 (5) | з | S21 (Ф) | ы | S30 (x) | ь |
| S06 (w) | н | S14 (9) | ч | S22 (ϑ) | ю | S31 (X) | ж |
| S07 (+) | а | S15 (ч-like tick) | м | S23 (Д) | ш | S32 (Л) | щ |
| S08 (ꙋ) | т | S16 (т) | ъ | S24 (Г) | ц | | |

- S26 (a long slanted stroke) is a divider and S33 (a line-end flourish) a stop or filler; neither is a letter (assumed before solving, decoded as / and //).
- The key does not tell ѣ from е or і from и (the solver's model folded them) [stated: SOLVE_LOG.md].
- Weak values: S29 ф and S32 щ have one training use each; S28 has two uses and was set by hand (below).
- No order was seen in the table (В = к, ш = о, 8 = и ...) [derived].

## Method

The pipeline is the contributor's (prior art first, frozen transcription and key, one decode, a separate strict judge, a shuffle control). Times are UTC on 24 Nov 2026 from the sandbox clock.

1. **Prior art** before transcription: `PRIOR_ART.md`. No key, decipherment, gloss or printed reading of this leaf found. See "Prior art" below.
2. **Transcription** from 5x crops of each line of the thumbnail, by one Claude Fable 5.2 session, one pass, blind to any key (none exists): signs by shape, gaps between groups, 7 doubtful signs marked `?`, one blot `[...]` (`TRANSCRIPTION.tsv`, conventions and doubtful pairs in `SIGNS.md`). Frozen with the split at 10:46 (`FREEZE_TX.txt`: sha256 of `TRANSCRIPTION.tsv` 34096000... and `SIGNS.md` 9fc9e0d6..., both matching the files here) [measured].
3. **Held-out design.** Training = lines 1-16 (622 letters); held-out = lines 17-20 (148 letters, 19.2% of 770). There is one leaf, so the held-out block is the last four lines of the same leaf. **Blindness:** the held-out lines were seen as images during transcription (unavoidable on one leaf), but no decode of them existed before the key was frozen [stated: SOLVE_LOG.md].
4. **Key from lines 1-16 only** (`SOLVE_LOG.md`, `scripts/`):
   - Statistics on 637 training signs: IC 0.0552, top sign S03 14.4%: one-to-one substitution on Russian.
   - Simulated annealing (`scripts/solve.py`) with an own Russian 5-gram character model with spaces (`scripts/rulm.py`), 30,000 steps, 8 seeds: 8 of 8 gave the same key (corpus at 143 pages); 6 of 6 again with the corpus complete at 160 pages; the same key with a 4-gram model without spaces (4 seeds).
   - **Language model:** `lang/` has no Russian model. The solver built one from 160 ru.wikisource pages of 1700-1749 documents in pre-reform spelling (mostly the Полное собрание законов), about 0.6 M characters, normalised to 31 letters (й, і to и; э, ё to е; ѳ to ф). Page list and hashes in `lmsrc/FETCH_LOG_lm.txt`, hash of the concatenated corpus in `lmsrc/CORPUS_SHA256.txt`. The genre is decrees, not diplomatic rescripts. The pages themselves are not committed.
   - **The one hand edit (disclosed):** S28 occurs twice, both in training lines. The solver gave it ѣ; it was set by hand to the ligature ѿ = "от" from the two training contexts "онъ _ себя" (line 8) and "_править" (line 14) (`SOLVE_LOG.md` 5, note in `KEY.tsv`). Nothing else in the key was set by hand.
5. **Key frozen** at 10:55 (`FREEZE_KEY.txt`: `KEY.tsv` sha256 6895d478..., matching the file here) [measured]; then **one decode** of all 20 lines (`decode_once.py` -> `DECODE.txt`, sha256 cf6cfcb5... as recorded in `FREEZE_KEY.txt`). No emendations: the first pass is the figure of record.
6. **Separate strict judge** (Claude Opus 5.5): saw only `judge/BRIEF.txt` and `judge/decode.txt`; scored every decoded letter S (sense), E (one-letter slip in a readable word) or N (no sense), the ligature as one letter (`judge/judge.tsv`). `judge/count.py` re-adds it [measured, re-run here; the script reads `/tmp/judge_ost/judge.tsv`, a copy identical to `judge/judge.tsv`].
7. **Shuffle control** (`shuffle.py`, `shuffle_out.txt`): 5,000 shuffled keys per seed (letter values permuted among the letter signs), same model, score of the whole rendering.
8. **Time-stamps** (`stamps/`): a sha256 manifest of the working folder (234 files) at 11:01:34, stamped by RFC 3161 at Sectigo and FreeTSA (both 11:01:35 GMT); OpenTimestamps failed (`stamps/STAMP_LOG.txt`).

The scripts keep the working folder's paths (`/home/claude/keyless/ostermann1737/`) and do not run from this folder as they stand. The corpus pages, the line crops and the image are not committed.

### The solver's report

The solver session's own report was not saved to disk, and no `REPORT.md` is included. This section and the Method above were written from the files by the assembling session.

## Figures (first pass of record)

Strict judge, letters (`judge/judge.tsv`, re-added by `judge/count.py`) [measured]:

| line | split | S | E | N | letters | S share |
|---|---|---|---|---|---|---|
| 1 | training | 29 | 0 | 0 | 29 | 100.0% |
| 2 | training | 41 | 1 | 0 | 42 | 97.6% |
| 3 | training | 40 | 1 | 0 | 41 | 97.6% |
| 4 | training | 41 | 0 | 0 | 41 | 100.0% |
| 5 | training | 36 | 1 | 0 | 37 | 97.3% |
| 6 | training | 38 | 2 | 0 | 40 | 95.0% |
| 7 | training | 37 | 1 | 0 | 38 | 97.4% |
| 8 | training | 41 | 0 | 0 | 41 | 100.0% |
| 9 | training | 39 | 0 | 0 | 39 | 100.0% |
| 10 | training | 37 | 0 | 0 | 37 | 100.0% |
| 11 | training | 42 | 0 | 0 | 42 | 100.0% |
| 12 | training | 37 | 0 | 0 | 37 | 100.0% |
| 13 | training | 33 | 2 | 0 | 35 | 94.3% |
| 14 | training | 41 | 0 | 0 | 41 | 100.0% |
| 15 | training | 41 | 1 | 0 | 42 | 97.6% |
| 16 | training | 40 | 0 | 0 | 40 | 100.0% |
| 17 | held-out | 36 | 1 | 0 | 37 | 97.3% |
| 18 | held-out | 36 | 0 | 0 | 36 | 100.0% |
| 19 | held-out | 35 | 0 | 0 | 35 | 100.0% |
| 20 | held-out | 40 | 0 | 0 | 40 | 100.0% |
| lines 1-16 | training | 613 | 9 | 0 | 622 | 613/622 = 98.6% |
| lines 17-20 | held-out | 147 | 1 | 0 | 148 | 147/148 = 99.3% |
| all | | 760 | 10 | 0 | 770 | 760/770 = 98.7% |

Sums: training 29+42+41+41+37+40+38+41+39+37+42+37+35+41+42+40 = 622; held-out 37+36+35+40 = 148; 622+148 = 770 [measured].

The judge's 10 E (one-letter slips), none emended:

- о for е, 6 times: подтворждаютца (l.2), спорсицкимъ (l.3), случао (l.6), имоешъ (l.6), порсицкои (l.7), имоешъ (l.13). S03 (three minims) = о and S04 (two minims) = е are a doubtful pair at this resolution (`SIGNS.md`), so these may be misreadings here or a confusion of two key cells by the clerk.
- хъъ (l.5, extra ъ; которыхъ), сосланось (l.13, н for л), разведыъа (l.15, ъ for в), изконстянтино (l.17, я for а).

The judge scored "писа" (l.8) and "происходи[...]ъ" (l.16) as sense; the reading counts both as holes (below).

Read share by words, the README read bar (`reading.md`) [measured with `research/reading_audit/v10_relabel.measure_text`]: 152 words; holes are the 9 one-letter slip words, marked `(?)` (the 10 judged slips less хъъ, which joins которы into one word), and 3 words with a letter not in the cipher (писа[л], разведыъа[ть], происходи[т]ъ). **Read share 140/152 = 0.921**; 149/152 = 0.980 if the slips were counted as read. The slip rule of README Conventions applies only to a surviving period key, and this key is rebuilt, so the slips are holes. The text builds coherent sentences throughout, so it is **read in part**. Word division in `reading.md` is today's (prepositions split off, line-end breaks joined); the count on the clerk's own gaps was not made.

Shuffle control (`shuffle_out.txt`) [measured]:

| split | letters | real key (per sign) | shuffles mean (sd), seed 20261112 | best shuffle | z | shuffles at or above real |
|---|---|---|---|---|---|---|
| whole text, lines 1-20 | 770 | -2237.6 (-2.906) | -6988.1 (286.0) | -5991.3 | 16.6 | 0 / 5,000 |
| held-out lines 17-20 | 148 | -486.5 (-3.287) | -1344.7 (63.7) | -1086.7 | 13.5 | 0 / 5,000 |
| training lines 1-16 | 622 | -1750.3 (-2.814) | -5637.6 (230.4) | -4857.2 | 16.9 | 0 / 5,000 |

Seed 7 gives z 16.9, 13.8 and 17.2, 0 / 5,000 each.

Repository validation: **not run.** `python docs/_validate.py ostermann1737` stops with "no model: add "# model: <id>" to the pairs file": `lang/` has no Russian model (24 Nov 2026). `validation.tsv` (787 sign tokens with their `KEY.tsv` values, S26 and S33 as nulls, the blot unread) is ready for a run once one is added. `profile.json` records verification as none for this reason.

## Reading and translation

`reading.md` gives the 20 lines as Russian sentences in the decode's spelling, holes marked; `translation.md` gives the English. Both were made by Claude Opus 5.5 for the contributor and are **unchecked** by a person or a reader of Russian [unverified].

Russian (reading.md, abridged marks):

> на которые тебе в резолюцию ничего иного не находитца, толко подтворждаютца(?) прежние указы. А что после того здесь с порсицкимъ(?) посломъ происходило в конференцияхъ, о техъ прилагаютца при семъ протоколы ... Но понеже порсицкои(?) посолъ не однократно домогался у нашего вице канцлера, чтобъ онъ от себя к шаху писа[л] ... Ты имоешъ(?) оное писмо пристоинымъ образомъ к шаху отправить, а в протчемъ бденно смотреть и прилежно разведыъа[ть], что между шаха и турокъ происходи[т]ъ, и какъ и с чемъ возвратился из констянтинополя(?) посолъ его абдулъ бакы ханъ ... На обращения же того турецкого посла тебе всячески

English [unverified: the contributor's translation]: "... to which nothing further is found [to give] you by way of resolution; only the former decrees are confirmed. And as to what has since passed here with the Persian ambassador in the conferences, the protocols are enclosed herewith, by which you are to act in case of need. But since the Persian ambassador more than once pressed our vice-chancellor to write to the Shah himself, and although no need for it was seen, nevertheless, to please the ambassador, the vice-chancellor did so by our order; a copy is sent to you herewith, where you will see that in everything reference is made to him, the ambassador, and to you. You are to send that letter to the Shah in a fitting manner, and for the rest to watch vigilantly and diligently find out what is going on between the Shah and the Turks, and how and with what his ambassador Abdul Baki Khan has returned from Constantinople, with whom, as is known here, the Turkish ambassador too has gone to the Shah. And as to the dealings of that Turkish ambassador, you [are] in every way ..."

The names and the historical setting (Nadir's embassy to Constantinople, the Turkish envoy) were not checked against any source.

## Prior art

`PRIOR_ART.md` (copied unchanged). Searched 24 Nov 2026, before transcription: Cyphersolver issues and PRs (`issues_index.tsv`, `issues_bodies.tsv`: ostermann, kalushkin, astrakhan, остерман, калушкин, 0 lines each; 1247 also 0 lines, checked again for this PR), the repository (only the sweep and vetting records of this lead), DECODE public (gate record: Ostermann 0, Kalushkin 0, Astrakhan 0; not re-run), the Commons file page (no transcription or decipherment), web searches in Russian and English, and after the decode two plaintext phrases (no hit). **No earlier key or reading was found.**

Flag: the SPbII RAN finding aid for f. 178 op. 3 (Astrakhan prikaznaya palata) lists 1739 rescripts to Kalushkin as "Шифр и дешифрант" and "Частично зашифрован, и дешифрант" (units 178-3-6, -7, -10): other documents, two years later, unpublished, with no key listed; whether they use the same alphabet is unknown [sourced through a fetch summary, unverified at page level].

Not checked: the Astrakhan archive's virtual exhibition page and caption (unreachable: whether it prints a reading is unknown); Soboleva, Тайнопись в истории России / История шифровального дела в России, at page level; AVPRI f. 77 "Сношения России с Персией" (the Collegium's clear draft of this rescript should be there); HathiTrust and Google Books full text. For the prior-art sheet: "бденно смотрѣть и прилѣжно развѣдывать", "Абдулъ Бакы ханъ", "Калушкину" 1737.

## Catalogue corrections for 1247 (not edited here)

- Extent: **20 cipher lines, not "about 17"** (vetting.seen.extent and .cipher). Count: 787 sign tokens (33 labels), of which 770 letter signs and 17 dividers and flourishes, giving 770 decoded letters; one illegible sign.
- The text runs on past l. 21 ("тебе всячески ..."): the next leaf of d. 11 holds the rest.
- Status: key recovered from the ciphertext alone, read in part, in `targets/ostermann1737/`.

Edited by the maintainers at the integration, 24 Nov 2026: catalogue 1247 now gives 20 cipher lines and 770 letter signs, the known and open pieces and a link to this folder. The entry stays in the catalogue until the write-up.

## Check by the project (PR #935, 24 Nov 2026)

Checked by a model session for the project (an AI agent, not a person) on the pull request as filed (head 37ddd5dbbe). No person has checked the transcription, the decode, the reading or the translation. Class, counts and credits are unchanged.

- Decode: a decoder written here (label to value from `KEY.tsv`, divider and flourish dropped, groups as transcribed) gives the text of `DECODE.txt` and `judge/decode.txt` on 20 of 20 lines: 787 sign tokens = 770 letter signs + 17 marks (S26 12, S33 5); 33 labels; 7 doubts; 1 blot. S28 (от) has 2 uses, both in training lines; S29 1; S32 2 (1 training, 1 held-out).
- Judge figures re-added from `judge/judge.tsv`: training 613 of 622, held-out 147 of 148, all 760 of 770; per line as in "Figures" above.
- Words recounted from `reading.md`: 152 words, 9 slip words marked (?) and 3 with a supplied letter: 140 of 152 (0.921), 149 of 152 with the slips. The reading's letters, the supplied letters taken out, equal the decode's letters exactly (only capitals differ): no unmarked departure.
- Read as sentences: coherent chancery Russian from end to end, breaking off at line 20; the translation follows it. Read in part by the README bar. The `reading_review` signed by the contributor's assembling session was replaced by the project's (grade B, 24 Nov 2026): the review is recorded by a reader who is not the author.
- Hashes: `FREEZE_TX.txt` and `FREEZE_KEY.txt` match their files; 25 of 25 committed entries of `stamps/MANIFEST.sha256` match; the manifest hashes to 5f924682..., as `STAMP_LOG.txt` says, and both RFC 3161 tokens carry that digest (11:01:35Z).
- Order of events: `FREEZE_KEY.txt` line 6 lists the sha256 of `DECODE.txt`, so that file was written after the decode existed and cannot show that the key was fixed first. Everything came in one commit; the order (transcription freeze 10:46Z, key freeze 10:55Z) rests on the contributor's record.
- Image: the Commons thumbnail (md5 992c3531..., as `FETCH_LOG.txt`) compared with the transcription at four places, line 1 whole, the right halves of lines 2 and 3 and the left of line 17 (with S27 я in "констянтино"): all agree. Counted on the full leaf: 20 cipher lines from "Въ цѣлости" on, not "about 17".
- Three minims: at two of the о-for-е places (подтв-о-рждаютца, line 2; сп-о-рсицкимъ, line 3) the thumbnail shows a clear three-minim sign (S03), so at this resolution they are as written, not misread here. Whether the original has two minims there needs a better image.
- The marks above the line (a model's reading of the thumbnail, not checked by a person): above the end of line 8 an a-shaped sign, the shape of S17 (л); above the end of line 15 the y-shaped S08 (т), as the gap line below suggests. Letters written above the line at line ends are normal in this hand (the clear opening has them). Read as signs they give писал and разведыват[ь] from the key, so the blocker "illegible" given for these two marks under Remaining gaps is in doubt; a second pass that reads them as signs is the next step. The frozen transcription is unchanged.
- Better image: the Commons original is 714 x 1021 (Commons API, and `FETCH_LOG.txt` line 3), one pixel more than the 713 x 1020 thumbnail that was read, so it settles nothing. The archive's own PNG has a Wayback copy (snapshot of 2 Aug 2021, `web.archive.org/web/20210802062718/https://archive.astrobl.ru/sites/archive.astrobl.ru/files/300-let/f-394-op-1-dop-d-11-l-21.png`, from the availability API). The project could not download it (the direct host reset the connection; the Wayback fetch gave an empty reply), so it is not shown to be larger.
- Method stays "key recovered from ciphertext-only": annealing with the solver's own Russian model; the one hand edit (S28 = от) is disclosed and comes from two training contexts; no crib or outside plaintext. The statistical validation cannot run (`lang/` has no Russian model), and the shuffle control could not be re-run here (the solver's model and corpus pages are not committed).
- Prior art, the project's pass: Sbornik IRIO vol. 114 (Cabinet of Ministers papers, 1736; archive.org full text) grepped, no Kalushkin; the 1737 volume was not found online in a quick search. Nothing contradicts "no earlier key or reading found".
- Not checked: the 7 doubts and the blot sign by sign, the four other о-for-е places, the archive's PNG, the shuffle control and the annealing, the times in the freeze files, the names and setting against a source.

## Remaining gaps

- Better image - blocker: needs-physical-access; only a 713x1020 re-encoded thumbnail was read; the Commons original (HTTP 429) and the archive's PNG (unreachable) were not obtained. A full image from GAAO would settle the doubtful sign pairs and the slips.
- The о/е slips, 6 of the 10 (подтворждаютца, порсицкимъ, случао, имоешъ twice, порсицкои) - blocker: illegible; S03 (three minims, о) and S04 (two minims, е) are hard to tell apart at this resolution; a misreading here or a key-cell confusion by the clerk; not emended.
- The other 4 slips (которыхъъ, сосланось, разведыъа, констянтинополя) - blocker: illegible; one sign each to be re-read on a better image.
- Flourishes and marks at line ends: above the line at the ends of lines 8 ({sup. flourish}) and 15 ({sup. y}), and the flourish after line 10 - blocker: illegible; transcribed as marks, not decoded; the sense wants писа[л] and разведыва[ть] (the line 15 mark may be S08 = т written above the line).
- One illegible sign in line 16 (происходи[...]ъ, т by sense) - blocker: illegible; a blot on the thumbnail.
- The text continues on an unimaged leaf after line 20 - blocker: needs-physical-access; only l. 21 is on Commons.
- Weak key values: S29 ф and S32 щ (one training use each), S28 от (two uses, set by hand) - blocker: too-short.
- Prior-art gaps: the exhibition caption, Soboleva at page level, AVPRI f. 77, the 1739 rescripts with "дешифрант" in SPbII RAN f. 178 op. 3 - blocker: needs-physical-access (unreachable from the sandbox, in print or not online).

Not a gap in the text, but open: the repository's statistical validation (`docs/_validate.py`) has not run, because `lang/` has no Russian model; a corpus and model would have to be added there.

## Transcription doubts

Doubts were not settled against the image after the decode: by the freeze rule no sign was changed. Each is listed with what the frozen key gives. None was checked on the image after the decode, and there is no second transcription.

- S06? (l.4) - read: S06 = н; checked: decode; gives "вконференцияхъ" (judge S). Image not rechecked.
- S16? (l.5 end) - read: S16 = ъ; checked: decode; gives "хъъ", the judge's extra-ъ slip (которыхъъ): the doubtful sign is the likely cause. Image not rechecked.
- S02? (l.6) - read: S02 = п; checked: decode; gives "впотребномъ" (judge S). Image not rechecked.
- S09? (l.8 end) - read: S09 = и; checked: decode; gives "писа" (judge S; the reading supplies [л] from the mark above the line). Image not rechecked.
- S04? (l.14) - read: S04 = е; checked: decode; gives "оное" (judge S). Image not rechecked.
- S01? (l.17) - read: S01 = к; checked: decode; gives "изконстянтино" (the slip is the я, not this sign). Image not rechecked.
- S01? (l.20) - read: S01 = к; checked: decode; gives "всячески" (judge S). Image not rechecked.
- [...] (l.16) - illegible sign (blot); checked: decode; the sense wants т ("происходитъ"). Image not rechecked.
- The doubtful pairs named in `SIGNS.md` (W/U, V/b, 8/y, x/X, D/A, p/n, q/Y) were not marked sign by sign; the six о-for-е slips fall on the W/U pair.

## Escalation

- [x] siblings: only l. 21 is imaged; the 1739 rescripts to Kalushkin with contemporary decipherments (SPbII RAN f. 178 op. 3) are recorded as a lead, not reachable
- [x] clear-pages: the clear opening of the leaf is the rescript itself, not a decipherment; it gave no key material and was not used
- [x] known-keys: no Russian Collegium key of 1737 is held in this repository or was found online (catalogue vetting key_check); none to compare
- [x] print: web searches in Russian and English, before and after the decode; Soboleva and AVPRI not reachable from here
- [x] key-rebuild: every sign valued; weak values listed above
- [ ] retry: a second, independent transcription from a better image is the next step (it would settle the о/е slips, the other slips and the line-end marks); not done under the freeze rule and for want of the image

## Files

Copied unchanged from the contributor's working folder (sha256, first 16 hex) [measured]:

| file | what | sha256 |
|---|---|---|
| `PRIOR_ART.md` | prior-art searches | b5f7de8ea80fa2fa |
| `FETCH_LOG.txt` | image URLs and failures, md5 | 56b8aee179c9b742 |
| `TRANSCRIPTION.tsv` | the frozen transcription | 340960006dbffafc |
| `SIGNS.md` | sign shapes, counts and conventions | 9fc9e0d6be748d56 |
| `FREEZE_TX.txt` | transcription freeze and split | 55fe0216a9890b6f |
| `SOLVE_LOG.md` | every solving attempt and the hand edit | 30cce95c7ce0a877 |
| `KEY.tsv` | the key of record | 6895d4783e6fa653 |
| `FREEZE_KEY.txt` | key freeze | 86e250a5e1530a75 |
| `decode_once.py`, `DECODE.txt` | the one decode (the decryption) | b15ecc7274b7fd04, cf6cfcb59ebe7775 |
| `shuffle.py`, `shuffle_out.txt` | shuffle control | 5f1d45f3d7fb32ef, 5253f78408ce0e82 |
| `judge/BRIEF.txt`, `judge/decode.txt`, `judge/judge.tsv`, `judge/count.py` | the strict judge's packet, scores and adder | 55522cc9e6d965f0, 2eb9839b8ca40b37, 1e3120c29f8a0efd, 55bbc44b82c52c36 |
| `scripts/common.py`, `crawl.py`, `crawl2.py`, `crop.py`, `mk_tx.py`, `rulm.py`, `solve.py` | helpers, corpus crawl, line crops, transcription builder, language model, annealer | 85ea8633d81d5370, 42fba7d2c278792a, 9417613d364cbb0c, 8949ec0335f8871d, 9015a73bccde6abb, 00662ef596c26557, a28d55a94c34b977 |
| `lmsrc/CORPUS_SHA256.txt`, `lmsrc/FETCH_LOG_lm.txt` | corpus hash and page list | 67879c036397b6c0, abd652a3ab704422 |
| `stamps/` (6 files) | manifest of the working folder and its time-stamps | MANIFEST.sha256 5f9246820d5722d9 |

The manifest in `stamps/` lists the working folder, including files not committed here (the corpus pages, crops and image).

Made here (24 Nov 2026): `transcription_l21.txt` (the 20 rows of `TRANSCRIPTION.tsv`, unchanged, with a header line), `reading.md`, `translation.md`, `validation.tsv` (input for `docs/_validate.py` once a Russian model exists), `profile.json`, this file. No images.

## Limits

- Model sessions did all the work: transcription, key recovery, decode, judge, reading and translation. No person read the signs or the text without AI.
- One transcription, one reader, one pass, from a thumbnail. The held-out lines test the key, not the transcriber.
- The held-out block is 148 letters on the same leaf as the training lines, and was seen as an image before the key was frozen.
- The judge was a model session scoring sense by its own lights.
- The reading, the translation and the historical setting are unchecked.
