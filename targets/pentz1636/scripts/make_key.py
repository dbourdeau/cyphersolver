"""Write key.tsv from the frozen tables (key_history/KEY_pentz1636_T1T2.py, md5 8306f733..., a verbatim copy of
lines 4-6 of scripts/original/b106_dec_pentz.py) with the evidence for each value from the Vienna 1636 letter, where
the key was found. No value is added or changed. usage: python3 -I scripts/make_key.py (from the target folder)"""
import hashlib, collections
KF = 'key_history/KEY_pentz1636_T1T2.py'
assert hashlib.md5(open(KF, 'rb').read()).hexdigest() == '8306f733e78da38f1f86ac61d6bfd582', 'key md5'
ns = {}; exec(open(KF).read(), ns); T1, T2 = ns['T1'], ns['T2']
seen = {'1': collections.defaultdict(list), '2': collections.defaultdict(list)}
for l in open('segmentation/vienna_1636-03-26_seg.tsv', encoding='utf8'):
    if l.startswith('#') or l.startswith('n\t'): continue
    n, figs, kind, decl = l.rstrip('\n').split('\t')
    if kind not in '12': continue
    T = T1 if kind == '1' else T2
    word = ''.join(T.get(int(x), '?') if x.isdigit() else '?' for x in figs.split())
    for x in figs.split():
        if x.isdigit(): seen[kind][int(x)].append(word)
rows = ['# key.tsv: Pentz family, key v1 (b106, frozen 12 Nov 2026 before the Vienna run at 04:11 UTC; RFC 3161 04:14:03 GMT).',
        '# 24-letter alphabet abcdefghiklmnopqrstuwxyz (i=j, u=v). The decoder uses exactly these rows (scripts/build.py checks them against key_history/KEY_pentz1636_T1T2.py).',
        '# Built from the ciphertext of the Vienna letter while transcribing it (before the freeze): einige reale dienste, sache, Fridericus showed the two tables and the switch.',
        '# basis: rule = value given by the run of the table only; seen = the value occurs in a Vienna word unit (words listed; E words in the list are not read).',
        '# Index numbers (not letters): 62 = table 1 follows; 13 = table 2 follows. How often each occurs: counts.txt.',
        '# Codes with no value: 168, 226, 85, 63, 64, 12, 11, 8, 9 (Vienna); 165 (Vienna, missed in the transcription); 182, 220, 232, 260, 280, 730, 767 (Glückstadt). Not in this key.',
        '# Not in the decoder: table 2 p=59 q=58 t=55 (implied by the run n=61 o=60 ... u=54, written in key_history/KEY_pentz_v1_b106.txt but never used); table 2 k l m w x y z (no value).',
        'table\tfigure\tletter\tbasis\tseen_in_vienna_words']
for name, T, k in (('T1', T1, '1'), ('T2', T2, '2')):
    for f in sorted(T):
        ws = seen[k].get(f, [])
        rows.append(f'{name}\t{f}\t{T[f]}\t{"seen" if ws else "rule"}\t{len(ws)}: {", ".join(sorted(set(ws)))}' if ws else f'{name}\t{f}\t{T[f]}\trule\t0')
rows.append('index\t62\t(table 1 follows)\tseen\tbefore every table-1 word run')
rows.append('index\t13\t(table 2 follows)\tseen\tbefore every table-2 word run')
open('key.tsv', 'w', encoding='utf8').write('\n'.join(rows) + '\n')
print('rows', len(rows) - 8)
