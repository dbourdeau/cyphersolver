import sys, os
sys.path.insert(0, r'C:\Users\dbour\cypher\research\pares_ags')
import sweep
HERE = os.path.dirname(os.path.abspath(__file__))
sweep.OUT = os.path.join(HERE, 'hits.jsonl'); sweep.PROGRESS = os.path.join(HERE, 'progress.json')
sweep.RAW = os.path.join(HERE, 'raw'); sweep.MAXREQ = int(os.environ.get('MAXREQ', '12'))
sweep.DELAY = 3
sys.stdout.reconfigure(encoding='utf-8')
term = sys.argv[1]; facet = sys.argv[2] if len(sys.argv) > 2 else None
try:
    print(sweep.run(term, int(os.environ.get('MAXPAGES', '30')), facet=facet), 'new')
except sweep.Blocked as e:
    print('stopped', e)
finally:
    for l in sweep.LOG: print(l)
