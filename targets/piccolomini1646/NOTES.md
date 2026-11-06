# Catalogue 2358: two Italian cipher letters to Ottavio Piccolomini, c. 1646 (SOA Zámrsk, RA Piccolomini, inv. 24874, 24876)

WAINUT, 6 Nov 2026. Work done with AI language-model agents viewing the photographs; checked by script as described
below. No human palaeographer has checked the text. An independent AI language-model agent checked the work
(`VERIFY.md`); the fixes made after that check are listed in "Changes after the independent check". A later reading
review lowered both letters to "decoded, not read" (see "Reading review").

Status: not read; both letters decoded, not read (6 Nov 2026 reading review). **24874 and 24876 decode with Vlnas's
key, but most of their sentences have holes**, so neither counts as read or read in part. The photographs are too
coarse for a full sign copy. 24873 (with 24873_1, 24873_2) is the key source and a control, not claimed.

## Result in one paragraph

The system and the key are not ours. V. Vlnas deciphered the neighbouring letter, inv. 24873, in his 2017 thesis
(ch. 4.2) and printed its key (table 3): consonants written plain, vowels as odd digits a e i o u = 1 3 5 7 9, even
digits and the letters a e i o u w x y as nulls. That decipherment is prior art. What this folder adds is the first
reading of the two letters Vlnas left undeciphered (his appendix B21 and B22): a two-pass sign transcription of each
from the thesis photographs, the mechanical decryption with his table, and a marked reading with a draft English
translation. **24874: 76 of 116 words (65.5%) decoded verbatim from the signs. 24876: 32 of 50 (64.0%).** These are
word counts of the decode, not a read share: the words do not yet build sentences (24874: 2 of 6 cipher sentences
read; 24876: 1 of 3), so both letters are decoded, not read. Counted strictly, with no s/i or g/q/u/v class choice
(see System), 33 of 116 (28.4%) and 14 of 50 (28.0%). Marked repairs are counted apart (6 and 4 words). The writer
is not identified.

## Documents and images

| inv. | image | content | status |
|---|---|---|---|
| 24874 | Vlnas 2017, appendix zip P_lohy_A_a_B.zip (theses.cz/id/p3p2kb), frame 24874.jpg | one page, begins in mid-letter: 19 cipher lines, then 4 clear lines (news of the coming of Don Miguel de Salamanca, "Don Michele di Salamanca") | decoded, not read (65.5% verbatim) |
| 24876 | Vlnas 2017, appendix zip P_lohy_A_a_B.zip (theses.cz/id/p3p2kb), frame 24876.jpg | 9 clear lines, cipher block A (5 lines), 2 clear lines (news from Vienna: Linz, Ratisbona), cipher block B (5 lines), clear end | decoded, not read (64.0% verbatim) |
| 24873 (+_1, _2) | Vlnas 2017, appendix zip P_lohy_A_a_B.zip (theses.cz/id/p3p2kb), frames 24873.jpg, 24873_1.jpg, 24873_2.jpg | the letter Vlnas deciphered (ch. 4.2); key source and control | not claimed (prior art); a held-out excerpt of the 24873_2 postscript, see below |

The images are photographs of a microfilm-reader screen (2200 x 1650 px, rotated 90°), from the appendix of
V. Vlnas, *Počítačová analýza šifrované korespondence rodu Piccolomini* (BA thesis, Univerzita Hradec Králové 2017,
theses.cz/id/p3p2kb). A letter is about 15-20 px high. The originals are in SOA Zámrsk, Rodinný archiv Piccolominiů;
clean scans would have to be ordered there (not done). No images and no copy of the thesis are in this folder. There
is no interlinear gloss on 24873, 24874 or 24876.

## System

Consonants written plain; vowels as odd digits a e i o u = 1 3 5 7 9 (u also for v); nulls mixed in. Key: Vlnas 2017,
ch. 4.2, table 3 ("Dešifrovací tabulka", p. 33, from inv. 24873). That table is Vlnas's own modern decipherment, not
a contemporary one; it treats even digits and the letters a e i o u w x y as nulls ("–"). `key.tsv` has his values
and all his null rows. Our additions, not in his table: 0 = null (zero occurs five times on the two frames), f = s
(long s), and the class tokens S and G (below).

What we settled on the bare frames:

- **Even digits (2 4 6 8, and 0) are nulls.** 24874 has 65 of them in 645 signs (4: 40, 2: 12, 6: 9, 0: 4), 24876 has
  43 in 301 signs (4: 18, 2: 17, 6: 6, 8: 1, 0: 1) (`python scripts/signs.py`). Wherever the word around them reads
  as Italian, they carry no value: e.g. `d3S4Sd3r41` desidera, `4S20S1rS2S` (nece)ssarii, `b1t24t3r3` battere,
  `l124uG1nt1G2G57` l'avantaggio. They sit inside words, often between doubled consonants, never as a whole word
  except one group of nulls in 24876 L08. **Weak point:** in this hand a six is close to b and to t. At two places in
  24874 a six stands where the sense needs another letter: L06 `esi{+b}isce` and L09 `poli{+t}ico`. Both are marked
  as repairs. The rule "even digits are nulls" is therefore partly applied by sense where 6 and b/t are confusable.
  No even digit behaves as a code word.
