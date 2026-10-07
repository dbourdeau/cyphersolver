"""Offline scoped site build (Python 3.12+).

Use the repository's builders, limiting page/replay writes to Battier and the
shared landing pages. Merge only Battier into JSON indexes so another target's
concurrent additions are preserved. No other target page is rewritten.
"""
import json
import contextlib
import io
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / 'docs'
sys.path.insert(0, str(DOCS))
import _build_site as site

SLUG = 'battier1686'


def merge_entry(path, entries, field='slug'):
    """Re-read the shared file immediately before the narrow update."""
    current = json.loads(path.read_text())
    added = [entry for entry in entries if entry.get(field) == SLUG]
    assert len(added) == 1, (path, len(added))
    positions = [i for i, entry in enumerate(current) if entry.get(field) == SLUG]
    if positions:
        current[positions[0]] = added[0]
    else:
        current.extend(added)
    path.write_text(json.dumps(current, ensure_ascii=False, separators=(',', ':')) + '\n')


# Generate only our replay through the normal builder.
original_paths = site.M.profile_paths
site.M.profile_paths = lambda: {SLUG: ROOT / 'targets' / SLUG / 'profile.json'}
try:
    site.write_steps()
finally:
    site.M.profile_paths = original_paths
site.STEPS.update(p.stem for p in (DOCS / 'steps').glob('*.json'))

with contextlib.redirect_stdout(io.StringIO()):
    runpy.run_path(str(DOCS / '_build_stats.py'), run_name='__main__')
site.page_dates(SLUG, (DOCS / f'{SLUG}.html').read_text())
(DOCS / 'writeups.html').write_text(site.writeups_html(), encoding='utf-8')

# process(index) invokes live_html; keep its rendering but merge only our record.
def live_html_scoped():
    page = next(p for p in site.PAGES if p['slug'] == SLUG)
    merge_entry(DOCS / 'reveal/index.json', [dict(slug=SLUG, label=site.plain(page['label']))])
    return ('<!-- live:start -->\n<div class="livecount">'
            '<button type="button" class="randbtn" aria-label="Open a random write-up">'
            'Random cipher &rarr;</button></div>\n<!-- live:end -->')


site.live_html = live_html_scoped
for slug in (SLUG, 'index', 'writeups'):
    site.process(DOCS / f'{slug}.html')

path = DOCS / '_dates.json'
dates = json.loads(path.read_text())
for slug in (SLUG, 'index', 'writeups'):
    dates['pages'][slug] = site.DATES['pages'][slug]
for key, value in site.DATES['findings'].items():
    if 'battier' in key.lower():
        dates['findings'][key] = value
site.save_dates(dates)
entries = [entry for entry in site.search_entries()
           if entry['u'].split('#')[0] == f'{SLUG}.html']
path = DOCS / 'search.json'
current = json.loads(path.read_text())
current = [entry for entry in current if entry['u'].split('#')[0] != f'{SLUG}.html']
path.write_text(json.dumps(current + entries, ensure_ascii=False, separators=(',', ':')) + '\n')
site.readme_glance()
meta = [dict(slug=p['slug'], label=site.plain(p['label']), title=site.plain(p['title']),
             y=p['y'], st=p['st'], stt=site.plain(p['stt']))
        for p in site.PAGES if p['slug'] not in site.SURVEYS]
merge_entry(DOCS / 'pages.json', meta)
print('key web:', site.check_keys(meta))
print('built Battier, index, writeups, replay and additive JSON indexes')
