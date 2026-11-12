"""Mark check. Standard library only.

    python scripts/check_marks.py

For every transcription_<doc>.txt (not the pass files):
1. rebuilds decryption_<doc>.txt from the transcription and key.tsv and fails if the file differs;
2. reads the ```marked block of reading_<doc>.md (lines `label | text`), resolves the marks to their mechanical side
   ({x/y} -> x, {+a} -> '', [?word] -> word, the quote marks of a not-read stretch dropped), normalises
   (lower case; no spaces, punctuation, accents, hyphens) and compares letter by letter with the decryption,
   where a two-valued key letter (a|b) accepts either value. Any unmarked departure fails.
3. counts words: verbatim (no mark), repair ({x/y} or {+a}), guess ([?word]), not read («...»), holes ([...]).
Exit 1 on any failure.
"""
import pathlib, re, subprocess, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
MARK = re.compile(r'\{([^{}/]*)/([^{}]*)\}|\{\+([^{}]*)\}')
GUESS = re.compile(r'\[\?([^\]]+)\]')

def mech(t):
    t = GUESS.sub(lambda m: m.group(1), t)
    t = MARK.sub(lambda m: m.group(1) if m.group(3) is None else '', t)
    return t.replace('«', '').replace('»', '').replace('[...]', '')

def norm(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z()|\[\]?]", '', s)

def units(dec):
    """decryption text -> list of sets of allowed letters"""
    out, i, s = [], 0, norm(dec)
    while i < len(s):
        if s[i] == '(':
            j = s.index(')', i); out.append(set(s[i + 1:j].split('|'))); i = j + 1
        elif s[i] == '[':
            j = s.index(']', i); out.append({'#'}); i = j + 1
        else:
            out.append({s[i]}); i += 1
    return out

def words(text):
    c = {'verbatim': 0, 'repair': 0, 'guess': 0, 'notread': 0, 'holes': text.count('[...]')}
    inside = False
    for w in re.sub(r'\[\.\.\.\]', ' ', text).split():
        if '«' in w: inside = True
        letters = re.sub(r'[^\w]', '', MARK.sub('x', GUESS.sub('x', w)))
        if letters:
            if inside: c['notread'] += 1
            elif GUESS.search(w): c['guess'] += 1
            elif MARK.search(w): c['repair'] += 1
            else: c['verbatim'] += 1
        if '»' in w: inside = False
    return c

bad = False
for tr in sorted(ROOT.glob('transcription_*.txt')):
    if '_pass' in tr.name:
        continue
    doc = tr.stem.split('_', 1)[1]
    out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(tr), str(ROOT / 'key.tsv')],
                         capture_output=True, text=True, encoding='utf-8').stdout
    have = (ROOT / f'decryption_{doc}.txt').read_text(encoding='utf-8')
    if out.strip() != have.replace('\r\n', '\n').strip():
        print(f'FAIL decryption_{doc}.txt is not what decrypt.py gives'); bad = True; continue
    print(f'decryption_{doc}.txt: rebuilt, identical')
    dec = dict(l.split('\t') for l in have.strip().splitlines())
    md = (ROOT / f'reading_{doc}.md').read_text(encoding='utf-8')
    block = md.split('```marked')[1].split('```')[0]
    tot = {'verbatim': 0, 'repair': 0, 'guess': 0, 'notread': 0, 'holes': 0}
    seen = set()
    for l in [x for x in block.strip().split('\n') if x.strip()]:
        lab, text = [x.strip() for x in l.split('|', 1)]
        seen.add(lab)
        a, b = norm(mech(text)), units(dec.get(lab, '#'))
        ok = len(a) == len(b) and all(ch in u for ch, u in zip(a, b))
        if not ok:
            bad = True
            print(f'FAIL {doc} {lab}\n  reading->mech: {a}\n  decryption:    {dec.get(lab)}')
        for k, v in words(text).items():
            tot[k] += v
    if set(dec) - seen:
        bad = True; print(f'FAIL {doc}: lines without reading {sorted(set(dec) - seen)}')
    n = tot['verbatim'] + tot['repair'] + tot['guess'] + tot['notread']
    print(f'{doc}: words {n}: verbatim {tot["verbatim"]} ({100 * tot["verbatim"] / n:.1f}%), marked repair {tot["repair"]}, '
          f'guess {tot["guess"]}, not read {tot["notread"]}; holes {tot["holes"]}; from a gloss 0 '
          '(clear words of the telegram are counted as verbatim)')
sys.exit(1 if bad else 0)
