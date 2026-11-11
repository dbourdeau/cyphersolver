"""Statistical validation of a reading: is the claimed decipherment better than what chance and overfitting give?

A reading is checked against a period character n-gram model from lang/ (order 4, no spaces, so word division
in the cipher does not matter). The input is the reading aligned token by token with the ciphertext:

  targets/<folder>/validation.tsv      one cipher token per line, in text order:  <token> TAB <reading>
                                       reading '?' or empty = unread (left out); '-' = a null (reads as nothing)
                                       header lines:  # model: fr-1600-letters    (else chosen from the profile)
                                                      # source: <file the pairs were taken from>
                                                      # note: <anything>
                                       other lines starting # are comments

From the pairs the script takes the key K (each cipher type -> the reading it carries most often) and scores

  real        K applied to the ciphertext (the share of occurrences that K reads differently is reported as
              polyphony; the claimed per-occurrence reading is scored too)
  null 1      random keys of the same structure: K's values permuted among the cipher types whose values have
              the same number of letters (nulls stay nulls), n = 200
  null 2      the overfitting test: the ciphertext tokens shuffled (gaps at unread tokens kept in place), then
              a key annealed onto them by swapping the values of two types whose values have the same number of
              letters, nulls fixed; started from K and from a null-1 key; the best of 2 restarts on each of 6
              shuffles. The length rule keeps the letters each token yields: with free swaps an n-gram model
              rewards a word value ('que') moved onto a frequent sign, or a frequent sign turned into a null,
              whatever the text ('deladelade'), and a fitted key on shuffled text then beats any real reading
  power       the same annealer from a null-1 key on the real ciphertext, to show it is strong enough that its
              failure to match the reading on shuffled text means something
  Readings over 5,000 read tokens are tested on their first 5,000. Unread tokens split the text: no n-gram
  spans them.

Verdict ("pass" / "weak" / "fail" / "underdetermined" / "too short"):
  too short   fewer than 40 read tokens (or fewer than 80 letters)
  not applicable  polyphonic reading: more than 10% of read tokens differ from their type's commonest value
  pass        real is at least 5 sd above null 1, above every null-2 fit, and at least 3 sd above the null-2 mean
  weak        real is at least 1 sd above the null-2 mean but short of a pass
  fail        real is within 1 sd of the null-2 mean: a key fitted to shuffled text reads as well as the claimed one
              (--control fakes land in fail, weak or underdetermined, never pass, though they beat
              null 1 by several sd: null 1 alone proves nothing)
  underdetermined  not a pass, and the annealer on the real ciphertext reaches a higher score than the reading:
              the letter model cannot tell the reading from a fitted key on this text (typically a syllabic
              nomenclator with few tokens per type), so the test neither confirms nor refutes it

Scores are mean natural-log probability per letter (lang/lm.py): real text about -1.6 to -2.0 at order 4 without
spaces, letter-shuffled text about -3.5 or lower.

  python docs/_validate.py <folder>                       print the result
  python docs/_validate.py <folder> --write               also record it in profile.json (outcome.validation, a
                                                          verification step, "statistical test" on a pass)
  python docs/_validate.py <folder> --pairs FILE          use another pairs file
  python docs/_validate.py <folder> --quick               fewer shuffles and iterations (a trial run)
  python docs/_validate.py <folder> --control             negative control: replace the reading by a key annealed
                                                          onto the shuffled ciphertext; it must not pass
  python docs/_validate.py <folder> --na "reason"         record that the test cannot run (transposition, no token
                                                          alignment, non-alphabetic plaintext)
  python docs/_validate.py --list                         readings that need validation and whether they have it
"""
import sys, re, json, math, random, pathlib, datetime, collections
import numpy as np

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(HERE))
from lang import lm
import _check_writeup as cw

