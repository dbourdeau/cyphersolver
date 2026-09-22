"""Cipher profiles: the machine-readable challenge and solution record behind the LLM-performance paper.

Each target folder carries profile.json, shaped by profile.schema.json at the repository root. This script
checks those files, measures ciphertext counts so they are not typed from memory, and lists targets that
still need one. It reads the working tree; only --measure with --write edits anything.

  python docs/_check_profile.py <folder>                  validate one profile; list its "unknown" fields
  python docs/_check_profile.py --audit                   every finished or README-listed target: missing,
                                                          invalid, or incomplete profiles
  python docs/_check_profile.py --measure <file> [--digits] [--width N] [--letters] [--drop-first] [--skip REGEX]
                                                          tokens, distinct, IC, separation of a ciphertext
                                                          file. --digits: only tokens with a digit (figures
                                                          mixed with clear words); --width N: split contiguous
                                                          figure runs into N-digit groups; --letters: count
                                                          single letters; --drop-first: drop a label column.
                                                          Lines starting # or == are always skipped.

Exit code 1 from <folder> or --audit when something is missing or invalid.
"""
import sys, re, json, pathlib, collections

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import _check_writeup as cw                              # target_dirs(), readme_rows(): same notion of "finished"

SCHEMA = json.loads((ROOT / 'profile.schema.json').read_text(encoding='utf-8'))
UNKNOWN = 'unknown'

# ---------------------------------------------------------------------------
# a small JSON Schema subset (type, enum, const, required, properties, items, additionalProperties,
# minItems, minimum, maximum). "unknown" is accepted for any leaf and reported as a gap.

TYPES = {'object': dict, 'array': list, 'string': str, 'integer': int, 'number': (int, float), 'boolean': bool}

def validate(v, s, path, errors, gaps):
    if v == UNKNOWN and path:
        gaps.append(path or '(root)'); return
    t = s.get('type')
    if t:
        ok = isinstance(v, TYPES[t]) and not (t in ('integer', 'number') and isinstance(v, bool))
        if not ok:
            errors.append(f'{path}: expected {t}, got {type(v).__name__} {json.dumps(v, ensure_ascii=False)[:40]}'); return
    if 'const' in s and v != s['const']: errors.append(f'{path}: must be {s["const"]!r}')
    if 'enum' in s and v not in s['enum']: errors.append(f'{path}: {v!r} not one of {s["enum"]}')
    if 'minimum' in s and isinstance(v, (int, float)) and v < s['minimum']: errors.append(f'{path}: below {s["minimum"]}')
    if 'maximum' in s and isinstance(v, (int, float)) and v > s['maximum']: errors.append(f'{path}: above {s["maximum"]}')
    if t == 'object':
        props = s.get('properties', {})
        for k in s.get('required', []):
            if k not in v: errors.append(f'{path}.{k}: required (write "unknown" if it cannot be established)'.lstrip('.'))
        for k, x in v.items():
            if k in props: validate(x, props[k], f'{path}.{k}'.lstrip('.'), errors, gaps)
            elif isinstance(s.get('additionalProperties'), dict): validate(x, s['additionalProperties'], f'{path}.{k}'.lstrip('.'), errors, gaps)
            elif props: errors.append(f'{path}.{k}: not in the schema'.lstrip('.'))
    if t == 'array':
        if len(v) < s.get('minItems', 0): errors.append(f'{path}: needs at least {s["minItems"]} item(s)')
        for i, x in enumerate(v): validate(x, s.get('items', {}), f'{path}[{i}]', errors, gaps)

# ---------------------------------------------------------------------------
# measuring

