"""Fetch IIIF manifests for candidate uuids; write manifests.json (uuid -> canvases [label, image service])."""
import json, sys, os
from fetch import get
OUT = os.path.join(os.path.dirname(__file__), "manifests.json")
m = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
for u in sys.argv[1:]:
    if u in m: continue
    b = get(f"https://edl-jarvis.cultura.gov.it/meta/iiif/{u}/manifest")
    try: j = json.loads(b)
    except Exception: m[u] = {"error": b[:200]}; continue
    cv = []
    items = j.get("items") or [c for s in j.get("sequences", []) for c in s.get("canvases", [])]
    for c in items:
        lab = c.get("label"); lab = json.dumps(lab, ensure_ascii=False)[:40] if not isinstance(lab, str) else lab
        svc = ""
        try: svc = c["images"][0]["resource"]["service"]["@id"]
        except Exception:
            try:
                body = c["items"][0]["items"][0]["body"]; s = body.get("service"); s = s[0] if isinstance(s, list) else s
                svc = (s.get("@id") or s.get("id")) if s else body.get("id")
            except Exception: pass
        cv.append([lab, svc])
    m[u] = {"n": len(cv), "canvases": cv}
    json.dump(m, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(m))