ORDER = 4
MIN_TOKENS = 40
MAX_TOKENS = 5000             # longer readings are tested on their first 5,000 read tokens (time)
MAX_POLYPHONY = 0.10          # above this share of tokens off their type's commonest value the test does not fit
STEP_PREFIX = 'Statistical validation (docs/_validate.py)'
KEY_RECOVERY = {'key recovered from ciphertext-only', 'key recovered based on adjacent plaintext',
                'key recovered based on plaintext from external sources'}

# ------------------------------------------------------------------ model choice

def default_model(lang, year):
    lang = (lang or '').lower(); y = year if isinstance(year, int) else 1600
    if 'french' in lang:  return 'fr-1530-despatches' if y < 1570 else 'fr-1600-letters' if y < 1660 else 'fr-modern'
    if 'spanish' in lang or 'castil' in lang: return 'es-golden-age' if y < 1700 else 'es-modern'
    if 'italian' in lang: return 'it-cinquecento' if y < 1680 else 'it-modern'
    if 'latin' in lang:   return 'la'
    if 'english' in lang: return 'en-1640s' if 1630 <= y < 1720 else 'en-modern'
    if 'german' in lang:  return 'de-1500s' if y < 1610 else 'de-1640s' if y < 1700 else 'de-1740s' if y < 1800 else 'de-modern'
    for k, m in (('dutch', 'nl-modern'), ('catalan', 'ca-modern'), ('portug', 'pt-modern'), ('danish', 'da-modern'),
                 ('swedish', 'sv-modern'), ('polish', 'pl-modern'), ('hungar', 'hu-modern'), ('welsh', 'cy-modern')):
        if k in lang: return m
    return None

def profile_of(folder):
    p = cw.tdir(folder) / 'profile.json'
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else None

# ------------------------------------------------------------------ input

def read_pairs(path):
    head, toks, vals = {}, [], []
    for line in pathlib.Path(path).read_text(encoding='utf-8').splitlines():
        if line.startswith('#') and '	' not in line:           # a token may itself start with '#'
            m = re.match(r'#\s*(model|source|note|norm)\s*:\s*(.*)', line)
            if m: head[m.group(1)] = m.group(2).strip()
            continue
        if not line.strip(): continue
        tok, _, val = line.partition('\t')
        toks.append(tok.strip()); vals.append(val.strip())
    return head, toks, vals

# ------------------------------------------------------------------ scoring

class Scorer:
    def __init__(self, model_id, norm=None):
        spec = lm.registry()[0][model_id]
        self.scheme = norm or spec['norm']
        self.m = lm.load(model_id, order=ORDER, spaces=False)
        self.model_id = model_id

    def enc(self, value):
        return self.m.encode(lm.norm(value, self.scheme, spaces=False))

    def per_char(self, arrays):
        """Mean log-probability per letter of the concatenated values. None marks an unread token: the text is
        scored as separate segments there, so no n-gram spans a gap."""
        tot = n = 0; seg = []
        for a in list(arrays) + [None]:
            if a is not None: seg.append(a); continue
            if seg:
                x = np.concatenate(seg); k = len(x) - ORDER + 1
                if k > 0: tot += self.m.score_idx(x); n += k
            seg = []
        return (tot / n if n > 0 else float('-inf')), n

def neighbours(inventory):
    """Swap partners: for each type, the other types whose K value has the same number of letters. Nulls (empty
    values) never move. Every token then yields as many letters as under K, so a fitted key cannot win by moving a
    word value ('que', 'pour') onto a frequent sign or by turning frequent signs into nulls, which an n-gram model
    rewards whatever the text."""
    by_len = collections.defaultdict(list)
    for i, v in enumerate(inventory): by_len[len(v)].append(i)
    return [[j for j in by_len[len(v)] if j != i] if len(v) else [] for i, v in enumerate(inventory)]

