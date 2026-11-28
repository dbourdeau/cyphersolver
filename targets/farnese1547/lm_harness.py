"""lm_harness.py -- Italian 16th-c. 5-gram LM, word-DP coverage scorer, and null-control harness
for Farnese 2339 (c. 78r) cryptanalysis. Writes cache ONLY under theories/cache/.
"""
import collections
import glob
import gzip
import json
import math
import os
import pathlib
import random
import re
import sys

import numpy as np

def _find_repo() -> pathlib.Path:
    here = pathlib.Path(__file__).resolve().parent
    for cand in [here] + list(here.parents):
        if (cand / 'lang' / 'lm.py').is_file():
            return cand
    raise FileNotFoundError('Cannot locate cyphersolver repository root')

REPO = _find_repo()
sys.path.insert(0, str(REPO))
from lang.lm import DenseLM, norm, alphabet

HERE = pathlib.Path(__file__).parent
CACHE = HERE / 'cache'

IT_WORDS_FILTER = set(
    'che di la il non per con si se et le della delle del dello alla alle quello questo questa sua suo '
    'ma sono essere da dal dalla come anche ancora tutto tutti molto piu cosa cose nostro vostra signore '
    'stato haver havere fatto quale quali questi quelli loro noi voi lui lei gli una uno mi ti ci vi ne '
    'lo li ha hanno era erano sia siano perche poi qui qua ogni altro altra altri senza sopra sotto '
    'dopo prima tanto quanto bene male dio papa imperatore francia roma parma piacenza eccellenza santita maesta'.split()
)
EN_DE_STOP = set(
    'the and of to in is that for with on was as by this from are not be it have or an which were been '
    'der die das und ist nicht von zu den dem des mit auf ein eine'.split()
)


def _gather_italian_corpus():
    chunks = []
    for pj in sorted(REPO.glob('targets/*/profile.json')):
        try:
            d = json.load(open(pj, encoding='utf-8'))
        except Exception:
            continue
        docs = d.get('documents', [])
        if not any(doc.get('language') == 'Italian' for doc in docs):
            continue
        years = [doc.get('year', 9999) for doc in docs if isinstance(doc.get('year'), int)]
        if years and min(years) > 1650:
            continue
        tdir = pj.parent
        cand_files = set()
        for t in d.get('outcome', {}).get('texts', []):
            for k in ('decryption', 'contemporary', 'reading'):
                fn = t.get(k)
                if isinstance(fn, str) and fn.endswith('.txt'):
                    cand_files.add(tdir / fn)
        for fn in sorted(tdir.glob('*.txt')) + sorted(tdir.glob('texts/*.txt')):
            if any(w in fn.name.lower() for w in ('reading', 'plaintext', 'decryption', 'cleartext')):
                cand_files.add(fn)
        for fp in sorted(cand_files):
            if not fp.exists():
                continue
            txt = fp.read_text(encoding='utf-8', errors='ignore')
            for line in txt.splitlines():
                line_clean = re.sub(r'\[[^\]]*\]|\{[^}]*\}|[?*_#`<>|]', ' ', line)
                words = re.findall(r"[A-Za-zÀ-ÿ]+", line_clean.lower())
                if len(words) < 6:
                    continue
                it_hits = sum(w in IT_WORDS_FILTER for w in words)
                bad_hits = sum(w in EN_DE_STOP for w in words)
                if it_hits >= 1 and it_hits >= 2 * bad_hits:
                    chunks.append(line_clean)
    return '\n'.join(chunks)


def load_it_lms():
    CACHE.mkdir(parents=True, exist_ok=True)
    ns_npy = CACHE / 'it_early_nospace_o5.npy'
    sp_npy = CACHE / 'it_early_spaced_o5.npy'
    if ns_npy.exists() and sp_npy.exists():
        def _load(prefix):
            meta = json.load(open(str(prefix) + '.json'))
            return DenseLM(np.load(str(prefix) + '.npy'), meta['order'], meta['alpha'], meta)
        return _load(CACHE / 'it_early_nospace_o5'), _load(CACHE / 'it_early_spaced_o5')

    raw = _gather_italian_corpus()
    txt_sp = norm(raw, scheme='early', spaces=True)
    txt_ns = norm(raw, scheme='early', spaces=False)
    print(f'[lm_harness] Built Italian corpus: {len(txt_sp)} spaced chars, {len(txt_ns)} nospace chars')

    lm_ns = DenseLM.build(txt_ns, order=5, alpha=alphabet('early', spaces=False), meta={'name': 'it_early_nospace'})
    lm_sp = DenseLM.build(txt_sp, order=5, alpha=alphabet('early', spaces=True), meta={'name': 'it_early_spaced'})
    lm_ns.save(str(CACHE / 'it_early_nospace_o5'))
    lm_sp.save(str(CACHE / 'it_early_spaced_o5'))
    return lm_ns, lm_sp


