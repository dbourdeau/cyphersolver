import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
from solve import load_runs
mp=json.load(open(sys.argv[1])); runs=load_runs()
for i in [int(x) for x in sys.argv[2:]]:
    r=runs[i]; print(i, ' '.join(f'{s}={mp.get(s,"?")}' for s in r))
