"""Wave 12: date + sender cross-check of the narrowed leads 2867-2869 against CSP Spain vol. 3 (1525-29) full pages: the index folio can differ from Bergenroth's.
Entry layout in vol. 3: 'NNN. Sender to X. M. Re. Ac. d. Hist. Salazar, A. N, f. M.' then the body ending '-Place, D Mon. YYYY.'"""
import json, re, os, glob
H = os.path.dirname(os.path.abspath(__file__)); W = os.path.join(H, '..', 'sweep_2026-11-15_chrome_wave11')
M = json.load(open(os.path.join(W, 'match_result.json'), encoding='utf8'))
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ents = []
for p in sorted(glob.glob(os.path.join(H, 'csp3_pages', '*.txt'))):
    b = open(p, encoding='utf8').read()
    refs = list(re.finditer(r'Salazar\W{0,4}A\.\W{0,3}(\d+)\W{1,4}ff?\.\W{0,3}([\d\-–, &and]+)', b))
    for i, m in enumerate(refs):
        end = refs[i + 1].start() if i + 1 < len(refs) else len(b)
        head = b[max(0, m.start() - 230):m.start()]
        body = b[m.end():end]
        dl = re.search(r'[—-]\s*([A-Z][\w\.\- ]{2,30}),? (?:the )?(\d{1,2})(?:st|nd|rd|th)?(?: of)? ([A-Z][a-z]{2,8})\.?,? (15\d\d)', body)
        ents.append(dict(node=os.path.basename(p)[:-4], vol=m.group(1), fol=m.group(2).strip(), head=head[-170:], date=(dl.group(4), dl.group(3)[:3], int(dl.group(2))) if dl else None))
print(len(ents), sum(1 for e in ents if e['date']))
json.dump(ents, open(os.path.join(H, 'csp3_entries.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
SP = {'2867': r'Perez|Peres', '2868': r'Caracciolo|Prothonotary|Marino', '2869': r'Herrera'}
for lid in ('2867', '2868', '2869'):
    n = 0; tot = 0
    for r in M[lid]:
        if r[3] == 'CAL': continue
        tot += 1
        y, m, d = r[0].split('-'); key = (y, MON[int(m) - 1], int(d))
        hits = [e for e in ents if e['date'] == key and re.search(SP[lid], e['head'])]
        if hits:
            n += 1; print(lid, r[:3], '->', [(e['vol'], e['fol'], e['head'][-60:]) for e in hits])
    print(lid, 'date matches', n, 'of', tot)
