# merge parts/<id>.json into proposals.json (incremental)
import json, glob, os
P = 'proposals.json'
out = json.load(open(P, encoding='utf8')) if os.path.exists(P) else {}
for f in sorted(glob.glob('parts/*.json')):
    out[os.path.basename(f)[:-5]] = json.load(open(f, encoding='utf8'))
json.dump(out, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(out), 'proposals:', ' '.join(f"{k}={v['verdict']}" for k, v in out.items()))
