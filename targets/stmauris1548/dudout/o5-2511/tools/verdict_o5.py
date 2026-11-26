"""verdict_o5.py (PREREG-O5 §10, 25/11/2026) - verdict unique d'O5, à partir des seuls fichiers gelés.
usage : python3 -I verdict_o5.py MESURE-O5.json L1.json L2.json ACCORD-L1L2.json
Critères (tous requis, fixés avant toute transcription de cc. 6v-8v) :
 C0 lettres décodées >= 300                         (sinon NON MESURABLE, pas FAIL)
 C1 part des mots lus par le sens >= 0,95           pour L1 ET pour L2   (lus = sûrs + probables + restitués)
 C2 part des mots restitués <= 0,05                 pour L1 ET pour L2
 C3 marge lexicale M - max(200 témoins) >= 0,30     (M lui-même : information, sans seuil absolu)
 C4 accord de segmentation L1/L2 (F1) >= 0,80
Les kappas sont rapportés pour information. La ligne VERDICT de measure_o4.py (seuil absolu 0,85 d'O2-O4) est ignorée."""
import sys, json
M = json.loads(open(sys.argv[1], encoding='utf-8').read().strip().split('\n')[-1])
L1, L2, A = (json.load(open(p, encoding='utf-8')) for p in sys.argv[2:5])
c = {}
c['C0 lettres >= 300'] = M['letters'] >= 300
c['C1 lus >= 0,95 (L1 %.4f, L2 %.4f)' % (L1['share_read'], L2['share_read'])] = L1['share_read'] >= 0.95 and L2['share_read'] >= 0.95
c['C2 restitués <= 0,05 (L1 %.4f, L2 %.4f)' % (L1['share_restored'], L2['share_restored'])] = L1['share_restored'] <= 0.05 and L2['share_restored'] <= 0.05
marge = M['M'] - M['ctrl_max']
c['C3 marge M - max témoins >= 0,30 (M %.4f, max %.4f, marge %.4f)' % (M['M'], M['ctrl_max'], marge)] = round(marge, 4) >= 0.30
c['C4 segmentation F1 >= 0,80 (%.4f)' % A['segmentation_F1']] = A['segmentation_F1'] >= 0.80
for k, v in c.items(): print('OUI' if v else 'NON', '-', k)
print('info : kappa 5 classes %.4f ; kappa lu/non lu %.4f ; z %.2f ; mots L1 %s ; mots L2 %s ; nulles L1 %.4f, L2 %.4f'
      % (A['kappa_5classes'], A['kappa_read_unread'], M['z'], L1['words'], L2['words'], L1['null_share'], L2['null_share']))
v = 'NON MESURABLE' if not c['C0 lettres >= 300'] else ('PASS' if all(c.values()) else 'FAIL')
print('VERDICT O5', v)
print(json.dumps(dict(verdict=v, criteria={k: bool(x) for k, x in c.items()}), ensure_ascii=False))
