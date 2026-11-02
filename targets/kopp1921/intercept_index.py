"""Index the intercepts: for each frame, date headers, route, addresses, the numbers and signatures in clear, group kind and count."""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
MON = 'JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER'
SIGN = r'(KOPP|LUTOW\w*|LUTOV\w*|KARA[CK]H\w*|T[S]?CHI\w*CHERIN\w*|LITVIN\w*|KRESTIN\w*|KRASS?IN|VOIKOV|LEJAVA|LENIN|BRONSK\w*|ROZANOV\w*|WEINSTEIN|VAINSHTEIN)'
rows = []
for l in open('ocr_frames.jsonl', encoding='utf-8'):
    r = json.loads(l)
    t = r['text']
    if not re.search(r'FROM\s+\w+\s+(TO\s*)?\w+', t):
        continue
    date = re.search(rf'({MON})\s+(\d+)', t)
    route = re.search(r'FROM\s+(\w+)\s+TO\s*(\w+)', t)
    ends = re.findall(r'(\d{1,2}\s*(?:' + MON + r'|[A-Z]{3,9})\s*(?:19|I9)?\S*\s*(?:N[Rr]\S*\s*\S+)?)', t)
    rows.append({'frame': r['file'][5:-4], 'date': ' '.join(date.groups()) if date else '', 'route': ' > '.join(route.groups()) if route else '',
                 'signers': sorted(set(m.group(0)[:12] for m in re.finditer(SIGN, t))), 'numbers': re.findall(r'N[Rr]\s*[\dIl]+(?:/\w+)*', t)[:10], 'groups': len(r['tokens'])})
json.dump(rows, open('intercepts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(rows))
for x in rows:
    if any(s.startswith(('KOPP', 'LUTO', 'KARA')) for s in x['signers']):
        print(x['frame'], x['date'], x['route'], x['signers'], x['numbers'][:6], x['groups'])
