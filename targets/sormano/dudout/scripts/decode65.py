"""Decode the no. 65 re-read sign file. Lasry's key + no. 66 values (null; looped Z = z, as in no. 63). D = DUCA code sign.
usage: python3 decode65.py no65_signs_reread.txt  -> prints tag, decoded line (clear text kept in [..], codes as <CODE>)"""
import sys, re
M = {'v':'a','u':'a','w':'a','3':'a','b':'b','c':'c','C':'cc','d':'d','e':'e','k':'e','g':'e','7':'e',
'f':'f','F':'f','S':'g','h':'h','y':'i','o':'i','p':'i','4':'i','L':'ll','9':'l','m':'m','n':'n',
'U':'o','1':'o','5':'o','6':'p','q':'q','r':'r','z':'s','s':'s','t':'t','T':'u','a':'u','Y':'u','H':'u',
'X':'x','Z':'z','!':'','P':'<PAPA>','W':'<W>','R':'<R>','I':'<I>','D':'<DUCA>','?':'?',' ':' '}
def dec(part):
    out=[]; j=0
    while j < len(part):
        ch=part[j]
        if ch=='(':
            k=part.index(')',j); opts=part[j+1:k].split('|')
            out.append(''.join(M.get(c,'<'+c+'>') for c in opts[0])); j=k+1; continue
        out.append(M.get(ch,'<'+ch+'>')); j+=1
    return ''.join(out)
def decode_line(sig):
    res=[]
    for part in re.split(r'(\[[^\]]*\])', sig):
        if part.startswith('['): res.append(part)
        else: res.append(dec(part))
    return ''.join(res)
if __name__=='__main__':
    for l in open(sys.argv[1],encoding='utf-8'):
        l=l.rstrip('\n')
        if not l or l.startswith('#'): continue
        tag,_,sig=l.partition('\t'); print(tag+'\t'+decode_line(sig))
