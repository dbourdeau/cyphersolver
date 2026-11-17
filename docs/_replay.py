"""Key replay: apply a target's published key to its published transcription and compare with its published reading.

    python docs/_replay.py <folder>            # writes targets/<folder>/replay.tsv and replay.json, prints the summary
    python docs/_replay.py <folder> --check    # exit 1 when a reading differs from the key output without a mark

The question it answers is the one a reviewer asks first: does the posted key reproduce the posted plaintext, and
where it does not, is every difference marked? Nothing here judges whether a reading is right.

Each target supplies `targets/<folder>/replay.py` with:

    DIVIDED    True when the cipher marks word division (words are then counted over cipher words);
               False when it runs on (words are counted over the words of the reading).
    POLYPHONY  {unit: [other values the notes declare for it]}; may be empty.
    SOURCES    {'key': ..., 'transcription': ..., 'reading': ...} file names, for the report.
    mechanical() -> [(label, [word, ...])], word = [(unit, value), ...]
               value is the key's value for the unit, None when the key has none (an open code).
               unit None marks clear text in the document, kept only to anchor the alignment.
    reading()  -> {label: text}. In the text `[abc]` is a marked emendation, `[..]`, `[…]` and `#` an unread hole.

Comparison is on letters only: case, accents and punctuation are dropped, u/v and i/j are folded (the signs do not
distinguish them). i/y is counted apart. Every other difference counts.

Classes, per word and per unit:
    exact      the reading has the key's output
    i/y        differs only by i written y or y written i
    polyphony  differs only by same-place substitutions inside POLYPHONY (and i/y)
    marked     differs, and every differing letter of the reading is inside [ ]
    silent     differs somewhere outside [ ]: an emendation the reading does not mark
    dropped    cipher with a key value that the reading leaves out
    unread     the reading has a hole there
    no-value   the key has no value for the unit (open code); not counted in the rates
    added      a word of the reading that no sign carries (listed, not counted in the rates)
"""
import os, sys, re, json, unicodedata, importlib.util, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOLE = '#'
CLASSES = ('exact', 'i/y', 'polyphony', 'marked', 'silent', 'dropped', 'unread', 'no-value', 'added')


def fold(s):
    out = []
    for c in unicodedata.normalize('NFD', s.lower()):
        if c == HOLE:
            out.append(c)
        elif c.isascii() and c.isalpha():
            out.append({'v': 'u', 'j': 'i'}.get(c, c))
    return ''.join(out)


def parse_reading(text):
    """-> (folded string, marked flag per char, word index per char, raw words)."""
    text = re.sub(r'\[\s*(\.\.+|…)\s*\]', ' %s ' % HOLE, text)
    s, marked, widx, words = [], [], [], []
    depth = 0
    for raw in text.split():
        letters = []
        for c in raw:
            if c == '[':
                depth += 1
            elif c == ']':
                depth = max(0, depth - 1)
            else:
                for ch in fold(c):
                    letters.append((ch, depth > 0))
        if not letters:
            continue
        for ch, m in letters:
            s.append(ch); marked.append(m); widx.append(len(words))
        words.append(raw)
    return ''.join(s), marked, widx, words


def build_mech(words):
    """-> (string, unit index per char, units). A unit with no key value is one HOLE char."""
    s, cu, units = [], [], []
    for wi, w in enumerate(words):
        for unit, value in w:
            v = HOLE if (unit is not None and value is None) else fold(value)
            units.append({'unit': unit, 'value': value, 'word': wi, 'a': len(s), 'b': len(s) + len(v)})
            cu.extend([len(units) - 1] * len(v)); s.extend(v)
    return ''.join(s), cu, units


