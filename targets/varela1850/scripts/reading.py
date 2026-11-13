"""Check the marked reading of catalogue 1500 against the mechanical decryption and count words. Stdlib only.

    python scripts/reading.py

marks_varela1850.md holds a fenced block ```marked ... ``` with one 'Rnn: text' line per cipher item of
transcription_varela1850.txt (items R.., N.., S..). Plain words of the letter around the cipher may be given in
<...>; they are not compared.
Marks: {x/y} = the signs give x, read y;  {+a} = letter a added (not in the signs);  [...=m] = hole: the signs
give m, not read;  [?g=m] = guess g for a stretch whose signs give m;  [25] = a lone number or sign kept as
written, not identified.
Comparison ignores case, accents, spaces and punctuation. Exit 1 on any line whose marks do not rebuild the
mechanical decryption, or on a missing line.
"""
import pathlib, re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent


def norm(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c) or c == '̃').lower()
    s = unicodedata.normalize('NFC', s)
    return re.sub(r"[^a-zñ0-9\[\]]", '', s)


def to_mech(m):
    s = re.sub(r'<[^>]*>', '', m)
    s = re.sub(r'\{([^/{}]*)/([^/{}]*)\}', r'\1', s)
    s = re.sub(r'\{\+[^{}]*\}', '', s)
    s = re.sub(r'\[\.\.\.=([^\]]*)\]', r'\1', s)
    s = re.sub(r'\[\?[^=\]]*=([^\]]*)\]', r'\1', s)
    return s


def classify(m):
    s = re.sub(r'<[^>]*>', ' ', m)
    counts = dict(verbatim=0, repaired=0, guess=0, hole=0, code=0)
    for tok in re.findall(r'\[[^\]]*\]|\S+', s):
        if tok.startswith('[...'):
            counts['hole'] += 1
        elif tok.startswith('[?'):
            counts['guess'] += 1
        elif tok.startswith('['):
            counts['code'] += 1
        elif '{' in tok:
            counts['repaired'] += 1
        elif re.search(r'[^\W\d_]', tok):
            counts['verbatim'] += 1
    return counts


mech = {}
for line in open(ROOT / 'decryption_varela1850.txt', encoding='utf-8'):
    if line.startswith('#'):
        continue
    p = line.rstrip('\n').split('\t')
    mech[p[0]] = p[3].replace(' / ', '')
text = (ROOT / 'marks_varela1850.md').read_text(encoding='utf-8')
block = re.search(r'```marked\n(.*?)```', text, re.S).group(1)
bad = False
tot = dict(verbatim=0, repaired=0, guess=0, hole=0, code=0)
seen = set()
for line in block.strip().split('\n'):
    rid, m = line.split(':', 1)
    seen.add(rid)
    if norm(to_mech(m)) != norm(mech[rid]):
        print(f'FAIL {rid}: marks give {norm(to_mech(m))!r}, decryption {norm(mech[rid])!r}'); bad = True
    for k, v in classify(m).items():
        tot[k] += v
for rid in mech:
    if rid not in seen:
        print(f'FAIL {rid}: no line in the marked block'); bad = True
words = tot['verbatim'] + tot['repaired'] + tot['guess'] + tot['hole']
print(f'cipher words (letter runs): {words}; verbatim {tot["verbatim"]}, repaired {tot["repaired"]}, '
      f'guess {tot["guess"]}, hole {tot["hole"]}; lone numbers and signs not identified: {tot["code"]}')
print(f'verbatim share of cipher words: {tot["verbatim"]}/{words} = {100 * tot["verbatim"] / words:.1f}%; '
      f'counting the unidentified numbers as holes: {tot["verbatim"]}/{words + tot["code"]} '
      f'= {100 * tot["verbatim"] / (words + tot["code"]):.1f}%')
sys.exit(1 if bad else 0)