- **Plain vowel letters are nulls** in the hand of 24876 (a 12, u 6, e 3, w 2), as Vlnas's table says; 24874 has three
  u. Example: `48ad52` = di, `l427 cwh3` = lo che.
- **Homographs.** In this cursive the digit five and the short letter s are the same shape on these photographs, and
  so are the digit nine and the letters g and q. The transcription keeps them as class tokens S and G
  (`SIGN_CONVENTIONS.md`); the reading chooses s/i and g/q/u/v by sense. This is a property of the system as written
  (Vlnas himself copied `S91` "Sua" as "sg11" in 24873), but it means many words depend on a context choice: 77
  class signs in the read words of 24874, 29 in 24876. The transcriptions also use a separate token `5` where the
  solver judged the shape a five, without a written criterion; the verifier wrote every such shape as S. The strict
  counts below therefore give the words with no S or G, and also those with no S, G or 5.
- The writer often writes a doubled consonant once (`3c34l3nz1` ecelenza, `GG3ul5` queli, `tr1l1Sc457` tralascio),
  as in 24873.

## Held-out excerpt (weak)

The key was frozen in `key_frozen.tsv` (Vlnas table 3 plus the null and class rules above) before the bare frames
were read, and then applied to part of the cipher postscript of 24873_2, which Vlnas did not print
(`heldout_24873_2_transcription.txt`, `heldout_24873_2_decryption.txt`). The 14 groups copied there all read as Italian
without change: `d3SS2d3r1 SG1 1lt3z4` desidera Sua Altez(za), `r1G22GG12GlS7` ragguaglio, `S7n7` sono,
`c7m3 1nc7r1 l35` come ancora lei, `c4h3 G3n3nd7` che venendo, `S3 n3 p7S24 G7G3rn1r3` se ne pos(sa) governare.

This is weak evidence, and it is not a blind score:

- The key is Vlnas's published table and could not have been tuned, so "frozen before" adds little.
- The solver chose the 14 groups ("only groups whose signs are clear") and scored them; there is no external
  decipherment of the postscript to grade against.
- The excerpt leaves out signs inside lines (now marked `[...]`): the verifier's blind copy has `w6Sl` (il) between
  `1lt3z4` and `r1G22GG12GlS7`, and about 20 signs before `c4h3` (among them `m3?GG24lS7` meglio).
- The freeze rests on file times only (key 15:12, held-out transcription 15:15, after the decryptions at 15:14);
  nothing was committed. The hash of the first frozen key is given in `key.tsv`. The null rows i, o, x, y were added
  to both key files after the check; no transcription uses them.

Read "14 of 14" as "the published key gives Italian on a selected excerpt". The stronger support for the key is
that it turns both bare letters, in two hands, into running Italian, on the solver's sign copy and on the verifier's
blind copy alike (`VERIFY.md` section 3). For a system this simple that settles the key; the reading is limited by
the photographs, not by the key.

## Method

Signs first: `SIGN_CONVENTIONS.md` was written before any value was applied; pass 1 (half-line strips 2.3x) and
pass 2 (fresh crops, other processing, 2.4-3x zooms) for each letter, reconciled on the image
(`transcription_<doc>_pass1/_pass2.txt` -> `transcription_<doc>.txt`, disagreements listed in the file headers).
Mechanical decryption: `scripts/decrypt.py` -> `decryption_<doc>.txt`. Marked reading in `reading_<doc>.md`.
`python scripts/check_marks.py` rebuilds both decryptions and the held-out decryption, checks key.tsv = key_frozen.tsv,
fails on any unmarked departure of the reading from the decryption, and prints the counts. It passes. It shows
consistency between the files only: a departure written into the transcription itself would not be caught (that is
what the independent check found, see below).

## Reading and counts (from `scripts/check_marks.py`)

| letter | words | verbatim from signs | verbatim % | verbatim, no S/G choice | verbatim, no S, G or 5 | marked repair | guess (context only) | holes | verbatim + repairs |
|---|---|---|---|---|---|---|---|---|---|
| 24874 | 116 | 76 | 65.5% | 33 (28.4%) | 29 (25.0%) | 6 | 7 | 27 | 82 (70.7%) |
| 24876 | 50 | 32 | 64.0% | 14 (28.0%) | 10 (20.0%) | 4 | 2 | 12 | 36 (72.0%) |

