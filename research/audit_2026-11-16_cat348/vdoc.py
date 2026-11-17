"""Fetch Vestigia document pages by vestigia_id; print record, notes, relations and image list.

python -I -X utf8 vdoc.py 2949,2950 [--img]   (run from this folder; writes img/v<ID>.html, img/v<ID>_<n>.jpg)
"""
import html, json, re, subprocess, sys, time, os

ids = sys.argv[1].split(',')
want_img = '--img' in sys.argv
os.makedirs('img', exist_ok=True)
out = {}


def curl(u, dest=None):
    a = ['curl', '-sL', '-A', 'Mozilla/5.0', u]
    if dest:
        subprocess.run(a + ['-o', dest])
        return None
    return subprocess.run(a, capture_output=True, text=True, encoding='utf8').stdout


def brief(lst):
    r = []
    for x in lst or []:
        r.append({k: x.get(k) for k in ('vestigia_id', 'df', 'archive_ref', 'format', 'date_from') if k in x} or
                 {k: v for k, v in x.items() if not isinstance(v, (dict, list))})
    return r


for vid in ids:
    s = curl(f'https://www.vestigia.hu/documents/{vid}')
    open(f'img/v{vid}.html', 'w', encoding='utf8').write(s)
    m = re.search(r'data-page="([^"]+)"', s)
    if not m:
        print(vid, 'no data-page'); continue
    doc = json.loads(html.unescape(m.group(1)))['props'].get('document') or {}
    ir = doc.get('import_raw') or {}
    rec = {
        'vestigia_id': vid, 'df': doc.get('df'), 'ref': doc.get('archive_ref'), 'date': doc.get('date_from'),
        'format': doc.get('format'), 'length': doc.get('length'), 'langs': [l['code'] for l in doc.get('languages') or []],
        'incipit': doc.get('incipit'), 'explicit': doc.get('explicit'), 'comment': doc.get('comment'),
        'summary': doc.get('summary'), 'bibliography': doc.get('bibliography'),
        'megjegyzesek': ir.get('megjegyzesek'), 'regi_megjegyzes': ir.get('regi_megjegyzes'),
        'publikaciok': ir.get('publikaciok'), 'mellerendelo': ir.get('mellerendelo_kapcsolatok'),
        'kivul': ir.get('adatbazison_kivuli_kapcsolat'), 'szulo': ir.get('szulo'), 'regi_jelzetek': ir.get('regi_jelzetek'),
        'parent': brief([doc['parent']]) if doc.get('parent') else None,
        'rel_left': brief(doc.get('related_documents_left')), 'rel_right': brief(doc.get('related_documents_right')),
        'enclosed': brief(doc.get('enclosed_documents')),
        'files': [(f['name'], f.get('size'), f.get('web_url')) for f in doc.get('files') or []],
        'public_images': doc.get('public_images'),
    }
    out[vid] = rec
    print(json.dumps({k: v for k, v in rec.items() if k != 'files'}, ensure_ascii=False))
    for i, f in enumerate(rec['files'], 1):
        print('   img', i, f[0], f[1])
        if want_img and f[2]:
            curl(f[2], f'img/v{vid}_{i}.jpg'); time.sleep(0.8)
    time.sleep(1.2)

old = {}
if os.path.exists('img/vdoc.json'):
    old = json.load(open('img/vdoc.json', encoding='utf8'))
old.update(out)
json.dump(old, open('img/vdoc.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
