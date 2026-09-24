"""Put the date of each finding into the result tables of README.md and SOLVED_CATALOGUE.md.

The dates are the ones the site publishes (docs/_dates.json, seeded from the git history by _seed_dates.py):
the day the finding first landed in the repository. Rows that have no write-up page are dated from the first
commit that touched their working directory. The new column is inserted after the existing "Date" column, which
holds the date of the document itself, not of the work; re-running updates the column in place.

Run:  python _stamp_markdown.py       (from docs/)
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import _build_site as B

PAGES = json.loads((HERE / '_dates.json').read_text(encoding='utf-8'))['pages']
_dir_cache = {}


def dir_date(name):
    """First commit that touched a working directory, for findings with no write-up page."""
    if name not in _dir_cache:
        out = subprocess.run(['git', 'log', '--reverse', '--format=%ad', '--date=short', '--', name],
                             cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
        _dir_cache[name] = out[0] if out else ''
    return _dir_cache[name]


def row_date(cells):
    """Date a README row from its links: the write-up page first, then the working directory."""
    text = ' | '.join(cells)
    m = re.search(r'cyphersolver/([a-z0-9]+)\.html', text)
    if m and m.group(1) in PAGES: return PAGES[m.group(1)]['first']
    for d in re.findall(r'\]\(([a-z0-9_]+)/', text):
        if d in PAGES: return PAGES[d]['first']
        if (ROOT / d).is_dir():
            got = dir_date(d)
            if got: return got
    return ''


def short(iso):
    return B.fmt_date(iso, short=True) if iso else '—'


def split_row(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def join_row(cells):
    return '| ' + ' | '.join(cells) + ' |'


def stamp_table(lines, i, header, date_of):
    """Insert or refresh the date column of the table whose header row is lines[i]. Returns rows stamped.

    The column goes immediately after the existing "Date" column, which is the date of the document itself."""
    head = split_row(lines[i])
    width = len(head)
    at = (head.index('Date') + 1) if 'Date' in head else len(head)
    if head[at if at < len(head) else -1] == header:   # already stamped: refresh in place
        at = head.index(header)
        insert = False
    else:
        insert = True
        head.insert(at, header)
    rows = 0
    j = i + 2
    body = []
    while j < len(lines) and lines[j].startswith('|'):
        cells = split_row(lines[j])
        if len(cells) != width:
            print(f'  skipped a row of {header} table with {len(cells)} cells, expected {width}')
            body.append(lines[j]); j += 1; continue
        iso = date_of(cells)
        if insert: cells.insert(at, short(iso))
        else: cells[at] = short(iso)
        body.append(join_row(cells)); rows += 1
        j += 1
    lines[i] = join_row(head)
    lines[i + 1] = '|' + '---|' * len(head)
    lines[i + 2:j] = body
    return rows, j


# README: heading above the table -> the word that heads its date column
import _methods as M
README_TABLES = {M.SECTION[m]: 'Landed' for m in M.METHODS}   # one table per outcome method

# SOLVED_CATALOGUE has no links in its rows, so its targets are matched by name
CATALOGUE_SLUGS = [
    ('Henry of Navarre', 'segur'), ('Swatow telegram', 'sunyatsen'), ('Huang Xing', 'huangxing'),
    ('Fra Giovanni di Lucca', 'lucca'), ('Warsaw, 24 Dec 1627', 'warsaw'), ('Maltravers', 'ormonde'),
    ('Richelieu', 'richelieu'), ('Armstrong', 'armstrong'), ('Louvois and Louis XIV', 'catinat1691'),
    ('Feuquières', 'feuquieres'), ('Urquhart', 'urquhart'), ('Lanssac', 'lanssac'), ('Philip II', 'mendoza1589'),
    ('Boswell', 'boswell'), ('Forster', 'forster'), ('Béthune', 'bethune'), ('Nevers', 'nevers1593'),
    ('Jean du Bellay', 'dir:dubellay'), ('Landgrave Maurice', 'hesse1603'), ('Roosevelt', 'roosevelt'),
    ('gold bar', 'goldbar'), ('Hyde', 'hyde'), ("D'Agapeyeff", 'dir:dagapeyeff'), ('Beale', 'dir:beale'),
    ('Mondoucet', 'mondoucet'), ('Vatican', 'vatican'), ('Debosnys', 'debosnys'), ('Scorpion', 'scorpion'),
    ('Copenhagen', 'copenhagen'), ('Voynich', 'voynich'), ('ADFGVX', 'adfgvx'),
]


def catalogue_date(cells):
    text = ' | '.join(cells)
    for needle, slug in CATALOGUE_SLUGS:
        if needle in text:
            return dir_date(slug[4:]) if slug.startswith('dir:') else PAGES.get(slug, {}).get('first', '')
    return ''


def stamp_file(path, tables, date_of):
    lines = path.read_text(encoding='utf-8').split('\n')
    total = 0
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line in tables:
            j = i + 1
            while j < len(lines) and not lines[j].startswith('|'): j += 1
            if j < len(lines):
                rows, end = stamp_table(lines, j, tables[line], date_of)
                print(f'  {line[:52]:54} {rows} rows')
                total += rows
                i = end
                continue
        i += 1
    path.write_text('\n'.join(lines), encoding='utf-8')
    return total


if __name__ == '__main__':
    print('README.md')
    n1 = stamp_file(ROOT / 'README.md', README_TABLES, row_date)
    print('SOLVED_CATALOGUE.md')
    n2 = stamp_file(ROOT / 'SOLVED_CATALOGUE.md', {
        '## 1. Solved or read in full': 'Solved',
        '## 2. Partly read (key recovered in part, long stretches read)': 'Read',
        '## 3. Explained: not a cipher, or nothing to read': 'Explained',
    }, catalogue_date)
    print(f'stamped {n1 + n2} rows')
