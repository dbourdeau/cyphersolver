# kc05-frozen - the frozen files of the K-C05 test on BnF fr. 16041 f. 272 v (17 Nov 2026)

Kept byte for byte as hashed (`SHA256SUMS`), so the two working notes stay in the contributor's French; validation.txt section 7 gives the same content in English.

- `PREREG-KC05.md` (f62420d9...): the pre-registration, hashed at 18:23 CET before any transcription of f. 272 v: page, key, transcription protocol, metric, seed 2722, bars.
- `K-C05.tsv` (3f21bdd8...): the key as frozen with it (`key-f16041-272v.tsv` is the same key without the two French header lines).
- `DERIVATION-KC05.md` (147484f7...): how the five new values were drawn from f. 272 r (counts per value), hashed with the pre-registration.
- `B-f272v-chiffre.txt` (4b339f50...): the measured block, frozen at 19:03 CET before decoding (`transcription-f16041-272v.txt` is the same with the word separators).
- `mlex2.py` (b57eaff9...): the measuring script, unchanged since sections 5-6 (it reads the lexicons of `lang/lexicons/`; its paths are the contributor's).
- `MESURE-B-f272v.txt`: the output of the single run and the decision written at once.
