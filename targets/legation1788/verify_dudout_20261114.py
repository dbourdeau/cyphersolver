"""legation1788: independent check (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Reads ONLY key.tsv, ct/*.txt (the code groups as transcribed) and texts/*_decryption.txt / *_reading.txt.
1. Short 26 Jul 1792 (Code No. 10): each group of ct/short_17920726.txt is looked up in key.tsv (171 values from
   Jefferson's interlinear) and set against the group=reading pairs of texts/short_17920726_decryption.txt.
2. key.tsv rows whose group carries more than one different word (not a mere inflection or a split marker).
3. Carmichael 14 Apr 1788 (Code No. 13): the read share of the reading file counted three ways.

    python3 verify_dudout_20261114.py [target_dir]     (part 3 uses research/reading_audit/v10_relabel.py; numpy)
"""
import re, sys, os, pathlib
T = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')

key, other = {}, {}
for line in (T / 'key.tsv').read_text(encoding='utf8').splitlines()[1:]:
    code, g, v, n, o, src = (line.split('\t') + [''] * 6)[:6]
    if code == '10': key[g] = v; other[g] = o

ct = [g for line in (T / 'ct/short_17920726.txt').read_text(encoding='utf8').splitlines() if not line.startswith('#')
      for g in line.strip().strip('.').split('.') if g.strip()]
dec = []
for line in (T / 'texts/short_17920726_decryption.txt').read_text(encoding='utf8').splitlines():
    if line.startswith('#'): continue
    dec += re.findall(r'([\d?]+)=(.*?)\[([A-Z])\]', line)

print('1. Short 26 Jul 1792')
print(f'   groups: ct {len(ct)}, decryption {len(dec)}')
k = lambda s: re.sub(r'[^a-z]', '', s.lower())
grades, same, diff, nokey, misalign, cont = {}, 0, [], 0, [], 0
for i, (g, (g2, r, gr)) in enumerate(zip(ct, dec)):
    grades[gr] = grades.get(gr, 0) + 1
    if g != g2: misalign.append((i + 1, g, g2)); continue
    if r.startswith('('): cont += 1; continue          # second and later groups of a word spread over several groups
    if g not in key: nokey += 1; continue
    if k(key[g]) == k(r) or k(r) in k(key[g]) or k(key[g]) in k(r) or k(r) in [k(x.rsplit(' x', 1)[0]) for x in other[g].split(';') if x]:
        same += 1
    else: diff.append((i + 1, g, key[g], r, gr))
print(f'   grades in decryption: {grades}')
print(f'   group sequence ct vs decryption: {len(misalign)} mismatches {misalign[:10]}')
print(f'   groups with a key.tsv value: {same + len(diff)}; reading agrees with key value or one of its other readings: {same}')
print(f'   continuation groups "(word)": {cont}')
print(f'   groups with no key.tsv value (editors\' reading or open): {nokey}')
for x in diff: print('   differs: pos %d group %s key "%s" decryption "%s" [%s]' % x)

print('\n2. key.tsv groups with more than one different word (two-part code: one group = one value)')
for g in key:
    if not other[g]: continue
    alts = [x.rsplit(' x', 1)[0] for x in other[g].split(';') if x.strip()]
    base = k(key[g])
    odd = [a for a in alts if not (k(a).startswith(base[:4]) or base.startswith(k(a)[:4]))]
    if odd: print(f'   {g}: {key[g]} | also {", ".join(odd)}')

print('\n3. Carmichael 14 Apr 1788: read share of texts/carmichael_17880414_reading.txt')
txt = (T / 'texts/carmichael_17880414_reading.txt').read_text(encoding='utf8')
body = '\n'.join(l for l in txt.splitlines() if l.strip() and not l.startswith('#'))
words = re.findall(r'[^\W\d_]+', re.sub(r'\[[^\]]*\]', ' ', body))
print(f'   clear words {len(words)}; code items 5 (108 x2, 223, 273 by context only, 597 open)')
print(f'   code items only, conjectures not counted as read (as recorded): 0/5 = 0.0')
print(f'   all words, the four conjectures and 597 counted as holes: {1 - 5 / (len(words) + 5):.3f}')
print(f'   all words, conjectures counted as read, 597 a hole: {1 - 1 / (len(words) + 5):.3f}')
try:
    ROOT = T.resolve().parents[1]; sys.path[:0] = [str(ROOT / 'research/reading_audit'), str(ROOT / 'docs')]
    cwd = os.getcwd(); os.chdir(ROOT); import v10_relabel; os.chdir(cwd)
    w, h, d = v10_relabel.share(txt)
    print(f'   v10_relabel.share: {w} words, {h} holes -> {round(1 - (h + d) / (w + h), 3)} '
          f'(capitalised [Maryland] [Massachusetts] are not turned into holes by v2_score.holes; 597, a number, is not counted)')
except Exception as e:
    print('   v10_relabel not loaded:', e)

print('\n4. Words spread over several groups, for the groups of part 2 and other first-group syllables'
      ' (transcription/short_17920726_full.tsv: TJ word over the first group, "(word)" over the rest)')
import csv
rows = list(csv.DictReader(open(T / 'transcription/short_17920726_full.tsv', encoding='utf8'), delimiter='\t'))
for g in ['1101', '689', '562', '1093', '1259', '494', '1388', '534', '1146']:
    spans = []
    for i, r in enumerate(rows):
        if r['group'] != g: continue
        w = r['interlinear'].strip()
        if w.startswith('('):
            j = i
            while j > 0 and rows[j]['interlinear'].startswith('('): j -= 1
            spans.append(f"{'.'.join(x['group'] for x in rows[j:i + 1])}+ ({rows[j]['interlinear']}, {r['frame']})")
            continue
        j = i + 1
        while j < len(rows) and rows[j]['interlinear'].startswith('('): j += 1
        if w: spans.append(f"{'.'.join(x['group'] for x in rows[i:j])} = {w} ({r['frame']})")
    print(f'   {g}: ' + '; '.join(spans))
