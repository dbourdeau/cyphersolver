"""Build key.tsv from the cipher/translation pairs of DLI.3.524.1.   python scripts/build_key.py"""
import sys
from keylib import ROOT, pairs_524, build

sys.stdout.reconfigure(encoding='utf-8', newline='\n')
pairs = pairs_524()
key, conf, cnt = build(pairs)
lines = ['# group\tletter\tpairs (from DLI.3.524.1 cipher + contemporary translation; rows tagged ! not used)']
for g in sorted(key):
    lines.append(f'{g}\t{key[g]}\t{sum(cnt[g].values())}')
(ROOT / 'key.tsv').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f'{len(pairs)} pairs, {len(key)} groups; conflicts: {conf or "none"}')
by = {}
for g, v in key.items():
    by.setdefault(v, []).append(g)
for v in sorted(by):
    print(v, ' '.join(sorted(by[v])))
