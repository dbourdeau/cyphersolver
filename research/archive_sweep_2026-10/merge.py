"""Merge the archive sweeps' candidates.json files into research/leads.json (not catalogue.json).

    python research/archive_sweep_2026-10/merge.py            # dry run: report what would be added
    python research/archive_sweep_2026-10/merge.py --write    # append to research/leads.json

Sweep rows are leads, not catalogue entries: a lead reaches catalogue.json only through the vetting gate
(python docs/_check_catalogue.py --promote <id>; README Conventions, "Catalogue vetting bar"). This script never
writes catalogue.json. Each sweep folder's candidates.json follows BRIEF.md. Rows are checked for the required
fields and allowed vocabularies, dropped if their shelfmark or a DECODE id is already in catalogue.json or
research/leads.json, given the next free ids (shared with the catalogue),
and tagged counted / scored "sweep". A row with needs_archive_scan "yes" becomes access "archive" (the site's
"needs archive scans" pill). merged.json records which sweep row became which id.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SWEEPS = ['nationaal_archief', 'torre_do_tombo', 'pares_ags', 'polish_archives', 'scandinavia', 'medici_bia',
          'founders_emlo', 'central_archives', 'archivportal_d', 'nara_catalog', 'nara_state', 'nara_military',
          'nara_triage_a', 'nara_triage_b', 'nara_triage_c', 'nara_triage_d', 'nara_triage_e',
          'nara_triage_f', 'nara_triage_g', 'nara_triage_h', 'nara_triage_i', 'nara_triage_j', 'nara_triage_k', 'nara_triage_l', 'us_loc', 'us_clements', 'us_friedman', 'us_beinecke_folger', 'us_huntington', 'chi_newberry', 'chi_nara', 'chi_polish', 'chi_riverbank', 'chi_uchicago', 'chi_consortium', 'chi_carli_uic', 'chi_pritzker_chm_cpl', 'chi_northwestern', 'chi_chrome_pass', 'vat_vatican', 'aut_hhsta', 'uk_tna', 'jacar', 'ia_meta', 'ia_fulltext', 'hathitrust', 'europeana', 'ia_pass2_a', 'ia_pass2_b', 'ia_pass2_c', 'venice_milan_decode', 'venice_milan_print', 'milan_archives', 'venice_archives', 'asia_india', 'asia_sinica', 'asia_anri', 'canada_lac', 'oceania_naa', 'latam_mexico', 'latam_brazil', 'latam_southcone', 'latam_north', 'qdl', 'dudout_leads_2026-10-29']
REQUIRED = ['year', 'date', 'title', 'correspondents', 'place', 'language', 'region', 'period', 'shelfmark',
            'folio_note', 'cls', 'status', 'why', 'importance', 'solvability', 'difficulty', 'score_note', 'verify',
            'links', 'seen', 'source']
REGIONS = {'England', 'France', 'Italy', 'Spain', 'Portugal', 'Low Countries', 'Central Europe', 'Germany',
           'Scandinavia', 'Poland-Lithuania', 'Papacy', 'Americas', 'Other'}
PERIODS = {'15th century', '1497-1559', '1560-1589', '1589-1598', '1598-1610', '1611-1650', '1651-1700',
           '1701-1800', '1801-1900', '1901-1950', 'unknown'}


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()


def main(write):
    cat = json.load(open(os.path.join(ROOT, 'catalogue.json'), encoding='utf-8'))
    leads_path = os.path.join(ROOT, 'research', 'leads.json')
    ld = json.load(open(leads_path, encoding='utf-8'))
    leads = ld['leads']
    entries = cat['entries'] + leads              # dedup and id allocation see both; only leads are written
    mp = os.path.join(HERE, 'merged.json')
    prev = json.load(open(mp, encoding='utf-8')) if os.path.exists(mp) else []
    done = {(m['sweep'], m['row']) for m in prev}  # merged once; if since closed and removed, not re-added
    next_id = max([e['id'] for e in entries] + [m['id'] for m in prev]) + 1  # ids are not reused
    have_shelf = {norm(e.get('shelfmark')) for e in entries}
    have_decode = {d for e in entries for d in e.get('decode_ids') or []}
    exclude = json.load(open(os.path.join(HERE, 'exclude.json'), encoding='utf-8'))
    notes = json.load(open(os.path.join(HERE, 'notes.json'), encoding='utf-8'))
    added, problems, log = [], [], []
    for sweep in SWEEPS:
        path = os.path.join(ROOT, 'research', sweep, 'candidates.json')
        if not os.path.exists(path):
            print(f'{sweep}: no candidates.json')
            continue
        rows = json.load(open(path, encoding='utf-8'))
        kept = 0
        for i, r in enumerate(rows):
            if (sweep, i) in done:
                continue
            if str(i) in exclude.get(sweep, {}):
                log.append(f'{sweep}[{i}] excluded: {exclude[sweep][str(i)]}')
                continue
            if str(i) in notes.get(sweep, {}):
                r = dict(r, status=r['status'].rstrip() + ' ' + notes[sweep][str(i)])
            miss = [k for k in REQUIRED if k not in r]
            bad = []
            if r.get('region') not in REGIONS: bad.append(f"region {r.get('region')!r}")
            if r.get('period') not in PERIODS: bad.append(f"period {r.get('period')!r}")
            if r.get('cls') not in ('A', 'B', 'C'): bad.append(f"cls {r.get('cls')!r}")
            for k in ('importance', 'solvability', 'difficulty'):
                if not isinstance(r.get(k), int) or not 1 <= r[k] <= 5: bad.append(f'{k} {r.get(k)!r}')
            if not isinstance(r.get('year'), int): bad.append(f"year {r.get('year')!r}")
            if miss or bad:
                problems.append(f'{sweep}[{i}] {r.get("title", "")[:60]}: missing {miss} bad {bad}')
                continue
            if norm(r['shelfmark']) in have_shelf or have_decode & set(r.get('decode_ids') or []):
                log.append(f'{sweep}[{i}] duplicate of an existing entry: {r["shelfmark"]}')
                continue
            e = {'id': next_id, 'counted': True}
            e.update({k: r[k] for k in r if k not in ('id', 'counted')})
            e.setdefault('ark', '')
            # needs_archive_scan "yes" = nothing to work from online: the site shows the "needs archive scans" pill
            if r.get('needs_archive_scan') == 'yes':
                e.setdefault('access', 'archive')
            elif 'needs_archive_scan' not in r:
                log.append(f'{sweep}[{i}] has no needs_archive_scan: archive access not recorded')
            e['scored'] = 'sweep'
            leads.append(e)
            have_shelf.add(norm(r['shelfmark']))
            have_decode |= set(r.get('decode_ids') or [])
            added.append({'id': next_id, 'sweep': sweep, 'row': i, 'title': r['title']})
            next_id += 1
            kept += 1
        print(f'{sweep}: {len(rows)} rows, {kept} new')
    for p in problems: print('PROBLEM', p)
    for l in log: print(l)
    print(f'total new: {len(added)}' + ('' if write else ' (dry run)'))
    if write and added:
        with open(leads_path, 'w', encoding='utf-8') as fh:
            json.dump(ld, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        json.dump(prev + added, open(mp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main('--write' in sys.argv)
