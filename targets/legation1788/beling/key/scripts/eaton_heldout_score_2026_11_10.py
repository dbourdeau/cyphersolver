"""Scoring for the held-out test on Eaton to Madison, 22 Oct 1802.

Implements output/code16_merged_2026-11-10/PREREGISTRATION_eaton_1802-10-22.md.
Written before the transcriptions or the edition text were seen.

Functions are generic:
  parse_code_line(text)        -> list of (group:int, marks:str, word_break_after:bool)
  agreement(a_groups, b_groups)-> aligned pairs, share identical
  ordered_match(values, text)  -> largest number of key values laid on `text` in order under the gap rule
  score(stretches, key, shuffles, seed)

A stretch is (groups, truth_text): the agreed groups of one coded passage and the edition's words for it.
"""
import csv, difflib, json, random, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha())
TOK = re.compile(r'(?:(ins|sup):)?(\d{1,4})([+^?]*)')


def parse_code_line(text):
    out = []
    for m in TOK.finditer(text):
        out.append((int(m.group(2)), m.group(3) + ('i' if m.group(1) == 'ins' else '') + ('s' if m.group(1) == 'sup' else '')))
    return out


def load_transcription(path):
    """-> list of rows (frame, line_no, kind, content)."""
    rows = []
    with open(path) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            rows.append(r)
    return rows


def agreement(a, b):
    """a, b: lists of group numbers. Returns (pairs, n_equal, n_a, n_b) from a longest-common-subsequence alignment."""
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    equal = sum(bl.size for bl in sm.get_matching_blocks())
    return sm.get_opcodes(), equal, len(a), len(b)


def ordered_match(values, text, skipped_before):
    """values: key values (letters) of covered groups in order; skipped_before[i]: groups skipped between
    covered value i-1 and i (uncovered groups).  A value must start within 12*(k+1) letters of the previous
    match's end, where k counts groups skipped since that match (uncovered ones and covered ones left unmatched).
    Returns the largest number of values matched."""
    # state: best[m] = dict(end_pos -> min skipped since last match)  kept small: for each m keep the smallest end and a few alternatives
    states = {0: {(0, 0)}}                 # m -> set of (end, k); before the first match the start is free
    first = True
    for i, v in enumerate(values):
        new = {}
        for m, st in states.items():
            for end, k in st:
                kk = k + skipped_before[i]
                # option: leave this value unmatched
                new.setdefault(m, set()).add((end, kk + 1))
                # option: match it
                lim = len(text) if m == 0 else end + 12 * (kk + 1)
                pos = text.find(v, end)
                while pos != -1 and pos <= lim:
                    new.setdefault(m + 1, set()).add((pos + len(v), 0))
                    pos = text.find(v, pos + 1)
                    if len(new[m + 1]) > 400: break
        # prune: per m keep the 40 states with smallest end (ties: smallest k)
        states = {m: set(sorted(st)[:40]) for m, st in new.items()}
    return max(states)


def score(stretches, key, shuffles=200, seed=18021022):
    """stretches: list of (groups:list[int], truth:str).  key: {group: value}."""
    def run(k):
        matched = covered = total = 0
        for groups, truth in stretches:
            t = norm(truth)
            vals, skipped, s = [], [], 0
            for g in groups:
                total += 1
                if g in k and norm(k[g]):
                    vals.append(norm(k[g])); skipped.append(s); s = 0
                else:
                    s += 1
            covered += len(vals)
            if vals: matched += ordered_match(vals, t, skipped)
        return matched, covered, total
    m, c, t = run(key)
    rng = random.Random(seed)
    gl = sorted(key); vl = [key[g] for g in gl]
    base = []
    for _ in range(shuffles):
        sh = vl[:]; rng.shuffle(sh)
        mm, cc, _ = run(dict(zip(gl, sh)))
        base.append(mm / cc if cc else 0.0)
    return dict(groups=t, covered=c, coverage=round(c / t, 3) if t else None, matched=m,
                score=round(m / c, 3) if c else None, shuffled_mean=round(sum(base) / len(base), 3),
                shuffled_max=round(max(base), 3))


def load_key(path=ROOT / 'output/code16_merged_2026-11-10/frozen_key_v1.tsv'):
    return {int(r['group']): r['value'] for r in csv.DictReader(open(path), delimiter='\t')}


if __name__ == '__main__':
    # machinery self-check on material that IS in the key (not a test of anything): Tunis postscript
    key = load_key()
    ps = list(csv.DictReader(open(ROOT / 'output/tunis_known_plaintext_2026-11-10/tunis_postscript_spans_v2.tsv'), delimiter='\t'))
    groups = [g for r in ps for g, _ in parse_code_line(r['groups'])]
    truth = ' '.join(r['word'] for r in ps)
    print('self-check (in-key material, expect high):', score([(groups, truth)], key, shuffles=50))
