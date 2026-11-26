"""Check marked_DCXXI.6.588.1.txt against the decryption and count words by the strict rule:
a word with any repaired or supplied letter ({x/y}) or an unidentified stretch ([?..], [... ]) is a hole.
python scripts/count_words.py"""
import re, sys, os
sys.stdout.reconfigure(encoding='utf-8')
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dec = {}
for l in open(os.path.join(here, 'decryption_DCXXI.6.588.1.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    i, p, d = l.rstrip('\n').split('\t'); dec[i] = d.replace('/', '')
clean = holes = est = 0; bad = []; stretches = []
for l in open(os.path.join(here, 'marked_DCXXI.6.588.1.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    i, m = l.rstrip('\n').split('\t')
    m1 = m.replace('|', '').replace(' ', '')
    # rebuild the key's letters from the marks
    letters = re.sub(r'\{([^/]*)/[^}]*\}', r'\1', m1)
    letters = re.sub(r'\[\.\.\.extentunknown:([^\]]*)\]', r'\1', letters).replace('/', '')
    letters = re.sub(r'\[\?([^\]]*)\]', r'\1', letters)
    if letters != dec[i]: bad.append(i)
    toks = re.findall(r'\[[^\]]*\]|\S+', m.replace(' | ', ' ').replace('|', ''))
    for t in toks:
        if '{' in t or t.startswith('['):
            holes += 1
            if t.startswith('[... extent unknown:'):
                stretches.append(len(re.sub(r'[^A-ZÑ?]', '', t.split(':', 1)[1])))
        else:
            clean += 1; est += len(t)
print('runs', len(dec), 'mismatches', bad or 'none')
avg = est / clean
extra = sum(max(1, round(n / avg)) - 1 for n in stretches)
print(f'minimum (each stretch of unknown extent = 1 word): word places {clean+holes}: clean {clean}, holes {holes}, share {clean/(clean+holes):.3f}')
print(f'estimated (each such stretch = its letters / {avg:.2f}, the mean letters per clean word): word places {clean+holes+extra}: clean {clean}, holes {holes+extra}, share {clean/(clean+holes+extra):.3f}')
