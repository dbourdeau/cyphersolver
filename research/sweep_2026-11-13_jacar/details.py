"""Fetch JACAR item pages (/das/meta/<ref>) -> details.jsonl: title, tree, dates, scale, 内容 (description)."""
import sys, json, re, time, jacar
refs = sys.argv[1:]
done = set()
try:
    done = {json.loads(l)["ref"] for l in open("details.jsonl", encoding="utf8")}
except FileNotFoundError:
    pass
with open("details.jsonl", "a", encoding="utf8") as f:
    for r in refs:
        if r in done:
            continue
        t = jacar.get(jacar.BASE + "/das/meta/" + r)
        x = jacar.clean(re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S))
        d = {"ref": r}
        m = re.search(r"件名標題 (.*?) レファレンスコード", x); d["title"] = m.group(1) if m else ""
        m = re.search(r"階層 (.*?) 印刷用ページ", x); d["tree"] = m.group(1) if m else ""
        m = re.search(r"請求番号 (.*?) 言語", x); d["callno"] = m.group(1) if m else ""
        m = re.search(r"資料作成年月日 (.*?) 規模", x); d["date"] = m.group(1) if m else ""
        m = re.search(r"規模 (\S+)", x); d["frames"] = m.group(1) if m else ""
        m = re.search(r"内容 (.*?) URIをコピー", x); d["desc"] = m.group(1) if m else ""
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
        print(r, d["date"], d["frames"], d["title"][:50], "|", d["desc"][:160], flush=True)
        time.sleep(0.7)
