"""build.py: rebuild decryptions/, units.tsv and counts.txt of targets/riva1722 from transcriptions/, key.tsv and
overrides.tsv. Standard library only. Run inside the folder:  python3 scripts/build.py

Notation of the transcriptions (one manuscript line per data line, `PAGE.Ln: body`):
  {..}   clear text, never decoded, never a unit
  NN     a number group; NN_ the same group underlined (another value); x before a group = the x-shaped sign (h + value)
  '      short stroke above a group (doubled consonant or accent; never changes the key lookup)
  ^n     small raised numeral over a group (plural ending on a code; never changes the lookup)
  ^(G)   small raised group at a line end
  ?      reader's doubt; #  illegible; [struck] a group cancelled by the writer; A|B alternatives (first decoded)
  -      link stroke between groups; = line-end hyphen
Classes: SYL (keyed, lower case), WORD (keyed, upper case), CODE (number >= 100; always counted not read, whatever the
key proposes), UNK (not in the key; no fallback from underlined to plain or back), ILL (illegible), X (struck).
Strict mark per unit: S = SYL/WORD, no doubt flag, not in overrides.tsv; E = CODE, UNK, any doubt flag, or listed in
overrides.tsv (downgrades only; nothing is upgraded by hand); N = ILL. X units are outside the denominator.
"""
import re, pathlib, collections
T = pathlib.Path(__file__).resolve().parent.parent
DOCS = ['selvatico_1721-12-10', 'selvatico_1722-01-02', 'selvatico_1722-06-10', 'selvatico_1722-07-29',
        'selvatico_1722-08-08', 'selvatico_1722-08-12', 'olivazzi_1725-04-17', 'starhemberg_1726-03-20',
        'starhemberg_1727-02-19']
LINE = re.compile(r'^(\d+[rv]\.L\d+):(.*)$')
UNIT = re.compile(r"^(c?)(x?)(\d+)((?:[_'?]|\^\d)*)$")


def loadkey(p):
    k = {}
    for l in open(p, encoding='utf-8'):
        f = l.rstrip('\n').split('\t')
        if len(f) < 2 or f[0] in ('token', '') or f[0].startswith('#'): continue
        k[f[0]] = f[1]
    return k


def parse_piece(p, extra=''):
    u = {'raw': p, 'flags': set(extra), 'canon': None, 'acc': '', 'sup': '', 'x': False, 'ill': False, 'struck': False}
    m = re.search(r'\[([^\]]*)\]', p)
    if m:
        if m.group(1).strip() == 'struck': u['struck'] = True
        else: u['flags'].add('D')
        p = re.sub(r'\[[^\]]*\]', '', p)
    if u['struck']: return u
    if '|' in p:
        subs = [parse_piece(a) for a in p.split('|')]
        first = subs[0]; first['raw'] = u['raw']; first['flags'] |= u['flags']
        if len({s['canon'] for s in subs}) > 1 or any(s['ill'] for s in subs): first['flags'].add('ALT')
        return first
    m = UNIT.match(p)
    if not m: u['ill'] = True; return u
    c, x, d, suf = m.groups()
    if c: u['flags'].add('C')
    if '?' in suf: u['flags'].add('D')
    u['canon'] = d + ('_' if '_' in suf else ''); u['acc'] = "'" if "'" in suf else ''
    s = re.search(r'\^(\d)', suf); u['sup'] = '^' + s.group(1) if s else ''
    u['x'] = bool(x); u['digits'] = d
    return u


def parse_body(body):
    for part in re.split(r'(\{[^}]*\})', body):
        if part.startswith('{'): yield ('clear', part[1:-1]); continue
        for ch in part.split():
            if ch == '[struck]': yield ('unit', parse_piece('[struck]')); continue
            extra = ''
            m = re.match(r'^\^\((.*)\)([.,:;=]*)$', ch)
            if m: ch = m.group(1); extra = 'R'
            while True:
                n = ch.rstrip('=').rstrip('.,:;')
                if n == ch: break
                ch = n
            if not ch: continue
            for pc in ch.split('-'):
                if pc in ('', '?'): continue
                yield ('unit', parse_piece(pc, extra))


def classify(u, key):
    if u['struck']: return 'X', '[x]'
    if u['ill']: return 'ILL', '#'
    d = u['digits']; c = u['canon']
    if len(d) >= 3:
        if u['x']: u['flags'].add('D')
        v = key.get(c) or key.get(d)
        return 'CODE', ('{%s=%s}' % (d, v) if v else '{%s}' % d) + u['sup']
    if c in key:
        v = key[c]
        if u['x']: v = 'h' + v
        return ('WORD' if v.isupper() else 'SYL'), v + u['acc'] + u['sup']
    return 'UNK', '{%s}' % c + u['acc'] + u['sup']


def mark(cls, flags):
    if cls == 'X': return 'X'
    if cls == 'ILL': return 'N'
    if cls in ('CODE', 'UNK') or flags & {'D', 'C', 'ALT'}: return 'E'
    return 'S'


