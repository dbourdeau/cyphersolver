"""merge one proposal (JSON file argv[2]) into proposals.json under id argv[1]"""
import json, sys, pathlib
P = pathlib.Path(__file__).with_name('proposals.json')
d = json.loads(P.read_text(encoding='utf-8')) if P.exists() else {}
v = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding='utf-8'))
if 'vetting' in v:
    v['vetting'].setdefault('date', '2026-11-16')
    v['vetting'].setdefault('by', 'claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting')
d[sys.argv[1]] = v
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('ok', sys.argv[1], v.get('verdict'))
