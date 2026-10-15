"""Word count of the cipher runs of R9367 in r9367/reading.txt (written 15 Oct 2026 when the entry was split from
kaa4591). Only the {..} runs (decoded cipher) are counted, on the L.. and P. lines; a word counts as unread if it
holds '_', '?', '[#]', '(' or '.', or is a single letter (the runs on L01-L02 and L07 are
letter strings without sense). Strict and rough: the reading itself is a working reading."""
import io, os, re
H = os.path.dirname(os.path.abspath(__file__))
n = k = 0
for l in io.open(os.path.join(H, 'r9367', 'reading.txt'), encoding='utf8'):
    if not re.match(r'(L\d\d|P\d) ', l):
        continue
    line = re.split(r'\s{2,}~|\s{3,}\(', l)[0]
    for run in re.findall(r'\{([^}]*)\}', line):
        for w in run.split():
            n += 1
            if re.search(r'[_?(.\[]', w) or len(w) == 1:
                continue
            k += 1
print(f'{k}/{n} words of the cipher runs = {k / n:.1%}')
