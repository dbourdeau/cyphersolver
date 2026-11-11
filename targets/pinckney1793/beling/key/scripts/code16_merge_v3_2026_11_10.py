"""Code 16 merged key, version 2 (10 Nov 2026).

Word sources (plaintext word + ordered groups with marks):
  tunis     Eaton's enclosure of 9 Oct 1802, body: aligned by hand to the 1802 printed translation (unflagged words only)
  tunis-ps  Eaton's postscript, editors' decipherment, re-read with the punctuation
  lear      Lear, Jan 1813: fresh transcription of 10 Nov (interlinear, placement clear)
  p1795     Pinckney 1795 (M31 roll 7, frames 0018-0021): Taylor's interlinear, placement clear; a word and the
            dash rows after it are one unit
  p1795b    Pinckney, Oct-Dec 1795 (M31 roll 7, frames 0020, 0111, 0177): interlinear, same rule
  e1801     Eaton, 25 May 1801 (T303 roll 2, frame 0049): Wagner's interlinear, same rule
Element list: Weber's WE023-WE028 vocabulary (sources/raw/weber_ill_2026-11-10/weber_1600_family_vocab.txt).
Marks: ^ doubles the element's last letter; + or ++ lets an inflection follow.

Grades in the output key:
  D  single unmarked group under a single word, in one or more sources (n = observations)
  S  not D, but the only list element that fits every word the group occurs in (frame solver)
  B  neither; value from Bourdeau's legation1788 key (c14c822) and that value is a list element not owned by another group
Bourdeau values that are not list elements are listed separately, not entered.
"""
from pathlib import Path
import csv, json, re, collections, importlib.util, hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/code16_merged_2026-11-10'
spec = importlib.util.spec_from_file_location('fs', ROOT / 'scripts/code16_frame_solver_2026_11_10.py')
fs = importlib.util.module_from_spec(spec); spec.loader.exec_module(fs)
norm = fs.norm


def tok(t):
    t = t.strip()
    m = re.fullmatch(r'(\d+)(\+\+|\+|\^)?', t)
    if not m: return None
    return (int(m.group(1)), '+' if (m.group(2) or '').startswith('+') else (m.group(2) or ''))


def clean_word(s):
    s = re.sub(r'\[.*?\]', '', s)
    return norm(s)


def load_interlined(path, tag, words):
    """Clerk-interlined spans: a word and the dash rows after it are one unit; 'ac —' continues on the next row."""
    rows = list(csv.DictReader(Path(path).open(), delimiter='\t'))
    cur = None
    def flush():
        nonlocal cur
        if cur and cur['ok'] and cur['w'] and ' ' not in cur['raw'].strip():
            words.append((tag, cur['loc'], cur['w'], cur['gs']))
        cur = None
    for r in rows:
        if r['kind'].strip() != 'interlinear':
            flush(); continue
        w = r['interlinear'].strip()
        gs = [tok(x) for x in r['groups'].split()]
        good = r['placement'].strip() == 'clear' and gs and all(gs)
        if re.fullmatch(r'[—–\-\s.]+', w):
            if cur:
                if good: cur['gs'] += gs
                else: cur['ok'] = False
            continue
        if cur and cur.get('cont'):
            cur['w'] += clean_word(w); cur['raw'] += w.replace(' ', '')
            cur['cont'] = bool(re.search(r'[A-Za-z]\s*[—–\-=]\s*$', w))
            if good: cur['gs'] += gs
            else: cur['ok'] = False
            continue
        flush()
        cont = bool(re.search(r'[A-Za-z]\s*[—–\-=]\s*$', w))
        cur = dict(loc=f"{r['frame']}-{r['line']}:{r['span_no']}", w=clean_word(w), raw=re.sub(r'\s*[—–\-=]\s*$', '', w), gs=gs if good else [], ok=good, cont=cont)
    flush()


