# The Fulda protest of 1576: a ciphered note in the Bavarian key volume (BayHStA KAA 4591 f.129, DECODE R9325)

Split on 15 Oct 2026 from `targets/kaa4591/` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue entry 161
grouped fourteen ciphertexts of the Munich key volume KAA 4591 in at least six systems; this note is in its own key,
R9324, filed a few leaves earlier. The other letters are different ciphers, each with its own page: System A′
([`targets/kaa4591/`](../kaa4591/NOTES.md)), Łaski's cipher ([`targets/kaa4591b/`](../kaa4591b/NOTES.md)), R9367
([`targets/r9367/`](../r9367/NOTES.md)), R9416 ([`targets/r9416/`](../r9416/NOTES.md)), R9424
([`targets/r9424/`](../r9424/NOTES.md)) and R9319 ([`targets/r9319/`](../r9319/NOTES.md)). Work 21 Sept 2026 (Claude
Opus 5) as part of kaa4591; `r9325/` moved here unchanged; `decode.py` added 15 Oct 2026.

Images: DECODE, login (cookie in `targets/bordeaux/decode/cookie.txt`); not public domain ("publishing only with the
permission of the Archive"), kept untracked (`targets/kaa4591/img/` in the main checkout); the page shows none.

Outcome: **read with known key, read** (every word; three scribal slips). Key state: R9324, complete for this note.

## R9325 (f.129) — read

Key R9324 (f.124–127): alphabet A x, b t, c o, d þ, e 2, f k, g y, h n, i a, k (looped b), l (barred b), m d, n i,
o c, p δ, q (looped δ), r ɓ, s Λ, t Z, u w, x ɣ, y 7, z ⊙; doubles bb v, cc ꝸ, dd XX, ee (crossed x), ff ß, gg,
ll, mm, nn 4, pp, rr, ss (m with tail), tt 3; sch st sp ch signs; nulls g, -o-, stemmed square, ⊟, W-like, 8
underlined. Nomenclator (f.126–127): Pontifex, Card. Comensis, Card. Matutius(?), Nuncius Ap., Electores
ecclesiastici, Cologne, Trier, Mainz, Würzburg (bishop, chapter, dean), Abbas / Capitulum / Decanus Fuldensis,
Imperator, Archdukes Matthias and Ernst, Landsberg league, Ferdinand of Austria, Dux Bavariae, Philip of Bavaria,
Nobilitas Fuldensis, Conradus til (?) dux nobilium, Nobilitas Franconiae, Landgrave Wilhelm, Elector of Saxony,
Augsburg-Confession princes, the Emperor's vice-chancellor and councillors. That is the 1576 deposition of Abbot
Balthasar von Dernbach of Fulda by his chapter and knights with Julius Echter of Würzburg.

The key was matched to R9325 by its null signs (the identical set) and applied unchanged. Reading in
`r9325/reading.txt`. Normalised:

> Protestatus [est] abbas secreto coactum [se] ad litem acceptare Pontificis inhibitionem. Rogatus Pontifex ut
> contradicendo se interponat, declaret sive sponte sive vi contra canones esse. Si id fiat, Abbas agere cessat et
> cum Pontifice litigabit; ad [quod] cum non possit, Consiliarii Caesaris iudicabunt, aut Pontifex tum facit quod
> iam voluit. Rogatus Dux Bavariae auxilio sit; Nuncius suadeat Pontifici ita ad protectionem via[m].

All signs resolve; slips: "secreto" written without its second e, "auxilio" begins with the i-sign, "voluit" ends
in the d-sign.

`decode.py` (15 Oct 2026) applies the key alphabet to the transcription codes of `r9325/reading.txt` and compares
each word with the plain column: 18 of 270 signs differ, all explained — the writer's three slips, the o/c look-alike
transcribed as o in "contradicendo", "declaret", "canones", "quod", and line 4, where the transcription keeps a first
pass ("Saz … Sdcize") beside the corrected "siwz" (siue). The reading was made on the image and stands; the
transcription of line 4 was not cleaned. `decode.py` also writes `r9325/signs.txt` (270 signs) and the site's
reveal file.

## Remaining gaps

None in the text. The sender and the recipient are not named in the note (it is filed with the Bavarian keys; the
Duke of Bavaria is asked for help in the third person).

## Escalation

- [x] siblings: R9324 (the key, ff. 124-127) found and matched by its null signs
- [x] clear-pages: none on f.129
- [x] known-keys: R9324 fits unchanged
- [x] print: web search 21 Sept 2026 for KAA 4591 ciphers found no edition; the Fulda affair of 1576 is well known in print, this note is not
- [n/a] key-rebuild: the key is complete for this note
- [n/a] retry: every word read

## Files

- `r9325/reading.txt`: transcription (codes per sign), plain column and normalised text.
- `decode.py`: key, comparison, `r9325/signs.txt`, `docs/reveal/fulda1576.json`.
