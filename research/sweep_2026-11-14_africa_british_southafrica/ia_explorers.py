"""Explorer books: collect ids by title phrases, download OCR to scratch, grep cipher contexts -> scratch/ocr/explorers_hits.jsonl, prints per-id counts."""
import json, re, os, subprocess, time, urllib.parse, urllib.request
S = "/tmp/claude-0/-home-user-cyphersolver/06daecfa-9b30-5200-bb87-f4a44776c99f/scratchpad/british/ocr"
T = ["missionary travels and researches in south africa","narrative of an expedition to the zambesi","last journals of david livingstone","how i found livingstone","through the dark continent","in darkest africa","coomassie and magdala","my dark companions","first footsteps in east africa","lake regions of central africa","zanzibar city island and coast","albert n'yanza","ismailia","the nile tributaries of abyssinia","journal of the discovery of the source of the nile","what led to the discovery of the source of the nile","walk across africa","life and letters of john hanning speke","emin pasha in central africa","through masai land","the life of sir richard burton","a thousand miles up the nile","fire and sword in the sudan","the river war","the mahdi and the soudan","khartoum campaign"]
ids = []
for t in T:
    q = 'title:("%s") AND mediatype:texts' % t
    u = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode({"q": q, "fl[]": ["identifier","title"], "rows": 6, "output": "json"}, doseq=True)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60))
        ids += [(x["identifier"], x["title"]) for x in d["response"]["docs"]]
    except Exception as e: print("ERR", t, e)
    time.sleep(2.5)
seen = set(); ids = [x for x in ids if not (x[0] in seen or seen.add(x[0]))]
print(len(ids), "ids", flush=True)
PAT = re.compile(r"\b(cipher|cypher|decipher|decypher|cyphered|ciphered|secret writing|cryptogram)\w*", re.I)
out = open(os.path.join(S, "explorers_hits.jsonl"), "w", encoding="utf8")
for i, t in ids:
    f = os.path.join(S, i + ".txt")
    if not os.path.exists(f):
        subprocess.run(["curl","-s","-L","-m","180","-A","Mozilla/5.0","-o",f,f"https://archive.org/download/{i}/{i}_djvu.txt"]); time.sleep(2.5)
    try: txt = open(f, encoding="utf8", errors="replace").read()
    except Exception: txt = ""
    if len(txt) < 5000: print("short/none", i, flush=True); continue
    n = 0
    for m in PAT.finditer(txt):
        out.write(json.dumps({"id": i, "title": t, "kw": m.group(0), "ctx": re.sub(r"\s+"," ",txt[max(0,m.start()-300):m.end()+300])}, ensure_ascii=False) + "\n"); n += 1
    print(i, (t or "")[:50], n, flush=True)
