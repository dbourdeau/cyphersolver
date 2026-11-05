"""Append validated rows to candidates.json (same schema as research/archive_sweep_2026-10/BRIEF.md).
Usage from another script:  from cand import add;  add({...})   (dedupes on shelfmark; checks vocab used by merge.py)"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, 'candidates.json')
REQUIRED = ['year','date','title','correspondents','place','language','region','period','shelfmark','folio_note','cls','status','why',
            'importance','solvability','difficulty','score_note','verify','links','seen','source','prior_art','needs_archive_scan','access_note']
REGIONS = {'England','France','Italy','Spain','Portugal','Low Countries','Central Europe','Germany','Scandinavia','Poland-Lithuania','Papacy','Americas','Other'}
PERIODS = {'15th century','1497-1559','1560-1589','1589-1598','1598-1610','1611-1650','1651-1700','1701-1800','1801-1900','1901-1950','unknown'}
def norm(s): return re.sub(r'[^a-z0-9]+',' ',(s or '').lower()).strip()
def period(y):
    return ('15th century' if y<1497 else '1497-1559' if y<1560 else '1560-1589' if y<1589 else '1589-1598' if y<1598 else
            '1598-1610' if y<1611 else '1611-1650' if y<1651 else '1651-1700' if y<1701 else '1701-1800' if y<1801 else
            '1801-1900' if y<1901 else '1901-1950')
def add(r):
    rows = json.load(open(PATH,encoding='utf-8')) if os.path.exists(PATH) else []
    r.setdefault('period', period(r['year']))
    miss=[k for k in REQUIRED if k not in r]
    bad=[]
    if r.get('region') not in REGIONS: bad.append('region')
    if r.get('period') not in PERIODS: bad.append('period')
    if r.get('cls') not in ('A','B','C'): bad.append('cls')
    for k in ('importance','solvability','difficulty'):
        if not isinstance(r.get(k),int) or not 1<=r[k]<=5: bad.append(k)
    if r.get('needs_archive_scan') not in ('yes','no','partly','unknown'): bad.append('nas')
    if miss or bad:
        print('REJECT', r.get('title','')[:60], miss, bad); return False
    if any(norm(x['shelfmark'])==norm(r['shelfmark']) for x in rows):
        print('DUP', r['shelfmark']); return False
    rows.append(r)
    json.dump(rows, open(PATH,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
    print('added', len(rows), r['shelfmark'][:70]); return True