"Verbatim" includes the s/i and g/q/u/v class choices described above; the two "no ..." columns are the strict
figures. Words split by a line end count once per line. In 24874, "dal" (L09) rests on a doubtful sign; if that sign
is not 1, 24874 has 75 of 116 verbatim (64.7%). A unit like `in_tu{t/l}t{-t}i` counts both words as repaired.

**24874** (cipher part, Italian of the signs): "... Ecelenza havrà recevuto la mia delli [?tredeci] et ... gran
consolazione dalla di lei [?lettera], tanto più per vedere [...] ... si esibisce di darli parte minutamente come si
[?ritrovano] ... modo et governo ..., a sì come dal governo politico. Desidera dunque una giusta et per[...] relatione,
mentre lei sa meglio queli avertimenti [?che siano] necessarii. Di quelo so tralascio per non tediarla. ... le
particolarità che ... per il governo ... del arciduca mio signore, asicurandola che oltre ... che ne cavarà, havrà
consolatione ..." The writer reports for someone he calls "l'arciduca mio signore"; the partly read middle speaks
of a "modo et governo" and of "the political government" (whether a military government is meant is not read); the
clear tail announces Don Miguel de Salamanca. Lines L01-L03 (faintest on the
photograph) are mostly holes.

**24876** (cipher parts): A "di Baviera non [?vengono] ... lo che si dobiamo battere ... di lamentationi; tutta già
se li risponde ... et il dovere ..."; B "... duca di Baviera vuoglia in tutti modi la pace, sì che [?puol] considerare
l'avantaggio che noi havremo". The clear text speaks of prisoners' reports on the enemy, Bavaria, and news from
Vienna of a journey to Linz and then Ratisbona.

Full texts with every hole, and English translations: `reading_24874.md`, `reading_24876.md`. The clear passages
there are draft readings from the photograph and are not part of the counts.

## Historical context (cautious)

Inv. 24873-24876 sit in the run of RA Piccolomini cipher frames that Vlnas dates, where dated, to 1646. 24873_2 is
dated in clear "li 13 [?9bre] 1646" (place read uncertainly as "Lammeling"). In 1646 Piccolomini served Spain in the
Low Countries; Archduke Leopold Wilhelm was named governor of the Spanish Netherlands at the end of 1646, which fits
24874's "governo ... del arciduca mio signore" and "governo politico", but nothing in the text names him.
24876's Bavaria passages ("the Duke of Bavaria wants peace by all means") fit Bavaria's moves toward a separate truce
in late 1646 (Ulm, March 1647); again this is context, not a statement of the letter.

## Writer

Not identified. 24874 and 24876 are in different hands (24876 upright, with plain vowel letters as nulls), using the
same key. 24873_1 (same hand and cipher style as 24874) also mentions Don Michele di Salamanca, so 24873 and 24874 are
likely one writer; 24873_2 ends with a flourished subscription that is not legible on this photograph. Nothing in the
cipher or clear text of 24874 or 24876 names the writer. A clean scan of 24873_2's signature is the obvious next step.

## Prior art (checked 6 Nov 2026)

- Vlnas 2017: ch. 4.2 deciphers inv. 24873 only (his decryption covers the 24873 frame's cipher lines; it is the key
  source, and the key is his). 24874 and 24876 are appendix B21 and B22, in the appendix titled as photocopies of
  cipher texts not deciphered in the thesis; no text of them is printed. The 24873_2 postscript is listed (A05) but
  not printed.
- Web search (6 Nov 2026) for Piccolomini 1646 cipher letters with "Michele di Salamanca": no edition or
  decipherment found. The catalogue's vetting (6 Nov 2026) found none in the DECODE dumps, Lasry's list, Tomokiyo or
  HistoCrypt 2018.
- Collision check: no target folder for these items in the repository; catalogue 2358 is still listed as bare, and
  the items are mentioned only in the catalogue's own sweep and vetting notes.

## Changes after the independent check (6 Nov 2026)

The verifier (`VERIFY.md`) confirmed the key and, at the time, both "read in part" statuses, and asked for eight
fixes. All are made; none changed a status. The statuses were later lowered at reading review (below).

1. 24874 L09 and L12: the first reconciled copy wrote the sign the sense needs where the passes and the blind copy saw
   another (`p7l5t5c7` for `p7l565c7`, `l54t5` for `l546?5`, `m3nt?5` for `m3nl?5`). The transcription now keeps the
   shapes the passes saw, and the reading marks `poli{+t}ico` and `avertimen{t/l}i` as repairs. `d1l` is now `d1?l`
   and "dal" is flagged. 24874 verbatim fell from 78 to 76 of 116.
