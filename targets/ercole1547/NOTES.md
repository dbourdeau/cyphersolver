# ercole1547: Ercole II d'Este to his secretary Claudio Ariosti, Ferrara, 8 Jan 1547, on the rising at Genoa (Biblioteca Estense, Autografoteca Campori, Ercole II, c. 16v; catalogue 2160)

Status: in progress. Contributed by pull request, not yet written up: the key was recovered from cipher lines 1-6 alone, frozen, and used for one decode of all 8 cipher lines (strict judge 388 of 435 letters, 89.2%; held-out lines 7-8 81 of 92, 88.0%). By the README read bar, counted in words, 77 of 98 words read as sense (0.786) with the one-letter slips counted as holes, so the target is filed read in part. The page, ledgers, DECODE queue and catalogue edit are left to the maintainers.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic): Claude Fable 5.2 the solver session, Claude Opus 5.5 the strict judge and the assembly of this folder. Earlier attempt on this letter: Brice Dudout, 5 Nov 2026, "Not solved" (`targets/ariosto1559/NOTES.md`, "Not read, declared").

Provenance tags: [measured] = counted or hashed from the files in this folder; [derived] = worked out from them; [sourced] = from a named source; [stated] = given by the contributor's working session, not checked here; [unverified] = a reading of the text not checked by anyone else.

## The source

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Ercole II d'Este, sfasc. I, cc. 16-17 (IIIF manifest https://edl-jarvis.cultura.gov.it/meta/iiif/89e1bdc6-a46d-4627-9770-efbd17e544fb/manifest). Ercole II to "Secretario n[ost]ro d[omi]no Claudio" (address on c. 17v, with "Cesarem"), date line "Ferrariae viij Jan. 1547" on c. 16v [sourced: the images]. The Estense record calls it "Lettera in parte cifrata" [sourced: as quoted in catalogue 2160].

| page | what is on it |
|---|---|
| c. 16r | clear |
| c. 16v | 10 clear lines, **8 cipher lines**, 2 clear lines, date |
| c. 17r | blank |
| c. 17v | address |

All four pages were viewed; there is no other cipher in the bifolium [stated]. The rest of the Ercole II folder in Campori was not swept for the same table.

