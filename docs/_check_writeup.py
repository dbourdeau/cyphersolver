"""Write-up completeness: is a finished cipher on every surface it should be on?

A finished result touches eleven places (see .claude/skills/writeup/SKILL.md). Sessions in this repository
kept skipping some of them, and concurrent sessions committed each other's folders without a write-up, so
this script checks the surfaces mechanically. It reads the working tree; it never edits anything.

Run from anywhere:

  python docs/_check_writeup.py <slug>          every surface for one write-up (slug = docs/<slug>.html)
  python docs/_check_writeup.py --audit         finished targets with no write-up, and other drift
  python docs/_check_writeup.py --hook start    SessionStart hook: short audit as context for the session
  python docs/_check_writeup.py --hook stop     Stop hook: block the stop once when a target this session
                                                worked on looks finished in its NOTES but has no write-up

Exit code 1 from <slug> or --audit when something is missing; the hook modes always exit 0.

A partial outcome ("read in part") is a stopping point only when it is justified: the folder's NOTES.md carries a
`## Remaining gaps` section (every unread piece with a blocker type) and an `## Escalation` checklist (every
standard move done or marked n/a with a reason), and profile.json has outcome.fraction_read and outcome.gaps.
See partial_problems() and the writeup skill, section 0a.
"""
import sys, re, json, pathlib, subprocess, time

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = pathlib.Path(__file__).resolve().parent          # docs/
ROOT = HERE.parent
SITE = 'https://dbourdeau.github.io/cyphersolver/'
SURVEYS = {'famous', 'solved', 'highlights'}
TOOL_PAGES = {'atlas', 'keys', 'secret', 'indus-bench', 'glossary'}   # interactive and reference pages, not write-ups
# The famous undeciphered targets (Indus script, Voynich, Beale, Kryptos ...) are written up on the site but keep no
# profile.json and stay out of the LLM-performance paper data (owner's rule, 23 Sept 2026).
FAMOUS = {'indus', 'voynich', 'beale', 'kryptos', 'dorabella', 'zodiac', 'z340', 'z13', 'linear_a', 'lineara',
          'phaistos', 'rongorongo', 'rohonc', 'goldbar', 'pigeon', 'shugborough', 'tamamshud'}
NOT_TARGETS = {'docs', 'papers', 'gallica_siblings', 'gallica_sweep', 'top50', 'oldest', 'source_headings.txt'}

def read(p):
    try: return pathlib.Path(p).read_text(encoding='utf-8')
    except (FileNotFoundError, UnicodeDecodeError): return ''

# ---------------------------------------------------------------------------
# the surfaces

def manifest():
    """slug -> st for every PAGES entry, and the IMAGES keys, from _build_site.py (no import: it has side effects)."""
    s = read(HERE / '_build_site.py')
    pages = {m.group(1): m.group(2) for m in re.finditer(r"dict\(slug='([a-z0-9]+)'.*?st='([a-z]+)'", s)}
    im = re.search(r'^IMAGES = \{(.*)\}\s*$', s, re.M)
    images = {}
    if im:
        for m in re.finditer(r"'([a-z0-9]+)': (\(|None)", im.group(1)): images[m.group(1)] = m.group(2) == '('
    for m in re.finditer(r"^IMAGES\['([a-z0-9]+)'\] = (\(|None)", s, re.M): images[m.group(1)] = m.group(2) == '('
    version = re.search(r"^VERSION = '([^']+)'", s, re.M)
    return pages, images, version.group(1) if version else ''

def dates():
    try: return json.loads(read(HERE / '_dates.json')).get('pages', {})
    except json.JSONDecodeError: return {}

def readme_rows():
    """Rows of README's Results tables: section, target cell, where cell, linked slugs, linked repo dirs."""
    rows, sect = [], None
    for line in read(ROOT / 'README.md').splitlines():
        if line.startswith('## '): sect = None
        if line.startswith('### '): sect = line[4:].strip(); continue
        if not sect or not line.startswith('| ') or line.startswith('| Target') or line.startswith('|---'): continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 4: continue
        where = cells[-1]
        rows.append(dict(section=sect, target=cells[0], where=where, line=line,
                         slugs=set(re.findall(r'cyphersolver/([a-z0-9]+)\.html', where)),
                         dirs=set(re.findall(r'\]\(([A-Za-z0-9_/]+?)/\)', where))))
    return rows

