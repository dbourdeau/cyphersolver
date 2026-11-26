#!/usr/bin/env python3
"""eaglepass1917: apply key.tsv to transcription.txt (first reading of every [a/b]); writes decryption.txt.
Standard library only.  Run from the repository root:  python3 -I targets/eaglepass1917/decrypt.py
Option --alt "121=N,241=P" swaps single letters (1-based cipher positions) to show the effect of a doubtful reading."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def key():
    k = {}
    for line in open(os.path.join(HERE, 'key.tsv'), encoding='utf-8'):
        if line.startswith('#') or line.startswith('cipher\t') or not line.strip():
            continue
        c, p = line.split('\t')[:2]
        k[c] = p
    return k

def lines():
    out = []
    for line in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        lab, groups = line.rstrip('\n').split('\t')
        groups = re.sub(r'\[(\w)/\w\]', r'\1', groups).replace('/', '')
        out.append((lab, groups.split()))
    return out

def main():
    alt = {}
    if '--alt' in sys.argv:
        for kv in sys.argv[sys.argv.index('--alt') + 1].split(','):
            i, v = kv.split('='); alt[int(i)] = v
    k = key(); n = 0; res = ['# eaglepass1917 - unedited output of key.tsv on transcription.txt (first readings), group by group; ? = no value',
                             '# line<TAB>cipher groups<TAB>plain groups']
    for lab, groups in lines():
        cg, pg = [], []
        for g in groups:
            cs, ps = '', ''
            for ch in g:
                n += 1
                ch = alt.get(n, ch)
                cs += ch; ps += k.get(ch, '?')
            cg.append(cs); pg.append(ps)
        res.append(f"{lab}\t{' '.join(cg)}\t{' '.join(pg)}")
    res.append(f'# {n} cipher letters')
    text = '\n'.join(res) + '\n'
    if alt:
        sys.stdout.write(text)
    else:
        open(os.path.join(HERE, 'decryption.txt'), 'w', encoding='utf-8').write(text); sys.stdout.write(text)

if __name__ == '__main__':
    main()
