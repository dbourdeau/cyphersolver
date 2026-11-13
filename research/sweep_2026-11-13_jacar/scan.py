"""Scan JACAR item descriptions (内容 = transcription of the document) for ciphertext-like digit-group runs.
usage: python -X utf8 scan.py refs.txt out.jsonl   (resumable; 4 threads)"""
import sys, json, re, time, jacar, concurrent.futures as cf
refs = open(sys.argv[1]).read().split(); out = sys.argv[2]
done = set()
try: done = {json.loads(l)["ref"] for l in open(out, encoding="utf8")}
except FileNotFoundError: pass
todo = [r for r in refs if r not in done]
Z = str.maketrans("０１２３４５６７８９", "0123456789")
def work(r):
    try:
        t = jacar.get(jacar.BASE + "/das/meta/" + r)
    except Exception as e:
        return {"ref": r, "err": str(e)}
    x = jacar.clean(re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)).translate(Z)
    m = re.search(r"内容 (.*?) URIをコピー", x); desc = m.group(1) if m else ""
    m = re.search(r"件名標題 (.*?) レファレンスコード", x); title = m.group(1) if m else ""
    m = re.search(r"資料作成年月日 (.*?) 規模", x); date = m.group(1) if m else ""
    m = re.search(r"規模 (\S+)", x); fr = m.group(1) if m else ""
    groups = re.findall(r"(?<!\d)\d{4,5}(?!\d)", desc)
    runs = re.findall(r"(?:(?<!\d)\d{4,5}(?!\d)[ ,、・]+){5,}", desc)
    return {"ref": r, "title": title, "date": date, "frames": fr, "n_groups": len(groups),
            "maxrun": max((len(re.findall(r"\d{4,5}", s)) for s in runs), default=0),
            "flag": bool(re.search(r"意味不明|解読不能|不明ノ暗号|判読不能|暗号ニテ|暗号ノ為|数字", desc)),
            "desc": desc[:1500]}
with open(out, "a", encoding="utf8") as f, cf.ThreadPoolExecutor(4) as ex:
    for i, d in enumerate(ex.map(work, todo)):
        f.write(json.dumps(d, ensure_ascii=False) + "\n"); f.flush()
        if i % 200 == 0: print(i, len(todo), flush=True)
