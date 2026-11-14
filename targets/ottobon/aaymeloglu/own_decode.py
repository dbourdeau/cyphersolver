"""Own decoder (integration of issue #552, 14 Nov 2026), not the contributor's decode.py (which needs their cipherkit):
look up every group of transcription.json in this folder's own R1789 transcription (../keys/zifra_prima_R1789.tsv, made
independently on 9 Oct 2026) and compare with the contributor's key.json. Standard library only.  python3 own_decode.py"""
import collections, json, os
H = os.path.dirname(os.path.abspath(__file__))
rk = {}
for line in open(os.path.join(H, '..', 'keys', 'zifra_prima_R1789.tsv'), encoding='utf8'):
    if line.strip() and not line.startswith('#'):
        p = line.rstrip('\n').split('\t')
        rk[p[0]] = p[1] if len(p) > 1 else ''
ck = json.load(open(os.path.join(H, 'key.json'), encoding='utf8'))['mapping']
tr = json.load(open(os.path.join(H, 'transcription.json'), encoding='utf8'))
slots = unc = same = 0
missing, diff, tok = collections.Counter(), collections.Counter(), collections.Counter()
for f in tr['folios']:
    for r in f['rows']:
        for t in r['tokens'].split():
            slots += 1
            tok[t] += 1
            if '?' in t or t.startswith('{'):
                unc += 1
            elif t not in rk:
                missing[t] += 1
            elif rk[t].strip().lower() == str(ck.get(t, '')).strip().lower():
                same += 1
            else:
                diff[(t, rk[t], ck.get(t))] += 1
print('slots', slots, '| alternative or unread', unc, '| same value in both key transcriptions', same,
      '| not in R1789 here', sum(missing.values()), '| different spelling', sum(diff.values()))
for k, n in diff.most_common():
    print('  ', n, k)
print('d83', tok['d83'], 'c86', tok['c86'], 'd53', tok['d53'], 'h86', tok['h86'])
