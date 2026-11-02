"""Every place in Mendelsohn 1937 where one of the telegrams' three-figure head groups occurs, with context."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
m = open('refs/m.txt', encoding='utf-8').read().split('\n')
heads = '017 010 018 692 693 405 406 378 437 435 425 732 971 177 400 991 135 149 963 556 157 564 119 943 961 967 370 865 753 916 414 777 819'.split()
for h in heads:
    hits = [i for i, l in enumerate(m) if re.search(r'(?<!\d)%s(?!\d)' % h, l)]
    print(h, len(hits))
    for i in hits[:6]:
        print('   ', i, ' | '.join(x.strip()[:60] for x in m[max(0, i-2):i+3]))
print('--- lines with Nr. or vom beside a three-figure group')
pat = re.compile(r'^\s*(\d{3})\s*$')
out = {}
for i, l in enumerate(m[:-1]):
    a = pat.match(l)
    if a and re.match(r'^\s*(Nr|vom|Nummer|Antwort|Im Anschluss|Telegramm|und\b|an\b)', m[i+1]):
        out.setdefault(a.group(1), set()).add(m[i+1].strip()[:40])
for k in sorted(out): print(k, sorted(out[k]))
