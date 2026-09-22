import sys
K={'2':'a','z':'a','8':'b','7':'c','X':'c','6':'d','t':'e','s':'e','p':'i','n':'l','o':'l','i9':'m','id':'n','l':'n','i7':'o','h':'Q','g':'r','i4':'r','i3':'s','f':'s','i2':'t','d':'u','y':'y','9':'a','J':'p','q':'y','r':'g','v':'d'}
def tok(r):
    out=[];j=0
    while j<len(r):
        if r[j]=='i' and j+1<len(r): out.append(r[j:j+2]);j+=2
        else: out.append(r[j]);j+=1
    return out
for l in open(sys.argv[1]):
    r=l.strip()
    if not r: continue
    t=tok(r)
    print(r.ljust(40),' '.join(t)); print(' '*40,' '.join(K.get(x,'['+x+']').ljust(len(x)) for x in t))