def anneal(sc, seq, inventory, init, iters, rng, t0=0.6, nb=None):
    """Anneal a type->value key onto the token sequence seq (type indices, -1 = gap) by swapping the values of two
    types whose values have the same length (neighbours()). inventory[i] is the encoded value of K's type i; key[t] = the
    inventory slot type t reads as. Swaps keep K's value multiset and the number of letters each token
    yields, so the n-gram model cannot be gamed with repetitive text
    ('deladelade'). Returns (best per-letter score, best key)."""
    key = list(init)
    nb = nb or neighbours(inventory)
    score = lambda k: sc.per_char([inventory[k[t]] if t >= 0 else None for t in seq])[0]
    cur = best = score(key); bestkey = key[:]
    nt = len(key)
    for i in range(iters):
        T = t0 * (1 - i / iters) + 1e-3
        k2 = key[:]
        a = rng.randrange(nt)
        if not nb[a]: continue
        b = rng.choice(nb[a])
        k2[a], k2[b] = k2[b], k2[a]
        s = score(k2)
        if s >= cur or rng.random() < math.exp((s - cur) / T * 50):     # scores are per letter: scale the step
            key, cur = k2, s
            if s > best: best, bestkey = s, k2[:]
    return best, bestkey

def effort(ntypes, quick):
    iters = (3000 if quick else 4000) + (10 if quick else 25) * ntypes
    return min(iters, 15000 if quick else 30000)

