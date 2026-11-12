"""Build the test keys for the 0178 held-out test (see tests/PREREGISTRATION_0178.md) and the transcription agreement.
Writes tests/K1_frozen_v1_minus_0178.tsv, tests/K2_frozen_v1_tunis_lear.tsv, tests/0178_groups_agreed.json."""
from pathlib import Path
import csv, re, json, hashlib, difflib

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'output/code16_pinckney_2026-11-11'
FROZEN = ROOT / 'output/code16_merged_2026-11-10/frozen_key_v1.tsv'
LEG = ROOT / 'output/push_2026-11-11/cyphersolver/targets/legation1788'  # integration note, 12 Nov 2026: in the repository these files are now targets/pinckney1793/key.tsv and transcription/pinckney_m30.tsv


def bourdeau_0178_groups():
    out = set()
    for l in (LEG / 'key.tsv').open():
        f = l.rstrip('\n').split('\t')
        if f[0] == '16' and 'M30-002-0178' in f[-1]:
            d = re.sub(r'\D', '', f[1].split()[0])
            if d: out.add(int(d))
    return out


def write_key(rows, path):
    with path.open('w') as f:
        f.write('group\tvalue\tsource\n')
        for r in rows: f.write(f"{r['group']}\t{r['value']}\t{r['source']}\n")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def blind_0178():
    rows = list(csv.DictReader((OUT / 'transcriptions/M30-002-0178/groups.tsv').open(), delimiter='\t'))
    seq = []
    for r in rows:
        g = r['group'].strip()
        ok = bool(re.fullmatch(r'\d+(\+\+|\+|\^)*', g))
        seq.append(dict(line=r['line'], pos=r['position'], raw=g, g=int(re.sub(r'\D', '', g)) if ok else None))
    return seq


def bourdeau_0178():
    rows = [r for r in csv.DictReader([l for l in (LEG / 'transcription/pinckney_m30.tsv').open() if not l.startswith('#')], delimiter='\t') if r['frame'] == '0178']
    out = []
    for r in rows:
        g = r['group'].strip(); d = re.sub(r'\D', '', g)
        out.append(int(d) if d and '?' not in g and '_' not in g else None)
    return out


def main():
    fro = list(csv.DictReader(FROZEN.open(), delimiter='\t'))
    b178 = bourdeau_0178_groups()
    removed = [r for r in fro if r['source'].startswith('bourdeau') and int(r['group']) in b178]
    k1 = [r for r in fro if r not in removed]
    k2 = [r for r in fro if not r['source'].startswith('bourdeau')]
    h1 = write_key(k1, OUT / 'tests/K1_frozen_v1_minus_0178.tsv')
    h2 = write_key(k2, OUT / 'tests/K2_frozen_v1_tunis_lear.tsv')
    a = blind_0178(); b = bourdeau_0178()
    A = [x['g'] if x['g'] is not None else -1 for x in a]
    B = [x if x is not None else -2 for x in b]
    sm = difflib.SequenceMatcher(a=A, b=B, autojunk=False)
    agreed = set()
    for blk in sm.get_matching_blocks():
        for i in range(blk.size): agreed.add(blk.a + i)
    groups_agreed = [a[i]['g'] for i in range(len(a)) if i in agreed and a[i]['g'] is not None]
    groups_blind = [x['g'] for x in a if x['g'] is not None]
    diffs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != 'equal': diffs.append(dict(tag=tag, blind=[a[i]['raw'] for i in range(i1, i2)], bourdeau=b[j1:j2], at=f"line {a[i1]['line']}" if i1 < len(a) else 'end'))
    res = dict(frozen_v1_sha256=hashlib.sha256(FROZEN.read_bytes()).hexdigest(),
               K1=dict(rows=len(k1), sha256=h1, removed=[(r['group'], r['value']) for r in removed]),
               K2=dict(rows=len(k2), sha256=h2),
               blind_rows=len(a), blind_certain=len(groups_blind), bourdeau_rows=len(b),
               identical_certain=len(groups_agreed),
               share_identical_of_blind_certain=round(len(groups_agreed) / len(groups_blind), 3),
               groups_agreed=groups_agreed, groups_blind_certain=groups_blind, differences=diffs)
    (OUT / 'tests/0178_groups_agreed.json').write_text(json.dumps(res, indent=1) + '\n')
    print({k: v for k, v in res.items() if k not in ('groups_agreed', 'groups_blind_certain', 'differences')})
    print(len(diffs), 'difference blocks')


if __name__ == '__main__':
    main()
