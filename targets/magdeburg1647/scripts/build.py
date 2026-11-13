"""build.py : rebuild every decryption, unit ledger and count of targets/magdeburg1647 from the frozen files.
Standard library only; run from the target folder with python3 -I scripts/build.py.
Judgements (S/E per word) are NOT made here: they are read from the original one-pass ledgers in units/ledgers/
(b160 for reader 1, b162 for reader 2) and matched, in order, to the decoded words. The script recounts them,
checks every per-line figure the ledger states, and writes units/*.tsv, decryptions/*.txt and counts.txt."""
import re, sys, pathlib, hashlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decode as D
HERE = pathlib.Path('.')
K1, K2 = 'gloss/KEY_lasa_v1.txt', 'gloss/KEY_lasa_v2.txt'
# slip, reader, transcription, key, ledger, role
JOBS = [
 ('f6_KEY_v1', 'R1', 'transcriptions/f6_frame10_R1_training.txt', K1, 'units/ledgers/R1_b160_score_f6_v1.txt', 'held out from KEY_v1; then TRAINING text of KEY_v2'),
 ('f7',   'R1', 'transcriptions/f7_frame11_R1.txt',   K2, 'units/ledgers/R1_b160_score_f7_v2.txt',   'held out (first pass)'),
 ('f7',   'R2', 'transcriptions/f7_frame11_R2.txt',   K2, 'units/ledgers/R2_b162_SCORES.txt#f.7',    'held out (second reader)'),
 ('f101', 'R2', 'transcriptions/f101_frame117_R2.txt', K2, 'units/ledgers/R2_b162_SCORES.txt#f.101', 'held out (first pass; one reader only)'),
 ('f102', 'R1', 'transcriptions/f102_frame118_R1.txt', K2, 'units/ledgers/R1_b160_score_f102_v2.txt', 'held out (first pass)'),
 ('f102', 'R2', 'transcriptions/f102_frame118_R2.txt', K2, 'units/ledgers/R2_b162_SCORES.txt#f.102', 'held out (second reader)'),
 ('f104', 'R1', 'transcriptions/f104_frame121_R1.txt', K2, 'units/ledgers/R1_b160_score_f104_v2.txt', 'held out (first pass)'),
 ('f104', 'R2', 'transcriptions/f104_frame121_R2.txt', K2, 'units/ledgers/R2_b162_SCORES.txt#f.104', 'held out (second reader)'),
 ('f204', 'R1', 'transcriptions/f204_frame233_R1.txt', K2, 'units/ledgers/R1_b160_score_f204_v2.txt', 'held out (first pass)'),
 ('f204', 'R2', 'transcriptions/f204_frame233_R2.txt', K2, 'units/ledgers/R2_b162_SCORES.txt#f.204', 'held out (second reader)'),
]
def ledger(spec):
    """returns (list of S words in order, list of (S, n) per line or None, stated total S, stated total words)"""
    fn, _, sec = spec.partition('#'); txt = open(fn, encoding='utf-8').read()
    if sec:
        m = re.search(re.escape(sec) + r' \(frame.*?\n(.*?)TOTAL S (\d+) / (\d+)', txt, re.S); body = m.group(1)
        tS, tN = int(m.group(2)), int(m.group(3))
    else:
        body = txt; m = re.search(r'S = [\d+ ]+= (\d+) ?; words = [\d+ ]+= (\d+)', txt) or re.search(r'Strict (\d+)/(\d+)', txt)
        tS, tN = int(m.group(1)), int(m.group(2))
    per = re.findall(r'L(\d+) ([^|\n]*?) ?(\d+)/(\d+)', body)
    if per:
        Sw = [w for _, ws, _, _ in per for w in ws.split()]
        return Sw, [(int(s), int(n)) for _, _, s, n in per], tS, tN
    m = re.search(r'S words(?: \(\d+\))?: (.*)', body); Sw = [w for w in m.group(1).replace('|', ' ').split() if w != '-']
    pm = re.search(r'Per line S/words: (.*)', body)
    per = [tuple(map(int, x.split('/'))) for x in pm.group(1).split(', ')] if pm else None
    return Sw, per, tS, tN
