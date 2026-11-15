"""python rank.py <k per volume> : top-k pages per volume by strict/relaxed detector score (title pages 1-3 skipped)"""
import sys,glob,os,json
SP=os.environ['RIK_SP'];k=int(sys.argv[1])
U={u['man']:u for u in json.load(open('units.json'))}
out={}
for f in glob.glob(SP+'/scan/*.tsv'):
    man=os.path.basename(f)[:-4]
    rows=[tuple(int(v) for v in l.split('\t')) for l in open(f)]
    rows=[r for r in rows if r[0]>3 and r[1]>=0]
    rows.sort(key=lambda r:-(r[1]+r[3]))
    out[man]=[r[0] for r in rows[:k]]
    print(man,U[man]['ref'][-28:],len(rows),[(r[0],r[1],r[3]) for r in rows[:k]])
json.dump(out,open('top.json','w'))
