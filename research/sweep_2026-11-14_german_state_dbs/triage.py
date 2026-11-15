import json, re, glob, os, sys
ROOT = '../..'
recs = [json.loads(l) for l in open('raw2.jsonl', encoding='utf-8')]
print(len(recs), 'raw')
def norm(s): return re.sub(r'[\s.\-/,_]+|nr\.?', '', s.lower())
# known corpus: item ids + normalized text of ledgers
files = ['catalogue.json','research/leads.json','decode_updates/queue.json'] + glob.glob('research/**/candidates.json', recursive=True) + glob.glob('research/**/key_leads.json', recursive=True) + glob.glob('research/vetting*/*.json', recursive=True)
raw = ''
for f in files:
    p = os.path.join(ROOT, f)
    if os.path.exists(p): raw += open(p, encoding='utf-8', errors='replace').read() + '\n'
for f in glob.glob(ROOT + '/targets/*/NOTES.md'): raw += open(f, encoding='utf-8', errors='replace').read()
for f in glob.glob(ROOT + '/research/*/*.md'): raw += open(f, encoding='utf-8', errors='replace').read()
ids = set(re.findall(r'[A-Z0-9]{32}', raw))
nraw = norm(raw)
BAD_PROV = re.compile(r'Bundesarchiv|Stasi|Bundesbeauftragte', re.I)
CW = re.compile(r'chiffr|chiffer|cifer|cyffer|zyffer|ziffernschrift|zifferschrift|zifferbrief|ziffernbrief|in ziffern|mit ziffern|zahlenschrift|zahlenchiffre|geheimschrift|geheimzeichen|geheimalphabet|geheimziffer|geheimschl|heimliche[rn]? schrift|geheime[rn]? schrift|kryptogr|entziffer|entschl[üu]ssel|verschl[üu]ssel|nomenk?clator|klarschrift|dechiffr|cifra|cifre|cifris|ziphra|zipher|cypher|cipher|steganogr|schl[üu]ssel zu', re.I)
NOISE = re.compile(r'Namens?chiffre|Chiffre[- ]?Anzeige|basse chiffr|Schiffer|Dampfschiff|Zeitungsanzeige|Entzifferung (der|von) (Inschrift|Schrift|Hieroglyph|Keilschrift|Runen)|schwer zu entziffern|nicht zu entziffern|nicht entziffer|unleserlich|kaum zu entziffern|Schl[üu]ssel (zum|zur|zu den|für das|für die) (Zimmer|Haus|Kirche|Tor|Turm|Schrank|Archiv|Kasse|Sarg)|Geheimschlüsselzahl|Verschlüsselungsmaschine|Chiffriermaschine', re.I)
out = []
for r in recs:
    prov = ' '.join(r.get('provider', []))
    if BAD_PROV.search(prov): continue
    view = r.get('view', [])
    text = ' '.join(r.get('label', [])) + ' || ' + ' | '.join(view)
    if not CW.search(text): continue
    ref = ' '.join(r.get('apd_reference_number', []))
    sig = norm(ref)
    known = r['id'] in ids or (len(sig) >= 5 and sig in nraw)
    r['_text'] = text; r['_ref'] = ref; r['_prov'] = prov; r['_known'] = known; r['_noise'] = bool(NOISE.search(text))
    out.append(r)
print(len(out), 'cipher-word, non-Bundesarchiv;', sum(r['_known'] for r in out), 'known;', sum(r['_noise'] and not r['_known'] for r in out), 'noise-flagged unknown')
new = [r for r in out if not r['_known']]
json.dump([{ 'id': r['id'], 'prov': r['_prov'], 'ref': r['_ref'], 'text': r['_text'][:900], 't': r['_t'], 'noise': r['_noise'], 'begin': r.get('begin_time')} for r in new], open('new_unknown.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
from collections import Counter
print(Counter(r['_prov'] for r in new).most_common(25))