def run():
    rows, report, ok = [], [], True
    for slip, rd, tf, kf, led, role in JOBS:
        k = D.load_key(kf); L = D.lines(tf)
        words = [(li + 1, w, D.dec_word(w, k)) for li, ws in enumerate(L) for w in ws if w != '|']
        Sw, per, tS, tN = ledger(led)
        lab = ['E'] * len(words); j = 0; unmatched = []
        for s in Sw:
            jj = next((i for i in range(j, len(words)) if words[i][2] == s), None)
            if jj is None: unmatched.append(s); continue
            lab[jj] = 'S'; j = jj + 1
        S = lab.count('S'); N = len(words)
        # per-line check
        lines_n = [sum(1 for w in ws if w != '|') for ws in L]; lines_s = [0] * len(L)
        for (li, _, _), l in zip(words, lab):
            if l == 'S': lines_s[li - 1] += 1
        per_ok = per is None or [n for _, n in per] == lines_n and [s for s, _ in per] == lines_s
        holes = sum('?' in d for _, _, d in words); s_with_hole = sum('?' in d for (_, _, d), l in zip(words, lab) if l == 'S')
        name = f'{slip}_{rd}'
        D_out = D.decode(kf, tf); pathlib.Path(f'decryptions/{name}.txt').write_text(D_out, encoding='utf-8')
        with open(f'units/{name}.tsv', 'w', encoding='utf-8') as f:
            f.write('line\tword\tcipher\tdecoded\tlabel\thole\n')
            for i, ((li, w, d), l) in enumerate(zip(words, lab)): f.write(f'{li}\t{i+1}\t{w}\t{d}\t{l}\t{"?" if "?" in d else ""}\n')
        good = (S == tS and N == tN and not unmatched and per_ok)
        ok &= good
        report.append((slip, rd, role, tf, D.md5(tf), kf, D.md5(kf), S, N, tS, tN, unmatched, per_ok, holes, s_with_hole, good))
    return report, ok
TRAIN = [('f5_R1_v2tx_KEY_v1_training', 'transcriptions/f5_frame8_R1_v2_training.txt', K1),
         ('f5_R1_v2tx_KEY_v2_training', 'transcriptions/f5_frame8_R1_v2_training.txt', K2),
         ('f6_R1_KEY_v2_training', 'transcriptions/f6_frame10_R1_training.txt', K2)]
if __name__ == '__main__':
    for name, tf, kf in TRAIN:   # training text: decoded for display only, never counted
        pathlib.Path(f'decryptions/{name}.txt').write_text(D.decode(kf, tf), encoding='utf-8')
    rep, ok = run()
    o = ['# counts.txt: written by scripts/build.py from the frozen files and the one-pass ledgers. Strict share = S/(S+E+N); N = 0 (no code groups in these slips).',
         "# Rule (b160, read after freezing): S = the decoded string is a German or Latin word as it stands (period spellings u/v, i/j, dt, th allowed;",
         "# proper names count; two words run together in the cipher count S when both read); E otherwise. No emendation, no rescoring.",
         "# Dan Bourdeau's rule ('?' units are holes): a word holding '?' (a cipher letter not in the key file: m, j, v) is counted not read.", '']
    for slip, rd, role, tf, tm, kf, km, S, N, tS, tN, um, pok, holes, swh, good in rep:
        o.append(f'{slip} {rd} [{role}]  tx {tf} md5 {tm[:8]}  key {kf.split("/")[-1]} md5 {km[:8]}')
        o.append(f'   strict S/(S+E+N) = {S}/{N} = {100*S/N:.2f}%   (ledger states {tS}/{tN}; per-line figures {"match" if pok else "DO NOT MATCH"}; unmatched ledger words {um or "none"})')
        o.append(f"   words holding '?': {holes}; of them labelled S: {swh}  ->  Dan's '?'-as-hole rule: {S-swh}/{N} = {100*(S-swh)/N:.2f}%")
        o.append(f'   reproduces: {"YES" if good else "NO"}')
    o.append('')
    o.append('Figure of record per slip (first pass with the frozen KEY_v2; training text excluded):')
    first = {('f7','R1'),('f101','R2'),('f102','R1'),('f104','R1'),('f204','R1')}
    for r in rep:
        if (r[0], r[1]) in first: o.append(f'   {r[0]}: {r[7]}/{r[8]} = {100*r[7]/r[8]:.2f}% (reader {r[1]})')
    o.append('Second reader on the same slips (b162, frozen before its own one decode):')
    for r in rep:
        if r[1] == 'R2' and r[0] != 'f101': o.append(f'   {r[0]}: {r[7]}/{r[8]} = {100*r[7]/r[8]:.2f}%')
    bad = [f'{r[0]} {r[1]} (ledger {r[9]}/{r[10]}, reproduced {r[7]}/{r[8]})' for r in rep if not r[-1]]
    o.append('No pooled figure is given as a headline.')
    o.append('ALL LEDGER FIGURES REPRODUCE' if ok else 'LEDGER FIGURES THAT DO NOT REPRODUCE (the reproduced figure is the one used): ' + '; '.join(bad))
    pathlib.Path('counts.txt').write_text('\n'.join(o) + '\n', encoding='utf-8'); print('\n'.join(o))
