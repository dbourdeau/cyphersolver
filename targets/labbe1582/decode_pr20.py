"""Check of PR #20 (AngusRobinson): decode every token line of KEY_AND_DECRYPTION.txt with the stated key,
compare the token streams with the project's earlier independent draft (runs_dots.txt, 23 Sept 2026),
measure the fraction read, and run a shuffled-key control with the shared French LM.

    PYTHONUTF8=1 python targets/labbe1582/decode_pr20.py      (from the repository root)
Writes reading_pr20.txt next to this file.
"""
import re, sys, random, difflib, statistics, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from lang import lm

KEY = {'02': 'a', '04': 'a', '08': 'b', '01': 'c', '03': 'd', '1': 'e', '11': 'e', '21': 'f', '31': 'g', '09': 'h',
       '3': 'i', '13': 'i', '23': 'l', '33': 'm', '43': 'n', '5': 'o', '15': 'o', '25': 'p', '07': 'q', '35': 'r',
       '45': 's', '55': 't', '9': 'u', '19': 'u', '8': 'x', '18': 'x', '29': 'z', '6': ' '}

L = (HERE / 'KEY_AND_DECRYPTION.txt').read_text(encoding='utf-8').splitlines()
lines = [(L[j - 1], l, L[j + 1]) for j, l in enumerate(L) if '|' in l and re.match(r'^[\d\[]', l)]

out, tokens, unread, mism = [], 0, 0, 0
for lab, t, gloss in lines:
    toks = t.split('|')
    dec = ''
    for x in toks:
        h = x.count('[hidden]'); x = x.replace('+[hidden]', '').replace('[hidden]', '')
        tokens += 1 if x else 0; unread += h; tokens += h
        dec += (KEY.get(x, '?') if x else '') + ('?' * h)
    if dec.replace(' ', '').replace('?', '') != re.sub(r'\[[^\]]*\]', '', gloss.replace('[', '').replace(']', '')).replace(' ', '').replace('?', '') \
       and '?' not in dec:
        mism += 1; print('decode differs from gloss:', lab, dec, '|', gloss)
    out.append(f'{lab}\t{t}\t{dec}\t{gloss}')
(HERE / 'reading_pr20.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(f'lines {len(lines)}  cipher tokens {tokens}  obscured {unread}  read {tokens-unread} '
      f'({(tokens-unread)/tokens:.1%})  decode/gloss mismatches {mism}')

prs = [re.sub(r'\D', '', t.replace('[hidden]', '')) for _, t, _ in lines]
ours = [re.sub(r'\D', '', l) for l in (HERE / 'runs_dots.txt').read_text().split('\n') if l.strip()]
tot = same = 0
for a in prs:
    b = max(ours, key=lambda o: difflib.SequenceMatcher(None, a, o).ratio())
    tot += len(a); same += sum(m.size for m in difflib.SequenceMatcher(None, a, b).get_matching_blocks())
print(f'digits agreeing with the 23 Sept draft: {same}/{tot} = {same/tot:.1%}')

M = lm.load('fr-1530-despatches')
seqs = [[x for x in t.replace('+[hidden]', '').split('|') if x.isdigit()] for _, t, _ in lines]
dec = lambda k: ' '.join(''.join(k.get(x, '') for x in s) for s in seqs)
score = lambda s: M.per_char(lm.norm(s, 'early', True))
true = score(dec(KEY))
codes = [c for c in KEY if c != '6']; letters = [KEY[c] for c in codes]; rs = []
for r in range(1000):
    random.seed(r); l = letters[:]; random.shuffle(l); k = dict(zip(codes, l)); k['6'] = ' '; rs.append(score(dec(k)))
mu, sd = statistics.mean(rs), statistics.stdev(rs)
print(f'LM per char: key {true:.3f}; 1000 shuffled keys mean {mu:.3f} sd {sd:.3f} best {max(rs):.3f}; z = {(true-mu)/sd:.1f}')
