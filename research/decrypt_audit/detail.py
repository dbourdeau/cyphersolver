"""Show where a target's published text departs from its mechanical decrypt (companion of audit.py).

For each text of the target that audit.py can compare, prints the key file and tokenisation used, the departures
by kind (letters replaced, letters only in the reading, letters dropped inside a word), the commonest
decrypt -> reading replacements, and a sample of departures spread through the text, each with ten letters of
context on both sides: decrypt[gap]context  |  reading[gap]context.

Usage: python research/decrypt_audit/detail.py <folder> [samples per text, default 14]
"""
import os, sys, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit as A


def gaps(me, rd, marked):
    bl = [(o.src_start, o.dest_start, o.src_end - o.src_start) for o in A.LCSseq.opcodes(me, rd)
          if o.tag == 'equal' and o.src_end - o.src_start >= A.ANCHOR]
    for q, (i, j, n) in enumerate(bl[:-1]):
        i2, j2, _ = bl[q + 1]
        ga, gb = i2 - i - n, j2 - j - n
        if ga <= A.GAP and gb <= A.GAP and (ga or gb):
            yield i + n, i2, j + n, j2, any(marked[j + n:j2])


def main(folder, k=14):
    d = os.path.join(A.ROOT, 'targets', folder)
    o = json.load(open(os.path.join(d, 'profile.json'), encoding='utf8'))['outcome']
    tables, names = [], []
    for kf in A.as_list(o.get('key_file')):
        if not kf.startswith('http'):
            tt = A.key_tables(os.path.join(d, kf)); tables += tt; names.append(f'{kf} ({len(tt)} tables)')
    print(f'== {folder} | method: {o.get("method")} | class: {o.get("class")} | key files: {", ".join(names) or "none"}')
    for n, t in enumerate(o.get('texts') or []):
        pub = A.as_list(t.get('reading')) or A.as_list(t.get('decryption'))
        trans = A.as_list(t.get('transcription'))
        if t.get('state') == 'not prose' or not pub or not trans or not tables or set(pub) & set(trans):
            continue
        tt = [A.read(os.path.join(d, x)) for x in trans if not x.startswith('http')]
        pp = [A.read(os.path.join(d, x)) for x in pub if not x.startswith('http')]
        if not tt or not pp or any(x is None for x in tt + pp):
            continue
        rd, marked, word = A.reading_letters('\n'.join(pp))
        m = A.mechanical('\n'.join(tt), tables, rd)
        if m is None or m['coverage'] < 0.7:
            continue
        r = dict(coverage=m['coverage'])
        r.update(A.compare(m['letters'], rd, marked, word))
        if r['agreement'] < 0.6 or r['mech_letters'] < 100 or r['words'] < 30:
            continue
        me, rdc = m['letters'][:A.CAP], rd[:A.CAP]
        g = [x for x in gaps(me, rdc, marked[:len(rdc)])]
        un = [x for x in g if not x[4] and x[3] > x[2]]
        kinds = collections.Counter('only in reading' if a1 == a2 else 'replaced' for a1, a2, b1, b2, _ in un)
        subs = collections.Counter((me[a1:a2], rdc[b1:b2]) for a1, a2, b1, b2, _ in un if a2 - a1 <= 2 and b2 - b1 <= 2)
        print(f'-- text {n}: {t.get("label") or t.get("doc")} | state {t.get("state", "read")} | transcription {";".join(trans)[:60]} | published {";".join(pub)[:60]}')
        print(f'   scheme {m["scheme"]}, key covers {m["coverage"]:.0%}; {r["words_departing"]} of {r["words"]} words depart ({(r["word_rate"] or 0):.0%}); '
              f'gaps unmarked {len(un)} {dict(kinds)}, marked {sum(1 for x in g if x[4])}; decrypt found in reading {r["agreement"]:.0%}')
        print('   commonest short replacements: ' + ', '.join(f'{a or "-"}>{b}x{c}' for (a, b), c in subs.most_common(12)))
        step = max(1, len(un) // k)
        for a1, a2, b1, b2, _ in un[::step][:k]:
            print(f'     {me[max(0, a1 - 10):a1]}[{me[a1:a2]}]{me[a2:a2 + 10]}  |  {rdc[max(0, b1 - 10):b1]}[{rdc[b1:b2]}]{rdc[b2:b2 + 10]}')


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 14)
