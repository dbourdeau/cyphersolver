"""Does a printed text fit groups 147-576? Local alignment of the part-2 groups whose value is fixed by No. 205.

    python align_part2.py <text file>    # e.g. the archive.org text of Bernstorff, Deutschland und Amerika (1920)

Only words with a safe word form are used. Prints the best-scoring places in the text. On Bernstorff 1920
(deutschlandunda00berngoog_djvu.txt) the top place is telegram No. 205 itself, which shares the vocabulary of the
key; no place reaches a long run of matches, so the second text is not in that book.
"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
P = [x for l in open(os.path.join(HERE, 'ciphertext_part2.txt')) if l[0].isdigit() for x in l.split()]
W = {'6147': 'erachtens', '6918': 'im', '7436': 'dieses', '2373': 'wilson wilsons wilsonsche wilsonschen', '7937': 'mit',
     '7424': 'bis', '2012': 'ist', '2199': 'es', '1275': 'sich', '3371': 'vielleicht', '8172': 'daß dass',
     '7294': 'amerikaner', '8517': 'davor', '6356': 'werden', '8693': 'auf', '8796': 'hierzu', '5810': 'muß muss',
     '8335': 'aber', '9793': 'da', '4349': 'alles', '0197': 'von', '2765': 'er', '5132': 'niemals', '0270': 'hat',
     '4003': 'erst', '3285': 'letzterer', '2878': 'exzellenz', '4905': 'legen', '7184': 'kann', '2880': 'ich',
     '9076': 'für', '1026': 'halte', '4203': 'wenn', '6887': 'instruktionen',
     '2396': 'friedens friedensvermittlung friedensverhandlungen friedenskonferenz frieden', '4873': 'staaten',
     '9699': 'wird', '1589': 'hier'}
W = {k: set(v.split()) for k, v in W.items()}
seq = [W[g[-4:]] for g in P if g[-4:] in W]
text = re.sub(r'-\s*\n\s*', '', open(sys.argv[1], encoding='utf-8', errors='replace').read())
T = [t.lower() for t in re.findall(r'[a-zäöüßA-ZÄÖÜ]+', text)]
M, res = [0.0] * (len(seq) + 1), []
for t in T:
    N = [0.0] * (len(seq) + 1)
    for i in range(1, len(seq) + 1):
        N[i] = max(0, M[i - 1] + (3.0 if t in seq[i - 1] else -100), N[i - 1] - 0.6, M[i] - 0.25)
    M = N
    res.append(max(M))
print(len(seq), 'known groups used;', len(T), 'tokens')
out = []
for j in sorted(range(len(res)), key=lambda j: -res[j]):
    if all(abs(j - o) > 400 for o in out):
        out.append(j)
        print(round(res[j], 1), j, ' '.join(T[max(0, j - 25):j + 5]))
    if len(out) >= 8:
        break
