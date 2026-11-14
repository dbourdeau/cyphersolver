"""Own check (14 Nov 2026), written for the integration of issue #554, not the contributor's apply_key.py:
apply key129.txt to f10_ct.txt and count how many cipher groups get a value. Standard library only.
    python3 apply_key129.py"""
import os, re
H = os.path.dirname(os.path.abspath(__file__))
key = {}
for line in open(os.path.join(H, 'key129.txt'), encoding='utf8'):
    m = re.match(r'^(\d+) (\S+)', line)
    if m:
        key[m.group(1)] = m.group(2)
groups = []
for line in open(os.path.join(H, 'f10_ct.txt'), encoding='utf8'):
    if line.startswith('#'):
        continue
    line = re.sub(r'\[[^\]]*\]', ' ', line)
    groups += [g.strip('?') for g in re.findall(r'\d+\??', line)]
hit = [g for g in groups if g in key]
print(len(groups), 'groups;', len(hit), 'with a value (%.1f%%)' % (100 * len(hit) / len(groups)))
print(' '.join(key.get(g, '.') for g in groups))
