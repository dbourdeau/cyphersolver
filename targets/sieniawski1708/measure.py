"""Measure the Vienna -> Schenck reading.

Cipher tokens = (1) numbers of the 2-digit letter cipher (transcr/RUNS_FINAL.txt runs),
              + (2) code numbers: 3-digit codes (codes.json from extract.py) and the 2-digit codes 80-99 and the
                    single-digit word codes ("3.", "5", "2.") standing outside runs,
              + (3) dotted letter signs (o., b., L., d., e., f., g., c., m., p., oo, ooo, oj) next to a number.
Read          = letter numbers in runs that give sense (NO_SENSE runs count as unread)
              + code tokens and signs whose value is in codes_key.json.
"""
import json, os, re, glob, collections
HERE = os.path.dirname(os.path.abspath(__file__))

NO_SENSE = {'gutswor', 'sollwiglaufeenden', 'is', 'lceth', 'be', 'datmseyihm', 't', 'ditlan'}
SIG = re.compile(r'^(oj|ooo|oo|o|b|L|d|e|f|g|c|m|p)\.?:?$')

def letter_runs():
    ok = bad = 0
    for l in open(os.path.join(HERE, 'transcr', 'RUNS_FINAL.txt'), encoding='utf-8'):
        if not l.startswith('R74'): continue
        f = [x.strip() for x in l.split('|')]
        if len(f) < 5 or 'not a run' in f[4]: continue
        n = len(re.findall(r'\d+', f[1]))
        if f[2] in NO_SENSE: bad += n
        else: ok += n
    return ok, bad

def small_and_signs():
    small, signs = collections.Counter(), collections.Counter()
    for p in glob.glob(os.path.join(HERE, 'transcr', 'R*.txt')):
        for l in open(p, encoding='utf-8'):
            m = re.match(r'\[P\w+ l\.\d+\]\s*(.*)', l)
            if not m: continue
            t = re.sub(r'\([^)]*\)', ' ', m.group(1)); t = re.sub(r'~~[^~]*~~', ' ', t)
            t = re.sub(r'\{[^}]*\}', ' ', t); t = re.sub(r'\^\S+', '', t)
            toks = t.split()
            for i, w in enumerate(toks):
                nb = ' '.join(toks[max(0, i - 1):i + 2])
                if SIG.match(w) and re.search(r'\d', nb):
                    signs[w.rstrip('.:')] += 1
                elif re.fullmatch(r'(8\d|9\d|[235])\.?', w):
                    # outside a run: neighbours are not 2-digit letter numbers
                    prev = toks[i - 1] if i else ''; nxt = toks[i + 1] if i + 1 < len(toks) else ''
                    if not (re.fullmatch(r'\d{1,2}\.?', prev) and re.fullmatch(r'\d{1,2}\.?', nxt)):
                        small[w.rstrip('.')] += 1
    return small, signs

def main():
    ok, bad = letter_runs()
    codes = json.load(open(os.path.join(HERE, 'codes.json'), encoding='utf-8'))
    known = json.load(open(os.path.join(HERE, 'codes_key.json'), encoding='utf-8'))
    c3 = {k: len(v) for k, v in codes.items() if len(k) == 3}
    small, signs = small_and_signs()
    ctot = sum(c3.values()) + sum(small.values())
    cknown = sum(v for k, v in c3.items() if k in known) + sum(v for k, v in small.items() if k in known)
    stot = sum(signs.values()); sknown = sum(v for k, v in signs.items() if k in known)
    total = ok + bad + ctot + stot
    read = ok + cknown + sknown
    print('letter-cipher numbers', ok + bad, 'giving sense', ok, '(%.3f)' % (ok / (ok + bad)))
    print('code tokens', ctot, '(3-digit', sum(c3.values()), '+ small', dict(small), ') with a value', cknown,
          '; distinct 3-digit codes', len(c3), 'with a value', len([k for k in c3 if k in known]))
    print('dotted signs', stot, dict(signs), 'with a value', sknown)
    print('all cipher tokens', total, 'read', read, 'fraction %.3f' % (read / total))

if __name__ == '__main__':
    main()
