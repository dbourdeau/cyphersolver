"""Print raw/audit.jsonl for review: each item with its regest, then every same-day / undated regest of its Konvolut and every
same-day Türkei I regest elsewhere, tagged DEC (a decipherment, clear copy, extract or translation is named), CIPH (cipher
only) or '' (no cipher word). Also flags folio cross-references to a decipherment inside the item's own regest (XREF).
Usage: python -I -X utf8 report.py [group]"""
import json, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
NODEC = re.compile(r'nincs\s+feloldv\w*|feloldás\s+nélkül|nincs\s+feloldás\w*|feloldatlan|feloldása\s+nincs|csak\s+sifrír|'
                   r'sifrír[ae]?n?\s+maradt|semmi\s+feloldás|mindenfajta\s+feloldás\s+nélkül', re.I)
DEC = re.compile(r'feloldv|feloldás|feloldott|megfejt|másolat|kivonat|fordítás|Auszug|Extract|dechiff|tisztázat|koncept', re.I)
CIPH = re.compile(r'sifr|titkosírás|chiffr', re.I)
XREF = re.compile(r'feloldás\w*\s+(?:a\s+)?(?:Kt|fol|hátrább|lásd|külön)|hátrább\s+feloldás\w*|feloldása\s+(?:Kt|fol)|pontosabban\s+feloldás', re.I)


def tag(d):
    rest = NODEC.sub('', d)
    if DEC.search(rest):
        return 'DEC'
    return 'CIPH' if CIPH.search(d) else ''


grp = sys.argv[1] if len(sys.argv) > 1 else None
for l in open(os.path.join(HERE, 'raw', 'audit.jsonl'), encoding='utf8'):
    r = json.loads(l)
    if grp and r['group'] != grp:
        continue
    it = r['item']
    x = ' XREF' if XREF.search(it['desc']) else ''
    print(f"== [{r['group']}] {it['id']} | {it['ref'][16:]} | {it['date']}{x}\n   {it['desc'][:600]}")
    for c in r['cands']:
        t = tag(c.get('desc', ''))
        if r['group'] not in ('1230',) or t == 'DEC':
            print(f"   {t:4} {c['how'][:9]:9} {c['id']} | {c['ref'][16:80]} | {c['date'][:40]} | {c.get('desc','')[:330]}")
