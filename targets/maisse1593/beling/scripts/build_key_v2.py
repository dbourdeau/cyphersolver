"""Round 2: build key v2 from the round-1 lines and copies (rule in ../PREREG_round2.md, step 2).

  python3 -I scripts/build_key_v2.py         key v2 from round 1 only  -> key/key_v2.tsv, results/build_key_v2.txt
  python3 -I scripts/build_key_v2.py --all   full construction from round 1 + round 2 (exploratory, after the test)
                                             -> key/key_full.tsv, results/build_key_full.txt
Run from beling/. Standard library only.
"""
import collections, difflib, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
R1 = 'transcription/round1_catalogue/'
R2 = 'transcription/round2/'
# (reader, file, pages taken, first line per page)
SOURCES = {
    'r1': {'406': [('a', R1 + 'f406r_cipher.tsv', {'406r': 23}), ('b', R1 + 'f406v_cipher.tsv', {'406v': 1})],
           '410': [('c', R1 + 'f410r_cipher.tsv', {'410r': 10})]},
    'r2': {'406': [('d', R2 + 'f406v_411v_cipher.tsv', {'406v': 21})],
           '410': [('e', R2 + 'f410v_cipher.tsv', {'410v': 1}), ('f', R2 + 'f411r_cipher.tsv', {'411r': 1}),
                   ('d', R2 + 'f406v_411v_cipher.tsv', {'411v': 1})]},
}
COPY_R1 = {'406': 'transcription/copy_406_from_cipher_start.txt', '410': 'transcription/copy_410_from_cipher_start.txt'}
COPY_R2 = {'406': 'transcription/copy_round2_406.txt', '410': 'transcription/copy_round2_410.txt'}
R1_END = {'406': 'pourlouuerturedelaqlle', '410': 'suiuantlespromessesqueledgondy'}
ROUNDS = 6


def norm(text):
    import unicodedata
    out = []
    for ch in unicodedata.normalize('NFD', text.lower()):
        if 'a' <= ch <= 'z':
            out.append({'j': 'i', 'v': 'u'}.get(ch, ch))
    return ''.join(out)


def load_tomokiyo():
    key = {}
    for row in (HERE / 'key' / 'tomokiyo_maisse2.tsv').read_text(encoding='utf-8').splitlines():
        if row.strip() and not row.startswith('#'):
            value, sign = row.split('\t')[:2]
            key[sign] = '' if value == 'null' else norm(value)
    return key


def sign_of(tok):
    """Token rule (PREREG_round2): x? -> x; a|b -> a; #x, ^x, m:x -> x; -x (struck) -> '' (dropped); [?] -> None."""
    if tok in ('[?]', '?'):
        return None
    tok = tok.split('|')[0]
    if tok.startswith('-') and len(tok) > 1:
        return ''
    for p in ('m:', '#', '^'):
        if tok.startswith(p) and len(tok) > len(p):
            tok = tok[len(p):]
    if tok.endswith('?') and len(tok) > 1:
        tok = tok[:-1]
    return tok


def load_rows(path):
    rows = []
    for row in (HERE / path).read_text(encoding='utf-8').splitlines():
        if not row.strip() or row.startswith('#'):
            continue
        parts = row.split('\t')
        if len(parts) < 3:
            continue
        digits = ''.join(c for c in parts[1] if c.isdigit())
        if not digits:
            continue
        rows.append((parts[0].strip(), int(digits), parts[1], parts[2].split(), parts[3] if len(parts) > 3 else ''))
    return rows


def tokens(stage, L):
    out = []
    for reader, f, pages in SOURCES[stage][L]:
        for page, n, line, tk, note in load_rows(f):
            low = (line + ' ' + note).lower()
            if page not in pages or n < pages[page] or 'short run' in low or 'inside clear' in low or 'clear only' in low:
                continue
            for x in tk:
                s = sign_of(x)
                if s != '':
                    out.append((reader, f'{page}.{n}', s))
    return out


def copy_text(path):
    rows = [r for r in (HERE / path).read_text(encoding='utf-8').splitlines() if not r.startswith('#')]
    return norm(' '.join(rows))


def r1_copy(L):
    T = copy_text(COPY_R1[L])
    end = T.find(R1_END[L])
    assert end > 0, L
    return T[:end + len(R1_END[L])]


