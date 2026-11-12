# build.py: targets/bonde1677. Standard library only. python3 -I scripts/build.py
# Decodes the cipher of R0003797 image 489R with the frozen key v9, checks that the segmentation rebuilds the decode
# exactly, classes each word unit S / E / N, and writes decryptions/, units.tsv, counts.txt and holes.md. Also decodes
# the blind second transcription (b127) with the same key and segmentation rules.
#
# Decoder and classing as in the session scripts (scripts/original/b119_decode3.py, b119_tally.py), unchanged in substance:
#   Decode: tiers A B F P Q T G H give their value (lower case; H = a word code fixed by a chancery gloss); tier C gives
#           CAPITALS (weak); tier W (word codes without a gloss of their own) and numbers not in the key give <n>; '~' = [~].
#   Class:  N if flagged !N by the reader; E if flagged !E or the decoded form holds a capital, '<' or '['; else S.
# Tiers of key v9 by source: A gloss of 1675 (image 102R); B 1675 gloss corrections (107L/105L); G and H chancery glosses
# of 1676-1677 (images 331-430); F, P, Q, T values read from context (image 324 of the 1676 memorial, its post-hoc
# values, and decodes of the 1676 despatches). counts.txt reports how many cipher numbers of the read units rest on each.
import os, re, sys, hashlib, collections

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(HERE, *a)
KEY_MD5 = 'af29e81f99e96f03663d94dea392e672'
TIERS = 'ABFPQTGH'
SOURCE = {'A': 'gloss 1675', 'B': 'gloss 1675', 'G': 'gloss 1676-77', 'H': 'gloss 1676-77',
          'F': 'context', 'P': 'context', 'Q': 'context', 'T': 'context', 'C': 'weak', 'W': 'code', 'U': 'code'}

def md5(p): return hashlib.md5(open(p, 'rb').read()).hexdigest()

def load_key(path):
    key = {}
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        g, s, t = l.rstrip('\n').split('\t'); key[g] = (s, t)
    return key

def decode(key, path):
    """Returns the decode lines and, for every cipher number, (number, output string, tier)."""
    lines = []; toks = []
    for l in open(path, encoding='utf-8'):
        m = re.match(r'(R\d+):\s*(.*)', l)
        if not m: continue
        out = []
        for part in re.findall(r'"[^"]*"|\S+', m.group(2)):
            if part.startswith('"'): out.append(' «' + part.strip('"') + '» '); continue
            if part.endswith('~'): o, t = '[~]', 'cut'
            elif part not in key: o, t = '<%s>' % part, 'none'
            else:
                s, t = key[part]
                o = s if t in TIERS else (s.upper() if t == 'C' else '<%s>' % part)
            out.append(o); toks.append((part, o, t))
        lines.append(m.group(1) + ' ' + ''.join(out))
    return lines, toks

def tally(dec_lines, seg_path, toks):
    dec = ''.join(re.sub(r'«[^»]*»', '', l.split(' ', 1)[1]).replace(' ', '').strip() for l in dec_lines if l.strip())
    segs = []
    for u in open(seg_path, encoding='utf-8').read().split():
        flag = None
        if u.endswith('!N') or u.endswith('!E'): flag = u[-1]; u = u[:-2]
        s, _, r = u.partition('='); segs.append((s, r, flag))
    rebuilt = ''.join(s for s, _, _ in segs)
    if rebuilt != dec: sys.exit('MISMATCH ' + seg_path)
    # character position -> token index, to say which numbers each unit uses
    owner = []
    for i, (_, o, _) in enumerate(toks): owner += [i] * len(o.replace(' ', ''))
    assert len(owner) == len(dec)
    rows = []; pos = 0
    for s, r, flag in segs:
        ti = sorted(set(owner[pos:pos + len(s)])); pos += len(s)
        weak = bool(re.search(r'[A-ZÅÄÖ<\[]', s))
        c = 'N' if flag == 'N' else ('E' if flag == 'E' or weak else 'S')
        rows.append((s, c, r, flag, [toks[i] for i in ti]))
    return rows

def pct(a, b): return '%d/%d = %.2f%%' % (a, b, 100.0 * a / b)

