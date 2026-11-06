"""Count cipher words and signs in reading_89_142.txt: read, read with doubt, unread."""
import re, sys
path = sys.argv[1] if len(sys.argv) > 1 else 'reading_89_142.txt'
words = {'read': 0, 'doubt': 0, 'open': 0}
signs = dict(words)
clear = 0
for l in open(path, encoding='utf-8'):
    if l.startswith('#') or '|' not in l:
        continue
    for tok in [t.strip() for t in l.split('|')[1:]]:
        if tok.startswith('['):
            clear += len(tok.strip('[]').split())
            continue
        if tok.startswith('#') or '=' not in tok:
            continue
        c, r = tok.rsplit('=', 1) if tok.count('=') == 1 else (tok[:tok.rindex('=')], tok[tok.rindex('=') + 1:])
        k = 'open' if r.strip() in ('?', '') else ('doubt' if r.endswith('?') else 'read')
        words[k] += 1
        signs[k] += len(c)
tw, ts = sum(words.values()), sum(signs.values())
print(f'cipher words {tw}: read {words["read"]} ({100*words["read"]/tw:.1f}%), doubtful {words["doubt"]}, open {words["open"]}')
print(f'cipher signs {ts}: read {signs["read"]} ({100*signs["read"]/ts:.1f}%), doubtful {signs["doubt"]}, open {signs["open"]}')
print(f'read or doubtful: words {100*(words["read"]+words["doubt"])/tw:.1f}%, signs {100*(signs["read"]+signs["doubt"])/ts:.1f}%')
print(f'clear words (approx.): {clear}')
