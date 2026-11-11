# Construit KEY-W1717b (TRAIN S1 sans V=0057-0061, sans enclos A) et KEY-W1717c (TRAIN S1 complet sans enclos A)
# selon PROTOCOLE-AVENANT-2 §3. Procédure mécanique (align.py inchangé) + liste manuelle fermée.
import sys, os, glob, collections, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, align
D = lib.D
S1 = ['0017', '0057', '0058', '0059', '0060', '0061', '0062', '0071', '0072', '0080', '0081', '0086', '0087', '0088']
V = {'0057', '0058', '0059', '0060', '0061'}

def passages(scans):
    ps = []
    for s in scans:
        ps += lib.read_releve(os.path.join(lib.REL, f'T-{s}.txt'))
    return ps

MAN_B = {
 '77': ('ss', 'sur', '0071, 0072, 0081, 0087'), '99': ('ss', 'probable', '0081'), '103': ('les', 'probable', '0088'),
 '110': ('la', 'probable', '0081, 0086'), '119': ('tt', 'probable', '0087'), '150': ('[le roy]', 'probable', '0062'),
 '154': ('[votre excellence]', 'sur', '0088'), '177': ('[le czar]', 'sur', 'hors V'), '190': ('la', 'probable', '0071'),
 '193': ('le', 'probable', '0086'), '275': ("[l'empire]", 'probable', '0071, 0081, 0080'), '355': ('[premier]', 'probable', '0017'),
 '700': ('et', 'probable', '0086'), '377': ('[ministre]', 'inféré', 'enclos A « ministre » x4'),
 '168': ("[l'empereur]", 'inféré', 'enclos A « der Käyser » x2 (traduit)'),
 '5024': ('', 'inféré', 'nulle'), '5043': ('', 'probable', 'nulle'), '5046': ('', 'inféré', 'nulle'),
}
ONLY_V = {'13', '18', '78', '97', '102', '130', '170', '217', '252', '292'}

def mech(scans):
    align.train_passages = lambda: passages(scans)
    with contextlib.redirect_stdout(io.StringIO()):
        K, votes = align.build(n_iter=8)
    return votes

def key_from(votes, man, keep_aligner_100_120):
    out = {}
    for n, cnt in votes.items():
        cnt = collections.Counter(cnt); v, c1 = cnt.most_common(1)[0]; c = sum(cnt.values())
        if len(n) >= 3 or len(v) > 2: continue
        out[n] = (v, c, 'sur' if c1 >= 3 and c1 / c >= 0.6 else 'probable', 'aligneur : ' + str(dict(cnt.most_common(3))))
    for n, (v, s, j) in man.items():
        out[n] = (v, sum(votes.get(n, {}).values()), s, j)
    for n in ('100', '120'):
        if n in votes and keep_aligner_100_120:
            cnt = collections.Counter(votes[n]); v = cnt.most_common(1)[0][0]
            if v == 'd': out[n] = ('d', sum(cnt.values()), 'sur' if cnt['d'] >= 3 else 'probable', 'aligneur : ' + str(dict(cnt.most_common(3))))
    return out

def write(name, K, head):
    L = [head, '# nombre\tvaleur\toccurrences_alignées\tsûreté\tjustification']
    for n in sorted(K, key=int):
        v, c, s, j = K[n]; L.append(f'{n}\t{v}\t{c}\t{s}\t{j}')
    open(os.path.join(D, name), 'w').write('\n'.join(L) + '\n'); return len(K)

if __name__ == '__main__':
    vb = mech([s for s in S1 if s not in V])
    Kb = key_from(vb, MAN_B, True)
    print('b', write('KEY-W1717b.tsv', Kb, '# KEY-W1717b — S1, TRAIN sans V (0057-0061) ni enclos A (Avenant 2 §3). PRIVÉE (InC).'))
    vc = mech(S1)
    # c : procédure mécanique + toutes les entrées manuelles de KEY-W1717 + 377, 168
    man_c = dict(MAN_B)
    for line in open(os.path.join(D, 'KEY-W1717.tsv'), encoding='utf-8'):
        if line.startswith('#'): continue
        f = line.rstrip('\n').split('\t')
        if f[4].startswith('aligneur'): continue
        man_c[f[0]] = (f[1], f[3], 'KEY-W1717 : ' + f[4])
    Kc = key_from(vc, man_c, True)
    print('c', write('KEY-W1717c.tsv', Kc, '# KEY-W1717c — S1, TRAIN complet sans enclos A + manuel KEY-W1717 + 377/168 (Avenant 2 §3). PRIVÉE (InC).'))