def catalogue():
    try:
        d = json.loads(read(ROOT / 'catalogue.json'))
        return d if isinstance(d, list) else d.get('entries', [])
    except json.JSONDecodeError: return []

FINISHED = re.compile(r'status:\s*\**\s*(solved|read|broken|resolved|done)\b|\bread in (full|part|substance)\b|'
                      r'\bletter is read\b|\bcipher is broken\b|\bkey (is )?recovered\b|\bdeciphered in full\b|'
                      r'\bsolved \(\d|\bsolved \d{1,2} [A-Z][a-z]+ \d{4}', re.I)
NOT_FINISHED = re.compile(r'status:\s*\**\s*(in progress|open|unsolved|attempted|stuck|blocked|no write-?up)', re.I)

def target_dirs():
    """Root folders with a NOTES.md, and whether the head of the notes reads as finished."""
    out = {}
    for d in sorted(ROOT.iterdir()):
        if not d.is_dir() or d.name in NOT_TARGETS or d.name.startswith('.'): continue
        notes = d / 'NOTES.md'
        if not notes.exists(): continue
        head = '\n'.join(read(notes).splitlines()[:40])
        m = FINISHED.search(head)
        out[d.name] = dict(finished=bool(m) and not NOT_FINISHED.search(head),
                           why=(m.group(0).strip() if m else ''), mtime=notes.stat().st_mtime)
    return out

# ---------------------------------------------------------------------------
# partial readings: "read in part" has to be earned

BLOCKERS = {
    'no-key-material': 'no key on DECODE, in print, or in a sibling, and none rebuildable from the text',
    'too-short': 'too little text to break or to extend the key',
    'illegible': 'the scan cannot be read, and no better image exists',
    'needs-physical-access': 'only the archive holds the missing leaf, key or better image',
    'open-codes': 'the letter reads but nomenclator code groups do not (still workable)',
    'not-attempted': 'not yet worked (never allowed at close)',
}
EXTERNAL = {'no-key-material', 'too-short', 'illegible', 'needs-physical-access'}   # blockers outside the session
ESCALATION = [
    ('siblings', 'neighbouring and sibling DECODE records, and leaves next to the cipher in the volume, opened'),
    ('clear-pages', '"clear" / "cleartext" / "postscript" pages checked for being the decipherment'),
    ('known-keys', 'every known key of the same series, archive, correspondent or decade tried'),
    ('print', 'printed editions and calendars searched (CSP, Bain, Forbes, Fraknoi, Nuntiaturberichte, '
              'Politische Correspondenz, Parke, Lasry GL.htm, Tomokiyo)'),
    ('key-rebuild', 'key extended from what reads (constrained/swap annealing, seeded EM, alphabetical '
                    'bracketing of the nomenclator, LM context)'),
    ('retry', 'every unread group and doubtful reading retried with the extended key and regraded'),
]
PARTIAL = re.compile(r'status:\s*\**\s*(read in part|partly read|partial)|\bread in part\b', re.I)

READ_BAR = 0.95    # README Conventions, "The read bar"; no field standard exists (DECODE status is owner-assigned)


def read_bar(folder):
    """(meets, reasons_not) for the read bar: coherent share >= 0.95, no gap not-attempted, every document read."""
    try: prof = json.loads(read(ROOT / folder / 'profile.json') or '{}')
    except ValueError: return None, ['profile.json unreadable']
    out = prof.get('outcome') or {}
    frac = out.get('fraction_coherent', out.get('fraction_read'))
    why = []
    if not isinstance(frac, (int, float)): why.append('no numeric fraction_read')
    elif frac < READ_BAR: why.append(f'{frac:.2f} < {READ_BAR} of text reads')
    if any((g.get('blocker') == 'not-attempted') for g in out.get('gaps') or []): why.append('a gap is not-attempted')
    docs_open = [d.get('id') for d in prof.get('documents') or [] if d.get('read') in ('read in part', 'not read')]
    if docs_open: why.append('documents not read in full: ' + ', '.join(map(str, docs_open[:4])))
    if out.get('fraction_read_method') == 'estimated': why.append('fraction_read is estimated, not measured')
    return not why, why

