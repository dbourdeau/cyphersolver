"""Merge hits/*.jsonl, dedupe by id, keep pre-1951 records whose title points to cipher text that is
unread / foreign / intercepted / reproduced, write cands_raw.jsonl and a summary."""
import json, glob, re, collections
seen = {}
for fn in glob.glob("hits/*.jsonl"):
    for l in open(fn, encoding="utf8"):
        h = json.loads(l)
        e = seen.setdefault(h["id"], h)
        e.setdefault("_t", []).append(fn[5:-6])
print("unique records", len(seen))

def year(h):
    d = h.get("資料作成年月日", "")
    m = re.search(r"(明治|大正|昭和|平成)([０-９0-9]+)", d)
    if not m:
        return None
    n = int(m.group(2).translate(str.maketrans("０１２３４５６７８９", "0123456789")))
    return {"明治": 1867, "大正": 1911, "昭和": 1925, "平成": 1988}[m.group(1)] + n

KEEP = re.compile(r"解読|未解読|判読|不明|不能|傍受|謎|怪|密書|暗号文|暗号電報.{0,6}(写|訳|翻)|暗号(書|表|符号).{0,8}(入手|盗|押収|獲得|発見|提供)|外国暗号|露国暗号|米国暗号|英国暗号|支那暗号|清国暗号|独逸暗号|独国暗号|仏国暗号|蘇連暗号|ソ連暗号|革命党|諜報|密偵|間諜|スパイ|秘密結社|符牒|隠語|暗号 *電報.*(押収|検閲|差押)")
KNOWN = re.compile(r"^B030500(88|89|90)|B03050738800|B03050731500")
out = []
for h in seen.values():
    y = year(h)
    h["year"] = y
    if y and y > 1950:
        continue
    if KNOWN.search(h["ref"]):
        continue
    if KEEP.search(h["title"]):
        out.append(h)
print("kept", len(out))
yc = collections.Counter((h["year"] or 0)//10*10 for h in out)
print(sorted(yc.items()))
json.dump(out, open("cands_raw.json", "w", encoding="utf8"), ensure_ascii=False, indent=0)
