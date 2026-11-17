# PREREG — BNCF Carte Machiavelli, 1510 Dieci cipher (catalogue 2910 V/125, 2911 V/134) — 17/11/2026, BEFORE any decoding of the held-out portion

## Key (frozen: KEY.sha256)
Period key BNCF Carte Machiavelli VI/82 c. 2r, headed "Roma & Francia da scrivere", endorsed c. 2v "Cifera a li Oratori di
Francia et Roma ... con Francesco Gualterotti et Luigi della Stufa": alphabet with homophones, nulls, syllables, doubles,
dictions. Transcribed into KEY.tsv (label -> plain; for labels whose shapes coincide, the first plain listed is the decode).
Learning (only): V/124 copy 2 (c. 236r) lines 3-4, against Opere VI (1877) pp. 76-77: confirms the key ("a Milano sopra a una
richiesta fattaci", "mandare le gente nostre in Lombardia la quale"); the only change from learning: label y -> ma|b.

## Held-out portion (never decoded before this file)
V/131 (c. 248r, Teca image BNCF0003856962, "Copia della di Ruberto Acciaiuoli"), cipher from the first sign after "Mag.ci D. etc."
to the end of line 6; if fewer than 300 signs, continue whole lines until >= 300.
Transcription: two blind passes (T1, T2), arbitration on the image, labels from KEY.tsv only; frozen by SHA-256 before the
reference text is read.

## Reference
Opere di Niccolò Machiavelli VI (Passerini-Milanesi, 1877), printed text of this letter (V/131, footnote "cassetta V, num. 131"),
from its first word. Normalisation (both sides): lowercase, letters only, accents removed, j->i, v->u, y->i, k->c, h removed.
Window: the first round(1.15 x n) normalised reference characters, n = length of the normalised decode.

## Measure (ONE)
score = sum of matching-block sizes of difflib.SequenceMatcher(None, decode, window, autojunk=False) / n.
Controls: 200 keys where the plain values of KEY.tsv are permuted among all labels (random.Random(seed), seeds 1-200),
same transcription, same score; best control kept.
VALIDATED if score >= 0.85 AND score >= best control + 0.30; PARTIAL if 0.50 <= score < 0.85 with margin >= 0.30; else FAIL.
The held-out portion is burnt after this measure.
