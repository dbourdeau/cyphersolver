"""compare_lectures_o5.py (PREREG-O5 §9, 25/11/2026) - accord entre les deux lecteurs par le sens L1 et L2.
usage : python3 -I compare_lectures_o5.py L1.json L2.json SORTIE.json   (JSON écrits par check_lecture_o5.py --json)
- kappa de Cohen à 5 classes (S, P, R, I, N=nulle) sur les caractères du décodage (chaque caractère prend la classe du
  mot qui le contient) ; kappa binaire lu (S/P/R) / non lu (I/N) ;
- accord de segmentation : F1 = 2 x (mots identiques) / (mots L1 + mots L2), un mot étant identique s'il couvre les mêmes
  caractères du décodage avec exactement les mêmes lettres (y compris les lettres données par le sens) ;
- accord de lecture : part des mots identiques qui ont aussi la même classe chez les deux lecteurs."""
import sys, json, collections
def kappa(a, b, labels):
    n = len(a); assert n == len(b) and n
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[l] * cb[l] for l in labels) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe), po
L1, L2 = (json.load(open(p, encoding='utf-8')) for p in sys.argv[1:3])
assert L1['decode_chars'] == L2['decode_chars'], 'les deux lectures ne portent pas sur le même décodage'
k5, po5 = kappa(L1['classes'], L2['classes'], 'SPRIN-')
bi = lambda s: ''.join('L' if c in 'SPR' else 'X' for c in s)
k2, po2 = kappa(bi(L1['classes']), bi(L2['classes']), 'LX')
w1 = {(s, e, w.lower(), w): c for s, e, w, c in L1['spans']}; w2 = {(s, e, w.lower(), w): c for s, e, w, c in L2['spans']}
same = set(w1) & set(w2); f1 = 2 * len(same) / (len(w1) + len(w2)) if (w1 or w2) else 0.0
samecls = sum(1 for k in same if w1[k] == w2[k]) / len(same) if same else 0.0
r = dict(kappa_5classes=round(k5, 4), agreement_5classes=round(po5, 4), kappa_read_unread=round(k2, 4),
         agreement_read_unread=round(po2, 4), segmentation_F1=round(f1, 4), identical_words=len(same),
         words_L1=len(w1), words_L2=len(w2), same_class_among_identical=round(samecls, 4))
json.dump(r, open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False); print(json.dumps(r, ensure_ascii=False))
