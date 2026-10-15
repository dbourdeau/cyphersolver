"""Circular-letter test for R1955 (negative). Scoring rule fixed before the results were seen (11 Oct 2026).

Hypothesis: R1955 repeats, in Michell's code, the wording of another royal letter of the same days (a circular sent to
several envoys), which would then supply its plaintext.
Query Q = the decoded whole words of R1955 (envoy table from envoy_key.py), in cipher order; the fragments
{s,e,r,ent,ant,oit,der,re,ment,ne} are dropped. Score of a letter = LCS(Q, its words); z = (LCS - mean)/sd over
100 shuffles of Q against the same letter. Candidates: PC letters dated 22 Dec 1751 - 10 Jan 1752. Controls: every
other French PC letter of vols 8-9. Decision rule: a candidate counts only if z >= 4 AND z exceeds the highest
control z.

usage: python scripts/circular.py <pc8.txt> <pc9.txt> [--power]          (from key1751/)
pc8.txt / pc9.txt: plain text of the Trier digital edition, made with pc_html2txt.py (git-ignored).
--power runs the positive control: a 17% random sample of a real letter's words (77 of ~450, as for R1955) must be
found against its own source letter and against a 50% paraphrase of it.
Result of 11 Oct 2026: query 77 words; best candidate PC 5268 (to Michell, 4 Jan 1752) z = 2.69; highest control
z = 4.85 (PC 5117); no candidate clearly above the controls. The original run also scored WAINUT's transcriptions of
five Dutch decipherments of royal letters to von der Hellen, 3-24 Dec 1751 (Fagel 5177): z between -2.01 and 0.57.
Those transcriptions are not part of this folder; leaving them out does not change the PC scores (same seed order)."""
import sys, os, re, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import decode as b
from common import DATA, norm, lcs

# R1955's transcription moved to targets/r1955/ when the entry was split (14 Oct 2026)
R1955 = os.path.join(DATA, '..', '..', 'r1955', 'R1955_tx.txt')

FRAG = {'s', 'e', 'r', 'ent', 'ant', 'oit', 'der', 're', 'ment', 'ne'}
MON = {'decembre': 12, 'décembre': 12, 'janvier': 1}


def query():
    key = b.load_key(os.path.join(DATA, 'envoy_key_lyonet.tsv'))
    Q = []
    for code, v, conf, fl in b.decode(key, [t for t in b.load_cipher(R1955) if t[0] != '||']):
        if v == '·':
            continue
        v = v.replace('princestadhouder', 'prince stadhouder').replace('PrinceStadhouder', 'prince stadhouder')
        Q += [w for w in norm(v) if w not in FRAG]
    return Q


def pc_letters(paths):
    out = []
    for p in paths:
        t = open(p, encoding='utf8').read()
        heads = list(re.finditer(r'\n(\d{4})\. ([^\n]*)\n', t))
        for k, m in enumerate(heads):
            e = heads[k + 1].start() if k + 1 < len(heads) else len(t)
            body = t[m.end():e]
            dm = re.search(r'(?:^|\n)[A-ZÄÖÜa-zäöü\- ]+, (\d{1,2})\.? ([a-zéû]+)\.? (175\d)\.', body)
            words = norm(re.sub(r'\d+-\d+|<\d+>', ' ', body.split('Nach dem Concept')[0]))
            fr = sum(1 for w in words if w in ('de', 'la', 'le', 'que', 'les', 'et', 'vous')) / max(len(words), 1)
            out.append(dict(id='PC' + m.group(1), title=m.group(2),
                            date=(dm.group(1) + ' ' + dm.group(2) + ' ' + dm.group(3)) if dm else '', words=words, fr=fr))
    return out


def is_cand(d):
    m = re.match(r'(\d+) (\w+) (175\d)', d)
    if not m:
        return False
    day, mon, y = int(m.group(1)), m.group(2), int(m.group(3))
    return (y == 1751 and MON.get(mon) == 12 and day >= 22) or (y == 1752 and MON.get(mon) == 1 and day <= 10)


def z(rng, Q, W, n=100):
    obs = lcs(Q, W)
    sh = [lcs(rng.sample(Q, len(Q)), W) for _ in range(n)]
    mu, sd = float(np.mean(sh)), float(np.std(sh)) or 1.0
    return (obs - mu) / sd, obs, mu


if __name__ == '__main__':
    paths = [a for a in sys.argv[1:] if not a.startswith('--')]
    L = [d for d in pc_letters(paths) if d['fr'] > 0.12 and len(d['words']) >= 60]
    for d in L:
        d['cand'] = is_cand(d['date'])
    if '--power' in sys.argv:
        by = {d['id']: d for d in L}
        rng = random.Random(3)
        for sid in ('PC5263', 'PC5262'):
            W = by[sid]['words']
            for rep in range(3):
                keep = sorted(rng.sample(range(len(W)), int(0.17 * len(W))))
                Qs = [W[i] for i in keep]
                para = [w if rng.random() < 0.5 else rng.choice(W) for w in W]
                ctrl = [z(rng, Qs, d['words'])[0] for d in rng.sample(L, 300)]
                print(sid, 'rep', rep, 'query', len(Qs), 'z(source)=%.1f' % z(rng, Qs, W)[0],
                      'z(50%% paraphrase)=%.1f' % z(rng, Qs, para)[0], 'controls max %.1f mean %.1f' % (max(ctrl), np.mean(ctrl)))
        sys.exit()
    Q = query()
    rng = random.Random(7); res = []
    for d in L:
        zz, obs, mu = z(rng, Q, d['words'])
        res.append((round(zz, 2), obs, round(mu, 1), len(d['words']), d['cand'], d['id'], d['date'], d['title'][:50]))
    res.sort(key=lambda r: -r[0])
    ctrl = [r for r in res if not r[4]]; cand = [r for r in res if r[4]]
    mx = max(r[0] for r in ctrl)
    print('query words', len(Q))
    print('letters scored', len(res), 'candidates', len(cand), 'controls', len(ctrl), 'max control z', mx, ctrl[0][5])
    print('candidates (z, LCS, shuffle mean, words, cand, id, date, title):')
    for r in cand:
        print('  ', r)
    print('DECISION:', [r[5] for r in cand if r[0] >= 4 and r[0] > mx] or 'no candidate clearly above controls')
