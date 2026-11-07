"""Wiki lint: front matter, links, evidence rules, lexicon consistency, index freshness, orphans. Prints 'result: clean' or the problems."""
import os,re,sys,json
import wikilib as W
sys.stdout.reconfigure(encoding="utf8")
P=W.pages(); ids=set(P)
problems=[]
REQ={"source":["id","type","title","updated"],"entity":["id","type","title","updated"],"system":["id","type","title","updated"],
     "claim":["id","type","title","status","confidence","evidence","updated"],"question":["id","type","title","status","updated"],"test":["id","type","title","updated"]}
STAT={"established","supported","hypothesis","open","rejected"}
inbound={k:0 for k in ids}
for k,(fm,body,path) in P.items():
    if fm is None: problems.append("%s: no front matter"%k); continue
    for r in REQ.get(fm.get("type"),[]):
        if r not in fm: problems.append("%s: missing '%s'"%(k,r))
    if fm.get("id")!=k: problems.append("%s: id %s does not match file name"%(k,fm.get("id")))
    for m in re.finditer(r"\[\[([A-Z]\d+)\]\]",body):
        t=m.group(1)
        if t not in ids: problems.append("%s: link to missing page %s"%(k,t))
        else: inbound[t]+=1
    for field in ("evidence","depends","refuted_by"):
        for t in (fm.get(field) or []):
            if isinstance(fm.get(field),list):
                if t not in ids: problems.append("%s: %s refers to missing %s"%(k,field,t))
                else: inbound[t]+=1
    if fm.get("type")=="claim":
        s=fm.get("status")
        if s not in STAT: problems.append("%s: bad status %s"%(k,s))
        ev=fm.get("evidence") or []
        if s=="supported" and len(ev)<1: problems.append("%s: supported claim without evidence"%k)
        if s=="established" and len(ev)<2: problems.append("%s: established claim needs >= 2 evidence ids"%k)
        if s=="rejected" and not (fm.get("refuted_by") or ev): problems.append("%s: rejected claim without refuted_by"%k)
        try:
            c=float(fm.get("confidence"))
            if not 0<=c<=1: problems.append("%s: confidence out of range"%k)
        except Exception: problems.append("%s: confidence not a number"%k)
warnings=[]
for k,(fm,body,path) in P.items():
    if fm and fm.get("type")=="claim" and fm.get("status") in ("supported","established"):
        for d in (fm.get("depends") or []):
            if d in P and P[d][0]:
                ds=P[d][0].get("status")
                if ds=="rejected": problems.append("%s: %s depends on rejected claim %s (contradiction)"%(k,fm.get("status"),d))
                elif ds in ("hypothesis","open"): warnings.append("%s (%s) depends on %s claim %s: stale or premature"%(k,fm.get("status"),ds,d))
tests_cited=set()
for k,(fm,body,path) in P.items():
    if fm and fm.get("type")=="claim":
        for e in (fm.get("evidence") or []):
            if e.startswith("T"): tests_cited.add(k)
gaps=[k for k,(fm,b,p) in P.items() if fm and fm.get("type")=="claim" and fm.get("status") in ("hypothesis","open") and k not in tests_cited]
# lexicons
for code in ("inspectors","favre"):
    L=W.load_lex(code)["entries"]; seen={}
    for e in L:
        if e["status"] not in STAT: problems.append("lexicon_%s %s: bad status"%(code,e["group"]))
        if e["group"] in seen and seen[e["group"]]!=e["reading"]: problems.append("lexicon_%s: group %s has two readings"%(code,e["group"]))
        seen[e["group"]]=e["reading"]
        for c in e.get("claims",[]):
            if c not in ids: problems.append("lexicon_%s %s: claim %s missing"%(code,e["group"],c))
            else:
                cs=P[c][0].get("status")
                if e["status"] in ("supported","established") and cs in ("rejected",): problems.append("lexicon_%s %s: accepted entry cites rejected claim %s"%(code,e["group"],c))
# index freshness
idx=os.path.join(W.ROOT,"index.md")
if not os.path.exists(idx): problems.append("index.md missing")
else:
    t=open(idx,encoding="utf8").read()
    for k in ids:
        if "[[%s]]"%k not in t: problems.append("index.md does not list %s"%k)
orph=[k for k,n in inbound.items() if n==0 and P[k][0] and P[k][0].get("type") in ("claim","test","question","source","entity","system")]
# orphans are warnings only
if problems:
    print("PROBLEMS (%d):"%len(problems))
    for p in problems[:60]: print(" -",p)
    print("result: not clean")
else:
    print("pages %d, orphan pages (no inbound link, warning only): %d %s"%(len(ids),len(orph),orph[:12]))
    print("warnings (%d):"%len(warnings))
    for w in warnings[:15]: print("  -",w)
    print("data gaps: hypothesis/open claims with no test cited: %s"%gaps)
    qs=[k for k,(fm,b,p) in P.items() if fm and fm.get("type")=="question" and fm.get("status")=="open"]
    print("open questions that suggest the next sources or tests: %s"%qs)
    print("result: clean")