class LexiconScorer:
    """Word-DP segmentation & coverage using cyphersolver's 6.75M-token Italian lexicon."""
    def __init__(self):
        raw = json.load(gzip.open(REPO / 'lang/lexicons/it.json.gz', 'rt', encoding='utf-8'))
        self.freq = collections.Counter()
        for w, c in raw.items():
            nw = norm(w, scheme='early', spaces=False)
            if nw:
                self.freq[nw] += c
        # Add 1547 Farnese/Parma/Piacenza diplomatic terms not always well-represented
        for extra in ('piacenza', 'parma', 'farnese', 'gonzaga', 'doria', 'ferrante', 'alessandro',
                      'eccellenza', 'santita', 'maesta', 'imperatore', 'pontefice', 'cardinale'):
            self.freq[norm(extra, 'early', False)] += 500
        self.total = sum(self.freq.values())
        self.logp = {w: math.log(c / self.total) for w, c in self.freq.items() if c >= 3}
        self.maxlen = max((len(w) for w in self.logp), default=15)

    def segment(self, text_ns):
        s = norm(text_ns, scheme='early', spaces=False)
        n = len(s)
        if n == 0:
            return [], 0.0, 0.0
        dp = [-1e18] * (n + 1)
        bp = [(0, False)] * (n + 1)
        dp[0] = 0.0
        for i in range(n):
            if dp[i] < -1e17:
                continue
            # fallback 1-char unknown penalty
            sc1 = dp[i] - 18.0
            if sc1 > dp[i + 1]:
                dp[i + 1] = sc1
                bp[i + 1] = (i, False)
            for L in range(1, min(self.maxlen, n - i) + 1):
                w = s[i:i + L]
                lp = self.logp.get(w)
                if lp is not None:
                    # slight length bonus so multi-letter real words beat single-letter chains
                    sc = dp[i] + lp + 1.5 * (L - 1)
                    if sc > dp[i + L]:
                        dp[i + L] = sc
                        bp[i + L] = (i, True)
        words = []
        cov4 = 0
        cov5 = 0
        idx = n
        while idx > 0:
            prev, known = bp[idx]
            w = s[prev:idx]
            words.append((w, known))
            if known:
                if len(w) >= 4:
                    cov4 += len(w)
                if len(w) >= 5:
                    cov5 += len(w)
            idx = prev
        words.reverse()
        return words, cov4 / n, cov5 / n


def score_with_null_controls(score_fn, stream, n_controls=20, seed=1547):
    """Run score_fn(real_stream) and score_fn(shuffled_stream) x n_controls.
    Returns dict with real, ctrl_mean, ctrl_std, z, ctrls.
    """
    real = score_fn(stream)
    rng = random.Random(seed)
    ctrls = []
    for _ in range(n_controls):
        shuf = list(stream)
        rng.shuffle(shuf)
        ctrls.append(score_fn(shuf))
    mean = sum(ctrls) / len(ctrls)
    var = sum((x - mean) ** 2 for x in ctrls) / max(1, len(ctrls) - 1)
    std = math.sqrt(var) if var > 0 else 1e-9
    z = (real - mean) / std
    return {
        'real': real,
        'ctrl_mean': mean,
        'ctrl_std': std,
        'ctrl_max': max(ctrls),
        'z': z,
        'ctrls': ctrls,
    }


if __name__ == '__main__':
    lm_ns, lm_sp = load_it_lms()
    lex = LexiconScorer()
    sample = (REPO / 'targets/farnese1547/cleartext_79r.txt').read_text(encoding='utf-8')
    sample_ns = norm(sample, 'early', False)
    words, cov4, cov5 = lex.segment(sample_ns)
    print(f'79r clear: len={len(sample_ns)}, lm_ns/ch={lm_ns.per_char(sample_ns):.3f}, cov4={cov4:.3f}, cov5={cov5:.3f}')
    res = score_with_null_controls(
        lambda seq: lm_ns.per_char(''.join(seq)),
        list(sample_ns),
        n_controls=20,
    )
    print(f"Null control test on 79r chars: real={res['real']:.3f} ctrl={res['ctrl_mean']:.3f}±{res['ctrl_std']:.3f} z={res['z']:.2f}")
