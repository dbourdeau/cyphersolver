"""Align Trezzo's sign transcription with a clear text using the soft-EM aligner of targets/duben1764/fb.py.

usage: python3 align.py <cipher.txt> <clear.txt> [iters] [skip_logp] [out.json]

Uses the exact-end aligner of targets/duben1764/fb.py unchanged: the cipher and the clear must start and end together.
The key of record (key_full_v1.json) is `python3 align.py c_full_aligned.txt t281_full.txt 25 -6 key_full_v1.json`.

Cipher lines are "<label> <tok> <tok> ..."; the line marks '|', '•', '∆' and '[blot]' are dropped and a trailing '?'
is removed. Superscripts are kept as part of the token (L^a and L^u are different signs). Clear lines starting with
'#' are comments; '[?]' marks are removed before normalising. Prints the top values of the 60 commonest signs and
writes {sign: [[value, weight], ...]} to out.json (default align_key.json).
"""
import collections, json, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'duben1764'))
import fb  # noqa: E402

DROP = {'|', '•', '∆', '[blot]'}


def load_tokens(path):
    out = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        line = re.sub(r'\[clear:[^\]]*\]', ' ', line)
        for t in line.split()[1:]:
            if t in DROP:
                continue
            out.append(t.rstrip('?'))
    return out


def load_clear(path):
    text = ' '.join(l for l in open(path, encoding='utf-8') if not l.startswith('#'))
    return fb.norm(re.sub(r'\[\?\]', '', text))


def main():
    t = load_tokens(sys.argv[1])
    s = load_clear(sys.argv[2])
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    skip = float(sys.argv[4]) if len(sys.argv) > 4 else -9.0
    print('tokens', len(t), 'types', len(set(t)), 'letters', len(s))
    key, *_ = fb.run(t, s, iters, skip)
    json.dump(key, open(sys.argv[5] if len(sys.argv) > 5 else 'align_key.json', 'w', encoding='utf-8'),
              indent=0, ensure_ascii=False)
    cnt = collections.Counter(t)
    for x, n in cnt.most_common(60):
        print(x, n, key[x])


if __name__ == '__main__':
    main()
