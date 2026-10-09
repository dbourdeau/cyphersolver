import collections, json
votes = collections.defaultdict(collections.Counter); bad = []
for line in open('align1889.txt', encoding='utf8'):
    if line.startswith('#') or '|' not in line: continue
    c, p = line.split('|'); c = c.split(); p = p.strip().replace('?', '')
    if len(c) != len(p): bad.append((c, p)); continue
    for t, ch in zip(c, p): votes[t][ch] += 1
key = {t: v.most_common() for t, v in votes.items()}
inv = collections.defaultdict(list)
for t, v in sorted(key.items(), key=lambda x: x[1][0][0]):
    inv[v[0][0]].append(t)
for t in sorted(key, key=lambda x: (x.isalpha(), x.zfill(3))): print(t, key[t])
print('---- by letter'); [print(k, inv[k]) for k in sorted(inv)]
print('---- length mismatches'); [print(b) for b in bad]
json.dump({t: v[0][0] for t, v in key.items()}, open('key1889.json', 'w'), indent=0)
