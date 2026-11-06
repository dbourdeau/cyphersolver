"""Build catalogue-only candidate rows from saved BNP detail records and merge them into candidates.json.

    python build_rows.py

Each spec names a bib id (BNP catalogue record) and the hand-written fields; shelfmark, the catalogue's cipher phrase and
the stable link are filled from details*.jsonl. Rows already in candidates.json with the same shelfmark are replaced.
Hand-vetted rows (PBA. 614 ...) are written by addrow.py and are not touched here.
"""
import glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REC = {}
for p in sorted(glob.glob(os.path.join(HERE, 'details*.jsonl'))):
    for l in open(p, encoding='utf-8'):
        r = json.loads(l)
        REC.setdefault(r['bib'], r)

CRX = re.compile(r'[^.;|]{0,160}(cifr|chiffr|zifr|c[óo]digo)[^.;|]{0,160}', re.I)
NOTE = 'Scored from the BNP catalogue description during the Nov 2026 BNP sweep (research/sweep_2026-11_bnp_portugal/); not viewed'
PRIOR = 'open as far as checked (5 Nov 2026: DECODE and repo via known.py{}; no edition of these letters found by web search)'


def cota(r):
    ex = re.sub(r'^Exemplares\|Cota\|(Fasciculo\|)?Colecao\|Tipo Acesso\|Estado\|', '', r['exemplares'])
    parts = ex.split('|')
    # microfilm first? take the first non-microfilm cota
    for i in range(0, len(parts), 4):
        if i + 1 < len(parts) and 'Microfilme' not in parts[i + 1]:
            return parts[i]
    return parts[0]


def phrase(r):
    segs = []
    for k in ('TITULO', 'NOTAS', 'CONTEM', 'RESUMO'):
        v = r['fields'].get(k, '')
        segs += [x.strip() for x in re.split(r' / | \. - ', v)]
    hits = [x for x in segs if re.search(r'cifr|chiffr|zifr|c[óo]digo', x, re.I)]
    out = []
    for h in hits:
        m = re.search(r'cifr|chiffr|zifr|c[óo]digo', h, re.I)
        a = max(0, m.start() - 150)
        h2 = ('...' if a else '') + h[a:m.end() + 150] + ('...' if m.end() + 150 < len(h) else '')
        if h2 not in out:
            out.append(h2)
    return ' | '.join(out[:2])


def row(s):
    r = REC[s['bib']]
    sm = s.get('shelfmark') or f"Biblioteca Nacional de Portugal, {s.get('fonds', '')}{cota(r)}"
    status = (f"BNP catalogue record {s['bib']}: '{phrase(r)}'. " + s.get('status', '') +
              (' Not digitised.' if s.get('scan', 'yes') == 'yes' else '') + ' Not on DECODE, not in the repo.')
    out = {
        'year': s['year'], 'date': s['date'], 'title': s['title'], 'correspondents': s['corr'],
        'place': s['place'], 'language': s.get('lang', 'Portuguese'), 'region': s.get('region', 'Portugal'),
        'period': s['period'], 'shelfmark': sm, 'folio_note': s['folio'].replace('{PHRASE}', phrase(r)), 'cls': s.get('cls', 'C'),
        'status': status.strip(), 'why': s['why'], 'importance': s['imp'], 'solvability': s.get('sol', 2),
        'difficulty': s.get('dif', 3), 'score_note': NOTE, 'verify': s['verify'],
        'links': [{'label': 'BNP catalogue record', 'href': f"http://id.bnportugal.gov.pt/bib/catbnp/{s['bib']}"}] + s.get('links', []),
        'seen': 'catalogue', 'source': 'Biblioteca Nacional de Portugal sweep',
        'prior_art': s.get('prior', PRIOR.format(s.get('known', ''))),
        'needs_archive_scan': s.get('scan', 'yes'),
        'access_note': s.get('access', 'Not digitised; BNP Reservados reading room (reservado, sob autorização) or a reproduction order'),
    }
    return out


SPECS = []
import specs  # noqa: E402  (the hand-written fields live in specs.py)
SPECS = list(specs.SPECS)
SPECS += specs.auto(REC, {s['bib'] for s in SPECS})

P = os.path.join(HERE, 'candidates.json')
rows = json.load(open(P, encoding='utf-8')) if os.path.exists(P) else []
for s in SPECS:
    n = row(s)
    rows = [x for x in rows if x['shelfmark'] != n['shelfmark']] + [n]
json.dump(rows, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows;', len(SPECS), 'from specs')
