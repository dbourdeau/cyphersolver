"""Re-check the carleton1782 folder: frozen test intact, predictions reproducible, scores and spelling counts.

    python targets/carleton1782/verify.py

Page images are not in the repository; their hashes stay listed in preclear/SHA256SUMS and the sources.json files
give the Canadiana IIIF addresses to fetch them again.
"""
import csv, hashlib, json, sys
from collections import Counter
from pathlib import Path

F = Path(__file__).resolve().parent
PRE, POST = F / 'carleton_1782-09-25/preclear', F / 'carleton_1782-09-25/postclear'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: list(csv.DictReader(p.open(encoding='utf-8'), delimiter='\t'))
ok = True
def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg); ok &= bool(cond)

# 1. the freeze: manifest and the three hashes the coordinator recorded before the clear copy was opened
missing, bad = [], []
for line in (PRE / 'SHA256SUMS').read_text().splitlines():
    h, n = line.split('  ', 1)
    p = PRE / n
    if not p.exists():
        missing.append(n); continue
    if sha(p) != h: bad.append(n)
check(not bad, f'preclear files match SHA256SUMS ({len(missing)} page images/crops not in the repository)')
check(all(m.startswith(('images/', 'crops/')) for m in missing), 'only images and crops are absent')
check(sha(PRE / 'SHA256SUMS') == 'f04ff7334176e54cc25d934a180450c832898be0ef4f1fc760bd967dbac93c58', 'SHA256SUMS hash = checkpoint')
check(sha(PRE / 'transcript.tsv') == '6d75a2d15991b0510eb0a5e46e6097c9413a15034c6d568d03bd5ba0f9a7d560', 'transcript.tsv hash = checkpoint')
check(sha(PRE / 'predictions.tsv') == '54d46e74558968d3da2418479dcb710e3b7c2e4d8a7084e5d4f52aaf7afece39', 'predictions.tsv hash = checkpoint')
check(json.loads((PRE / 'FREEZE.json').read_text())['clear_consulted'] is False, 'FREEZE.json: clear copy not consulted')
check(sha(F / 'key/armylist_titlepage_1778.txt') == sha(PRE / 'evidence/armylist_titlepage_1778.txt'), 'key file identical to the frozen copy')

# 2. predictions follow mechanically from the frozen key and table
key = {}
for l in (F / 'key/armylist_titlepage_1778.txt').read_text(encoding='utf-8').splitlines():
    if '\t' in l and not l.startswith('#'):
        n, s = l.split('\t', 1); key[int(n)] = ''.join(c.lower() for c in s if c.isalpha() or c == '&')
def spell(toks):
    out = []
    for a, b in (v.split('-') for v in toks.split()):
        try: out.append(key[int(a)][int(b) - 1])
        except (KeyError, IndexError): out.append('?')
    return ''.join(out)
wc = {r['tokens']: r for r in read(PRE / 'evidence/clinton_word_constraints.tsv')}
pred = read(PRE / 'predictions.tsv')
again = []
for r in read(PRE / 'transcript.tsv'):
    if r['kind'] == 'S': again.append(spell(r['tokens']))
    elif r['kind'] == 'W': again.append(wc[r['tokens']]['local_readings'] if r['tokens'] in wc else '[' + r['tokens'] + ']')
    else: again.append(r['tokens'])
check(again == [p['mechanical_prediction'] for p in pred], f'all {len(pred)} frozen predictions regenerate from key + table')
check(len(wc) == 100, f'frozen table has {len(wc)} word codes')

# 3. the score, against the independent hand alignment of the post-test layer (posttest/rescore.py writes it)
import subprocess
subprocess.run([sys.executable, str(F / 'posttest/rescore.py')], check=True, stdout=subprocess.DEVNULL)
comp = read(F / 'posttest/comparison.tsv')
check([c['prediction'] for c in comp] == [p['mechanical_prediction'] for p in pred], 'posttest/comparison.tsv carries the frozen predictions unchanged')
old = read(POST / 'comparison.tsv')
check([c['mechanical_prediction'] for c in old] == [p['mechanical_prediction'] for p in pred], 'the 12 Nov postclear/comparison.tsv also carries them (its clear column is superseded)')
by = Counter((c['basis'], c['status']) for c in comp)
check(by[('Clinton candidate lexical constraint', 'agrees')] == 55 and
      by[('Clinton candidate lexical constraint', 'fails')] == 3, 'unqualified word predictions: 55 agree, 3 fail')
check(by[('Clinton qualified', 'qualified_set_agrees')] == 21 and by[('Clinton qualified', 'qualified_mismatch')] == 3
      and by[('Clinton qualified', 'no_clear_counterpart')] == 1, 'qualified word predictions: 21 in set, 3 fail, 1 extra')
check(by[('Army List literal', 'agrees')] == 36 and by[('Army List literal', 'fails')] == 6
      and by[('Army List literal', 'no_clear_counterpart')] == 1, 'spelled groups as frozen: 36 exact, 6 differ, 1 extra')
check(by[('uncovered word code', 'uncovered_before_clear')] == 56, '56 word-code occurrences had no prediction')
fails = [(c['order'], c['tokens'], c['prediction'], c['clear_p102']) for c in comp
         if c['basis'] == 'Clinton candidate lexical constraint' and c['status'] != 'agrees']
print('     the three failures:', fails)
sc = json.loads((F / 'posttest/SCORE.json').read_text())['shuffled_control']
check(sc['reaching_real'] == 0, f"shuffled-table control: mean {sc['mean_agreements']}, max {sc['max']} of 58 over {sc['shuffles']} shuffles")

# 4. spelled words in the two training letters
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha()).replace('j', 'i')
sp = read(F / 'clinton_1782-02-22/spellings.tsv')
agree = sum(norm(spell(r['tokens'])) == norm(r['aligned_reading']) for r in sp)
check(len(sp) == 44 and agree == 39, f'Clinton 22 Feb: {agree} of {len(sp)} spelled words agree on the key')
letters = good = words = wgood = 0
for l in (F / 'carleton_1782-09-06/alignment.tsv').read_text(encoding='utf-8').splitlines():
    if l.startswith('S\t'):
        _, t, c = l.split('\t'); got, want = spell(t), norm(c.split()[0])
        words += 1; wgood += got == want; letters += len(want); good += sum(x == y for x, y in zip(got, want))
check((good, letters, wgood, words) == (95, 96, 14, 15), f'Carleton 6 Sep: {good} of {letters} letters, {wgood} of {words} spelled words agree')
fixed = {r['unit']: r['now'].split(' (')[0] for r in read(F / 'posttest/corrections.tsv') if r['letter'] == 'carleton_1782-09-25' and ' ' in r['now'].split(' (')[0]}
check(spell(fixed['129']) == 'escaped', 'post-test transcription correction: unit 129 spells escaped')
cl = {r['order']: r for r in read(F / 'clinton_1782-02-22/alignment.tsv')}
check(cl['159']['tokens'] == '43-19' and cl['159']['clear'] == 'thousand', 'Clinton 43-19 aligned as thousand (corrected)')
print('result:', 'pass' if ok else 'FAIL')
sys.exit(0 if ok else 1)
