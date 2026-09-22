"""Build signs.txt (one character per cipher sign) from the transcription files and count the read bar.

Letters stay letters, nulls ".", name signs <N1>..<N4> -> 1..4, place sign <P1> -> 5, unread sign "?" -> "?".
Struck-through text in [..] and notes after "|" are dropped. One output line per manuscript line, with its id.
"""
import re, sys, pathlib

HERE = pathlib.Path(__file__).parent
FILES = ['transcription_f101.txt', 'transcription_f103.txt', 'transcription_f107.txt']


def signs(text):
    text = text.split('|')[0]
    text = re.sub(r'\[[^\]]*\]', '', text)
    text = re.sub(r'<N([1-4])>', r'\1', text).replace('<P1>', '5')
    return re.sub(r'[^a-z.?1-5]', '', text.lower())


out, tot = [], {'letter': 0, 'null': 0, 'name': 0, 'unread': 0}
for f in FILES:
    p = HERE / f
    if not p.exists():
        continue
    for line in p.read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        lid, _, rest = line.partition(' ')
        s = signs(rest)
        out.append(f'{lid} {s}')
        for c in s:
            tot['letter' if c.isalpha() else 'null' if c == '.' else 'name' if c.isdigit() else 'unread'] += 1
(HERE / 'signs.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
n = sum(tot.values())
print(tot, 'total', n, 'with value', n - tot['name'] - tot['unread'], f"{(n - tot['name'] - tot['unread']) / n:.4f}")
