"""Merge the clear text of the transcription with the cipher reading (reading_aligned.txt) into one running text,
leaf by leaf; cipher passages are wrapped in ⟨ ⟩. Output: reading_merged.txt (to be edited into the reading .md)."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
read = {}; cur = None
for l in open(os.path.join(ROOT, 'reading_aligned.txt'), encoding='utf-8'):
    if l.startswith('#00'): cur = l[1:].strip(); read[cur] = ''; continue
    if cur and not l.startswith('# '): read[cur] += l.strip()
out = []
for leaf in ['0009r', '0009v', '0010r', '0010v', '0011r']:
    out.append(f'\n[f. {leaf[2:4].lstrip("0")}{leaf[4]}]')
    incipher = False
    for line in open(os.path.join(ROOT, 'transcription', leaf + '.txt'), encoding='utf-8'):
        m = re.match(r'^(L\d+\w?):\s*(.*)$', line.strip())
        if not m: continue
        for s in re.findall(r'\{[^}]*\}|[^\s{}]+', m.group(2)):
            if s.startswith('{') and not re.fullmatch(r'\{[/~^.].*', s):
                if incipher: out.append('⟩'); incipher = False
                out.append(s[1:-1])
            elif not incipher:
                run = f'{leaf} {m.group(1)}'
                out.append('⟨' + re.sub(r'\s*\|\s*', ' ', read.get(run, f'[run {run} missing]')).strip()); incipher = True
    if incipher: out.append('⟩')
open(os.path.join(ROOT, 'reading_merged.txt'), 'w', encoding='utf-8').write(re.sub(r' *\n *', '\n', ' '.join(out)))
