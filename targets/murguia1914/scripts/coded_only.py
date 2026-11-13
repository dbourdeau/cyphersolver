"""Write the coded runs of a reading file as plain sentences (marks resolved to the reading value,
guesses kept as [?], so the checker counts them as holes). usage: coded_only.py READING_MD OUT_TXT"""
import sys, re
t = open(sys.argv[1], encoding='utf8').read().split('## Coded runs')[1]
out = []
for ln in t.splitlines():
    m = re.match(r'^[SFCM]\d\d \| (.*)$', ln)
    if not m: continue
    r = re.sub(r'\{[^/{}+]*/([^{}]*)\}', r'\1', m.group(1)); r = re.sub(r'\{\+([^{}]*)\}', r'\1', r)
    r = re.sub(r'\[\?[^\]]*\]', '[?]', r); out.append(r + '.')
open(sys.argv[2], 'w', encoding='utf8').write('\n'.join(out) + '\n')
