"""Build only aerssen1601 with the repository builder (Python >=3.12).
Shared listings receive this entry; existing target pages are never processed.
Run: python3.14 targets/aerssen1601/scripts/build_page.py
"""
from pathlib import Path
import sys, json, re
if sys.version_info < (3, 12):
    raise SystemExit('The repository builder needs Python >=3.12; use python3.14 for this helper.')
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / 'docs'
sys.path.insert(0, str(DOCS))
import _build_site as site
slug = 'aerssen1601'
# The contribution date is supplied by the task; no commit/publication is implied.
site.TODAY = '2026-10-04'
profile = json.loads((ROOT / 'targets' / slug / 'profile.json').read_text())
c = profile['conditions']
steps = dict(slug=slug, title=profile['title'], steps=profile['solution'], outcome=profile['outcome'],
             attack=c['attack'], inputs=c['inputs'], prior=c['prior_solution'], human=c['human_role'],
             first=c.get('first_date'), last=c.get('last_date'))
(DOCS / 'steps' / (slug + '.json')).write_text(json.dumps(steps, ensure_ascii=False, separators=(',', ':')))
site.STEPS.add(slug)
site.process(DOCS / (slug + '.html'))
# Stamp only the new finding, preserving all pre-existing findings and page dates.
index = DOCS / 'index.html'
s = index.read_text()
s = re.sub(r'<li>(?:(?!</li>).)*<b>Aerssen to Oldenbarnevelt, 25 May 1601</b>.*?</li>',
           lambda m: site.stamp_finding(m[0]), s, flags=re.S)
index.write_text(s)
site.save_dates(site.DATES)
# Regenerate the shared write-up listing, not the target HTML pages it links.
(DOCS / 'writeups.html').write_text(site.writeups_html())
site.process(DOCS / 'writeups.html')  # Shared listing needs its scripts, icons and dateline too.
site.save_dates(site.DATES)
page = next(p for p in site.PAGES if p['slug'] == slug)
meta_path = DOCS / 'pages.json'
meta = json.loads(meta_path.read_text())
meta = [p for p in meta if p['slug'] != slug]
meta.append(dict(slug=slug, label=site.plain(page['label']), title=site.plain(page['title']),
                 y=page['y'], st=page['st'], stt=site.plain(page['stt'])))
meta_path.write_text(json.dumps(meta, ensure_ascii=False, separators=(',', ':')))
site.check_keys(meta)
search_path = DOCS / 'search.json'
search = [p for p in json.loads(search_path.read_text()) if not p['u'].split('#')[0] == slug + '.html']
search += [p for p in site.search_entries() if p['u'].split('#')[0] == slug + '.html']
search_path.write_text(json.dumps(search, ensure_ascii=False, separators=(',', ':')))
reveal_index = DOCS / 'reveal/index.json'
items = [p for p in json.loads(reveal_index.read_text()) if p['slug'] != slug]
items.append(dict(slug=slug, label=site.plain(page['label'])))
reveal_index.write_text(json.dumps(items, ensure_ascii=False))
site.readme_glance()
print('built aerssen1601.html; updated shared listings; no other target pages processed')
