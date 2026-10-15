# A son to his father, 22 March 1535: cipher passages in a German letter (BayHStA KAA 4591 f.169, DECODE R9367)

Split on 15 Oct 2026 from `targets/kaa4591/` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue entry 161
grouped fourteen ciphertexts of the Munich key volume KAA 4591 in at least six systems; this letter is in a key of
the volume's key register R9423 (block 2_4). The other letters are different ciphers, each with its own page:
System A′ ([`targets/kaa4591/`](../kaa4591/NOTES.md)), Łaski's cipher ([`targets/kaa4591b/`](../kaa4591b/NOTES.md)),
the Fulda note ([`targets/fulda1576/`](../fulda1576/NOTES.md)), R9416 ([`targets/r9416/`](../r9416/NOTES.md)), R9424
([`targets/r9424/`](../r9424/NOTES.md)) and R9319 ([`targets/r9319/`](../r9319/NOTES.md)). Work 21 Sept 2026 (Claude
Opus 5) as part of kaa4591; `r9367/` moved here unchanged; `signstream.py` and `measure.py` added 15 Oct 2026. The key
register transcriptions stay in `targets/kaa4591/keys9423/` (volume material: `2_4.txt`, `2_4_zoom.txt`, `index.md`).

Images: DECODE, login; not public domain, kept untracked; the page shows none.

Outcome: **read with known key, read in part**: the clear German is read; of the cipher runs, 78 of 143 words
(54.5%, `measure.py`, an upper bound). Key state: partial (# and O open).

## R9367 (f.169) — read in part

Son to father, Monday after Palm Sunday, 22 March 1535. In cipher: he was questioned about strange matters
("seltsam khinst gefragt") and denied everything ("aber a[ll]es verlaugnet"); he is taken for a poor writer
("schlechter schreiber") and sent to learn; nothing reliable learnt yet ("noch nicht freintlichs erfaren"); fears for
his person ("meines leib"); the Turks are coming up ("Tirckhen herauf ziechen"); a name read as Nothaft(?);
postscript names a Friedrich and "Schmalcz" (Schmalkalden?): "euch nicht guets". Key: R9423 block 2_4, "H. Wilh.
[15]25" (A 9, B v, C Δ, D +, E 6, F ⊥, G o, H 4, I w, K ‡, L 8, M ¥, N 3, O barred D, P two rings, Q 2, R 7, S y,
T ♉, V ‡‡, X o-o, Y ε, Z π; und 9, auch Z, ch t, das T, ll 9, rr m); the letter adds q a, Λ r, C s, H k, K z.

The block first failed with wrong pins; it fitted once the frequent signs were re-matched by shape
(`r9367/key_match.md`, `r9367/dec.py`, `r9367/decode_test.txt`). The register's name signs (Bayern ♀, H. Ludwig ≈)
do not fit the letter's frequencies: ♀ 25×, ≈ 16×, ⊡ 26× behave as nulls or word dividers ("gef(Q)rag(W)t" = gefragt).
Reading: `r9367/reading.txt` (clear German in bars, decoded cipher in braces, rough). The record's second image (the
back, with the address) was not examined in the 21 Sept session (`r9367/transcription.txt`, last note): look at it
first when this letter is taken up again, since it may name the father.

Measure (`measure.py`, 15 Oct 2026): words of the {..} cipher runs, a word with '_', '?', '[#]' or a single letter
counted unread: 78/143 (54.5%). Some counted words are letter strings of a working reading (L07), so this is an
upper bound. The transcription has 534 cipher signs (`signstream.py` → `r9367/signs.txt`).

## Remaining gaps

- L01-02, L07, L09-10, L13 cipher runs mostly unread - blocker: open-codes; paused 21 Sept 2026 (workable): the # sign and O open, doubtful shapes; next: a zoom re-transcription of these lines against block 2_4
- # (triple-barred cross, 13×) and O signs - blocker: open-codes; not in block 2_4, context does not fix them
## Escalation

- [x] siblings: R9423 register (19 keys) read block by block; R9422 (1583 key) checked
- [x] clear-pages: none; the clear German of the letter gives the context
- [x] known-keys: R9423 blocks tried; 2_4 fits after shape re-matching (reads in part)
- [x] print: web search for KAA 4591 ciphers found no edition
- [x] key-rebuild: five values added from context (q a, Λ r, C s, H k, K z)
- [x] retry: re-annealed with de-1500s, homophone caps and nulls (failed); block 2_4 reading by hand
