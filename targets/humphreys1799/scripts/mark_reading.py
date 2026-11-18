"""Mark every word of a reading as table value, context value or guess (packaging step, 14 Nov 2026).

Input: readings/words_<doc>.txt. Lines starting '@' open a passage ('@a 0414 right page'); lines starting '>' are
clear text written by Humphreys, copied from the image (not counted); other lines hold coded words separated by
spaces. A word is pieces joined by '+', optionally followed by '~normalised spelling'. Piece forms:
  994            group read with the frozen table (key/table_frozen_v1.tsv); an error if the table has no value
  1490=re/P      group read with a context value (key/context_values.tsv); basis H, P or S as there
  367.211=trade/S  several groups given one context value
  [314]          group left unread; printed as its number
  ^ga/S          a piece not visible on the film (lost in the binding), supplied as a guess
Word marks: T = every piece from the frozen table; C = at least one context value of basis H (also the clerk's
value in the held-out despatch or another glossed occurrence) or P (visible digits plus sense), none weaker;
G = at least one sense-only value (basis S) or supplied piece, i.e. a guess; U = a word with an unread group and no
word proposed. Punctuation groups (1527, 1436, 1235, 1312) are printed as punctuation and not counted.
In the printed reading: table pieces plain; {..} = context value H or P; [..?] = guess; [n] = unread group.
Writes readings/reading_<doc>.txt, readings/marked_<doc>.tsv and validation rows. Usage:
python scripts/mark_reading.py 214 188 0364"""
import csv, os, re, sys, collections
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
tab = {r['group']: r['value'] for r in csv.DictReader(open(B + '/key/table_frozen_v1.tsv'), delimiter='\t')}
PUNCT = {'1527': '.', '1436': '.', '1235': ',', '1312': ';'}
RANK = {'T': 0, 'C': 1, 'G': 2, 'U': 3}
CAP = {'united_states': 'United States', 'i': 'I', 'france': 'France', 'paris': 'Paris', 'spain': 'Spain',
       'america': 'America', 'president': 'President', 'king': 'King', 'england': 'England'}
GC = collections.Counter()
def piece(p):
    if p.startswith('^'):
        v, b = p[1:].split('/'); return ('', v, 'G', f'[{v}?]')
    m = re.fullmatch(r'\[([^\]]+)\]', p)
    if m: return (m.group(1), None, 'U', f'[{m.group(1)}]')
    if '=' in p:
        g, rest = p.split('=', 1); v, b = rest.rsplit('/', 1)
        mk = 'C' if b in ('H', 'P') else 'G'
        return (g, v, mk, '{' + v + '}' if mk == 'C' else f'[{v}?]')
    if p not in tab: sys.exit(f'no table value for {p}')
    v = CAP.get(tab[p], tab[p])
    return (p, v, 'T', v)
def run(doc):
    out, rows, val = [], [], []
    for line in open(f'{B}/readings/words_{doc}.txt', encoding='utf-8'):
        s = line.rstrip('\n')
        if not s.strip() or s.startswith('#'): continue
        if s.startswith('@'): out.append(f'\n\n{s[1:].strip()}.\n'); cur = s[1:].split()[0]; continue
        if s.startswith('>'): out.append(' (' + s[1:].strip() + ')'); continue
        for w in s.split():
            if w in PUNCT: GC[(doc, 'T')] += 1; out.append(PUNCT[w]); rows.append((cur, w, '', PUNCT[w], 'punct')); val.append((w, '-')); continue
            norm = None
            if '~' in w: w, norm = w.split('~', 1)
            ps = [piece(p) for p in w.split('+')]
            for x in ps:
                if x[0]: GC[(doc, x[2])] += len(x[0].split('.'))
            mk = max((x[2] for x in ps), key=RANK.get)
            if mk == 'U' and norm: mk = 'G'
            disp = ''.join(x[3] for x in ps)
            if mk == 'T' and norm: disp = norm
            out.append(' ' + disp)
            rows.append((cur, '.'.join(x[0] for x in ps if x[0]), '.'.join((x[1] or '?') for x in ps), norm or disp, mk))
            for x in ps:  # validation rows: table and supported context values only; guesses and unread = '?'
                if not x[0]: continue
                for g in x[0].split('.'):
                    ok = x[2] in ('T', 'C') and '.' not in x[0] and re.fullmatch(r'\d+', g)
                    val.append((g, x[1].lower().replace(' ', '') if ok else '?'))
    with open(f'{B}/readings/marked_{doc}.tsv', 'w', encoding='utf-8') as o:
        o.write('passage\tgroups\tpieces\tword\tmark\n')
        for r in rows: o.write('\t'.join(r) + '\n')
    c = collections.Counter(r[4] for r in rows if r[4] != 'punct')
    n = sum(c.values()); gn = sum(GC[(doc, k)] for k in 'TCGU')
    head = (f'# Reading of {doc}, made with scripts/mark_reading.py from readings/words_{doc}.txt.\n'
            f'# Plain = frozen table; {{..}} = context value supported by another occurrence or by visible digits;\n'
            f'# [..?] = guess (sense only); [n] = group left unread, shown by its number; (..) = Humphreys\'s clear text.\n'
            f'# Words: {n}; table {c["T"]}, context {c["C"]}, guess {c["G"]}, unread {c["U"]}. '
            f'Share of words resting on the table alone: {c["T"]/n:.3f}; table or supported context: {(c["T"]+c["C"])/n:.3f}.\n'
            f'# Code groups (punctuation groups included): {gn}; read by the frozen table {GC[(doc,"T")]} ({GC[(doc,"T")]/gn:.3f}); '
            f'supported context {GC[(doc,"C")]}; sense-only {GC[(doc,"G")]}; unread {GC[(doc,"U")]}.\n')
    text = re.sub(r' +([.,;])', r'\1', ''.join(out)).strip()
    open(f'{B}/readings/reading_{doc}.txt', 'w', encoding='utf-8').write(head + '\n' + text + '\n')
    print(doc, dict(c), n)
    return val
if __name__ == '__main__':
    allv = []
    for d in sys.argv[1:]: allv += run(d)
    with open(B + '/validation.tsv', 'w', encoding='utf-8') as o:
        o.write('# model: en-modern\n# source: readings/words_*.txt (' + ', '.join(sys.argv[1:]) + ') via scripts/mark_reading.py\n')
        o.write('# note: frozen-table values and supported context values (H, P); sense-only guesses, unread groups and groups\n')
        o.write('# with hidden digits read as "?"; punctuation groups as nulls ("-")\n')
        for g, v in allv: o.write(f'{g}\t{v}\n')
