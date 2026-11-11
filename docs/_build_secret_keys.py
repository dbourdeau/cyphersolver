"""Export the keys used by secret.html ("write your own letter") from the targets' own key files.
Run from anywhere:  python docs/_build_secret_keys.py   ->  docs/secret-keys.json
Each key: id, name, who, year, slug (write-up), kind (letters | code | pigpen), enc {plain: [groups]}, dec {group: plain},
and fold {letter: substitute} for letters the key has no sign for."""
import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'docs' / 'secret-keys.json'

def inv(dec):
    enc = {}
    for g, p in dec.items(): enc.setdefault(p, []).append(g)
    return enc

def load_py(path, name):
    """The module-level literal tables (KEY, NOMEN, SHAPES...) of a target's script, without running it."""
    import ast, types
    m = types.SimpleNamespace()
    for node in ast.parse(path.read_text(encoding='utf-8')).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try: setattr(m, node.targets[0].id, ast.literal_eval(node.value))
            except ValueError: pass
            else: continue
        if (isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Attribute) and node.value.func.attr == 'split'):
            setattr(m, node.targets[0].id, ast.literal_eval(node.value.func.value).split())
    return m

keys = []
# 1. Garcia de Toledo to Philip II, 1565: two-digit homophones 12-43 in alphabetical order
tol = json.loads((ROOT / 'targets' / 'toledo1565' / 'key.json').read_text(encoding='utf-8'))['codes']
keys.append(dict(id='toledo', seal='T', name='The viceroy of Sicily', who='García de Toledo to Philip II, Messina', year=1565, slug='toledo1565',
                 kind='letters', dec=tol, enc=inv(tol), fold={'j': 'i', 'v': 'u', 'w': 'u', 'k': 'c', 'ñ': 'n', 'ç': 'z'},
                 note='Two-digit figures from 12 to 43 in alphabetical order, with two or three figures for the common letters.'))
# 2. Richelieu to Rance, 1629: homophonic figures, two frequent-word codes and the nomenclature confirmed against Avenel
ri = load_py(ROOT / 'targets' / 'richelieu' / 'final.py', 'ri')
dec = {g: p for g, p in ri.KEY.items()}
for g, p in ri.NOMEN.items():
    if re.fullmatch(r'[A-Za-zéèàç\' ]+', p): dec[g] = p.lower()
keys.append(dict(id='richelieu', seal='R', name='The Cardinal', who='Richelieu to M. de Rancé', year=1629, slug='richelieu',
                 kind='letters', dec=dec, enc=inv(dec), fold={'j': 'i', 'v': 'u', 'w': 'u', 'k': 'c', 'y': 'i', 'x': 's', 'z': 's'},
                 note='Figures with three to five choices for each vowel, 40 = de and 42 = la, and numbers for the great names.'))
# 3. Armstrong to Madison, 1808: the THE = 972 diplomatic code (580 groups rebuilt from the State Department's pencil decodes)
src = (ROOT / 'docs' / 'armstrong_key972.js').read_text(encoding='utf-8-sig')
code = json.loads(src[src.index('{'):src.rindex('}') + 1])
dec = {g: v[0] for g, v in code.items() if v[0] and '*' not in v[0] and '?' not in v[0]}
keys.append(dict(id='armstrong', seal='A', name='The American minister', who='John Armstrong to James Madison, Paris', year=1808, slug='armstrong',
                 kind='code', dec=dec, enc=inv(dec), fold={},
                 note='A numbered code of whole words, syllables and letters; 972 is the. Words the code lacks are spelt from syllables.'))
# 4. Needham to Walsingham, 1587: the three-grid pigpen (Wilkes cipher)
nd = load_py(ROOT / 'targets' / 'needham1587' / 'decode.py', 'nd')
dec = {}
for i, s in enumerate(nd.SHAPES):
    dec[f'{i}'] = 'abcdefghi'[i]; dec[f'{i}.'] = 'klmnopqrs'[i]
    if i < 6: dec[f'{i}:'] = 'tuwxyz'[i]
keys.append(dict(id='pigpen', seal='W', name='The spy in the Low Countries', who='Needham to Walsingham, Flushing', year=1587, slug='needham1587',
                 kind='pigpen', dec=dec, enc=inv(dec), fold={'j': 'i', 'v': 'u'},
                 note='Nine box shapes, plain for a to i, with a dot below for k to s and a dot inside for t to z. The shapes are drawn '
                      'here in textbook grid form; the letter values are those of the key rebuilt from f. 39v.'))
# 5. Henri IV to Maurice of Hesse-Kassel, 1602-04: numbered letters, with a comma, two dots or an overbar marking word codes
import sys; sys.path.insert(0, str(ROOT / 'targets' / 'hesse1603')); import key as hk
OVER = lambda n: ''.join(ch + '̅' for ch in str(n))
dec = {str(n): p for n, p in hk.LET.items()}
for table, mark in ((hk.VIRG, lambda n: f'{n},'), (hk.DOTS, lambda n: f'{n}:'), (hk.BAR, OVER)):
    for n, p in table.items():
        if re.fullmatch(r"[A-Za-zéèàç' ]+", p): dec[mark(n)] = p.lower()
keys.append(dict(id='hesse', seal='H', name='The King of France', who='Henri IV to Maurice of Hesse-Kassel', year=1603, slug='hesse1603',
                 kind='letters', dec=dec, enc=inv(dec), fold={'j': 'i', 'v': 'u', 'w': 'u', 'k': 'c', 'z': 's'},
                 note='Two-digit figures with two to seven choices a letter; the same numbers with a comma, two dots or a bar over them '
                      'stand for words: 17, = la, 39, = mon, 31 with a bar = Pape.'))
# 6. Kauderbach to Friedrich August II, 1754-58: unseparated Saxon figures, letters and syllables (key rebuilt against the 1761 key)
kd = json.loads((ROOT / 'targets' / 'kauderbach1754' / 'key.json').read_text(encoding='utf-8'))
dec = {g: p for g, p in kd.items() if isinstance(p, str) and re.fullmatch(r'[a-z]+', p)}
keys.append(dict(id='kauderbach', seal='K', name='The Saxon resident', who='Kauderbach to Friedrich August II, The Hague', year=1755, slug='kauderbach1754',
                 kind='letters', dec=dec, enc=inv(dec), fold={'j': 'i', 'v': 'u', 'w': 'u', 'q': 'k', 'k': 'c'},
                 note='Two-digit figures for letters and common syllables (02 de, 41 la, 62 que), written in the originals without breaks between the groups.'))
OUT.write_text(json.dumps(dict(keys=keys), ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
print(OUT, [(k['id'], len(k['dec'])) for k in keys])
