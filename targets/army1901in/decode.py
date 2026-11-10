"""Independent decoder for the 1901 incoming serial kana table (issue #371, Harumi-Matsuba).
Rebuilt here from the table as stated; does not import the contributor's code. Read-only, prints to stdout.
Usage: python decode.py            decode every ct_*.txt in this folder and compare with the expected kana
       python decode.py control    shuffled-table control on the two test telegrams (seed 1901, 1,000 tables)"""
import pathlib, random, sys

ROWS = ['ア カ ガ サ ザ タ ダ ナ ハ バ パ マ ヤ ラ ワ', 'イ キ ギ シ ジ チ ニ ヒ ビ ピ ミ リ',
        'ウ ク グ ス ズ ツ ヌ フ ブ プ ム ユ ル', 'エ ケ ゲ セ ゼ テ デ ネ ヘ ベ ペ メ レ',
        'オ コ ゴ ソ ゾ ト ド ノ ホ ボ ポ モ ヨ ロ ン']
T = {}
for r in ROWS:
    for k in r.split():
        T['%02d' % len(T)] = k
assert len(T) == 68


def load(f):
    """Lines: '<digits with spaces> = <expected kana>' ; '#' comments."""
    out = []
    for line in f.read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        d, _, exp = line.partition('=')
        out.append((d.replace(' ', ''), exp.strip()))
    return out


def dec(d, tab=T):
    return [tab.get(d[i:i + 2], '[%s]' % d[i:i + 2]) for i in range(0, len(d) - 1, 2)]


def agree(d, exp, tab=T):
    got = dec(d, tab)
    e = [] ; i = 0
    while i < len(exp):  # expected kana, with [nn] for off-table values
        if exp[i] == '[':
            j = exp.index(']', i); e.append(exp[i:j + 1]); i = j + 1
        else:
            e.append(exp[i]); i += 1
    return sum(1 for a, b in zip(got, e) if a == b and not a.startswith('[')), len(e)


here = pathlib.Path(__file__).parent
files = sorted(here.glob('ct_*.txt'))
if len(sys.argv) > 1 and sys.argv[1] == 'control':
    rnd = random.Random(1901)
    test = [r for f in files if f.stem in ('ct_C09122796200', 'ct_C09122806100') for r in load(f)]
    real = sum(agree(d, e)[0] for d, e in test)
    vals = list(T.values()); best = []
    for _ in range(1000):
        rnd.shuffle(vals)
        tab = dict(zip(T.keys(), vals))
        best.append(sum(agree(d, e, tab)[0] for d, e in test))
    print('test telegrams: real table %d kana agree; 1,000 shuffled tables max %d, mean %.2f' % (real, max(best), sum(best) / 1000))
    sys.exit()
tot = ok = 0
for f in files:
    print(f.stem[3:])
    for d, e in load(f):
        a, n = agree(d, e)
        ok += a; tot += n
        print('  %-30s %-16s expected %-16s %d/%d' % (d, ''.join(dec(d)), e, a, n))
print('pairs %d, agreeing with the expected kana %d' % (tot, ok))
