"""Rebuild the decryption from transcription + key and check a marked reading against it, group by group.
python scripts/check_marks_litB.py key_1741.tsv transcription_litB_all.txt marked_litB.txt
(scripts/check_marks.py with two marks added for Lit. B, below.)
Fails (exit 1) on any piece that departs from the key value without a mark, on a piece with no group, or on a group
with no piece. Prints word counts.
{x/...} = a group whose key value x gives no sense here: counted as a hole (added for catalogue 2242).
{x/?y} = key value x gives no sense here and y is guessed from context: counted as a guess (added after the review). A word broken across rows (trailing "+", then leading "+") is counted once.
Comparison ignores case and treats i/j and u/v/w as one letter (the code does not separate them)."""
import sys, re
sys.path.insert(0, __file__.rsplit('scripts', 1)[0] + 'scripts')
from decrypt_litB import load_key, tokens
CODES = {'paix_', 'grefwen', 'storviziren', 'ottporten', 'hof', 'ambassadeur', 'frankrike', 'swerige', 'ryssland', 'tractat',
         'sultan', 'fred', 'prince'}
def n(s): return s.lower().replace('j', 'i').replace('v', 'u').replace('w', 'u')
def mech_seq(key, rest):
    out = []
    for t in tokens(rest):
        if t[0] == 'clear': out.append(('clear', t[1]))
        elif t[0] == 'p': out.append(('p', t[1]))
        else: out.append(('g', (key[t[1]] if t[1] in key else '[%s]' % t[1]) + ("'" if t[3] else ''), t[1], t[2]))
    return out
SPLIT = re.compile(r'\+(?![^{}\[\]]*[}\]])')
def main():
    key = load_key(sys.argv[1]); mech = {}
    for l in open(sys.argv[2], encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        lab, rest = l.split(' ', 1); mech[lab] = mech_seq(key, rest.strip())
    errors = 0; words = []; cur = None; open_word = False
    for l in open(sys.argv[3], encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        lab, rest = l.rstrip('\n').split(' ', 1); seq = mech[lab]; k = 0
        for tok in re.findall(r"«[^»]*»|\S+", rest):
            if tok.startswith('«'):
                if k >= len(seq) or seq[k][0] != 'clear' or seq[k][1] != tok[1:-1]:
                    print('ERR', lab, 'clear text differs', tok); errors += 1
                k += 1; continue
            if tok in ('.', ',', ';', ':'):
                if k >= len(seq) or seq[k] != ('p', tok): print('ERR', lab, 'punctuation', tok); errors += 1
                k += 1; continue
            lead = tok.startswith('+'); trail = tok.endswith('+')
            pieces = [p for p in SPLIT.split(tok) if p != '']
            cats = set(); doubt = False
            for p in pieces:
                if p.startswith('{+'): cats.add('repaired'); continue
                if k >= len(seq) or seq[k][0] != 'g':
                    print('ERR', lab, 'piece without a group', p); errors += 1; continue
                _, mv, grp, q = seq[k]; k += 1; doubt |= q
                m1 = re.fullmatch(r'\{([^/]*)/([^}]*)\}', p); m2 = re.fullmatch(r'\[\?([^\]]*)\]', p)
                m3 = re.fullmatch(r'\[(\d{4})\]', p)
                if m1 and m1.group(2) == '...':
                    if n(m1.group(1)) != n(mv): print('ERR', lab, grp, 'mark', p, 'but key gives', mv); errors += 1
                    cats.add('hole')
                elif m1 and m1.group(2).startswith('?'):
                    if n(m1.group(1)) != n(mv): print('ERR', lab, grp, 'mark', p, 'but key gives', mv); errors += 1
                    cats.add('guess')
                elif m1:
                    if n(m1.group(1)) != n(mv): print('ERR', lab, grp, 'mark', p, 'but key gives', mv); errors += 1
                    cats.add('code' if m1.group(1) in CODES else 'repaired')
                elif m2:
                    if not mv.startswith('['): print('ERR', lab, grp, 'guess mark on a known group', p, mv); errors += 1
                    cats.add('guess')
                elif m3:
                    if mv != p: print('ERR', lab, grp, p, mv); errors += 1
                    cats.add('hole')
                elif n(p) != n(mv):
                    print('ERR', lab, grp, 'UNMARKED departure:', p, 'key gives', mv); errors += 1
            if lead and open_word and cur is not None:
                cur[0] |= cats; cur[1] |= doubt
            else:
                cur = [cats, doubt, lab]; words.append(cur)
            open_word = trail
        if k != len(seq): print('ERR', lab, 'reading covers', k, 'tokens of', len(seq)); errors += 1
    def cat(c):
        for x in ('hole', 'guess', 'repaired'):
            if x in c: return x
        return 'verbatim'
    cnt = {}
    for c, d, _ in words: cnt[cat(c)] = cnt.get(cat(c), 0) + 1
    tot = len(words); dd = sum(1 for _, d, _ in words if d)
    v, r, g, h = (cnt.get(x, 0) for x in ('verbatim', 'repaired', 'guess', 'hole'))
    print('cipher words %d: verbatim %d (word codes included), repaired %d, guessed %d, holes %d; %d contain a doubtful digit'
          % (tot, v, r, g, h, dd))
    print('verbatim %.1f%%; verbatim + repaired %.1f%%' % (100 * v / tot, 100 * (v + r) / tot))
    if errors: print('FAIL:', errors); sys.exit(1)
    print('OK: no unmarked departure')
if __name__ == "__main__": main()
