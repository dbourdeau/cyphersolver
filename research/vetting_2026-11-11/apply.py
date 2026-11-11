"""Apply the 11 Nov 2026 cloud pass to research/leads.json and promote what passes the gate.

    python3 research/vetting_2026-11-11/apply.py blocks 01 02 ...   write verdicts / notes from out_NN.json (existing leads)
    python3 research/vetting_2026-11-11/apply.py sweeps             after merge.py --write: check the vetting blocks that
                                                                    sweep rows carried in; a block the gate refuses is
                                                                    taken off the lead and kept as vetting_note
    python3 research/vetting_2026-11-11/apply.py promote            promote every lead whose block is by this pass,
                                                                    verdict open, and passes the gate; prints the ids

An open block needs at least three per-lead searches and an unhedged seen.cipher (the check_out.py rules)."""
import collections, json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'docs'))
import _check_catalogue as C
MARK = ('claude cloud vetting 11 Nov', 'claude cloud sweep 11 Nov')
HEDGE = re.compile(r'\b(presumably|probably|likely|perhaps|possibly|may contain|should be)\b', re.I)


def mine(l):
    return str((l.get('vetting') or {}).get('by', '')).startswith(MARK)


def extra_problems(l):
    v = l.get('vetting') or {}
    bad = []
    s = v.get('searches')
    if not (isinstance(s, list) and len(s) >= 3 and all(isinstance(x, dict) and C.text_ok(x.get('query')) and C.text_ok(x.get('result')) for x in s)):
        bad.append('fewer than three per-lead searches')
    seen = v.get('seen') or {}
    if HEDGE.search(str(seen.get('cipher'))):
        bad.append('seen.cipher hedges')
    if seen.get('kind') == 'not online' and not re.search(r'["“\'‘«]', str(seen.get('cipher'))):
        bad.append('seen.cipher does not quote the description')
    return bad


def blocks(names):
    d, leads = C.load(C.LEADS, 'leads')
    byid = {str(l['id']): l for l in leads}
    tally = collections.Counter()
    for n in names:
        for i, b in json.loads((HERE / f'out_{n}.json').read_text(encoding='utf-8')).items():
            l = byid.get(i)
            if not l:
                print('not in leads.json:', i); continue
            if 'verdict' not in b:
                l['vetting_note'] = b['unvetted']; tally['unvetted'] += 1; continue
            b = dict(b)
            l.update(b.pop('lead_updates', None) or {})
            l['vetting'] = b
            l.pop('vetting_note', None)
            tally[b['verdict']] += 1
    C.save(C.LEADS, d)
    print(dict(tally))


def hold(l, why):
    v = l.pop('vetting')
    l['vetting_note'] = 'Sweep or vetting block of 11 Nov 2026 said open; held: ' + '; '.join(why) + '. Block kept in vetting_held.'
    l['vetting_held'] = v


def sweeps():
    d, leads = C.load(C.LEADS, 'leads')
    _, entries = C.load(C.CAT, 'entries')
    for l in leads:
        if mine(l) and l['vetting'].get('verdict') == 'open':
            why = C.vetting_problems(l) + extra_problems(l) + C.collisions(l, entries)
            if why:
                print(f"#{l['id']} held:", why); hold(l, why)
    C.save(C.LEADS, d)


def promote():
    _, leads = C.load(C.LEADS, 'leads')
    _, entries = C.load(C.CAT, 'entries')
    good = [l['id'] for l in leads if mine(l) and l['vetting'].get('verdict') == 'open'
            and not (C.vetting_problems(l) + extra_problems(l) + C.collisions(l, entries))]
    if good:
        C.promote(good)
    print('PROMOTED', ' '.join(map(str, good)))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    {'blocks': lambda: blocks(a[1:]), 'sweeps': sweeps, 'promote': promote}[a[0]]()
