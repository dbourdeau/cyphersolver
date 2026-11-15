exec(open('nomtest.py').read().split("for s in [")[0])
V=['che','et','per','con','non','de','di','la','le','el','il','lo','in','se','ch','qu','pr','tr','st','ss','ll','nn','tt','re','ra','ri','ro','ne','na','no','ta','te','ti','to','sa','si','so','ma','me','mi','mo','da','do','co','ca','ce','ci','pe','pa','po','vo','va','ve']
for s in ['c','q','P','u','l','w','Q','D1','m','r','o','2','6']:
    res=[]
    for a in V:
        k=dict(k0);k[s]=a; tr,ho=cov(k,TR),cov(k,HO)
        res.append((tr[1]-b[0][1]+ho[1]-b[1][1],a,tr[1]-b[0][1],ho[1]-b[1][1]))
    res.sort(reverse=True); print(s,'now',k0.get(s),'|',res[:4])
