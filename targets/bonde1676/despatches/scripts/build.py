# build.py: targets/bonde1676/despatches. Standard library only.   python3 -I despatches/scripts/build.py
# For every row of manifest.tsv (one page decode):
#   1. checks the md5 of each key file against the frozen md5 (KEY_MD5 below), and of each transcription against the
#      md5 logged at its freeze (first and second transcriptions);
#   2. decodes the transcription with the key named in the row (b125's L-format second transcriptions are first put in
#      R-format exactly as the session's torfmt.py did: ':' marks and '?' marks dropped, [clear] notes moved to line end);
#   3. checks that the decode equals the session's decode file (md5 of its R-lines, in the manifest);
#   4. takes the segmentation block of segmentation.txt (checks its md5), checks that it rebuilds the decode letter for
#      letter, and classes each word unit S / E / N with the session rule (below); checks the session tally;
#   5. writes decryptions/<despatch>.txt, units.tsv, counts.txt and readings/<despatch>.md.
# Decode (decode3.py of the sessions): tiers A B F P Q T G H give their value (lower case); C gives CAPITALS (weak); W, U and
#   numbers not in the key give <n>; a numeral cut at the gutter ('~') gives [~]; clear words are «quoted».
# Class (tally.py of the sessions): N if the reader flagged !N; E if flagged !E or the decoded form holds a capital, '<' or '[';
#   else S. Read = S only. A unit is a word of the plaintext.
# Sources of key values: A, B, G, H = chancery glosses (A, B the 1675 gloss of image 102R and its 107L/105L control; G letters
#   and H word codes from glosses of 1676-1678); F, P, Q, T = read from context, not from a gloss; C weak; W, U open codes.
import os, re, sys, hashlib, collections

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))           # .../despatches
P = lambda *a: os.path.join(HERE, *a)
KEY_MD5 = {'v3': '8e1d93d1188e698ad6dd14826e8ba168', 'v4': '8e6d8c77a68ede42f3cca0741dda5677', 'v5': '12bcb08e9c39b544b70629f8b7b4d745',
           'v6': '09e50de4f158061bf1465e1b695ea63a', 'v7': '63ddef1c8e07e9cff7fd9f535d814a56', 'v8': '9bda6437be2d7235362ca2bca2aec2e7',
           'v9': 'af29e81f99e96f03663d94dea392e672', 'v10': 'f780c0f3008146d4a2f4f1a6563f5047'}
SOURCE = {'A': 'gloss', 'B': 'gloss', 'G': 'gloss', 'H': 'gloss', 'F': 'context', 'P': 'context', 'Q': 'context', 'T': 'context',
          'C': 'weak', 'W': 'code', 'U': 'code', 'none': 'none', 'cut': 'cut'}
LABEL = {
 '1676-02-12': 'Carl Bonde (Paris) to Charles XI, 12/22 Feb 1676, images 159R-165L, cipher 161R-165L',
 '1676-08-12': 'Bonde and Lillieroot (Paris) to Charles XI, 12/22 Aug 1676, images 278R-283R, cipher 278R-282R',
 '1676-10-06': 'Bonde and Lillieroot (Paris) to Charles XI, 6/16 Oct 1676, images 317R-321L, cipher 317R-320R',
 '1676-10-13': 'Bonde and Lillieroot (Paris) to Charles XI, 13/23 Oct 1676, images 327R-330R',
 '1677-11-03': 'Carl Bonde (Paris) to Charles XI, 3/13 Nov 1677, images 471R-473R, cipher 471R-473L',
 '1677-11-17': 'Carl Bonde (Paris) to Charles XI, 17/27 Nov 1677, images 479R-482L, cipher 479R-481R',
 '1677-11-24_fr': 'Charles Bonde (Paris) to an Excellency, French, copy, 24 Nov/4 Dec 1677, images 490R-491L',
 '1677-12-01': 'Carl Bonde (Paris) to Charles XI, 1/11 Dec 1677, images 491R-493R, cipher 491R-493L',
 '1677-12-29': 'Carl Bonde (Paris) to Charles XI, 29 Dec 1677/8 Jan 1678, images 506R-511R, cipher 507L-511L',
 '1678-01-05': 'Carl Bonde (Paris) to Charles XI, 5/15 Jan 1678, images 512R-516L, cipher 513L-516L'}

