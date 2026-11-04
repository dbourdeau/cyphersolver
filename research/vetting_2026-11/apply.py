"""Apply the leads review to research/leads.json and promote in commit-sized batches.

    python research/vetting_2026-11/apply.py blocks b r c01 c02   write verdicts and notes from those outputs (later ones win)
    python research/vetting_2026-11/apply.py next 50              promote the next 50 open leads through the gate; prints their ids
    python research/vetting_2026-11/apply.py status               counts

"b" and "r" stand for every out_bNN or out_rNN file. A lead the review left unvetted keeps its note. A lead closed key_lookup with no
reading on record loses that verdict, because a key no longer closes a lead (rule of 3 Nov 2026)."""
import collections, json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'docs'))
import _check_catalogue as C
sys.stdout.reconfigure(encoding='utf-8')


def outputs(names):
    out = {}
    for n in names:
        fs = sorted(HERE.glob(f'out_{n}[0-9][0-9].json')) if n in ('b', 'r') else [HERE / f'out_{n}.json']
        for f in fs:
            out.update(json.loads(f.read_text(encoding='utf-8')))
    return out


def blocks(names):
    out = outputs(names)
    d, leads = C.load(C.LEADS, 'leads')
    byid = {str(l['id']): l for l in leads}
    tally, gone = collections.Counter(), []
    for i, b in out.items():
        l = byid.get(i)
        if not l:
            gone.append(i); continue
        if 'verdict' not in b:
            l['vetting_note'] = b['unvetted']
            if (l.get('vetting') or {}).get('verdict') == 'key_lookup':
                l['vetting'].pop('verdict')
            tally['unvetted'] += 1; continue
        b = dict(b)
        if re.match(r'[bcr]\d\d', str(b.get('by'))):
            b['by'] = 'claude leads review batch ' + b['by']
        l.update(b.pop('lead_updates', None) or {})
        l['vetting'] = b
        l.pop('vetting_note', None)
        tally[b['verdict']] += 1
    C.save(C.LEADS, d)
    print(dict(tally), 'not in leads.json (promoted or removed elsewhere):', gone)


def ready():
    _, leads = C.load(C.LEADS, 'leads')
    return [l['id'] for l in leads if (l.get('vetting') or {}).get('verdict') == 'open' and str(l['vetting'].get('by', '')).startswith('claude leads review')]


def status():
    _, leads = C.load(C.LEADS, 'leads')
    print(len(leads), 'leads;', dict(collections.Counter((l.get('vetting') or {}).get('verdict', 'none') for l in leads)), '; review open waiting:', len(ready()))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['blocks']:
        blocks(a[1:])
    elif a[:1] == ['next']:
        ids = ready()[:int(a[1])]
        _, entries = C.load(C.CAT, 'entries')
        _, leads = C.load(C.LEADS, 'leads')
        byid = {l['id']: l for l in leads}
        good = [i for i in ids if not (C.vetting_problems(byid[i]) + C.collisions(byid[i], entries))]
        for i in set(ids) - set(good):
            print(f'#{i} held:', C.vetting_problems(byid[i]) + C.collisions(byid[i], entries))
            byid[i]['vetting']['verdict_held'] = 'open'
            byid[i]['vetting'].pop('verdict')
            byid[i]['vetting_note'] = 'Review said open, the gate refused it: ' + '; '.join(C.vetting_problems(byid[i]) + C.collisions(byid[i], entries))
        if set(ids) - set(good):
            doc = json.loads(C.LEADS.read_text(encoding='utf-8')); doc['leads'] = leads; C.save(C.LEADS, doc)
        if good:
            C.promote(good)
        print('PROMOTED', ' '.join(map(str, good)))
    else:
        status()
