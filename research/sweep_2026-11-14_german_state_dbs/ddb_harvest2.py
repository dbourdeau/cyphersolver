"""Archivportal-D (DDB Solr, sec_01 archives) harvest with terms not yet run, dated before 1920 or undated.
Writes raw2.jsonl (one record per id, with hitting terms). Polite: 1.2 s per request."""
import json, sys, time, urllib.parse, urllib.request
B = 'https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select'
TERMS = ['chiffriert','chiffrierte','chiffrierten','chiffrierter','chiffrieren','Chiffrierung','Chiffre','Chiffren','Chiffern','Chiffer','Cifer','Ciffer','Cyffer','Zyffer',
 'dechiffriert','dechiffrierte','dechiffrieren','Dechiffrierung','Dechiffrement','entziffert','entzifferte','Entzifferung','Entschlüsselung','entschlüsselt','Entschlüsselte',
 'Geheimschrift','geheimschriftlich','"geheime Schrift"','"geheimen Schrift"','"heimliche Schrift"','"heimlicher Schrift"','Geheimzeichen','Geheimalphabet','Geheimsprache','Geheimziffer','Geheimschlüssel',
 'Ziffernschrift','Zifferschrift','Zifferbrief','Ziffernbrief','"in Ziffern"','"mit Ziffern"','"in Zahlen"','Zahlenschrift','Zahlenchiffre','Zahlenschlüssel','Ziffernschlüssel','Ziffernalphabet',
 'Kryptographie','Kryptographik','Kryptogramm','Steganographie','Nomenklator','Nomenclator','Klarschrift','Chiffrenbuch','Chiffrenbrief','Chiffrenschlüssel','Chiffrierschlüssel','Chiffrenalphabet',
 'Dechiffrierschlüssel','Schlüsselbuch','"Schlüssel zur Geheimschrift"','"Schlüssel zu den Chiffren"','Kanzleischlüssel','Gesandtschaftsschlüssel',
 'verschlüsselt','verschlüsselte','Verschlüsselung','cifra','cifre','cifrato','cifris','"litterae cifratae"','"litteris occultis"','cypher','cipher','ziphra','Zipher','chiffre','chiffré','chiffrée','chiffrés','"en chiffres"','"en chiffre"','cyfra','cifras']
FQ = ['sector_fct:sec_01', '*:* -begin_time:[700000 TO *]']
def get(p):
    u = B + '?' + urllib.parse.urlencode(p, doseq=True)
    for i in range(4):
        try:
            with urllib.request.urlopen(u, timeout=60) as r: return json.load(r)
        except Exception as e:
            print('retry', e, file=sys.stderr); time.sleep(3*(i+1))
    raise RuntimeError(u)
recs, counts = {}, {}
for t in TERMS:
    s = 0
    while True:
        d = get({'q': t, 'rows': 500, 'start': s, 'wt': 'json', 'sort': 'id asc', 'fq': FQ})
        docs = d['response']['docs']; n = d['response']['numFound']
        for x in docs:
            for k in ('preview_store','context'): x.pop(k, None)
            if x['id'] in recs: recs[x['id']]['_t'].append(t)
            else: x['_t'] = [t]; recs[x['id']] = x
        s += 500; time.sleep(1.2)
        if s >= n or not docs: break
    counts[t] = n; print(t, n, len(recs), file=sys.stderr)
with open('raw2.jsonl', 'w', encoding='utf-8') as f:
    for r in recs.values(): f.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(counts, open('raw2_counts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
