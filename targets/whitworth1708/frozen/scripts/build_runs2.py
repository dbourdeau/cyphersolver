"""Turn a merged transcription into runs of code groups, and pair each run with the stretch of the printed
text (Sbornik vol. 50) that stands between the same clear words.
Usage: python3 -I build_runs.py <letter f112|f114> <merged.tsv> <adjudication.tsv> <sbornik english txt> <overrides.tsv or -> <out.json>
The pairing uses only the words written in clear in the manuscript and the printed words; no code value is used.
Overrides (one per line: run number, first printed word index, last printed word index + 1) fix boundaries by hand.
build_runs2.py = build_runs.py plus the override 'merge <run a> <run b>' (b = a + 1): the two runs become one, for a
clear word in the manuscript that the print does not have, so that nobody has to decide where it falls."""
import sys, re, json, difflib
letter, merged, adj, sb, ovr, out = sys.argv[1:7]
dec = {}
over = {}; drop = set(); merges = []      # overrides: 'drop <page> <line>' removes the clear words of that manuscript line (address, later note);
if ovr != '-':               # '<run> <first printed word index> <last index + 1>' sets a run's printed stretch by hand
    for line in open(ovr, encoding='utf-8'):
        if not line.strip() or line.startswith('#'): continue
        q = line.split('#')[0].split()
        if q[0] == 'drop': drop.add(q[1] + ' ' + q[2])
        elif q[0] == 'merge': merges.append((int(q[1]), int(q[2])))
        else: over[int(q[0])] = (int(q[1]), int(q[2]))
for line in open(adj, encoding='utf-8').read().splitlines()[1:]:
    p = line.split('\t')
    if p[0] == letter: dec[int(p[1])] = p[4]
items = []     # ('W', [words]) or ('G', [groups])
for line in open(merged, encoding='utf-8').read().splitlines()[1:]:
    idx, kind, status, a, b, ap, bp, aa, ba = (line.split('\t') + [''] * 9)[:9]
    idx = int(idx)
    if kind == 'W':
        if (ap or bp) in drop: continue
        words = a.split() if a != '-' else b.split()
        if items and items[-1][0] == 'W': items[-1][1].extend(words)
        else: items.append(['W', words, ap or bp])
        continue
    if status == 'agree': g = a
    else:
        d = dec.get(idx, 'OPEN'); g = None if d == 'OPEN' else d
    if items and items[-1][0] == 'G': items[-1][1].append(g)
    else: items.append(['G', [g], ap or bp])
def nw(w):
    w = re.sub(r'[^a-z0-9]', '', w.lower())
    w = re.sub(r'(.)\1', r'\1', w)
    for a, b in (('our', 'or'), ('y', 'i'), ('ck', 'k'), ('ph', 'f')): w = w.replace(a, b)
    return w.rstrip('e') or w
text = open(sb, encoding='utf-8').read()
text = re.sub(r'\[[^\]]*\]', ' ', text)
pw = re.findall(r"[A-Za-z0-9'’-]+", text)
msw = []; runpos = []            # clear words in order; for each run, the count of clear words before it
for it in items:
    if it[0] == 'W': msw.extend(it[1])
    else: runpos.append((len(msw), it))
sm = difflib.SequenceMatcher(None, [nw(w) for w in msw], [nw(w) for w in pw], autojunk=False)
m2p = {}
for a, b, n in sm.get_matching_blocks():
    for k in range(n): m2p[a + k] = b + k
runs = []
for k, (pos, it) in enumerate(runpos):
    left = pos - 1
    while left >= 0 and left not in m2p: left -= 1
    right = pos
    while right < len(msw) and right not in m2p: right += 1
    s = m2p[left] + 1 if left >= 0 else 0
    e = m2p[right] if right < len(msw) else len(pw)
    exact = (left == pos - 1) and (right == pos or right >= len(msw))
    if k in over: s, e = over[k]; exact = True
    runs.append(dict(run=k, place=it[2], groups=it[1], print_start=s, print_end=e, print_words=pw[s:e],
                     ms_left=msw[max(0, pos - 4):pos], ms_right=msw[pos:pos + 4],
                     print_left=pw[max(0, s - 4):s], print_right=pw[e:e + 4], boundaries_matched=exact))
for a, b in sorted(merges, reverse=True):
    ra, rb = runs[a], runs[b]
    s, e = min(ra['print_start'], rb['print_start']), max(ra['print_end'], rb['print_end'])
    ra.update(groups=ra['groups'] + rb['groups'], print_start=s, print_end=e, print_words=pw[s:e],
              ms_right=rb['ms_right'], print_right=rb['print_right'], boundaries_matched=True, merged_with=b)
    del runs[b]
json.dump(dict(letter=letter, runs=runs), open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for r in runs:
    flag = '' if r['boundaries_matched'] else '  <-- CHECK'
    print(f"{r['run']:3d} {r['place']:9s} k={len(r['groups']):3d} chars={len(re.sub('[^a-z0-9]','',''.join(r['print_words']).lower())):3d} print[{r['print_start']}:{r['print_end']}] | ms: {' '.join(r['ms_left'])} [..] {' '.join(r['ms_right'])}{flag}")
    print(f"      print: {' '.join(r['print_left'])} [[ {' '.join(r['print_words'])} ]] {' '.join(r['print_right'])}")
print('groups', sum(len(r['groups']) for r in runs), 'runs', len(runs))