def load_words():
    words = []
    for r in csv.DictReader((ROOT / 'output/tunis_known_plaintext_2026-11-10/tunis_word_spans.tsv').open(), delimiter='\t'):
        if r['flag']: continue
        gs = [tok(x) for x in r['groups'].split('-')]
        if all(gs): words.append(('tunis', r['n'], norm(r['word']), gs))
    for r in csv.DictReader((ROOT / 'output/tunis_known_plaintext_2026-11-10/tunis_postscript_spans_v2.tsv').open(), delimiter='\t'):
        if r['flag']: continue
        gs = [tok(x) for x in r['groups'].split('-')]
        if all(gs): words.append(('tunis-ps', r['n'], norm(r['word']), gs))
    # Lear: join a word broken at a line end ("specu=" + "lations")
    rows = list(csv.DictReader((ROOT / 'output/lear1813_retranscription_2026-11-10/lear1813_spans.tsv').open(), delimiter='\t'))
    LEARFIX = {'report': 'reply', 'generally': 'fully'}       # the edition's corrections of Graham's interlines
    # unglossed groups that follow a word may belong to it: keep them as an extension candidate
    trailing = {}
    for i, r in enumerate(rows):
        if r['kind'].strip() == 'interlinear':
            ext = []
            for r2 in rows[i + 1:]:
                if r2['kind'].strip() != 'none': break
                g2 = [tok(x) for x in r2['groups'].split()]
                if not g2 or not all(g2): ext = None; break
                ext += g2
            if ext: trailing[f"{r['line']}:{r['span_no']}"] = ext
    pend = None
    for r in rows:
        if r['kind'].strip() != 'interlinear':
            pend = None; continue
        gs = [tok(x) for x in r['groups'].split()]
        ok = r['placement'].strip() == 'clear' and gs and all(gs)
        w = r['interlinear'].strip()
        cont = w.endswith('=') or w.endswith('-')
        if pend is not None:
            if ok:
                pend = (pend[0], pend[1] + clean_word(w), pend[2] + gs)
                if not cont:
                    words.append(('lear', pend[0], pend[1], pend[2])); pend = None
            else:
                pend = None
            continue
        if not ok: continue
        if cont: pend = (f"{r['line']}:{r['span_no']}", clean_word(w), gs)
        elif clean_word(w):
            cw = clean_word(w)
            words.append(('lear', f"{r['line']}:{r['span_no']}", LEARFIX.get(cw, cw), gs))
    load_interlined(ROOT / 'output/pinckney1795_code16_2026-11-10/spans.tsv', 'p1795', words)
    load_interlined(ROOT / 'output/eaton_1801_2026-11-10/spans.tsv', 'e1801', words)
    load_interlined(ROOT / 'output/code16_extension_2026-11-11/spans.tsv', 'p1795b', words)
    return words, trailing


