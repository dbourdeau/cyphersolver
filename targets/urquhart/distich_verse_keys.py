"""5 Oct 2026: distich (1834 numbers) as word- and letter-index keys into the short texts printed with the two
cryptograms. Prints each candidate decode and its en-1640s score per char (English text ~ -5.2)."""
import sys, os, re, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from ct import DISTICH
from lang import lm
D = list(DISTICH); D[55] = 38          # 1834 print: 5.38.5 where Schmeh has 5.33.5
T = {
 'verse6': "Of carping Zoil and despightful Momus Let th' innate baseness be exiled from us Who worthily would hear or read this book For if upon this Cyphral Distich look An honest skilful man he'll therein finde His own heart's wishes and the Author's minde",
 'parva': "Parva peto debens minus et plus spondeo at istis Plura dabit genio spero Camoena meo",
 'parvaEn': "Little I ask I owe less on the score I promise much yet hope to perform more",
 'octa': "Great Lord mantaine that regal familie Whereof King Charls the second is the head And grant that he may beare the supreme sweigh Where English Scots and Irsh are borne and bred And overthrow his usurpd authoritie Reigne in his royal predecessors stead Let him be our sole Cesar Artur Hector Our Emperour King Monarch and Protector Amen so be it",
 'decaverse': "To this Octastick if you will subjoyn A Decagram of this same stuff of mine All gather'd out of my Exskybalorum You'll finde a Rule by which with great decorum You may most comfortably regulate Your actions thoughts and speeches and know that I love an Aphaeresified treason Better then any Prosthesized Reason",
}
M = lm.load('en-1640s')
def score(s):
    s = s.lower().replace('_', '')
    return M.score(s) / max(1, len(s))
cands = {k: v for k, v in T.items()}
cands['verse6+parva'] = T['verse6'] + ' ' + T['parva']
cands['verse6+parva+parvaEn'] = T['verse6'] + ' ' + T['parva'] + ' ' + T['parvaEn']
base = ['verse6', 'parva', 'parvaEn']
for a, b in itertools.permutations(['verse6', 'octa', 'decaverse'], 2):
    cands[a + '+' + b] = T[a] + ' ' + T[b]
for a in base:
    cands[a + '+octa+decaverse'] = T[a] + ' ' + T['octa'] + ' ' + T['decaverse']
    cands['octa+decaverse+' + a] = T['octa'] + ' ' + T['decaverse'] + ' ' + T[a]
res = []
for name, t in cands.items():
    w = re.findall(r"[A-Za-z']+", t); L = re.sub('[^A-Za-z]', '', t)
    for mode, src in (('word', w), ('letter', L)):
        for wrap in (False, True):
            out = ''
            for n in D:
                if n <= len(src): x = src[n - 1]
                elif wrap: x = src[(n - 1) % len(src)]
                else: x = '_'
                out += x[0].upper()
            res.append((score(out), name, mode, 'wrap' if wrap else 'nowrap', len(src), out))
res.sort(reverse=True)
for r in res: print('%.3f %-28s %-6s %-6s len=%d %s' % r)
print('reference: English sentence', round(score('ogodupholdkingcharlsthesecondandmakehimthesupremeruler'), 3))
