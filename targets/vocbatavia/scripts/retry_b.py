# Escalation steps "retry" and "key-rebuild" for system B (27 Nov 2026, write-up session).
# Run from targets/vocbatavia:  python -I scripts/retry_b.py ../../lang/lexicons/nl.json.gz > letters/RETRY_B_2026-11-27.txt
# 1. retry: every system-B word of the 1640 postscript and the 1643 letter (the holes of scripts/house_count.py) decoded
#    with the frozen KEY_B_v1 (letters and B numbers); unknown signs print as '?'.
# 2. key-rebuild (LM context, dictionary only): for each word with unknown signs, the Dutch words of the right length that
#    fit the known letters, from the repository's nl lexicon plus the words already read in this target (1623, 1634).
#    A proposal is listed only; nothing is added to the key unless two or more words agree on the same new value.
# KEY_B_v1 is not edited. No figure of record and no house count changes. AI-checked only: the checks were done with AI
# tools and no person checked each record by hand.
import csv, gzip, json, re, sys
from collections import defaultdict

lex = set(json.load(gzip.open(sys.argv[1])))
# period words already read in this target (house_count's read words, 1623 and 1634 decodes are in these files)
for f in ['letters/1623_1634/RESULT_trackB.md', 'letters/1643/RESULT_1643.md', 'letters/1640/readings/reading.md']:
    lex |= set(w.lower() for w in re.findall(r'[A-Za-z]{2,}', open(f, encoding='utf-8').read()))

letters, numbers = {}, {}
sec = 'num'
for r in csv.reader(open('key/KEY_B_v1.tsv', encoding='utf-8'), delimiter='\t'):
    if not r: continue
    if r[0].startswith('LETTERS'): sec = 'let'; continue
    if r[0].startswith('ROMAN'): sec = 'rom'; continue
    if len(r) < 2 or r[0] == 'sign': continue
    if sec == 'num' and r[0].isdigit(): numbers[r[0]] = r[1].split('/')[0]
    if sec == 'let': letters[r[0]] = r[1].split('/')[0]

def dec(word):
    out = []
    for tok in re.findall(r'\d+|[A-Za-z]', word):
        if tok.isdigit(): out.append(numbers.get(tok, '?'))
        else: out.append(letters.get(tok.lower(), '?'))
    return ''.join(out)

words = []
t = open('letters/1640/transcriptions/T1640_transcription.txt', encoding='utf-8').read()
for lc in re.findall(r'\[LC: ([^\]]*)\]', t):
    for w in re.split(r'[\s.]+', lc):
        if w: words.append(('1640', w))
for w in ['k', 'bd', 'p']: words.append(('1640*', w))      # after 'Amsterdam', image and reader 2; not in the frozen file
for line in open('letters/1643/T1643_transcription.txt', encoding='utf-8'):
    if line.startswith('#') or '|' not in line: continue
    pl, body = [x.strip() for x in line.split('|', 1)]
    for w in re.findall(r'<([^>]*)>', body): words.append(('1643 ' + pl, w.strip(':')))

print('# retry: system-B words decoded with KEY_B_v1 (frozen); ? = sign with no value')
print('# where\tcipher\tKEY_B_v1\tfits (nl lexicon + words read in this target), at most 8')
full = 0; props = defaultdict(lambda: defaultdict(set))
for where, w in words:
    d = dec(w)
    if '?' not in d: full += 1
    fits = []
    if len(d) >= 3 and d.count('?') <= 2:
        pat = re.compile('^' + d.replace('?', '.') + '$')
        fits = sorted(x for x in lex if pat.match(x))
        toks = re.findall(r'\d+|[A-Za-z]', w)
        if 1 <= len(fits) <= 3:
            for x in fits:
                for tok, ch in zip(toks, x):
                    v = numbers.get(tok) if tok.isdigit() else letters.get(tok.lower())
                    if v is None: props[tok.lower()][ch].add(w)
    print(f'{where}\t{w}\t{d}\t{", ".join(fits[:8])}')
print(f'\n# words: {len(words)}; fully valued by KEY_B_v1: {full}')
print('# key-rebuild proposals (unknown sign -> letter, from words with 1-3 dictionary fits):')
agree = 0
for tok in sorted(props):
    for ch, ws in sorted(props[tok].items()):
        ok = len(ws) >= 2
        agree += ok
        print(f'  {tok} -> {ch}: {", ".join(sorted(ws))}{"  (two or more words agree)" if ok else "  (one word only: not adopted)"}')
print(f'# proposals with two or more agreeing words: {agree}')
