"""Leads waiting to be vetted, and the check of a vetting file before it is sent (research/VET.md).

  python research/vet.py --list [--online] [--area <word>]   leads in research/leads.json with no verdict yet: id,
                                                             access, year, title, shelfmark and what blocked the last
                                                             attempt (vetting_note). --online leaves out the leads whose
                                                             ciphertext is only in the archive; --area filters on a
                                                             word of the region, shelfmark or title
  python research/vet.py --show 1234                         one lead in full
  python research/vet.py --check <folder>/vetting.json       check a vetting file; prints result: pass or result: fail
  python research/vet.py --apply <folder>/vetting.json       project sessions only, after review: write the blocks of
                                                             a file that passes --check into research/leads.json and
                                                             print the ids now ready for _check_catalogue.py --promote

A vetting file is a JSON object {"<lead id>": block}. A block is either the "vetting" block of
docs/_check_catalogue.py with a verdict, or {"unvetted": "what is missing"}. The rules are those the project's own
vetting passes are held to (research/vetting_2026-11/check_out.py): an "open" verdict must pass the catalogue gate and
rest on at least three searches run for that lead; nothing may be pasted across leads; any other verdict says in
"closed" exactly what shows it. --list, --show and --check only read leads.json. --apply is the one step that writes
it, and it promotes nothing: an "open" block that collides with a catalogue entry is taken off the lead and kept as
"vetting_held" with the reason; a verdict that replaces an earlier one keeps the earlier block as "vetting_superseded".
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'docs'))
import _check_catalogue as C  # noqa: E402

HEDGE = re.compile(r'\b(presumably|probably|likely|perhaps|possibly|may contain|should be)\b', re.I)
VERDICTS = ('open', 'read', 'partly_read', 'duplicate', 'key_lookup', 'not_cipher')


def leads():
    with open(os.path.join(HERE, 'leads.json'), encoding='utf-8') as fh:
        return json.load(fh)['leads']


def waiting(l):
    return not (l.get('vetting') or {}).get('verdict')


def listing(args):
    online = '--online' in args
    area = args[args.index('--area') + 1].lower() if '--area' in args else None
    n = 0
    for l in sorted(leads(), key=lambda x: x['id']):
        if not waiting(l) or (online and l.get('access') == 'archive'):
            continue
        if area and area not in ' '.join(str(l.get(k, '')) for k in ('region', 'shelfmark', 'title', 'place')).lower():
            continue
        n += 1
        note = re.sub(r'\s+', ' ', l.get('vetting_note') or '')
        print('%d  [%s]  %s  %s' % (l['id'], l.get('access') or 'online', l.get('year', ''), l.get('title', '')))
        print('      %s' % l.get('shelfmark', ''))
        if note:
            print('      last attempt: %s' % (note if len(note) <= 300 else note[:297] + '...'))
    print('%d lead(s) waiting to be vetted' % n)


def show(n):
    for l in leads():
        if l['id'] == n:
            print(json.dumps(l, indent=1, ensure_ascii=False))
            return 0
    print('no lead %d in research/leads.json' % n)
    return 1


def check(path):
    with open(path, encoding='utf-8') as fh:
        out = json.load(fh)
    if not isinstance(out, dict):
        print('the file must be a JSON object {"<lead id>": block}\nresult: fail (1)')
        return 1
    by_id = {str(l['id']): l for l in leads()}
    bad, blocks, qs = [], {}, collections.Counter()
    for i, b in out.items():
        if i not in by_id:
            bad.append('%s: not a lead in research/leads.json' % i)
        elif not isinstance(b, dict):
            bad.append('%s: not an object' % i)
        elif 'verdict' not in b:
            if not (isinstance(b.get('unvetted'), str) and len(b['unvetted']) >= 25):
                bad.append('%s: needs a verdict, or "unvetted" naming the blocker' % i)
        elif b['verdict'] not in VERDICTS:
            bad.append('%s: verdict %r is not one of %s' % (i, b['verdict'], ', '.join(VERDICTS)))
        else:
            blocks[i] = b
    for i, b in blocks.items():
        if not waiting(by_id[i]) and not C.text_ok(b.get('supersedes')):
            bad.append('%s: already has the verdict %r; add "supersedes" saying what new evidence changes it'
                       % (i, by_id[i]['vetting']['verdict']))
        if b['verdict'] != 'open':
            if not (C.text_ok(b.get('by')) and re.match(r'\d{4}-\d\d-\d\d$', str(b.get('date')))):
                bad.append('%s: needs "date" (ISO) and "by" (the contributor, and the agent and model used)' % i)
            if not C.text_ok(b.get('closed')):
                bad.append('%s: verdict %s needs "closed" saying exactly what shows it' % (i, b['verdict']))
            continue
        e = dict(by_id[i])
        e.update(b.get('lead_updates') or {})
        e['vetting'] = {k: v for k, v in b.items() if k != 'lead_updates'}
        bad += ['%s: %s' % (i, p) for p in C.vetting_problems(e)]
        s = b.get('searches')
        if not (isinstance(s, list) and len(s) >= 3 and all(
                isinstance(x, dict) and C.text_ok(x.get('query')) and C.text_ok(x.get('result')) for x in s)):
            bad.append('%s: needs "searches": at least 3 of {"query", "result"}, run for this lead' % i)
        else:
            for q in {x['query'].strip().lower() for x in s}:
                qs[q] += 1
        seen = b.get('seen') or {}
        cipher = str(seen.get('cipher'))
        if HEDGE.search(cipher):
            bad.append('%s: seen.cipher hedges that cipher is there: show it, or write "unvetted"' % i)
        if seen.get('kind') == 'not online' and not re.search('["“\']', cipher):
            bad.append('%s: seen.cipher must quote the archive\'s description' % i)
    for q, n in qs.items():
        if n > 2:
            bad.append('query used for %d leads, run one for each: %s' % (n, q[:70]))
    opens = [b for b in blocks.values() if b['verdict'] == 'open']
    for k in C.PRIOR_ART:
        c = collections.Counter(str((b.get('prior_art') or {}).get(k)).strip() for b in opens)
        for t, n in c.items():
            if n > 2:
                bad.append('prior_art.%s is the same text on %d leads; say what was found for each: %s' % (k, n, t[:60]))
    for x in bad:
        print(x)
    print('%d lead(s);' % len(out),
          dict(collections.Counter(b.get('verdict', 'unvetted') if isinstance(b, dict) else '?' for b in out.values())))
    print('result: pass' if not bad else 'result: fail (%d)' % len(bad))
    return 1 if bad else 0


def apply(path):
    if check(path):
        print('not applied: the file must pass --check first')
        return 1
    with open(path, encoding='utf-8') as fh:
        out = json.load(fh)
    d, all_leads = C.load(C.LEADS, 'leads')
    _, entries = C.load(C.CAT, 'entries')
    by_id = {str(l['id']): l for l in all_leads}
    src = os.path.relpath(os.path.abspath(path), os.path.dirname(HERE)).replace(os.sep, '/')
    ready, tally = [], collections.Counter()
    for i, b in out.items():
        l = by_id[i]
        if 'verdict' not in b:
            l['vetting_note'] = '%s (%s)' % (b['unvetted'].rstrip(), src)
            tally['unvetted'] += 1
            continue
        b = dict(b)
        l.update(b.pop('lead_updates', None) or {})
        if (l.get('vetting') or {}).get('verdict'):
            l['vetting_superseded'] = l['vetting']
        l['vetting'] = b
        l.pop('vetting_note', None)
        if b['verdict'] == 'open':
            why = C.vetting_problems(l) + C.collisions(l, entries)
            if why:
                l['vetting_held'] = l.pop('vetting')
                l['vetting_note'] = 'Vetted open in %s; held: %s. Block kept in vetting_held.' % (src, '; '.join(why))
                print('#%s held: %s' % (i, '; '.join(why)))
                tally['held'] += 1
                continue
            ready.append(i)
        tally[b['verdict']] += 1
    C.save(C.LEADS, d)
    print('applied to research/leads.json:', dict(tally))
    if ready:
        print('ready to promote: python docs/_check_catalogue.py --promote ' + ' '.join(ready))
    return 0


def main():
    a = sys.argv[1:]
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if a[:1] == ['--list']:
        listing(a)
    elif a[:1] == ['--show'] and len(a) == 2:
        sys.exit(show(int(a[1])))
    elif a[:1] == ['--check'] and len(a) == 2:
        sys.exit(check(a[1]))
    elif a[:1] == ['--apply'] and len(a) == 2:
        sys.exit(apply(a[1]))
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == '__main__':
    main()
