"""Held-out test on M30-002-0178, as declared in tests/PREREGISTRATION_0178.md.
Imports ordered_match/score from scripts/eaton_heldout_score_2026_11_10.py unchanged.
Truth: ASP Foreign Relations 1:328, "Explication of the ciphers in Mr. Pinckney's letter of November 25, 1793" (archive.org OCR),
with the obvious OCR errors listed in OCR_FIXES corrected to the printed words (letters only matter)."""
from pathlib import Path
import csv, json, hashlib, importlib.util, sys

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'output/code16_pinckney_2026-11-11'
spec = importlib.util.spec_from_file_location('ev', ROOT / 'scripts/eaton_heldout_score_2026_11_10.py')
ev = importlib.util.module_from_spec(spec); spec.loader.exec_module(ev)
TRUTH = ROOT / 'sources/raw/code16_pinckney_2026-11-11/asp_fr1/extracts/asp_fr1_p328_explication_17931125_ocr.txt'
OCR_FIXES = [('(«.)', '(a.)'), ('lb.)', '(b.)'), ('liim', 'him'), ('fle answered', 'He answered'), ('tlielr', 'their'),
             ('embai-\nrassments', 'embarrassments'), ('embai- \nrassments', 'embarrassments'), ('furnish  lum', 'furnish  him'), ('(f.)', '(c.)')]


def load_key(p):
    return {int(r['group']): r['value'] for r in csv.DictReader(open(p), delimiter='\t') if ev.norm(r['value'])}


def truth():
    t = TRUTH.read_text()
    t = t[t.index('That  the  real'):]
    for a, b in OCR_FIXES: t = t.replace(a, b)
    return t


def main(truth_text=None, label='ASP FR 1:328'):
    ag = json.loads((OUT / 'tests/0178_groups_agreed.json').read_text())
    tt = truth_text or truth()
    keys = {'K1 (primary)': OUT / 'tests/K1_frozen_v1_minus_0178.tsv', 'K0 frozen_v1 as is (contaminated)': ROOT / 'output/code16_merged_2026-11-10/frozen_key_v1.tsv',
            'K2 Tunis+Lear only': OUT / 'tests/K2_frozen_v1_tunis_lear.tsv', 'K5 key v5 minus 0178 B': OUT / 'tests/K5_key_v5_minus_0178B.tsv'}
    res = dict(truth=label, truth_letters=len(ev.norm(tt)), runs={})
    for name, p in keys.items():
        k = load_key(p)
        for gname in ('groups_agreed', 'groups_blind_certain'):
            r = ev.score([(ag[gname], tt)], k, shuffles=200, seed=17931125)
            r['key_sha256'] = hashlib.sha256(p.read_bytes()).hexdigest()
            r['pass'] = bool(r['score'] is not None and r['score'] >= 0.85 and r['score'] - r['shuffled_max'] >= 0.30)
            res['runs'][f'{name} | {gname}'] = r
            print(f'{name:38s} {gname:22s}', {x: r[x] for x in ('groups', 'covered', 'matched', 'score', 'shuffled_mean', 'shuffled_max', 'pass')})
    return res


if __name__ == '__main__':
    res = main()
    (OUT / 'tests/0178_result_asp.json').write_text(json.dumps(res, indent=1) + '\n')
