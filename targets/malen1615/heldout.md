# Held-out test

Key frozen (`key_frozen.tsv`) from letter 1, scan 2 (L05-L32 of `transcription_malen1.txt`). Then transcribed and
decrypted with the frozen key, not used to build it: letter 1 scan 1 (L01-L04), scan 3 (L33), and letter 2 scan 5
(the first cipher passages, `transcription_malen2.txt` L01-L08).

| passage | words | French words straight from the frozen key | wrong | holes (faint signs) |
|---|---|---|---|---|
| letter 1, scans 1 and 3 | 21 | 18 | 0 | 3 (fai?t, ??, d??mes) |
| letter 2, scan 5, French part | 37 | 36 | 1 (voy for vos: one hook read R, probably X) | 0 |
| total | 58 | 54 | 1 | 3 |

54 of 55 legible held-out words (98%) come out as French words in context. Caveat: in letter 2 the split between
straight X (s) and cursive C (l) was made with the key in mind (see NOTES.md); without that split the test is weaker.
