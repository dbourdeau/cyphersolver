# House count for ercole1547 (Dan Bourdeau's review of PR #933, 27 Nov 2026): cipher words only, sure words only.
# Run from targets/ercole1547:  python3 -I scripts/house_count.py
# A word is a hole when it carries a hole mark ([?...], [?L4s], [?]) or a slip mark (word*): the README rule of
# 19 Nov 2026 counts only sure words as read. All 8 lines on c. 16v are cipher; the reading files hold no clear words.
# The checks were done with AI tools and no person checked each record by hand.
import re

def body(path):
    t = re.sub(r'<!--.*?-->', '', open(path, encoding='utf-8').read(), flags=re.S)
    return ' '.join(l for l in t.splitlines() if l.strip() and not l.startswith('#'))

def report(name, path):
    words = [re.sub(r'[,.;:]+$', '', w) for w in body(path).split()]
    words = [w for w in words if w]
    holes = [w for w in words if '[' in w or w.endswith('*')]
    n, h = len(words), len(holes)
    print(f'{name} ({path}): cipher_words {n} holes {h} read {n - h} read_share {(n - h) / n:.3f}')
    print('  holes: ' + ' '.join(holes))

report('pass 1, figure of record', 'reading.md')
report('pass 2 (v2), image re-check, same key', 'reading_v2.md')
