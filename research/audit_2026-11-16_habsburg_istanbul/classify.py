"""First-pass classification of raw/audit.jsonl for review (the final verdicts in findings.json are set by hand from this).
Per item: XREF = its own regest points to a decipherment elsewhere; SAME = a regest of the same day (or a range including it),
same sender surname, naming a decipherment / clear copy / extract; OTHER = same-day regest naming a decipherment but not
matching the sender. Prints one compact block per item. Usage: python -I -X utf8 classify.py [group] > raw/classify_<group>.txt"""
import json, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
NODEC = re.compile(r'nincs\s+feloldv\w*|feloldás\s+nélkül|nincs\s+feloldás\w*|feloldatlan|feloldása\s+nincs|csak\s+sifrír|'
                   r'sifrír[ae]?n?\s+maradt|semmi\s+feloldás|mindenfajta\s+feloldás\s+nélkül|nem\s+feloldott', re.I)
DEC = re.compile(r'feloldv|feloldás|feloldott|desifr|dechiffr|megfejt|kivonat|másolat|fordítás|Auszug|Extract|tisztázat', re.I)
XREF = re.compile(r'feloldás\w*\s+(?:a\s+)?(?:Kt|fol|hátrább|lásd|külön)|hátrább\s+feloldás\w*|feloldása\s+(?:Kt|fol)|'
                  r'pontosabban\s+feloldás|feloldás\w*\s+\w+\s+fol|feloldás\w*\s+(?:a\s+)?\d', re.I)
NAMES = ['Starzer', 'Mollart', 'Katzensteiner', 'Lustrier', 'Radibrati', 'Schmid', 'Greiffenklau', 'Czernin', 'Kurtz',
         'Questenberg', 'Althan', 'Negroni', 'Gratiani', 'Mair', 'Dietz', 'Quarient', 'Kreckwitz', 'Pezzen', 'Eizing']


def names(d):
    return {n for n in NAMES if n.lower() in d.lower()}


grp = sys.argv[1] if len(sys.argv) > 1 else None
for l in open(os.path.join(HERE, 'raw', 'audit.jsonl'), encoding='utf8'):
    r = json.loads(l)
    if grp and r['group'] != grp:
        continue
    it = r['item']
    nm = names(it['desc'])
    flags, lines = [], []
    if XREF.search(it['desc']):
        flags.append('XREF')
    for c in r['cands']:
        d = c.get('desc', '')
        if not DEC.search(NODEC.sub('', d)):
            continue
        same_day = c['how'] != 'konv-undated'
        sender = bool(nm & names(d))
        kind = 'SAME' if (same_day and sender) else ('OTHER' if same_day else 'UNDATED')
        if kind == 'UNDATED' and not re.search(r'feloldás|feloldv|feloldott|desifr', d):
            continue
        flags.append(kind)
        lines.append(f"     {kind:7} {c['id']} | {c['ref'][16:75]} | {c['date'][:34]} | {d[:230]}")
    f = 'SAME' if 'SAME' in flags else ('XREF' if 'XREF' in flags else ('OTHER' if 'OTHER' in flags else ('UNDATED' if flags else 'NONE')))
    print(f"[{r['group']}] {it['id']} {f} | {it['ref'][16:80]} | {it['date'][:40]} | {it['desc'][:260]}")
    for x in lines:
        print(x)
