#!/usr/bin/env python3
"""Replay the published proposed key. This does not solve or authenticate the cipher."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[1]

def load_inputs(root: Path = ROOT) -> tuple[list[dict[str, Any]], dict[str, str]]:
    from materialize import restore_source
    restore_source(root)
    source = json.loads((root / 'data/source.json').read_text(encoding='utf-8'))
    mapping = json.loads((root / 'data/key.json').read_text(encoding='utf-8'))['key']
    if not isinstance(source, list) or not isinstance(mapping, dict):
        raise ValueError('Invalid source/key schema')
    if not all(isinstance(k, str) and isinstance(v, str) for k, v in mapping.items()):
        raise ValueError('Key values must be strings; absent keys denote unresolved signs.')
    return source, mapping

def replay(source: list[dict[str, Any]], mapping: dict[str, str]) -> tuple[str, list[dict[str, Any]]]:
    lines, tokens, seen = [], [], set()
    for row in source:
        out = []
        for unit in row['units']:
            uid, label = unit['id'], unit['label']
            if uid in seen:
                raise ValueError(f'Duplicate source ID: {uid}')
            seen.add(uid)
            unresolved = label not in mapping
            value = f'[{label}]' if unresolved else mapping[label]
            out.append(value)
            tokens.append({'id': uid, 'line': row['line'], 'passage': row['passage'],
                           'label': label, 'expansion': value, 'unresolved': unresolved})
        lines.append(row['line'] + ' ' + ''.join(out))
    return '\n'.join(lines) + '\n', tokens

def select(tokens: list[dict[str, Any]], start: str, end: str) -> list[dict[str, Any]]:
    ids = {t['id']: i for i, t in enumerate(tokens)}
    if start not in ids or end not in ids or ids[start] > ids[end]:
        raise ValueError('Span must have existing, ordered source IDs.')
    selected = tokens[ids[start]:ids[end]+1]
    if len({t['passage'] for t in selected}) != 1:
        raise ValueError('A span cannot cross separate extracts.')
    return selected

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--span', nargs=2, metavar=('START_ID', 'END_ID'))
    ap.add_argument('--tokens', action='store_true', help='Print the position-by-position expansion.')
    args = ap.parse_args()
    try:
        source, mapping = load_inputs()
        literal, tokens = replay(source, mapping)
        if args.span:
            tokens = select(tokens, *args.span)
            literal = ''.join(t['expansion'] for t in tokens) + '\n'
        if args.tokens:
            print('source_id\tlabel\texpansion\tstatus')
            for t in tokens:
                status = 'unresolved' if t['unresolved'] else ('empty' if t['expansion']=='' else 'proposed')
                print(f"{t['id']}\t{t['label']}\t{t['expansion'] or '[empty]'}\t{status}")
        else:
            sys.stdout.write(literal)
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'Replay failed: {exc}', file=sys.stderr)
        return 1
if __name__ == '__main__':
    raise SystemExit(main())
