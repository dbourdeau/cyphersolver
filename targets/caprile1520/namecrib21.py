# Name/phrase cribs against R1136/R1139 token streams (3 Oct 2026): for each crib and window, count how many tokens can
# take the crib letter under the key (beam21 priors incl. look-alike unions; lone o = h/u/null is allowed to be skipped
# by trying windows with and without each lone o). Prints windows where >= 85 % of letters fit. Names from the Vestigia
# people lists of V1876 (R1136) and V1922 (R1139): Dragfi, Batthyany, Montelini, Perenyi; places/offices from context.
import os, sys, math, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('LOOK', '1')
import beam21
CRIBS = ['dragfi', 'dragffi', 'bactiani', 'batiani', 'bathiani', 'montelini', 'monteleni', 'pereni', 'peregni', 'perenio',
         'thesorero', 'tesoriero', 'thesaurario', 'uaradino', 'uaradiensis', 'strigonio', 'agria', 'agriensis', 'hipolito',
         'cardinale', 'reuerendissimo', 'signore', 'episcopato', 'custode', 'gubernatore', 'lactantio', 'buda', 'debito',
         'danari', 'ducati', 'fiorini', 'castello', 'decime', 'capitolo', 'canonici', 'prepositura',
         'testamento', 'codicillo', 'bisogna', 'uiasecura', 'scritti', 'consuetudine', 'regno', 'quaranta', 'milia', 'deuoluta', 'legasset', 'eodemdie', 'signore', 'mandaro', 'portaro', 'excellentia', 'uostra', 'italia', 'ungaria', 'rauenna', 'ferrara', 'roma', 'papa', 'commissione', 'procura', 'scriuero', 'hauemo', 'tesoro', 'thesoro']
P = beam21.priors()
def cands(t):
    d = P.get(t, {})
    return {v for v, p in d.items() if p > -3.5}
for src, fn in [('R1136', 'r1136_pass4.txt'), ('R1139', 'r1139_pass4.txt')]:
    toks = []
    for line in open(os.path.join(HERE, fn), encoding='utf8'):
        if line.startswith(src + ' '):
            toks += [(line.split(':')[0].split()[1].rstrip('*'), t) for t in beam21.tokens(line) if t != '|']
    for w in CRIBS:
        for i in range(len(toks)):
            j = i; k = 0; hit = 0; used = []
            while k < len(w) and j < len(toks):
                lab, t = toks[j]; c = cands(t)
                if t == 'o' and w[k] not in c: j += 1; used.append('_'); continue   # lone o as null
                if any(v and w.startswith(v, k) for v in c):
                    v = max((v for v in c if v and w.startswith(v, k)), key=len); hit += len(v); k += len(v)
                else:
                    k += 1
                used.append(t); j += 1
            if hit >= 0.85 * len(w) and hit >= 5:
                print(src, toks[i][0], w, f'{hit}/{len(w)}', ' '.join(used))
