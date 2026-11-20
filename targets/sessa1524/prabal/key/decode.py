"""Apply key/key.tsv to the rows files and print the decode lines; with --check, compare them with the record pages.

Usage (from the folder prabal/): python3 key/decode.py [--check]

Rules, as in key/key.tsv: a unit `?` is shown `…`; `v` followed by `db`, and `db` after `v`, are the opener (no
letter); a unit is looked up in lower case, with the long s as s and a final ~ dropped (the switch f~ keeps
it), in the scope of its page,
then in scope "all"; a ledger-key value is marked doubtful (x?) when the unit ends in ~ or the table names a
doubt; values of no letters do not show; letters spelled sign by sign are joined to their neighbours by hyphens.
"""
from __future__ import annotations

import glob
import os
import re
import sys

SHOW = {'added entry': 'entry', 'clear word': 'clear', 'clerk value': 'proposed', 'no value': 'none'}


def norm(unit: str) -> str:
    if unit == 'f~':
        return unit  # the switch keeps its ~
    return unit.replace('ſ', 's').lower().rstrip('~')


def load_key(path: str) -> dict[tuple[str, str], tuple[str, str, str]]:
    key: dict[tuple[str, str], tuple[str, str, str]] = {}
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or line.startswith('scope\t'):
            continue
        scope, label, _led, value, kind, _src, doubt, _n, _date = line.rstrip('\n').split('\t')
        if value == '(opener)':
            continue  # the opener rule applies before the lookup
        value = '' if value.startswith('(') else value
        key[(scope, label)] = (kind, value, doubt)
    return key


def render(parts: list[tuple[str, str]]) -> str:
    shown = []
    for kind, text in parts:
        if kind in ('key', 'key?', 'entry', 'proposed') and text == '':
            continue
        shown.append({'mask': '…', 'none': '·', 'clear': f'_{text}_', 'entry': '{' + text + '}',
                      'proposed': f'[{text}]', 'key?': f'{text}?', 'key': text}[kind])

    def letterish(s: str) -> bool:
        return len(s.strip('[]?')) == 1 and s not in ('…', '·') and not s.startswith('_')

    out = ''
    for i, s in enumerate(shown):
        if i == 0:
            out = s
        else:
            prev = shown[i - 1]
            joined = (letterish(prev) or letterish(s)) and '…' not in (prev, s)
            out += ('-' if joined else ' ') + s
    return out


def decode_row(rec: str, page: str, units: list[str], key) -> str:
    labels = [norm(u) if u != '?' else '?' for u in units]
    parts = []
    for i, u in enumerate(units):
        n = labels[i]
        if u == '?':
            parts.append(('mask', ''))
        elif (n == 'v' and i + 1 < len(labels) and labels[i + 1] == 'db') or \
                (n == 'db' and i > 0 and labels[i - 1] == 'v'):
            parts.append(('key', ''))
        else:
            kind, value, doubt = key.get((f'{rec}/{page}', n)) or key[('all', n)]
            if kind == 'ledger key':
                parts.append(('key?' if (u.endswith('~') or doubt) else 'key', value))
            else:
                parts.append((SHOW[kind], value))
    return render(parts)


def main() -> None:
    here = os.getcwd()
    key = load_key(os.path.join(here, 'key', 'key.tsv'))
    check = '--check' in sys.argv
    rows = differ = 0
    for path in sorted(glob.glob(os.path.join(here, 'transcription', '*_rows.txt'))):
        rec = os.path.basename(path).split('_')[0]
        page_lines = {}
        if check:
            for line in open(os.path.join(here, f'r{rec[1:]}.md'), encoding='utf-8'):
                m = re.match(r'- R\d+, p\. (\S+), (\S+): `(.*)`$', line.rstrip('\n'))
                if m:
                    page_lines[(m.group(1), m.group(2))] = m.group(3)
        for line in open(path, encoding='utf-8'):
            if line.startswith('#'):
                continue
            head, *units = line.rstrip('\n').split(' ')
            page, row = head.split('/')
            text = decode_row(rec, page, [u for u in units if u], key)
            rows += 1
            if check:
                differ += text != page_lines.get((page, row))
            else:
                print(f'{rec}, p. {page}, {row}: {text}')
    if check:
        print(f'rows {rows}, differ {differ}')


if __name__ == '__main__':
    main()
