# Vatican Challenge Part 5 — solution review

**Verdict (20 September 2026): solved, with a provisional scholarly edition.**

Simon Klee recovered the key and candidate plaintext of the Farnese–Poggio letter and published the result as
[“The Farnese letter”](https://simonklee.dk/farnese-letter) on 16 September 2026. MysteryTwister accepted his
submission after manual review. The cipher key is stable; some readings of the damaged manuscript remain editorially
uncertain, and Klee labels them as such.

## Why the solution is accepted

The result clears several checks that are independent of merely obtaining plausible Italian:

1. **Split recovery.** The first and second halves were solved separately. All twelve restarts (six per half)
   recovered the same eighteen letter assignments and null.
2. **Controls.** The same search recovered invented keys from clean and damaged synthetic ciphertexts. A shuffled
   version of the real ciphertext scored far below the proposed key.
3. **Manuscript confirmation.** Predictions made from the language and key were checked against the handwriting.
   For example, the disputed digit in *Montepulciano* is visibly `1` (`u/v`), not the transcribed `2` (`r`). The
   manuscript check also found duplicated, omitted, and swapped digits in the public transcription.
4. **Internal consistency.** The undotted one- and two-digit codes spell a coherent letter of 1,241 words. Dotted
   codes recur in the contexts required by `ce/ci`, `qua/que/qui`, `non`, and three titles.
5. **Historical corroboration.** Independent records agree with the letter’s account of the papal subsidy at the
   Diet of Speyer and with the Gonzaga family and place names in the closing report.
6. **External review.** MysteryTwister accepted the solution submitted on 15 September 2026.

The final alignment accounts for 6,358 of 6,562 corrected digit tokens exactly (including 365 nulls), accounts for
170 through explicitly recorded departures, and leaves 34 in gaps. That is strong evidence for the key and the
substance of the plaintext, but it does not make every supplied letter or damaged passage certain.

## Corrected cipher description

The earlier notes in this repository misidentified the design. The recovered system has one code for each of the
eighteen letters used by the clerk, with codes of either one or two digits; `1` represents both `u` and `v`, no code
is needed for `h`, and `9` is the null. Code boundaries are not written and must be inferred from context. A small
second layer uses a dot on one digit of a pair for syllables, `non`, and abbreviated titles. `81` means `et`.

The recovered key is in [`key.md`](key.md). Klee’s publication supplies the full edited Italian,
digit-by-digit alignment, corrected transcription, correction ledger, search results, and source notes.

## Credit and reuse

Solution, key recovery, manuscript review, edition, and historical identification: **Simon Klee**.

Challenge and public transcription: **George Lasry / MysteryTwister** and **EHum**, respectively. Manuscript:
Archivio Apostolico Vaticano, Segr. Stato, Spagna 1A, ff. 70r–73v; photographs supplied through DECODE record 92.

This repository records and reviews the result; it does not claim the decipherment. Cite Klee’s article and research
files for the solution itself.
