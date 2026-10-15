"""Write docs/reveal/r9367.json: lines L16-L19 of R9367 sign by sign with the mapping of r9367/dec.py (key R9423
block 2_4 matched by shape, plus the letter's own values); D, W and Q (the register's name signs) act as nulls or
dividers here. Signs with a doubtful value (O, # and those dec.py leaves open) are marked 'unk'. Clear words shown
as plain. Run: python targets/r9367/mk_reveal.py"""
import io, os, re, json
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(H))
src = io.open(os.path.join(H, 'r9367', 'dec.py'), encoding='utf8').read()
g = {}
exec(src.split('for l in open')[0], {'re': re}, g)     # the mapping m of dec.py
m = g['m']
toks = []
for l in io.open(os.path.join(H, 'r9367', 'transcription.txt'), encoding='utf8'):
    mm = re.match(r'(L1[6-9]) (.*)', l.rstrip('\n'))
    if not mm:
        continue
    rest = re.split(r'\s{3,}\(', mm.group(2))[0]
    for part in re.split(r'(\[[^\]]*\])', rest):
        if part.startswith('['):
            for w in part[1:-1].split():
                toks.append({'g': '', 'p': w + ' ', 'cls': 'plain'})
            continue
        for w in part.split():
            for c in w:
                v = m.get(c, '?')
                if v in ('·', '(c)'):
                    toks.append({'g': c, 'p': '', 'cls': 'null'})
                elif v in ('?', 'd?', '[#]') or v.startswith('['):
                    toks.append({'g': c, 'p': '?', 'cls': 'unk'})
                else:
                    toks.append({'g': c, 'p': v, 'cls': ''})
            toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
out = {
 'slug': 'r9367',
 'anchor': 'reading',
 'title': 'A son to his father, 22 March 1535: “seltsam khinst gefragt”',
 'caption': 'Lines 16–19 of R9367 (BayHStA Kurbayern Äußeres Archiv 4591 f. 169), the cipher runs sign by sign with key R9423 block 2_4 as matched by shape, between the clear words of the letter: “… erfodert mich … seltsam khinst gefragt, ich hab aber a[ll]es verlaugnet, so ich kan, und hab vergeben, ich sey am schlechter schreiber …”. A working reading: several values are uncertain, and three of the register’s name signs serve here as nulls.',
 'unit': 'signs',
 'key_note': 'Letter signs of key block 2_4 (A 9, B v, C Δ, D +, E 6 …, und 9, ch t) with five values added from the letter; shown as the transcription codes of r9367/transcription.txt.',
 'tokens': toks,
}
json.dump(out, io.open(os.path.join(ROOT, 'docs', 'reveal', 'r9367.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len([t for t in toks if t['g']]), 'signs')
print(''.join(t['p'] if t['cls'] != 'null' else '·' for t in toks))
