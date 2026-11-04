"""Check reading_marked_c13r.txt against the signs; exit 1 on any unmarked departure. Then word counts, the held-out
test (key frozen on M01-M06, scored on M07-M10) and the same test with shuffled tables.
Marks: {+x} restored letter (no unit); {-} consumes one null unit; {a/b} one unit whose values include b;
{?x} one doubtful unit whose values include x; [G text] one code unit G; <<...>> clear text on the page, skipped.
Limit: a unit passes when the reading's letter is ANY of the values of its sign name. For the sign names with two
values (9 g e + f q N o, and u|v) the checker cannot tell whether the right one was picked: such picks are listed
below ("two-valued picks") and were checked by eye against the clear translation on c. 14r, not by this script.
    python scripts/check_marks.py
"""
import pathlib, random, re, sys, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decode

ITEM = re.compile(r'<<[^>]*>>|\[[^\]]*\]|\{[^}]*\}|[^\W\d_]', re.UNICODE)
ASSIGNED = {}
PICKS = []


def plain(c):
    return unicodedata.normalize('NFD', c)[0].lower()


def reading():
    return {l.split('\t')[0]: l.split('\t', 1)[1] for l in
            (decode.ROOT / 'reading_marked_c13r.txt').read_text(encoding='utf8').splitlines() if l.startswith('M')}


def check(key):
    bad = []; words = {'verbatim': 0, 'marked': 0}; rd = reading()
    for ln, toks in decode.signs():
        us = decode.units(toks, key); k = 0

        def take(val, ok, msg):
            nonlocal k
            if k >= len(us):
                bad.append(f'{ln}: {msg}: past the end of the signs'); return
            if not ok(us[k]):
                bad.append(f'{ln}: {msg}: signs give {us[k][0]}={us[k][1]}{"?" if us[k][2] else ""}')
            if msg.startswith('letter') and len(us[k][1]) > 1 and val in us[k][1]:
                PICKS.append(f'{ln}:{us[k][0]}={val} (of {"|".join(us[k][1])})')
            ASSIGNED[(ln, k)] = val; k += 1

        for it in ITEM.findall(rd.get(ln, '')):
            if it.startswith('<<'):
                continue
            if it.startswith('['):
                g = it[1:-1].split(' ')[0]; take('[' + g + ']', lambda u: u[0] == g, f'code {it}')
            elif it == '{-}':
                take('null', lambda u: 'null' in u[1], 'null mark')
            elif it.startswith('{+'):
                pass
            elif it.startswith('{?'):
                x = plain(it[2]); take(x, lambda u: u[2] and x in u[1], f'doubtful mark {it}')
            elif it.startswith('{'):
                a, _, b = it[1:-1].partition('/'); take(b, lambda u: b in u[1], f'change mark {it}')
            else:
                x = plain(it); take(x, lambda u: x in u[1] and not u[2], f'letter {it} unmarked')
        if k != len(us):
            bad.append(f'{ln}: {len(us) - k} sign units not covered by the reading')
        t = re.sub(r'<<[^>]*>>', '', rd.get(ln, '')); t = re.sub(r'\[(\S+) ([^\]]*)\]', r'[\1]', t)
        for w in t.split():
            w = w.strip(',.;:')
            if not w or w.startswith('-') or w == '{-}':
                continue
            words['marked' if re.search(r'\{(?!-\})', w) else 'verbatim'] += 1
    return bad, words


def agrees(r, g, fv):
    return r is not None and (r in fv or r == '[' + g + ']')


def score(key):
    """Held-out units (M07-M10) whose value under `key` includes the value the reading gives them."""
    tot = agree = 0
    for ln, toks in decode.signs():
        if ln < 'M07':
            continue
        for k, (g, _, _) in enumerate(decode.units(toks, key)):
            tot += 1
            agree += agrees(ASSIGNED.get((ln, k)), g, key.get(g, []))
    return agree, tot


def main():
    bad, words = check(decode.load_key())
    for b in bad:
        print('FAIL', b)
    n = words['verbatim'] + words['marked']
    print(f"cipher words read: {n} (clear words on the page not counted); verbatim {words['verbatim']}, "
          f"with a marked repair {words['marked']}")
    uv = sum(1 for x in PICKS if '(of u|v)' in x)
    print(f'two-valued picks (letter chosen by the reader among the values of one sign name; not checked here): '
          f'{len(PICKS)} of {len(ASSIGNED)} units, {uv} of them u|v')
    print('    ' + ' '.join(x for x in PICKS if '(of u|v)' not in x))
    fk = decode.load_key(frozen_only=True)
    a, t = score(fk)
    print(f'held-out M07-M10: {t} units; frozen key (M01-M06) agrees with the reading on {a} ({100 * a / t:.1f}%); '
          f'scored against our own reading of M07-M10 (itself aligned to c. 14r), a two-valued name counts if either '
          f'value matches; others:')
    for ln, toks in decode.signs():
        if ln >= 'M07':
            for k, (g, _, _) in enumerate(decode.units(toks, fk)):
                r = ASSIGNED.get((ln, k)); fv = fk.get(g, [])
                if not agrees(r, g, fv):
                    print(f'    {ln}: {g} -> {r}: frozen key gives {"|".join(fv) or "nothing"}')
    random.seed(1546)
    names = [s for s in fk if not s.startswith('{') and s != 'eti']
    vals = [fk[s] for s in names]
    res = []
    for _ in range(1000):
        random.shuffle(vals)
        sk = dict(fk); sk.update(dict(zip(names, vals)))
        res.append(score(sk)[0])
    res.sort()
    print(f'shuffled tables (1000; letter values permuted among the sign names, nulls and eti kept): '
          f'mean {sum(res) / len(res):.1f}/{t}, 95th percentile {res[949]}, max {res[-1]}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
