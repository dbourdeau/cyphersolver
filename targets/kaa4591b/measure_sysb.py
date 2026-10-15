"""Word count of the System B (Łaski) decodes, written 15 Oct 2026 when the entry was split by key.

Counts the words of sysB/decoded.txt (R9322 f.121-122, R9417 f.264) and sysB/R9323_decoded.txt (R9323 f.123).
A word counts as unread if it holds '?' or is a sign without a settled value ([F]/[FLW] the flower sign, [I], [Y],
[XC], [struck]). The word signs [D]/[DAG] (King John) and [X]/[BIGX] (Ferdinand) count as read. Words in capitals in
decoded.txt are clear text in the letter and are not counted. These are machine decodes with the gloss key, not hand
readings: letter slips inside a word (e/r confusions such as 'feancie' for 'francie' on R9417 P1) are counted as read
when the word is recognisable, so the figure is generous; R9403 is measured separately in r9403/decoded.txt.
Run: python measure_sysb.py"""
import io, os, re
H = os.path.dirname(os.path.abspath(__file__))
READ_SIGNS = {'[D]', '[DAG]', '[X]', '[BIGX]'}

def count(lines):
    n = k = 0
    for l in lines:
        for w in l.split():
            if w.isupper() and w.isalpha():
                continue                      # clear text
            n += 1
            if w in READ_SIGNS:
                k += 1
            elif '?' in w or w.startswith('['):
                pass
            else:
                k += 1
    return n, k

rec = {}
cur = None
for l in io.open(os.path.join(H, 'sysB', 'decoded.txt'), encoding='utf8'):
    if l.startswith('=='):
        cur = l.split()[1][:5]
        continue
    m = re.match(r'\s*\d+\s+(.*)', l)
    if cur and m:
        rec.setdefault(cur, []).append(m.group(1))
for l in io.open(os.path.join(H, 'sysB', 'R9323_decoded.txt'), encoding='utf8'):
    m = re.match(r'(\d+):\s*(.*)', l)
    if m:
        rec.setdefault('R9323', []).append(m.group(2))
tn = tk = 0
for r in sorted(rec):
    n, k = count(rec[r])
    tn += n; tk += k
    print(f'{r}: {k}/{n} words = {k / n:.1%}')
print(f'all System B decodes: {tk}/{tn} = {tk / tn:.1%}')
