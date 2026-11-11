"""lang/lm.py - the shared language models.

One normaliser and one character n-gram engine for every target, in place of the ~25 per-folder lm.py
scripts. Models are declared in models.json, their corpora in sources.json; see lang/README.md.

    import sys; sys.path.insert(0, '../..')       # from a target folder, targets/<name>/
    from lang import lm
    m = lm.load('fr-1600-letters')                # builds on first use, then cached in lang/cache/
    m.per_char('le roy vous escrit')              # mean log-probability per character
    m.score_idx(m.encode(text))                   # same, on a pre-encoded int array (for annealing loops)

Two engines, chosen by order:
  DenseLM   order <= 5: a numpy table of log P(c | previous order-1 chars), interpolated absolute
            discounting (d = 0.75) down to a smoothed unigram. Vectorised scoring; 27^5 floats = 57 MB.
  SparseLM  order 6-8: count dictionaries with the same discounting, scored char by char. Slower, smaller.
"""
import json, math, os, re, sys, unicodedata, collections
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CACHE = os.path.join(HERE, 'cache')
D = 0.75

# ---------------------------------------------------------------- normalisation

def _deaccent(t):
    t = t.replace('æ', 'ae').replace('œ', 'oe').replace('Æ', 'ae').replace('Œ', 'oe').replace('ß', 'ss')
    t = t.replace('ł', 'l').replace('Ł', 'L')  # Polish ł has no NFD decomposition and was dropped
    return ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c) != 'Mn')

def norm(text, scheme='modern', spaces=True):
    """Reduce text to the model alphabet: a-z, plus ' ' when spaces=True.

    modern   accents stripped, everything else kept
    early    early-modern spelling merged as the cipher clerks wrote it: j->i, v->u (and w kept)
    latin    as early, plus k->c, y->i, w->u (classical/humanist Latin)
    enigma   German in Enigma conventions: umlauts ae/oe/ue, sz, ch/ck -> q, x for space
    """
    t = text.lower()
    if scheme == 'enigma':
        t = t.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'sz')
        t = t.replace('ch', 'q').replace('ck', 'q')
    t = _deaccent(t)
    if scheme in ('early', 'latin'):
        t = t.replace('j', 'i').replace('v', 'u')
    if scheme == 'latin':
        t = t.replace('k', 'c').replace('y', 'i').replace('w', 'u')
    t = re.sub(r'[^a-z]+', ' ', t).strip()
    return t if spaces else t.replace(' ', '')

def alphabet(scheme='modern', spaces=True):
    drop = {'early': 'jv', 'latin': 'jvkyw'}.get(scheme, '')
    return (' ' if spaces else '') + ''.join(c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in drop)

# ---------------------------------------------------------------- engines

class DenseLM:
    def __init__(self, table, order, alpha, meta=None):
        self.lp, self.order, self.alpha, self.meta = table, order, alpha, meta or {}
        self.A = len(alpha)
        self.index = {c: i for i, c in enumerate(alpha)}

    @classmethod
    def build(cls, text, order, alpha, meta=None):
        A, idx = len(alpha), {c: i for i, c in enumerate(alpha)}
        x = np.fromiter((idx[c] for c in text if c in idx), dtype=np.int64)
        c1 = np.bincount(x, minlength=A).astype(np.float64) + 0.5
        prev = c1 / c1.sum()                                   # P(c), shape (A,)
        for k in range(2, order + 1):
            ctx = np.zeros(len(x) - k + 1, dtype=np.int64)
            for j in range(k):
                ctx = ctx * A + x[j:len(x) - k + 1 + j]
            c = np.bincount(ctx, minlength=A ** k).astype(np.float64).reshape(-1, A)
            tot = c.sum(1, keepdims=True)
            nz = (c > 0).sum(1, keepdims=True)
            low = np.tile(prev.reshape(-1, A), (A, 1))           # drop the oldest context char
            with np.errstate(divide='ignore', invalid='ignore'):
                prev = np.where(tot > 0, (np.maximum(c - D, 0) + D * nz * low) / np.maximum(tot, 1), low)
        return cls(np.log(prev).astype(np.float32).ravel(), order, alpha, meta)

    def encode(self, s):
        return np.fromiter((self.index[c] for c in s if c in self.index), dtype=np.int64)

    def score_idx(self, x):
        """Total log-probability of an encoded string (first order-1 chars are context only)."""
        k = self.order
        if len(x) < k:
            return 0.0
        ctx = np.zeros(len(x) - k + 1, dtype=np.int64)
        for j in range(k):
            ctx = ctx * self.A + x[j:len(x) - k + 1 + j]
        return float(self.lp[ctx].sum())

    def score(self, s):
        return self.score_idx(self.encode(s))

    def per_char(self, s):
        x = self.encode(s)
        return self.score_idx(x) / max(1, len(x) - self.order + 1)

    def save(self, path):
        np.save(path + '.npy', self.lp)
        json.dump(dict(self.meta, order=self.order, alpha=self.alpha, engine='dense'),
                  open(path + '.json', 'w'), indent=1)