def section(text, name):
    m = re.search(rf'^##\s+{name}\b.*?$(.*?)(?=^##\s|\Z)', text, re.M | re.S | re.I)
    return m.group(1) if m else None

def partial_problems(folder):
    """(is_partial, problems, open_blockers) for a folder. Partial = profile outcome 'read in part', or no
    profile outcome and the NOTES head says read in part."""
    notes = read(ROOT / folder / 'NOTES.md')
    try: prof = json.loads(read(ROOT / folder / 'profile.json') or '{}')
    except ValueError: prof = {}
    out = prof.get('outcome') or {}
    cls = out.get('class')
    head = '\n'.join(notes.splitlines()[:40])
    if cls != 'read in part' and not (cls is None and PARTIAL.search(head) and not NOT_FINISHED.search(head)):
        return False, [], set()
    probs, blockers = [], []
    gaps = section(notes, 'Remaining gaps')
    if gaps is None:
        probs.append('NOTES.md has no "## Remaining gaps" section (one line per unread piece: '
                     '"- <piece> - blocker: <type>; <why>")')
    else:
        lines = [l for l in gaps.splitlines() if l.strip().startswith(('-', '*'))]
        if not lines: probs.append('"## Remaining gaps" lists nothing')
        for l in lines:
            m = re.search(r'blocker:\s*([a-z-]+)', l, re.I)
            b = m.group(1).lower() if m else None
            if b not in BLOCKERS: probs.append(f'gap without a valid blocker type: {l.strip()[:90]}')
            elif b == 'not-attempted': probs.append(f'gap marked not-attempted: {l.strip()[:90]}')
            if b: blockers.append(b)
    esc = section(notes, 'Escalation')
    if esc is None:
        probs.append('NOTES.md has no "## Escalation" checklist (' + ', '.join(k for k, _ in ESCALATION) + ')')
    else:
        for k, what in ESCALATION:
            m = re.search(rf'^\s*[-*]\s*\[(x|n/?a)\]\s*{k}\b(.*)$', esc, re.M | re.I)
            if not m: probs.append(f'escalation step "{k}" not done ({what})')
            elif m.group(1).lower().startswith('n') and len(m.group(2).strip(' :-')) < 10:
                probs.append(f'escalation step "{k}" marked n/a without a reason')
    if not out.get('key'): probs.append('profile.json outcome.key missing (recovered / partial / none: state of the key, apart from the text)')
    if 'fraction_read' not in out: probs.append('profile.json outcome.fraction_read missing (share of tokens read)')
    if not out.get('gaps'): probs.append('profile.json outcome.gaps missing (mirror the Remaining gaps list)')
    return True, probs, set(blockers) - EXTERNAL

def git(*args):
    try: return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=20).stdout
    except (OSError, subprocess.TimeoutExpired): return ''

def page_on_main(slug):
    """Does docs/<slug>.html exist on origin/main or main? (Cheap: git cat-file -e, no checkout.)"""
    for ref in ('origin/main', 'main'):
        try:
            r = subprocess.run(['git', 'cat-file', '-e', f'{ref}:docs/{slug}.html'], cwd=ROOT, capture_output=True, timeout=20)
            if r.returncode == 0: return True
        except (OSError, subprocess.TimeoutExpired): pass
    return False

def key_words(target_cell):
    """The name to look for in the ranking and catalogue tables: the README target cell up to the first comma."""
    t = re.sub(r'[*`\[\]]', '', target_cell).split(',')[0].split(' → ')[0].strip()
    return t[:40]

# ---------------------------------------------------------------------------
# one write-up