def attribute(toks, key, T):
    """Align the decryption to T; return for each token the copy substring it lines up with."""
    d, owner = [], []
    for i, (_, _, s) in enumerate(toks):
        v = key.get(s) if s is not None else None
        for ch in ('\x00' if v is None else v):
            d.append(ch)
            owner.append(i)
    got = [''] * len(toks)
    sm = difflib.SequenceMatcher(None, ''.join(d), T, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                got[owner[i1 + k]] += T[j1 + k]
        elif tag == 'replace':
            own = []
            for k in range(i1, i2):
                if not own or own[-1][0] != owner[k]:
                    own.append([owner[k], 0])
                own[-1][1] += 1
            pos = j1
            for n_, (o, cnt) in enumerate(own):
                take = (j2 - pos) if n_ == len(own) - 1 else round((j2 - j1) * cnt / (i2 - i1))
                got[o] += T[pos:pos + take]
                pos += take
        elif tag == 'insert':
            left = owner[i1 - 1] if i1 > 0 else None
            right = owner[i1] if i1 < len(owner) else None
            for o in (left, right):
                if o is not None and (toks[o][2] is None or key.get(toks[o][2]) is None) and j2 - j1 <= 6:
                    got[o] += T[j1:j2]
                    break
    return got


def score(toks, key, T):
    d = ''.join('\x00' if (s is None or key.get(s) is None) else key[s] for _, _, s in toks)
    sm = difflib.SequenceMatcher(None, d, T, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks()) / len(d) if d else 0.0


def collect(data, key):
    stats = collections.defaultdict(collections.Counter)
    readers = collections.defaultdict(set)
    for toks, T in data.values():
        for (rd, _, s), g in zip(toks, attribute(toks, key, T)):
            if s is not None:
                stats[s][g] += 1
                readers[s].add(rd)
    return stats, readers


def rule(stats, k1):
    new = dict(k1)
    for s, c in stats.items():
        n = sum(c.values())
        v, m = c.most_common(1)[0]
        if s in k1:
            if n >= 5 and m / n >= 0.5 and c[k1[s]] / n < 0.3:
                new[s] = v
        elif n >= 3 and m / n >= 0.6:
            new[s] = v
    return new


def main():
    full = '--all' in sys.argv
    k1 = load_tomokiyo()
    data = {L: (tokens('r1', L), r1_copy(L)) for L in ('406', '410')}
    if full:
        for L in ('406', '410'):
            toks, T = data[L]
            data[L] = (toks + tokens('r2', L), T + copy_text(COPY_R2[L]))
    key, log = dict(k1), []
    for r in range(ROUNDS):
        stats, _ = collect(data, key)
        new = rule(stats, k1)
        sc = {L: round(score(toks, new, T), 4) for L, (toks, T) in data.items()}
        changed = sorted(s for s in set(new) | set(key) if new.get(s) != key.get(s))
        log.append(f'round {r + 1}: in-sample score {sc}; changed {len(changed)}: {changed}')
        if not changed:
            break
        key = new
    stats, readers = collect(data, key)
    rows = [f'# Maisse Cipher 2, {"full construction (round 1 + round 2)" if full else "key v2 (round 1 only)"}, '
            'built by scripts/build_key_v2.py; rule in PREREG_round2.md step 2.',
            '# value ("?" = unknown, "null" = null)\tsign\tn\tshare of n taking the value\tTomokiyo\t'
            'other copy strings (top 4; "-" = nothing)\treaders']
    for s in sorted(set(stats) | set(key), key=lambda x: (-sum(stats[x].values()), x)):
        c = stats.get(s, collections.Counter())
        n = sum(c.values())
        v = key.get(s)
        share = c[v] / n if (n and v is not None) else 0
        others = ', '.join(f'{k or "-"}:{m}' for k, m in c.most_common(5) if k != v)[:90]
        rows.append(f'{"?" if v is None else (v or "null")}\t{s}\t{n}\t{share:.2f}\t'
                    f'{("null" if k1[s] == "" else k1[s]) if s in k1 else "-"}\t{others}\t{"".join(sorted(readers.get(s, ())))}')
    name = 'full' if full else 'v2'
    (HERE / 'key' / f'key_{name}.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    (HERE / 'results' / f'build_key_{name}.txt').write_text('\n'.join(log) + '\n\n' + '\n'.join(rows) + '\n',
                                                            encoding='utf-8')
    print('\n'.join(log))


if __name__ == '__main__':
    main()
