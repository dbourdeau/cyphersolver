# No. 19 ff. 41r-42r: held-out check of Lasry's key and strict count (14 Nov 2026)

## Frozen before measuring
- `n19_transcription.txt` SHA-256 96471b9ad1e08465bf815aa0480fd1ce1592400b11f71396e6f67e94b55c1bff
- `PREREG_n19.md` SHA-256 887a082b5acfc7f7370be421df4cd6d9c81794abeb9de54ea5209396d79a8fc3
- `n19_decode.py` SHA-256 f8edf6e5051e0c50408cb5efdbe8ab8f93768616459691db626d788f9eddb5d4
- The set of proposed code values was frozen as well (SHA-256 f51d12b2f84f408c1179a1a3fb7d414ddf0c566c95802afa48c0b85fd0871a53). It asserts no new value; its text is reproduced in NOTES.md, 14 Nov 2026.

## Held-out check (one run, `python3 n19_decode.py n19_transcription.txt --lexicon es.json.gz --measure`)
The portion has 612 groups in all. 232 of them are letter-only words, and those are the ones scored.

| key | share of words in lang/lexicons/es.json.gz |
|---|---|
| Lasry's key, unchanged | **0.591** |
| 200 shuffled keys | mean 0.045, best 0.164 |

The pre-registered threshold was ≥ 0.50 and ≥ best control + 0.30. **Verdict: PASS.**

Lasry built his key on ff. 16v–17v and 40. On text it never saw, it reads continuous Spanish:
- "esperança de socorro y yo espero en Dios";
- "procuraremos que se vaya la [bog] de [rar]";
- "todavia yo trabajare";
- "y iremos a buscar de comer y donde podamos".

The portion is now spent and cannot serve as a held-out check again.

## Strict count, no. 19 ff. 41r-42r (by sense, single reader)
| status | groups |
|---|---|
| syllable signs (Lasry labels) | 196 |
| nomenclator groups with a known value (this target's table) | 68 |
| nomenclator groups not read: fab ×4, coh ×2, dig ×2, de ×2, cot, bat, dob, dnh, baq, cnt, bnq, bob, dez, cil, be, rar | 22 |
| letter words read (lexicon or by sense) | 301 |
| letter words not read | 25 |
| **read** | **565 / 612 = 0.923** |

The 25 letter words not read are at:
- 41r.01, .02, .03, .05, .09 (×2), .12, .15, .18, .20, .21, .23, .25 (×2);
- 41v.02, .03, .07 (×2);
- 42r.04, .06 (×2), .08, .12, .15 (×2).

Most are misjoined or unclear signs. Word-level reading has not been edited yet.

## No. 6
No new code value has been asserted, so the count is unchanged: 1,646 / 1,680 = 0.980 (`n6_measure.py`).
