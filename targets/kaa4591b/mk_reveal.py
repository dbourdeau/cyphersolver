"""Write docs/reveal/kaa4591b.json: the first lines of R9322 f.121 decoded sign by sign with sysB/key_from_glosses.tsv.
A sign whose key letter disagrees with the contemporary gloss word above it (same length only) is marked 'unc';
word signs DAG / BIGX / FLW are 'code'. Run from anywhere: python targets/kaa4591b/mk_reveal.py"""
import io, os, json, re
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(H))
key = {}
for l in io.open(os.path.join(H, 'sysB', 'key_from_glosses.tsv'), encoding='utf8'):
    c = l.rstrip('\n').split('\t')
    if c[0] != 'sign':
        key[c[0]] = c[1]
CODES = {'DAG': 'King John', 'BIGX': 'Ferdinand', 'FLW': '?'}
toks = []
for l in io.open(os.path.join(H, 'sysB', 'R9322_p1.tsv'), encoding='utf8'):
    c = l.rstrip('\n').split('\t')
    if not c[0].isdigit() or int(c[0]) > 3:
        continue
    gw = c[2].split()
    for i, w in enumerate(c[1].split()):
        signs = [t.rstrip('?') for t in w.split('.') if t.rstrip('?')]
        g = re.sub(r'[^a-z]', '', gw[i].lower()) if i < len(gw) and gw[i] != "''" else ''
        if len(signs) == 1 and signs[0] in CODES:
            toks.append({'g': signs[0], 'p': CODES[signs[0]], 'cls': 'code' if CODES[signs[0]] != '?' else 'unk'})
        else:
            for j, s in enumerate(signs):
                v = key.get(s, '?')
                cls = '' if v != '?' else 'unk'
                if v != '?' and g and len(g) == len(signs) and g[j] != v:
                    cls = 'unc'
                toks.append({'g': s, 'p': v, 'cls': cls})
        toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
toks.pop()
out = {
 'slug': 'kaa4591b',
 'anchor': 'r9322',
 'title': "Łaski to a Bavarian duke, Buda, 24 November 1529: the opening",
 'caption': "The first three lines of R9322 (BayHStA Kurbayern Äußeres Archiv 4591 f. 121), decoded sign by sign with the key rebuilt from the contemporary glosses: “Dici non potest, princeps illustrissime et domine mi observantissime, quam grata fuerint [King John] consilia vestre illustrissime dominacionis, pro quibus magnas agit gracias”. A sign marked uncertain is one where the key letter and the gloss above it differ.",
 'unit': 'signs',
 'key_note': "One sign per letter (W serves c and t), and stand-alone word signs: the large dagger DAG is King John. Signs are shown as the transcription codes of sysB/signs.md (AST = starred x, O+ = circled cross, OD = dotted circle, HH = barred double stroke).",
 'tokens': toks,
}
json.dump(out, io.open(os.path.join(ROOT, 'docs', 'reveal', 'kaa4591b.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(sum(1 for t in toks if t['g']), 'signs;', sum(t['cls'] == 'unc' for t in toks), 'unc')
print(''.join(t['p'] if len(t['p']) == 1 else '[' + t['p'] + ']' for t in toks))
