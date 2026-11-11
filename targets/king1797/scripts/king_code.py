"""Rufus King's London despatch code (the = 769), NARA M30 rolls 4-8: rebuild, test, grow and apply the key.

Self-contained: reads only files in this target folder plus the element list given with --elements.
It merges, unchanged in substance, the contributor's working scripts of 10-11 Nov 2026
(king_key_build_2026_11_11.py, code16_frame_solver_2026_11_10.py, eaton_heldout_score_2026_11_10.py,
king_align_2026_11_11.py, code16_align_cribs_2026_11_10.py); only paths and file names were changed.

  python3 scripts/king_code.py build  --elements LIST [--out DIR]   key v1 from corpus/interlined_spans.tsv
  python3 scripts/king_code.py score  --key KEY                      the declared test on No. 59 (test_no59/)
  python3 scripts/king_code.py align  --elements LIST --key KEY [--out DIR]
                                                                     key v2 = v1 + values aligned to clear texts
  python3 scripts/king_code.py decode --key KEY FILE                 line-by-line decode of a transcription .txt

LIST is the printed 1600-element word list behind Weber's WE023-WE028 (one element per line, optional count after a
tab; lines starting # skipped). The list used on 10-11 Nov 2026 was the union of WE023-WE028 taken from the text layer
of Weber (1979), not bundled here. The WE028 sheet transcribed from NARA M97 roll 13 in
../morris1813/beling/key/codebook_M97_13_transcription.csv (column 'reading') is the same printed list and can stand in:
pass that .csv and its 'reading' column is used. Results then differ slightly (see key_method.md).

Grades written: D = one unmarked group under one interlinear word (majority reading); S1/S2 = the only list element
that fits every word the group occurs in (frame solver; S1 one occurrence, S2 two or more); A = aligned to a clear text.
"""
from pathlib import Path
import argparse, collections, csv, hashlib, json, random, re, sys

HERE = Path(__file__).resolve().parents[1]
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha())

# ----------------------------------------------------------------------------------------------- element list

def load_vocab(path):
    """Counter of normalised elements. A .csv is read as the WE028 transcription (column 'reading')."""
    p = Path(path); vocab = collections.Counter()
    if p.suffix == '.csv':
        for r in csv.DictReader(p.open(encoding='utf-8')):
            e = norm(r.get('reading') or '')
            if e: vocab[e] += 1
        return vocab
    for line in p.read_text(encoding='utf-8').splitlines():
        if line.startswith('#'): continue
        parts = line.split('\t'); e = norm(parts[0])
        if e: vocab[e] += int(parts[1]) if len(parts) > 1 and parts[1].strip().isdigit() else 1
    return vocab

# ----------------------------------------------------------------------------------------------- frame solver

SUFFIXES = ['s', 'es', 'd', 'ed', 'n', 'en']


def cuts(word, gs, dom, vocab):
    """All element sequences that spell `word` with one element per group. Marks: ^ doubles the last letter,
    + lets a suffix follow."""
    out = []
    def rec(i, pos, acc):
        if i == len(gs):
            if pos == len(word): out.append(tuple(acc))
            return
        g, marks = gs[i]
        cand = dom.get(g); rest = word[pos:]
        if cand is None:
            cand = [rest[:k] for k in range(1, len(rest) + 1) if rest[:k] in vocab]
        for e in cand:
            piece = e + (e[-1] if '^' in marks else '')
            if not rest.startswith(piece): continue
            ends = [pos + len(piece)]
            if '+' in marks:
                ends += [pos + len(piece) + len(s) for s in SUFFIXES if rest[len(piece):].startswith(s)]
                if piece.endswith('e'):
                    ends += [pos + len(piece) - 1 + len(s) for s in ('ed', 'en', 'es') if rest[len(piece) - 1:].startswith(s)]
            for e2 in set(ends): rec(i + 1, e2, acc + [e])
    rec(0, 0, [])
    return out


def solve(words, vocab, fixed):
    dom = {g: {v} for g, v in fixed.items()}; log = []
    for rnd in range(30):
        changed = False; newdom = {}; failures = []
        for src, loc, w, gs in words:
            cs = cuts(w, gs, dom, vocab)
            if not cs: failures.append((src, loc, w, gs)); continue
            for i, (g, m) in enumerate(gs):
                s = {c[i] for c in cs}
                newdom[g] = newdom[g] & s if g in newdom else s
        for g, s in newdom.items():
            if not s: log.append(('empty', g)); continue
            if g not in dom or s != dom[g]:
                if g not in dom or len(s) < len(dom[g]): dom[g] = s; changed = True
        single = {next(iter(s)): g for g, s in dom.items() if len(s) == 1}
        for g, s in dom.items():
            if len(s) > 1:
                t = {e for e in s if single.get(e, g) == g}
                if t and t != s: dom[g] = t; changed = True
        if not changed: break
    return dom, failures, log

