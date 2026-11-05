"""The catalogue vetting gate: catalogue.json holds vetted leads only; everything else waits in research/leads.json.

  python docs/_check_catalogue.py                 check catalogue.json: every entry from id GATE_ID on must carry a
                                                  complete "vetting" block with verdict "open"; prints result: valid
  python docs/_check_catalogue.py --lead 1234     what lead 1234 still needs before it can be promoted
  python docs/_check_catalogue.py --promote 1234 [1235 ...]
                                                  move leads that pass the gate from research/leads.json into
                                                  catalogue.json (same id); a lead that fails is left where it is
  python docs/_check_catalogue.py --close 1234 duplicate "same letter as catalogue 503"
                                                  set a lead's vetting verdict to something other than open (read,
                                                  duplicate, key_lookup, not_cipher) without promoting it
  python docs/_check_catalogue.py --audit         counts: gate failures, legacy entries never vetted, leads by state

The bar (README Conventions, "Catalogue vetting bar") is what CATALOGUE.md records going wrong with unvetted entries:
letters already read, editors' printed decipherments behind "cipher undeciphered", letters a held key reads, and
duplicates. A lead becomes a catalogue entry only when its "vetting" block shows:

  "vetting": {
    "date": "2026-10-28",                      # when the checks were done
    "by": "who or which session did them",
    "seen": {"kind": "scan" | "facsimile" | "transcription" | "not online",
             "where": "URL or citation of what was looked at",
             "extent": "how much cipher: folios, lines, groups",
             "cipher": "what is on the leaf: the system seen, and that no decipherment is written on or with it"},
    "prior_art": {"decode": "...", "tomokiyo": "...", "lasry": "...", "edition": "...", "literature": "..."},
    "key_check": "keys held here or in print that were tried or ruled out, and why none reads it",
    "key_in_volume": "optional: the key filed in the same volume or unit, and whether it was tested",
    "key_held": "optional: a key held here, on DECODE or in print, and whether it was tested. Neither key field blocks
                 promotion: a lead with no known decipherment is open whether or not a key exists (rule of 3 Nov 2026);
                 key_lookup is only for a text that a key has already been shown to read and that reading is on record",
    "duplicates": "what was searched (known.py terms, DECODE ids, correspondents and date) and the result",
    "verdict": "open"                          # or read / partly_read / duplicate / key_lookup / not_cipher
  }

"not online" is accepted only for an entry with access "archive" (needs a scan from the archive); "cipher" must
then quote the archive's description of the cipher. Each prior_art value says what was searched and found; write
"not on DECODE" or "no edition known" rather than leaving one out. Entries below GATE_ID came in before the gate:
they are listed by --audit, not failed.
"""
import datetime, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
CAT = ROOT / 'catalogue.json'
LEADS = ROOT / 'research' / 'leads.json'
GATE_ID = 861                     # entries 861 onwards came from the Oct 2026 sweeps and were moved back to leads
SEEN_KINDS = ('scan', 'facsimile', 'transcription', 'not online')
PRIOR_ART = ('decode', 'tomokiyo', 'lasry', 'edition', 'literature')
VERDICTS = ('open', 'read', 'partly_read', 'duplicate', 'key_lookup', 'not_cipher')
MIN_TEXT = 12                     # a check result shorter than this ("ok", "none", "checked") says nothing


def load(path, key):
    d = json.loads(path.read_text(encoding='utf-8'))
    return d, d[key]


def save(path, d):
    path.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def text_ok(v):
    return isinstance(v, str) and len(v.strip()) >= MIN_TEXT


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()


def vetting_problems(e):
    """What the entry's vetting block is missing; empty when it passes the gate."""
    v = e.get('vetting')
    if not isinstance(v, dict):
        return ['no "vetting" block']
    out = []
    try:
        datetime.date.fromisoformat(str(v.get('date')))
    except ValueError:
        out.append('vetting.date is not an ISO date')
    if not (isinstance(v.get('by'), str) and v['by'].strip()):
        out.append('vetting.by is empty')
    s = v.get('seen')
    if not isinstance(s, dict):
        out.append('vetting.seen missing (what was looked at, where, how much cipher)')
    else:
        if s.get('kind') not in SEEN_KINDS:
            out.append(f'vetting.seen.kind must be one of {", ".join(SEEN_KINDS)}')
        elif s['kind'] == 'not online' and e.get('access') != 'archive':
            out.append('vetting.seen.kind "not online" is allowed only with access "archive"')
        for k in ('where', 'extent', 'cipher'):
            if not text_ok(s.get(k)):
                out.append(f'vetting.seen.{k} missing or too short')
    pa = v.get('prior_art')
    if not isinstance(pa, dict):
        out.append(f'vetting.prior_art missing ({", ".join(PRIOR_ART)})')
    else:
        for k in PRIOR_ART:
            if not text_ok(pa.get(k)):
                out.append(f'vetting.prior_art.{k} missing or too short')
    for k in ('key_check', 'duplicates'):
        if not text_ok(v.get(k)):
            out.append(f'vetting.{k} missing or too short')
    if 'key_in_volume' in v and not text_ok(v['key_in_volume']):
        out.append('vetting.key_in_volume too short: say where the key is and whether it was tested')
    if 'key_held' in v and not text_ok(v['key_held']):
        out.append('vetting.key_held too short: say which key and whether it was tested')
    if v.get('verdict') not in VERDICTS:
        out.append(f'vetting.verdict must be one of {", ".join(VERDICTS)}')
    elif v['verdict'] != 'open':
        out.append(f'vetting.verdict is "{v["verdict"]}": only "open" leads enter the catalogue')
    return out


