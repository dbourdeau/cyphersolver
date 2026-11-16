"""Wave 12: split each CSP vol. 2 page (1522-24) into entries 'date. ref. NNN. Sender to X ...' and list those by the lead senders."""
import re, glob, os, json
H = os.path.dirname(os.path.abspath(__file__))
ents = []
for p in sorted(glob.glob(os.path.join(H, 'csp_pages', '*.txt'))):
    b = open(p, encoding='utf8').read()
    for m in re.finditer(r'(\d+ \w+\.?(?: \(\?\))?)\.? M\. Re\. Ac\. d\. Hist\. Salazar\. A\. (\d+)\. ff?\. ([\d,\- &and]+?)\. (\d{3,4})\. (.{0,260})', b):
        body_end = b.find(' M. Re. Ac.', m.end()); 
        ents.append(dict(node=os.path.basename(p)[:-4], date=m.group(1), vol=m.group(2), fol=m.group(3).strip(), no=m.group(4), head=m.group(5)[:200]))
json.dump(ents, open(os.path.join(H, 'csp_entries.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print(len(ents))
pat = {'Lannoy': r'Lannoy|Viceroy of Naples', 'Colonna': r'Colonna', 'Adorno': r'Adorno', 'Adrian': r'Adrian', 'Najera': r'Najera|Nagera'}
for k, rx in pat.items():
    print('==', k)
    for e in ents:
        if re.match(r'.{0,40}?(?:%s)' % rx, e['head']): print(e['node'], e['date'], 'A.%s f.%s' % (e['vol'], e['fol']), e['no'], e['head'][:90])