md5 = lambda b: hashlib.md5(b).hexdigest()
def pct(a, b): return '%d/%d = %.2f%%' % (a, b, 100.0 * a / b) if b else '0/0'

def load_key(path):
    key = {}
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        g, s, t = l.rstrip('\n').split('\t'); key[g] = (s, t)
    return key

def torfmt(text):
    """b125 L-format -> R-format, as b125's torfmt.py. Also returns, per kept numeral token, whether it carried '?'."""
    out = []; q = []
    for l in text.splitlines():
        m = re.match(r'L(\d+)\s+(.*)', l)
        if not m: continue
        body = m.group(2); clear = re.findall(r'\[clear[^\]]*\]', body); body = re.sub(r'\[clear[^\]]*\]', '', body)
        toks = [t for t in body.split() if t not in (':', '[:')]
        q += ['?' in t for t in toks]
        out.append(('R%d: %s' % (int(m.group(1)), ' '.join(t.replace('?', '') for t in toks) + (' "clear"' if clear else ''))).strip())
    return '\n'.join(out) + '\n', q

def rlines(text, lines):
    for l in text.splitlines():
        m = re.match(r'R(\d+):\s*(.*)', l)
        if not m: continue
        if lines != 'all':
            a, b = map(int, lines.split('-'))
            if not a <= int(m.group(1)) <= b: continue
        yield m.group(1), m.group(2)

def decode(key, text, lines):
    """decode lines; per cipher token (number, output, tier); per line the list of pieces ('c', out) / ('clear', text)."""
    dec = []; toks = []; pieces = []
    for n, body in rlines(text, lines):
        out = []; pl = []
        for part in re.findall(r'"[^"]*"|\S+', body):
            if part.startswith('"'): out.append(' «' + part.strip('"') + '» '); pl.append(('clear', part.strip('"'))); continue
            if part.endswith('~'): o, t = '[~]', 'cut'
            elif part not in key: o, t = '<%s>' % part, 'none'
            else:
                s, t = key[part]
                o = s if t in 'ABFPQTGH' else (s.upper() if t == 'C' else '<%s>' % part)
            out.append(o); toks.append((part, o, t)); pl.append(('c', o))
        dec.append('R' + n + ' ' + ''.join(out)); pieces.append(('R' + n, pl))
    return dec, toks, pieces

def seg_blocks(path, kind):
    blocks = {}
    text = open(path, encoding='utf-8').read()
    parts = re.split(r'^### ', text, flags=re.M)[1:]
    for p in parts:
        head, _, body = p.partition('\n')
        f = [x.strip() for x in head.split('|')]
        label = f[1]; m = re.search(r'md5 (\w+)', head).group(1); nb = int(re.search(r'bytes (\d+)', head).group(1))
        raw = body.encode('utf-8')
        if 'no-final-newline' in head: raw = raw[:-1]
        raw = raw[:nb]
        assert md5(raw) == m, 'block md5 differs: %s %s' % (path, label)
        blocks[label] = raw.decode('utf-8')
    return blocks

