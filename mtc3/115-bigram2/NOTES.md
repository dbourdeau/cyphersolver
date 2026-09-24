# MTC3 115: Bigram Substitution, Part 2 (Modi and Esslinger, October 2025)

Status: in progress. Key recovered 24 Sept 2026, but the site REJECTED it on the first submission (24 Sept, 1 of 15
attempts used). The pasted text matched `private/ANSWER_key_676.txt` token for token. Cause not yet known; see
"Submission" below.

Level II. Before this: 10 human solvers, no LLM solve.

## The challenge

- Ciphertext `bgs_ciphertext.txt`: 1608 letters = 804 bigrams, 223 distinct. A bigram substitution: the 676
  plaintext bigrams AA..ZZ are permuted onto the 676 ciphertext bigrams.
- Cribs: "studying societies", "sociology of knowledge", "patterns". The theme is Berger and Luckmann's *The Social
  Construction of Reality* (1966) with a modern complement.
- Answer: the key as 676 ciphertext bigrams in plaintext order AA..ZZ, `??` for plaintext bigrams that do not occur.

## Answer (kept out of git)

The answer and the full plaintext are in `private/` (git-ignored, because this is a live challenge and the repository is
public): `private/ANSWER_key_676.txt` (one line, 676 space-separated tokens, 223 known, 453 `??`) and
`private/plaintext.txt`. Before submitting, check the format against the challenge page (separator: space, tab or
comma are all accepted). The submission form asks whether an LLM was used: yes, Claude Opus 5.5 did the work.

## How it was solved

Model: Claude Opus 5.5 (Claude Code), with the tools in `src/`.

1. Annealing over ciphertext bigram -> plaintext bigram (injective), scored by an interpolated character 5-gram model of
   English (Gutenberg, Roman numerals and letter runs removed; `src/buildlm.py`). Plain random-value moves stalled at
   pseudo-English (-1859 log10).
2. Rewritten (`src/big2.cs`) with incremental scoring and letter-level moves (change one letter of a plaintext
   bigram, or swap two symbols' values): -1537, still pseudo-English.
3. Crib dragging "SOCIOLOGYOFKNOWLEDGE" across all 1589 placements with short anneals. The top placement (letter 460)
   showed "KNOWLEDGE" twice nearby. That matches the ciphertext: the run `DOMGFQLD` (NO WL ED GE) occurs three times
   (bigrams 218, 236, 315). Crib fixed at bigram 230.
4. The domain was the bottleneck: a model trained on fiction could not tell sociology prose from pseudo-English. Adding
   ~485 KB of Wikipedia text on sociology (the book, sociology of knowledge, socialization, symbolic interactionism,
   ideology, values, filter bubble ...) at weight 20 gave -1397 with long readable stretches, then -950 after
   refinement from the best state. The other two cribs appeared in the text unforced.
5. The last errors were corrected by hand with equal-length substitutions (HOW for NOW, MAINTAIN for PAINTAIN, "SEES AS
   REAL MIGHT" for "SWAS A GREAT NIGHT", ...). The check (`src/bgcheck.py`) passes: 223 ciphertext bigrams map one-to-one
   onto 223 plaintext bigrams, with no conflicts. Corrections at bigrams that occur more than once confirm each other
   (e.g. `ZJ` = SR in "SEES AS REAL", "ACCEPTED AS REALITY", "EXPECTATIONS REGULATE").
6. Verified with the challenge's own tool: `2-gram-subst.py encrypt --allow_unknown -k private/ANSWER_key_676.txt
   --infile private/plaintext.txt` reproduces `bgs_ciphertext.txt` exactly (1608/1608 letters).

The plaintext ends "...EMERGE AND EXERT E" plus the tool's X pad (odd length), so the text is cut mid-sentence.

## Submission

24 Sept 2026: Daniel pasted the 676-token key (space-separated, AA..ZZ order, identical to the tool's
`kpa --outkey` output); the site said the solution was incorrect. Checks made afterwards:
- the submitted text equals the key file (676/676 tokens);
- the key equals what `2-gram-subst.py kpa --outkey` derives from the recovered plaintext;
- all 84 single-occurrence ciphertext bigrams reread: none admits another same-length reading;
- the last ciphertext bigram (XB) also decodes as EX in "EXIST", "CONTEXT" and "EXPLAINING".
Open suspicion: the plaintext stops mid-word ("...EMERGE AND EXERT EX"), so the reference key may come from a longer
plaintext than the one encrypted here. Next step: ask the MysteryTwister team how the reference was built. Do not spend
attempts on guessed variants.

## Remaining gaps

The site's verdict (above). In the text itself every ciphertext bigram is mapped. 21 of the 223 key entries rest on a single occurrence
confirmed only by the sense of the text (e.g. MONK, BUSINESSMAN, "A FOCUS ON BEING VERSUS DOING").

## Escalation

Not needed.