Images (Estense, CC BY-NC-SA): **none is committed**. URLs and md5 in `FETCH_LOG.txt`; the cipher lies in region 250,2060 to 3050,3458 of canvas c2b5abe3 (https://edl-jarvis.cultura.gov.it/images/iiif/db/c2b5abe3-6d37-4eb8-9596-90b67184eb16/full/1000,/0/default.jpg for the whole page). Full-size requests were refused (HTTP 422); native-resolution crops were served.

Length [measured]: `python docs/_check_profile.py --measure transcription_c16v.txt --drop-first` gives 290 whitespace tokens = 276 signs (each with its raised mark; 160 marks) + 13 dots + 1 punctuation `{:}`. 25 sign shapes, 15 raised marks (`SIGNS.md`). The frozen key gives 435 letters (`validation.tsv`, `judge/judge.tsv`: 55 + 55 + 60 + 59 + 59 + 55 + 57 + 35 = 435).

## The system (`KEY.tsv`)

A sign-and-vowel table of the Este chancery, the same family as `ariosto1559` (catalogue 2159) but a different table [derived: PRIOR_ART.md compares the two].

- Raised figures give the vowel after a consonant: 4 a, 5 e (drawn as an S-curve), 6 i, 7 o, 8 u. A raised 4 drawn as a cross = a.
- Figures and some signs on the line are vowels: S16 (4) a, S21 (5) e, S09 (6) i, S07 (7) o, S23 (8) u; also S15 e, S20 a, S18 o, S08 i, S06 u/v.
- Consonant signs that take a raised figure: S01 p, S02 r, S11 t, S12 d, S13 qu, S17 s, S03 c (S24 an oval form of c).
- Consonant signs that take a stroke for the vowel: S14 l, S10 n, S04 m, S19 g (S25 a form of g); / a, \ e, upright stroke o.
- A bar over a consonant doubles it (ll, cc, ss); dots on the line beside barred signs carry nothing (nulls).
- S05 (d with a raised cross), always after S03 = "he": che.
- Weak values, frozen as they are: raised 9 = o (cosa wants o, circa wants a: one use each); raised 2 = o (como, one use); S10 under a bar = "ni" (ogni, twice, although a bar doubles elsewhere); S02^^ = "ri" (one use, set by sense); S02^/ = "za" (importanza; the sign is doubtful); S09^- = "fa" (per fare).
- No value: S01^4s, a code sign for a person, twice ("sia per castigare", "sia per fare"; the Emperor fits, unconfirmed); S12^- (h with a cross-stroke), once in line 5.

## Method

The pipeline is the contributor's (prior art first, frozen transcription and key, one decode, a separate strict judge, a shuffle control). Dates are 24 Nov 2026, Brisbane time.

1. **Prior art** before transcription: `PRIOR_ART.md`. No key, decipherment, gloss or printed reading found. See "Prior art" below.
2. **Transcription** from native-resolution IIIF crops, by one Claude Fable 5.2 session, one pass, blind to any key (none exists): signs by shape, raised marks, dots, 12 doubtful tokens marked `?` (`TRANSCRIPTION.tsv`, conventions in `SIGNS.md`). Frozen with the split at 09:28 UTC (`FREEZE_TX.txt`; sha256 of `TRANSCRIPTION.tsv` 4a970edd... and `SIGNS.md` b69865e7..., both matching the files here) [measured].
3. **Held-out design.** BUILD = lines 1-6 (216 signs); HELD-OUT = lines 7-8 (60 signs, 21.7% of 276). Only one page carries cipher, so the held-out block is the last two lines of the same page. A note made before solving recorded that 276 signs is short and the shuffle control might fail on length.
4. **Key from lines 1-6 only** (`SOLVE_LOG.md`, `log/`, `work/`), with a local Italian 5-gram model (`work/build_lm.py`: the registry's it-gutenberg corpus plus the Serristori legations; the registry model it-cinquecento could not be built because gutenberg.org answered 503):
   - Counts by sign split the consonant signs into two classes (raised figures against strokes).
   - Annealing on five structural models (A, B, B2, B3, C; 3 to 4 seeds each) did not converge on the consonants, but model B gave raised 5 = e, 6 = i, 7 = o in 4 of 4 runs and 4 = a in 3 of 4. Every run is logged, failures included.
   - With the vowel figures fixed (model B5), one seed of five read "intenderete", "opera per intendere", "potrete", "e da credere"; the others failed.
   - In parallel, by hand: the pattern S09 S10 S11^5 S10 S12^5 S02^5, twice (lines 1 and 3, once followed by S11^5) = "intendere", "intenderete". That gave "per" (10 times), "opera per intendere", "piu che potrete", and the rest of the key by sense from lines 1-6.
   - **Crib caveat:** "intendere" also stands in the clear lines of the same letter ("vederete intendere"), which the solver could see on the image. The word was found as a repeated pattern in the cipher, but the method label "key recovered from ciphertext-only" should be read with that in mind; `profile.json` lists "cleartext context" among the inputs.
5. **Key frozen** at 09:54 UTC (`FREEZE_KEY.txt`: `KEY.tsv` sha256 6fb733eb..., `decode_once.py` c11fffb1..., both matching the files here) [measured]; then **one decode** of all 8 lines (`decode_once.py` -> `DECODE.txt`). No emendations. The first pass is the figure of record.
6. **Separate strict judge** (Claude Opus 5.5): saw only `judge/BRIEF.txt` and `judge/decode.txt`; scored every decoded letter S (sense), E (one-letter slip in a readable word) or N (no sense) (`judge/judge.tsv`). `judge/count.py` re-adds it [measured, re-run here].
7. **Shuffle control** (`shuffle.py`, `shuffle_out.txt`): 5,000 shuffled keys per seed (values permuted within consonant bases, vowel bases and vowel marks), same local model, mean log-probability per letter.

The scripts were run in the contributor's working folder and keep its paths (`/home/claude/keyless/ercole1547/`, a private copy of `lang/`). They do not run from this folder without changing those paths. The 31 MB local model table is not committed.

## Figures (first pass of record)

Strict judge, letters (`judge/judge.tsv`, re-added by `judge/count.py`) [measured]:

| line | split | S | E | N | letters | S share |
|---|---|---|---|---|---|---|
| 1 | build | 55 | 0 | 0 | 55 | 100.0% |
| 2 | build | 46 | 2 | 7 | 55 | 83.6% |
| 3 | build | 59 | 1 | 0 | 60 | 98.3% |
| 4 | build | 46 | 1 | 12 | 59 | 78.0% |
| 5 | build | 47 | 1 | 11 | 59 | 79.7% |
| 6 | build | 54 | 1 | 0 | 55 | 98.2% |
| 7 | held-out | 52 | 5 | 0 | 57 | 91.2% |
| 8 | held-out | 29 | 0 | 6 | 35 | 82.9% |
| lines 1-6 | build | 307 | 6 | 30 | 343 | 307/343 = 89.5% |
| lines 7-8 | held-out | 81 | 5 | 6 | 92 | 81/92 = 88.0% |
| page | | 388 | 11 | 36 | 435 | 388/435 = 89.2% |

Sensitivity [derived]: "perosuntione" (line 4) has 12 letters, scored 1 E and 11 S by the judge. If the whole word were scored N, 11 S letters go: line 4 35/59 = 59.3%, page 377/435 = 86.7%, still over the project's 65% line.

Read share by words, the README read bar (`reading.md`) [measured: 98 words counted from the file]:

- Holes: 8 words with no sense (icciate, quesot, delill, sot, the unvalued sign, rit, diare, arirui) and the code sign twice = 10.
- One-letter slip words, left as decoded and marked `*`: essre, impertanza, circo, perosuntione, essende, italla, rancesi, oi, le, dillgentia, estraoodinaria = 11. The README rule of 19 Nov 2026 counts only sure words as read, so they are counted as holes here.
- **Read share 77/98 = 0.786**; 88/98 = 0.898 if the slips were counted as read. Both are under 95%; the text builds coherent sentences except the line 4-5 stretch, so it is **read in part**.

Shuffle control (`shuffle_out.txt`) [measured]:

| split | real key | shuffles mean (sd), seed 20261112 | best shuffle | z | shuffles at or above real |
|---|---|---|---|---|---|
| held-out lines 7-8 | -2.284 | -5.184 (0.455) | -3.439 | 6.4 | 0 / 5,000 |
| build lines 1-6 | -1.876 | -4.803 (0.370) | -3.574 | 7.9 | 0 / 5,000 |
| whole page | -1.963 | -4.886 (0.360) | -3.691 | 8.1 | 0 / 5,000 |

Seed 7 gives z 6.3, 7.9 and 8.1, 0 / 5,000 each.

Repository validation (`python docs/_validate.py ercole1547 --write`, 24 Nov, on `validation.tsv`: the 276 signs of `TRANSCRIPTION.tsv` with their `KEY.tsv` values through `decode_once.dec_token`, dots as nulls, the code sign and S12^- unread) [measured]: it-cinquecento, order 4: reading -1.985 per letter; 200 random keys -3.253 (sd 0.120, best -2.984, z 10.6); a key annealed onto shuffled ciphertext best -2.309 (6 shuffles, z 33.2); the annealer on the real text from random keys reaches -2.271, below the reading. Verdict: pass (recorded in `profile.json`). The it-cinquecento corpora were fetched for this run with the Gutenberg texts from the aleph.pglaf.org mirror (gutenberg.org answered 503), same files and paths.

Repository sentence check (`python docs/_check_reading.py ercole1547`) [measured]: `DECODE.txt` 12 of 13 sentences clean (0.923, "marginal"); `reading.md` 5 of 9 (0.556), hole rate 0.193. The class rests on the word count. (A reading review signed by our own session was withdrawn on 27 Nov 2026; see "Reader's notes" below.)

## Gist [unverified: the contributor's reading of the decode, not checked by a person or against any source]

"Since you will hear what has newly happened in Genoa, the matter being of the great importance that it is, we want you to make every effort to learn as much as you can, both about the causes of that rising and about how [code sign: a person, probably the Emperor] means to punish the presumption of [unread] the affairs of that city; which, being the ladder of Spain into Italy, it is to be believed that [the same person] will do everything not to let it fall into the hands of the French. Use extraordinary diligence to inform yourself fully of everything." The words "make", "remedy" and "inform yourself" are what the context wants, not what the decode gives (`translation.md` keeps the holes).

[unverified] The date fits the Fieschi rising at Genoa of early January 1547. That link is from general knowledge and was not checked in a source. Claudio Ariosti's mission is filed in ASMo, Ambasciatori Germania, busta 7: "1546, novembre 5 – 1547, agosto 6. Segretario ducale." [sourced: the ASMo inventory, read through a fetch summary, PRIOR_ART.md].

## Transcription doubts

Doubts were not settled against the image after the decode: by the freeze rule no sign was changed. Each is listed with what the frozen key gives.

- S02?^/ (l.2) - read: S02^/ = za; checked: decode; gives "impertanza" (judge E). Image not rechecked.
- S11^/? (l.2 end) - read: ^/ on a figure-class sign = e; checked: decode; gives "icciate" (N). Image not rechecked.
- S24^6? (l.3) - read: ci; checked: decode; gives "circo" (judge E). Image not rechecked.
- S06? (l.3, blotted) - read: u; checked: decode; gives "cause". Image not rechecked.
- S17?^6 (l.4) - read: si; checked: decode; gives "sia". Image not rechecked.
- S03^7? (l.4) - read: co; checked: decode; gives "anco". Image not rechecked.
- S19^/? (l.4) - read: ga; checked: decode; gives "castigare". Image not rechecked.
- .? (l.4) - read: dot (null); checked: decode; nothing. Image not rechecked.
- S17?^- (l.6) - read: ss; checked: decode; gives "lassa|re". Image not rechecked.
- S03^s? (l.7) - read: ce; checked: decode; gives "rancesi" (judge E). Image not rechecked.
- S19^\? (l.7) - read: ge; checked: decode; gives "dillgentia" (judge E). Image not rechecked.
- S18? (l.7) - read: o; checked: decode; gives "estraoodinaria" (judge E); flagged at transcription as possibly S02 (r), which would give "estraordinaria". Open.

## Proposed emendations (NOT applied)

Listed in `SOLVE_LOG.md`, 11 places: essere (l.2), importanza (l.2), che facciate (l.2), circa (l.3), questo (l.4-5), rimediare (l.5), essendo (l.5), de Francesi (l.7), estraordinaria (l.7), dilligentia (l.7), per chiarirvi (l.8). None was re-checked on the image after the decode. All figures above are on the unemended first pass.

## Prior art

`PRIOR_ART.md` (copied unchanged). Searched 24 Nov 2026, before transcription: the pages and the Estense record; Cyphersolver catalogue 2160 and `targets/` (including Brice Dudout's attempt in `targets/ariosto1559/NOTES.md`: "8 cipher lines transcribed blind (455 tokens)", the 2159 key and neighbouring keys applied, "annealing did not converge. No key was frozen", "**Not solved**"); DECODE public search (Ercole II, Ariosti, Ariosto, Campori, Ferrara 1547, Este, Ercole, Estense: nothing for this letter); web searches; the ASMo inventory of Ambasciatori Germania (first half of the file only; busta 7 is Claudio Ariosti's mission, no cipher mentioned in the part read); filodiritto.com on Este ciphers (keys of 1495 and 1512 only). The neighbouring keys (ariosto1559, ercole1559, ercole1544, capilupi1545, capilupi1546, bresegno1548, francescoeste1546) are other tables. **No earlier key or reading was found.**

Not checked: ASMo, Cancelleria ducale, Cifrario (8 buste; the original key may survive there); P. Cremonini, "Segrete scritture estensi" (2019, print); ASMo, Ambasciatori Germania, busta 7 (the letters themselves: more text in the same table, perhaps a decipherment); HathiTrust and Google Books full text ("scala de Spagna in Italia", "novamente successo in Genova", "Claudio Ariosti" 1547 cifra); DECODE records behind login.

## Reader's notes (24 Nov 2026; review withdrawn 27 Nov 2026)

The session that assembled this folder (Claude Opus 5.5, a model, not independent of the reading and translation it made) read `reading.md` as sentences on 24 Nov 2026 and recorded a reading_review in profile.json with grade B and "independent": false. That review is withdrawn (27 Nov 2026): a contributor does not sign the reading review; the maintainer records it at merge (Dan Bourdeau, review of PR #997). This is our error, the same one as on fenian1885letter2 (PR #997), caught here by our own audit rather than by review. The notes stand as the contributor's notes only: one long period on the Genoa rising and the likely response of the person in code (probably the Emperor), coherent except the stretch from line 4 end to line 5 start; 98 words, 10 holes and 11 one-letter slips, all counted as holes; the slips are left as decoded. Class (read in part), read share (0.786) and all figures are unchanged. The checks were done with AI tools and no person checked each record by hand.

## Remaining gaps

- Line 4 end to line 5 start, "de quesot delill sot ? rit diare" (about 23 letters, 6 words of the reading) - blocker: illegible; read as written in one pass; two proposed emendations fall here (S17^7 S11 -> questo; S02^^ S11 -> rimediare) and need a second reader on the image.
- Code sign S01^4s, twice (a person; the Emperor fits, unconfirmed) - blocker: open-codes; two uses, no key material.
- S12^- (h with a cross-stroke), once in line 5 - blocker: no-key-material; one use ("et" or "da" would fit).
- "icciate" (l.2) and "arirui" (l.8), and the 11 one-letter slips - blocker: illegible; the decode suggests a different reading of a sign in each place (SOLVE_LOG.md, 11 emendations, not applied); a second transcription from the image is needed before any is applied.
- S09 mixes two signs (figure 6 = i, and a b/f-like sign = f) - blocker: illegible; not separated at transcription; "de i rancesi" wants the second as F.
- Weak key values: raised 9 (o or a), raised 2 (o), S02^^ (ri), S10 under a bar (ni) - blocker: too-short; one or two uses each in 276 signs.
- ASMo Cancelleria, Cifrario; Ambasciatori Germania busta 7; Cremonini 2019 - blocker: needs-physical-access; the original key or more text in the same table may be there.

## Escalation

- [x] siblings: cc. 16r, 17r, 17v viewed (clear, blank, address; no other cipher); the 1559 letter of the same writer and recipient (ariosto1559, c. 39r) compared: another table
- [x] clear-pages: the clear lines of c. 16v are the letter itself, not a decipherment; they gave context only
- [x] known-keys: ariosto1559, ercole1559, ercole1544, capilupi1545, capilupi1546, bresegno1548, francescoeste1546 compared: none fits
- [x] print: web searches and the ASMo inventory (first half); Cremonini 2019 and the ASMo Cifrario not reachable from here
- [x] key-rebuild: every sign valued except S01^4s and S12^-; weak values listed above
- [ ] retry: a second, independent transcription of the 8 lines from the image is the next step (it would settle the emendations, S09 and the line 4-5 stretch); not done under the freeze rule

## Files

Copied unchanged from the contributor's working folder (sha256, first 16 hex) [measured]:

| file | what | sha256 |
|---|---|---|
| `REPORT.md` | the contributor's report (written before the judge ran; figures "pending" there are filled in above) | 1714e3de0ecb2146 |
| `PRIOR_ART.md` | prior-art searches | ebcea91a5e617fd2 |
| `FETCH_LOG.txt` | image URLs with md5 | a3d035a1b489c6ce |
| `TRANSCRIPTION.tsv` | the frozen transcription | 4a970eddb50e5503 |
| `SIGNS.md` | sign shapes and transcription conventions | b69865e7200052b5 |
| `FREEZE_TX.txt` | transcription freeze and split | 4b73d337683ac4a8 |
| `SOLVE_LOG.md` | every solving attempt, failures included; weak values; proposed emendations | 3845be34999d5124 |
| `log/anneal_*.txt` (8 files) | raw annealing outputs | listed by `sha256sum log/*` |
| `work/solver.py`, `work/solver2.py`, `work/build_lm.py`, `work/tx_build.py`, `work/tx_short.txt` | solvers, local model builder, shorthand transcription and its converter | f5691e22cc25d2cb, 134da676c1e0e9c9, 9392d3c7335574fe, 81ba5614ef3212cb, 057f5bee925af281 |
| `KEY.tsv` | the key of record | 6fb733eb6da62fe0 |
| `FREEZE_KEY.txt` | key freeze | 9bde2f6c30de399c |
| `decode_once.py`, `DECODE.txt` | the one decode (the decryption) | c11fffb1d7508a09, 512d062995fb315f |
| `shuffle.py`, `shuffle_out.txt` | shuffle control | e940cdfb66bbef9b, 5fe48b381186e8ad |
| `judge/BRIEF.txt`, `judge/decode.txt`, `judge/judge.tsv`, `judge/count.py` | the strict judge's packet, scores and adder | 94d2a6cc0cbd92b6, 25220de8fe000996, c581fe047a099b44, 4d3eb137789f44bc |

Made here (24 Nov 2026): `transcription_c16v.txt` (the 8 rows of `TRANSCRIPTION.tsv`, unchanged, with a header line), `reading.md` (the decode as sentences, holes and slips marked, nothing emended), `translation.md`, `validation.tsv` (input to `docs/_validate.py`), `profile.json`, this file. No images.

## Limits

- Model sessions did all the work: transcription, key recovery, decode, judge, reading and translation. No person read the signs or the text without AI.
- One transcription, one reader, one pass. The held-out lines test the key, not the transcriber.
- The held-out block is 60 signs on the same page as the build lines.
- The judge was a model session scoring sense by its own lights.
- The gist, the translation and the link to the Fieschi rising are unchecked.
