"""Pick the Waller records to page from the harvest (rdf_manuscript.jsonl): the whole Italian series before 1700 and the
political, princely and diplomatic letters of the other series (chosen by hand from names and descriptions)."""
import json, re, sys
S = sys.argv[1]
R = {}
for l in open(S + '/h/rdf_manuscript.jsonl'):
    r = json.loads(l); R[r['id']] = r
HAND = """23370 51773 47628 30209 30219 30254 46465 45361 24675 31311 31933 37853 37854 38414 36012 38014 34317 33478
28137 28139 28223 28542 28666 28681 28703 24702 25539 24631 31257 29591 20605""".split()
out = []
for r in R.values():
    sm = [n for n in r['num'] if n.startswith('Waller Ms ')]
    if not sm or not r['nimg']: continue
    m = re.search(r'(1[0-9]{3})', r['time'] or ''); y = int(m.group(1)) if m else None
    mm = re.match(r'Waller Ms ([a-z]+)', sm[0]); ser = mm.group(1) if mm else ''
    if (ser in ('it', 'espt', 'hu', 'pl') and y and y < 1700) or r['id'] in HAND:
        out.append({'id': r['id'], 'sm': sm[0], 'year': y, 'nimg': r['nimg'], 'take': list(range(1, min(r['nimg'], 8) + 1)),
                    'names': r['names'], 'title': r['title']})
out.sort(key=lambda o: o['sm'])
json.dump(out, open(S + '/list_waller.json', 'w'), ensure_ascii=False, indent=0)
print(len(out), sum(len(o['take']) for o in out), sum(o['nimg'] for o in out))
