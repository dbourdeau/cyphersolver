#!/usr/bin/env python3
"""Restore the exact frozen source and derive public review tables. No network calls."""
from pathlib import Path
import collections
import hashlib
import html
import json
import lzma
ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA256 = '8543944c982603cefa638a022131541d22344a8326638d849ac8537491c18b1c'

def restore_source(root=ROOT):
    seed = json.loads(lzma.decompress((root/'data/source.seed.xz').read_bytes()))
    def expand(value, uid, label):
        if isinstance(value, str):
            return uid if value == '@ID@' else label if value == '@LABEL@' else value
        if isinstance(value, list):
            return [expand(v, uid, label) for v in value]
        if isinstance(value, dict):
            return {k: expand(v, uid, label) for k, v in value.items()}
        return value
    rows = [{'line': line, 'passage': passage, 'units': [
        expand(seed['templates'][n], line+':'+suffix, label)
        for suffix, label, n in units]} for line, passage, units in seed['rows']]
    data = (json.dumps(rows, ensure_ascii=False, indent=2)+'\n').encode('utf-8')
    if hashlib.sha256(data).hexdigest() != SOURCE_SHA256:
        raise ValueError('Frozen source hash mismatch')
    path = root/'data/source.json'
    if path.exists() and path.read_bytes() != data:
        raise ValueError('Refusing to overwrite modified source.json')
    if not path.exists():
        path.write_bytes(data)
    return rows

def derive_review(root=ROOT):
    from decode import replay
    source = restore_source(root)
    key = json.loads((root/'data/key.json').read_text())['key']
    notes = json.loads((root/'data/key_notes.json').read_text())
    literal, tokens = replay(source, key)
    groups = collections.defaultdict(list)
    for t in tokens:
        groups[t['label']].append(t['id'])
    entries = []
    for label in sorted(groups):
        value = key.get(label)
        category = ('unassigned' if value is None else 'separator' if label == 'SEP_SLASH'
                    else 'candidate_null' if value == '' else 'one_letter' if len(value) == 1
                    else 'multiple_letters')
        grade, note = notes.get(label, ['Inherited proposal',
            'Retained for replay; no independent authentication. See full source and other occurrences.'])
        entries.append(dict(label=label, proposed_value=value, category=category,
            occurrences=len(groups[label]), positions=groups[label], grade=grade, evidence_note=note))
    for name, value in [('data/key_register.json', entries), ('results/token_replay.json', tokens)]:
        (root/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
    lines = ['# Proposed key register', '', 'All values are provisional. Counts are not accuracy.', '',
             '| Label | Value | Count | Grade |', '|---|---|---:|---|']
    for e in entries:
        val = '[unassigned]' if e['proposed_value'] is None else e['proposed_value'] or '[empty]'
        lines.append(f"| {e['label']} | {val} | {e['occurrences']} | {e['grade']} |")
    for e in entries:
        lines += ['', '## '+e['label'], e['evidence_note'], 'Positions: '+', '.join(e['positions'])]
    (root/'KEY_REGISTER.md').write_text('\n'.join(lines)+'\n')
    esc = html.escape
    doc = ['<!doctype html><meta charset="utf-8"><title>Catherine preliminary review</title>',
           '<style>body{font:16px sans-serif;max-width:1100px;margin:2em auto}td,th{padding:.3em;border:1px solid #aaa}table{border-collapse:collapse}code{overflow-wrap:anywhere}</style>',
           '<h1>Proposed partial decipherment</h1><p>Lawrence Beck, with the assistance of ChatGPT. Source photographs and prior work: Daniel Bourdeau.</p>',
           '<p>No manuscript images are included. Use data/line_coordinates.json with separately obtained photographs. Empty values are hypotheses, not deleted source observations.</p>']
    for row in source:
        out = ''.join(key.get(u['label'], '['+u['label']+']') for u in row['units'])
        doc += ['<h2>'+esc(row['line'])+'</h2><p><code>'+esc(out)+'</code></p><table><tr><th>ID</th><th>Label</th><th>Proposed expansion</th></tr>']
        for u in row['units']:
            val = key.get(u['label'], '[unassigned]') or '[empty]'
            doc.append('<tr><td>'+esc(u['id'])+'</td><td>'+esc(u['label'])+'</td><td>'+esc(val)+'</td></tr>')
        doc.append('</table>')
    (root/'review.html').write_text('\n'.join(doc))
    return source, key, literal, tokens, entries

if __name__ == '__main__':
    derive_review()
    print('Restored exact source and generated key register, token replay and local review.html.')
