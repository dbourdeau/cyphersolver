"""Petkum (unit 261267): save every image lo..hi not on the 1-in-4 grid at 1000 px wide to <out>/p<img>.jpg. usage: python3 pet.py <bsid> <out> <lo> <hi> [all]"""
import sys, os, time, ao
bsid, out, lo, hi = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); os.makedirs(out, exist_ok=True); ids = ao.refs(bsid)
for n in range(lo, min(hi, len(ids)) + 1):
    fn = os.path.join(out, 'p%d.jpg' % n)
    if os.path.exists(fn): continue
    try: ao.image(ids[n - 1], 1000).save(fn, quality=80)
    except Exception as e: print('fail', n, e, flush=True)
    time.sleep(1.0)
print('done', flush=True)
