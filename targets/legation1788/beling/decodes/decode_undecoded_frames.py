"""Decode, with key/code16_key_v4.tsv, the Pinckney groups in ../transcription/pinckney_m30.tsv that carry no
interlinear decoding (frames 0106, 0107, 0135, 0136, 0148 foot, 0178, 0196 ll. 5-10, 0305, 0317; 0140 is handled
in corrections/). "Decoded, not read": a stream of key values with no word division and no editing.

Run from targets/legation1788/beling:   python3 decodes/decode_undecoded_frames.py
Writes decodes/m30_undecoded_v4.txt and decodes/coverage.tsv.

Coverage is given three ways, because key v4 is not independent of these frames:
  all        any key v4 value
  no_A       without grade A: the A values were read off by aligning frames 0106-0107, 0135-0136, 0183, 0196,
             0305 and 0317 of this transcription to the printed editions (key/scripts/code16_align_cribs_2026_11_10.py)
  no_A_no_B  also without grade B, i.e. values from Eaton, Lear and Pinckney 1795 only (B values are this
             repository's own key.tsv, built from Taylor's decodings and, for 0178, from the Explication on 0179)
"""
import csv, re, collections
from pathlib import Path

B = Path(__file__).resolve().parents[1]
key = {int(r['group']): (r['value'], r['grade']) for r in csv.DictReader(open(B / 'key' / 'code16_key_v4.tsv'), delimiter='\t')}
rows = list(csv.DictReader([l for l in open(B.parent / 'transcription' / 'pinckney_m30.tsv', encoding='utf-8') if not l.startswith('#')], delimiter='\t'))
FRAMES = ['0106', '0107', '0135', '0136', '0148', '0178', '0196', '0305', '0317']
NOTE = {'0106': '5 Jul 1793 (PTJ 26 prints the passages from Bankson\'s Tr: https://founders.archives.gov/documents/Jefferson/01-26-02-0388)',
        '0107': '5 Jul 1793, continuation',
        '0135': '15 Aug 1793 (PTJ 26 prints it from Bankson\'s clear Tr: https://founders.archives.gov/documents/Jefferson/01-26-02-0620)',
        '0136': '15 Aug 1793, continuation',
        '0148': '25 Sep 1793, the undecoded line below the signature (line PS) (https://founders.archives.gov/documents/Jefferson/01-27-02-0157)',
        '0178': '25 Nov 1793; the clerk\'s "Explication of the Cyphers" on frame 0179 is its plaintext (this repository aligned 173 groups to it)',
        '0196': '28 Jan 1794, lines 5-10 (no interlinear) (Pinckney Statesmen: https://rotunda.upress.virginia.edu/founders/PNKY-01-02-02-0003-0076)',
        '0305': '23-27 Feb 1795 (Pinckney Statesmen: https://rotunda.upress.virginia.edu/founders/PNKY-01-02-02-0004-0125)',
        '0317': '3 Apr 1795 (Pinckney Statesmen: https://rotunda.upress.virginia.edu/founders/PNKY-01-02-02-0004-0243-0001)'}
cov = collections.OrderedDict((f, collections.Counter()) for f in FRAMES)
out = ['# Code No. 16: Pinckney frames on NARA M30 roll 2 without a contemporary decoding, decoded with key v4. DECODED, NOT READ.',
       '# Groups from ../transcription/pinckney_m30.tsv (this repository). value = key v4 value; [n] = group not in key v4;',
       '# [n?] = group with a doubtful digit in the transcription (not decoded); a trailing + is the writer\'s plural/inflection mark.',
       '# Upper-case values are grade A (read off by aligning these frames to the printed editions), so they are not evidence for the text.',
       '# Images: https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M30/M30-002/M30-002-NNNN.jpg', '']
for f in FRAMES:
    rs = [r for r in rows if r['frame'] == f]
    if f == '0148':                                   # the line below the signature only
        rs = [r for r in rs if r['line'] == 'PS']
    if f == '0196':                                   # lines 5-10, which Taylor did not interline
        rs = [r for r in rs if r['line'] in {'5', '6', '7', '8', '9', '10'}]
    if not rs:
        continue
    out.append(f'== frame {f}: {NOTE[f]}')
    by_line = collections.OrderedDict()
    for r in rs:
        by_line.setdefault(r['line'], []).append(r)
    for ln, lr in by_line.items():
        toks = []
        for r in lr:
            g = r['group'].strip(); d = re.sub(r'\D', '', g); plus = '+' if '+' in g else ''
            c = cov[f]; c['groups'] += 1
            if not d or '?' in g or not d.isdigit():
                toks.append(f'[{g}]'); continue
            v = key.get(int(d))
            if v is None:
                toks.append(f'[{d}]{plus}'); continue
            val, gr = v
            c['all'] += 1; c['no_A'] += gr != 'A'; c['no_A_no_B'] += gr not in ('A', 'B')
            toks.append((val.upper() if gr == 'A' else val) + plus)
        out.append(f'L{ln}: ' + ' '.join(toks))
    out.append('')
(B / 'decodes' / 'm30_undecoded_v4.txt').write_text('\n'.join(out) + '\n')
with open(B / 'decodes' / 'coverage.tsv', 'w') as fh:
    fh.write('frame\tgroups\tcovered_all\tshare_all\tcovered_no_A\tshare_no_A\tcovered_no_A_no_B\tshare_no_A_no_B\n')
    tot = collections.Counter()
    for f, c in cov.items():
        if not c['groups']: continue
        tot.update(c)
        fh.write(f"{f}\t{c['groups']}\t{c['all']}\t{c['all']/c['groups']:.3f}\t{c['no_A']}\t{c['no_A']/c['groups']:.3f}\t{c['no_A_no_B']}\t{c['no_A_no_B']/c['groups']:.3f}\n")
    fh.write(f"all\t{tot['groups']}\t{tot['all']}\t{tot['all']/tot['groups']:.3f}\t{tot['no_A']}\t{tot['no_A']/tot['groups']:.3f}\t{tot['no_A_no_B']}\t{tot['no_A_no_B']/tot['groups']:.3f}\n")
print(open(B / 'decodes' / 'coverage.tsv').read())
