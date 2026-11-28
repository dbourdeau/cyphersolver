"""Applique les décisions de la relecture 3x (planches/) à l'alignement gelé de Daniel et mesure
la cohérence avant/après. Contrôle : toute ligne d'alignement d'une classe NON visée reste identique."""
import json, os, sys, copy, collections
sys.path.insert(0, os.path.dirname(__file__))
from consistency import consistency
G = os.environ.get('KEYS_EYE', os.path.join(os.path.dirname(__file__), '..', '..', '..', 'keys_eye'))
OUT = os.path.join(os.path.dirname(__file__), '..', 'out')
TARGET = {'24v.6': {'LA', 'Al', 'W', 'Sr', 'St'}, '33r.4': {'S12', 'S16', 'S23', 'S24'}, '59r.2': {'S15'},
          '81r.5': {'S20'}, '92r.10': set(), '88v.10': {'S16'}, '103v.2': {'S19'}, '101r.2': {'S9'}}
def find(al, line, pos):
    for i, r in enumerate(al):
        if r[0] == line and r[1] == pos: return i
    raise KeyError((line, pos))
def find_drop(al, letter, word):
    for i, r in enumerate(al):
        if r[2] is None and r[3] == letter and r[4] == word: return i
    raise KeyError((letter, word))
LOG = collections.defaultdict(list)
PROBABLE = []
def ed(c, al, line, pos, shape=None, letter=None, why=''):
    i = find(al, line, pos); old = list(al[i])
    if shape is not None: al[i][2] = shape
    if letter is not None: al[i][3] = letter if letter != '-' else None
    LOG[c].append({'row': old, 'new': list(al[i]), 'why': why})
def edits(c, al):
    if c == '24v.6':
        for ln, p in (('24v08', 6), ('24v09', 5), ('24v10', 3)):
            ed(c, al, ln, p, shape='LB', why='planche 24v6_LA : forme B (lam-alif a barre haute crochue), = ب x3')
        ed(c, al, '24v11', 9, shape='LC', why='planche 24v6_LA Q9 : forme C (lam-alif a tete bouclee), singleton = ص')
        ed(c, al, '24v10', 5, shape='Sg', letter='غ', why='planche 24v6_Al-St-W-Sr Q23 : dents de sin sur un corps de ى, forme absente ailleurs ; البلاغه : alif omis au lieu de غ')
        al[find_drop(al, 'غ', 15)][3] = 'ا'
        ed(c, al, '24v08', 10, letter='ق', why="planche Q13/Q14 : 'سا' = un seul signe (St) aux deux endroits ; الاقاليم : alif apres lam omis (note de Daniel) au lieu de ق")
        al[find_drop(al, 'ق', 10)][3] = 'ا'
        i = find(al, '24v09', 13); LOG[c].append({'row': list(al[i]), 'new': ['(supprime)'], 'why': "planche Q14 : le trait vertical est la fin du signe 'سا' (St), pas un signe Al separe ; م de قمر non ecrit"})
        al[i] = [None, None, None, 'م', 14]
    if c == '33r.4':
        ed(c, al, '33r07', 11, shape='S18', why='planche 33r4_triangle-yabarree Q21 : meme forme que le ت de وافيت (S18), distincte du triangle de الدر')
        # Q10, Q13 (coupe a dent) : lecteur A = B, lecteur B aveugle = indecis -> {probable}, NON compte (Daniel garde)
        PROBABLE.append(('33r.4', '33r09 pos6 et 33r10 pos8 : coupe a dent = ي (S11)', 'lecteur B indecis'))
        i = find(al, '33r10', 3)
        al.insert(i + 1, ['33r10', 3.5, 'S8', 'ل', 18]); LOG[c].append({'row': ['(absent)'], 'new': al[i + 1], 'why': 'planche 33r4_divers Q18 : sablier non compte par Daniel entre la 1re coupe et le ya-barree'})
        ed(c, al, '33r10', 4, letter='ح', why='decalage apres insertion du sablier (lecture provisoire {ح})')
        ed(c, al, '33r10', 5, letter='-', why='boite longue : signe en surplus, non resolu')
        j = find_drop(al, 'م', 20); al[j] = ['33r11', 3.5, 'S1', 'م', 20]
        LOG[c].append({'row': ['(م non ecrit)'], 'new': al[j], 'why': 'planche 33r4_triangle-yabarree Q23 : ya-barree apres le separateur de la l.11, non compte par Daniel ; منكور complet'})
    if c == '103v.2':
        ed(c, al, '103v_l06', 5, shape='?', why='planche 103v2_S19 Q2 : signe gratte ; lecteurs A et B : ni A ni autre forme -> illisible')
        # Q3 : lecteur A illisible, lecteur B 'A probable' -> discordant, Daniel garde
        PROBABLE.append(('103v.2', '103v_l06 pos6 : illisible (A) / forme I probable (B)', 'discordant'))
    if c == '101r.2':
        for r in al:
            if r[2] == 'S9':
                old = list(r); r[2] = 'S9a' if r[3] == 'ه' else 'S9b'
                LOG[c].append({'row': old, 'new': list(r), 'why': 'planche 101r2_S9 : A (croix a jambage descendant) = ه x3 ; B (boucle assise sans jambage) = ح x3'})
    return al
