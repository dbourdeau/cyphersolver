# Sense measure for malvezzi1548 (5 Oct 2026).
# The old figure (0.83) was a mark count: a word was "read" unless it carried [?] / [..]; it never asked whether the
# text made Latin, and it left out p. 1 lines 1-8. This measure works on reading_full.txt (every ciphered passage,
# nulls removed) and counts a plaintext word as read only when
#   (1) it is marked read (plain, {slip-corrected} or <code word>), not [unread]; and
#   (2) for a non-code word: the word occurs in the Latin corpus (lang 'la', latin normalisation) or scores as a
#       Latin word form (WTHR below), AND the 9-word
#       window centred on it scores above THR per character under the 'la' 5-gram model.
# THR is the 2nd percentile of the same window score over 2000 random 9-word windows of the Latin corpus, so real
# Latin passes ~98% of the time. Control: the reading with its letters shuffled inside each word.
import os, sys, re, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M = lm.load('la')
N = lambda s: lm.norm(s, 'latin')
corpus = N(open(os.path.join('..', '..', 'lang', 'corpora', 'la-gutenberg.txt'), encoding='utf8', errors='ignore').read())
cw = corpus.split()
LEX = set(cw)
random.seed(1)
cal = []
for _ in range(2000):
    i = random.randrange(len(cw) - 9)
    cal.append(M.per_char(' '.join(cw[i:i + 9])))
cal.sort()
THR = cal[int(0.02 * len(cal))]
# word test: in the corpus vocabulary, or the word alone (with its spaces) scores above the 2nd percentile of
# corpus word tokens of 5+ letters that occur only once (rare inflected forms, the hard case)
from collections import Counter
cnt = Counter(cw)
rare = [w for w, c in cnt.items() if c == 1 and len(w) >= 5]
random.shuffle(rare)
wc = sorted(M.per_char(' ' + w + ' ') for w in rare[:3000])
WTHR = wc[int(0.02 * len(wc))]
def wordok(w):
    return w in LEX or M.per_char(' ' + w + ' ') > WTHR

def parse():
    pages = {}
    for line in open('reading_full.txt', encoding='utf8'):
        if line.startswith('#') or '|' not in line: continue
        p, t = line.split('|', 1)
        for tok in t.split():
            if tok.startswith('['): kind, w = 'U', tok.strip('[]')
            elif tok.startswith('{'): kind, w = 'S', tok.strip('{}')
            elif tok.startswith('<'): kind, w = 'C', tok.strip('<>')
            else: kind, w = 'R', tok
            pages.setdefault(p.strip(), []).append((kind, w))
    return pages

def judge(toks, W=4):
    words = [N(w) for _, w in toks]
    ok = []
    for i, (k, w) in enumerate(toks):
        if k == 'U': ok.append(False); continue
        if k == 'C': ok.append(True); continue
        win = ' '.join(words[max(0, i - W): i + W + 1])
        ok.append(wordok(words[i]) and M.per_char(win) > THR)
    return ok

if __name__ == '__main__':
    pages = parse()
    print(f'THR window = {THR:.3f}, WTHR word = {WTHR:.3f}')
    T = S = 0
    for p, toks in pages.items():
        ok = judge(toks)
        T += len(toks); S += sum(ok)
        bad = [w for (k, w), o in zip(toks, ok) if not o]
        print(f'{p}: {sum(ok)}/{len(toks)} = {sum(ok)/len(toks):.3f}  not counted: {" ".join(bad)}')
    print(f'overall: {S}/{T} = {S/T:.3f}')
    marks = sum(k != 'U' for toks in pages.values() for k, _ in toks)
    print(f'mark count only (old method on the new file): {marks}/{T} = {marks/T:.3f}')
    slips = sum(k == 'S' for toks in pages.values() for k, _ in toks)
    print(f'of which slip-corrected words: {slips}; code words: {sum(k == "C" for toks in pages.values() for k, _ in toks)}')
    random.seed(2)
    ctl = [[(k, ''.join(random.sample(w, len(w))) if k != 'C' else w) for k, w in toks] for toks in pages.values()]
    cs = sum(sum(judge(t)) for t in ctl)
    print(f'control (letters shuffled within words): {cs}/{T} = {cs/T:.3f}')
