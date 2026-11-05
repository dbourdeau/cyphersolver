"""The holding archive of each catalogue entry, from ../repositories.json.

    python docs/_repositories.py            report: entries per archive, entries left unassigned, assignments that would change
    python docs/_repositories.py --write    write each catalogue.json entry's "repository" id (an entry with
                                            "repository_fixed": true is left as it is)

The catalogue's "source" field says how an entry was found (which sweep); this says where the document is. An entry
is matched on its shelfmark first, then on its verify, folio_note and access_note lines, its To-the-Archive request and
its links: the first text with any match decides, a "match" pattern beats a "fallback" one, and among matches the
institution named earliest in the text wins ("Calendar of the Clarendon State Papers" is the Bodleian, not TNA).
"""
import json, pathlib, re, sys, collections

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
REG = json.loads((ROOT / 'repositories.json').read_text(encoding='utf-8'))['repositories']
BY_ID = {r['id']: r for r in REG}
_PATS = [(r['id'], re.compile(p), False) for r in REG for p in r.get('match', [])] + \
        [(r['id'], re.compile(p), True) for r in REG for p in r.get('fallback', [])]


def _requests():
    f = ROOT / 'archive_requests.json'
    rq = json.loads(f.read_text(encoding='utf-8')).get('requests', []) if f.is_file() else []
    return {r['catalogue']: f'{r["archive"]} | {r.get("shelfmark") or ""}' for r in rq if r.get('catalogue')}


REQ = _requests()


def _best(text, fallback):
    hits = [(m.start(), -len(m.group(0)), rid) for rid, p, fb in _PATS if fb == fallback for m in [p.search(text)] if m]
    return min(hits)[2] if hits else None


def guess(e):
    """The repository id the patterns give for entry e, or None."""
    texts = [e.get('shelfmark') or '', e.get('verify') or '', e.get('folio_note') or '', e.get('access_note') or '',
             REQ.get(e['id'], ''), ' '.join(f'{l.get("label", "")} {l.get("href", "")}' for l in e.get('links') or [])]
    for fallback in (False, True):
        for t in texts:
            r = t and _best(t, fallback)
            if r: return r
    return None


def of(e):
    """The entry's repository id: the stored one, else the patterns' guess, else 'unidentified'."""
    return e.get('repository') or guess(e) or 'unidentified'


def info(rid):
    return BY_ID.get(rid) or {'id': 'unidentified', 'name': 'Holding archive not yet identified', 'city': '', 'country': '', 'kind': 'unknown'}


def main(write=False):
    path = ROOT / 'catalogue.json'
    d = json.loads(path.read_text(encoding='utf-8'))
    E = d['entries']
    changed, missing = [], []
    for e in E:
        if e.get('repository_fixed'): continue
        g = guess(e)
        if not g: missing.append(e); continue
        if e.get('repository') != g:
            changed.append((e['id'], e.get('repository'), g))
            if write: e['repository'] = g
    n = collections.Counter(of(e) for e in E)
    bad = sorted({e['repository'] for e in E if e.get('repository') and e['repository'] not in BY_ID})
    print(f'{len(E)} entries, {len(n)} repositories, {len(missing)} unassigned, {len(changed)} assignments {"written" if write else "would change"}')
    for rid, k in n.most_common(): print(f'  {k:4} {rid:14} {info(rid)["name"]}')
    for e in missing: print(f'  unassigned no. {e["id"]}: {e["shelfmark"][:110]}')
    if bad: print('unknown repository ids:', ', '.join(bad))
    if write and changed:
        path.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