# ----------------------------------------------------------------------------------------------- key v1

def tok(t):
    m = re.fullmatch(r'(\d{1,4})([\^v+]*)', t.strip())
    if not m: return None
    return (int(m.group(1)), '+' if m.group(2) else '')        # caret, v and + all allow a suffix


def load_rows():
    """Rows of corpus/interlined_spans.tsv. Left out: ambiguous placement, a doubtful (?) or hidden (_) digit,
    an interlinear of two words. Unlabelled groups that follow a word are kept as possible continuations."""
    words, stats, trailing = [], collections.Counter(), {}
    last, cur_src = None, None
    with (HERE / 'corpus/interlined_spans.tsv').open(encoding='utf-8') as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            if r['source'] != cur_src: cur_src, last = r['source'], None     # a new transcription file
            groups = r['groups'].split(); stats['groups'] += len(groups)
            w = r['interlinear'].strip()
            if groups and not w:
                stats['no_word'] += len(groups)
                g2 = [tok(g) for g in groups]
                if last and all(g2): trailing.setdefault(last, []).extend(g2)
                else: last = None
                continue
            last = None
            if not groups: continue
            if r['placement'].strip().startswith('amb'): stats['ambiguous'] += len(groups); continue
            gs = [tok(g) for g in groups]
            if not all(gs): stats['doubtful_digit'] += len(groups); continue
            w2 = re.sub(r'[—–\-_.,;:]+\s*$', '', re.sub(r'\[.*?\]|\(.*?\)', '', w)).strip()
            if not w2 or ' ' in w2: stats['multiword_or_empty'] += len(groups); continue
            loc = f"{r['source']}|{r['frame']}:{r['page']}:{r['line']}:{r['span_no']}"
            words.append((r['source'], loc, norm(w2), gs)); last = loc
            stats['usable_groups'] += len(groups)
    return words, stats, trailing


def build(a):
    vocab = load_vocab(a.elements)
    words, stats, trailing = load_rows()
    direct = collections.defaultdict(collections.Counter)
    for src, loc, w, gs in words:
        if len(gs) == 1 and gs[0][1] == '': direct[gs[0][0]][w] += 1
    fixed, conflicts = {}, []
    for g, c in direct.items():
        top = c.most_common()
        if len(top) > 1:
            conflicts.append((g, dict(c)))
            if top[0][1] == top[1][1]: continue                         # a tie is not entered
        if top[0][0] in vocab or top[0][1] >= 2: fixed[g] = top[0][0]   # a lone off-list value is not entered
    own = collections.defaultdict(list)
    for g, v in fixed.items(): own[v].append(g)
    aside = []
    for v, gs in own.items():                                           # one word, one group: keep the best attested
        if len(gs) > 1:
            gs.sort(key=lambda g: -sum(direct[g].values()))
            lose = gs[1:] if sum(direct[gs[0]].values()) > sum(direct[gs[1]].values()) else gs
            for g in lose: aside.append((g, v, sum(direct[g].values()), gs[0])); fixed.pop(g)
    fx = {g: {v} for g, v in fixed.items()}; ext = 0; new = []
    for src, loc, w, gs in words:                                       # retry a word with the bare groups after it
        if loc in trailing and not (len(gs) == 1 and gs[0][1] == '' and gs[0][0] in fixed and fixed[gs[0][0]] == w) and not cuts(w, gs, fx, vocab):
            for k in range(1, len(trailing[loc]) + 1):
                if cuts(w, gs + trailing[loc][:k], fx, vocab):
                    gs = gs + trailing[loc][:k]; ext += 1; break
        new.append((src, loc, w, gs))
    words = new
    multi = [x for x in words if len(x[3]) > 1 or x[3][0][1] or x[3][0][0] not in fixed]
    dom, failures, log = solve(multi, vocab, fixed)
    solved = {g: next(iter(s)) for g, s in dom.items() if len(s) == 1 and g not in fixed}
    owners = collections.defaultdict(list)
    for g, v in list(fixed.items()) + list(solved.items()): owners[v].append(g)
    occ = collections.Counter(g for _, _, _, gs in multi for g, _ in gs)
    for e, gs in owners.items():
        if len(gs) > 1:
            if any(g in fixed for g in gs):
                for g in gs: solved.pop(g, None)
            else:
                gs2 = sorted(gs, key=lambda g: -occ[g])
                for g in (gs2[1:] if occ[gs2[0]] >= 3 and occ[gs2[0]] > occ[gs2[1]] else gs2): solved.pop(g, None)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    p = out / 'key_v1.tsv'
    with p.open('w') as f:
        f.write('group\tvalue\tgrade\tn\ton_element_list\n')
        for g in sorted(set(fixed) | set(solved)):
            if g in fixed: f.write(f"{g}\t{fixed[g]}\tD\t{sum(direct[g].values())}\t{'y' if fixed[g] in vocab else 'n'}\n")
            else: f.write(f"{g}\t{solved[g]}\t{'S2' if occ[g] >= 2 else 'S1'}\t{occ[g]}\ty\n")
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    summary = dict(transcription=dict(stats), words=len(words), direct=len(fixed),
                   direct_on_list=sum(1 for v in fixed.values() if v in vocab), solved=len(solved),
                   key_groups=len(fixed) + len(solved), direct_conflicts=len(conflicts), set_aside=aside,
                   unsegmentable=len(failures), words_extended=ext, sha256=h)
    (out / 'key_v1_summary.json').write_text(json.dumps(summary, indent=1) + '\n')
    with (out / 'key_v1_conflicts.tsv').open('w') as f:
        f.write('group\treadings\n')
        for g, c in sorted(conflicts): f.write(f"{g}\t{json.dumps(c)}\n")
    print(json.dumps({k: v for k, v in summary.items() if k != 'set_aside'}, indent=1))

