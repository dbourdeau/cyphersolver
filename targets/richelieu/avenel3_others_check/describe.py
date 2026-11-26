"""Complément 1630 (PREREG2.md) : description de l'accord clé #813 / gloses d'Avenel, et comptage des signes.
Usage : python3 -I describe.py <avenel_figures_V2.txt> <out.json> <out_decodage.txt>
Écrit AVANT toute exécution sur V2 ; une seule exécution (voir PREREG2.md).
Clé : PR #813, tête fbc611f8 (targets/richelieu/final.py : KEY + 41 = que), gelée ; 42 = « la » tel quel.
Pas de seuil appliqué ici si la portion « sans déchiffrement imprimé » compte < 300 signes : sortie descriptive."""
import re, sys, json, random, unicodedata
KEY = {'10':'c','11':'b','12':'g','13':'p','14':'l','15':'o','16':'r','17':'f','18':'t','19':'a','20':'d','21':'i',
       '22':'n','23':'h','24':'m','25':'s','26':'u','27':'e','28':'q','29':'a','30':'e','31':'i','32':'o','33':'u',
       '34':'a','35':'e','36':'i','37':'o','38':'u','39':'et','40':'de','41':'que','42':'la'}
NOMEN = {'51':'le Roi','52':'la Reine mère','54':'Monsieur','58':'Mme de Chevreuse','59':'princesse Marie',
         '60':'Mme de Longueville','66':'card. de La Valette','83':"l'Espagne",'84':"l'Angleterre",'92':'la Lorraine',
         '55':'M. le Prince','61':"le duc d'Epernon",'62':'Montmorency','67':'Calori','68':'le cardinal de Berulle',
         '69':'le garde des sceaux','95':'Nismes','96':'Castres','97':'Montauban'}
DANIEL_CODES = {'51','52','54','58','59','60','66','83','84','92'}   # table de Daniel @ 9736c436
LETTER_FIGS = [str(n) for n in range(10, 39)]
SEED, NWIT, MIN_SIGNS = 20261120, 200, 300
NO_WORD_READING = {('CCCXVII', 4)}   # Avenel donne les valeurs des lettres, pas la lecture en mots

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if 'a' <= c <= 'z')
    return s.translate(str.maketrans('jvy', 'iui'))

def parse(path):
    t = open(path, encoding='utf-8').read()
    t = t.split('\n## Hors système')[0]
    letters = {}
    for m in re.finditer(r"== (\S+) \|(.*?)(?=\n== |\Z)", t, re.S):
        name, block = m.group(1), m.group(2)
        pages = []
        for l in block.splitlines():
            mm = re.match(r"# p\.(\d+): (.*)", l)
            if mm:
                notes = {}
                for part in mm.group(2).split(' | '):
                    pm = re.match(r"(\d+) (.*)", part.strip())
                    if pm: notes[int(pm.group(1))] = pm.group(2)
                pages.append((int(mm.group(1)), notes))
        body = '\n'.join(l for l in block.splitlines() if not l.startswith('#'))
        segs, cur, pi, prev = [], [], 0, None
        for mm in re.finditer(r"\[([^\]]*)\]|\{(\d+)\}|\^(\d+)", body):
            if mm.group(1) is not None:
                toks = [x for x in mm.group(1).split() if re.fullmatch(r"~?\d+", x)]
                if toks: cur.append(('run', toks))
            elif mm.group(2): cur.append(('code', mm.group(2)))
            else:
                n = int(mm.group(3))
                if prev is not None and n <= prev: pi += 1
                prev = n
                page, notes = pages[pi] if pi < len(pages) else (None, {})
                segs.append({'items': cur, 'call': n, 'page': page, 'gloss': notes.get(n)}); cur = []
        letters[name] = segs
    return letters

def dec(toks, key):
    out = ''
    for t in toks:
        d = t.startswith('~'); f = t.lstrip('~')
        v = key.get(f, '?')
        out += (v * 2 if d and len(v) == 1 else v)
    return out

def semi(r, g):
    prev = [0] * (len(g) + 1)
    for i in range(1, len(r) + 1):
        cur = [i] + [0] * len(g)
        for j in range(1, len(g) + 1):
            cur[j] = min(prev[j] + 1, cur[j-1] + 1, prev[j-1] + (r[i-1] != g[j-1]))
        prev = cur
    return min(prev)

def score(segs, key):
    dist = n = signs = 0
    for s in segs:
        if not s['gloss']: continue
        g = norm(s['gloss'])
        for kind, x in s['items']:
            if kind != 'run': continue
            r = dec(x, key); dist += semi(r, g); n += len(r); signs += len(x)
    return (1 - dist / n if n else None), signs, n

def main():
    L = parse(sys.argv[1])
    out = {'key': 'PR #813 fbc611f8 (KEY + 41)', 'pieces': {}}
    untested_signs = 0; existing = []
    lines = []
    for name, segs in L.items():
        runs = [x for s in segs for k, x in s['items'] if k == 'run']
        codes = [x for s in segs for k, x in s['items'] if k == 'code']
        signs = sum(len(x) for x in runs)
        nog = [s for s in segs if any(k == 'run' for k, _ in s['items']) and (not s['gloss'] or (name, s['call']) in NO_WORD_READING)]
        u = sum(len(x) for s in nog for k, x in s['items'] if k == 'run'); untested_signs += u
        ex = [s for s in segs if s['gloss'] and (name, s['call']) not in NO_WORD_READING]
        existing += ex
        acc, sc, nc = score(ex, KEY)
        out['pieces'][name] = {'runs': len(runs), 'signs': signs, 'codes': codes,
                               'codes_not_in_key813': sorted({c for c in codes if c not in NOMEN}),
                               'codes_ext813_used': sorted({c for c in codes if c in NOMEN and c not in DANIEL_CODES}),
                               'signs_without_word_reading': u,
                               'agreement_with_gloss': round(acc, 4) if acc is not None else None,
                               'signs_scored': sc, 'decoded_chars': nc}
        lines.append(f'\n== {name}')
        for s in segs:
            parts = []
            for k, x in s['items']:
                parts.append('⟦' + dec(x, KEY) + '⟧' if k == 'run' else '{' + NOMEN.get(x, '?' + x) + '}')
            if parts:
                lines.append(f"p.{s['page']} ^{s['call']}: {' '.join(parts)}   ‖ Avenel : {s['gloss']}")
    acc, sc, nc = score(existing, KEY)
    rng = random.Random(SEED); vals = [KEY[f] for f in LETTER_FIGS]; wit = []
    for _ in range(NWIT):
        v = vals[:]; rng.shuffle(v); k = dict(KEY); k.update(dict(zip(LETTER_FIGS, v)))
        wit.append(score(existing, k)[0])
    out['existing_descriptive'] = {'signs_scored': sc, 'decoded_chars': nc, 'agreement': round(acc, 4),
                                   'best_control': round(max(wit), 4), 'mean_control': round(sum(wit) / len(wit), 4),
                                   'note': 'descriptif (pièces glosées = EXISTING), pas un test'}
    out['untested_signs'] = untested_signs
    out['measurable'] = untested_signs >= MIN_SIGNS
    out['verdict'] = 'mesure' if out['measurable'] else 'non mesurable (< 300 signes sans déchiffrement imprimé) : description seulement'
    json.dump(out, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
    open(sys.argv[3], 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print(json.dumps(out, ensure_ascii=False, indent=1))
if __name__ == '__main__': main()
