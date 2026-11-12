"""Round 2 held-out test of key v2 on the round-2 lines (see ../PREREG_round2.md).

Run from beling/:  python3 -I scripts/test_key_v2.py
Writes results/test_key_v2_result.json and results/test_key_v2_output.txt. Standard library only.
"""
import collections, difflib, json, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / 'scripts'))
import build_key_v2 as b  # noqa: E402

SEED, N_SHUFFLE, PASS_SCORE, PASS_MARGIN = 15932, 200, 0.85, 0.30


def load_key(path):
    key = {}
    for row in (HERE / path).read_text(encoding='utf-8').splitlines():
        if row.strip() and not row.startswith('#'):
            v, s = row.split('\t')[:2]
            key[s] = None if v == '?' else ('' if v == 'null' else v)
    return {s: v for s, v in key.items() if v is not None}


def decode(toks, key):
    return ''.join('\x00' if (s is None or key.get(s) is None) else key[s] for _, _, s in toks)


def matched(d, T):
    sm = difflib.SequenceMatcher(None, d, T, autojunk=False)
    return sum(x.size for x in sm.get_matching_blocks())


def main():
    key = load_key('key/key_v2.tsv')
    tom = b.load_tomokiyo()
    letters = {L: (b.tokens('r2', L), b.copy_text(b.COPY_R2[L])) for L in ('406', '410')}

    def score(k):
        m = n = 0
        for toks, T in letters.values():
            d = decode(toks, k)
            m += matched(d, T)
            n += len(d)
        return m / n if n else 0.0

    true = score(key)
    signs = sorted(key)
    vals = [key[s] for s in signs]
    rng = random.Random(SEED)
    shuf = []
    for _ in range(N_SHUFFLE):
        v = vals[:]
        rng.shuffle(v)
        shuf.append(score(dict(zip(signs, v))))
    best = max(shuf)
    res = {'score': round(true, 4), 'best_shuffled': round(best, 4), 'mean_shuffled': round(sum(shuf) / len(shuf), 4),
           'margin': round(true - best, 4), 'pass': true >= PASS_SCORE and true - best >= PASS_MARGIN,
           'tokens_scored': sum(len(t) for t, _ in letters.values()), 'per_letter': {}, 'per_reader': {},
           'tomokiyo_round1_key_same_lines': round(score(tom), 4)}
    out = []
    per_reader = collections.defaultdict(lambda: [0, 0])
    for L, (toks, T) in letters.items():
        d = decode(toks, key)
        m = matched(d, T)
        unknown = sum(1 for _, _, s in toks if s is None or key.get(s) is None)
        res['per_letter'][L] = {'tokens': len(toks), 'decoded_chars': len(d), 'matched': m,
                                'score': round(m / len(d), 4) if d else 0, 'copy_chars': len(T),
                                'unknown_tokens': unknown, 'unknown_share': round(unknown / len(toks), 4) if toks else 0,
                                'lines': sorted({ln for _, ln, _ in toks}, key=lambda x: (x.split('.')[0], int(x.split('.')[1])))}
        for rd in sorted({r for r, _, _ in toks}):
            sub = [x for x in toks if x[0] == rd]
            ds = decode(sub, key)
            per_reader[rd][0] += matched(ds, T)
            per_reader[rd][1] += len(ds)
        out.append(f'== letter {L}')
        out.append('decrypted: ' + d.replace('\x00', '?'))
    res['per_reader'] = {rd: round(m / n, 4) if n else 0 for rd, (m, n) in per_reader.items()}
    (HERE / 'results' / 'test_key_v2_result.json').write_text(json.dumps(res, indent=1), encoding='utf-8')
    (HERE / 'results' / 'test_key_v2_output.txt').write_text(json.dumps(res, indent=1) + '\n\n' + '\n'.join(out) + '\n',
                                                             encoding='utf-8')
    print(json.dumps({k: res[k] for k in ('score', 'best_shuffled', 'mean_shuffled', 'margin', 'pass', 'tokens_scored',
                                          'per_reader', 'tomokiyo_round1_key_same_lines')}))


if __name__ == '__main__':
    main()
