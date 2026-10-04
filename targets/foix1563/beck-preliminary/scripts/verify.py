#!/usr/bin/env python3
"""Verify frozen evidence and replay. This is not historical authentication."""
import hashlib
import json
import re
import sys
from pathlib import Path
from decode import ROOT, replay, select
from materialize import derive_review

def require(condition, message):
    if not condition:
        raise ValueError(message)

def main():
    try:
        manifest = json.loads((ROOT/'manifest.json').read_text())['files']
        for name, digest in manifest.items():
            path = ROOT/name
            require(path.resolve().is_relative_to(ROOT.resolve()), 'Unsafe manifest path')
            require(path.is_file(), 'Missing file: '+name)
            require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, 'Hash mismatch: '+name)
        source, key, literal, tokens, register = derive_review()
        prov = json.loads((ROOT/'data/provenance.json').read_text())
        require(len(source) == 41 and len(tokens) == 1038, 'Source count changed')
        require(len(register) == 96, 'Label count changed')
        require(sum(t['unresolved'] for t in tokens) == 25, 'Unknown count changed')
        require(literal == (ROOT/'results/literal.txt').read_text(), 'Literal output changed')
        for name, field in [('source.json','copied_source_sha256'), ('key.json','copied_key_sha256')]:
            require(hashlib.sha256((ROOT/'data'/name).read_bytes()).hexdigest() == prov[field], 'Research input changed: '+name)
        origins = [v for row in source for u in row['units'] for v in u.get('v9_origins', [u['id']])]
        require(len(origins) == len(set(origins)) == 1041, 'Origin accounting changed')
        claims = json.loads((ROOT/'data/claims.json').read_text())
        for c in claims:
            q = select(tokens, c['start'], c['end'])
            text = ''.join(t['expansion'] for t in q)
            require(text == c['literal'], 'Anchor text mismatch: '+c['id'])
            require(len(q) == c['source_units'] and len(text) == c['emitted_letters'], 'Anchor count mismatch')
            require(text == re.sub('[^a-z]', '', c['french'].lower()), 'Anchor has an unrecorded letter edit')
            require(not any(t['unresolved'] for t in q), 'Anchor contains an unknown')
            require([t['id'] for t in q if not t['expansion']] == c['null_positions'], 'Anchor null positions changed')
        for label in ['26','34','70','10','M_SWASH','N_MONOGRAM']:
            require(label not in key, 'Unknown silently assigned: '+label)
        require(replay(source, dict(key, RX='l'))[0] == (ROOT/'results/rival_RX_l.txt').read_text(), 'RX rival changed')
        print(json.dumps(dict(status='PASS', source_units=1038, lines=41, labels=96, unknowns=25,
            original_v9_positions=1041, anchors=len(claims), files_checked=len(manifest),
            meaning='Integrity and reproducible replay only; not authentication of handwriting or historical meaning.'), indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print('FAIL: '+str(exc), file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