def validate(folder, pairs=None, quick=False, seed=1, control=False):
    prof = profile_of(folder)
    path = pathlib.Path(pairs) if pairs else cw.tdir(folder) / 'validation.tsv'
    if not path.exists():
        return {'error': f'no pairs file {path.relative_to(ROOT) if path.is_absolute() else path}'}
    head, toks, vals = read_pairs(path)
    doc0 = ((prof or {}).get('documents') or [{}])[0]
    model_id = head.get('model') or default_model(doc0.get('language'), doc0.get('year'))
    if not model_id: return {'error': 'no model: add "# model: <id>" to the pairs file'}
    sc = Scorer(model_id, head.get('norm'))

    # read tokens; an unread token stays in the sequence as a gap (None / -1), so no n-gram spans it
    isread = lambda v: bool(v) and v != '?'
    read = [(t, v) for t, v in zip(toks, vals) if isread(v)]
    gaps = [not isread(v) for v in vals]
    rng = random.Random(seed)
    if control:
        # negative control: replace the reading by a fake one, a key annealed onto the shuffled ciphertext (the
        # overfit a solver could produce from noise). The test must not pass it.
        ty = sorted({t for t, _ in read}); Kc = {}
        for t, v in read: Kc.setdefault(t, collections.Counter())[v] += 1
        Kc = {t: c.most_common(1)[0][0] for t, c in Kc.items()}
        inv = [sc.enc('' if Kc[t] == '-' else Kc[t]) for t in ty]
        ix = {t: i for i, t in enumerate(ty)}
        sh = [ix[t] for t, _ in read]; rng.shuffle(sh)
        nbc = neighbours(inv)
        def start():                                     # K's values shuffled within each length class
            k = list(range(len(ty)))
            for cls in {tuple(sorted([i] + nbc[i])) for i in range(len(ty)) if nbc[i]}:
                vals_ = [k[i] for i in cls]; rng.shuffle(vals_)
                for i, v in zip(cls, vals_): k[i] = v
            return k
        best, key = max((anneal(sc, sh, inv, start(), effort(len(ty), quick), rng, nb=nbc)
                         for _ in range(1 if quick else 2)), key=lambda r: r[0])     # as many restarts as a null fit
        read = [(ty[t], Kc[ty[key[t]]]) for t in sh]
        gaps = [False] * len(read)
    seq_tok = [t for t, _ in read]
    by_type = collections.defaultdict(collections.Counter)
    for t, v in read: by_type[t][v] += 1
    types = sorted(by_type)
    K = {t: by_type[t].most_common(1)[0][0] for t in types}
    poly = sum(1 for t, v in read if v != K[t]) / max(1, len(read))
    # value inventory: every distinct value K uses, with multiplicity over types
    inv_vals = [('' if K[t] == '-' else K[t]) for t in types]
    inventory = [sc.enc(v) for v in inv_vals]
    tix = {t: i for i, t in enumerate(types)}
    it = iter(seq_tok)
    seq = [-1 if g else tix[next(it)] for g in gaps]
    seq = [x for i, x in enumerate(seq) if x >= 0 or i == 0 or seq[i - 1] >= 0]     # one gap marker per run
    if len(read) > MAX_TOKENS:                           # cut to the first MAX_TOKENS read tokens
        k = 0
        for i, x in enumerate(seq):
            k += x >= 0
            if k == MAX_TOKENS: seq = seq[:i + 1]; break
    nb = neighbours(inventory)
    def scramble(key):                                   # a random start: K's values shuffled within each length class
        key = key[:]
        for cls in {tuple(sorted([i] + nb[i])) for i in range(len(key)) if nb[i]}:
            vals_ = [key[i] for i in cls]; rng.shuffle(vals_)
            for i, v in zip(cls, vals_): key[i] = v
        return key
    def shuffled(s):                                     # shuffle the read tokens, keep the gaps where they are
        vals_ = [x for x in s if x >= 0]; rng.shuffle(vals_); it2 = iter(vals_)
        return [next(it2) if x >= 0 else -1 for x in s]
    dec = lambda key, s=None: [inventory[key[i]] if i >= 0 else None for i in (seq if s is None else s)]
    keyK = list(range(len(types)))                       # type i takes inventory[i] (its own K value)

    claimed, letters = sc.per_char([sc.enc('' if v == '-' else v) if isread(v) else None for v in
                                    ([v for _, v in read] if control else vals)])
    real, _ = sc.per_char(dec(keyK))
    res = dict(date=datetime.date.today().isoformat(), model=model_id, file=path.name, tokens=len(read),
               unread=sum(gaps), types=len(types), tokens_per_type=round(len(read) / max(1, len(types)), 2),
               letters=letters, polyphony=round(poly, 3), score=round(real, 3), claimed_score=round(claimed, 3))
    if len(read) < MIN_TOKENS or letters < 2 * MIN_TOKENS:
        res.update(nulls={}, verdict='too short'); return res
    if poly > MAX_POLYPHONY:
        # a polyphonic system (one sign, several values) has no one-value key K to permute or refit
        res.update(nulls={}, verdict='not applicable',
                   na=f"polyphonic: {poly:.0%} of read tokens differ from their type's commonest value"); return res

    # null 1: K's values permuted among the types
    n1 = []
    for _ in range(200):
        perm = scramble(keyK)                            # K's values permuted within each length class
        n1.append(sc.per_char(dec(perm))[0])
    # null 2: shuffled ciphertext, key annealed onto it; power: same annealer on the real text from random keys
    shuffles, restarts = (3, 2) if quick else (6, 2)
    iters = effort(len(types), quick)
    n2 = []
    for s in range(shuffles):
        sh = shuffled(seq)
        best = max(anneal(sc, sh, inventory, keyK if r == 0 else scramble(keyK), iters, rng, nb=nb)[0]
                   for r in range(restarts))
        n2.append(best)
    power = max(anneal(sc, seq, inventory, scramble(keyK), iters, rng, nb=nb)[0] for _ in range(restarts))

    def stats(xs):
        m = sum(xs) / len(xs); sd = (sum((x - m) ** 2 for x in xs) / max(1, len(xs) - 1)) ** 0.5
        z = (real - m) / sd if sd > 0 else float('inf')
        p = (sum(x >= real for x in xs) + 1) / (len(xs) + 1)
        return dict(n=len(xs), mean=round(m, 3), sd=round(sd, 3), max=round(max(xs), 3),
                    z=round(z, 1) if math.isfinite(z) else 99.0, p=round(p, 4))
    s1, s2 = stats(n1), stats(n2)
    res['nulls'] = {'random keys': s1, 'shuffled refit': s2}
    res['power'] = round(power, 3)
    if s1['z'] >= 5 and real > s2['max'] and s2['z'] >= 3: v = 'pass'
    elif s2['z'] >= 1: v = 'weak'
    else: v = 'fail'
    if v != 'pass' and power >= real: v = 'underdetermined'
    res['verdict'] = v
    return res

