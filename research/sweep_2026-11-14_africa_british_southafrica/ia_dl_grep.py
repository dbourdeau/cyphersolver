"""Download OCR (djvu.txt) of selected archive.org ids into scratch, grep cipher contexts. python ia_dl_grep.py -> ocr_hits.jsonl"""
import json, re, os, subprocess, time
S = "/tmp/claude-0/-home-user-cyphersolver/06daecfa-9b30-5200-bb87-f4a44776c99f/scratchpad/british/ocr"
os.makedirs(S, exist_ok=True)
d = json.load(open("ids.json"))
sel = []
for k in ["theal_cape", "theal_se", "basuto", "moodie", "annals_natal", "cape_arch", "gold_coast", "sierra_leone", "zanzibar", "bechuana"]:
    for i, t, y in d[k]:
        if k == "sierra_leone" and not re.search(r"Correspondence|Class A|Accounts", t or ""): continue
        if k == "gold_coast" and not re.search(r"Correspondence|Papers|Ashanti|Fanti|War", t or ""): continue
        sel.append((k, i, t))
EXP = re.compile(r"Gordon.{0,40}(Kartoum|Khartoum)|source of the Nile|Emin Pasha|Emin's rescue|Oswell|Letters from Khartoum|Khartoum and the Blue|Uganda to Khartoum|Soudan War|Too Late for Gordon|Gordon At Khartoum|Lake Victoria To Khartoum|Imperial vanities|Davidson|Political and Secret Letters", re.I)
for k in ["explorers", "khartoum", "barbary"]:
    for i, t, y in d[k]:
        if EXP.search(t or ""): sel.append((k, i, t))
seen = set(); sel = [x for x in sel if not (x[1] in seen or seen.add(x[1]))]
print(len(sel), "ids", flush=True)
out = open("ocr_hits.jsonl", "a", encoding="utf8")
PAT = re.compile(r"\b(cipher|cypher|decipher|decypher|cyphered|ciphered|in code|secret writing|cryptogram|cryptograph)\w*", re.I)
for k, i, t in sel:
    f = os.path.join(S, i + ".txt")
    if not os.path.exists(f):
        subprocess.run(["curl", "-s", "-L", "-m", "180", "-A", "Mozilla/5.0", "-o", f, f"https://archive.org/download/{i}/{i}_djvu.txt"])
        time.sleep(2.5)
    try: txt = open(f, encoding="utf8", errors="replace").read()
    except Exception: txt = ""
    if len(txt) < 5000: print("short/none", i, len(txt), flush=True); continue
    n = 0
    for m in PAT.finditer(txt):
        ctx = re.sub(r"\s+", " ", txt[max(0, m.start() - 300):m.end() + 300])
        out.write(json.dumps({"grp": k, "id": i, "title": t, "kw": m.group(0), "ctx": ctx}, ensure_ascii=False) + "\n"); n += 1
    print(k, i, (t or "")[:50], len(txt), n, flush=True)
