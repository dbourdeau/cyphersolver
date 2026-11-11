"""Code 16: align bare code groups to a printed decipherment and read off new values.

Input pairs (groups from Bourdeau's transcription of NARA M30 roll 2, pin c14c822; text from the editions
saved in sources/raw/pinckney_edition_texts_2026-11-10):
    15 Aug 1793   frames 0135-0136   Jefferson Papers 26 (the coded part: from note 1 to "...strongly relied upon.")
    5 Jul 1793    frames 0106-0107   Jefferson Papers 26 (the two italic passages)

Method: dynamic programming over (group, position in text).  A group with a known value must lie on its
letters (free of charge), or pays to skip.  An unknown group takes the next 0-14 letters: cheapest when they
form an element of Weber's 1600-element list that no other number owns.  A '+' mark lets an inflection follow.
The cheapest path is the alignment.

A value is ACCEPTED for an unknown group only if: it is a list element nobody owns; every occurrence of the
group in the aligned material took the same letters; and at each occurrence the groups on both sides were
known groups lying exactly on their own letters (so the gap is pinned on both sides), or it occurs twice or more.

Calibration (reported, not tuned): the same procedure with a random tenth of the known key hidden, ten times;
share of hidden groups for which a value is accepted, and share of accepted values that are right.
"""
from pathlib import Path
import csv, json, re, random, collections, importlib.util, sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/code16_merged_2026-11-10'
ED = ROOT / 'sources/raw/pinckney_edition_texts_2026-11-10'
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha())
SUFF = ['s', 'es', 'd', 'ed', 'n', 'en', 'ing', 'ly']
MAXL = 14


def load_vocab():
    v = set()
    for l in (ROOT / 'sources/raw/weber_ill_2026-11-10/weber_1600_family_vocab.txt').read_text().splitlines():
        if not l.startswith('#'):
            e = norm(l.split('\t')[0])
            if e: v.add(e)
    return v


def load_key(path):
    return {int(r['group']): norm(r['value']) for r in csv.DictReader(open(path), delimiter='\t') if norm(r['value'])}


def frames(names):
    p = ROOT / 'sources/raw/reconstruction_2026-11-06/repo/targets/legation1788/transcription/pinckney_m30.tsv'
    rows = list(csv.DictReader([l for l in p.open() if not l.startswith('#')], delimiter='\t'))
    out = []
    for r in rows:
        if r['frame'] in names:
            g = r['group'].strip()
            d = re.sub(r'\D', '', g)
            out.append(dict(frame=r['frame'], line=r['line'], pos=r['position'], raw=g,
                            g=int(d) if d and '?' not in g else None, plus='+' in g))
    return out


def text_aug15():
    t = (ED / '1793-08-15_TP_to_Jefferson_FO.txt').read_text()
    b = t.split('=' * 20)[-1]
    i = b.index('[1]'); j = b.index('Our mint will receive', i)
    return re.sub(r'\[[^\]]*\]', ' ', b[i + 3:j])


def text_jul5():
    t = (ED / '1793-07-05_TP_to_Jefferson_FO.txt').read_text()
    b = t.split('=' * 20)[-1]
    b = b[:b.index('RC (DNA')]
    b = re.sub(r'\[(?:\d+|page break[^\]]*)\]', ' ', b)
    return ' '.join(m.group(1) for m in re.finditer(r'_([^_]+)_', b))


def text_tagged(fn):
    """Rotunda small capitals: join from the first to the last tagged passage, dropping the tags (initial capitals sit outside them)."""
    t = (ED / fn).read_text(); b = t.split('=' * 20)[-1]
    i = b.index('[[CIPHER>'); j = b.rindex('<CIPHER]]')
    return re.sub(r'\[\[CIPHER>|<CIPHER\]\]|\[\d+\]', ' ', b[i:j])


def text_body(fn, start, stop):
    t = (ED / fn).read_text(); b = t.split('=' * 20)[-1]
    i = b.index(start); j = b.index(stop, i)
    return re.sub(r'\[\[CIPHER>|<CIPHER\]\]|\[[^\]]*\]', ' ', b[i:j])


def align(seq, text, key, vocab, owned, beam=400, free=False):
    T = norm(text); n = len(seq)
    # states: pos -> (cost, backpointer); free=True lets the groups start and stop anywhere in the text
    cur = {p: (0.0, None) for p in range(len(T))} if free else {0: (0.0, None)}
    back = []
    for i, it in enumerate(seq):
        nxt = {}
        def put(p2, c, p, L, kind):
            if p2 <= len(T) and (p2 not in nxt or c < nxt[p2][0]): nxt[p2] = (c, (p, L, kind))
        for p, (c, _) in cur.items():
            g = it['g']
            v = key.get(g) if g is not None else None
            if v:
                if T.startswith(v, p):
                    put(p + len(v), c, p, len(v), 'hit')
                    if it['plus']:
                        for s in SUFF:
                            if T.startswith(s, p + len(v)): put(p + len(v) + len(s), c, p, len(v) + len(s), 'hit')
                        if v.endswith('e'):
                            for s in ('ed', 'en', 'es', 'ing'):
                                if T.startswith(s, p + len(v) - 1): put(p + len(v) - 1 + len(s), c, p, len(v) - 1 + len(s), 'hit')
                for L in range(0, MAXL + 1):                 # known value does not fit here: pay
                    put(p + L, c + 4.0 + 0.15 * L, p, L, 'miss')
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
        # beam: keep states near the cheapest
        keep = sorted(nxt.items(), key=lambda kv: kv[1][0])[:(max(beam, len(T)) if free and i < 40 else beam)]
        cur = dict(keep); back.append(dict(keep))
    # end: prefer finishing at the end of the text
    end = min(cur, key=lambda p: cur[p][0] + (0.0 if free else 0.5 * (len(T) - p)))
    path = []; p = end
    for i in range(n - 1, -1, -1):
        c, (pp, L, kind) = back[i][p]
        path.append((pp, L, kind)); p = pp
    path.reverse()
    return T, path, cur[end][0], end


