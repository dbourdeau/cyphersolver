"""Outcome method: George Lasry's categories (email 21 Sept 2026), proposed from the fields every profile already has.

  python docs/_classify_outcomes.py              table of proposals and flags for every profile without outcome.method
  python docs/_classify_outcomes.py --all        include profiles that already carry a method (proposal vs recorded)
  python docs/_classify_outcomes.py --csv FILE   write the table as CSV (default papers/lasry/classification_review.csv)
  python docs/_classify_outcomes.py --counts     tally of recorded methods
  python docs/_classify_outcomes.py --apply F.jsonl [...]
                                                 write reviewed decisions ({folder, method, method_basis,
                                                 contribution}) into outcome, leaving the rest of the file as it is

Read-only apart from the CSV. A proposal is a starting point: every flagged row needs NOTES.md read before a
method is written into the profile, and so does any row the rules could not settle. The method itself is
defined in profile.schema.json (outcome.method).
"""
import sys, csv, json, pathlib, collections

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import _check_writeup as cw

from _methods import CT, EXT_PT, ADJ_PT, EXT_KEY, KNOWN, DECIPH, NOT, NA, METHODS

ADJ_LOC = {'interlinear', 'margin', 'separate paragraph', 'separate folio'}
EXT_LOC = {'printed edition', 'separate collection', 'unrelated source'}

def profiles():
    """(folder, profile) for every non-famous profile, nested sweep folders included."""
    for p in sorted(ROOT.glob('*/profile.json')) + sorted(ROOT.glob('*/*/profile.json')):
        folder = p.parent.relative_to(ROOT).as_posix()
        if folder.split('/')[-1] in cw.FAMOUS or folder.split('/')[0] in cw.FAMOUS: continue
        try: yield folder, json.loads(p.read_text(encoding='utf-8'))
        except ValueError: print(f'  {folder}: profile.json does not parse')

def propose(prof):
    """(method, flags): the rule-based proposal and the reasons it needs a human look."""
    out = prof.get('outcome') or {}
    cond = prof.get('conditions') or {}
    cls, attack = out.get('class'), cond.get('attack')
    inputs = set(cond.get('inputs') or [])
    prior = cond.get('prior_solution') or {}
    def loc(d):
        v = (d.get('plaintext') or {}).get('location') or [] if isinstance(d.get('plaintext'), dict) else []
        return [v] if isinstance(v, str) else v
    locs = {l for d in prof.get('documents') or [] if isinstance(d, dict) for l in loc(d) if isinstance(l, str)}
    steps = [s for s in prof.get('solution') or [] if isinstance(s, dict)]
    keystep = any(s.get('kind') in ('sibling key', 'key from source') and s.get('result') in ('worked', 'partial') for s in steps)
    breakstep = any(s.get('kind') in ('solver', 'crib', 'statistics') and s.get('result') in ('worked', 'partial') for s in steps)
    flags = []
    if cls in ('not a cipher', 'offline only'): return NA, flags
    if cls == 'not read': return NOT, flags
    adj = bool(locs & ADJ_LOC) or 'cleartext context' in inputs
    ext = bool(locs & EXT_LOC) or 'published reading' in inputs
    if attack == 'ciphertext-only':
        if locs - {'none', 'unknown'}: flags.append(f'plaintext recorded ({", ".join(sorted(locs - {"none", "unknown"}))})')
        if keystep: flags.append('a sibling-key / key-from-source step worked')
        if prior.get('used') is True: flags.append('prior solution used')
        m = CT
    elif attack in ('crib', 'known plaintext'):
        if adj and ext: flags.append('plaintext both adjacent and external: which one gave the key?'); m = ADJ_PT if locs & ADJ_LOC else EXT_PT
        elif adj: m = ADJ_PT
        elif ext: m = EXT_PT
        else: flags.append('crib source not recorded'); m = ADJ_PT
        if keystep: flags.append('a sibling-key / key-from-source step worked: key may have been in hand')
        if prior.get('exists') in ('in archive', 'in print', 'online') and prior.get('found') == 'before attempt':
            flags.append(f'full prior solution {prior.get("exists")}, found before attempt')
    elif attack == 'sibling key':
        m = EXT_KEY
    elif attack in ('published key', 'key from archive'):
        m = KNOWN
        if 'sibling key' in inputs or any(s.get('kind') == 'sibling key' and s.get('result') == 'worked' for s in steps):
            flags.append('sibling key in inputs/steps: was the key tied to this document, or matched?')
        if breakstep: flags.append('solver/crib steps worked: key extended or rebuilt?')
    elif attack == 'archive decipherment':
        m = DECIPH
        if breakstep or out.get('key') in ('recovered', 'partial'): flags.append('key rebuilt from the decipherment? then adjacent/external plaintext')
    elif attack == 'none':
        m = DECIPH if cls == 'already solved' else NOT
        flags.append(f'attack none, class {cls}: what did the work add?')
    else:
        m = NOT if cls not in ('read', 'read in part') else KNOWN
        flags.append(f'attack {attack!r}')
    if cls == 'already solved' and m in (CT, ADJ_PT, EXT_PT):
        flags.append('already solved elsewhere: independent re-solution?')
    return m, flags