def tally(dec, segtext, toks):
    d = ''.join(re.sub(r'«[^»]*»', '', l.split(' ', 1)[1]).replace(' ', '').strip() for l in dec if l.strip())
    segs = []
    for u in segtext.split():
        flag = None
        if u.endswith('!N') or u.endswith('!E'): flag = u[-1]; u = u[:-2]
        s, _, r = u.partition('='); segs.append((s, r, flag))
    if ''.join(s for s, _, _ in segs) != d: sys.exit('segmentation does not rebuild the decode')
    owner = []
    for i, (_, o, _) in enumerate(toks): owner += [i] * len(o.replace(' ', ''))
    assert len(owner) == len(d)
    rows = []; pos = 0
    for s, r, flag in segs:
        ti = sorted(set(owner[pos:pos + len(s)])); start = pos; pos += len(s)
        weak = bool(re.search(r'[A-ZÅÄÖ<\[]', s))
        c = 'N' if flag == 'N' else ('E' if flag == 'E' or weak else 'S')
        rows.append(dict(dec=s, cls=c, reading=r, flag=flag, toks=ti, start=start, end=pos))
    return rows

def reading_md(d, page_runs):
    """page_runs: list of (page, pieces, units). Cipher words between asterisks; clear words as transcribed (approximate)."""
    out = []
    for page, pieces, units in page_runs:
        words = []; pos = 0; ui = 0; pending = []
        # positions of clear segments in cipher-letter coordinates
        clear_at = []
        for ln, pl in pieces:
            for kind, x in pl:
                if kind == 'c': pos += len(x.replace(' ', ''))
                else: clear_at.append((pos, x))
        ci = 0; text = []
        for u in units:
            while ci < len(clear_at) and clear_at[ci][0] <= u['start']:
                text.append(('clear', clear_at[ci][1])); ci += 1
            if u['cls'] == 'S': w = u['dec']
            elif u['cls'] == 'E': w = '[?%s]' % u['reading'] if u['reading'] and u['reading'] != '?' else '[%s]' % u['dec']
            else: w = '[...]'
            text.append(('c', w))
            while ci < len(clear_at) and clear_at[ci][0] < u['end']:
                text.append(('clear', clear_at[ci][1])); ci += 1
        while ci < len(clear_at): text.append(('clear', clear_at[ci][1])); ci += 1
        s = []; run = []
        for kind, x in text:
            if kind == 'c': run.append(x)
            else:
                if run: s.append('*' + ' '.join(run) + '*'); run = []
                s.append(x)
        if run: s.append('*' + ' '.join(run) + '*')
        out.append('## %s\n\n%s\n' % (page, ' '.join(s)))
    return '\n'.join(out)

