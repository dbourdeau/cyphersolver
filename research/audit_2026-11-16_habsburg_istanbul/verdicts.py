"""Per-item verdicts for the multi-item catalogue entries 1226-1229, from raw/audit.jsonl, by rule (spot-checked by hand,
see README):
  filed     - the item's own regest points to its decipherment (XREF), or a same-day regest of the same sender AND the same
              recipient names a decipherment / clear copy / extract / copy (the cipher original and its clear text);
  probable  - the item names no recipient, and a same-day regest of the same sender names a decipherment / clear copy;
  parallel  - a same-day letter of the same sender to a different recipient is deciphered or clear (a crib, not the letter);
  none      - nothing of the kind found.
Writes raw/verdicts.json and prints a tally and the item lines. Usage: python -I -X utf8 verdicts.py"""
import json, re, os
from collections import Counter, defaultdict
import importlib.util, sys
_a = sys.argv; sys.argv = ['x']
_spec = importlib.util.spec_from_file_location('audit', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audit.py'))
AUD = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(AUD); sys.argv = _a
HERE = os.path.dirname(os.path.abspath(__file__))
NODEC = re.compile(r'nincs\s+feloldv\w*|feloldás\s+nélkül|nincs\s+feloldás\w*|feloldatlan|feloldása\s+nincs|csak\s+sifrír|'
                   r'sifrír[ae]?n?\s+maradt|semmi\s+feloldás|mindenfajta\s+feloldás\s+nélkül|nem\s+feloldott|egy\s+másik\s+feloldás\s+nélküli', re.I)
DEC = re.compile(r'feloldv|feloldás|feloldott|desifr|dechiffr|megfejt|kivonat|másolat|Extract|Auszug|tisztázat', re.I)
XREF = re.compile(r'hátrább\s+feloldás\w*|feloldása:?\s+(?:Kt|fol)|pontosabban\s+feloldás|feloldás\w*\s+(?:a\s+)?(?:Kt|fol)\.?\s*\d|'
                  r'feloldás\w*\s+\w+\s+fol\.?\s*\d|(?:feloldás|kivonat)\w*\s+lásd|lásd\s+fol|sorszéli\s+feoldás|sorszéli\s+feloldás', re.I)
SENDERS = ['Starzer', 'Gratiani', 'Lustrier', 'Radibrati', 'Schmid', 'Greiffenklau', 'Czernin', 'Kurtz', 'Questenberg',
           'Negroni', 'Dietz', 'Gallo', 'Mollart', 'Ferdinánd', 'Mátyás']
RECIP = {'Mollart': r'Moll?art', 'Zacharias': r'Zacharias', 'Katzensteiner': r'Katzenst', 'Mátyás': r'Mátyás|Matthias', 'Ferdinánd': r'Ferdinánd',
         'Hofkriegsrat': r'Hofkriegsrat|Haditanács', 'Maximilian': r'Miksa', 'Questenberg': r'Questenberg', 'Althan': r'Althan',
         'Mair': r'Mair', 'Greiffenklau': r'Greiffenklau', 'Czernin': r'Czernin', 'Schmid': r'Schmid', 'Collalto': r'Collalt'}


def parties(d):
    """(sender, recipients) from 'A – B (...)' regest text; recipients by keyword in the part after the dash."""
    head = d.split('(')[0]
    if '–' in head:
        a, b = head.split('–', 1)
    else:
        a, b = head, ''
    snd = {s for s in SENDERS if s.lower() in a.lower()}
    if not snd:
        snd = {s for s in SENDERS[:11] if s.lower() in d.lower()}
    rec = {k for k, p in RECIP.items() if re.search(p, b)}
    if 'Hofkriegsrat' in rec and 'Mollart' in rec:
        rec.discard('Hofkriegsrat')
    return snd, rec


out, tally = {}, defaultdict(Counter)
for l in open(os.path.join(HERE, 'raw', 'audit.jsonl'), encoding='utf8'):
    r = json.loads(l)
    if r['group'] not in ('1226', '1227', '1228', '1229'):
        continue
    it = r['item']
    snd, rec = parties(it['desc'])
    v, ev = 'none', []
    if XREF.search(it['desc']):
        v = 'filed'; ev.append(f"own regest: {XREF.search(it['desc']).group(0)}")
    for c in r['cands']:
        if c['how'] == 'konv-undated':
            continue
        d = c.get('desc', '')
        if not (AUD.days(c['date']) & AUD.days(it['date'])):
            continue
        if not DEC.search(NODEC.sub('', d)):
            continue
        cs, cr = parties(d)
        if not (snd & cs):
            continue
        if rec and cr and (rec & cr):
            k = 'filed'
        elif not rec:
            k = 'probable'
        else:
            k = 'parallel'
        ev.append(f"{c['id']} [{k}] {c['date'][:30]}: {d[:160]}")
        order = ['none', 'parallel', 'probable', 'filed']
        if order.index(k) > order.index(v):
            v = k
    out[it['id']] = {'group': r['group'], 'verdict': v, 'ref': it['ref'], 'date': it['date'], 'desc': it['desc'][:300],
                     'sender': sorted(snd), 'recipient': sorted(rec), 'evidence': ev}
    tally[r['group']][v] += 1
json.dump(out, open(os.path.join(HERE, 'raw', 'verdicts.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
for g in sorted(tally):
    print(g, dict(tally[g]))
for i, x in sorted(out.items(), key=lambda kv: (kv[1]['group'], kv[0])):
    print(f"[{x['group']}] {i} {x['verdict']:8} {x['date'][:28]:28} {','.join(x['sender'])}->{','.join(x['recipient'])} | {x['desc'][:110]}")
    for e in x['evidence'][:3]:
        print('        ', e[:230])
