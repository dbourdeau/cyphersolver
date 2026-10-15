"""Build validation.tsv for docs/_validate.py from the System B (Łaski) letters (written 15 Oct 2026, when the
entry was split by key; the old validation.tsv here was R9414's and moved with it to targets/wardein1537/).

Pairs come from sysB/R9322_p1/_p2, R9323_p1 and R9417_p1/_p2.tsv, which align each cipher word with the word of the
contemporary interlinear gloss above it. Where the cipher word has exactly as many signs as the gloss word has
letters, sign i is paired with letter i; every other sign (unglossed words, words whose lengths differ, word signs
DAG/FLW/BIGX) is written '?'. So the reading tested is the gloss of the time, not this project's decode.
R9403 is left out: its sign codes were written from its reading with the key (r9403/build.py)."""
import io, os, re
H = os.path.dirname(os.path.abspath(__file__))
FILES = ['R9322_p1.tsv', 'R9322_p2.tsv', 'R9323_p1.tsv', 'R9417_p1.tsv', 'R9417_p2.tsv']
WORDSIGNS = {'DAG', 'FLW', 'BIGX'}
rows = []
for fn in FILES:
    for l in io.open(os.path.join(H, 'sysB', fn), encoding='utf8'):
        c = l.rstrip('\n').split('\t')
        if len(c) < 3 or not c[0].strip().isdigit():
            continue
        cw = [w for w in re.sub(r'\[(?!ins:)[^\]]*\]', '', c[1]).split()]
        gw = c[2].split()
        for i, w in enumerate(cw):
            w = re.sub(r'\[ins:([^\]]*)\]', r'\1', w)
            signs = [t.rstrip('?') for t in w.split('.') if t.rstrip('?') and t != "''"]
            if not signs:
                continue
            g = gw[i] if i < len(gw) else "''"
            g = re.sub(r'[^a-z]', '', g.lower()) if g != "''" else ''
            ok = g and len(g) == len(signs) and not (set(signs) & WORDSIGNS)
            for j, s in enumerate(signs):
                rows.append((s, g[j] if ok else '?'))
with io.open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf8') as f:
    f.write('# model: la\n')
    f.write('# source: sysB/R9322_p1/_p2, R9323_p1, R9417_p1/_p2.tsv cipher words paired with the contemporary gloss words of equal length (mk_validation.py)\n')
    f.write('# note: System B (Łaski) only; unglossed words, length mismatches and the word signs DAG/FLW/BIGX unread; R9403 left out (sign codes rebuilt from its reading)\n')
    for s, r in rows:
        f.write(f'{s}\t{r}\n')
print(len(rows), sum(r != '?' for _, r in rows))
