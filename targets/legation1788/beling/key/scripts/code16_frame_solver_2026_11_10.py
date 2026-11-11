"""Code 16: frame-constrained segmentation.

Premise tested on 10 Nov 2026: Code 16 (Pinckney 1793, Eaton 1802, Lear 1813) draws its plaintext
elements from the printed 1600-element list that Weber gives for WE023-WE028 (different numbering).
If so, every multi-group word must split into list elements, and each element belongs to one number.

Inputs (word = plaintext letters + ordered groups with marks):
  - Tunis word spans (output/tunis_known_plaintext_2026-11-10/tunis_word_spans.tsv), flags '' only
  - Tunis postscript spans re-read 10 Nov (editors' decipherment), output/tunis_known_plaintext_2026-11-10/tunis_postscript_spans_v2.tsv
  - Lear 1813 interlined spans, output/adjudication_2026-11-06/lear_span_ledger.tsv
  - Bourdeau's Pinckney interlines, repo pin c14c822 transcription/pinckney_m30.tsv (optional, --with-pinckney)
Marks: ^ doubles the element's last letter; + lets a suffix follow (s, es, d, ed, n, en, 's).

Method: enumerate every way to cut each word into list elements; a group's domain is the set of elements
it takes in at least one cut of every word it occurs in; singletons are removed from other domains; repeat
to a fixed point.  No scoring, no language model: a value is "derived" only when one element survives.

Usage: python3 scripts/code16_frame_solver_2026_11_10.py [--with-pinckney] [--vocab PATH]
"""
from pathlib import Path
import csv, json, re, sys, collections, argparse

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/code16_merged_2026-11-10'
SUFFIXES = ['s', 'es', 'd', 'ed', 'n', 'en']
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha())


def load_vocab(path):
    vocab = collections.Counter()
    p = Path(path)
    if p.suffix == '.json':                      # rough parse: code -> {number: element}
        T = json.loads(p.read_text())
        for code in ('WE023', 'WE024', 'WE025', 'WE026', 'WE027', 'WE028'):
            for v in set(norm(x) for x in T.get(code, {}).values()):
                if v: vocab[v] += 1
    else:                                        # cleaned list: element<TAB>count
        for line in p.read_text().splitlines():
            parts = line.split('\t')
            e = norm(parts[0])
            if e: vocab[e] += int(parts[1]) if len(parts) > 1 and parts[1].strip().isdigit() else 1
    return vocab


def tok(t):
    t = t.strip()
    m = re.fullmatch(r'(\d+)([+^?]*)', t)
    return (int(m.group(1)), m.group(2)) if m else None


def load_words(with_pinckney):
    words = []                                   # (source, locator, word_letters, [(group, marks)])
    for r in csv.DictReader((ROOT / 'output/tunis_known_plaintext_2026-11-10/tunis_word_spans.tsv').open(), delimiter='\t'):
        if r['flag']:
            continue
        gs = [tok(x) for x in r['groups'].split('-')]
        if all(gs) and not any('?' in m for _, m in gs):
            words.append(('tunis', r['n'], norm(r['word']), gs))
    for r in csv.DictReader((ROOT / 'output/tunis_known_plaintext_2026-11-10/tunis_postscript_spans_v2.tsv').open(), delimiter='\t'):
        if r['flag']:
            continue
        gs = [tok(x) for x in r['groups'].split('-')]
        if all(gs):
            words.append(('tunis-ps', r['n'], norm(r['word']), gs))
    fix = {'generally': 'fully', 'report': 'reply'}       # the edition's corrections, noted 6 Nov
    for r in csv.DictReader((ROOT / 'output/adjudication_2026-11-06/lear_span_ledger.tsv').open(), delimiter='\t'):
        gs = [tok(x) for x in r['groups'].split()]
        w = norm(fix.get(r['interlinear'].strip().lower(), r['interlinear']))
        if w and gs and all(gs) and not any('?' in m for _, m in gs):
            words.append(('lear', f"{r['line']}:{r['span']}", w, gs))
    if with_pinckney:
        p = ROOT / 'sources/raw/reconstruction_2026-11-06/repo/targets/legation1788/transcription/pinckney_m30.tsv'
        rows = list(csv.DictReader([l for l in p.open() if not l.startswith('#')], delimiter='\t'))
        cur = None
        for r in rows:
            w = (r['interlinear_word'] or '').strip()
            g = tok(r['group'])
            if not w or g is None or 'approx' in (r['note'] or '') or '——' in w or w in (';—',):
                if cur and w.startswith('(') and g is not None and norm(w) == cur[2]:
                    cur[3].append(g); continue
                if cur: words.append(tuple(cur)); cur = None
                continue
            if w.startswith('('):
                if cur and norm(w) == cur[2]: cur[3].append(g)
                continue
            if cur: words.append(tuple(cur))
            cur = ['pinckney', f"{r['frame']}:{r['line']}:{r['position']}", norm(w.replace('[', '').replace(']', '')), [g]]
        if cur: words.append(tuple(cur))
        words = [w for w in words if w[2] and not any('?' in m for _, m in w[3])]
    return words


