"""TNA Discovery harvest, Africa slant. Usage: python harvest.py  (one request / 2.5 s). Writes raw.jsonl, harvest.log"""
import json, os, subprocess, time, urllib.parse
U = "https://discovery.nationalarchives.gov.uk/API/search/records"
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw.jsonl"); LOG = os.path.join(HERE, "harvest.log")
seen = {}
if os.path.exists(RAW):
    for l in open(RAW, encoding="utf8"):
        seen[json.loads(l)["id"]] = 1
out = open(RAW, "a", encoding="utf8"); log = open(LOG, "a", encoding="utf8")
KEEP = ["id","reference","title","description","coveringDates","numStartDate","numEndDate","department","heldBy","context","catalogueLevel","note"]
def q(**p):
    url = U + "?" + urllib.parse.urlencode(p)
    for i in range(4):
        r = subprocess.run(["curl", "-s", "-m", "60", url], capture_output=True)
        try: return json.loads(r.stdout.decode("utf8"))
        except Exception: time.sleep(4)
def run(term, dept=None, extra=None, maxpages=30):
    page = 1; tot = 0; new = 0; count = None
    while page <= maxpages:
        p = {"sps.searchQuery": term, "sps.dateFrom": "1500-01-01", "sps.dateTo": "1950-12-31",
             "sps.resultsPageSize": 100, "sps.page": page}
        if dept: p["sps.departments"] = dept
        if extra: p.update(extra)
        time.sleep(2.5)
        j = q(**p)
        if not j or not j.get("records"): break
        count = j.get("count")
        for r in j["records"]:
            tot += 1
            if r["id"] in seen: continue
            seen[r["id"]] = 1; new += 1
            d = {k: r.get(k) for k in KEEP}; d["term"] = term; d["dept_q"] = dept
            out.write(json.dumps(d, ensure_ascii=False) + "\n")
        out.flush()
        if len(j["records"]) < 100: break
        page += 1
    msg = f"{term!r} dept={dept} count={count} fetched={tot} new={new}"
    print(msg, flush=True); log.write(msg + "\n"); log.flush()
TERMS = ['cipher','cypher','"in cipher"','"in cypher"','decipher','decypher','deciphered','decyphered','undeciphered','undecyphered','enciphered','"cipher telegram"','"cypher telegram"','"in code"','"code telegram"','"secret writing"','cryptogram','"cipher key"','"cypher key"','"in secret characters"']
if __name__ == "__main__":
    import sys
    depts = sys.argv[1:] or ["CO","FO","WO","T","DO","CAB"]
    for d in depts:
        for t in TERMS: run(t, d)