def harvest(seq, T, path, key, vocab, owned):
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
        if all(p for _, p in obs) or len(obs) >= 2:
            acc[g] = (v, len(obs), sum(1 for _, p in obs if p))
    return acc, cand


def run(key, vocab, pairs, beam=400):
    owned = set(key.values())
    total = collections.Counter(); accepted = {}; details = []
    for name, seq, text, *fr in pairs:
        T, path, cost, end = align(seq, text, key, vocab, owned, beam, free=bool(fr and fr[0]))
        kinds = collections.Counter(k for _, _, k in path)
        acc, cand = harvest(seq, T, path, key, vocab, owned)
        details.append(dict(pair=name, groups=len(seq), text_letters=len(T), reached=end, cost=round(cost, 1), kinds=dict(kinds)))
        for g, v in acc.items():
            if g in accepted:
                if accepted[g] is not None and accepted[g][0] != v[0]: accepted[g] = None      # two letters disagree: drop
            else: accepted[g] = v
    accepted = {g: v for g, v in accepted.items() if v}
    # one element, one number
    byv = collections.defaultdict(list)
    for g, (v, n, p) in accepted.items(): byv[v].append(g)
    for v, gs in byv.items():
        if len(gs) > 1:
            for g in gs: accepted.pop(g)
    return accepted, details


def main():
    vocab = load_vocab()
    key = load_key(OUT / 'code16_key_v3.tsv')
    pairs = [('1793-08-15 frames 0135-0136', frames({'0135', '0136'}), text_aug15()),
             ('1793-07-05 frames 0106-0107', frames({'0106', '0107'}), text_jul5()),
             ('1795-02-23 frame 0305', frames({'0305'}), text_tagged('1795-02-23_TP_to_Randolph_PNKY.txt'), True),
             ('1795-04-03 frame 0317', frames({'0317'}), text_tagged('1795-04-03a_TP_to_Randolph_PNKY.txt'), True),
             ('1793-12-17 frame 0183', frames({'0183'}), text_tagged('1793-12-17_TP_to_Jefferson_PNKY.txt'), True),
             ('1794-01-28 frame 0196', frames({'0196'}), text_body('1794-01-28b_TP_to_Randolph_PNKY.txt', 'In addition to my letter', 'TP’s letter of 10 January'), True)]
    rounds = []; grown = dict(key); added = {}
    for rnd in range(1, 6):
        accepted, details = run(grown, vocab, pairs)
        new = {g: v for g, v in accepted.items() if g not in grown}
        rounds.append(dict(round=rnd, new=len(new), pairs=details))
        if not new: break
        for g, (v, n, p) in new.items():
            grown[g] = v; added[g] = (v, n, p, rnd)
    # calibration on the first round's conditions: hide a tenth of the starting key that occurs in these frames
    present = sorted({it['g'] for _, seq, *_ in pairs for it in seq if it['g'] in key})
    rng = random.Random(20261110); hid = prop = right = 0
    for _ in range(10):
        h = set(rng.sample(present, max(1, len(present) // 10)))
        k2 = {g: v for g, v in key.items() if g not in h}
        acc, _ = run(k2, vocab, pairs, beam=250)
        hid += len(h); prop += sum(1 for g in h if g in acc); right += sum(1 for g in h if g in acc and acc[g][0] == key[g])
    cal = dict(hidden=hid, accepted=prop, right=right, recall=round(prop / hid, 3), precision=round(right / prop, 3) if prop else None)
    with (OUT / 'code16_aligned_values.tsv').open('w') as f:
        f.write('group\tvalue\toccurrences\tpinned_both_sides\tround\n')
        for g in sorted(added): f.write(f"{g}\t{added[g][0]}\t{added[g][1]}\t{added[g][2]}\t{added[g][3]}\n")
    # key v4 = v3 + aligned values (grade A)
    rows = list(csv.DictReader(open(OUT / 'code16_key_v3.tsv'), delimiter='\t'))
    with (OUT / 'code16_key_v4.tsv').open('w') as f:
        f.write('group\tvalue\tgrade\tn\tsources\ton_element_list\n')
        allr = [(int(r['group']), r['value'], r['grade'], r['n'], r['sources'], r['on_element_list']) for r in rows]
        allr += [(g, v, 'A', n, f'aligned round {rd}', 'y') for g, (v, n, p, rd) in added.items()]
        for r in sorted(allr): f.write('\t'.join(map(str, r)) + '\n')
    # coverage of the aligned frames before and after
    def cov(k):
        tot = hit = 0
        for _, seq, *_ in pairs:
            for it in seq:
                tot += 1; hit += it['g'] in k
        return round(hit / tot, 3)
    res = dict(rounds=rounds, added=len(added), key_v3=len(key), key_v4=len(grown), coverage_v3=cov(key), coverage_v4=cov(grown), calibration=cal)
    (OUT / 'code16_alignment_summary.json').write_text(json.dumps(res, indent=1) + '\n')
    print(json.dumps({k: v for k, v in res.items() if k != 'rounds'}, indent=1))
    for r in rounds: print(r['round'], r['new'], [(d['pair'][:10], d['kinds']) for d in r['pairs']])


if __name__ == '__main__':
    main()
