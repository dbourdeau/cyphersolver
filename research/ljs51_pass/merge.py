"""Merge the per-chunk page records of the LJS 51 pass; recompute folios from image numbers."""
import json, glob, re, sys, collections
pages = {}
for f in sorted(glob.glob('pages_*.jsonl')):
    for i, l in enumerate(open(f, encoding='utf8')):
        l = l.strip()
        if not l: continue
        try: d = json.loads(l)
        except Exception as e: print('BAD', f, i, e); continue
        n = int(re.sub(r'\D', '', str(d['image']))[-4:])
        d['n'] = n
        k = n - 6
        d['folio_computed'] = f"{k//2+1}{'r' if k%2==0 else 'v'}"
        if str(d.get('folio')) != d['folio_computed']:
            d['_folio_label_was'] = d.get('folio'); d['folio'] = d['folio_computed']
        if n in pages: print('DUP', n)
        pages[n] = d
missing = [n for n in range(6, 218) if n not in pages]
print('pages', len(pages), 'missing', missing)
print('folio labels corrected:', [(p['n'], p['_folio_label_was'], p['folio']) for p in pages.values() if '_folio_label_was' in p])
json.dump([pages[n] for n in sorted(pages)], open('pages_merged.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
kinds = collections.Counter(); blocks = []
for n in sorted(pages):
    p = pages[n]
    for s in p['contents']:
        kinds[s.get('kind')] += 1
        if s.get('kind') == 'cipher':
            blocks.append((p['folio'], s))
print(kinds)
print('cipher segments', len(blocks))
red = [(f, s) for f, s in blocks if s.get('red_gloss')]
print('red-gloss segments', len(red), sorted({f for f, _ in red}, key=lambda x: (int(x[:-1]), x[-1])))
nop = [p['folio'] for n, p in sorted(pages.items()) if p.get('cipher_without_plaintext')]
print('pages flagged cipher_without_plaintext', len(nop), nop)
