"""Run rekey.py (read-only, imported) on LJS 51 chains whose segmentation can be trusted.
Selection (rule agreed with the coordinating session, 27 Nov 2026):
  - fit_check starts with 'fits' (signs vs letters within 2),
  - no by-eye correction in the record (no signs_corrected_by_eye, 'by eye' absent from fit_check),
  - the segmenter's own sign count on the chain's cipher lines equals the record's signs_total exactly,
  - plus the tashifi run 14v.7 as a known-good control.
Every key is provisional: learned from its own alignment on uncorrected segmentation.
usage: python run_fork.py [--select-only] [--shuffles N]
"""
import os, sys, json, glob, re, argparse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import numpy as np
import rekey

SIGNS = rekey.SIGNS
FILES = ['chains_0006_0029.jsonl', 'chains_0030_0053.jsonl', 'chains_0054_0077.jsonl']

def img_of(p):
    return int(re.sub(r'\D', '', str(p['image']))[-4:])

def seg_count(img, l0, l1):
    d = json.load(open(os.path.join(SIGNS, '%04d' % img, 'index.json')))
    return sum(1 for r in d if r['kind'] == 'sign' and l0 <= r['line'] <= l1)

def cipher_spec(r):
    """cipher entries come first in `pages`; take the shortest prefix whose segmenter count equals signs_total."""
    tot, spec = 0, []
    for p in r.get('pages', []):
        l = p.get('lines') or []
        if len(l) < 2: break
        img = img_of(p)
        spec.append((img, l[0], l[1]))
        tot += seg_count(img, l[0], l[1])
        if tot == r.get('signs_total'):
            return spec, tot
    return None, tot

def select():
    keep, skip = [], []
    for f in FILES:
        for line in open(os.path.join(os.path.dirname(HERE), f), encoding='utf8'):
            r = json.loads(line)
            cid = r['chain_id']
            fc = json.dumps(r.get('fit_check', ''), ensure_ascii=False)
            if cid == '14v.7':
                continue
            if not fc.strip('"').lower().startswith('fits'):
                skip.append((cid, 'fit_check not "fits": ' + fc[:80])); continue
            if 'signs_corrected_by_eye' in r or 'by eye' in fc or 'by eye' in str(r.get('count_method', '')).lower()[:12]:
                skip.append((cid, 'by-eye correction in record')); continue
            spec, tot = cipher_spec(r)
            if not spec:
                skip.append((cid, 'segmenter count on the cipher lines (%s) does not equal signs_total (%s)' % (tot, r.get('signs_total')))); continue
            pt = (r.get('plaintext') or {}).get('text') or ''
            if not pt or 'not read' in pt[:20]:
                skip.append((cid, 'no plaintext')); continue
            keep.append(dict(chain_id=cid, spec=spec, plaintext=pt, red=bool(r.get('red_gloss')), gloss=r.get('gloss_letters'),
                             signs_total=r.get('signs_total'), letters=r.get('plaintext_letters'), certainty=(r.get('plaintext') or {}).get('certainty')))
    return keep, skip

def conv(o):
    if isinstance(o, np.integer): return int(o)
    if isinstance(o, np.floating): return float(o)
    return str(o)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--select-only', action='store_true'); ap.add_argument('--shuffles', type=int, default=100)
    a = ap.parse_args()
    keep, skip = select()
    json.dump(dict(keep=[{k: v for k, v in c.items() if k != 'plaintext'} for c in keep], skip=skip), open(os.path.join(HERE, 'selection.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1, default=conv)
    print('keep', len(keep), [c['chain_id'] for c in keep]); print('skip', len(skip))
    if a.select_only: sys.exit()
    # control: the tashifi run with the pilot's plaintext
    jobs = [dict(chain_id='14v.7', spec=rekey.CHAINS['D']['spec'], plaintext=rekey.PT['D'], red=False)] + keep
    for c in jobs:
        out_json = os.path.join(HERE, c['chain_id'] + '.json')
        if os.path.exists(out_json): print('done', c['chain_id']); continue
        try:
            out, *_ = rekey.run_chain('fork_' + c['chain_id'], c['spec'], c['plaintext'], s=1, nshuf=a.shuffles,
                                      outdir=os.path.join(rekey.ROOT, 'output', 'ljs51', 'keys_fork', c['chain_id']), log=lambda *x: None)
        except Exception as e:
            out = dict(chain=c['chain_id'], error=repr(e))
        out['label'] = 'provisional: learned from its own alignment on uncorrected segmentation'
        out['chain_id'] = c['chain_id']
        if c.get('red'): out['gloss_letters_record'] = c.get('gloss')
        json.dump(out, open(out_json, 'w', encoding='utf8'), ensure_ascii=False, indent=1, default=conv)
        m = out.get('measures', {}); cs = out.get('control', {})
        print(c['chain_id'], out.get('signs'), out.get('letters'), {k: m.get(k) for k in ('aligned_share', 'letter_fit', 'rasm_purity')}, 'ctrl', {k: cs.get(k) for k in ('letter_fit',)}, out.get('error', ''))
