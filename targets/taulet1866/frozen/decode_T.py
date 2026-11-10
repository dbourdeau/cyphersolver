import sys
key = {}
for l in open(sys.argv[2], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    p = l.rstrip('\n').split('\t'); key[p[0]] = p[1]
part = sys.argv[3]
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    s, pt, nums = l.rstrip('\n').split('\t')
    if pt != part: continue
    print(s, ''.join(key.get(t.split('|')[0].rstrip('?'), '?') for t in nums.split('.')))
