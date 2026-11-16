"""Merge one proposal file (JSON object keyed by lead id) into proposals.json. Usage: python -I -X utf8 add.py part.json"""
import json, sys, pathlib
here = pathlib.Path(__file__).resolve().parent
out = here / 'proposals.json'
d = json.loads(out.read_text(encoding='utf-8')) if out.exists() else {}
part = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
BY = "claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting"
for k, v in part.items():
    if 'vetting' in v:
        v['vetting'] = {'date': '2026-11-16', 'by': BY, **v['vetting']}
    d[k] = v
out.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('proposals:', len(d), sorted(d))
