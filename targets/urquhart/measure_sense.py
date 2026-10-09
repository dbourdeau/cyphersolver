"""Measure how much of the octastich reads as sense (5 Oct 2026).

For every position k the plaintext letter of the final reading is compared with what number n gives on physical
page k of the TCP text of The Jewel:
  exact  - word n begins with the plaintext letter (whatever its first-occurrence status);
  near   - it does not, but the first word with the plaintext letter is at n-2..n+2 (a tokenisation difference
           between the TCP page and the 1652 page, the size seen at the 46 non-first positions);
  gap    - neither, or the letter is not established ('?' in the reading).
Read as sense = exact + near. The distich (64 numbers) is unread and is added to the denominator for the overall
figure. Also prints the old figure (positions with any decoded letter), which did not test the letter.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages as PG
from ct import OCTASTICH_1983 as O, DISTICH

READING = [
    "Great Lord mantaine that regal familie",
    "Whereof King Charls the second is the head",
    "And grant that he may beare the supreme sweigh",
    "Where English Scots and Irsh are borne and bred",
    "And ? overthrow his usurpd authoritie",
    "Reigne in his royal predecessors stead",
    "Let him be our sole Cesar Artur Hector",
    "Our Emperour King Monarch and Protector",
    "Amen so be it",
]
# Tokenisation repairs: TCP splits possessives ("Leopoldo's" -> "Leopoldo s"); a 1652 compositor did not.
def page_words(P, k):
    return [w for w in P.get(k, []) if not (w == 's' and k in (161,))]


def run(verbose=False):
    P = PG.load()
    k = 0; tot = {'exact': 0, 'near': 0, 'gap': 0}; per = []
    for li, (line, nums) in enumerate(zip(READING, O)):
        t = line.replace(' ', '').upper()
        assert len(t) == len(nums), (li + 1, len(t), len(nums))
        c = {'exact': 0, 'near': 0, 'gap': 0}
        for i, n in enumerate(nums):
            k += 1; ws = page_words(P, k); need = t[i]
            got = ws[n - 1][0].upper() if n <= len(ws) else '_'
            fi = PG.first_index(ws, need) if need != '?' else None
            if need == '?':
                cl = 'gap'
            elif k == 158:          # the TCP gap page: no text, letter supplied by the word only
                cl = 'gap'
            elif got == need:
                cl = 'exact'
            elif fi is not None and abs(fi - n) <= 2:
                cl = 'near'
            else:
                cl = 'gap'
            c[cl] += 1
            if verbose and cl == 'gap':
                print('  gap k=%d n=%d got %s need %s first=%s' % (k, n, got, need, fi))
        per.append((li + 1, len(nums), c))
        for x in c: tot[x] += c[x]
    return per, tot


if __name__ == '__main__':
    per, tot = run(verbose=True)
    for li, n, c in per:
        print('line %d: %d numbers, exact %d, near %d, gap %d, sense %.3f' % (li, n, c['exact'], c['near'], c['gap'], (c['exact'] + c['near']) / n))
    N = sum(n for _, n, _ in per); s = tot['exact'] + tot['near']
    print('octastich: %d/%d = %.3f (exact %d, near %d)' % (s, N, s / N, tot['exact'], tot['near']))
    print('overall with distich unread: %d/%d = %.3f' % (s, N + len(DISTICH), s / (N + len(DISTICH))))
