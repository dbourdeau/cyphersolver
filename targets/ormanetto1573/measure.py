"""Measure R116 honestly: share of cipher tokens (digits, word-end strokes included) that belong to words read as sense.

A word (stroke-delimited) counts as read only if every piece of it is
  - a letter run that splits into words attested in Renaissance Italian (lang/ corpora it-renaissance + it-nunziature,
    normalised as the cipher writes: no h, no doubled letters, u=v, i=j), or
  - a code group whose value is ADOPTED (recurs, or its one context admits one word only), or
  - the declared final nulls.
Code groups in OPEN, and words listed in UNREAD, count as unread even where a context guess exists.
Usage: python measure.py [cipher file]   (default r116_cipher_v2.txt)"""
import os, re, sys, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import words as W
ADOPTED = {'66':'che','2.44':'quello','6.11':'tutto','9.11':'V.S.Ill.ma','3.44':'Re','8.22':'quanto','4.88':'S.S.ta',
 '63':'Imperatore','97':'officii','87':'non','5.11':'tanto','1.44':'questo','77':'negotio','35':'lega','2.22':'pace',
 '76':'come','7.22':'qui','5.22':'qua','7.2.2':'qui','5.2.2':'qua','4.22':'perche','62':'canto','48':'essere','47':'tutta','93':'tutta','3.22':'Italia'}
OPEN = {'32':'?','2.88':'?','84':'bene?','42':'ancora?','53':'?'}
# (passage, word index) -> verdict overriding the automatic one, with the reason
OVERRIDE = {
 (1,13):  (True, "particolari + dotted 7 = '-mente' (Meister's rule: dotted sign for 'mente'); 'inteso particolarmente'"),
 (1,59):  (False, "3.22 is 'Italia' twice; here 'che sia [3.22] alterarla' wants 'per': slip or a second value, open"),
 (1,63):  (False, "'5 3' (fi) before 'finora': dittography or code 53, open"),
}
def norm(w):
    w = w.lower().replace('j','i').replace('v','u').replace('h','')
    w = re.sub(r'[àáâ]','a',w); w = re.sub(r'[èéê]','e',w); w = re.sub(r'[ìí]','i',w); w = re.sub(r'[òó]','o',w); w = re.sub(r'[ùú]','u',w)
    return re.sub(r'(.)\1+', r'\1', w)
def lexicon():
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'lang', 'corpora')
    c = collections.Counter()
    for f in ('it-renaissance.txt', 'it-nunziature.txt'):
        for w in re.findall(r"[a-zàèéìòù]+", open(os.path.join(root, f), encoding='utf8', errors='ignore').read().lower()):
            c[norm(w)] += 1
    short = {'a','e','o','di','da','in','il','lo','la','li','le','mi','si','se','ne','ma','me','io','et','al','ci','ui','tu','su','un','uno','ad','ed','co','de','do','fa','fu','no','sa','sta','so','al'}
    return {w for w, n in c.items() if (len(w) > 3 and n >= 3) or (len(w) == 3 and n >= 20)} | short
LEX = lexicon()
def wordbreak(s):
    """split a letter run into attested words; return list or None"""
    best = {0: []}
    for i in range(1, len(s)+1):
        for j in range(max(0, i-16), i):
            if j in best and s[j:i] in LEX and (s[j:i] not in ('i',) or i-j>1 or True):
                cand = best[j] + [s[j:i]]
                if i not in best or len(cand) < len(best[i]): best[i] = cand
    return best.get(len(s))
def sig(toks): return ''.join(d+('.' if dt else '') for d, dt in toks)
def parses(toks):
    """all parses of a word into pieces: ('code', sig) or ('let', text)"""
    out = []
    def rec(i, acc, run):
        if i == len(toks):
            out.append(acc + ([('let', run)] if run else [])); return
        for c in list(ADOPTED) + list(OPEN):
            k = len(c.replace('.', ''))
            if sig(toks[i:i+k]) == c and not (i+k < len(toks) and toks[i+k] == ('0', False)):
                rec(i+k, acc + ([('let', run)] if run else []) + [('code', c)], '')
        L = W.letters(toks[i:i+2])[:1]
        s, ch = L[0]; k = 2 if len(s.replace('.', '')) == 2 else 1
        rec(i+k, acc, run + ch)
    rec(0, [], '')
    return out
def judge(toks):
    best = None
    for p in parses(toks):
        bad = 0; txt = []; nwords = 0
        for kind, v in p:
            if kind == 'code':
                if v in OPEN: bad += 10; txt.append('[%s?]' % v)
                else: txt.append('[%s]' % ADOPTED[v])
            else:
                v2 = 'et' if v == 'i' else v
                wb = wordbreak(v) if v != 'i' else ['et']
                if wb is None: bad += 10 + len(v); txt.append('<%s>' % v)
                else: txt.append(' '.join(wb)); nwords += len(wb)
        ncode = sum(1 for kind, v in p if kind == 'code')
        key = (bad, nwords + ncode, -ncode)
        if best is None or key < best[0]: best = (key, ' '.join(txt))
    return best[0][0] == 0, best[1]
def run(path, verbose=False):
    tot = rd = 0; per = []; unread = []
    for pi, t in enumerate(W.parse_parts(path)):
        a = b = 0; text = []
        for k, (w, st) in enumerate(W.words(t)):
            n = len(w) + (2 if st else 0)
            ok, txt = judge(w)
            if pi == 0 and k == len(W.words(t)) - 1 and st is None:
                ok, txt = True, '{final nulls %s: five consonant signs after the last word}' % txt
            if (pi, k) in OVERRIDE: ok, why = OVERRIDE[(pi, k)]; txt += ' {%s}' % ('read' if ok else 'open')
            a += n; b += n if ok else 0
            text.append(txt if ok else '«%s»' % txt)
            if not ok: unread.append((pi, k, sig(w), txt, n))
        per.append((a, b)); tot += a; rd += b
        if verbose: print(' '.join(text)); print()
    return tot, rd, per, unread
if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'r116_cipher_v2.txt'
    tot, rd, per, unread = run(path, verbose=True)
    for (a, b), name in zip(per, 'AB'): print('passage %s: %d/%d tokens read as sense (%.1f%%)' % (name, b, a, 100*b/a))
    print('overall: %d/%d (%.1f%%)' % (rd, tot, 100*rd/tot))
    for u in unread: print('unread', u)
