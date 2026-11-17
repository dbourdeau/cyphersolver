"""Align the cipher groups of doc. 124, p. 2 ll. 1-2 (sample_transcription.txt, key_excerpt.tsv) with the clear
text of doc. 129, image 1 ll. 15-16 (dudout/doc129_transcription.txt and the two passes), and compare the clear
lines of doc. 124 p. 2 ll. 2-6 with doc. 129 word by word.

    python align_doc129.py        writes doc129_alignment.txt

Standard library only. Integration check of PR #623, 14 Nov 2026. Only the sample of doc. 124 is transcribed, so
only eight cipher groups fall inside the text doc. 129 has.
"""
import difflib, pathlib, random, re, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
KEY = {}
for line in (HERE / 'key_excerpt.tsv').read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or line.startswith('number'): continue
    n, roman, value, *_ = line.split('\t')
    KEY[int(n)] = value

def words(s):
    s = re.sub(r'<del>.*?</del>', '', s); s = re.sub(r'</?ins>', '', s).replace('[circled:]', '')
    s = re.sub(r'<[^>]*>', '', s)                      # cipher groups of doc. 124
    s = re.sub(r'\{([^}|]*)\|[^}]*\}', r'\1', s)       # first alternative of {a|b}
    s = re.sub(r'‹[^›]*›', ' ~ ', s).replace('[?]', ' ~ ')
    s = re.sub(r'[{}\[\]?]', '', s)
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if not unicodedata.combining(c)).replace('ç', 'c')
    out = []
    for w in re.findall(r'[a-z~]+', s):                # spelling and numerals levelled, nothing else
        w = w.replace('rr', 'r').replace('v', 'u').replace('y', 'i').replace('j', 'i').replace('ct', 't').replace('mp', 'np')
        w = {'hecho': 'fecho', 'xx': 'ueinte', 'xxi': 'ueinte e uno', 'xxii': 'ueinte e dos'}.get(w, w)
        out += w.split()
    return out

def pages(name):
    d = {}
    for line in (HERE / 'dudout' / name).read_text(encoding='utf-8').splitlines():
        m = re.match(r'(img0[12]\.\d\d)\s+(.*)', line)
        if m: d[m.group(1)] = words(m.group(2))
    return d

def flat(d, keys): return [w for k in keys for w in d[k]]
def same(a, b): return sum(k for _, _, k in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())

S, P1, P2 = pages('doc129_transcription.txt'), pages('doc129_pass1.txt'), pages('doc129_pass2_blind.txt')
out = ['# doc. 129 against doc. 124 (align_doc129.py). Words compared after levelling spelling (u/v, i/y/j, rr, ç,',
       '# ct/t, hecho/fecho) and writing the numerals xx, xxi, xxij out; first alternative of {a|b}.', '',
       '## 1. The two passes over doc. 129, pp. 1-2 (words that agree, in order)']
for label, x, y in (('pass 1 / pass 2 (blind)', P1, P2), ('settled / pass 1', S, P1), ('settled / pass 2 (blind)', S, P2)):
    for pg in ('img01', 'img02'):
        ks = sorted(k for k in S if k.startswith(pg)); a, b = flat(x, ks), flat(y, ks)
        out.append(f'{label:26s} {pg}: {same(a, b)} of {max(len(a), len(b))} words = {same(a, b) / max(len(a), len(b)):.3f}')

c124 = []
for line in (HERE / 'sample_transcription.txt').read_text(encoding='utf-8').splitlines():
    if re.match(r'p2\.[2-6]', line): c124 += words(line.split(None, 1)[1])
c124 = c124[c124.index('partio'):]
ks = ['img01.16', 'img01.17'] + ['img02.%02d' % i for i in range(1, 11)]
out += ['', '## 2. The clear lines of doc. 124 (p. 2 ll. 2-6, from "partio de aca" to "cargo dello") in doc. 129',
        f'doc. 124: {len(c124)} words (the unread word after "mayo" counted as one)']
for label, d in (('settled text', S), ('pass 1', P1), ('pass 2 (blind)', P2)):
    w = flat(d, ks); w = w[w.index('partio'):]
    out.append(f'doc. 129 {label:15s}: {same(c124, w)} of {len(c124)} words of doc. 124 found in order = {same(c124, w) / len(c124):.3f}')
    if d is S:
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, c124, w, autojunk=False).get_opcodes():
            if op != 'equal': out.append(f'    doc. 124 {" ".join(c124[i1:i2]) or "-"}  |  doc. 129 {" ".join(w[j1:j2]) or "-"}')

groups = [1813, 852, 868, 1221, 638, 29, 1885, 855]   # doc. 124 p. 2 ll. 1-2, between "dezia sea hecho" and "partio de aca"
clear = ['porque', '{desde|despues}', '{alli|aca}', 'en', 'fin', 'de', 'abril', 'que', 'el dotor']   # doc. 129 img01.15-16

def hit(v, c): return v.lower() == c or (v.lower().startswith('dotor') and 'dotor' in c)
def score(key, shift=0):
    cl = clear[::-1][shift:] if shift >= 0 else [''] * (-shift) + clear[::-1]
    return sum(1 for g, c in zip(groups[::-1], cl) if g in key and hit(key[g], c))

out += ['', '## 3. The cipher groups of doc. 124 p. 2 ll. 1-2 against doc. 129 img01.15-16',
        'doc. 124: dezia sea hecho . <1813> <852?> <868> <1221?> <638> <29?> <1885> <855> . partio de aca',
        'doc. 129: dezis sea fecho porque {desde|despues} {alli|aca} en fin de abril que el dotor partio de aca',
        'Eight groups, nine words or units; aligned from the right (the last group against "el dotor"):']
for g, c in zip(groups[::-1], clear[::-1]):
    out.append(f'  {g:5d}  key: {KEY.get(g, "(not in key_excerpt.tsv)"):26s} doc. 129: {c}')
out.append('  (left over at the head of doc. 129: "porque"; from the left, 1813 stands against it)')
out.append(f'groups with a value in the key excerpt: {sum(g in KEY for g in groups)}; agreeing with doc. 129: {score(KEY)}')
for s in (-2, -1, 1, 2): out.append(f'control, alignment moved by {s:+d} word(s): {score(KEY, s)} agree')
random.seed(1495); vals, nums, dist = list(KEY.values()), list(KEY), {}
for _ in range(10000):
    random.shuffle(vals); s = score(dict(zip(nums, vals))); dist[s] = dist.get(s, 0) + 1
out.append('control, 10000 shuffles of the 16 values of the key excerpt over its 16 numbers (seed 1495): '
           + ', '.join(f'{k} agree {v} times' for k, v in sorted(dist.items())))
(HERE / 'doc129_alignment.txt').write_text('\n'.join(out) + '\n', encoding='utf-8', newline='\n')
print('\n'.join(out))
