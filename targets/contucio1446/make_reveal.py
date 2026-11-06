"""Write docs/reveal/contucio1446.json (the site's "Watch it decipher" figure) from transcription.txt, lines 26-28."""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from decode import KEY, lines

# label -> an approximation of the sign as drawn in f. 148 (key.md, "Sign labels")
GLYPH = {
    'a1': '-o', 'a2': 'o', 'a3': 'ϙ', 'c1': 'ſi', 'c2': 'f', 'd1': 'ꞡ', 'd2': "ꞡ'", 'e1': 'ɧ', 'e2': 'ƀ',
    'f1': 'x', 'f2': 'ꭗ', 'g1': 'l', 'i1': 'n', 'i2': 'ŋ', 'l1': 'ſ', 'l2': '|', 'm1': 'b', 'n1': 'c', 'n2': 'α',
    'o1': 'q', 'p1': 'u', 'p2': 'ϑ', 'q1': 'ꝛ', 'q2': 'xp', 'r1': 't', 'r2': 'ŧŧ', 's1': 'k', 's2': 'ꝁ',
    't1': '∍', 't2': '∓', 'u1': '⊔', 'u2': 'Π', 'u3': '⊏', 'u4': 'E', 'et': '⊖', 'per': '≻', 'che': 'bɪ',
    'con': 'ŧŧ°', 'quale': 'ṽ', 'stat': 'stat', 'pec': 'pec', 'utinam': 'vtinã', 'null': '✱',
}
CODE = {'et', 'per', 'che', 'con', 'quale', 'stat', 'pec'}

tokens = []
for ref, body in lines():
    if ref not in ('f148r.26', 'f148r.27', 'f148r.28'):
        continue
    for p in re.split(r'(\{[^}]*\})', body):
        if p.startswith('{'):
            tokens.append({'g': '', 'p': p.strip('{}'), 'cls': 'plain'})
            continue
        for tok in p.split():
            lab = tok.rstrip('?')
            v = KEY[lab].strip('[]').lower()
            cls = 'unk' if lab == 'utinam' else 'code' if lab in CODE else 'unc' if tok.endswith('?') else ''
            tokens.append({'g': GLYPH[lab], 'p': '?' if lab == 'utinam' else v, 'cls': cls})

out = {
    'slug': 'contucio1446', 'anchor': 'reading',
    'title': 'Watch it decipher: f. 148r, lines 26-28',
    'caption': 'The first three cipher lines deciphered sign by sign with the envoys\' key (DECODE R5314): "tanto per la '
               'desfatione del Duca de Milano quanto de la vostra perdeta, et del vostro danno ..."',
    'unit': 'sign',
    'key_note': 'Key: ASMi Carteggio Sforzesco cart. 1597 no. 14 (DECODE R5314). Signs drawn approximately; '
                'utinam is a code word not on the key copy.',
    'tokens': tokens,
}
dest = HERE.parent.parent / 'docs' / 'reveal' / 'contucio1446.json'
dest.write_text(json.dumps(out, ensure_ascii=False, indent=0) + '\n', encoding='utf-8')
print(dest, len(tokens), 'tokens')
