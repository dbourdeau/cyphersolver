"""Write docs/reveal/laigue1649.json: the first lines of the unglossed opening (f. 117r ll. 0-4), values exactly as
n43/decode_opening.py assigns them (gloss majority G, code structure S, context C). C values are marked uncertain,
nulls as null, clear words as plain."""
import re, json
G = {}
for l in open('n43/key43.txt', encoding='utf-8'):
    n, rest = l.rstrip('\n').split('\t'); G[int(n)] = rest.split()[0].rsplit(':', 1)[0]
S = {37: 'o', 38: 'n', 46: 'e', 59: 'i', 80: 't', 81: 's', 86: 'n'}
NULL = {99, 119, 129, 150, 206, 207, 222, 229, 230, 237, 240}
C = {279: 'de', 277: 'do', 354: 'ne', 358: 'me', 364: 'la', 314: 'je', 321: 'gu', 390: 'ru', 398: 'que', 400: 'pu',
     407: 'e', 439: 'se', 442: 'ti', 443: 'te', 445: 'su'}
toks = []
for line in open('n43/opening_c245.txt', encoding='utf-8'):
    if line.startswith('#'): continue
    lab, body = line.split(':', 1)
    if int(lab[1:]) > 4: break
    body = re.sub(r'\^\[([^\]]*)\]', r'\1', body)
    for tok in body.split():
        if tok.startswith('#'):
            toks.append({'g': '', 'p': tok[1:], 'cls': 'plain'}); continue
        n = int(re.sub(r'\D', '', tok)); g = tok.rstrip('?').replace('_', '̲')
        if n in NULL: toks.append({'g': g, 'p': '', 'cls': 'null'}); continue
        if n in S: v, cls = S[n], ''
        elif n in C: v, cls = C[n], 'unc'
        elif n in G: v, cls = G[n], ''
        else: toks.append({'g': g, 'p': '?', 'cls': 'unk'}); continue
        if tok.endswith('_') and len(v) == 2: v = v[::-1]
        if tok.endswith('?'): cls = 'unc'
        toks.append({'g': g, 'p': v, 'cls': cls})
d = {'slug': 'laigue1649', 'anchor': 'no43',
     'title': 'Pour Monsieur de Legue: the unglossed opening',
     'caption': "f. 117r, lines 1-5 of no. 43, which the clerk left without a decipherment, with the values of the key rebuilt from his glosses elsewhere. Uncertain = a second-series syllable fixed by context; an underlined number reverses its syllable.",
     'unit': 'numbers',
     'key_note': 'Values as n43/decode_opening.py assigns them: majority gloss of the same number, code structure, or context.',
     'tokens': toks}
json.dump(d, open('../../docs/reveal/laigue1649.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(toks), ' '.join(t['p'] for t in toks))
