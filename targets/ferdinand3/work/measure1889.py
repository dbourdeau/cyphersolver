import json
key = json.load(open('key1889.json'))
key['6'] = 'e'  # majority; 6 also m (see NOTES)
ok = tot = 0; words = okw = 0; dev = []
for l in open('align1889.txt', encoding='utf8'):
    if l.startswith('#') or '|' not in l: continue
    c, w = l.split('|'); c = c.split(); w = w.strip()
    dec = ''.join(key.get(t, '?') for t in c)
    words += 1; okw += dec == w
    if len(c) == len(w):
        for t, ch in zip(c, w):
            tot += 1; ok += key[t] == ch or (t == '6' and ch in 'em')
    else:
        tot += len(c)
    if dec != w: dev.append((w, dec, ' '.join(c)))
print('tokens', tot, 'agree', ok, round(100*ok/tot, 1), '% ; words', words, 'exact', okw)
for d in dev: print(d)