def image_problems(slug, images=None, skip=None):
    """Images on the page (README Conventions, writeup skill section 1): every image figure names its own source in
    data-credit, and the page shows a snip of the cipher (a figure or an IMAGES
    entry), or docs/_explore_skip.json "snip" says why none can be had. Returns (uncredited figures, problems)."""
    if images is None: images = manifest()[1]
    if skip is None:
        try: skip = json.loads(read(HERE / '_explore_skip.json') or '{}')
        except ValueError: skip = {}
    page = read(HERE / f'{slug}.html') or ''
    figs = [m for m in re.finditer(r'<figure((?! class="(?:party|lead))[^>]*)>.*?</figure>', page, re.S)
            if re.search(r'<img src="[^"]+\.(?:jpe?g|png|gif|webp|svg)"', m.group(0)) and 'portrait_' not in m.group(0)]
    bare = [re.search(r'<img src="([^"]+)"', m.group(0)).group(1) for m in figs
            if not (re.search(r'data-credit="([^"]*)"', m.group(1)) or [0, ''])[1].strip()]
    probs = []
    if bare: probs.append(f'{len(bare)} image figure(s) without data-credit naming their source: {", ".join(bare[:6])}')
    im = images.get(slug)      # True when IMAGES has a lead crop (its credit is the entry's third field)
    if not figs and not im and slug not in skip.get('snip', {}):
        probs.append('no snip of the cipher on the page: crop one from the scans (IMAGES entry or a figure), '
                     'or record why none can be had in docs/_explore_skip.json "snip"')
    return bare, probs