NEWKEYS = ('method', 'method_basis', 'contribution')

def apply(path):
    """Insert or replace outcome.method / method_basis / contribution by text edit, so an unchanged profile keeps
    its layout (half the profiles do not round-trip through json.dumps)."""
    import re
    n = 0
    for line in pathlib.Path(path).read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        d = json.loads(line)
        if d['method'] not in METHODS: print(f'  {d["folder"]}: bad method {d["method"]!r}'); continue
        f = ROOT / d['folder'] / 'profile.json'
        raw = f.read_bytes().decode('utf-8')
        nl = '\r\n' if '\r\n' in raw else '\n'
        text = raw.replace('\r\n', '\n')
        prof = json.loads(text)
        for k in NEWKEYS:                                   # drop an earlier value, one line each
            if k in prof.get('outcome', {}):
                text = re.sub(r'\n[ \t]*"' + k + r'": (?:"(?:[^"\\]|\\.)*"|\[[^\]]*\]),?(?=\n)', '', text, count=1)
        text = re.sub(r',(\s*\n[ \t]*\})', r'\1', text)     # a removed last key may leave a trailing comma
        m = re.search(r'\n[ \t]*"outcome": \{\n([ \t]*)"', text)
        if not m: print(f'  {d["folder"]}: no outcome block'); continue
        ins = ''.join(f'{m.group(1)}"{k}": {json.dumps(d[k], ensure_ascii=False)},\n' for k in NEWKEYS)
        text = text[:m.start(1)] + ins + text[m.start(1):]
        new = json.loads(text)
        strip = lambda o: {k: v for k, v in o.items() if k not in NEWKEYS}
        assert strip(new['outcome']) == strip(prof['outcome']), d['folder']
        assert {k: v for k, v in new.items() if k != 'outcome'} == {k: v for k, v in prof.items() if k != 'outcome'}, d['folder']
        assert all(new['outcome'][k] == d[k] for k in NEWKEYS), d['folder']
        f.write_bytes(text.replace('\n', nl).encode('utf-8')); n += 1
    print(f'{n} profiles updated from {path}')

def table(all_=False):
    rows = []
    for folder, prof in profiles():
        out = prof.get('outcome') or {}
        m, flags = propose(prof)
        rec = out.get('method')
        if rec and not all_: continue
        cond = prof.get('conditions') or {}
        rows.append(dict(folder=folder, proposed=m, recorded=rec or '', flags=' | '.join(flags),
                         cls=out.get('class'), attack=cond.get('attack'),
                         prior=f'{(cond.get("prior_solution") or {}).get("exists")}/{(cond.get("prior_solution") or {}).get("found")}',
                         title=prof.get('title', '')[:90]))
    return rows

if __name__ == '__main__':
    a = sys.argv[1:]
    if '--apply' in a:
        for f in a[a.index('--apply') + 1:]: apply(f)
        sys.exit(0)
    if '--counts' in a:
        c = collections.Counter((p.get('outcome') or {}).get('method', '(none)') for _, p in profiles())
        for k in METHODS + ['(none)']: print(f'{c.get(k, 0):4d}  {k}')
        sys.exit(0)
    rows = table('--all' in a)
    path = ROOT / (a[a.index('--csv') + 1] if '--csv' in a else 'papers/lasry/classification_review.csv')
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ['folder']); w.writeheader(); w.writerows(rows)
    c = collections.Counter(r['proposed'] for r in rows)
    print(f'{len(rows)} profiles, {sum(1 for r in rows if r["flags"])} flagged; written to {path.relative_to(ROOT)}')
    for k in METHODS: print(f'{c.get(k, 0):4d}  {k}')