# ------------------------------------------------------------------ recording

def _span(text, key, start=0):
    """(start, end) of the JSON value of "key" at or after start."""
    m = re.compile(r'"%s"\s*:\s*' % re.escape(key)).search(text, start)
    if not m: return None
    _, end = json.JSONDecoder().raw_decode(text, m.end())
    return m.end(), end

def record(folder, res):
    p = cw.tdir(folder) / 'profile.json'
    text = p.read_text(encoding='utf-8')
    prof = json.loads(text)
    o = prof['outcome']
    val = {k: res[k] for k in ('date', 'model', 'file', 'tokens', 'types', 'tokens_per_type', 'score', 'nulls', 'power', 'verdict')
           if k in res}
    val['notes'] = res['na'] if 'na' in res else (f"claimed per-occurrence score {res['claimed_score']}; polyphony {res['polyphony']}; "
                    f"{res['unread']} unread tokens left out; annealer on the real text from random keys reached "
                    f"{res.get('power', 'n/a')}")
    ver = [x for x in (o.get('verification') if isinstance(o.get('verification'), list) else []) if x != 'none']
    if res['verdict'] == 'pass' and 'statistical test' not in ver: ver.append('statistical test')
    if res['verdict'] != 'pass' and 'statistical test' in ver: ver.remove('statistical test')
    if not ver: ver = ['none']
    # outcome: replace or insert "validation", then the verification list (textual edits keep the file's layout)
    os_, oe = _span(text, 'outcome')
    out = text[os_:oe]
    vj = json.dumps(val, ensure_ascii=False)
    sp = _span(out, 'validation')
    out = out[:sp[0]] + vj + out[sp[1]:] if sp else out[:1] + '"validation": ' + vj + ', ' + out[1:]
    sp = _span(out, 'verification')
    vl = json.dumps(ver, ensure_ascii=False)
    out = out[:sp[0]] + vl + out[sp[1]:] if sp else out[:1] + '"verification": ' + vl + ', ' + out[1:]
    text = text[:os_] + out + text[oe:]
    # solution: replace an earlier validation step, else append one
    n2 = res['nulls'].get('shuffled refit', {}); n1 = res['nulls'].get('random keys', {})
    step = {'date': res['date'], 'kind': 'verification', 'technique': ['statistical test', 'language-model scoring'],
            'what': (f"{STEP_PREFIX}: {res['tokens']} tokens, {res['types']} types, {res['model']} order {ORDER}: "
                     f"reading {res['score']} per letter; "
                     + (f"random keys {n1.get('mean')} (z {n1.get('z')}); key annealed onto shuffled ciphertext best "
                        f"{n2.get('max')} (mean {n2.get('mean')}, z {n2.get('z')}); annealer on the real text "
                        f"{res.get('power')}. " if n1 else (res.get('na', '') + '. ' if res.get('na') else ''))
                     + f"Verdict: {res['verdict']}."),
            'result': {'pass': 'worked', 'weak': 'partial', 'fail': 'failed', 'too short': 'partial',
                       'underdetermined': 'partial', 'not applicable': 'partial'}[res['verdict']]}
    ss, se = _span(text, 'solution')
    sol = text[ss:se]
    steps = json.loads(sol)
    sj = json.dumps(step, ensure_ascii=False)
    old = [i for i, s in enumerate(steps) if str(s.get('what', '')).startswith(STEP_PREFIX)]
    if old:
        # find that step's object in the text by its what string
        w = json.dumps(steps[old[0]]['what'], ensure_ascii=False)
        i = sol.find(w); a = sol.rfind('{', 0, i); _, b = json.JSONDecoder().raw_decode(sol, a)
        sol = sol[:a] + sj + sol[b:]
    else:
        close = sol.rstrip().rfind(']')
        body = sol[:close].rstrip()
        ind = re.search(r'\n(\s*)\{', sol)
        pad = ind.group(1) if ind else '  '
        sol = body + (',' if steps else '') + '\n' + pad + sj + '\n' + pad[:-1] + ']'
    text = text[:ss] + sol + text[se:]
    json.loads(text)
    p.write_text(text, encoding='utf-8', newline='')

