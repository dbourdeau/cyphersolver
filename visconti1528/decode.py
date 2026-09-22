import sys
K={'Y':'i','L':'c','X':'n','M':'l','S':'s','d':'e','D':'d','7':'a','Q':'q','z':'a','8':'g','F':'che','U':'[fu]',
   't':'[t]','a':'t','o':'p','k':'r','n':'o','y':'n','s':'u','l':'c','5':'v','q':'h','p':'m','r':'[r]','v':'[v]','b':'[b]','g':'[g]','f':'[f]','u':'[u]','m':'[m]','i':'[i]','rex':'[REX]'}
for l in open('cipher.txt',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k,*t=l.split()
    print(k,''.join(K.get(x,'?'+x) for x in t))
