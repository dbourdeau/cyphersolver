import re,collections,sys
txt=open('lm_qc/italian.txt',encoding='utf-8',errors='ignore').read().lower()
words=collections.Counter(re.findall('[a-z]{5,12}',txt)); common={w for w,c in words.most_common(6000)}
def cov(p):
    t=open(p,encoding='utf-8').read().split('--- decryption')[1].split(chr(10),1)[1].replace(chr(10),'').lower()
    i=0;k=0
    while i<len(t):
        for L in range(12,4,-1):
            if t[i:i+L] in common: k+=L;i+=L;break
        else: i+=1
    return k/len(t)
for f in sys.argv[1:]: print(f,round(cov(f),3))