def record_na(folder, reason):
    p = cw.tdir(folder) / 'profile.json'
    text = p.read_text(encoding='utf-8')
    val = json.dumps({'date': datetime.date.today().isoformat(), 'verdict': 'not applicable', 'notes': reason},
                     ensure_ascii=False)
    os_, oe = _span(text, 'outcome')
    out = text[os_:oe]
    sp = _span(out, 'validation')
    out = out[:sp[0]] + val + out[sp[1]:] if sp else out[:1] + '"validation": ' + val + ', ' + out[1:]
    text = text[:os_] + out + text[oe:]
    json.loads(text)
    p.write_text(text, encoding='utf-8', newline='')

# ------------------------------------------------------------------ listing

def needing():
    rows = []
    for p in sorted((ROOT / 'targets').glob('*/profile.json')):
        if p.parent.name in cw.FAMOUS: continue
        o = json.loads(p.read_text(encoding='utf-8')).get('outcome', {})
        if o.get('class') not in ('read', 'read in part'): continue
        v = o.get('verification') if isinstance(o.get('verification'), list) else []
        weak = set(v) <= {'historical consistency', 'none', 'statistical test'}
        if o.get('method') in KEY_RECOVERY or weak:
            rows.append((p.parent.name, o.get('method'), (o.get('validation') or {}).get('verdict', '-'),
                         (p.parent / 'validation.tsv').exists()))
    return rows

def show(folder, res):
    if 'error' in res: print(f'{folder}: {res["error"]}'); return
    print(f'{folder}: {res["tokens"]} read tokens ({res["unread"]} unread), {res["types"]} types, '
          f'{res["tokens_per_type"]} tokens/type, {res["letters"]} letters, model {res["model"]}')
    print(f'  reading (key K)        {res["score"]:8.3f}   claimed per occurrence {res["claimed_score"]:.3f}, polyphony {res["polyphony"]}')
    for k, s in res.get('nulls', {}).items():
        print(f'  {k:22} {s["mean"]:8.3f}   sd {s["sd"]:.3f}  max {s["max"]:.3f}  z {s["z"]}  p {s["p"]}  (n={s["n"]})')
    if 'power' in res: print(f'  annealer power         {res["power"]:8.3f}   (real text, random start)')
    print(f'  verdict: {res["verdict"]}')

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--list']:
        rows = needing()
        print(f'{len(rows)} readings need validation; {sum(r[2] != "-" for r in rows)} validated, '
              f'{sum(r[3] for r in rows)} have validation.tsv')
        for f, m, v, has in rows: print(f'  {v:9} {"tsv" if has else "   "}  {f:22} {m}')
        sys.exit(0)
    if not a or a[0].startswith('-'): print(__doc__); sys.exit(2)
    folder = a[0]
    if '--na' in a:                                      # the test cannot run on this reading: record why
        record_na(folder, a[a.index('--na') + 1]); print(f'{folder}: recorded as not applicable'); sys.exit(0)
    pairs = a[a.index('--pairs') + 1] if '--pairs' in a else None
    res = validate(folder, pairs, quick='--quick' in a, control='--control' in a)
    if '--control' in a and 'error' not in res: res['file'] += ' (negative control: fake reading fitted to shuffled ciphertext)'
    if '--control' in a and '--write' in a: print('--control is never recorded'); a.remove('--write')
    show(folder, res)
    if 'error' in res: sys.exit(2)
    if '--write' in a:
        record(folder, res); print(f'  recorded in targets/{folder}/profile.json')
    sys.exit(0 if res['verdict'] in ('pass', 'too short', 'underdetermined', 'not applicable') else 1)