def check_slug(slug):
    pages, images, version = manifest()
    rows = readme_rows()
    ok = True
    def item(good, text, warn=False):
        nonlocal ok
        mark = 'ok  ' if good else ('warn' if warn else 'MISS')
        if not good and not warn: ok = False
        print(f'  [{mark}] {text}')

    page_path = HERE / f'{slug}.html'
    page = read(page_path)
    print(f'{slug}: write-up surfaces')
    item(bool(page), f'docs/{slug}.html exists')
    if page:
        item('<section class="hero">' in page, 'page has a <section class="hero"> (kicker, h1, sub, meta)')
        item('<p class="meta">' in page, 'hero has the <p class="meta"> byline the builder stamps')
        item(bool(re.search(r'<title>.+</title>', page)) and 'name="description"' in page, 'title and meta description')
        item(bool(re.search(r'<h2[^>]*>.*?Sources', page, re.S)), 'a Sources section', warn=True)
        item(bool(re.search(r'\bclass="callout[" ]', page)), 'a summary callout at the top of <main>', warn=True)
        for img in set(re.findall(r'<img[^>]+src="([^"]+)"', page)):
            item((HERE / img).exists(), f'figure file docs/{img} exists')
        item(f'?v={version}' in page if version else True, 'page carries the current stylesheet version (else rebuild)', warn=True)
        item(bool(git('ls-files', f'docs/{slug}.html').strip()), 'page is tracked by git', warn=True)
    st = pages.get(slug)
    item(st is not None, f'PAGES entry in docs/_build_site.py (st={st})')
    item(slug in images, 'IMAGES entry in docs/_build_site.py (None is allowed, a lead figure is better)')
    item(slug in dates(), 'docs/_dates.json has the page (created by the first build)')
    mine = [r for r in rows if slug in r['slugs']]
    item(bool(mine), f'README.md results row links {SITE}{slug}.html')
    index = read(HERE / 'index.html')
    reg = re.search(r'<h2 id="recent">.*?(?=\n<h2|\n<!-- |\Z)', index, re.S)
    item(bool(reg) and f'href="{slug}.html"' in reg.group(0), 'index.html Recent findings has a <li> linking the page')
    wu = read(HERE / 'writeups.html')
    if wu: item(f'href="{slug}.html"' in wu, 'writeups.html lists the page (regenerated by the build)', warn=True)
    # the catalogue holds open targets only: a written-up target's entry is removed (or narrowed and marked attempted)
    folders = set(mine[0]['dirs']) if mine else set()
    if not any(f.lower().rstrip('/').split('/')[-1] == slug.lower() for f in folders) \
            and (not folders or (ROOT / slug).is_dir()):
        folders.add(slug)
    rids = {int(n) for f in folders for n in re.findall(r'\bR(\d{2,5})\b', read(ROOT / f / 'NOTES.md'))}
    cat = [e for e in catalogue() if not (e.get('outcome') or '').startswith('attempted')
           and ((e.get('writeup') or '') == f'{slug}.html' or rids & set(e.get('decode_ids') or [])
                or any(f'{f}/' in str(e.get('status', '')) for f in folders))]
    item(not cat, 'catalogue.json no longer lists the target (read/resolved entries are removed, see the skill)'
         + (': still there as #' + ', #'.join(str(e.get('id')) for e in cat) if cat else ''), warn=True)
    for folder in sorted(folders):
        if folder in FAMOUS:
            item(not (ROOT / folder / 'profile.json').exists(),
                 f'{folder}: a famous target keeps no profile.json and stays out of the paper data')
            continue
        prof = ROOT / folder / 'profile.json'
        good = False
        if prof.exists():
            try:
                import _check_profile, io, contextlib
                with contextlib.redirect_stdout(io.StringIO()):
                    good = _check_profile.check(folder, quiet=True)[0] == 'valid'
            except Exception:
                good = False
        item(good, f'{folder}/profile.json exists and is valid (/profile skill; python docs/_check_profile.py {folder})')
    # a partial reading has to be justified before it is written up as one
    for folder in sorted(folders):
        try: cls = (json.loads(read(ROOT / folder / 'profile.json') or '{}').get('outcome') or {}).get('class')
        except ValueError: cls = None
        if cls == 'read':
            ok, why = read_bar(folder)
            item(ok, f'{folder}: "read" meets the read bar (README Conventions)' + ('' if ok else ': ' + '; '.join(why)),
                 warn=any(w.startswith('no numeric') for w in why))
    for folder in sorted(folders):
        part, probs, _ = partial_problems(folder)
        if part:
            item(not probs, f'{folder}: "read in part" is justified (gaps with blockers, escalation checklist, coverage)'
                 + ''.join(f'\n         - {p}' for p in probs))
    # a finished target read from DECODE records queues its DECODE edits (decode_updates/, see the skill)
    try:
        dq = json.loads(read(ROOT / 'decode_updates' / 'queue.json') or '{}').get('targets', {})
    except ValueError:
        dq = {}
    for folder in sorted(folders):
        prof = ROOT / folder / 'profile.json'
        if not prof.exists():
            continue
        try:
            p = json.loads(read(prof))
        except ValueError:
            continue
        cls = (p.get('outcome') or {}).get('class', '')
        has_ids = any(re.search(r'\bR ?\d{2,5}\b', d.get('id', '') + ' ' + d.get('shelfmark', '')) for d in p.get('documents', []))
        if not has_ids or cls not in ('read', 'read in part', 'partly read'):
            continue
        q = dq.get(folder)
        todo = q and not q.get('skip') and 'TODO' in json.dumps(q)
        item(bool(q) and not todo, f'decode_updates/queue.json queues the DECODE edits for {folder} '
             f'(python decode_updates/queue.py add {folder}, fill the TODOs; or queue.py skip {folder} "<why>")'
             + (': TODO fields left' if todo else ''))
    # portraits and "watch it decipher" (skill steps 2 and 2a): required on every page, or a reason recorded in
    # docs/_explore_skip.json {"portrait": {slug: why}, "reveal": {slug: why}}
    try: skip = json.loads(read(HERE / '_explore_skip.json') or '{}')
    except ValueError: skip = {}
    try: pics = json.loads(read(HERE / '_portraits.json') or '{}')
    except ValueError: pics = {}
    item(any(q.get('img') for q in pics.get(slug) or []) or slug in skip.get('portrait', {}),
         f'a correspondent portrait in docs/_portraits.json (python docs/_add_portrait.py), '
         f'or the reason there is none in docs/_explore_skip.json "portrait"')
    for prob in image_problems(slug, skip=skip)[1] or [None]:
        item(prob is None, prob or 'every image names its source (data-credit) and the page shows a snip of the cipher')
    item((HERE / 'reveal' / f'{slug}.json').exists() or slug in skip.get('reveal', {}),
         f'a "watch it decipher" file docs/reveal/{slug}.json, or the reason there is none in docs/_explore_skip.json "reveal"')
    # the explore data (skill step 2a): nudges only, since many targets have no named key or no known route
    try: kw = json.loads(read(HERE / 'keys.json') or '{}')
    except ValueError: kw = {}
    try: at = json.loads(read(HERE / 'atlas.json') or '{}')
    except ValueError: at = {}
    for folder in sorted(folders):
        try: p = json.loads(read(ROOT / folder / 'profile.json') or '{}')
        except ValueError: continue
        keyed = (p.get('conditions') or {}).get('attack') in ('sibling key', 'key from archive', 'published key') or any(
            s.get('kind') in ('sibling key', 'key from source') and s.get('result') in ('worked', 'partial') for s in p.get('solution') or [])
        if keyed:
            item(any(l.get('target') == slug for l in kw.get('links', [])) or slug in kw.get('unlinked', {}),
                 f'docs/keys.json links the key that read {folder} (its profile names a sibling, archive or published key)', warn=True)
        routed = [d for d in p.get('documents') or [] if '->' in str(d.get('route', '')) and '?' not in str(d.get('route', ''))
                  and 'unknown' not in str(d.get('route', '')).lower()]
        if routed:
            item(any(l.get('slug') == slug for l in at.get('letters', [])),
                 f'docs/atlas.json maps the letters of {folder} ({len(routed)} documents have a route)', warn=True)
    if mine:
        name = key_words(mine[0]['target'])
        ledgers = ('SOLVED_CATALOGUE.md', 'SOLVED_RANKING.md', 'TARGETS.md') if st != 'stuck' else ('TARGETS.md',)
        for f in ledgers:
            item(name.lower() in read(ROOT / f).lower(), f'{f} mentions "{name}" (checked by name, confirm the row by eye)',
                 warn=(f == 'TARGETS.md'))
    print('  result:', 'complete' if ok else 'INCOMPLETE - see MISS lines')
    return ok

