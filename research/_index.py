"""Write research/README.md, the index of every folder in research/.

  python research/_index.py            rewrite research/README.md
  python research/_index.py --check    exit 1 if a folder is missing from the index or the file is out of date

Each folder is listed once, under its kind (sweep, vetting pass, contributed batch, survey, analysis, tooling) and,
for sweeps, its area. The title is the first line of the folder's README.md (or BRIEF.md, REPORT.md, PLAN.md), the
count is the number of rows in its candidates.json. A new folder is placed by the rules in `place()`; when no rule
fits it lands under "Not yet filed" and --check fails, so add a rule or an OVERRIDE entry here.

Folders are not renamed or moved: merge.py, COVERAGE.md, the leads' score notes and the target notes cite them by path.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'README.md')

AREAS = [
    'France', 'Italy and the Papacy', 'Spain and Portugal', 'Low Countries',
    'Germany, Austria, Switzerland and central Europe', 'Scandinavia and the Baltic', 'Britain and Ireland',
    'Poland, Russia, the Balkans and the Ottoman world', 'United States and Canada', 'Latin America',
    'Asia, Oceania and Africa', 'Across archives: portals, print and follow-up passes',
]
(FR, IT, ES, NL, DE, SC, UK, EAST, US, LATAM, ASIA, CROSS) = AREAS

KINDS = ['tooling', 'brief', 'vetting', 'contributed', 'survey', 'analysis']
KIND_TITLES = {
    'tooling': 'Shared tooling',
    'brief': 'Session briefs',
    'vetting': 'Vetting and verification passes',
    'contributed': 'Lead batches sent by contributors',
    'survey': 'Surveys and collections',
    'analysis': 'Analyses across targets',
}
KIND_NOTES = {
    'tooling': 'The sweep brief (what counts as a lead, the row schema), the duplicate search and the merge into `leads.json`.',
    'brief': 'The instructions given to every agent of one sweep pass. Kept for the record; the current rules are in `archive_sweep_2026-10/BRIEF.md` and `vetting_2026-11/BRIEF.md`.',
    'vetting': 'Passes that took leads already found and checked them against the vetting bar (README Conventions), or re-checked catalogue entries.',
    'contributed': 'Leads, corrections and key material sent by contributors through issues and pull requests, filed as they arrived.',
    'survey': 'Work on a list or a collection that is not one target.',
    'analysis': 'Studies run over the finished targets and their profiles.',
}

# Folders the rules below cannot place from their name.
OVERRIDE = {
    'archive_sweep_2026-10': 'tooling',
    'catalogue_review_20261020': 'vetting', 'frame_check_2026-10': 'vetting', 'latam_vetting': 'vetting',
    'verify_2026-10': 'vetting',
    'dudout_2026-10-29': 'contributed', 'dudout_sarmiento_ms2093': 'contributed',
    'catalogue_harvest': 'survey', 'cryptoole': 'survey', 'oldest': 'survey', 'top50': 'survey', 'mtc3': 'survey',
    'siena2308': 'survey',
    'families': 'analysis', 'keyedit': 'analysis', 'patterns': 'analysis', 'qa': 'analysis',
    'reading_audit': 'analysis', 'routes': 'analysis',
    'central_archives': CROSS, 'chrome_pass_2026-11': CROSS, 'founders_emlo': CROSS,
    'browser_pass_oenb_basel_geneva': DE, 'swiss_austrian': DE, 'nara_military': US,
    'sweep_2026-11_A_halfdone': CROSS, 'sweep_2026-11_B_unswept_south': CROSS, 'sweep_2026-11_D_east_north': CROSS,
    'sweep_2026-11_malta_nordic_baltic': SC, 'sweep_2026-11_baltic_hungary_chrome': CROSS,
    'sweep_2026-11_turin_genoa_naples': IT, 'sweep_2026-11_africa_us_remainder': CROSS,
    'sweep_2026-11-11_us_uk_leftovers': CROSS, 'sweep_2026-11_hab_swiss_german_libs': DE,
    'sweep_2026-11_mirka_cryptoworld': DE, 'sweep_2026-11_slovak_croatia_findingaids': DE,
    'sweep_2026-11-11_southeast': DE, 'sweep_2026-11_hhsta_ais': DE, 'sweep_2026-11_ireland_uk_univ': UK,
    'sweep_2026-11_swiss_cantonal': DE, 'sweep_2026-11_an_digitised': IT, 'sweep_2026-11_manus_italian_libs': IT,
    'sweep_2026-11_internet_culturale': IT, 'sweep_2026-11-11_alvin_waller': SC, 'sweep_2026-11_ape': CROSS,
    'sweep_2026-11_canada_chrome': US, 'sweep_2026-11_canada_provincial': US, 'canada_latam': LATAM,
    'sweep_2026-11_us_blocked': US, 'chi_polish': US, 'sweep_2026-11_digital_ms_libraries': CROSS, 'sweep_2026-11_austria_german_states': DE,
}

# First match wins; tested against the folder name without its "sweep_<date>_" prefix.
RULES = [
    (r'gallica|bellievre|archives_nationales|calames|france', FR),
    (r'pares|bne|hispana|bdcyl|bvpb|spain|torre_do_tombo|bnp|portugal', ES),
    (r'^it_|ital|asf|map_paging|medici|milan|venice|naples|turin|vat|b1\d\d_backfill', IT),
    (r'nationaal|dutch|netherlands|belgium|kb_', NL),
    (r'riksarkivet|tkua|nordic|scandinavia|denmark|baltic', SC),
    (r'german|archivportal|kalliope|hhsta|aut_|czech|hungary|mnl', DE),
    (r'^uk_|tna|archiveshub|lambeth|bodleian|british_library', UK),
    (r'polish|russia|balkans|ottoman', EAST),
    (r'^latam|mexico|brazil', LATAM),
    (r'^chi_|^us_|^nara|nyc|dpla|canada', US),
    (r'asia|oceania|jacar|qdl', ASIA),
    (r'^ia_|hathitrust|europeana|wikisource|literature|printed|undeciphered|siblings|leftovers|arabic|hebrew|'
     r'digital_ms|new_sources', CROSS),
]


def place(name):
    """Kind or area for one folder, or None."""
    if name in OVERRIDE:
        return OVERRIDE[name]
    if re.match(r'_nov\d+$', name):
        return 'brief'
    if name.startswith('vetting'):
        return 'vetting'
    if re.match(r'(dudout|wainut)_leads', name):
        return 'contributed'
    bare = re.sub(r'^sweep_\d{4}-\d\d(-\d\d)?_', '', name)
    for pat, area in RULES:
        if re.search(pat, bare):
            return area
    return None


def title(folder):
    for f in ('README.md', 'BRIEF.md', 'REPORT.md', 'PLAN.md', 'FAMILIES.md', 'CANDIDATES.md', 'NOTES.md'):
        p = os.path.join(HERE, folder, f)
        if os.path.exists(p):
            with open(p, encoding='utf-8', errors='replace') as fh:
                for line in fh:
                    line = line.strip().lstrip('#').strip()
                    if line:
                        line = re.sub(r'\s+', ' ', line).replace('|', '/')
                        return line if len(line) <= 150 else line[:147].rstrip() + '...'
    return ''


def rows(folder):
    p = os.path.join(HERE, folder, 'candidates.json')
    if not os.path.exists(p):
        return None
    try:
        with open(p, encoding='utf-8') as fh:
            data = json.load(fh)
    except ValueError:
        return None
    return len(data) if isinstance(data, list) else None


def when(folder, text):
    """Sort key: the date in the folder name, else the first date in its title."""
    m = re.search(r'(\d{4})-(\d\d)(?:-(\d\d))?', folder)
    if m:
        return (m.group(1), m.group(2), m.group(3) or '00')
    months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
    m = re.search(r'(?:(\d{1,2})(?:-\d{1,2})? )?(%s)[a-z]* (20\d\d)' % '|'.join(months), text)
    if m:
        return (m.group(3), '%02d' % (months.index(m.group(2)) + 1), '%02d' % int(m.group(1) or 0))
    return ('0000', '00', '00')


def build():
    folders = sorted(d for d in os.listdir(HERE) if os.path.isdir(os.path.join(HERE, d)) and d != '__pycache__')
    placed, unfiled = {}, []
    for d in folders:
        k = place(d)
        (placed.setdefault(k, []) if k else unfiled).append(d)
    sweeps = sum(len(placed.get(a, [])) for a in AREAS)

    out = ['# research/', '',
           '<!-- Generated by research/_index.py; do not edit by hand. Edit the script, then run it. -->', '',
           'Work that is not a single cipher target: the archive sweeps that look for new ciphers, the passes that '
           'vet what they find, and a few surveys and analyses. One folder per piece of work, %d in all, %d of them '
           'sweeps. This file lists each folder once.' % (len(folders), sweeps), '',
           '## Start here', '',
           '| File | What it is |', '|---|---|',
           '| [`SWEEP.md`](SWEEP.md) | The brief a contributor gives their own AI agent to run one sweep: read what has '
           'been searched, choose an archive, search, write the folder. |',
           '| [`VET.md`](VET.md), [`vet.py`](vet.py) | The brief a contributor gives their agent to vet leads already found, '
           'the list of leads waiting (`--list`) and the check of a vetting file (`--check`). |',
           '| [`COVERAGE.md`](COVERAGE.md) | What has **not** been swept yet, by area and archive. Pick a sweep from it; '
           'remove the row when a sweep closes it. |',
           '| [`leads.json`](leads.json) | Every lead the sweeps found that is not yet vetted into `catalogue.json`. '
           'Written by `merge.py`, never by hand. |',
           '| [`archive_sweep_2026-10/BRIEF.md`](archive_sweep_2026-10/BRIEF.md) | What counts as a lead, and the row a '
           'sweep writes for each one (`candidates.json`). |',
           '| [`archive_sweep_2026-10/known.py`](archive_sweep_2026-10/known.py) | `python known.py "<shelfmark or name>"`: '
           'is this item already in the catalogue, the leads, the notes or DECODE? Run it before writing a row. |',
           '| [`vetting_2026-11/BRIEF.md`](vetting_2026-11/BRIEF.md) | How a lead is vetted before it can enter the '
           'catalogue (the vetting bar is in the README Conventions). |', '',
           'A lead goes from a sweep to the catalogue in four steps: the sweep writes `<folder>/candidates.json`; '
           '`python research/archive_sweep_2026-10/merge.py --write` merges it into `leads.json`; a vetting pass fills '
           'the lead\'s `vetting` block; `python docs/_check_catalogue.py --promote <id>` moves it to `catalogue.json`. '
           'A contributor\'s agent does the first step from [`SWEEP.md`](SWEEP.md) or the third from [`VET.md`](VET.md), and sends its folder as a pull '
           'request ([CONTRIBUTING.md](../CONTRIBUTING.md), "Searching an archive with your AI").', '',
           '## A sweep folder', '',
           '| File | Content |', '|---|---|',
           '| `README.md` | What was searched (portal, terms, date), what was found, what was blocked and what is left. '
           'A sweep that found nothing still keeps this, so the next one does not repeat it. |',
           '| `candidates.json` | One row per lead, in the BRIEF schema. `[]` is a valid result. |',
           '| `coverage.md`, `key_leads.json` | Optional: series looked at page by page; bare keys found on the way. |',
           '| scripts, `hits.jsonl`, logs | The harvest as it was run. Page images and downloads stay out of git. |', '',
           'Folder names are historical and are cited by path from `merge.py`, `COVERAGE.md`, the leads and the target '
           'notes, so folders are not renamed. A new sweep is named `sweep_<yyyy-mm-dd>_<archive or area>`; after adding '
           'one, run `python research/_index.py`.', '',
           '## Sweeps, by area', '',
           '"Rows" is the number of leads in the folder\'s `candidates.json` (0 = searched, nothing kept; a dash = the '
           'sweep kept its finds elsewhere, see its README). Oldest first within an area.', '']

    def table(names, with_rows):
        info = [(when(d, title(d)), d, title(d)) for d in names]
        info.sort()
        head = '| Folder | Rows | What it covers |' if with_rows else '| Folder | What it is |'
        t = [head, '|---|---|---|' if with_rows else '|---|---|']
        for _, d, ti in info:
            if with_rows:
                n = rows(d)
                t.append('| [`%s/`](%s/) | %s | %s |' % (d, d, '&mdash;' if n is None else n, ti))
            else:
                t.append('| [`%s/`](%s/) | %s |' % (d, d, ti))
        return t + ['']

    for a in AREAS:
        if placed.get(a):
            out += ['### ' + a, ''] + table(placed[a], True)
    for k in KINDS:
        if placed.get(k):
            out += ['## ' + KIND_TITLES[k], '', KIND_NOTES[k], ''] + table(placed[k], False)
    if unfiled:
        out += ['## Not yet filed', '', 'Add a rule or an `OVERRIDE` entry in `_index.py` for these.', '']
        out += table(unfiled, True)
    return '\n'.join(out).rstrip() + '\n', unfiled


def main():
    text, unfiled = build()
    if '--check' in sys.argv:
        old = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else ''
        if unfiled:
            print('not filed in research/_index.py: ' + ', '.join(unfiled))
        if old != text:
            print('research/README.md is out of date: run python research/_index.py')
        sys.exit(1 if unfiled or old != text else 0)
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)
    print('wrote research/README.md' + ('; not filed: ' + ', '.join(unfiled) if unfiled else ''))


if __name__ == '__main__':
    main()
