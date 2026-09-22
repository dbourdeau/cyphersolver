"""Measure how much of the matignon1586 target is read, per leaf, from the transcription files.

Usage:  python measure.py            (decodes are cached in measure_cache/, delete it to redo)
        python measure.py --control  (also runs the scrambled-key control)

Needs lm.pkl and corpus_words.txt (git-ignored; built by mklm.py from ../bethune/xivrey/).

THE RULE (what counts as a read cipher token)
---------------------------------------------
The unit is the cipher token: one figure or one code group, as written in the transcription files
(`cipher_f143.txt`, `f143v_cipher.txt`, `f1xx_cipher.txt`, one manuscript line per file line).

1. Keyed or not. A token is KEYED if key.json gives it a value. A token that key.json does not
   list (a shape the reader could not match to the key), `BOX` (an illegible or unrecognised mark),
   any token containing `?`, and every code group whose value is unidentified (`+` in key.json, or
   `*` other than 76 = le roi de Navarre) is UNKEYED, i.e. unread, whatever the decoder puts there.
2. Read as sense. Each leaf is decoded line by line exactly as dec.py does (beam search over the
   key's candidate letters with the period-French 6-gram model; unkeyed tokens may take any letter),
   the lines are joined and segmented into words with the corpus lexicon (solve.segment). A word is
   LEXICAL if it has at least two letters and occurs at least MINCOUNT times in the corpus, or is
   one of the one-letter words a / y. A SENSE RUN is a maximal stretch of at least MINWORDS
   consecutive lexical words with at least MINLETTERS letters between them. Code groups with a
   known value are words of the run like any other.
3. A token is READ if it is keyed and every plaintext letter it produced lies inside a sense run.
   A token that is unkeyed but falls inside a sense run is counted separately as CONTEXT (the
   language model supplied a plausible letter); it is NOT counted as read.
4. Untranscribed lines are unread. Their token count is estimated as (missing lines) x (the leaf's
   mean tokens per transcribed line), or 30 tokens a line for a leaf with no transcription at all.
   Those estimates are flagged `est` in the output.

The rule is deliberately mechanical and generous in one way (a sense run of short common words can
arise by chance), so two floors are reported with it: f. 110, which is declared unread (its decode
is noise), and a scrambled-key control (--control: the key's values permuted among its single-letter
figures, same decoder, same rule). The corrected fraction is (measured - floor) / (1 - floor), floor
taken from the scrambled control of the same leaf.
"""
import json, os, sys, random, pickle, math
from solve import logp, segment, WORDS, AL as ALS

MINCOUNT = 20
MINWORDS = 3
MINLETTERS = 10
AL = list(ALS)

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

# leaf, transcription file(s), cipher lines on the leaf (counted on the image), note
LEAVES = [
    ('fr.15572 f.110',  ['f110_cipher.txt'],   54, '37 of 54 rows transcribed (f110_status.md); declared unread'),
    ('fr.15572 f.123r', ['f123r_cipher.txt'],  None, ''),
    ('fr.15572 f.123v', ['f123v_cipher.txt'],  None, ''),
    ('fr.15572 f.124r', ['f124r_cipher.txt'],  None, ''),
    ('fr.15572 f.124v', ['f124v_cipher.txt'],  None, ''),
    ('fr.15572 f.143r', ['cipher_f143.txt'],   None, ''),
    ('fr.15572 f.143v', ['f143v_cipher.txt'],  None, ''),
    ('fr.15572 f.150',  ['f150_cipher.txt'],   None, ''),
    ('fr.15572 f.154',  ['f154_cipher.txt'],   None, ''),
    ('fr.15572 f.173',  ['f173_cipher.txt'],   None, ''),
    ('fr.15572 f.196',  ['f196_cipher.txt'],   31, 'part-line after "auquel" + 30 full lines; the first three full lines and the 13th ("mo£7om...") untranscribed'),
    ('fr.15572 f.201',  ['f201_cipher.txt'],   None, ''),
    ('fr.15571 f.177',  ['f177_cipher.txt'],   29, '29 cipher lines on canvas 185 right, 24 transcribed'),
    ('fr.15572 f.276',  [],                    27, 'Cipher-3 (Matignon); canvas 285 right; not transcribed'),
    ('fr.15571 f.179',  [],                    25, 'Cipher-3 (Matignon); canvas 187 left, bound upside down; not transcribed'),
]