2. The header of `transcription_24874.txt` now says that pass 1 and pass 2 agree on 6 (L09) and l (L12).
3. 24874 L12 `S4tn7`: the t is under an ink blot; now `S4[?]n7`.
4. 24876: L02 `d76?ubS1m7` (a missed b/6 sign), L04 `c7nep?7r02a43` (a, not n; p or f open), L07 `a?b1G453r1` (a
   missed u/a loop). All three are nulls; no word of the reading changed. 24876 now has 301 signs.
5. The counts table gives verbatim % first (65.5% and 64.0%; the first version's headline 71% and 72% included the
   marked repairs) and the strict figures with no class choice. `scripts/reading.py` computes them.
6. The held-out excerpt shows its in-line gaps and is described above as a selected excerpt, not a score; the hash of
   the first frozen key is recorded.
7. `SIGN_CONVENTIONS.md` now states how the token `5` was used; the key lists Vlnas's null rows i, o, x, y and says
   which rows are our additions (0, f, S, G).
8. Internal workspace references were removed from these notes.

The verifier's figures in `VERIFY.md` predate these fixes. The scripts now set UTF-8 console output.

## Reading review (6 Nov 2026)

A reviewer independent of the solver (an AI language-model agent, for WAINUT) read each cipher sentence against the
translation and three lines per letter against the photograph, as the repository's review rule asks. Result: holes in
most sentences, so both letters are **decoded, not read**, and the target is classed "not read". No reading_review
grade is recorded, since a "decoded, not read" entry needs none.

- **24874**: six cipher sentences; two read ("Desidera dunque una giusta et per [...] relatione, mentre lei sa meglio
  queli avertimenti [?che siano] necessarii"; "Di quelo so tralascio per non tediarla"). The middle (L03-L09) gives an
  outline, but its two sentences carry 7 and 6 holes or guesses. L01-L03 have 11 holes or guesses in 22 words; L14-L20
  have 10 holes in 33 words. Of the 76 words decoded verbatim, 43 rest on an s/5 or g/q/9 choice made by sense.
- **24876**: three cipher sentences, all with holes. Block B holds after three opening holes and one guess ("[...] duca
  di Baviera vuoglia in tutti modi la pace, sì che [?puol] considerare l'avantaggio che noi havremo"). Block A does not
  build sentences (6 holes or guesses in 17 words; 4 in 12). Of the 32 words decoded verbatim, 18 rest on a class
  choice.
- **Sentence check** (`docs/_check_reading.py`, language "it", as the repository check runs it): 15% of sentences
  clean on `reading_24874.md` (11 of 73), 28% on `reading_24876.md` (12 of 43). On the cipher prose alone: 1 of 8 clean
  in 24874, 0 of 3 in 24876 (the clean sentences of 24876 are all in the clear passages, which are not counted). A
  local run without a language gave 41% and 42%, because it guessed "es" and scored each sentence against every word
  list; those figures are not the check's.
- Open: 24874 L01-L03 and L14-L20, 24876 block A, ideally from a clean scan; that may raise either letter to "read in
  part".

## Remaining gaps

- 27 + 12 holes, mostly in 24874 L01-L03 and in words where several signs are doubtful at this resolution. A clean
  scan (SOA Zámrsk) would likely raise both letters much further. (illegible on the photographs)
- About 15 of 357 compared signs are unresolved at this resolution (VERIFY.md section 2), among them 24874 L08
  `61St4G...`, L19 `Snc7n??S1r1`, 24876 L04 `Sl?S72G3`; all in holes. (illegible on the photographs)
- The s/5 and g/q/9 homographs: most read words depend on a class choice by sense. (property of the system)
- The clear passages are given as draft readings only. (not attempted in full)
- The writer and the date of each letter. (not attempted beyond the context above)
- The two letters may later be split into separate target folders (different hands).

## Escalation

- [x] siblings: Vlnas's key for 24873 (same microfilm run, same system) applied to both letters
- [x] print: Vlnas 2017 read for the key and for what it prints; web search for an edition
- [ ] clear-pages: the clear passages are read only in draft
- [ ] retry: a clean scan from SOA Zámrsk (not ordered) for the holes, the unresolved signs and the signature of
  24873_2

## Files

`SIGN_CONVENTIONS.md`, `transcription_24874{_pass1,_pass2,}.txt`, `transcription_24876{_pass1,_pass2,}.txt`,
`decryption_24874.txt`, `decryption_24876.txt`, `reading_24874.md`, `reading_24876.md`, `translation_24874.md`,
`translation_24876.md`, `key.tsv`, `key_frozen.tsv`, `heldout_24873_2_*.txt`, `scripts/decrypt.py`,
`scripts/reading.py`, `scripts/check_marks.py`, `scripts/signs.py`, `VERIFY.md`. The scripts use the standard library
only. Scans and the thesis are not in git.
