"""Which shortlisted records are already in the repo? Matches each shelfmark loosely (Nr. and punctuation ignored) against
catalogue.json, research/leads.json, SOLVED_CATALOGUE.md and targets/*/NOTES.md, and prints the hits and the new ones."""
import glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))


def norm(s):
    s = re.sub(r'\b(nr|no|bü|bue)\b\.?', ' ', s.lower())
    return re.sub(r'[^a-z0-9/]+', ' ', s).strip()


hay = {}
for name, path in [('catalogue', 'catalogue.json'), ('leads', 'research/leads.json'), ('solved', 'SOLVED_CATALOGUE.md')]:
    hay[name] = norm(open(os.path.join(ROOT, path), encoding='utf-8').read())
hay['targets'] = norm(' '.join(open(p, encoding='utf-8', errors='replace').read() for p in glob.glob(os.path.join(ROOT, 'targets', '*', 'NOTES.md'))))

SHORT = [
    # Arcinsys Hessen
    'HStAM 3 3054', 'HStAM 3 92', 'HStAM 3 276', 'HStAM 3 1450', 'HStAM 3 2550', 'HStAM 3 899', 'HStAM 3 1170', 'HStAM 3 2767', 'HStAM 3 2613',
    'HHStAW 170 III 29', 'HHStAW 170 III 30', 'HHStAW 170 III 1552', 'HHStAW 171 S 995', 'HHStAW 171 F 867', 'HHStAW 171 Z 1807',
    'HStAM 4 h 1411', 'HStAM 4 h 1815', 'HStAM 304 462', 'HStAM 115/01 1290', 'HStAM 1 2146', 'HStAM 4 h 632', 'HStAM 4 d 33',
    'HStAD D 4 113/9', 'HStAD D 4 115/5', 'HStAD D 4 245/1', 'HStAD D 4 248/3', 'HStAD D 4 343/1', 'HStAD D 4 343/3', 'HStAD D 4 409/1', 'HStAD D 4 487/4', 'HStAD D 4 487/6', 'HStAD D 4 130/13',
    'HStAD E 8 A 118/3', 'HStAD E 8 A 217/1', 'HStAD E 8 A 227/2', 'HStAD E 8 A 150/2', 'HStAD E 8 A 208/3', 'HStAD E 8 A 142/5', 'HStAD E 8 A 121/12', 'HStAD E 8 B 23/4', 'HStAD E 8 B 7/6', 'HStAD E 8 B 7/9', 'HStAD E 8 B 7/12', 'HStAD E 8 B 18/4',
    'HStAD E 1 M 54/1', 'KHA Inv. A 22 Nr. 51', 'KHA Inv. A 22 Nr. 191', 'KHA Inv. A 22 Nr. 195', 'KHA Inv. A 22 Nr. 197', 'KHA Inv. A 23 Nr. 203', 'KHA Inv. A 23 Nr. 223', 'KHA Inv. A 24 Nr. 8', 'KHA Inv. A 25 Nr. 347',
    # Arcinsys Niedersachsen
    'NLA WO 1 Alt 8 393', 'NLA WO 1 Alt 8 505', 'NLA WO 1 Alt 8 549', 'NLA WO 1 Alt 8 407', 'NLA WO 1 Alt 8 408', 'NLA ST Rep. 32 194', 'NLA ST Rep. 32 463', 'NLA HA Cal. Br. 15 3805', 'NLA WO 1 Alt 22 204a', 'NLA OS Rep 100 Abschnitt 1 43', 'NLA OS Rep 100 Abschnitt 256 4',
    'StadtA HI Best. 100 135 91', 'NLA HA Hann. 91 Ballati 23', 'NLA HA Hann. 91 Ballati 24', 'NLA HA Hann. 91 Ballati 5', 'NLA WO 1 Alt 3 27', 'NLA WO 1 Alt 22 786', 'NLA WO 2 Alt 560', 'NLA WO 2 Alt 3565', 'NLA WO 2 Alt 1598', 'NLA WO 2 Alt 3356',
    'NLA ST Rep. 5a 654', 'NLA ST Rep. 5a 670', 'NLA ST Rep. 5a 643', 'NLA ST Rep. 5a 642', 'NLA ST Rep. 5a 4049', 'NLA ST Rep. 5a 636', 'NLA ST Rep. 5a 379', 'NLA HA Hann. 92 2094', 'NLA HA Dep. 110 A 111', 'NLA HA Dep. 110 A 113', 'NLA HA Dep. 110 A 116', 'NLA HA Dep. 110 A 228', 'NLA HA Dep. 110 A 64', 'NLA HA Dep. 110 A 66', 'NLA HA Dep. 110 A 9',
    'NLA HA Hann. 9g 964', 'NLA HA Hann. 9g 1130', 'NLA HA Hann. 9g 1225', 'NLA HA Hann. 9g 1494', 'NLA HA Hann. 9g 1492', 'NLA HA Cal. Br. 24 5084',
    # Landesarchiv BW
    'A 2 Bü 10', 'A 2 Bü 11', 'J 1 Nr. 219', 'L 6 22', 'GLA 46 3889', 'GLA 50', 'E 50/05', 'A 74', 'FA N 12',
    # gda.bayern.de
    'Kurbayern Geheimer Rat 889', 'Hochstift Bamberg Archiv 892', 'Hochstift Bamberg 893', 'Pfalz-Neuburg Akten 793/II', 'Neuburger Abgabe 1989 6286', 'Pfalz-Neuburg Akten 1346', 'Pfalz-Neuburg Akten 1450/1',
    'Kasten blau 61/3', 'Kasten blau 61/25', 'Kasten blau 61/30', 'Kasten blau 61/32', 'Kasten blau 61/42', 'Kasten blau 59/3', 'Kasten blau 59/5', 'Kasten blau 62/1', 'Kasten blau 60/38', 'Kasten blau 196/8',
    'Grassegger 15280', 'GAB 4023', 'Gesandtschaft Wien 201', 'Gesandtschaft Wien 215', 'Gesandtschaft Wien 1703', 'Gesandtschaft Bern 59', 'Fechenbach 2189', 'Geistliche Sachen 1455', 'Ansbach Geheimes Archiv 99', 'Reichswesen 125', 'Schloss Birkenfeld Ortenburg 4509', 'Geheimer Rat 16091', 'MA 1 5 9', 'MA 16', 'MA 13',
]
new, seen = [], []
for s in SHORT:
    n = norm(s)
    where = [k for k, v in hay.items() if re.search(r'\b' + re.escape(n) + r'\b', v)]
    (seen if where else new).append((s, where))
print('IN REPO', len(seen))
for s, w in seen:
    print('  ', s, w)
print('NEW', len(new))
for s, _ in new:
    print('  ', s)
