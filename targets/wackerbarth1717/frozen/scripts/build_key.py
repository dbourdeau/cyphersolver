# Construit KEY-W1717.tsv (système S1) à partir de l'alignement TRAIN (align-train.tsv, sortie de align.py)
# + décisions manuelles documentées (nomenclateur, polygrammes, corrections d'alignement) — TRAIN seul.
import ast, collections
votes = {}
for line in open('align-train.tsv'):
    f = line.rstrip('\n').split('\t')
    votes[f[0]] = ast.literal_eval(f[2])
MAN = {  # nombre: (valeur, sûreté, justification)
 '77': ('ss', 'sur', "aggrandissement x2 (0072, 0081), Loss (0087), russes (0071) : ss ; l'aligneur préfère s (coût)"),
 '78': ('t', 'probable', "1 x « le » (0057, nombre corrigé 74>78), 1 x t (0087 suiet) : égalité → valeur la plus fréquente des paires (règle du protocole)"),
 '97': ('m', 'probable', "0057 sa [m]aieste ; 0059 « propriete 97 courlande » (la ?) : égalité → m (plus fréquent)"),
 '13': ('m', 'probable', "m 7 / c 4 (temoin, comme, mariage ×2, Mr… ; avec, sincerite, cour) : majorité m ; 13 et 15 peut-être confondus à la lecture"),
 '18': ('q', 'probable', "0057 « que » 18.6.2 sûr ; 0081 aligné r sans appui : q retenu (le r de l'aligneur tombe dans un passage mal glosé)"),
 '100': ('d', 'sur', "de/des/dans : 10+ cas"), '120': ('d', 'sur', "de/des/d' : 6+ cas"),
 '102': ('ss', 'probable', "princesse 0057"), '103': ('les', 'probable', "0088 « V.E. les desire »"),
 '110': ('la', 'probable', "la Cour d'Angl. (0060), et la princesse (0086), de la puiss. (0081)"),
 '119': ('tt', 'probable', "cette (0087)"), '130': ('et', 'probable', "et leur (0057)"),
 '190': ('la', 'probable', "la demeure (0071)"), '193': ('le', 'probable', "le Prince royal (0086)"),
 '700': ('et', 'probable', "cour icy et avec (0059), et la princesse (0086)"),
 '150': ('[le roy]', 'probable', "le Roy et le Czar (0062)"),
 '154': ('[votre excellence]', 'sur', "0058, 0088"),
 '170': ('[le roy]', 'probable', "le Roy notre maitre (0060, 0057) ; 0017 glose « C. de Werthern » (minorité)"),
 '177': ('[le czar]', 'sur', "8+ cas"),
 '217': ("[le roy d'angleterre]", 'sur', "0059 x2, 0060"),
 '252': ('[le roy de prusse]', 'probable', "0060"),
 '275': ("[l'empire]", 'probable', "0071, 0081"),
 '292': ('[la pologne]', 'probable', "0058, 0060"),
 '355': ('[premier]', 'probable', "Jean George premier (0017)"),
 '5043': ('', 'probable', "nulle : avant « mariage » épelé (0087)"),
 '5024': ('', 'inféré', "nulle : « de 5024 Czar » (0072)"), '5046': ('', 'inféré', "nulle : après Saphorin (0086)"),
 '99': ('ss', 'probable', "russienne (0081)"),
}
SKIP = {'5043', '5024', '5046'}
out = ['# KEY-W1717 — système S1 (Wackerbarth↔Flemming, mars–juin 1717), construite sur TRAIN seul (PROTOCOLE §2). PRIVÉE (InC).',
       '# nombre\tvaleur\toccurrences_alignées\tsûreté\tjustification']
nums = set(votes) | set(MAN)
for n in sorted(nums, key=int):
    if n in MAN:
        v, s, j = MAN[n]; c = sum(votes.get(n, {}).values())
    else:
        cnt = collections.Counter(votes[n]); v, c1 = cnt.most_common(1)[0]; c = sum(cnt.values())
        if len(n) >= 3 or len(v) > 2:  # 3 chiffres non tranchés à la main : pas de valeur
            continue
        s = 'sur' if c1 >= 3 and c1 / c >= 0.6 else 'probable'; j = 'aligneur : ' + str(dict(cnt.most_common(3)))
    out.append(f'{n}\t{v}\t{c}\t{s}\t{j}')
open('KEY-W1717.tsv', 'w').write('\n'.join(out) + '\n'); print(len(out) - 2, 'entrées')
