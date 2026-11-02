"""python research/vetting_2026-10/apply_legacy.py L01 [...]: write vetting blocks from out_L*.json onto legacy catalogue entries (id < 861).
A non-open verdict is NOT removed from the catalogue here: it is listed in research/vetting_2026-10/legacy_removals.json for the user to decide."""
import json, pathlib, sys
R = pathlib.Path(__file__).resolve().parents[2]
CP = R / 'catalogue.json'; RM = R / 'research/vetting_2026-10/legacy_removals.json'
rm = json.loads(RM.read_text(encoding='utf-8')) if RM.exists() else {}
for nn in sys.argv[1:]:
    out = json.loads((R / 'research/vetting_2026-10' / f'out_{nn}.json').read_text(encoding='utf-8'))
    d = json.loads(CP.read_text(encoding='utf-8')); by = {str(e['id']): e for e in d['entries']}
    ok = bad = 0
    for k, v in out.items():
        e = by.get(k)
        if not e or not isinstance(v, dict): continue
        v = v.get('vetting', v)
        if 'unvetted' in v and 'verdict' not in v: continue
        upd = v.pop('lead_updates', None)
        if upd:
            add = upd.pop('links_add', None)
            e.update(upd)
            if add: e.setdefault('links', []).extend(add if isinstance(add, list) else [{'label': 'item', 'href': add}])
        e['vetting'] = v
        ok += 1
        if v.get('verdict') != 'open':
            rm[k] = {'verdict': v.get('verdict'), 'closed': v.get('closed', ''), 'title': e.get('title', '')}; bad += 1
    CP.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    RM.write_text(json.dumps(rm, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(nn, 'vetted', ok, 'non-open (listed for removal)', bad)
