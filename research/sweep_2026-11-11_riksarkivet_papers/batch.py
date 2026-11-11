"""python batch.py <k> <refsubstr> ... : k-sample sheets for every resolved unit whose ref contains a substring; logs to sheets.log"""
import json, sys, subprocess, os
H = os.path.dirname(os.path.abspath(__file__))
k = sys.argv[1]; done = open(H + '/sheets.log').read() if os.path.exists(H + '/sheets.log') else ''
u = json.load(open(H + '/units.json', encoding='utf-8'))
for ref, v in sorted(u.items()):
    if any(s in ref for s in sys.argv[2:]) and v['man'] and v['n'] and (v['man'] + ' ') not in done:
        o = subprocess.run([sys.executable, H + '/rik.py', 'sheet', v['man'], k], capture_output=True, text=True).stdout
        open(H + '/sheets.log', 'a').write(f"{v['man']} {ref} n={v['n']} k={k}\n{o}")