# ----------------------------------------------------------------------------------------------- held-out score

def ordered_match(values, text, skipped_before):
    """Largest number of key values laid on `text` in order: a value must start within 12*(k+1) letters of the
    previous match's end, k = groups skipped since that match."""
    states = {0: {(0, 0)}}
    for i, v in enumerate(values):
        new = {}
        for m, st in states.items():
            for end, k in st:
                kk = k + skipped_before[i]
                new.setdefault(m, set()).add((end, kk + 1))
                lim = len(text) if m == 0 else end + 12 * (kk + 1)
                pos = text.find(v, end)
                while pos != -1 and pos <= lim:
                    new.setdefault(m + 1, set()).add((pos + len(v), 0))
                    pos = text.find(v, pos + 1)
                    if len(new[m + 1]) > 400: break
        states = {m: set(sorted(st)[:40]) for m, st in new.items()}
    return max(states)


def score_stretches(stretches, key, shuffles=200, seed=18021022):
    def run(k):
        matched = covered = total = 0
        for groups, truth in stretches:
            t = norm(truth); vals, skipped, s = [], [], 0
            for g in groups:
                total += 1
                if g in k and norm(k[g]): vals.append(norm(k[g])); skipped.append(s); s = 0
                else: s += 1
            covered += len(vals)
            if vals: matched += ordered_match(vals, t, skipped)
        return matched, covered, total
    m, c, t = run(key)
    rng = random.Random(seed); gl = sorted(key); vl = [key[g] for g in gl]; base = []
    for _ in range(shuffles):
        sh = vl[:]; rng.shuffle(sh)
        mm, cc, _ = run(dict(zip(gl, sh))); base.append(mm / cc if cc else 0.0)
    return dict(groups=t, covered=c, coverage=round(c / t, 3) if t else None, matched=m,
                score=round(m / c, 3) if c else None, shuffled_mean=round(sum(base) / len(base), 3),
                shuffled_max=round(max(base), 3))


def no59_truth():
    t = (HERE / 'test_no59/no59_department_clear.txt').read_text(encoding='utf-8')
    return t[t.index('Dear Sir') + len('Dear Sir'):]


def score(a):
    kp = Path(a.key)
    key = {int(r['group']): r['value'] for r in csv.DictReader(kp.open(), delimiter='\t')}
    groups = []
    for r in csv.DictReader((HERE / 'test_no59/no59_transcription.tsv').open(encoding='utf-8'), delimiter='\t'):
        for t in r['groups'].split():
            if '?' in t or '_' in t: groups.append(-1)       # hidden digit: an uncovered, skipped group
            else:
                d = re.sub(r'\D', '', t); groups.append(int(d) if d else -1)
    res = score_stretches([(groups, no59_truth())], key)
    res.update(key_sha256=hashlib.sha256(kp.read_bytes()).hexdigest(), key_groups=len(key))
    res['pass_rule'] = bool(res['score'] is not None and res['score'] >= 0.85 and res['score'] - res['shuffled_max'] >= 0.30)
    print(json.dumps(res, indent=1))

