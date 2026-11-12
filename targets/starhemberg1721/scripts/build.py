"""build.py: rebuild decryptions/, units.tsv and counts.txt of targets/starhemberg1721 from transcriptions/, key.tsv,
overrides.tsv and unglossed.tsv. Standard library only. Run inside the folder:  python3 scripts/build.py

Notation: one manuscript line per data line (`PAGE.Ln: body`); a number = one group (the dots of the original are
written as spaces); {..} clear text; " after a group = the double stroke written after it (doubled consonant);
? reader's doubt; # a sign not read; a lone : is the writer's colon and is not a unit.
Strict mark per unit: N = #; E = a number of 80 and over (code), a number not in the key, a doubt mark, the doubling
mark, or a unit listed in overrides.tsv (downgrades only); S = the rest. A second, labelled figure counts the
doubling mark as read. unglossed.tsv lists the units with no contemporary gloss (the part that is new).
"""
import re, pathlib, collections
T = pathlib.Path(__file__).resolve().parent.parent
DOCS = ['starhemberg_1720-12-21', 'starhemberg_1721-05-31', 'starhemberg_1721-06-14']


def rows(p):
    return [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#') and not l.startswith(('doc\t', 'token\t'))]


def main():
    key = {f[0]: f[1] for f in rows(T / 'key.tsv')}
    ov = {(f[0], f[1], int(f[2])): f[3] for f in rows(T / 'overrides.tsv')}
    ung = set()
    for f in rows(T / 'unglossed.tsv'):
        for i in range(int(f[2]), int(f[3]) + 1): ung.add((f[0], f[1], i))
    units = ['doc\tline\tidx\traw\tvalue\tmark\tdoubling_mark\tgloss\treason']; counts = ['counts.txt: written by scripts/build.py. Rule in the header of scripts/build.py.', '']
    used = set(); grand = collections.Counter()
    for doc in DOCS:
        R = []; out = []; run = []
        for l in open(T / 'transcriptions' / (doc + '.txt'), encoding='utf-8'):
            m = re.match(r'^(\d+[rv]\.L\d+):(.*)$', l.rstrip('\n'))
            if not m: continue
            lid, body = m.groups(); i = 0; lit = []
            for part in re.split(r'(\{[^}]*\})', body):
                if part.startswith('{'): lit.append('«%s»' % part[1:-1]); continue
                for ch in part.split():
                    if ch == ':': continue
                    i += 1; g = 'unglossed' if (doc, lid, i) in ung else 'glossed'
                    if ch == '#': R.append((lid, i, ch, '#', 'N', False, g, 'sign not read')); lit.append('#'); continue
                    q = '"' in ch; dd = '?' in ch; d = ch.replace('"', '').replace('?', ''); code = int(d) >= 80; v = key.get(d)
                    val = ('{%s=%s}' % (d, v) if v else '{%s}' % d) if code else (v + ('"' if q else '') if v else '{%s}' % d)
                    why = 'code' if code else 'not in the key' if not v else 'transcription doubt' if dd else ''
                    if (doc, lid, i) in ov: used.add((doc, lid, i)); why = (why + '; ' if why else '') + ov[(doc, lid, i)]
                    ok = not why
                    if ok and q: why = 'doubling mark'
                    R.append((lid, i, ch, val, 'S' if (ok and not q) else 'E', ok and q, g, why)); lit.append(val + ('?' if dd else ''))
            out.append(lid + ': ' + body.strip()); out.append('    ' + ' '.join(lit))
            run.append(''.join(x if not x.startswith('«') else ' ' + x[1:-1] + ' ' for x in lit))
        (T / 'decryptions' / (doc + '.txt')).write_text('# ' + doc + ': each manuscript line as transcribed, then its decryption with key.tsv (K21), unit for unit.\n# «..» clear text; {n} code or number without a key value; {n=WORD} code with a value from the gloss (counted not read); " doubling mark; # not read.\n' + '\n'.join(out) + '\n\nThe same, run together, clear text included, no word division added by us: ' + ' '.join(' '.join(run).split()) + '\n', encoding='utf-8')
        for r in R: units.append('\t'.join([doc, r[0], str(r[1]), r[2], r[3], r[4], 'yes' if r[5] else '', r[6], r[7]]))
        counts.append(doc)
        def tally(sel, name, qs=False):
            Tt = collections.OrderedDict()
            for r in R:
                if not sel(r): continue
                t = Tt.setdefault(r[0], [0, 0, 0]); mk = 'S' if (qs and r[5]) else r[4]; t['SEN'.index(mk)] += 1
            if not Tt: return None
            S, E, N = (sum(t[k] for t in Tt.values()) for k in range(3))
            counts.append('  %s: S %s = %d; E %s = %d; N %s = %d; %d + %d + %d = %d; strict %d/%d = %.2f%%' % (name, ' + '.join(str(t[0]) for t in Tt.values()), S, ' + '.join(str(t[1]) for t in Tt.values()), E, ' + '.join(str(t[2]) for t in Tt.values()), N, S, E, N, S + E + N, S, S + E + N, 100 * S / (S + E + N)))
            return S, S + E + N
        a = tally(lambda r: True, 'all units'); tally(lambda r: True, 'all units, doubling mark counted read (second figure)', True)
        u = tally(lambda r: r[6] == 'unglossed', 'unglossed units (new)'); g = tally(lambda r: r[6] == 'glossed', 'glossed units (deciphered at the time)')
        assert a[1] == (u[1] if u else 0) + (g[1] if g else 0)
        why = collections.Counter(r[7].split(';')[0] if r[7].split(';')[0] in ('code', 'not in the key', 'transcription doubt', 'doubling mark', 'sign not read') else 'downgraded on reading' for r in R if r[4] != 'S')
        counts.append('  not read, by kind: ' + '; '.join('%s %d' % kv for kv in sorted(why.items())) + ' (sum %d)' % sum(why.values())); counts.append('')
        grand.update({'S': a[0], 'D': a[1], 'uS': u[0] if u else 0, 'uD': u[1] if u else 0}); print(doc, a, u, g)
    assert not set(ov) - used, set(ov) - used
    counts.append('THREE LETTERS: all units %d/%d = %.2f%%; unglossed units %d/%d = %.2f%% (sums; each letter is counted on its own above)' % (grand['S'], grand['D'], 100 * grand['S'] / grand['D'], grand['uS'], grand['uD'], 100 * grand['uS'] / grand['uD']))
    extra = T / 'counts_notes.txt'
    if extra.exists(): counts += ['', extra.read_text(encoding='utf-8').rstrip('\n')]
    (T / 'units.tsv').write_text('\n'.join(units) + '\n', encoding='utf-8'); (T / 'counts.txt').write_text('\n'.join(counts) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