def main():
    cols = None; rows = []
    for l in open(P('manifest.tsv'), encoding='utf-8'):
        if l.startswith('#'): continue
        f = l.rstrip('\n').split('\t')
        if cols is None: cols = f; continue
        rows.append(dict(zip(cols, f)))
    keys = {}
    for r in rows:
        if r['key'] not in keys:
            kp = os.path.normpath(P(r['keyfile']))
            assert md5(open(kp, 'rb').read()) == KEY_MD5[r['key']], 'key %s is not the frozen file' % r['key']
            keys[r['key']] = load_key(kp)
    segs = {}; units_out = ['despatch\tpage\trole\tkey\tunit\tdecoded\tclass\treading\tnumbers (value, tier)']
    per = collections.OrderedDict(); dec_out = collections.OrderedDict(); page_runs = collections.defaultdict(list)
    for r in rows:
        d = r['despatch']
        if d not in segs: segs[d] = seg_blocks(P(d, 'segmentation.txt'), 'segmentation')
        if os.path.exists(P(d, 'doubts.md')) and d not in per: seg_blocks(P(d, 'doubts.md'), 'doubts')
        raw = open(P(d, r['transcription']), 'rb').read()
        if r['freeze_md5'] != '-': assert md5(raw) == r['freeze_md5'], 'transcription differs from the frozen file: ' + r['transcription']
        text = raw.decode('utf-8'); qmarks = None
        if r['rformat'] == 'torfmt': text, qmarks = torfmt(text)
        key = keys[r['key']]
        dec, toks, pieces = decode(key, text, r['lines'])
        if qmarks is not None: assert len(qmarks) == len(toks)
        assert md5('\n'.join(x.rstrip() for x in dec).encode('utf-8')) == r['session_decode_md5'], 'decode differs from the session decode: %s %s' % (d, r['seg_label'])
        units = tally(dec, segs[d][r['seg_label']], toks)
        S = sum(u['cls'] == 'S' for u in units); E = sum(u['cls'] == 'E' for u in units); N = sum(u['cls'] == 'N' for u in units)
        assert (S, E, N) == (int(r['S']), int(r['E']), int(r['N'])), 'tally differs from the session: %s %s' % (d, r['seg_label'])
        # sources of the numbers in read units
        src = collections.Counter(); tiers = collections.Counter(); ctx_units = 0; h_units = 0; q_units = 0
        for i, u in enumerate(units):
            tl = [toks[j] for j in u['toks']]
            if u['cls'] == 'S':
                for n, o, t in tl: src[SOURCE[t]] += 1; tiers[t] += 1
                ctx_units += any(SOURCE[t] == 'context' for _, _, t in tl)
                h_units += any(t == 'H' for _, _, t in tl)
                if qmarks is not None: q_units += any(qmarks[j] for j in u['toks'])
            units_out.append('\t'.join([d, r['page'], r['role'], r['key'], str(i + 1), u['dec'], u['cls'], u['reading'],
                                        ' '.join('%s=%s(%s)' % (n, o, t) for n, o, t in tl)]))
        per.setdefault(d, []).append(dict(r=r, S=S, E=E, N=N, T=len(units), src=src, tiers=tiers, ctx=ctx_units, H=h_units,
                                          q=q_units if qmarks is not None else None, nq=sum(qmarks) if qmarks else 0, ntok=len(toks)))
        dec_out.setdefault(d, []).append('## %s, %s transcription%s, key %s (%s)\n%s\n' % (
            r['page'], {'first': 'first', 'second': 'second', 'rescore': 'first'}[r['role']],
            {'first': ', decoded once (figure of record)', 'second': ', decoded once (not the figure of record)',
             'rescore': ', RE-SCORED with a later key: NOT held-out'}[r['role']], r['key'], r['transcription'], '\n'.join(dec)))
        if r['role'] == 'first': page_runs[d].append(('%s (key %s%s)' % (r['page'], r['key'], '' if r['lines'] == 'all' else ', lines ' + r['lines']), pieces, units))
    os.makedirs(P('decryptions'), exist_ok=True); os.makedirs(P('readings'), exist_ok=True)
    for d, bl in dec_out.items():
        open(P('decryptions', d + '.txt'), 'w', encoding='utf-8').write(
            '# Decryption of %s, written by scripts/build.py. <n> = number with no value in the key; [~] = numeral cut at the gutter; CAPITALS = weak value (tier C); «» = clear on the page (transcribed approximately, not scored).\n\n' % LABEL[d] + '\n'.join(bl))
    for d, runs in page_runs.items():
        open(P('readings', d + '.md'), 'w', encoding='utf-8').write(
            '# %s: reading (first pass)\n\nWritten by scripts/build.py from the first-pass decodes and the reader\'s segmentation. Cipher words between asterisks; the rest is clear text as transcribed next to the cipher (approximate, not scored). [?word] = the reader\'s emendation or a sense from context, counted not read; [decoded] = a unit with a number of no value, a cut numeral or a weak value, counted not read; [...] = no reading. Spelling is the writer\'s; word division is the reader\'s.\n\n' % LABEL[d] + reading_md(d, runs))
    open(P('units.tsv'), 'w', encoding='utf-8').write('\n'.join(units_out) + '\n')
    # counts
    out = ['counts.txt: written by scripts/build.py. One block per despatch; figures per page and per despatch, never pooled across despatches.',
           'Read = S: every number of the word gives its frozen value and the word is spelt. E and N are not read. Unit = a word of the plaintext.',
           'Gloss values: tiers A B G H (chancery decipherments). Context values: tiers F P Q T (read from context, not from a gloss).', '']
    for d, ps in per.items():
        out.append('## ' + LABEL[d])
        for role, title in (('first', 'First pass: each page frozen, then decoded once with the key frozen before it (figure of record)'),
                            ('second', 'Second transcription'), ('rescore', 'Re-score with a later key: NOT held-out (the pages had been seen; values may come from them)')):
            sel = [p for p in ps if p['r']['role'] == role]
            if not sel: continue
            out.append(title + ':')
            for p in sel:
                r = p['r']
                out.append('  %-18s key %-3s %-4s tx md5 %s%s: S %d + E %d + N %d = %d; strict %s' % (
                    r['page'], r['key'], r['session'], md5(open(P(d, r['transcription']), 'rb').read()),
                    (' frozen ' + r['freeze_utc']) if r['freeze_utc'] != '-' else '', p['S'], p['E'], p['N'], p['T'], pct(p['S'], p['T'])))
            S = sum(p['S'] for p in sel); T = sum(p['T'] for p in sel)
            kv = list(dict.fromkeys(p['r']['key'] for p in sel))
            if len(kv) > 1:
                for k in kv:
                    ks = [p for p in sel if p['r']['key'] == k]
                    out.append('  key %s pages: %s of %s = %s' % (k, ' + '.join(str(p['S']) for p in ks), ' + '.join(str(p['T']) for p in ks),
                                                              pct(sum(p['S'] for p in ks), sum(p['T'] for p in ks))))
                out.append('  whole despatch, first pass under the keys above (mixed key states, given for completeness only): %s of %s = %s' % (
                    ' + '.join(str(p['S']) for p in sel), ' + '.join(str(p['T']) for p in sel), pct(S, T)))
            else:
                out.append('  sum: %s of %s = %s' % (' + '.join(str(p['S']) for p in sel), ' + '.join(str(p['T']) for p in sel), pct(S, T)))
            if role == 'first':
                short = [p['r']['page'] for p in sel if p['T'] < 20]
                if T < 150: out.append('  SHORT DESPATCH: %d word units (under 150); the shuffle test is weak on so little text' % T)
                if short: out.append('  short pages (under 20 units): ' + ', '.join(short))
            if role == 'second':
                firsts = {p['r']['page']: p for p in ps if p['r']['role'] == 'first'}
                rep = {p['r']['page'] for p in sel}
                mix = [p for pg, p in firsts.items() if pg not in rep] + sel
                out.append('  despatch with this transcription in place of the first on %s: %s of %s = %s' % (
                    ', '.join(sorted(rep)), ' + '.join(str(p['S']) for p in mix), ' + '.join(str(p['T']) for p in mix),
                    pct(sum(p['S'] for p in mix), sum(p['T'] for p in mix))))
            if role == 'first':
                src = sum((p['src'] for p in sel), collections.Counter()); tiers = sum((p['tiers'] for p in sel), collections.Counter())
                out.append('  numbers inside the read units, by source of their key value: gloss %d, context %d (%s)' % (
                    src['gloss'], src['context'], ', '.join('%s %d' % (t, tiers[t]) for t in sorted(tiers))))
                out.append('  read units using at least one context value: %d of %d' % (sum(p['ctx'] for p in sel), S))
                h = sum(p['H'] for p in sel)
                out.append('  word-layer sensitivity: read units resting on a gloss word code (tier H): %d; with them counted not read: %s' % (h, pct(S - h, T)))
            if role == 'second' and any(p['q'] is not None for p in sel):
                q = sum(p['q'] or 0 for p in sel); nq = sum(p['nq'] for p in sel)
                out.append("  '?' rule (a numeral marked '?' makes its unit a hole): %d numerals marked '?', %d read units hold one; strict %s by our rule, %s by the '?' rule" % (nq, q, pct(S, T), pct(S - q, T)))
        out.append('')
    open(P('counts.txt'), 'w', encoding='utf-8').write('\n'.join(out))
    print('\n'.join(out))

if __name__ == '__main__':
    main()
