"""Sample D (25 Sept 2026): the legible stretches of the damaged ICIT texts that rtools.load_all's clean sample F leaves
out (broken edges, illegible 000 signs, uncertain '?'). Each line is cut at its gaps; a run of 2+ legible signs is a
segment, with flags for an open start / end (a broken edge or a gap next to it). Segments found intact inside a clean
text (A, B or F lines) are dropped as probable copies (mould mates, sealings), so D is independent of the samples used
so far. Line order reversed as rtools (LINES_REVERSED = True)."""
import icit_full
import rtools as R
from signs import load


def _sub(a, b):
    n = len(a)
    return any(tuple(b[i:i + n]) == a for i in range(len(b) - n + 1))


def segments(min_len=2, drop_copies=True):
    A, B, rowsA, recs, F = R.load_all()
    keep = {r['sealid'] for r in F}
    clean = [tuple(t) for t in A] + [tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln] + [tuple(ln) for r in F for ln in r['seq'] if ln]
    by_len = {}
    for t in set(clean):
        by_len.setdefault(len(t), []).append(t)
    out = []
    for rec in icit_full.records(R.FPATH):
        if rec[0] in keep:
            continue
        for ln in icit_full.lines_of(rec[34]):
            run, start_open = [], ln['broken_start']
            sig = ln['signs'] + [None]
            for k, g in enumerate(sig):
                if g is None or g == '?':
                    end_open = (k < len(sig) - 1) or ln['broken_end']
                    if len(run) >= min_len:
                        seg = tuple(run)
                        if not (drop_copies and any(_sub(seg, t) for L_, ts in by_len.items() if L_ >= len(seg) for t in ts)):
                            out.append({'sealid': rec[0], 'site': rec[3], 'type': rec[20], 'motif': rec[18].split(':')[0],
                                        'signs': seg, 'open_start': start_open, 'open_end': end_open})
                    run, start_open = [], True
                else:
                    run.append(g)
    return out
