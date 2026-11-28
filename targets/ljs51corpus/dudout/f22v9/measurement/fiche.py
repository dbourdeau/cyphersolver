# Fiche post-mesure (exploratoire) : statut de chaque lettre/mot du clair selon l'alignement complet.
import json, sys, collections
d = json.load(open(sys.argv[1], encoding='utf8')); C = d['counts']
words = [l.split('\t')[0] for l in open(sys.argv[2], encoding='utf8') if not l.startswith('#') and l.strip()]
words[0] = 'بني'
sk = {}
for g in ['بتثني', 'جحخ', 'دذ', 'رز', 'سش', 'صض', 'طظ', 'عغ', 'فق']:
    for ch in g: sk[ch] = g[0]
maj = {c: max(v.items(), key=lambda kv: (kv[1], kv[0]))[0] for c, v in C.items()}
byj = {r[3] - 1: r[1] for r in d['alignment'] if r[3] > 0}
j = 0; out = []; stat = collections.Counter()
for w in words:
    parts = []; worst = 0
    for ch in w:
        c = byj.get(j)
        if c is None: parts.append('[%s]' % ch); s = 2
        elif sum(C[c].values()) < 2: parts.append('{%s}' % ch); s = 1   # classe vue une seule fois : non contrôlable
        elif maj[c] == ch: parts.append(ch); s = 0
        elif sk.get(maj[c], maj[c]) == sk.get(ch, ch): parts.append('{%s}' % ch); s = 1
        else: parts.append('‹%s›' % ch); s = 3
        worst = max(worst, s); j += 1
    lab = ['sûr', 'probable', 'restitué', 'irrésolu'][worst]; stat[lab] += 1
    out.append('%-10s %-22s %s' % (w, ''.join(parts), lab))
print('\n'.join(out)); print(dict(stat), 'mots sûrs %d/21' % stat['sûr'])