# ---------------------------------------------------------------------------
# the audit

def audit(brief=False):
    pages, images, _ = manifest()
    rows = readme_rows()
    dirs = target_dirs()
    listed_dirs = set().union(*(r['dirs'] for r in rows)) if rows else set()
    listed_slugs = set().union(*(r['slugs'] for r in rows)) if rows else set()
    html_slugs = {p.stem for p in HERE.glob('*.html')} - {'index', 'catalogue', 'writeups'} - TOOL_PAGES
    problems = 0

    # 1. finished in the notes, nowhere else. The shared checkout is often on a stale branch, so a page that
    #    exists on main counts as written up and is only mentioned.
    gaps, on_main = [], []
    for d, info in dirs.items():
        if not info['finished']: continue
        if d in listed_dirs or d in pages or d in html_slugs: continue
        if page_on_main(d): on_main.append(d)
        else: gaps.append((d, info['why']))
    print(f'A. Finished in NOTES.md, no README row and no site page: {len(gaps)}')
    for d, why in gaps: print(f'   {d}/   (notes say: "{why}")')
    if on_main: print(f'   (written up on main, not in this checkout: {", ".join(on_main)})')
    problems += len(gaps)

    # 2. README rows with a repo link but no write-up page
    notes_only = [r for r in rows if not r['slugs'] and r['dirs']
                  and r['section'].split(' ')[0] in ('Solved:', 'Read', 'Explained:', 'Partly', 'Found')]
    print(f'B. README results rows with no write-up page (notes only): {len(notes_only)}')
    if not brief:
        for r in notes_only: print(f'   [{r["section"][:22]}] {key_words(r["target"])}  ->  {", ".join(sorted(r["dirs"]))}/')

    # 3. catalogue.json holds open targets only: anything marked read/resolved should have been removed
    cat = [e for e in catalogue() if e.get('outcome') and not e['outcome'].startswith('attempted')]
    print(f'C. catalogue.json entries marked read or resolved, still in the catalogue (remove them): {len(cat)}')
    for e in cat: print(f'   #{e.get("id")} {str(e.get("title", ""))[:60]}  (outcome: {e.get("outcome")})')
    problems += len(cat)

    # 4. site pages / README / manifest drift
    drift = []
    for s in sorted(set(pages) - SURVEYS - listed_slugs): drift.append(f'docs/{s}.html is in the manifest but README has no row linking it')
    for s in sorted(html_slugs - set(pages) - SURVEYS): drift.append(f'docs/{s}.html exists but has no PAGES entry in _build_site.py')
    for s in sorted(listed_slugs - html_slugs): drift.append(f'README links {s}.html, which does not exist in docs/')
    for s in sorted(set(pages) - set(images) - SURVEYS): drift.append(f'{s} has no IMAGES entry (add one, or None)')
    print(f'D. Manifest / README / docs drift: {len(drift)}')
    for x in drift: print('   ' + x)
    problems += len(drift)

    # 5. partial readings still workable: unjustified, or with gaps not blocked from outside (informational)
    workable = []
    for d in dirs:
        part, probs, open_b = partial_problems(d)
        if part and (probs or open_b): workable.append((d, probs, open_b))
    print(f'E. "Read in part" targets still workable (unjustified, or gaps not blocked from outside): {len(workable)}')
    for d, probs, open_b in workable:
        why = f'{len(probs)} check(s) fail' if probs else 'open gaps: ' + ', '.join(sorted(open_b))
        print(f'   {d}/  ({why})')
        if not brief:
            for p in probs: print(f'      - {p}')
    # 6. the read bar, both ways (informational)
    ready, below = [], []
    for d in dirs:
        try: cls = (json.loads(read(ROOT / d / 'profile.json') or '{}').get('outcome') or {}).get('class')
        except ValueError: continue
        if cls not in ('read', 'read in part'): continue
        ok, why = read_bar(d)
        if cls == 'read in part' and ok: ready.append(d)
        if cls == 'read' and not ok and not any(w.startswith('no numeric') for w in why): below.append((d, why))
    print(f'F. Read bar (README Conventions): read in part but meeting the bar: {len(ready)}; classed read but below it: {len(below)}')
    for d in ready: print(f'   reclass to read?  {d}/')
    for d, why in below: print(f'   below the bar     {d}/  ({"; ".join(why)})')
    # 7. outcome method (README Conventions): every classified target sits in the README section of its method, and
    # every page whose target has a profile carries a method (the badge is derived from it by _build_site.py)
    import _methods as M
    paths = M.profile_paths()
    pages = {m.group(1): (m.group(2), m.group(3)) for m in re.finditer(
        r"dict\(slug='([a-z0-9]+)'.*?st='([a-z]+)', stt='([^']*)'", read(HERE / '_build_site.py'), re.S)}
    drift = []
    for r in readme_rows():
        want = M.section_of(r['section'])
        if not want or len(r['dirs']) != 1: continue
        folder = next(iter(r['dirs'])).split('/')[-1].lower()
        prof = M.load(paths[folder]) if folder in paths else None
        got = ((prof or {}).get('outcome') or {}).get('method')
        if prof and got != want:
            drift.append(f'{key_words(r["target"])}: README section "{want}" but profile method is {got!r}')
    for s in sorted(pages):
        if s in SURVEYS or s in FAMOUS: continue
        prof = M.load(paths[s]) if s in paths else None
        if prof and ((prof.get('outcome') or {}).get('method') not in M.METHODS):
            drift.append(f'{s}.html: profile.json has no outcome.method (run docs/_classify_outcomes.py)')
    print(f'G. Outcome method (README Conventions): README section or page without a matching profile method: {len(drift)}')
    for x in drift: print('   ' + x)
    # 8. images: every figure credited to its own source; a snip of the cipher on every page (informational)
    try: skip = json.loads(read(HERE / '_explore_skip.json') or '{}')
    except ValueError: skip = {}
    imgs = []
    for s in sorted(html_slugs - SURVEYS):
        if s not in pages: continue
        bare, probs = image_problems(s, images, skip)
        if probs: imgs.append((s, len(bare), any(p.startswith('no snip') for p in probs)))
    print(f'H. Images (writeup skill section 1): {sum(1 for x in imgs if x[1])} pages with uncredited figures '
          f'({sum(x[1] for x in imgs)} figures), {sum(1 for x in imgs if x[2])} pages with no snip of the cipher')
    if not brief:
        for s, n, nosnip in imgs:
            print(f'   {s}: ' + ', '.join(filter(None, [f'{n} uncredited' if n else '', 'no snip' if nosnip else ''])))
    return problems, gaps

