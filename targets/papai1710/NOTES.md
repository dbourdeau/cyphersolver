# János Pápai (Belgrade) to Ferenc Rákóczi II, 6 March 1710: the graphic-sign passages — DECODE R731

Attempted, not solved: closed unread on 21 Sept 2026 (the camera images do not settle the signs; a validated solver
finds no Hungarian on the tentative transcription). Written up in docs/papai1710.html.

Split on 14 Oct 2026 from `papai1706` under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. The old
entry (catalogue 46) joined this letter with Pápai's eleven numeric despatches, which are in the envoy key DECODE
R580/R581. Those are a different cipher, with their own page ([`targets/papai1706/`](../papai1706/),
docs/papai1706.html). Catalogue entry 46 was restored on 14 Oct 2026, narrowed to R731, as "attempted, open". The
images (`img/`, git-ignored, not in the public domain) stay in the main checkout `targets/papai1706/img/`
(IMG_R731_I4153-4155, key image R581 3842). `solve731.py` trains its model on the deciphered letters in
`../papai1706/*read.txt`; `../papai1706/retry_groups.py` imports it from here.

## The letter

R731 = MNL OL G15 Caps. H Fasc. 226, pp. 31–33: 6 March 1710, Landor Fejérvár (Belgrade), signed *Pápai János*.
Written in clear except six short passages in a graphic alphabet of perhaps 25 signs (∂, π, m-like, q, ÷, =, "11",
with colons), about 350 signs in all, on p. 1 (three passages) and pp. 2–3 (three). DECODE has no transcription.
Lead checked: the top-left corner of the key copy R581 carries a line of signs of the same family (δ, ♀, ⊔, =, :),
which the DECODE transcriber noted as "symbols which do not occur in the key itself". Read the right way up it is a
line of cipher, not an alphabet, so it gives no key.

## What was tried

The six passages were transcribed from the images at 1.8–1.9× zoom into `R731_signs.txt` (about 330 signs, 15 sign
types plus dot clusters). The transcription is tentative: the low swash stroke may be a pen link rather than a sign,
and the dots above and below the bars (÷, ∴, ::) were collapsed into one token, although they may be vowel marks.

`solve731.py` is a swap-annealing substitution solver with a 4-gram model trained on Pápai's deciphered letters.
On a control (Pápai's own text cut to the same line lengths and enciphered at random) it recovers the text exactly
(−8.96 per 4-gram, against −8.87 for real text). On R731 it reaches only about −10.1 under every reading tried:
as transcribed, dots dropped, swash dropped, reversed. So R731 is not a simple Hungarian substitution *on this
transcription*. Either signs are merged in it or the dot patterns carry letters. Neither can be settled from the
2448-px camera images. The recurring group `~n~s` has the letter pattern of *Pasa* read backwards, but this
did not lead to a key.

Print: Benda (ed.), *Pápai János törökországi naplói* (Budapest: Szépirodalmi, 1963, Magyar Századok) is not online
(antiquarian copies only); whether it prints these passages deciphered is not known.

## Log

- 2026-09-21: images fetched at full resolution; R581 corner line checked; transcription; control and solver runs; closed unread.
- 2026-10-14: split from `papai1706`; `R731_signs.txt` and `solve731.py` moved here.

## Remaining gaps

- R731 (6 Mar 1710, Belgrade), six graphic-sign passages, ~330 signs - blocker: illegible; tentative transcription in R731_signs.txt; sign segmentation and dot counts cannot be fixed from the 2448-px camera images, and a control-validated substitution solver finds no Hungarian on it; needs better images or the sign alphabet

## Escalation

- [x] siblings: the twelve Pápai records and the key copies R580, R581, R452 opened; no graphic alphabet among them
- [x] clear-pages: R731's three pages are clear apart from the sign passages, with no interlinear or decipherment; R581's corner sign line checked (cipher, not an alphabet)
- [x] known-keys: R580/R581/R452 (Pápai's keys) are numeric, with no graphic alphabet among them
- [x] print: Benda 1963 searched for online (antikvarium.hu only); DECODE and web searched, nothing printed online
- [x] key-rebuild: control-validated swap annealer (solve731.py) under four readings of the transcription; no solution
- [n/a] retry: nothing reads, so there is no extended key to retry with
