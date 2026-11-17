"""Wave 12: apply the date+sender cross-check against CSP Spain vol. 3 to catalogue entries 2867-2869.
A narrowed letter is dropped when the CSP prints a letter of the same sender and date with a folio within 10 of the index folio (same letter or its copy);
a same-date match with a distant folio is kept and named in the note. Entry 2869 ends with no letter and is moved back to leads.json as read."""
import json, re, os
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..'))
W = os.path.join(H, '..', 'sweep_2026-11-15_chrome_wave11')
M = json.load(open(os.path.join(W, 'match_result.json'), encoding='utf8')); ents = json.load(open(os.path.join(H, 'csp3_entries.json'), encoding='utf8'))
MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
SP = {'2867': r'Perez|Peres', '2868': r'Caracciolo|Prothonotary|Marino', '2869': r'Herrera'}
def lo_hi(s):
    n = [int(x) for x in re.findall(r'\d+', s)]
    return (n[0], n[-1]) if n else (0, 0)
def fmt(r): return '%s %s f.%s' % (r[0], r[1], r[2])
res = {}
for lid in ('2867', '2868', '2869'):
    keep, out, far = [], [], []
    for r in M[lid]:
        if r[3] == 'CAL': continue
        y, m, d = r[0].split('-'); key = [y, MON[int(m) - 1], int(d)]
        hits = [e for e in ents if e['date'] == key and re.search(SP[lid], e['head']) and e['vol'] == r[1][2:]]
        if not hits: keep.append(r); continue
        a, b = lo_hi(r[2]); near = [e for e in hits if min(abs(a - lo_hi(e['fol'])[1]), abs(b - lo_hi(e['fol'])[0]), abs(a - lo_hi(e['fol'])[0])) <= 10 or (lo_hi(e['fol'])[0] <= a <= lo_hi(e['fol'])[1])]
        if near: out.append((r, near[0]['fol']))
        else: keep.append(r); far.append((r, [e['fol'] for e in hits]))
    res[lid] = (keep, out, far)
    print(lid, 'keep', len(keep), 'out', len(out), 'far', [(fmt(r), f) for r, f in far])
json.dump({k: dict(keep=v[0], out=[(fmt(r), f) for r, f in v[1]], far=[(fmt(r), f) for r, f in v[2]]) for k, v in res.items()}, open(os.path.join(H, 'vol3_result.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
cp, lp = os.path.join(ROOT, 'catalogue.json'), os.path.join(ROOT, 'research', 'leads.json')
C = json.load(open(cp, encoding='utf8')); LL = json.load(open(lp, encoding='utf8'))
for e in list(C['entries']):
    k = str(e['id'])
    if k not in res: continue
    keep, out, far = res[k]
    outs = '; '.join('%s (CSP A.%s f.%s)' % (fmt(r), r[1][2:], f) for r, f in out)
    note = ("Wave 12 (15 Nov 2026) date check: the wave 11 match was by folio and missed CSP entries whose folio is printed with an en dash or a typo, or differs from the index. "
            "Matching CSP Spain vol. 3 by sender and date drops %d more letters (the CSP prints a letter of that sender and date within 10 folios; same letter or its copy; a calendar entry means the editor read it): %s." % (len(out), outs))
    if far: note += " Kept although the CSP has a same-date letter of that sender at a distant folio (possibly a second letter): %s." % '; '.join('%s vs CSP f.%s' % (fmt(r), ','.join(f)) for r, f in far)
    if keep:
        e['folio_note'] = e['folio_note'] + ' ' + note
        e['vetting']['seen']['extent'] = '%d letters (index records), RAH Salazar y Castro' % len(keep)
        e['vetting']['searches'].append(dict(query="CSP Spain vol. 3 (BHO nodes 74485-74700) full pages re-read; index letters matched by sender and date, not folio", result='%d dropped, %d kept (wave 12 vol3_result.json)' % (len(out), len(keep))))
        e['title'] = re.sub(r', \d+ (cipher letters|cipher letters)', ', %d cipher letters' % len(keep), e['title'], 1)
        e['folio_note'] = e['folio_note'] + ' Letters now left: ' + '; '.join(fmt(r) for r in keep) + '.'
    else:
        e['vetting']['verdict'] = 'read'
        e['vetting']['closed'] = ("decipherment_filed (wave 12 date match, 15 Nov 2026): " + note + " Nothing left open; the printed calendar entries show Bergenroth read these letters. Volumes not seen.")
        C['entries'].remove(e); LL['leads'].append(e)
LL['leads'].sort(key=lambda x: x['id'])
open(cp, 'w', encoding='utf8').write(json.dumps(C, ensure_ascii=False, indent=1)); open(lp, 'w', encoding='utf8').write(json.dumps(LL, ensure_ascii=False, indent=1))
