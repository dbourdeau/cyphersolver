"""Ur III seal inscriptions from ORACC epsd2/admin/ur3 (CC0), as a read control for the Indus seal texts.

build(zip) streams the ORACC JSON export (epsd2-admin-ur3.zip, 562 MB, not unpacked) and keeps only the lines on
'seal N' surfaces, with each lemma's citation form and part of speech (PN personal name, DN deity, RN royal name, N
noun, V verb ...). Writes data/ur3_seals.tsv: text, provenience, seal, line, tokens ('cf|pos' separated by spaces).
load() returns {(text, seal): {'site', 'lines': [[(cf, pos), ...], ...]}}.

Also runs on other ORACC epsd2 admin exports with an output path (the Old Akkadian export has seals on only 26
texts, too few to use).

Usage: python ur3_seals.py path/to/epsd2-admin-ur3.zip [out.tsv]
"""
import json
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(HERE, 'data', 'ur3_seals.tsv')
HEADER = '# Source: ORACC epsd2/admin/ur3 JSON export (CC0), seal surfaces only; tokens are citation form|POS.\n'


def build(path, out_path=TSV):
    z = zipfile.ZipFile(path)
    cat = json.loads(z.read([n for n in z.namelist() if n.endswith('/catalogue.json')][0]))['members']
    rows = []
    for n in z.namelist():
        if '/corpusjson/P' not in n:
            continue
        s = z.read(n).decode('utf-8')
        if '"seal' not in s:
            continue
        pid = os.path.basename(n)[:-5]
        state = {'seal': None, 'line': None}
        lines = {}

        def walk(x):
            if isinstance(x, dict):
                if x.get('node') == 'd':
                    if x.get('type') == 'surface':
                        lab = x.get('label') or ''
                        state['seal'] = lab.split()[1] if lab.startswith('seal') and len(lab.split()) > 1 else None
                        state['line'] = None
                    elif x.get('type') == 'line-start' and state['seal']:
                        state['line'] = x.get('n')
                if x.get('node') == 'l' and state['seal'] and state['line']:
                    f = x.get('f', {})
                    cf = (f.get('cf') or f.get('form') or x.get('frag') or '?').replace(' ', '_').replace('|', '/')
                    lines.setdefault((state['seal'], state['line']), []).append('%s|%s' % (cf, f.get('pos', '?')))
                for v in x.get('cdl', []):
                    walk(v)
        walk(json.loads(s))
        prov = (cat.get(pid, {}).get('provenience') or '').replace('\t', ' ')
        for (seal, line), toks in lines.items():
            rows.append((pid, prov, seal, line, ' '.join(toks)))
    with open(out_path, 'w', encoding='utf-8', newline='\n') as out:
        out.write(HEADER)
        out.write('text\tprovenience\tseal\tline\ttokens\n')
        for r in rows:
            out.write('\t'.join(r) + '\n')
    print('seal lines %d, texts %d' % (len(rows), len({r[0] for r in rows})))


def load(path=TSV):
    out = {}
    with open(path, encoding='utf-8') as f:
        hdr = None
        for ln in f:
            if ln.startswith('#'):
                continue
            p = ln.rstrip('\n').split('\t')
            if hdr is None:
                hdr = p
                continue
            r = dict(zip(hdr, p))
            o = out.setdefault((r['text'], r['seal']), {'site': r['provenience'], 'lines': {}})
            o['lines'][int(r['line']) if r['line'].isdigit() else r['line']] = [tuple(t.rsplit('|', 1)) for t in r['tokens'].split()]
    for o in out.values():
        o['lines'] = [o['lines'][k] for k in sorted(o['lines'], key=str)]
    return out


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else TSV)