def align(mech, read, dcost):
    """Edit-distance alignment -> [(mi|None, ri|None)]. A hole takes any letter cheaply; i/y is a cheap swap;
    dcost[i] is the cost of leaving mech[i] out (clear text is dearer, so it anchors)."""
    n, m = len(mech), len(read)

    def sub(x, y):
        if x == y:
            return 0.0
        if HOLE in (x, y):
            return 0.6
        if {x, y} == {'i', 'y'}:
            return 0.3
        return 1.0
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        D[i][0] = D[i - 1][0] + dcost[i - 1]
    for j in range(1, m + 1):
        D[0][j] = float(j)
    for i in range(1, n + 1):
        Di, Dp, x = D[i], D[i - 1], mech[i - 1]
        for j in range(1, m + 1):
            Di[j] = min(Dp[j - 1] + sub(x, read[j - 1]), Dp[j] + dcost[i - 1], Di[j - 1] + 1.0)
    out, i, j = [], n, m
    while i or j:
        if i and j and abs(D[i][j] - (D[i - 1][j - 1] + sub(mech[i - 1], read[j - 1]))) < 1e-9:
            out.append((i - 1, j - 1)); i -= 1; j -= 1
        elif i and abs(D[i][j] - (D[i - 1][j] + dcost[i - 1])) < 1e-9:
            out.append((i - 1, None)); i -= 1
        else:
            out.append((None, j - 1)); j -= 1
    return out[::-1]


def compare(label, words, text, poly, divided):
    mech, cu, units = build_mech(words)
    read, marked, widx, rwords = parse_reading(text)
    pairs = align(mech, read, [1.0 if units[u]['unit'] is not None else 3.0 for u in cu])
    m2r = {mi: ri for mi, ri in pairs if mi is not None}
    r2m = {ri: mi for mi, ri in pairs if ri is not None and mi is not None}
    polyset = {u: {fold(x) for x in v} for u, v in poly.items()}

    def cipher(mi):
        return units[cu[mi]]['unit'] is not None

    def kind(mi):
        ri = m2r[mi]
        if ri is None:
            return 'del'
        x, y = mech[mi], read[ri]
        if y == HOLE:
            return 'hole'
        if x == y:
            return 'eq'
        if {x, y} == {'i', 'y'}:
            return 'iy'
        u = units[cu[mi]]
        if u['b'] - u['a'] == 1 and y in polyset.get(u['unit'], ()):
            return 'poly'
        return 'sub'
    mk = [kind(i) for i in range(len(mech))]
    changed = True                      # a deleted run next to a hole is part of the hole
    while changed:
        changed = False
        for i in range(len(mech)):
            if mk[i] == 'del' and ((i and mk[i - 1] == 'hole') or (i + 1 < len(mech) and mk[i + 1] == 'hole')):
                mk[i] = 'hole'; changed = True

    def classify(states, rchars, whole_marked):
        """states: states of the word's mech chars; rchars: the reading's letters that differ (substituted, inserted)."""
        if 'hole' in states:
            return 'unread'
        diff = [s for s in states if s != 'eq']
        if not diff and not rchars:
            return 'exact'
        if not rchars and set(diff) <= {'iy'}:
            return 'i/y'
        if not rchars and set(diff) <= {'iy', 'poly'}:
            return 'polyphony'
        if all(marked[r] for r in rchars) and (rchars or whole_marked) and ('del' not in diff or whole_marked):
            return 'marked'
        return 'silent'

    U = collections.Counter(); seen = collections.defaultdict(collections.Counter)
    for u in units:
        if u['unit'] is None:
            continue
        if u['value'] is None:
            U['no-value'] += 1; continue
        ks = range(u['a'], u['b'])
        U[classify([mk[k] for k in ks], [m2r[k] for k in ks if mk[k] == 'sub'], False)] += 1
        if len(ks) == 1 and mk[u['a']] in ('eq', 'iy', 'poly', 'sub'):
            seen[u['unit']][read[m2r[u['a']]]] += 1

    rows, W = [], collections.Counter()
    rw_chars = collections.defaultdict(list)
    for r, wi in enumerate(widx):
        rw_chars[wi].append(r)

    def show(ids, sep):
        return sep.join(str(units[i]['unit']) for i in ids)

    def val(ids):
        return ''.join(units[i]['value'] if units[i]['value'] is not None else '{%s}' % units[i]['unit'] for i in ids)

    if divided:
        # inserted letters of the reading go to the cipher word that the rest of their reading word sits on
        ins_to = collections.defaultdict(list); added = []
        for wi, rs in rw_chars.items():
            al = [(r, units[cu[r2m[r]]]['word']) for r in rs if r in r2m]
            ins = [r for r in rs if r not in r2m]
            if not ins:
                continue
            if not al:
                if read[rs[0]] != HOLE:
                    added.append(wi)
                continue
            for r in ins:
                prev = [w for q, w in al if q < r]; nxt = [w for q, w in al if q > r]
                ins_to[prev[-1] if prev else nxt[0]].append(r)
        byw = collections.defaultdict(list)
        for i, u in enumerate(units):
            byw[u['word']].append(i)
        for w in sorted(byw):
            ids = byw[w]
            ks = [k for i in ids for k in range(units[i]['a'], units[i]['b'])]
            rws = list(dict.fromkeys(widx[m2r[k]] for k in ks if m2r[k] is not None))
            if all(units[i]['value'] is None for i in ids):
                st = 'no-value'
            else:
                rch = [m2r[k] for k in ks if mk[k] == 'sub'] + ins_to.get(w, [])
                whole = bool(rws) and all(marked[r] for x in rws for r in rw_chars[x])
                st = classify([mk[k] for k in ks], rch, whole)
                if st == 'silent' and not rws:
                    st = 'dropped'
            W[st] += 1
            if st != 'exact':
                rows.append((label, show(ids, ''), val(ids), ' '.join(rwords[x] for x in rws), st))
        for wi in added:
            W['added'] += 1
            rows.append((label, '', '', rwords[wi], 'added'))
    else:
        dels = collections.defaultdict(list); k = 0
        while k < len(mech):
            if mk[k] == 'del' and cipher(k):
                j = k
                while j < len(mech) and mk[j] == 'del':
                    j += 1
                pw = widx[m2r[k - 1]] if k and m2r[k - 1] is not None else None
                nw = widx[m2r[j]] if j < len(mech) and m2r[j] is not None else None
                if pw is not None and pw == nw:
                    dels[pw].extend(range(k, j))
                else:
                    ids = list(dict.fromkeys(cu[k:j])); W['dropped'] += 1
                    rows.append((label, show(ids, ' '), mech[k:j], '', 'dropped'))
                k = j
            else:
                k += 1
        for wi in sorted(rw_chars):
            rs = rw_chars[wi]
            ms = [r2m[r] for r in rs if r in r2m]
            if not ms:
                before = [r2m[q] for q in range(rs[0]) if q in r2m]
                after = [r2m[q] for q in range(rs[-1] + 1, len(read)) if q in r2m]
                if not (before and after and cipher(before[-1]) and cipher(after[0])):
                    continue
                st, ids = 'added', []
            elif not any(cipher(m) for m in ms):
                continue
            elif all(read[r] == HOLE for r in rs):
                a = b = ms[0]
                if units[cu[a]]['value'] is None:
                    ids, st = [cu[a]], 'no-value'
                else:                    # the hole swallows the valued cipher around it, up to the next open code
                    ok = lambda k: mk[k] == 'hole' and cipher(k) and units[cu[k]]['value'] is not None
                    while a and ok(a - 1):
                        a -= 1
                    while b + 1 < len(mech) and ok(b + 1):
                        b += 1
                    ids, st = list(dict.fromkeys(cu[a:b + 1])), 'unread'
            else:
                ids = list(dict.fromkeys(cu[m] for m in ms))
                rch = [r for r in rs if r not in r2m or mk[r2m[r]] == 'sub']
                st = classify([mk[m] for m in ms] + ['del'] * len(dels.get(wi, [])), rch, all(marked[r] for r in rs))
            W[st] += 1
            if st != 'exact':
                rows.append((label, show(ids, ' '), val(ids), rwords[wi], st))
    return rows, W, U, seen


