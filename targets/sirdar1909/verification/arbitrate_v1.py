# Arbitrage mécanique fixé avant mesure : lettre retenue si A et B donnent la même lettre sûre ; sinon '?'.
import re, sys
def toks(s):
    out=[]
    for m in re.finditer(r'\[[^\]]*\]|[A-Za-z?]', s):
        t=m.group(0)
        if t.startswith('['):
            inner=t[1:-1]
            out.append(inner.lower() if re.fullmatch(r'[A-Za-z]', inner) and False else ('?' if not re.fullmatch(r'[A-Za-z]', inner) else inner.lower()))
        else: out.append(t.lower())
    return out
RUNS = [
 ("240-A", "uq[h/k][c/e]p outqt kxyzy qfyuw x?wde", "ughcp outqt kxyzy qfyu[w] x[k?]wde"),
 ("240-B", "ofkjos ykoeo fkjw[p/a] qkatj qkwxy cpeuq glxyk uovvv", "ofkjos ykoeo fkjw[p+a] [q/g]katj [q/g]kwxy cpeuq glxyk uovvv"),
 ("214", "[F/T]gmos zghko kzvjk [r/z]kvut oyxik omvyy rkbk[q/g] wwwku pkp[y/g]s wkbql og[i/s]dt sn[b/l]gm vyyxo okwry kx[t/l]x[v/u] ugsqs uowpk bbkqs wwkup xgvsu ovuqx okosz zvkju sgoku gkuak pgspk xghrn gmvxy usgbk qswwk upgsw kbqlg msoku gku[q/g]k pgspk xghog sdghk gmsok a[g/q]ku[g/q] kpgsp kxghm kbaxy osghx btkpm vghgn tbwnb p[k/h]bor",
         "Fgmos zghko kzvjk rkvut oyxik omvyy rkbkq wwwku pkpys wkbql og[i/s]dt snlgm vyyxo okwry kxtx[v/u] ugsqs uovpk bbkqs wwkup x[g/q]vsu ovu[q/g]x okosz zvkju sgoku gkuak [p]gspk xghrn gmvyy usgbk [q/g]swwk upgsw kbglg msoku gkugk p[g/y]spk xghog sdghk gmsok agkug kp[y/g]sp kxghm kb[a/o]xy osghx btkpm vghgn tbwnb pkbor"),
]
allt=[]; rep=[]
for name,a,b in RUNS:
    ta,tb=toks(a),toks(b)
    assert len(ta)==len(tb),(name,len(ta),len(tb))
    t=[x if (x==y and x!='?') else '?' for x,y in zip(ta,tb)]
    rep.append(f"{name}: {len(t)} signes, {t.count('?')} '?'")
    if allt: allt.append('|')
    allt+=t
open(sys.argv[1],'w').write(' '.join(allt)+'\n')
print('\n'.join(rep)); print('total signes (hors |):', sum(1 for x in allt if x!='|'))