def main():
    key = loadkey(T / 'key.tsv')
    OV = {}
    for l in open(T / 'overrides.tsv', encoding='utf-8'):
        f = l.rstrip('\n').split('\t')
        if f[0] != 'doc' and len(f) >= 4: OV[(f[0], f[1], int(f[2]))] = f[3]
    used = set(); units = ['doc\tline\tidx\traw\tcanon\tclass\tvalue\tflags\tmark\treason']
    counts = ['counts.txt: written by scripts/build.py. Strict count per cipher unit (rule in the header of scripts/build.py).',
              'S = keyed value stands as transcribed; E = code, unkeyed, doubtful or downgraded in overrides.tsv; N = illegible.', '']
    tot = collections.Counter(); summary = []; kinds = collections.Counter()
    for doc in DOCS:
        per = collections.OrderedDict(); out = []; why = collections.Counter()
        for l in open(T / 'transcriptions' / (doc + '.txt'), encoding='utf-8'):
            m = LINE.match(l.rstrip('\n'))
            if not m: continue
            lid, body = m.groups(); i = 0; lit = []; c = per.setdefault(lid, collections.Counter())
            for kind, o in parse_body(body):
                if kind == 'clear': lit.append('«%s»' % o); continue
                i += 1; cls, val = classify(o, key); mk = mark(cls, o['flags']); r = ''
                if cls == 'X': r = 'struck by the writer'
                elif cls == 'ILL': r = 'illegible'
                elif cls == 'CODE': r = 'code'
                elif cls == 'UNK': r = 'not in the key'
                elif o['flags'] & {'D', 'C', 'ALT'}: r = 'transcription doubt'
                if (doc, lid, i) in OV:
                    used.add((doc, lid, i))
                    if mk == 'S': mk = 'E'; r = OV[(doc, lid, i)]
                    else: r += '; ' + OV[(doc, lid, i)]
                c[mk] += 1; lit.append(val)
                if mk in 'EN': why[r.split(';')[0] if cls in ('CODE', 'UNK', 'ILL') or o['flags'] & {'D', 'C', 'ALT'} else 'downgraded on reading'] += 1
                units.append('\t'.join([doc, lid, str(i), o['raw'], o['canon'] or '', cls, val, ''.join(sorted(o['flags'])), mk, r]))
            out.append(lid + ': ' + body.strip()); out.append('    ' + ' '.join(lit))
        (T / 'decryptions' / (doc + '.txt')).write_text(
            '# ' + doc + ': each manuscript line as transcribed, then its decryption with key.tsv (K3), unit for unit.\n'
            '# «..» clear text; UPPER = word sign; {n} code or group without a key value; {n=WORD} code with a proposed value (counted not read); # illegible; [x] struck.\n'
            + '\n'.join(out) + '\n', encoding='utf-8')
        ls = list(per); S, E, N, X = (sum(per[l][k] for l in ls) for k in 'SENX')
        counts.append(doc)
        for k, v in (('S', S), ('E', E), ('N', N)):
            counts.append('  %s by line: ' % k + ' + '.join(str(per[l][k]) for l in ls) + ' = %d' % v)
        counts.append('  units %d + %d + %d = %d; struck, outside the count: %d; strict %d/%d = %.2f%%' % (S, E, N, S + E + N, X, S, S + E + N, 100 * S / (S + E + N)))
        counts.append('  not read, by kind: ' + '; '.join('%s %d' % kv for kv in sorted(why.items())) + ' (sum %d)' % sum(why.values())); counts.append('')
        assert sum(why.values()) == E + N
        tot.update({'S': S, 'E': E, 'N': N, 'X': X}); summary.append((doc, S, S + E + N)); kinds.update(why)
    assert not (set(OV) - used), sorted(set(OV) - used)
    D = tot['S'] + tot['E'] + tot['N']
    counts.append('ALL NINE LETTERS')
    counts.append('  S: ' + ' + '.join(str(s) for _, s, _ in summary) + ' = %d' % tot['S'])
    counts.append('  units: ' + ' + '.join(str(d) for _, _, d in summary) + ' = %d' % D)
    counts.append('  E %d, N %d; %d + %d + %d = %d; struck %d' % (tot['E'], tot['N'], tot['S'], tot['E'], tot['N'], D, tot['X']))
    counts.append('  strict %d/%d = %.2f%% (pooled only as a sum; each letter is counted on its own above)' % (tot['S'], D, 100 * tot['S'] / D))
    counts.append('  not read, by kind: ' + '; '.join('%s %d' % kv for kv in sorted(kinds.items())) + ' (sum %d)' % sum(kinds.values()))
    extra = T / 'counts_notes.txt'
    if extra.exists(): counts += ['', extra.read_text(encoding='utf-8').rstrip('\n')]
    (T / 'units.tsv').write_text('\n'.join(units) + '\n', encoding='utf-8')
    (T / 'counts.txt').write_text('\n'.join(counts) + '\n', encoding='utf-8')
    for doc, s, d in summary: print('%-24s %4d/%4d = %.2f%%' % (doc, s, d, 100 * s / d))
    print('ALL %d/%d = %.2f%%' % (tot['S'], D, 100 * tot['S'] / D))


if __name__ == '__main__':
    main()
