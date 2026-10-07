# Palm 1727: BL Add MS 32270, DECODE R7927 / R7930

Status: attempted, open

Catalogue: "Palm (Germany) to Visconti / Staremberg, 2 ciphertexts" (DECODE R7927, R7930). Karl Joseph von Palm was
the Emperor Charles VI's resident in London; he was expelled in 1727. Staremberg is presumably Count Konrad Sigmund
Starhemberg, Imperial envoy (d. 1727). Session 21 Sept 2026.

## What the records actually are

| Record | Folios | Content |
|---|---|---|
| R7927 | ff. 16–17 | Docket "Palm & Staremberg / German". A **German letter fragment**, mostly in clear, with 14 ciphered passages (ff. 16v–17r). Images P1 and P4 show only show-through. The Deciphering Branch glossed a few groups interlinearly, some in a second, darker hand. |
| R7928 | f. 18 | **Key fragment**, "Count Windischgrätz & Ct Staremberg": numbers 1–50 → letters, about 30 filled. It is **not** Palm's key: 40=r here, but the glosses on Palm give 40=ſ, and 23=u against 23=n. |
| R7929 | ff. 19–40 | Emperor → Staremberg, 42 pp., "Decrypted", no images on DECODE. |
| R7930 | f. 41 | Cover "Palm to Visconti 1727 … Visconti to Palm" plus a decipherer's **worksheet**: a 1–500 grid with tallies and partial values (Hollande 109, Italie 120, Traité 215, Addresse 21, syllables mo/pe/ca/pi… in the 300s–400s, several numbers marked zero). This is a French/Italian nomenclator, not the German system in R7927. **Visconti's letter itself is not imaged**, so R7930 has no ciphertext to read. |

## The R7927 cipher

- Transcription: `ct.txt`. It keeps the clear context and has 162 letter tokens across 47 different values (2–79) and
  10 code values (124, 138, 170×5, 210×3, 230×6, 380, 423, 432, 474, 799).
- The contemporary glosses (in Kurrent script) give 33=e, 23=n, 10=d, 15=t, 40=ſ, 230=der, probably 9=u/ü and 4=z; 8 looks like "ch".
- Clear context: the letter is about how England views the coming war (of 1727, over Gibraltar and the Hanover alliance). One passage
  runs "… und 380 d ſ ? e t z e n zu bringen", with some verb in *-setzen*/*-etzen*.
- Solver runs: `anneal.py` and `anneal2.py` (de-modern 5-gram model; codes drawn from a syllable/word list, gloss values fixed).
  Nothing converged. Scores stayed around −1950 and the output was word salad. The text is too short for a homophonic system
  with about two homophones per letter.

## Control: why this is a skip

A longer run (12 restarts × 250k moves, `anneal3.py`) gave scattered scores from −1985 to −2022, and no two runs agreed.
`control.py` builds a synthetic German homophonic text with the same shape: 162 letter tokens over the same 47 values,
the same code groups and the same clear context. It fixes the TRUE values of the six commonest symbols.
The same solver then recovers only 81/162 and 71/162 tokens (seeds 1 and 2), which is unreadable. The real letter has
fewer certain glosses, so a ciphertext-only reading is not achievable with this much text. The target is skipped until a
key or clear copy is found.

## Prior art

Searched the web for a printed decipherment of Palm's 1727 intercepts and found none. As a Deciphering Branch intercept it was
probably read at the time, but the clear copy is not on DECODE. The printed material on Palm's expulsion (his memorial of March 1727)
does not include these letters.

## What would move it

- A clear copy of the letter, or Palm's Imperial key: Vienna HHStA, England Berichte 1727, or a Willes decipher in
  BL Add MS 32xxx or SP 107.
- The rest of Add MS 32270 on DECODE: R7929 is marked "Decrypted" but has no images.

## Word-level solver test (4 Oct 2026, contributed by Feyseel Nur, PR #21)

A word-level annealer on a 30M-character German corpus of 1724-1767 (Deutsches Textarchiv) recovers synthetic German
homophonic texts of the same size (164-177 tokens, ~44 numbers, 6 commonest values given) at 99-100%, 99.4% with 9
syllable code groups mixed in, and 90% with 5% of the numbers corrupted. So 162 tokens is not too short for a word-level
model. On R7927 about 70 runs over 14 settings (gloss values; Latin readings 23=u, 33=n, 40=r, matching R7928; nulls,
syllable or word values for small numbers; code groups as letters) give no German and score like shuffled ciphertext
(real −901 to −961, shuffled −916 to −1006), while IoC (0.024) and 13 repeated pairs look like a real cipher. The block
is the input: the glosses or more than ~5% transcription error (internal contradictions: "d n" twice and "?dt" in P17
if 10=d; 8=ch cannot follow the clear "über" in P6). The clear text matches Palm's reports of Dec 1726 in Coxe, *Walpole*
II 504-510 ("my last P.S." on the King, the ministry and the nation). Next: re-transcribe ff. 16v-17r digits and every
gloss from the DECODE images; the full R7928 table.