def collisions(e, entries):
    """Mechanical duplicate check against the catalogue: shared DECODE ids or the same shelfmark."""
    out = []
    ids = set(e.get('decode_ids') or [])
    sh = norm(e.get('shelfmark'))
    for o in entries:
        if o['id'] == e['id']:
            continue
        if ids & set(o.get('decode_ids') or []):
            out.append(f'shares DECODE ids {sorted(ids & set(o["decode_ids"]))} with catalogue {o["id"]}')
        elif sh and sh == norm(o.get('shelfmark')):
            out.append(f'same shelfmark as catalogue {o["id"]}')
    return out


def check():
    _, entries = load(CAT, 'entries')
    _, leads = load(LEADS, 'leads')
    bad = 0
    ids = [e['id'] for e in entries]
    for d in sorted({i for i in ids if ids.count(i) > 1}):
        print(f'catalogue id {d} appears more than once'); bad += 1
    for d in sorted(set(ids) & {l['id'] for l in leads}):
        print(f'id {d} is both a catalogue entry and a lead'); bad += 1
    import _repositories as R       # each entry's holding archive: an id in repositories.json (docs/_repositories.py --write fills it)
    for e in entries:
        if e.get('repository') and e['repository'] not in R.BY_ID:
            print(f'#{e["id"]} repository "{e["repository"]}" is not in repositories.json'); bad += 1
        if e['id'] < GATE_ID:
            continue
        p = vetting_problems(e)
        if p:
            bad += 1
            print(f'#{e["id"]} {e.get("title", "")[:60]}')
            for x in p: print(f'   {x}')
    print(f'{len(entries)} catalogue entries, {len(leads)} leads; {bad} problem(s)')
    print('result: valid' if not bad else 'result: invalid (move unvetted entries to research/leads.json)')
    return bad


def lead(n):
    _, entries = load(CAT, 'entries')
    _, leads = load(LEADS, 'leads')
    e = next((l for l in leads if l['id'] == n), None)
    if not e:
        print(f'no lead {n} in research/leads.json'); return 1
    p = vetting_problems(e) + collisions(e, entries)
    print(f'#{n} {e.get("title", "")}')
    for x in p: print(f'   {x}')
    print('ready to promote' if not p else f'{len(p)} item(s) before it can be promoted')
    return len(p)


def promote(nums):
    cat, entries = load(CAT, 'entries')
    ld, leads = load(LEADS, 'leads')
    moved = []
    for n in nums:
        e = next((l for l in leads if l['id'] == n), None)
        if not e:
            print(f'#{n}: not a lead'); continue
        p = vetting_problems(e) + collisions(e, entries)
        if p:
            print(f'#{n}: not promoted'); [print(f'   {x}') for x in p]; continue
        leads.remove(e)
        import _repositories as R
        e.setdefault('repository', R.guess(e) or 'unidentified')
        e['scored'] = 'vetted'
        if e['vetting']['seen']['kind'] != 'not online':
            e['seen'] = 'image'
        entries.append(e)
        moved.append(n)
        print(f'#{n}: promoted')
    if moved:
        entries.sort(key=lambda x: x['id'])
        save(CAT, cat); save(LEADS, ld)
    return 0 if len(moved) == len(nums) else 1


def close(n, verdict, why):
    ld, leads = load(LEADS, 'leads')
    e = next((l for l in leads if l['id'] == n), None)
    if not e or verdict not in VERDICTS or verdict == 'open':
        print('usage: --close <lead id> <read|partly_read|duplicate|key_lookup|not_cipher> "<reason>"'); return 1
    v = e.setdefault('vetting', {})
    v.update(verdict=verdict, closed=why, date=v.get('date') or datetime.date.today().isoformat())
    save(LEADS, ld)
    print(f'#{n}: {verdict}')
    return 0


def summary():
    """(gate failures, one-line summary) for the SessionStart audit in _check_writeup.py."""
    _, entries = load(CAT, 'entries')
    _, leads = load(LEADS, 'leads')
    fail = [e for e in entries if e['id'] >= GATE_ID and vetting_problems(e)]
    legacy = sum(1 for e in entries if e['id'] < GATE_ID and 'vetting' not in e)
    closed = sum(1 for l in leads if (l.get('vetting') or {}).get('verdict') not in (None, 'open'))
    ready = sum(1 for l in leads if not vetting_problems(l))
    line = (f'{len(fail)} catalogue entries fail the vetting gate; {legacy} legacy entries (before #{GATE_ID}) never '
            f'vetted; research/leads.json: {len(leads)} leads, {ready} ready to promote, {closed} closed')
    return fail, line


def audit():
    fail, line = summary()
    print(line)
    for e in fail: print(f'   #{e["id"]} {e.get("title", "")[:60]}  (move to research/leads.json)')
    return len(fail)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    if a[:1] == ['--lead'] and len(a) == 2: sys.exit(1 if lead(int(a[1])) else 0)
    if a[:1] == ['--promote'] and len(a) >= 2: sys.exit(promote([int(x) for x in a[1:]]))
    if a[:1] == ['--close'] and len(a) == 4: sys.exit(close(int(a[1]), a[2], a[3]))
    if a[:1] == ['--audit']: sys.exit(1 if audit() else 0)
    if not a: sys.exit(1 if check() else 0)
    print(__doc__); sys.exit(2)
