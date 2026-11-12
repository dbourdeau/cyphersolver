"""Put key v4 values next to the clerk's interlinear words, span by span, for the new blind transcriptions
(0196, 0208) and the existing 1 Oct 1795 rows. Read-only on the key. Output: interlinear_vs_v4.tsv"""
from pathlib import Path
import csv, re, sys

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'output/code16_pinckney_2026-11-11'
V4 = ROOT / 'output/code16_merged_2026-11-10/code16_key_v4.tsv'
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha())


def key():
    return {int(r['group']): r for r in csv.DictReader(V4.open(), delimiter='\t')}


def toks(s):
    out = []
    for t in s.split():
        m = re.fullmatch(r'\[?<?(\d+)([+^]*)(\??)>?\]?', t)
        out.append((int(m.group(1)), m.group(2), bool(m.group(3)) or t.startswith('<')) if m and '_' not in t else (None, '', True))
    return out


def rows():
    for fr in ('M30-002-0196', 'M30-002-0208'):
        for r in csv.DictReader((OUT / f'transcriptions/{fr}/spans.tsv').open(), delimiter='\t'):
            yield fr, r['line'], r['groups'], r['interlinear'], r['kind'], r['placement']
    for r in csv.DictReader((ROOT / 'output/pinckney1795_code16_2026-11-10/spans.tsv').open(), delimiter='\t'):
        if r['frame'] in ('0020', '0021'):
            yield 'M31-007-' + r['frame'], r['line'], r['groups'], r['interlinear'], r['kind'], r['placement']


def main():
    k = key()
    with (OUT / 'interlinear_vs_v4.tsv').open('w') as f:
        f.write('frame\tline\tgroups\tinterlinear\tplacement\tv4_values\tv4_grades\n')
        for fr, line, gs, w, kind, pl in rows():
            if not gs.strip(): continue
            t = toks(gs)
            vals = ' '.join((k[g]['value'] if g in k else '.') + ('?' if d else '') if g else '_' for g, m, d in t)
            grs = ' '.join((k[g]['grade'] if g in k else '-') if g else '_' for g, m, d in t)
            f.write(f'{fr}\t{line}\t{gs}\t{w}\t{pl}\t{vals}\t{grs}\n')
    print((OUT / 'interlinear_vs_v4.tsv').read_text())


if __name__ == '__main__':
    main()
