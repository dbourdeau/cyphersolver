import sys, time, json
sys.stdout.reconfigure(encoding='utf-8')
from fts import run
Q = [
 # Dubrovnik / Ragusa
 '"lettera in cifra" Ragusa', '"in cifra" Ragusei', '"in cifra" "Lettere di Levante"', '"scritta in cifra" Ragusa senato',
 '"litterae in cifra" Ragusa', 'šifrom pismo Dubrovnik republika', '"pisma u šifri" Dubrovnik', 'šifrirano pismo Dubrovnik arhiv',
 '"cifra" "Monumenta Ragusina"', '"in cifra" Dubrovnik archivio lettere',
]
for q in Q:
    try:
        rows = run(q, 25, 1, show=False)
    except Exception as e:
        print('ERR', q, e); continue
    print('==', q, len(rows))
    for r in rows[:12]:
        print('  ', r['id'], '|', (r['title'] or '')[:55], '|', r['year'], '| p', r['page'])
    time.sleep(3)