KEY = json.load(open('key.json', encoding='utf-8'))


def keyed(tok):
    if '?' in tok or tok not in KEY:
        return False
    v = KEY[tok]
    if v == ['+']:
        return False
    if v == ['*'] and tok != '76':
        return False
    return True


def cand_for(tok, key):
    if tok in key:
        v = key[tok]
        if tok == '76':
            return ['roidenauarre']
        if v in (['+'], ['*']):
            return ['+']
        return v
    return AL


def beam_aligned(tokens, key, width=300):
    """dec.py's beam, keeping how many plaintext letters each token produced."""
    N = 6
    beams = [('', 0.0, ())]
    for t in tokens:
        opts = cand_for(t, key)
        nb = []
        for txt, sc, lens in beams:
            for o in opts:
                s = sc; c = txt
                for ch in o:
                    if ch == '+':
                        c = c + ch
                        continue
                    s += logp(c.replace('+', ''), ch); c = c + ch
                nb.append((c, s, lens + (len(o),)))
        nb.sort(key=lambda x: -x[1])
        seen = set(); out = []
        for txt, sc, lens in nb:
            k = txt[-(N - 1):]
            if k in seen:
                continue
            seen.add(k); out.append((txt, sc, lens))
            if len(out) >= width:
                break
        beams = out
    return beams[0][0], beams[0][2]


def lexical(w):
    if w in ('a', 'y'):
        return True
    return len(w) >= 2 and WORDS.get(w, 0) >= MINCOUNT


def sense_mask(text):
    """text: decoded letters with '+' for unknown codes. Returns per-character bool."""
    mask = [False] * len(text)
    # split on '+' (an unidentified code breaks the sentence as far as this measure goes)
    pos = 0
    for chunk in text.split('+'):
        if chunk:
            words = segment(chunk).split(' ')
            spans = []; p = pos
            for w in words:
                spans.append((p, p + len(w), lexical(w))); p += len(w)
            i = 0
            while i < len(spans):
                if not spans[i][2]:
                    i += 1; continue
                j = i
                while j < len(spans) and spans[j][2]:
                    j += 1
                nlet = spans[j - 1][1] - spans[i][0]
                if j - i >= MINWORDS and nlet >= MINLETTERS:
                    for k in range(spans[i][0], spans[j - 1][1]):
                        mask[k] = True
                i = j
        pos += len(chunk) + 1
    return mask


def decode_leaf(files, key, tag):
    os.makedirs('measure_cache', exist_ok=True)
    cf = os.path.join('measure_cache', tag + '.json')
    if os.path.exists(cf):
        return json.load(open(cf, encoding='utf-8'))
    lines = []
    for f in files:
        for ln in open(f, encoding='utf-8'):
            if ln.strip():
                lines.append(ln.split())
    res = []
    for toks in lines:
        txt, lens = beam_aligned(toks, key)
        res.append({'tokens': toks, 'text': txt, 'lens': list(lens)})
    json.dump(res, open(cf, 'w', encoding='utf-8'))
    return res


def score(res):
    text = ''.join(r['text'] for r in res)
    mask = sense_mask(text)
    n = read = ctx = unkeyed = 0
    p = 0
    for r in res:
        for t, L in zip(r['tokens'], r['lens']):
            inside = L > 0 and all(mask[p:p + L])
            n += 1
            if keyed(t):
                if inside:
                    read += 1
            else:
                unkeyed += 1
                if inside:
                    ctx += 1
            p += L
    return n, read, ctx, unkeyed, text, mask


