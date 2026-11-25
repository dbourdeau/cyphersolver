# -*- coding: utf-8 -*-
"""C13 — arbitrage sur l'image des désaccords passe 1 (Claude) / passe 2 (Opus 5.5 API).
Règle PREREG : désaccord non tranché -> code de la passe 1 en attendant la planche de Brice (marqué 'planche').
Unités réécrites ici ; les autres = passe 1 inchangée. D = passe 1 (les deux passes à 'b', 15 px/signe)."""
import json, sys
p1 = json.load(open(sys.argv[1], encoding='utf-8'))['signs']
# code:conf[:P] (P = question de planche, code provisoire = passe 1)
NEW = {
 'A2': 'FLECHE:b:P V13:h CERCLE:m M17x2:m N29:m',
 'A3': 'V6:h S28:h INSECTE:h PILET:m FLECHE:h TROISPOINTS:m',
 'A5': 'V6:h S28:h INSECTE:m INCONNU:b PILET:m FLECHE:h TROISPOINTS:h',
 'A6': 'V6:h S28:h INSECTE:h PILET:m FLECHE:m TROISPOINTS:h',
 'A7': 'V6:h S28:h INSECTE:h PILET:m FLECHE:h TROISPOINTS:m',
 'A9': 'FLECHE:h BLOB:m ONDE:m',
 'B48': 'S28:h BARRE:m:P V13:h',
 'B51': 'Z1:b D21:h V13:h V13:h FLECHE:h INCONNU:b',
 'B54': 'BOLCORNES:m BOLCORNES:m INCONNU:b BOLCORNES:m BOLCORNES:m TETE:b',
 'B55': 'NAOS:m M17x2:m X1:m BARRE:m',
 'B56': 'Aa1:b:P INCONNU:b BLOB:m',
 'B57': 'INCONNU:b:P N11:b G5:h V13:h',
 'C15': 'LCOUCHE:m D4:h V6:m BARRE:m BLOB:b',
 'C18': 'S28:m INCONNU:b BARRE:b:P',
 'C19': 'O1:b:P S28:b:P M23x2:b:P V13:m',
 'C20': 'BARRE:m:P V13:m INCONNU:b',
 'F1': 'OBLNOIR:h A53:b:P M23:m BOUTON:m N35:h PILET:h S28:m TRAPEZE:h BARRE:m:P BOUTON:m N35:h LCOUCHE:h Z1:m LCOUCHE:h Z1:m ONDE:h PILET:h V6:h CERCLE:m BARRE:b M23x2:h V13:h INCONNU:b INSECTE:h ONDE:h D56:h D56:h ONDE:h Z4:m PILET:h BARRE:b V6:h V13:h PILET:h',
 'F2': 'M23x2:h V13:h PILET:h N1:m:P L1:m PILET:h S28:h PILET:h V13:h INCONNU:b BLOB:m N35:h V13:h M17:m A40:m BOUTON:m N35:h LCOUCHE:h OISEAU:m BARRE:m PILET:h N29:b:P PILET:h PILET:m V13:h O1:m N35:h V13:h M17:h A40:m',
 'F3': 'BOUTON:m N35:h PILET:h M17:h ONDE:h M17:h BOLCORNES:m OISEAU:m BARREFOURCHE:m ONDE:h M17:h BARRE:h OBLNOIR:h A40:h BARRE:h A40:m BOLCORNES:m OISEAU:m BARREFOURCHE:m ONDE:h M17:h PILET:m ONDE:h PILET:h OBLNOIR:h OBLNOIR:h OBLNOIR:h V13:h M17:h A40:m',
 'F4': 'BOUTON:m N35:h TETE:m V13:h FIGBRAS:h V13:h O1:m PILET:h INCONNU:m INCONNU:m PILET:h TROISPOINTS:h S28:h OISEAU:h OISEAU:h BARREFOURCHE:h TROISPOINTS:m M17:m PILET:h OBLNOIR:h O1:m BOUTON:m ONDE:h PILET:h S28:h PILET:h PILET:h D21:b LCOUCHE:h Z4:m ONDE:h',
 'F5': 'M17:h PILET:h V6:h ONDE:h CERCLE:h ONDE:h PILET:h PILET:h S28:h PILET:h V13:h BARREFOURCHE:h TROISPOINTS:m CERCLE:h Z1:m LCOUCHE:h V30:m N29:m OISEAU:m X1:b OISEAU:m O49:h INCONNU:b D21:h LCOUCHE:m V6:m V30:h CERCLE:m INCONNU:b INCONNU:b N35:m:P F34:b Z1:m V30:h',
}
out = []
for u in dict.fromkeys(s['unit'] for s in p1):
    if u in NEW:
        for k, t in enumerate(NEW[u].split()):
            parts = t.split(':')
            out.append({'id': f'{u}-{k+1:02d}', 'unit': u, 'zone': u[0], 'code': parts[0], 'conf': parts[1],
                        'planche': len(parts) > 2, 'source': 'arbitrage'})
    else:
        out += [dict(s, planche=False, source='passe 1' + (' (D : non arbitrable)' if u[0] == 'D' else ' = passe 2')) for s in p1 if s['unit'] == u]
json.dump({'doc': 'Transcription arbitrée C13 (gelée avant décodage). planche=true : code provisoire, question posée à Brice.',
           'n': len(out), 'signs': out}, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
from collections import Counter
print(len(out), Counter(s['zone'] for s in out), 'planche:', sum(s['planche'] for s in out))
