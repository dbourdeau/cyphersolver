"""python research/frame_check_2026-10/apply.py NN [NN ...]  — write out_NN.json results into catalogue.json as 'frame_check'."""
import datetime, json, pathlib, sys
R = pathlib.Path(__file__).resolve().parents[2]
CP = R / 'catalogue.json'
for nn in sys.argv[1:]:
    out = json.loads((R / 'research/frame_check_2026-10' / f'out_{nn}.json').read_text(encoding='utf-8'))
    d = json.loads(CP.read_text(encoding='utf-8'))
    by = {str(e['id']): e for e in d['entries']}
    n = 0
    for k, v in out.items():
        e = by.get(k)
        if not e or v.get('result') not in ('confirmed', 'no_cipher_at_frame', 'not_found', 'unreachable'): continue
        e['frame_check'] = dict(v, date=datetime.date.today().isoformat(), by=f'claude frame check {nn}')
        n += 1
    CP.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(nn, 'recorded', n, {r: sum(1 for v in out.values() if v.get('result') == r) for r in ('confirmed', 'no_cipher_at_frame', 'not_found', 'unreachable')})
