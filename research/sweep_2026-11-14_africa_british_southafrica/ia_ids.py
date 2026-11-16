"""Collect archive.org identifiers for Africa printed source collections. python ia_ids.py -> ids.json"""
import json, urllib.parse, urllib.request, time
Q = {
 "theal_cape": 'title:("records of the cape colony")',
 "theal_se": 'title:("records of south-eastern africa") OR title:("records of south eastern africa")',
 "hist_rec_sa": 'title:("historical records of south africa")',
 "basuto": 'title:("basutoland records")',
 "moodie": 'title:("record") AND creator:(moodie)',
 "annals_natal": 'title:("annals of natal")',
 "cape_arch": 'title:("cape archives") OR title:("archives of the cape of good hope") OR title:("kaapse argiefstukken") OR title:("reports on the" "cape archives")',
 "gold_coast": 'title:("gold coast") AND (title:(records) OR title:(correspondence) OR title:(documents) OR title:(papers))',
 "sierra_leone": 'title:("sierra leone") AND (title:(records) OR title:(documents) OR title:(papers) OR title:(correspondence))',
 "explorers": '(creator:(burton) OR creator:(speke) OR creator:(baker) OR creator:(stanley) OR creator:(livingstone) OR creator:(gordon) OR creator:(grant, james) OR creator:(emin)) AND (title:(journal) OR title:(journals) OR title:(letters) OR title:(diary) OR title:(diaries) OR title:(khartoum))',
 "khartoum": 'title:(khartoum) OR title:("journals at khartoum") OR title:("sudan" "papers") OR title:("egypt" "blue book")',
 "calendar_colonial": 'title:("calendar of state papers" "colonial")',
 "barbary": 'title:(barbary) OR title:(tangier) OR title:(morocco) AND (title:(papers) OR title:(records) OR title:(letters) OR title:(correspondence))',
 "zanzibar": 'title:(zanzibar) AND (title:(letters) OR title:(papers) OR title:(records))',
 "bechuana": 'title:(matabele) OR title:(rhodesia) OR title:(bechuanaland) AND (title:(records) OR title:(papers) OR title:(correspondence))',
}
out = {}
for k, q in Q.items():
    u = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode({"q": "(" + q + ") AND mediatype:texts", "fl[]": ["identifier", "title", "year"], "rows": 150, "output": "json"}, doseq=True)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=90))
        out[k] = [(x["identifier"], x.get("title"), x.get("year")) for x in d["response"]["docs"]]
    except Exception as e:
        out[k] = []; print(k, "ERR", e)
    print(k, len(out[k]), flush=True); time.sleep(2.5)
json.dump(out, open("ids.json", "w"), indent=1)
