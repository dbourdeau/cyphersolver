"""Apply the 3 Nov 2026 lead review (review_hessen, review_ni_labw, review_bayern) to research/leads.json through the gate.

open -> vetting block written, then --promote; read, partly_read, duplicate, key_lookup, not_cipher -> --close with the reason;
stay -> stays a lead, the blocker goes into "verify". Decisions taken by the main session over the reviewers' verdicts are in OVERRIDE.
Writes review_summary.md."""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
LEADS = os.path.join(ROOT, 'research', 'leads.json')
CHECK = os.path.join(ROOT, 'docs', '_check_catalogue.py')
R = {}
for f in ('review_hessen', 'review_ni_labw', 'review_bayern'):
    R.update(json.load(open(os.path.join(HERE, f + '.json'), encoding='utf-8')))
OVERRIDE = {'2011': ('stay', "Ernst II's memoirs print many extracts of these letters in clear, so the text may already be in print; check the memoirs against a scan before promoting.")}
DUPES = {1951: 'same unit as lead 2033 (KHA A22-195)', 1952: 'same unit as lead 2033 (KHA A22-191)',
         1954: 'same unit as lead 1982 (KHA A23-223)', 1956: 'same unit as lead 1982 (KHA A25-347)',
         1641: 'same unit as lead 1969 (We 5 Bü 2955, listed there as We 50 Bü 2955)'}
d = json.load(open(LEADS, encoding='utf-8'))
by = {e['id']: e for e in d['leads']}
opened, closes, stays, rows = [], [], [], []
for k, r in sorted(R.items(), key=lambda x: int(x[0])):
    n = int(k)
    verdict, reason = r['verdict'], r['reason']
    if k in OVERRIDE:
        verdict, reason = OVERRIDE[k]
    e = by[n]
    for f, v in (r.get('corrections') or {}).items():
        if v:
            e[f] = v
    if r.get('shelfmark'):
        e['shelfmark'] = r['shelfmark']
    if verdict == 'open':
        if r.get('access'):
            e['access'] = r['access']
            e['needs_archive_scan'] = 'yes'
        e['vetting'] = r['vetting']
        e['prior_art'] = 'open (checked 3 Nov 2026: see vetting block)'
        opened.append(n)
    elif verdict == 'stay':
        e['verify'] = 'Blocked (review 3 Nov 2026): ' + reason
        stays.append(n)
    else:
        closes.append((n, verdict, reason))
    rows.append('| %d | %s | %s | %s |' % (n, verdict, e['shelfmark'].replace('|', '/')[:70], reason.replace('|', '/').replace('\n', ' ')))
# Lead-specific clean-up
e = by[1992]
e['shelfmark'] = 'BayHStA, Pfalz-Neuburg Akten 1346'
e['title'] = "Wolfgang Wilhelm of Pfalz-Neuburg: personal notes on his conversion to Catholicism, partly ciphered"
e['verify'] = ('Order a scan. The sibling Neuburger Abgabe 1989, 6286 (copies of two letters to Maximilian, many cipher passages) was left out: '
               'Altmann 1978 treats this relationship from the Munich originals, some with decipherment, and was seen only as snippets.')
e = by[2017]
e['vetting']['key_check'] += ' Promoted on the 13-year gap, like catalogue 1971; if the key reads it, close as key lookup.'
json.dump(d, open(LEADS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for n, verdict, reason in closes:
    subprocess.run([sys.executable, CHECK, '--close', str(n), verdict, reason], check=True)
for n, why in DUPES.items():
    subprocess.run([sys.executable, CHECK, '--close', str(n), 'duplicate', why], check=True)
    rows.append('| %d | duplicate | %s | %s |' % (n, by[n]['shelfmark'][:70], why))
subprocess.run([sys.executable, CHECK, '--promote'] + [str(n) for n in opened], check=True)
# Catalogue 1971: the printed key found by the review
CAT = os.path.join(ROOT, 'catalogue.json')
c = json.load(open(CAT, encoding='utf-8'))
for e in c['entries']:
    if e['id'] == 1971:
        e['vetting']['key_check'] += " Strasser 2017 (https://www.sav.sk/journals/uploads/0307161001500opt.pdf) prints Heinrich the Younger's ciphers from 1 Alt 8 Nr. 490 (Figs 3, 12); not tried, no scan, try them first."
json.dump(c, open(CAT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(os.path.join(HERE, 'review_summary.md'), 'w', encoding='utf-8').write(
    '# Lead review, 3 Nov 2026\n\n| Lead | Outcome | Shelfmark | Why |\n|---|---|---|---|\n' + '\n'.join(rows) + '\n')
print('promoted', len(opened), 'closed', len(closes) + len(DUPES), 'stay', len(stays), stays)
