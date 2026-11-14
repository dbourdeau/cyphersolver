"""Rebuilds validation/val_L101.json (27 Oct 2026 held-out check on 101 right) and counts it.
The 27 Oct run was scripts/align_em.py with the key as hard anchors (env ANCH), 1 EM iteration, ratio 2.7,
on transcr/i101d.txt against clears/L101_clear_contemporary.txt (reconstructed 14 Nov 2026: the path is identical, 320/320).
Agreement = groups whose key value is non-empty and whose aligned clear substring equals one of the key's values.
usage (from system_a/):  python3 -I scripts/val_L101.py key_c01.json [validation/controls/key_shuf1.json ...]"""
import json,os,subprocess,sys
here=os.path.dirname(os.path.abspath(__file__))
def run(key):
    env=dict(os.environ,ANCH=key)
    subprocess.run([sys.executable,'-I',os.path.join(here,'align_em.py'),'clears/L101_clear_contemporary.txt','1,2.7','transcr/i101d.txt'],
                   env=env,check=True,capture_output=True)
    d=json.load(open('align_out.json')); os.replace('align_out.json','val_'+os.path.basename(key)); return d['path']
def count(path,key):
    K=json.load(open(key)); n=ok=0
    for t,s in path:
        vals=[v for v in K.get(t,[]) if v]
        if not vals: continue
        n+=1; ok+= s in vals
    return ok,n
for key in sys.argv[1:]:
    p=run(key); ok,n=count(p,key); print(f"{key}: {ok}/{n} = {ok/n:.3f}")
