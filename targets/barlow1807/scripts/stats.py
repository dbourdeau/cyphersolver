import re,glob,collections,sys
for f in sorted(glob.glob('trans_raw/p*_A.txt')):
    t=open(f,encoding='utf8').read()
    nums=re.findall(r'\d+',t)
    c=collections.Counter(nums)
    print(f[10:13], len(nums), 'distinct',len(c), ' '.join(f'{k}:{v}' for k,v in c.most_common(14)))