def run(folder, write=True):
    tdir = os.path.join(ROOT, 'targets', folder)
    spec = importlib.util.spec_from_file_location('replay_' + folder, os.path.join(tdir, 'replay.py'))
    ad = importlib.util.module_from_spec(spec); sys.path.insert(0, tdir); spec.loader.exec_module(ad)
    sys.path.pop(0)
    R = ad.reading(); poly = getattr(ad, 'POLYPHONY', {})
    rows, W, U, seen = [], collections.Counter(), collections.Counter(), collections.defaultdict(collections.Counter)
    missing = []
    labels = set()
    for label, words in ad.mechanical():
        labels.add(label)
        if label not in R:
            missing.append(label); continue
        r, w, u, s = compare(label, words, R[label], poly, ad.DIVIDED)
        rows += r; W += w; U += u
        for k, c in s.items():
            seen[k] += c

    def rates(C):
        n = sum(v for k, v in C.items() if k not in ('no-value', 'added'))
        d = {k: C.get(k, 0) for k in CLASSES}
        d['counted'] = n
        pct = lambda x: round(100 * x / n, 1) if n else None
        d['exact_pct'] = pct(d['exact'])
        d['exact_iy_pct'] = pct(d['exact'] + d['i/y'])
        d['exact_iy_polyphony_pct'] = pct(d['exact'] + d['i/y'] + d['polyphony'])
        d['unmarked_pct'] = pct(d['silent'] + d['dropped'])
        return d
    multi = {k: dict(c.most_common()) for k, c in seen.items() if len(c) > 1}
    firm = {k: {x: n for x, n in v.items() if n >= 3} for k, v in multi.items()}
    firm = {k: v for k, v in firm.items() if len(v) > 1}
    summary = {
        'folder': folder, 'sources': getattr(ad, 'SOURCES', {}),
        'word_basis': 'cipher words' if ad.DIVIDED else 'words of the reading in the cipher passages',
        'words': rates(W), 'units': rates(U),
        'lines_without_reading': missing,
        'reading_lines_without_transcription': sorted(set(R) - labels),
        'declared_polyphony': poly,
        'values_read_per_sign': multi,
        'most_values_on_one_sign': max((len(v) for v in multi.values()), default=1),
        'values_read_per_sign_3_times_or_more': firm,
        'most_values_on_one_sign_3_times_or_more': max((len(v) for v in firm.values()), default=1),
        'folding': 'case, accents, punctuation dropped; u=v, i=j; i/y counted apart',
    }
    if not write:
        return summary, rows
    with open(os.path.join(tdir, 'replay.tsv'), 'w', encoding='utf8', newline='\n') as f:
        f.write('# key replay (docs/_replay.py): every word where the reading is not the key output\n')
        f.write('line\tcipher\tkey_output\treading\tclass\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    with open(os.path.join(tdir, 'replay.json'), 'w', encoding='utf8', newline='\n') as f:
        json.dump(summary, f, ensure_ascii=False, indent=1); f.write('\n')
    return summary, rows


def has_adapter(folder):
    return os.path.exists(os.path.join(ROOT, 'targets', folder, 'replay.py'))


def saved(folder):
    """The summary of the last written run (targets/<folder>/replay.json), or None."""
    try:
        return json.load(open(os.path.join(ROOT, 'targets', folder, 'replay.json'), encoding='utf8'))
    except (OSError, ValueError):
        return None


def unmarked(summary):
    w = summary['words']
    return w['silent'] + w['dropped']


def line(summary):
    w = summary['words']
    return (f"{w['exact']} of {w['counted']} {summary['word_basis']} are the key's output ({w['exact_pct']}%), "
            f"{w['marked']} differ with a mark, {unmarked(summary)} differ or are left out with no mark, {w['unread']} unread")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        sys.exit(__doc__)
    bad = 0
    for folder in args:
        s, rows = run(folder)
        print(f"{folder}: key replay ({s['word_basis']})")
        for name in ('words', 'units'):
            d = s[name]
            print(f"  {name} {d['counted']:5d}: exact {d['exact']} ({d['exact_pct']}%); with i/y {d['exact_iy_pct']}%; "
                  f"with declared polyphony {d['exact_iy_polyphony_pct']}%; marked {d['marked']}; "
                  f"unmarked {d['silent'] + d['dropped']} ({d['unmarked_pct']}%), of them dropped {d['dropped']}; "
                  f"unread {d['unread']}; open codes {d['no-value']}; added by the reading {d['added']}")
        if s['lines_without_reading']:
            print('  lines with no reading:', ' '.join(s['lines_without_reading']))
        if s['reading_lines_without_transcription']:
            print('  reading lines with no transcription behind them:', ' '.join(s['reading_lines_without_transcription']))
        print(f"  signs read with more than one value: {len(s['values_read_per_sign'])} "
              f"(most on one sign: {s['most_values_on_one_sign']}); counting only values read 3+ times: "
              f"{len(s['values_read_per_sign_3_times_or_more'])} signs, most {s['most_values_on_one_sign_3_times_or_more']}")
        ok = s['words']['silent'] + s['words']['dropped'] == 0
        print('  result:', 'reproduces (every difference marked)' if ok else 'unmarked differences, see replay.tsv')
        bad += not ok
    if '--check' in sys.argv and bad:
        sys.exit(1)


if __name__ == '__main__':
    main()