# ----------------------------------------------------------------------------------------------- alignment (key v2)

SUFF = ['s', 'es', 'd', 'ed', 'n', 'en', 'ing', 'ly']
MAXL = 14


def align(seq, text, key, vocab, owned, beam=400, free=False):
    """DP over (group, position in text): a known group lies on its letters or pays to skip; an unknown group takes
    the next 0-14 letters, cheapest when they form a list element no other number owns."""
    T = norm(text); n = len(seq)
    cur = {p: (0.0, None) for p in range(len(T))} if free else {0: (0.0, None)}
    back = []
    for i, it in enumerate(seq):
        nxt = {}
        def put(p2, c, p, L, kind):
            if p2 <= len(T) and (p2 not in nxt or c < nxt[p2][0]): nxt[p2] = (c, (p, L, kind))
        for p, (c, _) in cur.items():
            g = it['g']; v = key.get(g) if g is not None else None
            if v:
                if T.startswith(v, p):
                    put(p + len(v), c, p, len(v), 'hit')
                    if it['plus']:
                        for s in SUFF:
                            if T.startswith(s, p + len(v)): put(p + len(v) + len(s), c, p, len(v) + len(s), 'hit')
                        if v.endswith('e'):
                            for s in ('ed', 'en', 'es', 'ing'):
                                if T.startswith(s, p + len(v) - 1): put(p + len(v) - 1 + len(s), c, p, len(v) - 1 + len(s), 'hit')
                for L in range(0, MAXL + 1): put(p + L, c + 4.0 + 0.15 * L, p, L, 'miss')
            else:
                put(p, c + 1.3, p, 0, 'null')
                for L in range(1, MAXL + 1):
                    s = T[p:p + L]
                    if len(s) < L: break
                    if s in vocab and s not in owned: cc = 0.9 if L > 1 else 1.1
                    elif s in vocab: cc = 2.2
                    else: cc = 2.6 + 0.1 * L
                    put(p + L, c + cc, p, L, 'new')
                    if it['plus'] and s in vocab:
                        for sf in SUFF:
                            if T.startswith(sf, p + L): put(p + L + len(sf), c + cc, p, L, 'new+')
        keep = sorted(nxt.items(), key=lambda kv: kv[1][0])[:(max(beam, len(T)) if free and i < 40 else beam)]
        cur = dict(keep); back.append(dict(keep))
    end = min(cur, key=lambda p: cur[p][0] + (0.0 if free else 0.5 * (len(T) - p)))
    path = []; p = end
    for i in range(n - 1, -1, -1):
        c, (pp, L, kind) = back[i][p]; path.append((pp, L, kind)); p = pp
    path.reverse()
    return T, path, cur[end][0], end


def harvest(seq, T, path, key, vocab, owned):
    """Accept a value only if every occurrence took the same letters, it is an unowned list element, and each
    occurrence is pinned by exact hits on both sides, or it occurs twice or more."""
    cand = collections.defaultdict(list)
    for i, (it, (p, L, kind)) in enumerate(zip(seq, path)):
        if it['g'] is None or it['g'] in key or kind not in ('new', 'new+'): continue
        left = i > 0 and path[i - 1][2] == 'hit'
        right = i + 1 < len(path) and path[i + 1][2] == 'hit'
        cand[it['g']].append((T[p:p + L], left and right))
    acc = {}
    for g, obs in cand.items():
        vals = {v for v, _ in obs}
        if len(vals) != 1: continue
        v = next(iter(vals))
        if v not in vocab or v in owned: continue
        if all(p for _, p in obs) or len(obs) >= 2: acc[g] = (v, len(obs), sum(1 for _, p in obs if p))
    return acc, cand


def run_align(key, vocab, pairs, beam=400):
    owned = set(key.values()); accepted = {}; details = []
    for name, seq, text, *fr in pairs:
        T, path, cost, end = align(seq, text, key, vocab, owned, beam, free=bool(fr and fr[0]))
        acc, cand = harvest(seq, T, path, key, vocab, owned)
        details.append(dict(pair=name, groups=len(seq), text_letters=len(T), reached=end, cost=round(cost, 1),
                            kinds=dict(collections.Counter(k for _, _, k in path))))
        for g, v in acc.items():
            if g in accepted:
                if accepted[g] is not None and accepted[g][0] != v[0]: accepted[g] = None
            else: accepted[g] = v
    accepted = {g: v for g, v in accepted.items() if v}
    byv = collections.defaultdict(list)
    for g, (v, n, p) in accepted.items(): byv[v].append(g)
    for v, gs in byv.items():
        if len(gs) > 1:
            for g in gs: accepted.pop(g)
    return accepted, details


