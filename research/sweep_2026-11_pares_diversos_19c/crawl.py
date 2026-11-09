"""BFS over PARES catalogo/contiene children. Leaves (rows with 'Signatura:') go to leaves.json {id: text}; series to tree.json.
Usage: crawl.py <maxreq> <rootid> [<rootid> ...]   (state in tree.json/leaves.json; resumes; 4 s spacing; stops on 429)"""
import fetch,tempfile,os,re,html,sys,json
H=os.path.dirname(os.path.abspath(__file__))
TF,LF=os.path.join(H,'tree.json'),os.path.join(H,'leaves.json')
tree=json.load(open(TF,encoding='utf-8')) if os.path.exists(TF) else {}   # id -> {'t':title,'done':bool,'n':total}
leaves=json.load(open(LF,encoding='utf-8')) if os.path.exists(LF) else {}
maxreq=int(sys.argv[1]); roots=sys.argv[2:]
cnt=[0]
def parse(h):
    out={}
    for m in re.finditer(r'name="sel" value="(\d+)">(.*?)(?=name="sel" value=|</table>|$)',h,flags=re.S):
        t=html.unescape(re.sub(r'<[^>]+>',' ',m.group(2))); out[m.group(1)]=re.sub(r'\s+',' ',t)[:500]
    return out
def get(url,p,jar):
    cnt[0]+=1
    return fetch.curl(url,p,jar)
def children(sid):
    jar=tempfile.mktemp(); rows={}
    get(fetch.B+'catalogo/description/'+sid,os.path.join(fetch.SCR,'x.html'),jar)
    p=os.path.join(fetch.SCR,'cc_%s_1.html'%sid); get(fetch.B+'catalogo/contiene/'+sid,p,jar)
    h=open(p,encoding='utf-8',errors='replace').read(); rows.update(parse(h))
    tot=re.search(r'Todos los resultados \((\d+)\)',h); tot=int(tot.group(1)) if tot else len(rows)
    n=2
    while len(rows)<tot and n<80 and cnt[0]<maxreq:
        p=os.path.join(fetch.SCR,'cc_%s_%d.html'%(sid,n)); get(fetch.B+'catalogo/SearchController.do?d-2677838-p=%d'%n,p,jar)
        new=parse(open(p,encoding='utf-8',errors='replace').read())
        if not set(new)-set(rows): break
        rows.update(new); n+=1
    return rows,tot
def save():
    json.dump(tree,open(TF,'w',encoding='utf-8'),ensure_ascii=False); json.dump(leaves,open(LF,'w',encoding='utf-8'),ensure_ascii=False)
queue=list(roots)
for r in roots: tree.setdefault(r,{'t':'ROOT','done':False})
while queue and cnt[0]<maxreq:
    sid=queue.pop(0)
    if tree.get(sid,{}).get('done'):
        queue=[c for c in tree[sid].get('kids',[]) if not tree.get(c,{}).get('done') and c not in leaves]+queue; continue
    rows,tot=children(sid)
    if len(rows)<tot: print('partial',sid,len(rows),tot)
    kids=[]
    for k,t in rows.items():
        t=re.sub(r'<input.*','',t)
        if 'Signatura:' in t: leaves[k]=t
        else:
            tree.setdefault(k,{'t':t[:120],'done':False}); kids.append(k)
    tree[sid].update({'done':len(rows)>=tot,'n':tot,'kids':kids})
    queue=kids+queue if False else queue+kids
    print(sid,tree[sid].get('t','')[:50],'rows',len(rows),'leaves so far',len(leaves),'req',cnt[0],flush=True); save()
save(); print('stopped; queue',len(queue))
