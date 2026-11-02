"""Atlas letters from profiles.

Each profile document's free-text `route` ("Paris -> London", "Henri de Rohan, Valtellina -> Paris") is matched against
the gazetteer (docs/atlas.json "places" plus NEW_PLACES, with ALIASES); a document may instead carry
`places: {"from": <place>, "to": <place>}` with gazetteer names when the route names only people. The site build (docs/_build_site.py) calls sync() to add one atlas letter per such document
for every target whose letters are not drawn by hand, so the atlas follows the profiles without a manual step.

    python tools/atlas_places.py --gaps       # write-ups with no atlas letter, and the route ends that matched no place
    python tools/atlas_places.py              # sync docs/atlas.json now
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ATLAS = ROOT / 'docs' / 'atlas.json'

# places added with the 25 Oct 2026 backfill (lat, lon); names are what the atlas shows
NEW_PLACES = {
    'San Antonio': [29.424, -98.494], 'Austin': [30.267, -97.743], 'Chicago': [41.878, -87.630],  # augur1874
    'Gualdo Tadino': [43.230, 12.784], 'Pavia': [45.185, 9.155], 'Rimini': [44.060, 12.566], 'Pesaro': [43.910, 12.913],  # barbavara1447 (Sforza at Pesaro, 1447)
    'Cusago': [45.448, 9.035], 'Abbiategrasso': [45.398, 8.918],  # visconti1446, visconti1447 (the Duke's residences, 1446-47)
    'Salamanca': [40.965, -5.664], 'Tordesillas': [41.500, -5.000], 'Worms': [49.632, 8.359], 'Bender': [46.83, 29.48], 'Estremoz': [38.844, -7.586],  # Dudout PRs, Oct 2026
    'Monte Estoril': [38.705, -9.397], 'Oran': [35.697, -0.633], 'Bussaco': [40.3775, -8.3692], 'Sintra': [38.7876, -9.3906],  # Portuguese royal telegrams 1903-10
    'Martinique': [14.602, -61.071],  # Fort-Royal (Fort-de-France), seat of the governor and intendant of the Windward Islands
    'Mexico City': [19.433, -99.133],  # US legation, Ellis 1836-39
    'Fürstenau': [49.664, 9.003],  # Schloss Fürstenau, Michelstadt (Odenwald)
    'Potsdam': [52.391, 13.065], 'Emmerich': [51.835, 6.245], 'Lyon': [45.764, 4.836], 'Prague': [50.088, 14.42], 'Breslau': [51.11, 17.03], 'Danzig': [54.35, 18.65],
    'Moscow': [55.756, 37.617], 'Shanghai': [31.23, 121.47], 'Nagasaki': [32.75, 129.87], 'Toledo': [39.857, -4.024],
    'Bologna': [44.494, 11.343], 'Fontainebleau': [48.404, 2.701], 'Marly': [48.869, 2.094], 'Nancy': [48.692, 6.184],
    'Valencia': [39.47, -0.376], 'La Rochelle': [46.16, -1.151], 'Reims': [49.258, 4.032], 'Chenonceau': [47.325, 1.07],
    'Cambrai': [50.176, 3.235], 'Alessandria': [44.913, 8.615], 'Montauban': [44.018, 1.355], 'Beaupréau': [47.204, -0.988],
    'Alcalá de Henares': [40.482, -3.364], 'Desenzano': [45.469, 10.537], 'Chur': [46.85, 9.532], 'Iași': [47.158, 27.601],
    'Lwów': [49.842, 24.032], 'Belgrade': [44.787, 20.457], 'Perpignan': [42.699, 2.895], 'San Germano': [41.49, 13.832],
    'Badajoz': [38.879, -6.97], 'Niort': [46.323, -0.459], 'Castets': [43.882, -1.144], 'Saint-Quentin': [49.848, 3.287],
    'Saint-Aignan': [47.269, 1.376], 'Châlons': [48.957, 4.363], 'Brouage': [45.862, -1.069], 'Randan': [46.017, 3.355],
    'Hof': [50.313, 11.912], 'Monaco': [43.733, 7.417], 'Basle': [47.559, 7.588], 'Bolton Castle': [54.322, -1.954],
    'Greenwich': [51.477, 0.0], 'Nonsuch': [51.35, -0.235], 'Dorking': [51.232, -0.331], 'Jargeau': [47.863, 2.128],
    'Saumur': [47.26, -0.077], 'Angers': [47.473, -0.554], 'Strasbourg': [48.573, 7.752], 'Noirmoutier': [47.0, -2.25],
    'Sondrio': [46.17, 9.872], 'Compiègne': [49.418, 2.826], 'Agen': [44.203, 0.616], 'Landriano': [45.311, 9.26], 'Locate': [45.351, 9.226],
    'Jackson, Mississippi': [32.299, -90.185], 'Richmond, Virginia': [37.541, -77.436], 'Manassas': [38.751, -77.475],
    'Leszno': [51.8457, 16.5753], 'Sárospatak': [48.3188, 21.5683], 'Tortosa': [40.812, 0.521], 'Almazán': [41.486, -2.531],
}
# words in a route that stand for a gazetteer place
ALIASES = {
    'Hannover': 'Hanover', 'Whitehall': 'Westminster', 'St Germain': 'Saint-Germain-en-Laye', 'Pall Mall': 'London',
    'Charing Cross': 'London', 'Coire': 'Chur', 'Jászvásár': 'Iași', 'Lwow': 'Lwów', 'Lemberg': 'Lwów', 'Valtellina': 'Sondrio',
    'Agenais': 'Agen', 'Gergeau': 'Jargeau', 'Chalons': 'Châlons', 'Guyenne': 'Bordeaux', 'Basel': 'Basle',
    'Landriano': 'Landriano', 'Locate': 'Locate', 'Gdańsk': 'Danzig', 'Wrocław': 'Breslau', 'Bratislava': 'Pozsony',
    'Pressburg': 'Pozsony', 'Constantinople': 'Constantinople', 'Istanbul': 'Constantinople', 'Leghorn': 'Pisa',
}
MONTHS = {m: i for i, m in enumerate(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], 1)}


def gazetteer(at):
    names = dict(at['places'])
    for k, v in NEW_PLACES.items(): names.setdefault(k, v)
    return names


def place_in(text, names):
    """First gazetteer place named in a free-text route end, skipping titles such as 'duc de Nevers'."""
    words = {**{n: n for n in names}, **{a: p for a, p in ALIASES.items() if p in names}}
    best = None
    for w, p in words.items():
        for m in re.finditer(r'(?<![\w-])' + re.escape(w) + r'(?![\w-])', text):
            before = text[max(0, m.start() - 8):m.start()].lower()
            if re.search(r"(duc|duke|comte|count|sieur|seigneur|marquis|prince|bishop|archbishop|cardinal|dame|madame)\s+(de|d'|of)\s*$", before):
                continue
            if best is None or m.start() < best[0]: best = (m.start(), p)
    return best[1] if best else None


def ends_of(d, names):
    """(from, to) places of a document: its `places` field if set, else both ends of its free-text `route`."""
    pl = d.get('places') or {}
    if pl.get('from') and pl.get('to'): return pl['from'], pl['to']
    ends = re.split(r'\s*(?:->|→)\s*', str(d.get('route') or ''))
    if len(ends) != 2: return None, None
    a, b = place_in(ends[0], names), place_in(ends[1], names)
    return (a, b) if a and b and a != b else (None, None)


def year_of(doc):
    y = doc.get('year')
    if not isinstance(y, int): return None
    d = str(doc.get('date') or '').lower()
    m = re.search(r'(\d{1,2})\s+([a-z]{3})', d) or re.search(r'([a-z]{3})[a-z]*\.?\s+(\d{1,2})', d)
    mon = day = None
    for g in (m.groups() if m else ()):
        if g.isdigit(): day = int(g)
        elif g[:3] in MONTHS: mon = MONTHS[g[:3]]
    if not mon:
        for k, v in MONTHS.items():
            if re.search(r'\b' + k, d): mon = v; break
    return round(y + ((mon or 6) - 1) / 12 + ((day or 15) - 1) / 365, 2) if mon else y + 0.5


def profiles():
    for f in sorted((ROOT / 'targets').glob('*/profile.json')):
        try: yield f, json.loads(f.read_text(encoding='utf-8'))
        except ValueError: continue


def sync(pages=None):
    """Rewrite the profile-generated letters of docs/atlas.json. Hand-drawn letters (no "src") are kept, and a target
    with any hand-drawn letter gets no generated ones. Returns (letters added, places added)."""
    at = json.loads(ATLAS.read_text(encoding='utf-8')); names = gazetteer(at)
    if pages is None:
        pages = {p['slug']: p for p in json.loads((ROOT / 'docs' / 'pages.json').read_text(encoding='utf-8'))}
    hand = [l for l in at['letters'] if l.get('src') != 'profile']
    drawn = {l['slug'] for l in hand}; gen = []; used = set()
    for f, p in profiles():
        slug = f.parent.name
        if slug not in pages or slug in drawn: continue
        for d in p.get('documents') or []:
            a, b = ends_of(d, names); y = year_of(d)
            if a in names and b in names and y:
                gen.append({'slug': slug, 'doc': d.get('id', ''), 'year': y, 'date': d.get('date', ''), 'from': a, 'to': b,
                            'st': pages[slug]['st'], 'label': pages[slug]['label'], 'src': 'profile'})
                used |= {a, b}
    added = sorted(k for k in used if k not in at['places'])
    for k in added: at['places'][k] = names[k]
    at['letters'] = hand + sorted(gen, key=lambda l: (l['year'], l['slug']))
    ATLAS.write_text(json.dumps(at, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return len(gen), len(added)


def gaps():
    at = json.loads(ATLAS.read_text(encoding='utf-8')); names = gazetteer(at)
    pages = {p['slug'] for p in json.loads((ROOT / 'docs' / 'pages.json').read_text(encoding='utf-8'))}
    drawn = {l['slug'] for l in at['letters']}
    miss = sorted(pages - drawn)
    print(f'{len(miss)} write-ups with no atlas letter:'); print('  ' + ' '.join(miss))
    for f, p in profiles():
        for d in p.get('documents') or []:
            r = str(d.get('route') or '')
            if f.parent.name in miss and r and not d.get('places'):
                ends = re.split(r'\s*(?:->|→)\s*', r)
                bad = [e for e in ends if not place_in(e, names)] if len(ends) == 2 else [r]
                if bad: sys.stdout.write(f'  {f.parent.name} {d.get("id")}: no place for {bad}\n')


if __name__ == '__main__':
    if '--gaps' in sys.argv: gaps()
    else: print('atlas letters from profiles: %d (new places %d)' % sync())