def measure(path, digits=False, skip=None, width=0, letters=False, drop_first=False):
    text = pathlib.Path(path).read_text(encoding='utf-8', errors='replace')
    lines = [l for l in text.splitlines() if l.strip() and not l.lstrip().startswith(('#', '=='))]
    if skip: lines = [l for l in lines if not re.search(skip, l)]
    if drop_first: lines = [l.split(None, 1)[1] if len(l.split(None, 1)) > 1 else '' for l in lines]
    body = '\n'.join(lines)
    toks = body.split()
    if digits or width: toks = [t for t in toks if re.search(r'\d', t)]
    toks = [t.strip('.,;:') or t for t in toks]
    if width:                                            # contiguous figure runs -> fixed-width groups
        toks = [r[i:i + width] for t in toks for r in re.findall(r'\d+', t) for i in range(0, len(r), width)]
    if letters: toks = [ch for t in toks for ch in t if ch.isalpha()]
    c = collections.Counter(toks)
    n = len(toks)
    ic = sum(k * (k - 1) for k in c.values()) / (n * (n - 1)) if n > 1 else 0.0
    runs = re.findall(r'\d+(?:[.,]\d+)+', body)
    sep = 'dots' if any('.' in r for r in runs) else 'commas' if runs else 'spaces'
    if re.search(r'\d{5,}', body) and not digits: sep = 'contiguous'
    return dict(tokens=n, distinct=len(c), ic=round(ic, 4), separation=sep,
                top=', '.join(f'{k} x{v}' for k, v in c.most_common(8)))

# ---------------------------------------------------------------------------

def check(folder, quiet=False):
    p = ROOT / folder / 'profile.json'
    if not p.exists():
        if not quiet: print(f'{folder}: no profile.json (run the /profile skill)')
        return 'missing', [], []
    try: prof = json.loads(p.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        if not quiet: print(f'{folder}: profile.json is not valid JSON: {e}')
        return 'invalid', [str(e)], []
    errors, gaps = [], []
    validate(prof, SCHEMA, '', errors, gaps)
    if prof.get('target') not in (folder, UNKNOWN): errors.append(f'target: {prof.get("target")!r} is not the folder name {folder!r}')
    for i, d in enumerate(prof.get('documents', [])):          # a measured count must still match its file
        ln = d.get('length', {}) if isinstance(d, dict) else {}
        if ln.get('measured') is True:
            if not ln.get('file'): errors.append(f'documents[{i}].length: measured is true but no file is named')
            elif ln['file'].startswith('withheld:'): pass    # file kept out of the public repo; count stands as measured
            elif not (ROOT / folder / ln['file']).exists(): errors.append(f'documents[{i}].length.file: {ln["file"]} not found')
    if not quiet:
        print(f'{folder}: profile.json')
        for e in errors: print(f'  [MISS] {e}')
        for g in gaps: print(f'  [gap ] {g} = "unknown"')
        print('  result:', 'INVALID' if errors else f'valid, {len(gaps)} unknown field(s)')
    return ('invalid' if errors else 'valid'), errors, gaps

def audit():
    dirs = cw.target_dirs()
    rows = cw.readme_rows()
    listed = set().union(*(r['dirs'] for r in rows)) if rows else set()
    want = sorted(({d for d, i in dirs.items() if i['finished']} | {d for d in listed if (ROOT / d).is_dir()}) - cw.NOT_TARGETS)
    have = sorted(p.parent.name for p in ROOT.glob('*/profile.json'))
    res = {d: check(d, quiet=True) for d in sorted(set(want) | set(have))}
    missing = [d for d in want if res[d][0] == 'missing']
    invalid = [d for d, r in res.items() if r[0] == 'invalid']
    valid = [d for d, r in res.items() if r[0] == 'valid']
    print(f'Profiles: {len(valid)} valid, {len(invalid)} invalid, {len(missing)} missing, of {len(want)} targets that need one')
    for d in invalid: print(f'  INVALID {d}: {res[d][1][0]}' + (f' (+{len(res[d][1]) - 1} more)' if len(res[d][1]) > 1 else ''))
    for d in valid:
        if res[d][2]: print(f'  gaps    {d}: {len(res[d][2])} unknown')
    if missing: print('  missing: ' + ', '.join(missing))
    return len(missing) + len(invalid)

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--audit']:
        sys.exit(1 if audit() else 0)
    elif a[:1] == ['--measure'] and len(a) >= 2:
        skip = a[a.index('--skip') + 1] if '--skip' in a else None
        width = int(a[a.index('--width') + 1]) if '--width' in a else 0
        print(json.dumps(measure(a[1], digits='--digits' in a, skip=skip, width=width, letters='--letters' in a,
                                 drop_first='--drop-first' in a), ensure_ascii=False, indent=1))
    elif len(a) == 1 and (ROOT / a[0]).is_dir():
        sys.exit(0 if check(a[0])[0] == 'valid' else 1)
    else:
        print(__doc__); sys.exit(2)
