"""Single-threaded JACAR item-page scan, one request per 2.5 s; stops on any 403/429/5xx. usage: scan1.py refs out.jsonl"""
import sys, json, re, time, urllib.request, urllib.error, os
sys.path.insert(0, "../jacar")
import jacar
refs = open(sys.argv[1]).read().split(); out = sys.argv[2]
done = set()
if os.path.exists(out):
    done = {json.loads(l)["ref"] for l in open(out, encoding="utf8")}
Z = str.maketrans("０１２３４５６７８９", "0123456789")
n = 0
with open(out, "a", encoding="utf8") as f:
    for r in refs:
        if r in done: continue
        try:
            req = urllib.request.Request(jacar.BASE + "/das/meta/" + r, headers=jacar.UA)
            t = urllib.request.urlopen(req, timeout=40).read().decode("utf8", "replace")
        except urllib.error.HTTPError as e:
            print("HTTP", e.code, r, flush=True); sys.exit(2 if e.code in (403, 429) else 3)
        except Exception as e:
            print("ERR", r, e, flush=True); time.sleep(10); continue
        x = jacar.clean(re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)).translate(Z)
        m = re.search(r"内容 (.*?) URIをコピー", x); desc = m.group(1) if m else ""
        m = re.search(r"件名標題 (.*?) レファレンスコード", x); title = m.group(1) if m else ""
        m = re.search(r"資料作成年月日 (.*?) 規模", x); date = m.group(1) if m else ""
        m = re.search(r"規模 (\S+)", x); fr = m.group(1) if m else ""
        groups = re.findall(r"(?<!\d)\d{4,5}(?!\d)", desc)
        runs = re.findall(r"(?:(?<!\d)\d{4,5}(?!\d)[ ,、・]+){5,}", desc)
        d = {"ref": r, "title": title, "date": date, "frames": fr, "n_groups": len(groups),
             "maxrun": max((len(re.findall(r"\d{4,5}", s)) for s in runs), default=0),
             "flag": bool(re.search(r"意味不明|解読不能|不明ノ暗号|判読不能|暗号ニテ|暗号ノ為|数字", desc)),
             "desc": desc[:1500]}
        f.write(json.dumps(d, ensure_ascii=False) + "\n"); f.flush()
        n += 1
        if n % 50 == 0: print(n, flush=True)
        time.sleep(2.5)
print("finished")
