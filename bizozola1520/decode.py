M={'+':'p','q':'e','J':'r','z':'l','e':'m','8':'i','3':'a','g':'t','c':'c','1':'d','o':'o','n':'n','f':'f','7':'b','w':'-','X':'<?>','Z':'z','b':'v','d':'s','6':'h','2':'g','Q':'q','t':'t','v':'u','5':'u','?':'?'}
import sys
for l in open('codes.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    k,_,c=l.strip().partition(' ')
    print(k,' '.join(''.join(M.get(ch,ch) for ch in w) for w in c.split()))