def seq_from_groups(tokens):
    out = []
    for t in tokens:
        d = re.sub(r'\D', '', t); ok = d and '?' not in t and '_' not in t
        out.append(dict(raw=t, g=int(d) if ok else None, plus=bool(re.search(r'[\^+v]', t))))
    return out


def align_cmd(a):
    vocab = {e for e in load_vocab(a.elements)}
    key = {int(r['group']): norm(r['value']) for r in csv.DictReader(open(a.key), delimiter='\t') if norm(r['value'])}
    rows = list(csv.DictReader((HERE / 'test_no59/no59_transcription.tsv').open(encoding='utf-8'), delimiter='\t'))
    pairs = [('No. 59, 23 Dec 1797', seq_from_groups([t for r in rows for t in r['groups'].split()]), no59_truth(), False)]
    pairs += [(x['name'], seq_from_groups(x['groups']), x['text'], True)
              for x in json.loads((HERE / 'checks/print_pairs.json').read_text(encoding='utf-8'))]
    grown, added = dict(key), {}
    for rnd in range(1, 6):
        acc, details = run_align(grown, vocab, pairs)
        new = {g: v for g, v in acc.items() if g not in grown}
        if not new: break
        for g, (v, n, p) in new.items(): grown[g] = v; added[g] = (v, n, p, rnd)
    present = sorted({it['g'] for _, seq, *_ in pairs for it in seq if it['g'] in key})
    rng = random.Random(17971223); hid = prop = right = 0
    for _ in range(10):                                         # calibration: hide a tenth of the key, ten times
        h = set(rng.sample(present, max(1, len(present) // 10)))
        k2 = {g: v for g, v in key.items() if g not in h}
        acc, _ = run_align(k2, vocab, pairs, beam=250)
        hid += len(h); prop += sum(1 for g in h if g in acc); right += sum(1 for g in h if g in acc and acc[g][0] == key[g])
    cal = dict(hidden=hid, accepted=prop, right=right, precision=round(right / prop, 3) if prop else None)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(open(a.key), delimiter='\t'))
    with (out / 'key_v2.tsv').open('w') as f:
        f.write('group\tvalue\tgrade\tn\ton_element_list\n')
        allr = [(int(r['group']), r['value'], r['grade'], r['n'], r['on_element_list']) for r in rows]
        allr += [(g, v, 'A', n, 'y') for g, (v, n, p, rd) in added.items()]
        for r in sorted(allr): f.write('\t'.join(map(str, r)) + '\n')
    res = dict(pairs=len(pairs), added=len(added), key_v1=len(key), key_v2=len(grown), calibration=cal,
               added_values={str(g): v[0] for g, v in sorted(added.items())})
    print(json.dumps(res, indent=1))

# ----------------------------------------------------------------------------------------------- decode

def decode(a):
    """Decode a transcription .txt: lines 'LABEL<TAB>content' where content mixes {clear words} and groups.
    Output per group: its value; <n> = no value; [?value] = grade I (context only); [n?] = doubtful digit."""
    key = {}
    for r in csv.DictReader(open(a.key), delimiter='\t'):
        key[int(r['group'])] = f"[?{r['value'].rstrip('?')}]" if r.get('grade') == 'I' else r['value']
    for line in Path(a.file).read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'): continue
        label, _, content = line.partition('\t')
        out = []
        for part in re.split(r'(\{[^}]*\})', content):
            if part.startswith('{'): out.append(part); continue
            for t in part.split():
                m = re.fullmatch(r'(\d{1,4}|\d*\?\d*)\.?([\^v+]*)\.?', t)
                if not m: out.append(t); continue
                g, marks = m.group(1), m.group(2)
                if '?' in g: out.append(f'[{g}]'); continue
                v = key.get(int(g))
                out.append((v if v else f'<{g}>') + (marks if marks else ''))
        print(f'{label}\t' + ' '.join(out))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    b = sub.add_parser('build'); b.add_argument('--elements', required=True); b.add_argument('--out', default='rebuild')
    s = sub.add_parser('score'); s.add_argument('--key', required=True)
    al = sub.add_parser('align'); al.add_argument('--elements', required=True); al.add_argument('--key', required=True); al.add_argument('--out', default='rebuild')
    d = sub.add_parser('decode'); d.add_argument('--key', required=True); d.add_argument('file')
    a = ap.parse_args()
    {'build': build, 'score': score, 'align': align_cmd, 'decode': decode}[a.cmd](a)
