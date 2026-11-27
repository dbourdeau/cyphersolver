"""Hypothesis (a'): is the block verses 1-5 of the riddle under a NEW key? Hill-climb a sign->letter map (many-to-one
allowed) maximising the LCS between the decoded block and the plaintext; compare with word-shuffled controls."""
import random, sys
V = ('فما وليد ربا في شهر مولده وعاد فيه قديم السن مدخلا وما ثياب قد خيطت بلا ابر وما ادبرها سلك ولا فتلا '
     'وما فتى ان تهيبا هيب جانبه ولا يهاب اذا في الملبس انتعلا وما جبان لما عان في شرف ان لحظا اساعة مبناهما بطلا '
     'وما مساكن ترتاح القلوب لها يريدها القوم قد كانت لهم حللا')
lines = [l.split()[1:] for l in open('transcription.txt', encoding='utf8') if not l.startswith('#')]
def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]
def run(toks, plain, seed, iters):
    random.seed(seed); syms = sorted(set(toks)); letters = sorted(set(plain))
    k = {s: random.choice(letters) for s in syms}
    f = lambda: lcs([k[t] for t in toks], plain); cur = f()
    for _ in range(iters):
        s = random.choice(syms); o = k[s]; k[s] = random.choice(letters); n = f()
        if n >= cur: cur = n
        else: k[s] = o
    return cur, k
if __name__ == '__main__':
    rev = len(sys.argv) > 1 and sys.argv[1] == 'rev'
    toks = [t for l in lines for t in (l[::-1] if rev else l) if t != '|']
    if rev: toks = toks  # lines kept in order, signs within each line reversed
    words = V.split(); plain = V.replace(' ', '')
    print('direction', 'L->R' if rev else 'R->L', 'signs', len(toks), 'letters', len(plain))
    for trial in range(3):
        sc, k = run(toks, plain, trial, 1500)
        print('true order  seed', trial, 'LCS', sc, round(sc / len(plain), 3), flush=True)
    for trial in range(3):
        w = words[:]; random.seed(100 + trial); random.shuffle(w)
        sc, _ = run(toks, ''.join(w), trial, 1500)
        print('word-shuffled control', trial, 'LCS', sc, round(sc / len(plain), 3), flush=True)