def main():
    assert md5(P('key.tsv')) == KEY_MD5, 'key.tsv is not the frozen key v9'
    key = load_key(P('key.tsv'))
    out = ['counts.txt: written by scripts/build.py. Strict count per word unit (rule in the header of scripts/build.py).',
           'key.tsv md5 %s (= key v9, frozen 12 Nov 2026 06:08:58 UTC, before this page was transcribed).' % md5(P('key.tsv')), '']
    tx = P('transcriptions', 'despatch_1677-11-24_489R.txt')
    dec, toks = decode(key, tx)
    open(P('decryptions', 'despatch_1677-11-24_489R.txt'), 'w', encoding='utf-8').write(
        '# Decryption of transcriptions/despatch_1677-11-24_489R.txt with key.tsv (v9), written by scripts/build.py. «» = clear on the page (transcribed in part only); <n> = no value; first decoded once on 12 Nov 2026 06:24:26 UTC (b119).\n' + '\n'.join(dec) + '\n')
    rows = tally(dec, P('segmentation', 'seg_despatch_1677-11-24_489R.txt'), toks)
    S = sum(r[1] == 'S' for r in rows); E = sum(r[1] == 'E' for r in rows); N = sum(r[1] == 'N' for r in rows); T = S + E + N
    out.append('## A. Image 489R, first transcription (b119), frozen 06:24:26 UTC, decoded once with v9')
    out.append('transcription md5 %s; cipher numbers %d' % (md5(tx), len(toks)))
    out.append('units: ' + ' '.join('%s[%s]' % (r[0], r[1]) for r in rows))
    out.append('S %d + E %d + N %d = %d; strict %s; S+E %s' % (S, E, N, T, pct(S, T), pct(S + E, T)))
    # sources of the numbers inside the S units
    src = collections.Counter(); tiers = collections.Counter(); ctx_units = []
    for s, c, r, flag, tk in rows:
        if c != 'S': continue
        for part, o, t in tk:
            src[SOURCE.get(t, t)] += 1; tiers[t] += 1
        cx = [p + '=' + o + '(' + t + ')' for p, o, t in tk if SOURCE.get(t) == 'context']
        if cx: ctx_units.append('%s: %s' % (s, ' '.join(cx)))
    n = sum(src.values())
    out.append('')
    out.append('Numbers inside the %d read units, by the source of their key value: ' % S + ' + '.join('%s %d' % (k, v) for k, v in sorted(src.items())) + ' = %d' % n)
    out.append('by tier: ' + ', '.join('%s %d' % kv for kv in sorted(tiers.items())))
    out.append('read units that use at least one context value (F/P/Q/T): %d of %d' % (len(ctx_units), S))
    out += ['  ' + x for x in ctx_units]
    out.append('read units resting on gloss values only (A/B/G/H): %d of %d' % (S - len(ctx_units), S))
    # B. blind second transcription
    bd, bt = decode(key, P('second_transcription', 'blindR_489R.txt'))
    open(P('decryptions', 'blind_489R.txt'), 'w', encoding='utf-8').write(
        '# Decryption of second_transcription/blindR_489R.txt (b127 blind transcription, cipher runs only) with key.tsv (v9).\n' + '\n'.join(bd) + '\n')
    br = tally(bd, P('second_transcription', 'seg_blind_489R.txt'), bt)
    bS = sum(r[1] == 'S' for r in br); bE = sum(r[1] == 'E' for r in br); bN = sum(r[1] == 'N' for r in br)
    out += ['', '## B. Blind second transcription (b127), frozen 09:35:28 UTC before any earlier file was opened; decoded once with v9',
            'cipher numbers %d' % len(bt),
            'S %d + E %d + N %d = %d; strict %s' % (bS, bE, bN, bS + bE + bN, pct(bS, bS + bE + bN)),
            'units that differ in class from A: ' + ', '.join('%s[%s] vs %s[%s]' % (b[0], b[1], a[0], a[1]) for a, b in zip(rows, br) if (a[0], a[1]) != (b[0], b[1])),
            'Numeral agreement: controls/compare_blind.txt (scripts/compare_blind.py).']
    with open(P('units.tsv'), 'w', encoding='utf-8') as f:
        f.write('transcription\tunit\tdecoded\tclass\treading\tnumbers (value, tier)\n')
        for name, rr in (('first_b119', rows), ('blind_b127', br)):
            for i, (s, c, r, flag, tk) in enumerate(rr, 1):
                f.write('%s\t%d\t%s\t%s\t%s\t%s\n' % (name, i, s, c, r, ' '.join('%s=%s(%s)' % x for x in tk)))
    holes = ['# Holes: every word unit of image 489R not counted read (first transcription, b119)', '',
             'Written by scripts/build.py. E = holds a number with no value, or emended by the reader; N = no reading.', '',
             '| unit | decoded | class | reading | numbers (value, tier) | why |', '|---|---|---|---|---|---|']
    for ui, (s, c, r, flag, tk) in enumerate(rows, 1):
        if c == 'S': continue
        w = []
        if flag == 'E': w.append('emended by the reader (key spelling short of the word)')
        for nn in re.findall(r'<(\d+)>', s): w.append('no value for %s' % nn)
        if re.search(r'[A-Z]', s): w.append('weak C-tier value')
        holes.append('| %d | `%s` | %s | %s | %s | %s |' % (ui, s, c, r, ' '.join('%s=%s(%s)' % x for x in tk), '; '.join(w)))
    holes += ['', 'Numbers with no value: 418 (twice, both before -en: "<418>en"; sense from context perhaps march/marchen, not read), 435 (once, "uti <435>": a place for the diversion, not read). key v10 (b122, later, not used here) proposes 418 = march and 435 = Preussen from glosses; see NOTES.md.']
    open(P('holes.md'), 'w', encoding='utf-8').write('\n'.join(holes) + '\n')
    open(P('counts.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('\n'.join(out))

if __name__ == '__main__':
    main()
