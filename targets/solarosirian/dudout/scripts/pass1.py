# -*- coding: utf-8 -*-
"""C13 passe 1 (Claude, sous-agent) — codes de forme seulement, par unité (légende/colonne), ordre de lecture.
Notation 'CODE:conf' (h/m/b). Colonnes F : haut -> bas ; à l'intérieur d'une rangée, signe de droite d'abord
(signes tournés vers la droite). Légendes A-C : haut -> bas. D : groupes grossiers (résolution 15 px/signe)."""
import json, sys
U = {
# Zone A — Guilmant LXXXI, légendes des serpents
'A2': 'FLECHE:m V13:h CERCLE:m M17x2:m N29:m',
'A3': 'V6:m S28:h INSECTE:h PILET:m PILET:b FLECHE:h TROISPOINTS:m',
'A4': 'V6:m S28:h PILET:m INSECTE:h FLECHE:h TROISPOINTS:h',
'A5': 'V6:m S28:h INSECTE:m INCONNU:b PILET:b PILET:b FLECHE:h TROISPOINTS:h',
'A6': 'V6:m S28:h INSECTE:h PILET:b PILET:b FLECHE:m TROISPOINTS:h',
'A7': 'V6:m S28:h INSECTE:h PILET:m PILET:b FLECHE:h TROISPOINTS:m',
'A8': 'BLOB:m F34:m ONDE:h',
'A9': 'FLECHE:h ONDE:m BLOB:m',
# Zone B — Guilmant LXXXI, légendes 48-58
'B48': 'S28:m BARRE:m V13:h',
'B49': 'S28:b BARRE:m V13:h',
'B50': 'PILET:b M23x2:b V13:h',
'B51': 'Z1:m D21:h V13:h V13:h V13:h FLECHE:h INCONNU:b',
'B52': 'FLECHE:m BLOB:m FLECHE:h BLOB:m',
'B53': 'V13:m V13:m V13:m V13:m M17x2:m X1:m',
'B54': 'V30:b V30:b INCONNU:b V30:b V30:b INCONNU:b',
'B55': 'NAOS:b TIRETS:b M17x2:m X1:m BARRE:m',
'B56': 'Aa1:b INCONNU:b BLOB:m',
'B57': 'INCONNU:b N11:b G5:h V13:h',
'B58': 'Z11:m BARRE:m Z11:h BARRE:h TROISPOINTS:m',
# Zone C — Guilmant LXXX, légendes 15-21
'C15': 'V28:m Q3:m D4:h BARRE:m',
'C16': 'L1:h',
'C17': 'BLOB:b INCONNU:b',
'C18': 'S28:m INCONNU:b BARRE:m',
'C19': 'O1:m S28:m M23x2:b V13:m',
'C20': 'BARRE:m V13:m INCONNU:b',
'C21': 'INCONNU:b M23:b V13:m',
# Zone F — Guilmant LXXVI, colonnes 1-5
'F1': 'OBLNOIR:m M13:b A53:m BOUTON:m N35:h PILET:m TRAPEZE:h S28:m BARRE:h BOUTON:b N35:h LCOUCHE:h Z1:m LCOUCHE:h Z1:m ONDE:h PILET:m M23x2:m CERCLE:m BARRE:m V6:m V13:h INCONNU:b INSECTE:h ONDE:h D56:h D56:h ONDE:h Z4:h PILET:m BARRE:m V13:h V6:h PILET:b',
'F2': 'M23x2:h V13:h PILET:m N1:m L1:m PILET:m S28:m PILET:m V13:h INCONNU:b N35:h V13:h M23:m A40:m BOUTON:m N35:h LCOUCHE:m OISEAU:m BARRE:h PILET:h N29:m PILET:m PILET:m V13:h O1:m N35:h V13:h M23:m A40:m',
'F3': 'BOUTON:m N35:h M17:m PILET:m M17:m ONDE:h V30:m OISEAU:m BARREFOURCHE:m M17:m ONDE:h BARRE:h OBLNOIR:m A40:h BARRE:h A40:m V30:m OISEAU:m BARREFOURCHE:m M17:m ONDE:h INSECTE:m ONDE:h PILET:m OBLNOIR:h OBLNOIR:h OBLNOIR:h V13:h M17:m A40:m',
'F4': 'BOUTON:m N35:h TETE:b V13:h FIGBRAS:m V13:h O1:m PILET:m INCONNU:b INCONNU:b PILET:m Z4:b TROISPOINTS:m S28:h OISEAU:h OISEAU:h BARREFOURCHE:m TROISPOINTS:b M17:m PILET:m OBLNOIR:h O1:m BOUTON:b ONDE:h PILET:m S28:h PILET:m PILET:m D21:b Z4:m LCOUCHE:m ONDE:h',
'F5': 'M17:m PILET:m V6:h ONDE:h CERCLE:m ONDE:h PILET:m PILET:m S28:h PILET:m V13:h BARREFOURCHE:m TROISPOINTS:m CERCLE:m Z1:m LCOUCHE:m V30:m N29:m OISEAU:m V30:m O49:h A40:b INCONNU:b D21:h V13:m V6:m V30:m CERCLE:m INCONNU:b INCONNU:b N35:m Z1:m INCONNU:b V30:h',
# Zone D — Piankoff pl. II registre inférieur (gauche -> droite sur la planche ; groupes grossiers)
'D1a': 'PILET:b PILET:b PILET:b PILET:b',
'D1b': 'S28:b O1:b OIE:m',
'D1c': 'INCONNU:b O1:b',
'D1d': 'INCONNU:b BARRE:b',
'D1e': 'M23:b INCONNU:b',
'D1f': 'OIE:m INCONNU:b',
'D1g': 'CERCLE:b',
'D1h': 'INCONNU:b OIE:b',
'D1i': 'INCONNU:b INCONNU:b INCONNU:b',
'D1j': 'OIE:b INCONNU:b',
'D1k': 'S28:b',
'D2a': 'INCONNU:b S28:b O1:b',
'D2c': 'OIE:m O1:b',
'D2d': 'M23:b Z4:b BARRE:b',
'D2e': 'OIE:b INCONNU:b',
'D2f': 'OIE:b O1:b INCONNU:b',
'D2g': 'INCONNU:b INCONNU:b BARRE:b',
'D2h': 'INCONNU:b INCONNU:b BARRE:b',
'D2i': 'INCONNU:b BARRE:b INCONNU:b',
'D3a': 'S28:b M23:b',
'D3b': 'INCONNU:b M23:b INCONNU:b BARRE:b INCONNU:b INCONNU:b M23:b',
'D3c': 'S28:b INCONNU:b Z4:b INCONNU:b D21:b INCONNU:b',
'D3d': 'BARRE:b INCONNU:b M23:b INCONNU:b INCONNU:b',
'D3e': 'N14:m INCONNU:b M23:b N29:b N14:m INCONNU:b M23:b N29:b N14:m INCONNU:b M23:b N29:b',
'D3f': 'INCONNU:b INCONNU:b INCONNU:b INCONNU:b Z4:b O1:b INCONNU:b INCONNU:b INCONNU:b INCONNU:b',
'D4a': 'S28:b N14:m INCONNU:b N29:b S28:b N14:m INCONNU:b N29:b S28:b N14:m INCONNU:b N29:b',
'D4c': 'INCONNU:b INCONNU:b Z4:b M23:b S28:b OIE:b M23:b',
'D4d': 'INCONNU:b INCONNU:b INCONNU:b INCONNU:b',
'D4e': 'N29:b S34:m CERCLE:b INCONNU:b INCONNU:b',
'D4f': 'PILET:b PILET:b',
'D5': 'OIE:b INCONNU:b INCONNU:b N14:m CERCLE:b BARRE:b INCONNU:b M23:b OIE:b INCONNU:b N14:m CERCLE:b BARRE:b M23:b OIE:b INCONNU:b N14:m CERCLE:b OIE:b OIE:b INCONNU:b N14:m INCONNU:b',
'D6': 'OIE:b OIE:b INCONNU:b OIE:b INCONNU:b INCONNU:b M23:b INCONNU:b S28:b OIE:b INCONNU:b INCONNU:b OIE:b INCONNU:b INCONNU:b INCONNU:b OIE:b INCONNU:b',
}
signs = []
for u, s in U.items():
    for k, t in enumerate(s.split()):
        c, conf = t.split(':')
        signs.append({'id': f'{u}-{k+1:02d}', 'unit': u, 'zone': u[0], 'code': c, 'conf': conf})
out = sys.argv[1]
json.dump({'lecteur': 'Claude Opus 5.5 (sous-agent C13), passe 1', 'n': len(signs), 'signs': signs},
          open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
from collections import Counter
print(len(signs), Counter(s['zone'] for s in signs), Counter(s['conf'] for s in signs))
