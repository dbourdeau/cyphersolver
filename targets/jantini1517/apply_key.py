"""Apply Brice Dudout's reading key (dudout/key_K3v2_reading.json) to a column transcription in the notation of
t1126.txt / t1127.txt (upper/base per column; -/[x] = bracket sign).

    python apply_key.py t1127.txt > R1127_decryption.txt

Merges as in dudout/R1126_decryption.txt: '-/X -/9' -> X+9, '-/X -/y' -> X+y, '-/7 -/9' -> 9/7.
Output marks: ∅ = null, ‹x› = sign with no value in the key, … = lost or illegible on the leaf.
Check (14 Nov 2026): on dudout/R1126_transcription_v2.txt this reproduces 40 of the 43 lines of
dudout/R1126_decryption.txt exactly (v written u); the 3 others differ at u/1 (key 'vex', decryption 'ues') and at
the a+9 merge and a struck passage on p. 2 ll. 14 and 17, none of which occurs in R1127.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
KEY = json.loads((HERE / 'dudout' / 'key_K3v2_reading.json').read_text(encoding='utf8'))


def val(k):
    v = KEY.get(k)
    return '‹%s›' % k if v is None else ('∅' if v == '' else v)


def decode(tokens):
    out, i = [], 0
    while i < len(tokens):
        t = tokens[i].replace('?', '')
        nx = tokens[i + 1].replace('?', '') if i + 1 < len(tokens) else None
        if t.startswith('-/') and not t.startswith('-/[') and nx in ('-/9', '-/y'):
            k = '9/7' if (t == '-/7' and nx == '-/9') else t[2:] + '+' + nx[2:]
            if k in KEY:
                out.append(val(k)); i += 2; continue
        k = t[2:] if t.startswith('-/[') else t
        out.append('…' if ('#' in k or k == '…') else val(k))
        i += 1
    return ' '.join(out).replace('v', 'u')


if __name__ == '__main__':
    for line in open(sys.argv[1], encoding='utf8'):
        m = re.match(r'(R\d+ P\d+ L\d+): (.*)', line)
        if not m:
            continue
        body = re.sub(r'\[faded:[^\]]*\]|\([^)]*\)', ' … ', m.group(2))
        print(m.group(1), decode(body.split()))
