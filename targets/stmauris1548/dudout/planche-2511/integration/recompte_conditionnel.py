"""recompte_conditionnel.py (25/11/2026, fil 🔓) — recompte de LECTURE seulement, CONDITIONNEL, NON APPLIQUÉ.
Planche stmauris1548-2511 : contrôle caché K1 raté -> rien n'est intégré (REGLE-SELECTION.md §0). Ce script dit seulement
ce que deviendraient les lectures L1/L2 d'O5 SI Brice levait le contrôle K1 et si les 95 jetons tB-t1 (« ∞ ») étaient
nommés `w` (clé WAINUT inchangée : w = o). Aucune nouvelle mesure, aucun verdict ; O5 reste FAIL.
Règles : une MAJUSCULE O posée par un lecteur sur un ∞ devient une lettre du décodage (o) ; une majuscule autre que O sur un ∞
= conflit, le mot passe irrésolu ; les mots irrésolus et les nulles ne sont PAS relus (restent tels quels, ? -> o).
Reclassement mécanique par mot (règles check_lecture_o5.py) : 0 lettre du sens -> sûr ; 1 lettre et >= 2 du décodage ->
probable ; sinon restitué. Lancer : python3 -I recompte_conditionnel.py (depuis n'importe où)."""
import os, sys, re, json
H = os.path.dirname(os.path.abspath(__file__)); O5 = os.path.join(H, '..', '..', 'o5-2511')
sys.path.insert(0, os.path.join(O5, 'tools')); import check_lecture_o5 as C
def key(p):
    K = {}
    for l in open(p, encoding='utf-8'):
        if not l.strip() or l.startswith('# '): continue
        f = l.rstrip('\n').split('\t')
        if len(f) >= 2: K[f[0]] = '' if f[1] == '-' else f[1].lower().replace('j', 'i').replace('v', 'u')
    return K
sys.path.insert(0, os.path.join(O5, '..', 'o2-2311', 'wainut-scripts')); from compare import load
K = key(os.path.join(O5, '..', 'o2-2311', 'wainut-key.tsv'))
rows = load(os.path.join(O5, 'transcription_1548-03-12_Q_merged_named.txt'))
D = []; SRC = []
for k, r in rows.items():
    for t in r:
        t = 'NIL' if t.endswith('_') else t
        v = K.get(t, '?')
        for c in v: D.append(c); SRC.append(t)
D = ''.join(D); D0 = ''.join(s for _, s in C.load_decode(os.path.join(O5, 'lecture-input', 'DECODE-O5.txt')))
assert D == D0, 'décodage non reproduit'
INF = {i for i, t in enumerate(SRC) if t == 'tB-t1'}
assert all(D[i] == '?' for i in INF)
D2 = ''.join('o' if i in INF else c for i, c in enumerate(D))
out = {'tB-t1_jetons': len(INF), '?_avant': D.count('?'), '?_apres': D2.count('?')}
def redo(path):
    text = '\n'.join(l for l in open(path, encoding='utf-8').read().split('\n') if not l.startswith('#'))
    starts = {}; q = 0
    for k, s in C.load_decode(os.path.join(O5, 'lecture-input', 'DECODE-O5.txt')): starts[k] = q; q += len(s)
    p = 0; new = []; st = dict(O_confirmes=0, conflits=0, conflits_detail=[], mots_changes=[])
    for raw in C.tokens(text):
        if raw.startswith('§'): new.append(raw); continue
        cls = 'S'; body = raw
        if raw[0] in C.OPEN: cls = C.OPEN[raw[0]][1]; body = raw[1:-1]
        n_suffix = ''
        if cls == 'I' and '|' in body: body, _, n = body.rpartition('|'); n_suffix = '|' + n
        parts = re.split(r"([\s'’-]+)", body); outw = []; conflict = False
        for w in parts:
            if not w or re.fullmatch(r"[\s'’-]+", w): outw.append((w, None, w)); continue
            nw = ''; ns = nd = 0; raw2 = ''
            for c in w:
                if c == '?' or c.islower():
                    nw += ('o' if (c == '?' and p in INF) else c); raw2 += D2[p]; p += 1; nd += 1
                else:
                    if p < len(D) and D[p] == '?':
                        raw2 += D2[p]
                        if p in INF:
                            if c == 'O': nw += 'o'; nd += 1; st['O_confirmes'] += 1
                            else: nw += c; ns += 1; conflict = True; st['conflits'] += 1; st['conflits_detail'].append('%s (%s sur ∞)' % (raw, c))
                        else: nw += c; ns += 1
                        p += 1
                    else: nw += c; ns += 1
            outw.append((nw, (ns, nd), raw2))
        if cls in 'IN':
            new.append({'I': '‹%s›', 'N': '(%s)'}[cls] % (''.join(x[0] for x in outw) + n_suffix)); continue
        if conflict:
            new.append('‹%s|%d›' % (''.join(x[2] for x in outw), sum(1 for x in outw if x[1] is not None))); continue
        for w, info, _ in outw:
            if info is None: continue
            ns, nd = info
            c2 = 'S' if ns == 0 else ('P' if ns == 1 and nd >= 2 else 'R')
            if c2 != cls: st['mots_changes'].append('%s %s→%s' % (w, cls, c2))
            new.append(w if c2 == 'S' else ('{%s}' % w if c2 == 'P' else '[%s]' % w))
    assert p == len(D)
    t2 = ' '.join(new)
    err, toks, _ = C.analyse(D2, {k: v for k, v in starts.items()}, t2)
    err = [e for e in err if 'repère' not in e]
    assert not err, err[:5]
    r = C.score(D2, toks); r.pop('spans'); r.pop('classes')
    return r, st, t2
for L in ('L1', 'L2'):
    r, st, t2 = redo(os.path.join(O5, 'lecture-' + L, 'LECTURE.txt'))
    old = json.load(open(os.path.join(O5, 'lecture-' + L, L + '.json'), encoding='utf-8'))
    out[L] = dict(avant={k: old[k] for k in ('words', 'words_total', 'share_read', 'share_restored', 'share_probable')},
                  apres_conditionnel={k: r[k] for k in ('words', 'words_total', 'share_read', 'share_restored', 'share_probable', 'decode_unknown', 'warnings')},
                  O_poses_sur_inf_confirmes=st['O_confirmes'], conflits=st['conflits'], conflits_detail=st['conflits_detail'],
                  n_mots_reclasses=len(st['mots_changes']), mots_reclasses=st['mots_changes'])
    open(os.path.join(H, 'LECTURE-%s-conditionnelle-inf-w.txt' % L), 'w', encoding='utf-8').write(
        '# CONDITIONNEL, NON APPLIQUÉ (K1 raté) : lecture %s d\'O5 reclassée mécaniquement si ∞ (tB-t1) = w = o. Pas une mesure.\n' % L + t2 + '\n')
json.dump(out, open(os.path.join(H, 'recompte-conditionnel.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if kk not in ('mots_reclasses',)}) for k, v in out.items()}, ensure_ascii=False, indent=1))
