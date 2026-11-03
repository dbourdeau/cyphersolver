#!/usr/bin/env python3
"""Recount the readings per letter and leaf. Standard library only.

Estimated words: letters of the decryption with codes expanded, divided by 4.35, the rate of c. 107.
plain      words outside any bracket, including repairs word-with-degree-mark. This is the ceiling.
no hole    plain words in sentence blocks with no [...]; they may hold [?word] and codes.
clean      words in blocks with no [...], no [?word] and no unknown code.
verbatim   clean blocks that also hold no repair.
A block counts on the leaf where it starts.
"""
import os, re

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here if os.path.exists(os.path.join(here, 'key.tsv')) else os.path.dirname(here))
est = {}
for f in ('decryption_0078_0079.txt', 'decryption_0174_0175.txt'):
    for l in open(f, encoding='utf8'):
        lab, _, b = l.strip().partition(' ')
        b = re.sub(r'\[#[^\]]+\]', 'xxxxx', b)
        b = re.sub(r'[\[\]?. ]', '', b)
        est[lab[0]] = est.get(lab[0], 0) + len(b)
LEAF = dict(A='78r', B='78v', C='79r', D='174r', E='174v', F='175r', G='175v')
HOLE = r'\[\.\.\.\]'
CODE = r'\[(?:L\^\w+|\d+)\]'
WORD = r"[A-Za-zà°]+(?:'[A-Za-zà°]+)?"
KEYS = ('blocks', 'nohole_blocks', 'clean_blocks', 'verbatim_blocks', 'plain', 'nohole', 'clean', 'verbatim',
        'repaired', 'doubtful', 'holes', 'codes')


def plain(t):
    return re.findall(WORD, re.sub(r'\[[^\]]*\]', ' ', t))


leaf = {k: dict.fromkeys(KEYS, 0) for k in LEAF}
for f in ('reading_0078_0079.md', 'reading_0174_0175.md'):
    text = open(f, encoding='utf8').read()
    for lab, t in re.findall(r'^IT\[([A-G]\d\d)(?:-[A-G]\d\d)?\]: (.*)$', text, re.M):
        r = leaf[lab[0]]
        n = len(plain(t))
        h = len(re.findall(HOLE, t))
        c = len(re.findall(CODE, t))
        dq = re.findall(r'\[\?[^\]]+\]', t)
        rep = t.count('°')
        r['blocks'] += 1
        r['plain'] += n
        r['holes'] += h
        r['codes'] += c
        r['repaired'] += rep
        r['doubtful'] += sum(len(x.split()) for x in dq)
        if not h:
            r['nohole_blocks'] += 1
            r['nohole'] += n
            if not c and not dq:
                r['clean_blocks'] += 1
                r['clean'] += n
                if not rep:
                    r['verbatim_blocks'] += 1
                    r['verbatim'] += n


def show(name, keys):
    e = sum(est[k] for k in keys) / 4.35
    s = {k: sum(leaf[x][k] for x in keys) for k in KEYS}

    def pc(v):
        return f'{v} ({100 * v / e:.0f}%)'
    print(f"{name:14} est {e:5.0f}  plain {pc(s['plain']):11} no hole {pc(s['nohole']):10} blocks {s['nohole_blocks']}/{s['blocks']}"
          f"  clean {pc(s['clean']):9} blocks {s['clean_blocks']}  verbatim {pc(s['verbatim']):9}"
          f"  repairs {s['repaired']}  doubtful {s['doubtful']}  holes {s['holes']}  codes {s['codes']}")


for k in LEAF:
    show('c. ' + LEAF[k], k)
show('cc. 78r-79r', 'ABC')
show('cc. 174r-175v', 'DEFG')
show('without 175r', 'DEG')