def cons(al):
    pairs = [(r[0], r[1], r[2], r[3]) for r in al if r[2] and r[3] and r[2] != '?']
    return consistency(pairs)
os.makedirs(OUT + '/revised', exist_ok=True)
rows = []; ok_all = True
for c in TARGET:
    d = json.load(open(f'{G}/{c}.json'))
    before = cons(d['alignment'])
    al = edits(c, copy.deepcopy(d['alignment']))
    after = cons(al)
    # contrôle : classes non visées inchangées (lignes existantes)
    orig = {(r[0], r[1]): r for r in d['alignment'] if r[0]}
    touched_other = [ (k, orig[k], r) for r in al if r[0] and (r[0], r[1]) in orig
                     for k in [(r[0], r[1])] if orig[k][2] not in TARGET[c] and orig[k] != r]
    added = [r for r in al if r[0] and (r[0], r[1]) not in orig]
    if touched_other: ok_all = False
    nd = dict(d); nd['alignment'] = al; nd['revision'] = {'by': 'dudout (ljs51-residus)', 'log': LOG[c]}
    json.dump(nd, open(f'{OUT}/revised/{c}.json', 'w'), ensure_ascii=False, indent=1)
    rows.append({'chain': c, 'before': [before[0], before[1]], 'after': [after[0], after[1]],
                 'breaks_before': before[3], 'breaks_after': after[3], 'non_target_rows_changed': len(touched_other),
                 'signs_added': len(added), 'signs_before': sum(1 for r in d['alignment'] if r[2]),
                 'signs_after': sum(1 for r in al if r[2])})
json.dump(rows, open(f'{OUT}/resultats.json', 'w'), ensure_ascii=False, indent=1)
tb = tA = 0; ob = oA = 0
for r in rows:
    b, a = r['before'], r['after']; tb += b[1]; tA += a[1]; ob += b[0]; oA += a[0]
    print(f"{r['chain']:7s} avant {b[0]}/{b[1]} = {b[0]/b[1]:.3f}  apres {a[0]}/{a[1]} = {a[0]/a[1]:.3f}  signes {r['signs_before']}->{r['signs_after']}  lignes non visees modifiees: {r['non_target_rows_changed']}  ruptures apres: {json.dumps(r['breaks_after'], ensure_ascii=False)}")
json.dump(PROBABLE, open(f'{OUT}/probables_non_comptes.json', 'w'), ensure_ascii=False, indent=1)
print(f'TOTAL avant {ob}/{tb} = {ob/tb:.4f}  apres {oA}/{tA} = {oA/tA:.4f}  controle non-vises OK = {ok_all}')
