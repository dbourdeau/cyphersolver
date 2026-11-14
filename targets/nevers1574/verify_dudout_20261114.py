#!/usr/bin/env python3
"""nevers1574: independent check of f. 15-16 (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Reads ONLY f15_key.md (the alphabet table) and f15_signs.tsv, and compares with f15_reading.md. Does not use
research/reading_audit/verify2_nevers_*.py.
Usage: python3 verify_dudout_20261114.py [path/to/targets/nevers1574] [-v]

The key has homophone-free signs but two signs with two values (9 = q/s, + = f/m), so instead of decoding to one
text, the reading is enciphered back into sign classes with the key and compared with the transcribed signs.
Both streams are normalised (in the reading y -> i and final -ct -> -t, the cipher's spelling): doubling signs (ʒ, crossed b) dropped and runs of one sign collapsed (the writer
doubles a letter either way), name/number signs (SS, [RM], [-d-], XX…) and unread marks dropped.
"""
import os, re, sys, difflib, unicodedata
D = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else '.'
V = '-v' in sys.argv
md = open(os.path.join(D, 'f15_key.md'), encoding='utf-8').read()
enc = {}
for plain, signs in re.findall(r'^\| ([a-z](?: / [a-z])?) \| ([^|]*) \|', md, re.M):
    first = re.findall(r'`([^`]+)`', signs)[0]           # first sign listed for the letter
    for p in plain.split(' / '):
        enc[p] = first
assert enc['e'] == 'F' and enc['q'] == '9' and enc['s'] == '9', enc
enc['k'] = enc['c']; enc['w'] = enc['u']
cls = {'G': 'P', '(9': 'P', 'E': 'F', 'q̶': '+'}             # same-letter variants listed in the key


def norm_signs(s):
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'\[[^\]]*\]|SS|XX[0-9m.]*', ' ', s)        # name and number signs
    s = s.replace('q̶', '+').replace('b̶', '').replace('ʒ', '').replace('(9', 'P').replace('G', 'P').replace('E', 'F')
    s = s.replace('̶', '')
    out = []
    for w in s.split():
        w = ''.join(c for c in w if c in '1±Cb F+0h73 28P9T46Zy'.replace(' ', ''))
        if w: out.append(w)
    return out


def norm_reading(t):
    t = re.sub(r'\[…\]|\[\.\.\.\]', ' ', t)
    t = re.sub(r'\[\?([^\]]*)\]', r'\1', t)
    t = re.sub(r'\b(Roy|Royne mere|Royne)\b', ' ', t)
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if c.isascii())
    t = t.replace('y', 'i')                               # spelling only: the cipher writes i for the gloss's y (luy, ay)
    t = re.sub(r'ct\b', 't', t)                           # and dit / fait for the reading's dict / faict
    out = []
    for w in re.findall(r'[a-z]+', t):
        out.append(''.join(enc[c].replace('(9', 'P').replace('G', 'P') if c != 'p' else 'P' for c in w))
    return out


def collapse(s):
    return re.sub(r'(.)\1+', r'\1', s)


sig = {}
for l in open(os.path.join(D, 'f15_signs.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    page, line, signs = l.rstrip('\n').split('\t')[:3]
    sig.setdefault(page, []).append((line, signs))
rd = open(os.path.join(D, 'f15_reading.md'), encoding='utf-8').read()
sec = {'15r': rd.split('## f. 15r')[1].split('## f. 15v')[0],
       '15v': rd.split('## f. 15v')[1].split('## f. 16r (cipher')[0],
       '16r': rd.split('## f. 16r (cipher, lines 1-19)')[1].split('## f. 16r (clear')[0]}


def stream_reading(text):
    """collapsed enciphered reading, with the reading word each class char comes from"""
    words = [w for w in re.split(r'\s+', re.sub(r'<!--.*?-->', ' ', text, flags=re.S)) if w and not w.startswith('#')]
    chars, owner = [], []
    for i, w in enumerate(words):
        e = ''.join(norm_reading(w))
        for c in e:
            if chars and chars[-1] == c: continue
            chars.append(c); owner.append(i)
    return ''.join(chars), owner, words


def stream_signs(lines):
    chars, owner = [], []
    for line, x in lines:
        for w in norm_signs(x):
            for c in w:
                if chars and chars[-1] == c: continue
                chars.append(c); owner.append((line, w))
    return ''.join(chars), owner


tot_s = tot_m = 0
for page in ('15r', '15v', '16r'):
    s, so = stream_signs(sig[page])
    r, ro, words = stream_reading(sec[page])
    sm = difflib.SequenceMatcher(None, s, r, autojunk=False)
    m = sum(b.size for b in sm.get_matching_blocks())
    tot_s += len(s); tot_m += m
    print(f'f. {page}: transcribed signs {len(s)} (collapsed), reading enciphered {len(r)}, matched {m} = {m/len(s):.3f} of the signs')
    if V:
        for op, a1, a2, b1, b2 in sm.get_opcodes():
            if op == 'equal': continue
            ws = sorted({ro[k] for k in range(max(b1-1,0), min(b2+1, len(ro)))}) if r else []
            sl = so[min(a1, len(so)-1)]
            print(f'   {op:7s} l.{sl[0]:>2s} sign word {sl[1]:14s} signs[{s[a1:a2]}] reading[{r[b1:b2]}]  ~ "{" ".join(words[i] for i in ws)}"')
print(f'all: {tot_m} of {tot_s} = {tot_m/tot_s:.3f}')
