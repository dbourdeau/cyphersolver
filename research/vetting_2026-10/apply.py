"""Apply out_NN.json vetting blocks to research/leads.json; promote 'open' leads that pass the gate, close the rest.
   python research/vetting_2026-10/apply.py NN [NN ...]"""
import json, pathlib, subprocess, sys
R = pathlib.Path(__file__).resolve().parents[2]
LP = R / 'research' / 'leads.json'
for nn in sys.argv[1:]:
    out = json.loads((R / 'research/vetting_2026-10' / f'out_{nn}.json').read_text(encoding='utf-8'))
    d = json.loads(LP.read_text(encoding='utf-8'))
    byid = {str(l['id']): l for l in d['leads']}
    prom, closed, skipped = [], [], []
    for k, v in out.items():
        v = v.get('vetting', v) if isinstance(v, dict) else v
        l = byid.get(k)
        if not l: skipped.append(k); continue
        if 'unvetted' in v and 'verdict' not in v:
            l['vetting_note'] = v['unvetted']; skipped.append(k); continue
        if isinstance(v, dict) and 'lead_updates' in v:
            v = dict(v); l.update(v.pop('lead_updates'))
        l['vetting'] = v
        (prom if v.get('verdict') == 'open' else closed).append(int(k))
    LP.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    c = [sys.executable, str(R / 'docs/_check_catalogue.py')]
    if prom: subprocess.run(c + ['--promote'] + [str(i) for i in prom])
    print(f'batch {nn}: promote tried {len(prom)}, closed-verdict {len(closed)}, left as leads {len(skipped)}')
