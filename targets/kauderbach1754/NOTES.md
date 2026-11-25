# Kauderbach (The Hague) to Friedrich August II, 1754-58 — KHA Prins Willem V inv. 201

Status: in progress. Nine letters read; R1954 decoded, not read (reading audit, 22 Oct 2026).

**23 Oct 2026, re-read (REREAD_BRIEF, batch b29)**: R1954 still **decoded, not read**. The 314 digits the September
transcription marked uncertain were resolved by a French 5-gram beam over the look-alike pairs and checked by eye
(`trans/R1954_b29.txt`, helper `research/reading_audit/b29_kd_beam.py`); seven places corrected on the images
(`trans/R1954_b29_corrections.tsv`: *l'inpossible*, *le colonel Yorcke*, *deux objets*, *six mille hommes*, *de la
proteger* ...). Partial reading `read/R1954_partial_reading.md` (0.549 clean sentences; explicit holes 0.725), English
`read/R1954_en.md`, log `read/R1954_reread_log.md`. The arguments paragraph (why Holland cannot refuse the 6,000 men)
now reads; the d'Affry clause and most of f. 4 do not: copyist's slips in this intercept copy, the Dresden original
not online. Key unchanged.

**22 Oct 2026, reading audit** (George Lasry's test): nine of the ten hand readings build French sentences. read/R1954.txt (March 1756, about 65% read on a weak transcription) has holes in most sentences: *decoded, not read*. Class read -> read in part; fraction_read 0.998 (groups given a value) -> 0.81 (groups in letters that read).

Earlier status (before the 22 Oct 2026 reading audit): read (19 Sept 2026); written up as docs/kauderbach1754.html

Catalogue target: Johann Heinrich Kauderbach, Saxon-Polish resident at The Hague, despatches to Dresden intercepted
by the Dutch (copies in the Stadtholder's archive, KHA Prins Willem V inv. 201). DECODE R1043, R1044, R1954, R1958,
R1959, R2078-R2082 (10 records, 32 pp.). DECODE: "None of the encrypted messages by Kauderbach intercepted in The
Hague were ever solved"; "codegroups are not separated".

## Material

- `decode/rec*.htm` record pages; `decode/DOC_R1043/R1044/R2078_*.txt` DECODE manual transcriptions (only three).
- `img/` full-resolution PNGs (git-ignored, DECODE login images). `sm/` previews (git-ignored).
- `trans/R*.txt` new transcriptions of the other seven records (this project, 2026-09-19).

## Prior work

- Web search (2026-09-19): Sächsische Biografie entry; no printed decipherment of Kauderbach's cipher found.
  Originals in Hauptstaatsarchiv Dresden (Geheimes Kabinett, Gesandtschaften) — not online here.

## The copies

Intercept copies, clear French with cipher passages. Cipher = continuous digit runs, no separators, with clear
abbreviations inside the runs (`E.M.`, `C./.`, `Q./.`, `M./.`, `S./.`, `J./.`, `T./.`).

## Analysis log

1. Digit counts over the three DECODE transcriptions (6,096 digits): 2 1012, 1 964, 9 910, 4 825, 6 696, 3 664,
   7 411, 0 401, 5 135, 8 78. Strongly skewed successor table (6→3/9, 1→6/9/4, 0 never →0/5/8).
2. No 2- or 3-digit phase preference from segment starts (IC 1.98/1.96 and 3.61/3.59/3.61): groups are of
   variable length. Transcribers' spacing does not mark groups.
3. Long exact repeats (e.g. `02 69143116921929144424` ×4, `7969 4716419474792 13` ×4, `11696324` ×8): a fixed
   code, not a running key.
4. Digits 5 and 8 are never inside a code group: dropping them (single-digit nulls) gives a clean 2-digit phase
   (IC 2.72 vs 2.10; 4-phase 0.155/0.161 vs 0.103/0.103). Code table after re-alignment (`align.py`, Viterbi
   pair model with skip penalty): first digit in {0,1,2,3,4,6,7,9}, second in {1,2,3,4,6,7,9}; ~50 codes in real use.
   The same pair profile in every letter: one key for 1754-58.
5. Letter-homophonic solves (quadgram coordinate ascent, validated on synthetic French at 98% with 2% noise and
   through the full digit pipeline) fail on the real stream (-4.7 to -5.1 per token vs -3.9 synthetic); German,
   Dutch, Italian, word-reversed French, null codes, merged look-alike digits (4/7, 1/7, 1/4, 6/0): all fail.
6. **Sibling key found: DECODE R936**, "Kauderbach in Den Haag - Saxony 1761" (HStAD 10024 Loc. 08236/11 Bl. 5),
   transcribed on DECODE. One code per letter or syllable (a ai an au b be ... que qui ... vous), capital letters for
   names (S = la Hollande, Q = la Russie, T = l'Angleterre, U = la France, W = la Reine, Z = l'Empereur, ...),
   and "6 est faux chiffre" (a declared null). Explains our 5/8 nulls and the `S./.`, `Q./.` markers. The 1761
   numbers themselves are a different table (they use 5 and 8). Next: solve the 1754 table as a one-to-one
   assignment onto the 1761 vocabulary (`perm.py`).
7. **Solved (19 Sept 2026).** `perm.py`: simulated annealing over a one-to-one assignment of the 61 codes onto the
   1761 vocabulary (letters + syllables, `m` added after checking the R936 image, where DECODE's "30 - ni?" is m),
   char-4-gram score. Seeds 22 and 24 converged independently to the same key (-3.847/letter, synthetic French
   -3.95). Refined with an extended vocabulary (`perm2.py`, then by reading): 27 = in, 91 = ou, 33 = qu, 79 = st,
   17 = par, 22 = pas, 46 = qui, 60 = ent, 77 = nt. Key in `key.json`; decoder `decode.py`; machine readings
   `read/machine_R*.txt`; code-level lookup `codes.py`.
   First readings: R2078 (24 Dec 1754) "il n'y a pas eu depuis longtems une assemblée des etats de Hollande dont
   les objets de deliberation soient eté plus importans ... les ouvertures faites par le comte d'Affry ... le
   colonel Yorck ne s'endort pas dans ces circonstances"; R2080 (22 Jul 1755) the debate in the Estates on the
   13,000-man augmentation ("le lord Holderness l'a fait connaitre ici"; first written 30,000, see 9); R1959 (5 Aug 1758) "le bruit que [E.M.]
   est en negociation avec [P.] ne parait pas etre entierement sans fondement".
8. Lengths (measured, `cipher/R*.txt`, pairs after null removal): R1043 1054, R1044 628, R1954 1621, R1958 542,
   R1959 391, R2078 1231, R2079 558, R2080 1260, R2081 802, R2082 425; all 8,512 groups, 62 distinct, IC 0.036.
   The capital-letter names (E.M., P., J./C., Q., S., Y., M.) are clear sigla whose 1754 meanings are not those
   of the 1761 table; read from context only.
9. **Corrections (30 Sept 2026).** Four phrases in `read/R1043.txt`, `read/R2080.txt` and the write-up had been
   normalised away from the figures; each re-checked group by group in `cipher/R*.txt` with `key.json`, and against
   `read/machine_R*.txt`. R1043: "parce qu'on croit qu'il y a des articles secrets qui vont encore plus loin" is
   "parce qu'on craint qu'il n'y ait des articles secrets qui aillent encore plus loin" (43 92 12 32 29 c-r-ai-n-t;
   33 93 32 13 12 29 qu-il-n-y-ai-t; 46 12 69 07 32 29 qui-ai-l-le-n-t; "croit ... y a ... vont" was probably a
   paraphrase of the pre-swap machine text, where 12 gave "croint ... nyoit ... quioillent"); "l'on a dit aussi beaucoup de reflexions" is "l'on a
   fait aussi ..." (69 44 19 23 29 l-on-a-fai-t). R2080: "une augmentation de trente mille hommes" is "treize mille"
   (29 03 14 77 16 t-re-i-z-e, seen on image IMG_R2080_I14904_P2, line 8 of figures: 0229031477 16; 77 = z in
   `key.json` as in declarez, assez, Zelande, not the "77 = nt" of item 7), so the debate is over a 13,000-man
   augmentation; the "30,000" in the profile's verification step came from the misreading. "sacrifier jusqu'au
   dernier sol et combattre" is "... pour combatre" (66 96 94 31 19 29 03 pour-co-m-b-a-t-re; no 26 = et). Corrected
   in both reading files and in the write-up (summary, R2080 and R1043 extracts). Still to correct in the shared
   files: `decode_updates/decryptions/R1043.txt` and `R2080.txt` repeat the old wording.

## Verification 5, 23 Oct 2026

Plain-bar check (French 1754-56): R2078, R1958, R2079 and R1043 had been scored on `read/R*.txt` whole (heading line,
English summaries of the clear passages, key notes). The French cipher texts are now written out alone in
`read/R*_reading.md`: plain 0.618, 0.647, 0.75, 0.6; explicit 0.794, 0.882, 0.938, 0.68. All keep read; R1043 sits at
the bar, its failing sentences carrying unread name codes.

## Decrypt audit, 16 Nov 2026

The audit (`research/decrypt_audit/`) applies `key.json` to `cipher/R*.txt` and compares the letters with the reading. It found 346 of 2,469 compared words departing over the ten letters (R2078 42 of 352, R1958 17 of 165, R2079 19 of 174, R2080 47 of 365, R1959 10 of 118, R2081 29 of 260, R2082 13 of 124, R1044 17 of 184, R1954 106 of 442, R1043 46 of 285). Checked here with a comparison written for this purpose (read-only; no script of this folder was run):

- **The key file is the key that was used.** `key.json` applied to `cipher/R*.txt` gives the letters of `read/machine_R*.txt` exactly, in all ten letters. No code value is in the scripts or in these notes that the key file lacks. The departures lie between the machine decryptions and the hand readings (`read/R*.txt`, copied into `read/R*_reading.md`).
- **Letters changed in the readings without a mark** (nine letters that read; 291 of 2,044 words differ from the machine decryption, about 240 of them in this way). Where the decoded string is not a French word the reader printed the word meant: `dessaance` printed "d'esperance" (R2079), `neracastle` printed "Newcastle" (R2079), `tcerande` printed "grande" (R1958), `necessila` printed "necessité" (R2080). Several are a figure taken for its look-alike in the transcription and put right in the reading only: 41 (la) where 71 (te) is meant, three times; 09 (ne) where 69 (l) is meant, twice; 14 (i) where 44 (on) is meant, twice. The `Slips:` lines of `read/R*.txt` name a few of these; the reading files carry no mark at the words, and their headers explain only `[...]` and `[?]`. By letter (words differing, of words compared): R2078 53 of 352, R1958 20 of 165, R2079 20 of 174, R2080 53 of 365, R1959 11 of 118, R2081 34 of 261, R2082 14 of 125, R1044 33 of 195, R1043 53 of 289. The readings were not changed in this check.
- **Spelling normalised** (about 50 of the 291 words): a consonant doubled (`aparences` printed "apparences", `oposans` "opposans"), `in` before p or m printed "im" (`inpossible` "impossible", code 27, five times), final z printed s (`degrez` "degrés", code 77, five of its 11 uses), a plural or verb ending added (`diminue` "diminuent").
- **Code 49.** `key.json` has 49 = sa. The readings print "per" at five of its ten uses: "permissent" (R2078), "esperance" (R2079), "permettant" (R2080), "desespere" (R2081), "desesperoit" (R1958). At two more the figures fit "per" and the reading prints another word: 39 92 24 49 24 14 24 29 ... gives `prs-49-sistant`, read "s'obstinant?" in the notes of `read/R2078.txt`, and `etre 49 suade` (R1958) is printed "etre assuré". With "sa" none of the ten uses gives a word. No file of this folder states 49 = per, so `key.json` was left as it is; the value needs a decision, and the validation figures were computed with 49 = sa.
- **Code 13.** `key.json` has 13 = y. The notes of `read/R1043.txt` and `read/R1044.txt` give it a second value, re ("membres", 94 16 94 31 13 24; "reflexions"), and the readings print it so twice. `key.json` holds one value per code and was not changed.
- **R1954: transcription and reading out of step.** `cipher/R1954.txt` and `read/machine_R1954.txt` are the September transcription (`trans/R1954.txt` decoded gives the same 2,273 letters). `read/R1954_partial_reading.md` was made from `trans/R1954_b29.txt` (23 Oct), which has no `cipher/` file. Against the September state 121 of the 533 words of the partial reading differ; against `trans/R1954_b29.txt` decoded with `key.json`, 37 do. The profile lists both transcriptions and three published files for this letter, and the audit script joins them, so its figure for R1954 (106 of 442) measures nothing.

Nothing was changed in the key, the transcriptions or the readings, so the audit figures are the same after this check. Not checked: the transcriptions against the images, and whether each corrected word in the readings is right.

**Marked on 16 Nov 2026.** `mark_emendations.py` (new) aligns each of the nine `read/R*_reading.md` with `read/machine_R*.txt` and puts square brackets round every letter of the reading that the machine decryption does not give; a word with half or more of its letters not given is bracketed whole. It checks that the text without brackets is unchanged. Marked: R2078 41 places (39 words of 352), R1958 14 (13 of 165), R2079 10 (10 of 174), R2080 43 (43 of 365), R1959 5 (5 of 118), R2081 25 (25 of 261), R2082 8 (7 of 125), R1044 23 (23 of 195), R1043 42 (37 of 289): 211 places in 202 of 2,044 words. This exact alignment replaces the estimate of about 240 words above. Each file got one header line explaining the marks and the three spelling conventions that are not marked (a doubled consonant, m for n before p, b or m, s for z: 59 letters). Not markable: 378 letters of the machine decryptions that the readings leave out, some inside words and some in stretches the reading gives as `[...]`; they are listed in `emendations.tsv` as dropped. Left unmarked: `read/R1954_partial_reading.md` (37 words differ from `trans/R1954_b29.txt` decoded; the folder has no machine file for that transcription), and the older hand readings `read/R*.txt`, which carry the same wording without marks. With each marked word counted as a hole (`research/reading_audit/v2_score.py`), the hole rates are: R2078 0.065 before, 0.165 after; R1958 0.041, 0.107; R2079 0.020, 0.070; R2080 0.017, 0.126; R1959 0.015, 0.052; R2081 0.029, 0.111; R2082 0.028, 0.077; R1044 0.035, 0.132; R1043 0.096, 0.200. All nine are now over 0.05; the states in `profile.json` were not changed.

## Remaining gaps

- R1954 (March 1756, 1,621 groups): decoded, not read - blocker: needs-physical-access; re-read 23 Oct 2026 (b29): uncertain digits resolved, seven places corrected on the images, partial reading 0.549; the remaining runs (f. 2 ll. 6, 8, 13; f. 4 ll. 6-10, 17-25) read legibly but do not decode, copyist slips; the original in HStA Dresden is not online
- nomenclator names left as code letters ([C./.], [Q./.], [S./.] ...) - blocker: no-key-material; the 1761 key R936 does not carry this table's names

## Escalation

- [x] siblings: all ten records of KHA Prins Willem V inv. 201 decoded with one key
- [x] clear-pages: 23 Oct (b29): R1954's four DECODE images and record checked; the clear passages are the copy's own (Hessian courier, N. 21), no decipherment on the record
- [x] known-keys: Kauderbach's 1761 key R936 (vocabulary only; numbers differ)
- [x] print: 19 Sept web search found no printed decipherment of Kauderbach's cipher (not repeated 23 Oct); the originals are in HStA Dresden (not online)
- [x] key-rebuild: table recovered by annealing
- [x] retry: 23 Oct (b29): R1954 uncertain digits resolved and checked on the images, partial reading written (`read/R1954_reread_log.md`)
