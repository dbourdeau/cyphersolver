"""R23 b4 (16 Nov 2026): read share over cipher words only, for readings whose source file marks the clear words
in <angle> brackets but whose reading does not.

    python research/reading_audit/r23_angle_split.py catinat1691      # the seven letters, clear words from letters/L*.txt
    python research/reading_audit/r23_angle_split.py laigue1649       # no. 43, clear words from n43/body_assembled.txt

Each run of consecutive <clear> words is looked up in the reading, letters compared without spaces, accents or
punctuation (so the reading's word division does not matter), and masked. What is left is the cipher. Both sides are
scored with the v2_score hole rules (holes by words; an apostrophe word is one word). Runs that cannot be found are
printed; they stay on the cipher side unless removed by hand (the NOTES say which).
"""
import re, sys, unicodedata, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research' / 'reading_audit')); sys.path.insert(0, str(ROOT / 'docs'))
import v2_score as v2
WORD = re.compile(r'[^\W\d_]+')


def count(s):
    s = re.sub(r"(?<=\w)['’](?=\w)", '', s)
    b = v2.holes(s)
    h = b.count('[?]'); d = len(re.findall(r'\(\?\)', b))
    w = len(WORD.findall(b.replace('[?]', ' ').replace('(?)', ' ')))
    return w, h, d


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalpha())


def runs_of(tokens):
    runs, cur = [], []
    for t in tokens:
        if t.startswith('<') and t not in ('<CANCEL>', '<->', '<*>'):
            cur.append(t[1:-1])
        elif t in ('<->',) or (cur and re.fullmatch(r'\d+(er)?', t) and not re.fullmatch(r'\d{2,3}', t)):
            if t != '<->': cur.append(t)          # a printed date figure inside a clear run
        else:
            if cur: runs.append(' '.join(cur)); cur = []
    if cur: runs.append(' '.join(cur))
    return runs


def split(text, runs, window=None):
    nb, idx = [], []
    for k, c in enumerate(text):
        for ch in norm(c): nb.append(ch); idx.append(k)
    nbs = ''.join(nb); mask = [False] * len(text); pos = 0; miss = []
    for r in runs:
        key = norm(r)
        if not key: continue
        j = nbs.find(key, pos)
        if j < 0 and window is None: j = nbs.find(key)
        if j < 0 or (window is not None and j - pos > window): miss.append(r); continue
        for k in range(idx[j], idx[j + len(key) - 1] + 1): mask[k] = True
        pos = j + len(key)
    clear = ''.join(c if m else ' ' for c, m in zip(text, mask))
    ciph = ''.join(' ' if m else c for c, m in zip(text, mask))
    return clear, ciph, miss


def report(name, text, clear, ciph, miss):
    W, C, X = count(text), count(clear), count(ciph)
    share = (X[0] - X[2]) / (X[0] + X[1]) if X[0] + X[1] else 0
    print(f'{name}: whole {W[0]} words {W[1]} holes | clear {C[0]} words {C[1]} holes | cipher {X[0]} words read, '
          f'{X[1]} holes, {X[2]} doubtful, share {share:.4f}' + (f' | runs not found: {miss}' if miss else ''))


def catinat():
    D = ROOT / 'targets' / 'catinat1691' / 'letters'
    for i in range(1, 8):
        grp = (D / f'L{i}.txt').read_text(encoding='utf8').split('## Groups as printed', 1)[1]
        runs = runs_of(re.findall(r'<[^>]*>|\S+', grp))
        rd = (D / f'L{i}_reading.md').read_text(encoding='utf8')
        body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', rd, re.S | re.M).group(1)
        if '⟨' in body:   # L5, L6: the reading marks the clear passages itself
            clear = ' '.join(re.findall(r'⟨([^⟩]*)⟩', body)); ciph = re.sub(r'⟨[^⟩]*⟩', ' ', body); miss = []
        else:
            clear, ciph, miss = split(body, runs)
        report(f'L{i}', body, clear, ciph, miss)


def laigue():
    D = ROOT / 'targets' / 'laigue1649'
    rd = (D / 'READING43.md').read_text(encoding='utf8')
    txt = rd.split('## Text', 1)[1].split('## The whole', 1)[0]
    q = '\n'.join(l[2:] for l in txt.split('\n') if l.startswith('>'))
    runs = [r.strip() for r in re.sub(r'\*[^*]*\*', '|', q).split('|') if norm(r)]   # the opening: roman = clear
    toks = []
    for line in (D / 'n43' / 'body_assembled.txt').read_text(encoding='utf8').split('\n'):
        if line.startswith('L'): toks += re.findall(r'<[^>]*>|\S+', line.split(':', 1)[1])
    runs += runs_of(toks)
    ed = rd.split('## The whole', 1)[1].split('### Notes on the edition', 1)[0]
    ed = '\n'.join(l[2:] for l in ed.split('\n') if l.startswith('>'))
    clear, ciph, miss = split(ed, runs, window=400)
    report('no. 43 (edition)', ed, clear, ciph, miss)


if __name__ == '__main__':
    {'catinat1691': catinat, 'laigue1649': laigue}[sys.argv[1]]()
