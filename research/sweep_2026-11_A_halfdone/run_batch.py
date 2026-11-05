"""Run several PARES sweep jobs one after another, under one hard request cap (Oct 2026 archive sweep).

    python research/pares_ags/run_batch.py CAP JOB [JOB ...] [--maxpages N]
    python research/pares_ags/run_batch.py CAP --jobs FILE [--maxpages N]

CAP      hard cap on live requests for the whole batch (all jobs, both passes, every request counts).
JOB      "term"                 the whole term, no year filter
         "term@1500-1549"       one year range (anio1=1500, anio2=1549)
         "term@1500-1599/10"    split into ranges of 10 years: 1500-1509, 1510-1519, ..., 1590-1599
                                (year jobs are refused: PARES ignores anio1/anio2, README access log)
         "term#idFI=16"         a PARES facet filter (here: start date in the 16th century; idFI=0 = no
                                date, idD=S/N = digitised or not); this is the working way to split a term
FILE     one JOB per line; empty lines and lines starting with # are skipped.

Example (with PARES_RAW set to a scratch folder for the raw pages):
    python research/pares_ags/run_batch.py 120 "carta cifrada" "cifrada@1500-1599/10" --maxpages 30

Each job is sweep.run(term, maxpages, anio1, anio2): one PARES session, 100 rows a page, resumable through
hits_progress.json, so a batch that stops can be started again with the same arguments. When a finished job has
fewer unique hits than the total PARES reports (the result order is not stable between pages), the job gets a
second pass in title order (PARES_ORDER=0) while the cap allows. Politeness is sweep.py's: one request at a time,
PARES_DELAY (default 20) s plus 0-10 s jitter between requests; on top of that a 10-minute pause after every 50
requests. The batch stops at the first 429 (exit 2) and when the cap is reached (exit 3); it never retries.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sweep  # noqa: E402

PAUSE_EVERY, PAUSE_SECS = 50, 600


def expand(job):
    """'term', 'term#facet', 'term@a-b' or 'term@a-b/step' -> list of (term, anio1, anio2, facet)."""
    if '#' in job:
        term, facet = job.split('#', 1)
        return [(term.strip(), None, None, facet.strip())]
    if '@' not in job:
        return [(job.strip(), None, None, None)]
    term, rng = job.rsplit('@', 1)
    step = None
    if '/' in rng:
        rng, step = rng.split('/')
        step = int(step)
    a, b = (int(x) for x in rng.split('-'))
    if not step:
        return [(term.strip(), a, b, None)]
    return [(term.strip(), y, min(y + step - 1, b), None) for y in range(a, b + 1, step)]


def main(argv):
    if not argv or not argv[0].isdigit():
        print(__doc__, file=sys.stderr)
        return 1
    cap, rest, jobs, maxpages = int(argv[0]), argv[1:], [], 50
    i = 0
    while i < len(rest):
        if rest[i] == '--maxpages':
            maxpages, i = int(rest[i + 1]), i + 2
        elif rest[i] == '--jobs':
            jobs += [l.strip() for l in open(rest[i + 1], encoding='utf-8') if l.strip() and not l.startswith('#')]
            i += 2
        else:
            jobs.append(rest[i])
            i += 1
    todo = [t for j in jobs for t in expand(j)]
    if not todo:
        print('no jobs', file=sys.stderr)
        return 1
    if any(a1 is not None for _, a1, _, _ in todo):
        # Year-filter bug (README, access log 27 Oct 2026): anio1/anio2 are dropped by the 100-row formBusqueda
        # POST, so every year job re-runs the whole term. Refuse until sweep.open_search sends them in the POST too.
        print('year ranges are not applied by PARES in the 100-row session (README, year-filter bug); '
              'fix sweep.open_search first', file=sys.stderr)
        return 1
    sweep.MAXREQ, sweep.PAUSE_EVERY, sweep.PAUSE_SECS = cap, PAUSE_EVERY, PAUSE_SECS
    print(f'{len(todo)} jobs, cap {cap} requests, pause {PAUSE_SECS} s after every {PAUSE_EVERY}', file=sys.stderr)
    code = 0
    try:
        for term, a1, a2, fc in todo:
            sweep.ORDER = 8
            n = sweep.run(term, maxpages, a1, a2, fc)
            st = sweep.load_progress().get(sweep.key_of(term, a1, a2, fc), {})
            if st.get('done') and isinstance(st.get('total'), int) and st.get('unique_hits', 0) < st['total']:
                sweep.ORDER = 0
                n += sweep.run(term, maxpages, a1, a2, fc)
            print(f'job {sweep.key_of(term, a1, a2, fc)!r}: {n} new hits, {sweep.NREQ} requests so far', file=sys.stderr)
    except sweep.Blocked as e:
        print('stopped:', e, file=sys.stderr)
        code = 2 if '429' in str(e) else 3
    finally:
        sweep.ORDER = 8
        for t, m, s in sweep.LOG:
            print(t, 'UTC', m, s, file=sys.stderr)
        print(json.dumps({'requests': sweep.NREQ, 'exit': code}), file=sys.stderr)
    return code


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main(sys.argv[1:]))
