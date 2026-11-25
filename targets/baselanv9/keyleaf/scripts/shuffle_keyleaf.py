"""Shuffle control for pass 2 (key leaf). The KEY_LEAF.tsv values are permuted among its single-sign tokens (every
token row of the key; the pairs, the two whole-word forms, the dot/diaeresis marks and the D2/D3 rules stay as they
are), 5,000 keys at each of seeds 20261112 and 7. Each shuffled key decodes the same frozen transcriptions with the
same decoder. Statistic: la-letters language model (lang/, corpus sha256 asserted below), mean log-probability per
character of the decoded text (letters only, [?] and ~ dropped), per section and per pentacle.
Also a mechanical lexicon pointer (NOT the judge): share of decoded letters in words of lang/lexicons/la.json.gz.
Writes work/shuffle_keyleaf_out.txt and work/lexcheck_keyleaf.tsv."""
import sys, os, re, random, statistics, json, gzip, hashlib
sys.path.insert(0, '/home/claude/keyless/_cs')
from lang import lm
K = '/home/claude/keyless/round40c/basel_anv9/keyleaf/'
src = open(K + 'scripts/decode_keyleaf.py').read().replace("if __name__ == '__main__':", 'if False:')
G = {}
exec(compile(src, 'decode_keyleaf', 'exec'), G)   # runs the freeze check
CORPUS = '/home/claude/keyless/_cs/lang/corpora/la-latlib-letters.txt'
assert hashlib.sha256(open(CORPUS, 'rb').read()).hexdigest() == 'c0299efd2c7693842835363aea68141c254e84761e19be91d055c09f71e2787f', 'corpus changed'
M = lm.load('la-letters')
LEX = set(json.load(gzip.open('/home/claude/keyless/_cs/lang/lexicons/la.json.gz', 'rt', encoding='utf-8')))

FILES = [('TRAIN', 'tx2/f004r.txt'), ('TRAIN', 'tx2/f004v.txt'), ('H1', 'tx2/f015r.txt'), ('H2', 'tx2/f159r.txt'),
         ('H3', 'tx2/f034r_p34.txt'), ('PENT', 'tx/PENTACLES.txt')]
UNITS = []   # (section, line id, [word signs])
for sec, f in FILES:
    for ln in open(K + f, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        lid, txt = ln.rstrip('\n').split('\t')
        ws = [w.split() for w in txt.split(' / ') if w.split() and w.split() != ['Fill']]
        UNITS.append((sec, lid, ws))

BASE = dict(G['KEY'])
PERM = sorted(BASE)


def dec_units(key):
    G['KEY'].clear(); G['KEY'].update(key)
    out = []
    for sec, lid, ws in UNITS:
        out.append((sec, lid, ' '.join(G['decode_word'](w)[0] for w in ws)))
    return out


def letters(t):
    return re.sub('[^a-z ]', '', t.replace('[?]', ' ').replace('~', ''))


def lmscore(dec, sel):
    txt = ' '.join(letters(t) for s, l, t in dec if sel(s, l))
    return M.per_char(lm.norm(txt, 'latin'))


SELS = [('TRAIN', lambda s, l: s == 'TRAIN'), ('H1', lambda s, l: s == 'H1'), ('H2', lambda s, l: s == 'H2'),
        ('H3', lambda s, l: s == 'H3'), ('PENT all', lambda s, l: s == 'PENT')]
pent_ids = [l for s, l, w in UNITS if s == 'PENT']
real = dec_units(BASE)
out = ['# shuffle control, pass 2 (key leaf). Model la-letters, per-character log-probability. %d single-sign tokens permuted.' % len(PERM)]
real_s = {n: lmscore(real, f) for n, f in SELS}
real_p = {p: lmscore(real, lambda s, l, p=p: l == p) for p in pent_ids}
for seed in (20261112, 7):
    rnd = random.Random(seed)
    sh = {n: [] for n, f in SELS}
    shp = {p: [] for p in pent_ids}
    vals = [BASE[t] for t in PERM]
    for i in range(5000):
        v = vals[:]; rnd.shuffle(v)
        d = dec_units(dict(zip(PERM, v)))
        for n, f in SELS:
            sh[n].append(lmscore(d, f))
        for p in pent_ids:
            shp[p].append(lmscore(d, lambda s, l, p=p: l == p))
    out.append('## seed %d, 5000 keys' % seed)
    out.append('section\treal\tshuffle mean\tsd\tbest shuffle\tz\tshuffles >= real')
    for n, f in SELS:
        xs = sh[n]; m, sd = statistics.mean(xs), statistics.pstdev(xs)
        out.append('%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.1f\t%d/5000' % (n, real_s[n], m, sd, max(xs), (real_s[n] - m) / sd, sum(x >= real_s[n] for x in xs)))
    out.append('pentacle\treal\tshuffle mean\tsd\tbest shuffle\tz\tshuffles >= real')
    for p in pent_ids:
        xs = shp[p]; m, sd = statistics.mean(xs), statistics.pstdev(xs)
        out.append('%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.1f\t%d/5000' % (p, real_p[p], m, sd, max(xs), (real_p[p] - m) / sd, sum(x >= real_p[p] for x in xs)))
open(K + 'work/shuffle_keyleaf_out.txt', 'w').write('\n'.join(out) + '\n')

rows = ['section\tline\tletters\tletters in lexicon words\tshare']
for sec, lid, t in real:
    a = b = 0
    for w in letters(t).split():
        b += len(w)
        if w.replace('j', 'i').replace('v', 'u') in LEX:
            a += len(w)
    rows.append('%s\t%s\t%d\t%d\t%.1f%%' % (sec, lid, b, a, 100.0 * a / b if b else 0))
open(K + 'work/lexcheck_keyleaf.tsv', 'w').write('\n'.join(rows) + '\n')
print('\n'.join(out[:12]))
