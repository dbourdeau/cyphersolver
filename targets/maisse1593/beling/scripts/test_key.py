"""Held-out test of Tomokiyo's key for Maisse's Cipher 2 on fr. 16093 ff. 406 and 410 (see ../PREREG.md).

Run from the beling/ folder:  python3 -I scripts/test_key.py
Standard library only. Writes results/test_key_result.json and results/test_key_output.txt.
"""
import difflib, json, random, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
KEY = HERE / 'key' / 'tomokiyo_maisse2.tsv'
CIPHER = {'406': ['transcription/f406r_cipher.tsv', 'transcription/f406v_cipher.tsv'],
          '410': ['transcription/f410r_cipher.tsv']}
COPY = {'406': 'transcription/copy_406_from_cipher_start.txt',
        '410': 'transcription/copy_410_from_cipher_start.txt'}
FIRST_TEST_LINE = {'406r': 25, '406v': 1, '410r': 12}  # 406r: leaf numbering; WAINUT's l.17 = leaf l.24
LAST_TEST_LINE = {'406v': 20}
SEED, N_SHUFFLE, PASS_SCORE, PASS_MARGIN = 1593, 200, 0.85, 0.30


def load_key():
    key = {}
    for row in KEY.read_text(encoding='utf-8').splitlines():
        if not row.strip() or row.startswith('#'):
            continue
        value, sign = row.split('\t')[:2]
        key[sign] = '' if value == 'null' else value
    return key


def norm(text):
    text = unicodedata.normalize('NFD', text.lower())
    out = []
    for ch in text:
        if 'a' <= ch <= 'z':
            out.append({'j': 'i', 'v': 'u'}.get(ch, ch))
    return ''.join(out)


def token_sign(tok):
    if tok == '[?]':
        return None
    tok = tok.split('|')[0]
    return tok[:-1] if tok.endswith('?') and len(tok) > 1 else tok


def load_lines(path, page_filter=True):
    rows = []
    for row in (HERE / path).read_text(encoding='utf-8').splitlines():
        if not row.strip() or row.startswith('#'):
            continue
        parts = row.split('\t')
        page, line, toks = parts[0], parts[1], parts[2]
        note = parts[3] if len(parts) > 3 else ''
        try:
            n = int(''.join(c for c in line if c.isdigit()))
        except ValueError:
            continue
        rows.append((page, n, line, toks.split(), note))
    return rows


def is_test(page, n, line, note):
    low = (line + ' ' + note).lower()
    if 'wainut' in low or 'consistency' in low or 'short run' in low or 'inside clear' in low:
        return False
    if n < FIRST_TEST_LINE.get(page, 1):
        return False
    if page in LAST_TEST_LINE and n > LAST_TEST_LINE[page]:
        return False
    return True


def decode(tokens, key):
    out = []
    for t in tokens:
        s = token_sign(t)
        v = key.get(s) if s is not None else None
        out.append('?' if v is None else norm(v) if v else '')
    return ''.join(out)


def matched(d, T):
    sm = difflib.SequenceMatcher(None, d, T, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks())


def main():
    key = load_key()
    letters = {}
    for L, files in CIPHER.items():
        toks, used, other = [], [], []
        for f in files:
            for page, n, line, tk, note in load_lines(f):
                (used if is_test(page, n, line, note) else other).append((page, line))
                if is_test(page, n, line, note):
                    toks.extend(tk)
        copy_rows = (HERE / COPY[L]).read_text(encoding='utf-8').splitlines()
        T = norm(' '.join(r for r in copy_rows if not r.startswith('#')))
        letters[L] = (toks, T, used, other)

    def score(k):
        m = n = 0
        for L, (toks, T, _, _) in letters.items():
            d = decode(toks, k)
            m += matched(d.replace('?', '\x00'), T)
            n += len(d)
        return m / n if n else 0.0

    true = score(key)
    signs, vals = list(key), [key[s] for s in key]
    rng = random.Random(SEED)
    shuf = []
    for _ in range(N_SHUFFLE):
        v = vals[:]
        rng.shuffle(v)
        shuf.append(score(dict(zip(signs, v))))
    best = max(shuf)
    res = {'score': round(true, 4), 'best_shuffled': round(best, 4),
           'mean_shuffled': round(sum(shuf) / len(shuf), 4), 'margin': round(true - best, 4),
           'pass': true >= PASS_SCORE and true - best >= PASS_MARGIN,
           'signs_scored': sum(len(v[0]) for v in letters.values()),
           'lines_scored': {L: len(v[2]) for L, v in letters.items()},
           'per_letter': {}}
    lines_out = []
    for L, (toks, T, used, other) in letters.items():
        d = decode(toks, key)
        m = matched(d.replace('?', '\x00'), T)
        res['per_letter'][L] = {'signs': len(toks), 'decoded_chars': len(d), 'matched': m,
                                'score': round(m / len(d), 4) if d else 0, 'copy_chars': len(T),
                                'unknown': d.count('?')}
        lines_out.append(f'== letter {L}: lines scored {used[:1]}..{used[-1:]} ({len(used)}); not scored {other}')
        lines_out.append('decrypted: ' + d)
    (HERE / 'results' / 'test_key_result.json').write_text(json.dumps(res, indent=1), encoding='utf-8')
    (HERE / 'results' / 'test_key_output.txt').write_text(json.dumps(res, indent=1) + '\n\n' + '\n'.join(lines_out) + '\n',
                                                          encoding='utf-8')
    print(json.dumps({k: res[k] for k in ('score', 'best_shuffled', 'mean_shuffled', 'margin', 'pass', 'signs_scored')}))


if __name__ == '__main__':
    main()
