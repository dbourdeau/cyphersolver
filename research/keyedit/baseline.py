"""Baseline editor: greedy single-token letter swaps, most frequent tokens first, every trial costs one score()."""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
import keyedit
sess, = sys.argv[1:2]
s = keyedit.Session(sess)
ALPH = 'abcdefghilmnopqrstuxyz'
best = s.score()
cnt = s.task.counts
for tok, n in cnt.most_common():
    if tok.isdigit() and len(tok) == 3: continue
    cur = s.state['key'].get(tok, '')
    for a in sorted(set(ALPH) | set(s.state['start_key'].values()) - {''}):
        if a == cur: continue
        if s.state['spent'] >= s.state['budget']: break
        old = s.state['key'].get(tok, '')
        s.state['key'][tok] = a
        sc = s.score()
        if sc > best + 1e-6: best = sc; print('keep', tok, a, round(sc, 4))
        else: s.state['key'][tok] = old
    if s.state['spent'] >= s.state['budget']: break
s.save()