def scrambled(seed):
    rng = random.Random(seed)
    single = [k for k, v in KEY.items() if len(v) == 1 and len(v[0]) == 1 and v[0] not in '+*']
    vals = [KEY[k] for k in single]
    rng.shuffle(vals)
    k2 = dict(KEY)
    for k, v in zip(single, vals):
        k2[k] = v
    return k2


def main():
    control = '--control' in sys.argv
    rows = []
    T = dict(tok=0, est=0, read=0, ctx=0, unkeyed=0, trans=0)
    print(f"rule: keyed token inside a run of >= {MINWORDS} lexical words (corpus count >= {MINCOUNT}) "
          f"and >= {MINLETTERS} letters\n")
    hdr = f"{'leaf':17} {'lines':>9} {'tokens':>10} {'keyed':>6} {'read':>6} {'ctx':>5} {'read/trans':>10} {'read/leaf':>9}"
    if control:
        hdr += f" {'scramb':>7} {'corr':>6}"
    print(hdr)
    for name, files, page_lines, note in LEAVES:
        tag = name.replace(' ', '_').replace('.', '')
        if files:
            res = decode_leaf(files, KEY, tag)
            n, read, ctx, unk, text, mask = score(res)
            tl = len(res)
            pl = page_lines or tl
            est = round((pl - tl) * n / tl) if pl > tl else 0
        else:
            n = read = ctx = unk = 0; tl = 0; pl = page_lines; est = 30 * pl
        tot = n + est
        fr_t = read / n if n else 0.0
        fr_l = read / tot if tot else 0.0
        line = (f"{name:17} {tl:>4}/{pl:<4} {n:>5}{('+' + str(est) + 'e') if est else '':>5} "
                f"{(n - unk):>6} {read:>6} {ctx:>5} {fr_t:>10.3f} {fr_l:>9.3f}")
        row = dict(leaf=name, lines_transcribed=tl, lines_on_leaf=pl, tokens_transcribed=n,
                   tokens_untranscribed_est=est, keyed=n - unk, read=read, context_only=ctx,
                   read_of_transcribed=round(fr_t, 3), read_of_leaf=round(fr_l, 3), note=note)
        if control and files:
            fl = []
            for s in range(3):
                r2 = decode_leaf(files, scrambled(s), tag + f'_scr{s}')
                fl.append(score(r2)[1] / n)
            floor = sum(fl) / len(fl)
            corr = max(0.0, (fr_t - floor) / (1 - floor))
            row['scrambled_floor'] = round(floor, 3); row['corrected_of_transcribed'] = round(corr, 3)
            line += f" {floor:>7.3f} {corr:>6.3f}"
        print(line)
        rows.append(row)
        T['tok'] += n; T['est'] += est; T['read'] += read; T['ctx'] += ctx; T['unkeyed'] += unk
    tot = T['tok'] + T['est']
    print()
    print(f"transcribed tokens {T['tok']}, untranscribed (estimated) {T['est']}, whole target ~{tot}")
    print(f"keyed {T['tok'] - T['unkeyed']} ({(T['tok'] - T['unkeyed']) / T['tok']:.3f} of transcribed)")
    print(f"read {T['read']}: {T['read'] / T['tok']:.3f} of transcribed, {T['read'] / tot:.3f} of the whole target")
    print(f"context-only (unkeyed but inside a sense run, not counted): {T['ctx']}")
    if control:
        corr_read = sum(r.get('corrected_of_transcribed', 0) * r['tokens_transcribed'] for r in rows)
        print(f"scrambled-control corrected: {corr_read / T['tok']:.3f} of transcribed, {corr_read / tot:.3f} of the whole target")
    json.dump(dict(rule=__doc__.split('THE RULE')[1].split('"""')[0].strip(), leaves=rows, totals=T),
              open('measure.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