class SparseLM:
    def __init__(self, counts, order, alpha, meta=None):
        self.cnts, self.order, self.alpha, self.meta = counts, order, alpha, meta or {}
        self.total = sum(counts[1].values())
        self.memo = {}

    @classmethod
    def build(cls, text, order, alpha, meta=None, prune=1):
        t = ''.join(c for c in text if c in alpha)
        cnts = [None] + [collections.Counter(t[i:i + n] for i in range(len(t) - n + 1)) for n in range(1, order + 1)]
        for n in range(4, order + 1):                        # singletons at high orders add size, not skill
            cnts[n] = collections.Counter({g: v for g, v in cnts[n].items() if v > prune})
        return cls(cnts, order, alpha, meta)

    def _p(self, ctx, ch):
        if not ctx:
            return (self.cnts[1][ch] + 0.5) / (self.total + 0.5 * len(self.alpha))
        lower = self._p(ctx[1:], ch)
        den = self.cnts[len(ctx)][ctx]
        if not den:
            return lower
        num = self.cnts[len(ctx) + 1][ctx + ch]
        return max(num - D, 0) / den + D * min(den, 10) / den * lower

    def logp(self, ctx, ch):
        key = ctx + ch
        v = self.memo.get(key)
        if v is None:
            v = self.memo[key] = math.log(self._p(ctx, ch))
        return v

    def score(self, s):
        s = ''.join(c for c in s if c in self.alpha)
        return sum(self.logp(s[max(0, i - self.order + 1):i], s[i]) for i in range(len(s)))

    def per_char(self, s):
        n = sum(c in self.alpha for c in s)
        return self.score(s) / max(1, n)

    def save(self, path):
        import pickle
        pickle.dump(self.cnts, open(path + '.pkl', 'wb'))
        json.dump(dict(self.meta, order=self.order, alpha=self.alpha, engine='sparse'),
                  open(path + '.json', 'w'), indent=1)

# ---------------------------------------------------------------- registry

def registry():
    return (json.load(open(os.path.join(HERE, 'models.json'), encoding='utf-8')),
            json.load(open(os.path.join(HERE, 'sources.json'), encoding='utf-8')))

def _cache_name(mid, order, spaces):
    return os.path.join(CACHE, f"{mid}.o{order}.{'sp' if spaces else 'ns'}")

def load(model_id, order=None, spaces=None, rebuild=False):
    """Load a registered model, building (and fetching its corpora) on first use."""
    models, _ = registry()
    if model_id not in models:
        raise KeyError(f"unknown model {model_id!r}; known: {', '.join(sorted(models))}")
    spec = models[model_id]
    order = order or spec.get('order', 5)
    spaces = spec.get('spaces', True) if spaces is None else spaces
    alpha = alphabet(spec['norm'], spaces)
    path = _cache_name(model_id, order, spaces)
    meta = json.load(open(path + '.json')) if not rebuild and os.path.exists(path + '.json') else None
    # a cache built from another recipe (sources or norm edited in models.json since) is stale: rebuild it.
    # Caches written before 'norm' was recorded are judged on their sources alone.
    if meta and meta.get('sources') == spec['sources'] and meta.get('norm', spec['norm']) == spec['norm']:
        if meta['engine'] == 'dense':
            return DenseLM(np.load(path + '.npy'), order, alpha, meta)
        import pickle
        return SparseLM(pickle.load(open(path + '.pkl', 'rb')), order, alpha, meta)
    from lang import corpora
    text = norm(corpora.text(spec['sources']), spec['norm'], spaces)
    meta = dict(model=model_id, chars=len(text), sources=spec['sources'], norm=spec['norm'])
    m = (DenseLM if order <= 5 else SparseLM).build(text, order, alpha, meta)
    os.makedirs(CACHE, exist_ok=True)
    m.save(path)
    return m

def best_language(text, candidates=None, order=4):
    """Rank registered models by per-character score of text (a quick language-ID for a decrypt)."""
    models, _ = registry()
    out = []
    for mid in candidates or [k for k, v in models.items() if v.get('language_id', True)]:
        m = load(mid, order=order, spaces=' ' in text)
        out.append((round(m.per_char(norm(text, models[mid]['norm'], ' ' in text)), 3), mid))
    return sorted(out, reverse=True)

if __name__ == '__main__':
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    args = [a for a in sys.argv[1:] if a != '--rebuild']          # the flag may come anywhere, also first
    mid = args[0] if args else 'fr-1600-letters'
    m = load(mid, rebuild='--rebuild' in sys.argv)
    print(mid, m.meta.get('chars'), 'chars, order', m.order)
    for s in args[1:]:
        print(round(m.per_char(norm(s, registry()[0][mid]['norm'], ' ' in m.alpha)), 3), s)
