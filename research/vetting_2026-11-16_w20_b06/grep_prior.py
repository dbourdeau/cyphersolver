import json, glob, os, sys
ids = set(sys.argv[1:])
for f in sorted(glob.glob('research/vetting_*/**/*.json', recursive=True)):
    b = os.path.basename(f)
    if b.startswith('in_'):
        continue
    try:
        d = json.load(open(f, encoding='utf8'))
    except Exception:
        continue
    if isinstance(d, dict):
        items = list(d.items())
        if 'leads' in d and isinstance(d['leads'], list):
            items = [(str(x.get('id')), x) for x in d['leads'] if isinstance(x, dict)]
    elif isinstance(d, list):
        items = [(str(x.get('id', x.get('lead_id'))), x) for x in d if isinstance(x, dict)]
    else:
        continue
    for k, v in items:
        if str(k) in ids:
            print(f, k, json.dumps(v, ensure_ascii=False)[:900])
            print()
