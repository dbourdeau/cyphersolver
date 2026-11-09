import sys, os
sys.path.insert(0, r'C:\Users\dbour\cypher\.worktrees\sweep-nov9\research\pares_ags')
import sweep
HERE = os.path.dirname(os.path.abspath(__file__)); os.makedirs(os.path.join(HERE,"raw"),exist_ok=True)
sweep.OUT = os.path.join(HERE, 'hits.jsonl'); sweep.PROGRESS = os.path.join(HERE, 'progress.json')
sweep.RAW = os.path.join(HERE, 'raw'); sweep.MAXREQ = int(os.environ.get('MAXREQ', '400'))
sweep.DELAY = 4
sweep.STAMP = os.path.join(HERE,'stamp')
sys.stdout.reconfigure(encoding='utf-8')
# usage: run.py facet term1 term2 ...
facet = sys.argv[1]
for term in sys.argv[2:]:
    try:
        print(term, facet, sweep.run(term, int(os.environ.get('MAXPAGES', '30')), facet=facet), 'new', flush=True)
    except sweep.Blocked as e:
        print('stopped', e); break
for l in sweep.LOG[-3:]: print(l)
