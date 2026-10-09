"""Sense measure: count cipher tokens that fall inside words read as German sense, word by word.

decode.py counts every token outside the hand-marked UNREAD spans. This script checks that count: the decrypt is
split into the words of the reading (WORDS below, letters as decode.py emits them), each word is marked sense or not,
and its tokens are counted. Each sense word is also scored by the de-1640s model against the unread stretches.

    python measure_sense.py
"""
import os, subprocess, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

# (segment, [(word as decrypted, sense?)]), code words omitted; '?' = unread letter
WORDS = {
 'S1': [('iobs', 1)],                                   # Jobs(t) [508]
 'S2': [('in', 1), ('n', 0), ('iohann', 1), ('???????????', 0), ('uber', 1)],   # 'n' after [513]: no sense alone
 'S3': [(w, 1) for w in 'nach der oberpfaltz und gegen die'.split()],
 'S4': [(w, 1) for w in 'etwa auch dein schlesien agirende dazu ziehen'.split()],  # 'dein' = die in (slip)
 'S5': [(w, 1) for w in 'darau gute acht geben und sobaldt'.split()] + [('?', 0)] +
       [(w, 1) for w in 'ich sein gegen ehender au solche'.split()] + [('??????????????', 0), ('zu', 1), ('dem', 1),
       ('??', 0)] + [(w, 1) for w in 'ein guten fursichtigkeit nachuolgen'.split()],
 'S6': [(w, 1) for w in 'durch espionen sie koen das sie moen'.split()],   # ko[M]en, mo[G]en: code letters
 'S7': [(w, 1) for w in 'wohin er seinen arche zu richten entgegen wolten'.split()],
}

out = subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'decode.py')],
                     capture_output=True, text=True, encoding='utf-8').stdout
dec = {l.split()[0]: ''.join(c for c in l[3:] if c.islower() or c == '?') for l in out.splitlines() if l[:1] == 'S' and l[1].isdigit()}
m = lm.load('de-1640s')
tot = sense = 0
for s, ws in WORDS.items():
    joined = ''.join(w for w, _ in ws)
    assert joined == dec[s], (s, joined, dec[s])
    for w, ok in ws:
        tot += len(w)
        sense += len(w) if ok else 0
read_txt = ' '.join(w for ws in WORDS.values() for w, ok in ws if ok and len(w) > 2)
print(f'tokens {tot}, in sense words {sense} ({sense / tot:.1%}), not sense {tot - sense}')
print(f'de-1640s per char, sense words: {m.score(read_txt) / len(read_txt):.2f}')
