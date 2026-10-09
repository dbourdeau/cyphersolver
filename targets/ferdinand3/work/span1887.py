import sys, itertools, heapq
sys.path.insert(0, r'C:\Users\dbour\cypher')
from lang import lm
M = lm.load('la', order=5, spaces=False)
L = 'adperagendumhuncipsorumque'; R = 'negociumarmorumsuorummotu'
# span tokens: 4 ib ad p xir m/ a+ 4 4) xir 4 ten h^ga != S e~
opts = [['m','n','s','i',''], ['mi'], ['na'], ['n'], ['ti','tu'], ['r'], ['i','u'], ['m','n','s',''], ['a','e','i','o','u','s','t','c','l','n','r',''],
        ['ti','tu'], ['m','n','s',''], ['re'], ['l','d','i','g','',"t","s","c"], ['a'], ['t'], ['i','io','o','e','u','is','us','','um','a']]
best = []
for combo in itertools.product(*opts):
    s = ''.join(combo)
    sc = M.score(L + s + R) - M.score(L + R) * 0  # absolute
    heapq.heappush(best, (sc, s))
    if len(best) > 25: heapq.heappop(best)
for sc, s in sorted(best, reverse=True): print(round(sc, 1), s)