def cuts(word, gs, dom, vocab):
    """All element sequences that spell `word` with one element per group."""
    out = []
    def rec(i, pos, acc):
        if i == len(gs):
            if pos == len(word): out.append(tuple(acc))
            return
        g, marks = gs[i]
        cand = dom.get(g)
        rest = word[pos:]
        if cand is None:
            cand = [rest[:k] for k in range(1, len(rest) + 1) if rest[:k] in vocab]
        for e in cand:
            piece = e + (e[-1] if '^' in marks else '')
            if not rest.startswith(piece):
                continue
            ends = [pos + len(piece)]
            if '+' in marks:
                ends += [pos + len(piece) + len(s) for s in SUFFIXES if rest[len(piece):].startswith(s)]
                if piece.endswith('e'):                       # receive+d, take+n
                    ends += [pos + len(piece) - 1 + len(s) for s in ('ed', 'en', 'es') if rest[len(piece) - 1:].startswith(s)]
            for e2 in set(ends):
                rec(i + 1, e2, acc + [e])
    rec(0, 0, [])
    return out


def solve(words, vocab, fixed):
    dom = {g: {v} for g, v in fixed.items()}
    log = []
    for rnd in range(30):
        changed = False
        newdom = {}
        failures = []
        for src, loc, w, gs in words:
            cs = cuts(w, gs, dom, vocab)
            if not cs:
                failures.append((src, loc, w, gs)); continue
            for i, (g, m) in enumerate(gs):
                s = {c[i] for c in cs}
                newdom[g] = newdom[g] & s if g in newdom else s
        for g, s in newdom.items():
            if not s:
                log.append(('empty', g)); continue
            if g not in dom or s != dom[g]:
                if g not in dom or len(s) < len(dom[g]):
                    dom[g] = s; changed = True
        single = {next(iter(s)): g for g, s in dom.items() if len(s) == 1}
        for g, s in dom.items():
            if len(s) > 1:
                t = {e for e in s if single.get(e, g) == g}
                if t and t != s:
                    dom[g] = t; changed = True
        if not changed:
            break
    return dom, failures, log


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--with-pinckney', action='store_true')
    ap.add_argument('--vocab', default=str(ROOT / 'sources/raw/weber_ill_2026-11-10/weber_tables_ocr_parse.json'))
    ap.add_argument('--tag', default='rough')
    a = ap.parse_args()
    vocab = load_vocab(a.vocab)
    words = load_words(a.with_pinckney)
    # fixed: single-group words in the same word list (each must itself be on the element list or it is kept as given)
    fixed = {}
    conflicts = []
    for src, loc, w, gs in words:
        if len(gs) == 1 and gs[0][1] == '':
            g = gs[0][0]
            if g in fixed and fixed[g] != w: conflicts.append((g, fixed[g], w, src, loc))
            fixed.setdefault(g, w)
    multi = [x for x in words if len(x[3]) > 1 or x[3][0][1]]
    dom, failures, log = solve(multi, vocab, fixed)
    derived = {g: next(iter(s)) for g, s in dom.items() if len(s) == 1 and g not in fixed}
    owners = collections.defaultdict(list)
    for g, s in dom.items():
        if len(s) == 1: owners[next(iter(s))].append(g)
    duplicates = {e: sorted(gs) for e, gs in owners.items() if len(gs) > 1}
    small = {g: sorted(s) for g, s in dom.items() if 1 < len(s) <= 4}
    in_vocab = sum(1 for v in fixed.values() if v in vocab)
    res = dict(vocab_elements=len(vocab), words=len(words), multi_group_words=len(multi), fixed_direct=len(fixed),
               fixed_direct_on_list=in_vocab, derived_unique=len(derived), small_domains=len(small),
               unsegmentable=len(failures), direct_conflicts=conflicts, duplicate_elements=duplicates,
               fixed_not_on_list=sorted((g, v) for g, v in fixed.items() if v not in vocab))
    (OUT / f'frame_solver_{a.tag}.json').write_text(json.dumps(dict(summary=res, derived={str(k): v for k, v in sorted(derived.items())},
                                                                   small={str(k): v for k, v in sorted(small.items())},
                                                                   unsegmentable=[(s, l, w, '-'.join(f'{g}{m}' for g, m in gs)) for s, l, w, gs in failures]), indent=1) + '\n')
    print(json.dumps({k: v for k, v in res.items() if k not in ('fixed_not_on_list',)}, indent=1))
    print('fixed not on list:', res['fixed_not_on_list'])
    print('derived:', sorted(derived.items()))
    print('small:', sorted(small.items())[:60])
    print('unsegmentable:', [(s, w, '-'.join(f'{g}{m}' for g, m in gs)) for s, l, w, gs in failures][:80])
    return dom, fixed, derived


if __name__ == '__main__':
    main()
