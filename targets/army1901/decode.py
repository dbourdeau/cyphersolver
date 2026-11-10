"""Independent decoder for the 1901 General Staff outgoing grid table (catalogue 715).
Rebuilt here from the rule stated by Harumi-Matsuba (issue #374); it does not import the contributor's code.
Read-only: prints to stdout, writes nothing.  Usage: python decode.py [ct_outgoing1901.txt]"""
import re, sys, pathlib

K = {'': 'アイウエオ', 'k': 'カキクケコ', 'g': 'ガギグゲゴ', 's': 'サシスセソ', 'z': 'ザジズゼゾ', 't': 'タチツテト',
     'd': 'ダヂヅデド', 'n': 'ナニヌネノ', 'h': 'ハヒフヘホ', 'b': 'バビブベボ', 'p': 'パピプペポ', 'm': 'マミムメモ',
     'y': 'ヤ?ユ?ヨ', 'r': 'ラリルレロ'}
T = {}
for v in range(5):
    for u, c in zip('123456789', ['', 'k', 'g', 's', 'z', 't', 'd', 'n', 'h']):
        T['%d%s' % (v, u)] = K[c][v]
    T['%d0' % (v + 1)] = K['b'][v]          # b column: 10 20 30 40 50
    for u, c in zip('1234', 'pmyr'):
        T['%d%s' % (v + 5, u)] = K[c][v]
T['55'] = 'ワ'
T['65'] = 'ン'

# Issue #371: serial table of the incoming telegrams (00-67), tested here against the outgoing drafts.
ROWS = ['ア カ ガ サ ザ タ ダ ナ ハ バ パ マ ヤ ラ ワ', 'イ キ ギ シ ジ チ ニ ヒ ビ ピ ミ リ',
        'ウ ク グ ス ズ ツ ヌ フ ブ プ ム ユ ル', 'エ ケ ゲ セ ゼ テ デ ネ ヘ ベ ペ メ レ',
        'オ コ ゴ ソ ゾ ト ド ノ ホ ボ ポ モ ヨ ロ ン']  # 00-67, as in issue #371 / READING1901.en.md
INC = {}
for r in ROWS:
    for k in r.split():
        INC['%02d' % len(INC)] = k


def runs(line):
    out, cur = [], []
    for t in line.split():
        if re.fullmatch(r'\d+', t):
            cur.append(t)
        elif cur:
            out.append(''.join(cur))
            cur = []
    if cur:
        out.append(''.join(cur))
    return out


def dec(d, tab):
    return ''.join(tab.get(d[i:i + 2], '[%s]' % d[i:i + 2]) for i in range(0, len(d), 2))


f = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).with_name('ct_outgoing1901.txt'))
tot = intab = inc = nruns = odd = 0
for line in f.read_text(encoding='utf-8').splitlines():
    if line.startswith('C0'):
        print(line)
        continue
    if not line.strip() or line.startswith('#'):
        continue
    for d in runs(line):
        nruns += 1
        odd += len(d) % 2
        p = [d[i:i + 2] for i in range(0, len(d), 2)]
        tot += len(p)
        intab += sum(x in T for x in p)
        inc += sum(x in INC for x in p)
        print('  %-40s %-22s | #371 table: %s' % (d, dec(d, T), dec(d, INC)))
print('runs %d (odd length %d), pairs %d, in grid table %d, inside #371 serial range %d' % (nruns, odd, tot, intab, inc))