def main():
    vocab = fs.load_vocab(ROOT / 'sources/raw/weber_ill_2026-11-10/weber_1600_family_vocab.txt')
    words, trailing = load_words()
    direct = collections.defaultdict(collections.Counter); dsrc = collections.defaultdict(set)
    for src, loc, w, gs in words:
        if len(gs) == 1 and gs[0][1] == '':
            direct[gs[0][0]][w] += 1; dsrc[gs[0][0]].add(src)
    fixed, direct_conflicts = {}, []
    for g, c in direct.items():
        top = c.most_common()
        if len(top) > 1:
            direct_conflicts.append((g, dict(c), sorted(dsrc[g])))
            if top[0][1] == top[1][1]: continue            # tie: do not fix
        if top[0][0] in vocab or top[0][1] >= 2:           # a lone off-list value is not taken as settled
            fixed[g] = top[0][0]
    # the same element under two numbers: keep the better attested, set the other aside for an image check
    own = collections.defaultdict(list)
    for g, v in fixed.items(): own[v].append(g)
    set_aside = []
    for v, gs in own.items():
        if len(gs) > 1:
            gs.sort(key=lambda g: -sum(direct[g].values()))
            best = sum(direct[gs[0]].values())
            for g in gs[1:] if best > sum(direct[gs[1]].values()) else gs:
                set_aside.append((g, v, sum(direct[g].values()), sorted(dsrc[g]), gs[0])); fixed.pop(g)
    # Lear words that do not cut on their own groups are retried with the unglossed groups after them
    ext_used = []
    new = []
    for src, loc, w, gs in words:
        if src == 'lear' and loc in trailing and not fs.cuts(w, gs, {g: {v} for g, v in fixed.items()}, vocab):
            g2 = gs + trailing[loc]
            if fs.cuts(w, g2, {g: {v} for g, v in fixed.items()}, vocab):
                ext_used.append((loc, w, len(trailing[loc]))); gs = g2
        new.append((src, loc, w, gs))
    words = new
    multi = [x for x in words if len(x[3]) > 1 or x[3][0][1] or x[3][0][0] not in fixed]
    dom, failures, log = fs.solve(multi, vocab, fixed)
    solved = {g: next(iter(s)) for g, s in dom.items() if len(s) == 1 and g not in fixed}
    owners = collections.defaultdict(list)
    for g, v in list(fixed.items()) + list(solved.items()): owners[v].append(g)
    dup = {e: sorted(gs) for e, gs in owners.items() if len(gs) > 1}
    # drop solved values that collide with a direct value's element
    occ0 = collections.Counter(g for _, _, _, gs in multi for g, _ in gs)
    for e, gs in dup.items():
        if any(g in fixed for g in gs):
            for g in gs: solved.pop(g, None)
        else:                                               # two solved groups with one element: keep neither unless one is clearly better attested
            gs2 = sorted(gs, key=lambda g: -occ0[g])
            for g in (gs2[1:] if occ0[gs2[0]] >= 3 and occ0[gs2[0]] > occ0[gs2[1]] else gs2): solved.pop(g, None)
    key = {}
    for g, v in fixed.items(): key[g] = (v, 'D', sum(direct[g].values()), ' '.join(sorted(dsrc[g])))
    occ = collections.Counter(g for _, _, _, gs in multi for g, _ in gs)
    for g, v in solved.items(): key[g] = (v, 'S', occ[g], '')
    used = {v for v, *_ in key.values()}
    b_off_list = []
    for r in csv.DictReader((ROOT / 'sources/raw/reconstruction_2026-11-06/repo/targets/legation1788/key.tsv').open(), delimiter='\t'):
        if r['code'] != '16' or not r['group'].isdigit(): continue
        g = int(r['group']); v = norm(re.sub(r'[\[\]?()]', '', r['value']))
        if g in key or not v: continue
        if v in vocab and v not in used:
            key[g] = (v, 'B', int(r['n']), 'bourdeau-c14c822'); used.add(v)
        else:
            b_off_list.append((g, r['value'], r['n']))
    p = OUT / 'code16_key_v3.tsv'
    with p.open('w') as f:
        f.write('group\tvalue\tgrade\tn\tsources\ton_element_list\n')
        for g in sorted(key):
            v, gr, n, s = key[g]
            f.write(f"{g}\t{v}\t{gr if gr != 'S' else ('S2' if n >= 2 else 'S1')}\t{n}\t{s}\t{'y' if v in vocab else 'n'}\n")
    grades = collections.Counter(v[1] for v in key.values())
    summary = dict(words=len(words), by_source=dict(collections.Counter(w[0] for w in words)), multi_group_words=len(multi),
                   key_groups=len(key), grades=dict(grades), direct_on_list=sum(1 for g in fixed if fixed[g] in vocab), direct_total=len(fixed),
                   direct_conflicts=direct_conflicts, duplicate_elements=dup, set_aside_direct=set_aside, lear_words_extended=len(ext_used), unsegmentable=len(failures),
                   bourdeau_values_not_entered=len(b_off_list), sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    (OUT / 'code16_key_v3_summary.json').write_text(json.dumps(summary, indent=1, default=str) + '\n')
    with (OUT / 'code16_v3_unsegmentable.tsv').open('w') as f:
        f.write('source\tlocator\tword\tgroups\n')
        for s, l, w, gs in failures: f.write(f"{s}\t{l}\t{w}\t{'-'.join(f'{g}{m}' for g, m in gs)}\n")
    with (OUT / 'bourdeau_values_not_entered.tsv').open('w') as f:
        f.write('group\tbourdeau_value\tn\tour_value\n')
        for g, v, n in b_off_list: f.write(f"{g}\t{v}\t{n}\t{key[g][0] if g in key else ''}\n")
    print(json.dumps({k: v for k, v in summary.items() if k not in ('direct_conflicts',)}, indent=1, default=str))
    print('direct conflicts:', direct_conflicts)
    print('unsegmentable sample:', [(s, w, '-'.join(f'{g}{m}' for g, m in gs)) for s, l, w, gs in failures][:40])


if __name__ == '__main__':
    main()
