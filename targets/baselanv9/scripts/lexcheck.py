"""Mechanical lexicon check (NOT the judge): share of decoded letters standing in words found in the shared Latin
lexicon (lang/lexicons/la.json.gz, 37,769 forms from humanist Latin letters). Words joined across '='. Normalised
j>i, v>u. Run on the real decode and on the clear references, so the lexicon's own coverage is visible."""
import gzip, json, re
D = '/home/claude/keyless/round40c/basel_anv9/'
LEX = set(json.load(gzip.open('/home/claude/keyless/_cs/lang/lexicons/la.json.gz', 'rt', encoding='utf-8')))
def norm(w): return w.lower().replace('j', 'i').replace('v', 'u')
def words_from_decode(prefix):
    txt = ''
    for ln in open(D + 'DECODE.txt'):
        if ln.startswith('#') or not ln.strip(): continue
        k, t = ln.rstrip('\n').split('\t')
        if k.startswith(prefix + ' '): txt += t + ' '
    txt = txt.replace('= ', '')
    return [norm(w) for w in txt.split()]
def words_from_clear(f, keyed=False):
    txt = ''
    for ln in open(D + f):
        if ln.startswith('#') or not ln.strip(): continue
        t = ln.rstrip('\n').split('\t')[-1] if keyed else ln
        txt += re.sub(r'[\[\]]', '', t) + ' '
    return [norm(re.sub('[^A-Za-z]', '', w)) for w in txt.split() if re.sub('[^A-Za-z]', '', w)]
def rate(ws):
    tot = sum(len(re.sub('[^a-z]', '', w)) for w in ws)
    hit = sum(len(re.sub('[^a-z]', '', w)) for w in ws if w in LEX)
    return hit, tot
out = []
for h, f, keyed in (('H1', 'score/CLEAR_H1_f109v.txt', False), ('H2', 'score/CLEAR_H2_f167r.txt', True), ('H3', 'score/CLEAR_H3_f123r.txt', True)):
    a, b = rate(words_from_decode(h)); c, d = rate(words_from_clear(f, keyed))
    out.append('%s decode: %d of %d letters in lexicon words (%.1f%%) | clear reference: %d of %d (%.1f%%)' % (h, a, b, 100.0 * a / b, c, d, 100.0 * c / d))
print('\n'.join(out)); open(D + 'score/lexcheck_out.txt', 'w').write('\n'.join(out) + '\n')
