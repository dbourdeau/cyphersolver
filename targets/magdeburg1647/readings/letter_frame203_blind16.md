# cipher in a letter, frame 203 right, LASA A 1 Nr. 530: reading with holes, blind sibling decode of 16 Nov 2026

State: decoded, not read (`docs/_check_reading.py`: not readable). Filed crediting the hold in Andrew Beling's addition (PR #578; NOTES.md, Addition of 16 Nov 2026).

Blind transcription `transcriptions/letter_frame203_blind16.tsv` (= `blind16/letter_fr203/BLIND.tsv`, sha256 in `blind16/letter_fr203/FREEZE_blind.txt`, frozen before
the decode), decoded once with the frozen key (`blind16/FREEZE/key_upstream.tsv` = `key.tsv` of upstream 89e25ef) by
`blind16/decode_once.py`: `decryptions/letter_frame203_blind16.txt`. Strict one-pass judge (letter units, `blind16/letter_fr203/judge.tsv`,
`blind16/JUDGE_NOTES.txt`): S/(S+E+N) = 134/189 = 70.9% (S 134, E 17, N 38; 3 [S] units). Shuffled keys: 0 of 5,000 at both seeds (`blind16/shuffle_out.txt`).

The text below is the judge's segmented text, unchanged, built mechanically by `python3 -I blind16/build_reading.py blind16/letter_fr203`:
the judge's reading where the judge gave one, the decode where the judge left it as it stands. Language: German with
Latin passages, period spelling. Conventions: `[...]` = one cipher word read as no sense, a drawn name sign or a blot;
`[r]` = a letter missing from the cipher word, supplied by the judge (not penalised, listed in the judge notes);
`?` = a doubtful word. Nothing else is supplied or emended. Each line is 'image line: text'.

```
fr0203_right 14: von [...] verstanden das etwas
fr0203_right 15: noch diesen winter in [...] umb relation zu thun [...]
fr0203_right 16: tractaten [...] newe instruction
fr0203_right 17: zu holen [...] [...] eine
fr0203_right 18: gute gelegenheit gebe [...] dero negotia undt
fr0203_right 19: desideria beßer recommendiren [...] [...]
```

Notes from the judge: newe = neue (judge).
