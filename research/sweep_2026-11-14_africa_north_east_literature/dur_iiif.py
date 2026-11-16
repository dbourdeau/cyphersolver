#!/usr/bin/env python3
"""Durham IIIF helper. usage: dur_iiif.py ARK_ID [list | get LABEL OUTDIR [width]]
ARK_ID like t2mqj72p714z (from the n2t.durham.ac.uk/ark:/32150/<id>.html links in the XTF finding aid).
Manifest: https://iiif.durham.ac.uk/manifests/trifle/32150/<id[0:2]>/<id[2:4]>/<id[4:6]>/<id>/manifest ; images need no login."""
import sys, json, subprocess, time
ark = sys.argv[1]; cmd = sys.argv[2] if len(sys.argv) > 2 else 'list'
u = 'https://iiif.durham.ac.uk/manifests/trifle/32150/%s/%s/%s/%s/manifest' % (ark[0:2], ark[2:4], ark[4:6], ark)
d = json.loads(subprocess.run(['curl', '-s', '-m', '60', '-A', 'Mozilla/5.0 (research sweep)', u], capture_output=True).stdout)
cs = d['sequences'][0]['canvases']
if cmd == 'list':
    print(d.get('label'), len(cs)); print([c['label'] for c in cs])
else:
    label, out = sys.argv[3], sys.argv[4]; w = sys.argv[5] if len(sys.argv) > 5 else '1800'
    for c in cs:
        if c['label'] == label:
            svc = c['images'][0]['resource']['service']['@id']
            fn = '%s/%s.jpg' % (out, label.replace('/', '_'))
            subprocess.run(['curl', '-s', '-m', '90', '-o', fn, '%s/full/%s,/0/default.jpg' % (svc, w)]); print(fn); time.sleep(2.5)
