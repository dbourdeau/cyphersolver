import re
V='aeiouy'
def syll(word):
    w=word
    # tokens: treat ch, sch, ck, ph, th, qu, ei, ie, au, eu, ai as units
    units=re.findall(r'sch|ch|ck|ph|qu|ei|ie|au|eu|ai|ay|ey|[a-z]',w)
    isv=[any(c in V for c in u) and u not in('sch','ch','ck','ph','th','qu') for u in units]
    sy=[];cur=''
    i=0;n=len(units)
    vpos=[k for k in range(n) if isv[k]]
    if not vpos: return [w]
    # split points between consecutive vowel nuclei
    cuts=[]
    for a,b in zip(vpos,vpos[1:]):
        cons=b-a-1
        if cons<=1: cuts.append(a+1)       # V-CV
        else: cuts.append(b-1)             # VC..-CV (last consonant to next)
    out=[];start=0
    for c in cuts: out.append(''.join(units[start:c])); start=c
    out.append(''.join(units[start:]))
    return [s for s in out if s]
def tokens(text):
    from parse import norm
    toks=[]
    for w in text.split():
        w2=w.lower().replace('ä','a').replace('ö','o').replace('ü','u').replace('ß','ss')
        w2=re.sub('[^a-z]','',w2)
        if w2: toks+=syll(w2)
    return toks
if __name__=='__main__':
    import sys; sys.path.insert(0,'.')
    print(tokens('dieses enthalten dass man sich wohl vorzusehen hätte weil Jacobi zu promoviren'))