# ---------------------------------------------------------------------------
# hooks

def hook_start():
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): problems, gaps = audit(brief=True)
    if not problems:
        print(json.dumps({'suppressOutput': True})); return
    text = ('Write-up audit (docs/_check_writeup.py --audit). A finished cipher is not done until it is written up: '
            'run the /writeup skill for it. Section E lists partial readings that can still be pushed toward a full '
            'reading: "read in part" is a stopping point only when every gap has an outside blocker.\n' + buf.getvalue())
    print(json.dumps({'hookSpecificOutput': {'hookEventName': 'SessionStart', 'additionalContext': text}}))

def hook_stop():
    try: inp = json.loads(sys.stdin.read() or '{}')
    except json.JSONDecodeError: inp = {}
    if inp.get('stop_hook_active'):                     # we already blocked once this stop; never loop
        print(json.dumps({'suppressOutput': True})); return
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()): _, gaps = audit(brief=True)
    # only targets this session worked in: a tool call whose input names a path in the folder (a folder merely
    # mentioned in prose, or in this script's own audit output, does not count); without a transcript, fall
    # back to uncommitted changes in the folder or notes edited in the last 6 h
    tpath = inp.get('transcript_path') or ''
    tpath = re.sub(r'^/([a-zA-Z])/', lambda m: m.group(1).upper() + ':/', tpath)     # Git Bash spelling on Windows
    transcript = read(tpath) if tpath else ''
    tool_lines = [l for l in transcript.splitlines() if '"type":"tool_use"' in l or '"type": "tool_use"' in l]
    status = git('status', '--porcelain')
    dirs = target_dirs()
    def touched(d):
        if transcript: return any(re.search(rf'"input":.*\b{re.escape(d)}[/\\]', l) for l in tool_lines)
        return f' {d}/' in status or time.time() - dirs[d]['mtime'] < 6 * 3600
    mine = [(d, why) for d, why in gaps if touched(d)]
    if mine:
        names = ', '.join(d for d, _ in mine)
        reason = (f'Write-up check: {names} reads as finished in NOTES.md ("{mine[0][1]}") but has no README results row '
                  f'and no site page. Before stopping, either run the /writeup skill for it now (every surface, then '
                  f'`python docs/_check_writeup.py {mine[0][0]}` must print "complete"), or, if it is not finished, put '
                  f'"Status: in progress" at the top of {mine[0][0]}/NOTES.md so the check stops asking.')
        print(json.dumps({'decision': 'block', 'reason': reason})); return
    # a partial reading this session worked on: push it further, or justify each gap
    part = []
    for d in dirs:
        if not (touched(d) if transcript else f' {d}/' in status): continue   # no mtime fallback here
        is_part, probs, open_b = partial_problems(d)
        if is_part and (probs or open_b): part.append((d, probs, open_b))
    if not part:
        print(json.dumps({'suppressOutput': True})); return
    lines = [f'{d}: ' + ('; '.join(probs[:6]) if probs else 'gaps still open by choice: ' + ', '.join(sorted(ob)))
             for d, probs, ob in part]
    reason = ('Partial-reading check: "read in part" is a stopping point only when every unread piece has an outside '
              'blocker (no-key-material, too-short, illegible, needs-physical-access). ' + ' | '.join(lines) +
              '. Keep working the escalation steps (siblings, clear-pages, known-keys, print, key-rebuild, retry) '
              'toward a full reading, and record each gap and step in NOTES.md "## Remaining gaps" / "## Escalation" '
              'and profile.json outcome.gaps. If the work genuinely has to stop now, put "Status: in progress" '
              'at the top of NOTES.md and say in your reply what is left.')
    # block once per distinct list: the same unchanged gaps do not re-block every stop (background agents)
    import hashlib, tempfile
    sid = re.sub(r'\W', '', inp.get('session_id') or 'nosession')
    mark = pathlib.Path(tempfile.gettempdir()) / f'cypher_partial_{sid}.txt'
    digest = hashlib.sha1(reason.encode('utf-8')).hexdigest()
    if read(mark).strip() == digest:
        print(json.dumps({'suppressOutput': True})); return
    try: mark.write_text(digest, encoding='utf-8')
    except OSError: pass
    print(json.dumps({'decision': 'block', 'reason': reason}))

if __name__ == '__main__':
    args = sys.argv[1:]
    try:
        if args[:1] == ['--hook']:
            (hook_stop if args[1:2] == ['stop'] else hook_start)()
        elif args[:1] == ['--audit']:
            problems, _ = audit()
            sys.exit(1 if problems else 0)
        elif len(args) == 1 and re.fullmatch(r'[a-z0-9]+', args[0]):
            sys.exit(0 if check_slug(args[0]) else 1)
        else:
            print(__doc__); sys.exit(2)
    except SystemExit: raise
    except Exception as e:                              # a hook must never break the session
        if args[:1] == ['--hook']: print(json.dumps({'suppressOutput': True, 'systemMessage': f'_check_writeup.py: {e!r}'}))
        else: raise
