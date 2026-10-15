"""Decode R483 with the rebuilt key; compare with the clerk's interlinear; list cipher lines without interlinear."""
import json, re, glob, difflib
from pathlib import Path
from align483 import norm
ROOT = Path(__file__).resolve().parent
K = json.load(open(ROOT / 'R483_key_rebuilt.json', encoding='utf8'))
def dec(groups):
    return ''.join(K[g]['value'] if g in K and K[g]['of'] >= 2 else f'<{g}>' for g in groups)
tot = agree = 0; noP = 0; ng = 0; out = []
for f in sorted(glob.glob(str(ROOT / 'tr' / 'R483_p*.txt'))):
    out.append(f'[{Path(f).stem}]'); p = None
    for l in open(f, encoding='utf8'):
        if l.startswith('P:'): p = l[2:].strip()
        elif l.startswith('C:'):
            parts = re.split(r'(\{clear:[^}]*\})', l[2:].strip())
            txt = []
            for part in parts:
                if part.startswith('{'): txt.append('[' + part[7:-1].strip() + ']'); continue
                gs = [re.sub(r'\D', '', g) for g in part.split() if re.sub(r'\D', '', g)]
                if gs: txt.append(dec(gs)); ng += len(gs)
            line = ' '.join(txt); out.append(line)
            if p and p != '(none)':
                a = re.sub(r'<\d+>', '', ''.join(t for t in txt if not t.startswith('['))); b = norm(p)
                sm = difflib.SequenceMatcher(None, a, b); m = sum(x.size for x in sm.get_matching_blocks())
                tot += len(b); agree += m
                out.append('   clerk: ' + p)
            elif any(not t.startswith('[') for t in txt): noP += 1
            p = None
print(f'groups {ng}; clerk letters matched by key {agree}/{tot} = {agree/tot:.1%}; cipher lines without interlinear {noP}')
(ROOT / 'R483_key_read.txt').write_text('\n'.join(out) + '\n', encoding='utf8')
