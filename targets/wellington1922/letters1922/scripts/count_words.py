"""Check the marked word division against the decryption and count words by the strict rule:
a word with any changed, supplied or dropped letter ({x/y}), an unidentified or doubtful word ([?..]) is a hole;
a stretch with no words ([... extent unknown: ..]) counts as one hole (minimum) or as its letters / mean letters per
clean word (estimated). python3 -I scripts/count_words.py"""
import re, sys
from pathlib import Path
here = Path(__file__).resolve().parent.parent
for doc in ('DCXXI.6.576.1', 'DCXXI.8.731.1'):
    dec = {}
    for l in open(here / f'decryption_{doc}.txt', encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        i, img, d = l.rstrip('\n').split('\t'); dec[i] = d.replace(' ', '')
    clean = holes = est = 0; bad = []; stretches = []
    for l in open(here / f'marked_{doc}.txt', encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        i, m = l.rstrip('\n').split('\t')
        letters = re.sub(r'\[\.\.\. extent unknown: ([^\]]*)\]', r'\1', m)
        letters = re.sub(r'\{([^/]*)/[^}]*\}', r'\1', letters)
        letters = re.sub(r'\[\?([^\]]*)\]', r'\1', letters).replace(' ', '')
        if letters != dec[i]: bad.append(i)
        for t in re.findall(r'\[\.\.\. extent unknown: [^\]]*\]|\[[^\]]*\]|\S+', m):
            if t.startswith('[... extent unknown:'):
                holes += 1; stretches.append(len(t.split(':', 1)[1].strip(' ]')))
            elif '{' in t or t.startswith('['):
                holes += 1
            else:
                clean += 1; est += len(t)
    avg = est / clean
    extra = sum(max(1, round(n / avg)) - 1 for n in stretches)
    print(f'{doc}: runs {len(dec)}, marks checked against decryption, mismatches: {bad or "none"}')
    print(f'  minimum (each stretch = 1 word): word places {clean+holes}: clean {clean}, holes {holes}, share {clean/(clean+holes):.3f}')
    print(f'  estimated (stretch = letters / {avg:.2f}): word places {clean+holes+extra}: clean {clean}, holes {holes+extra}, share {clean/(clean+holes+extra):.3f}')
