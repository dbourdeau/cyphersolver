#!/usr/bin/env python3
"""Apply the shape classes in shapes/ to the transcriptions as published at commit 46dec7b: relabel ÷ by dot
position (Na/Nb, /a and /b) and Ridolfi's stem signs by form (Zh, Za, LL), keeping the two-valued label or the
recorded alternative wherever the sorter's confidence was low, then move to strict the words that no longer hold
an ambiguous sign. Record of what was done on 14 November 2026; the committed transcriptions are its output plus
hand edits (spellings with ll, person-sign rows, Alamanni 220v:21.4 and 221v:3-4, and the
alternatives and notes added after the second review: Ridolfi 112r:10.6, Alamanni 220v:10.2,
221v:2.6, 221v:4.6, and the bare n/c and d/l notes removed from strict rows).
usage: python3 apply_shapes.py <dir holding the 46dec7b transcriptions and key.json>"""
import csv, json, re, sys, os
D = sys.argv[1]; F = os.path.dirname(os.path.abspath(__file__))
TOKEN = re.compile(r"^(\^?)([^=\{\?]+|\?)(?:=([^\{\?]*))?(?:\{([^}]*)\})?(\?)?$")
key = json.load(open(os.path.join(D, 'key.json')))['signs']
def load(p): return list(csv.DictReader(open(p), delimiter='\t'))
def new_label(letter, fam, r):
    hi = r['confidence'] == 'high'
    if fam == 'A':
        gen = 'N' if letter == 'ridolfi' else '/'
        if not hi: return None
        if 'above' in r['dots']: return gen + 'a'
        if r['dots'] == 'below': return gen + 'b'
        return None
    c = r['class']
    if letter == 'ridolfi':
        if not hi: return None
        return {'B1': 'Zh', 'B6': 'Zh', 'B2': 'Za', 'B5': 'LL'}.get(c)
    return None
stats = {}
for letter, fn, sd in (('ridolfi', 'ridolfi-transcription.tsv', 'ridolfi'), ('alamanni', 'alamanni-transcription.tsv', 'alamanni')):
    rel = {}
    for fam in 'AB':
        for r in load(os.path.join(F, 'shapes', sd + '-' + fam + '.tsv')):
            nl = new_label(letter, fam, r)
            if nl: rel[(r['id'], int(r['j']))] = (nl, r)
    conf = {(r['id'], int(r['j'])): r['confidence'] for r in load(os.path.join(F, 'shapes', sd + '-B.tsv'))}
    lines = open(os.path.join(D, fn)).read().split('\n'); out = []; n_rel = n_strict = 0
    for line in lines:
        f = line.split('\t')
        if line.startswith('#') or line.startswith('id\t') or len(f) < 6 or f[3] != 'word':
            out.append(line); continue
        toks = f[4].split(); changed = False
        for j, t in enumerate(toks):
            if (f[0], j) in rel:
                nl, r = rel[(f[0], j)]
                raised, lab, chosen, alts, low = TOKEN.match(t).groups()
                if lab not in ('N', '/', 'Z', 'Zx', '5'): raise SystemExit(f"{f[0]} {j}: unexpected label {lab}")
                if alts and set(alts.split(',')) <= {'Z', '5'}: alts = None      # both were the same arm/hook form
                toks[j] = raised + nl + ('{' + alts + '}' if alts else '') + (low or ''); changed = True; n_rel += 1
        if letter == 'alamanni':                     # a d/l alternative is dropped only on a high-confidence sort
            for j, t in enumerate(toks):
                if t in ('5{Zd}', 'Zd{5}') and conf.get((f[0], j)) == 'high': toks[j] = t.split('{')[0]; changed = True
        f[4] = ' '.join(toks)
        if changed and f[5] in ('forced', 'lenient'):
            clean = True
            for t in toks:
                raised, lab, chosen, alts, low = TOKEN.match(t).groups()
                if lab not in key and lab not in ('Na', 'Nb', '/a', '/b', 'Zh', 'Za', 'LL'): raise SystemExit(lab)
                multi = lab in key and len(key[lab]['values']) > 1
                if multi or alts or low or lab == '?' or (lab in key and key[lab]['grade'] == 'I'): clean = False
            if clean: f[5] = 'strict'; n_strict += 1
        out.append('\t'.join(f))
    open(os.path.join(D, fn), 'w').write('\n'.join(out))
    print(letter, 'signs relabelled', n_rel, 'words moved to strict', n_strict)
