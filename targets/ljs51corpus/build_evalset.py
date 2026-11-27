"""Build eval_set.json from the transcription agents' chain records (chains_*.jsonl).

    python build_evalset.py            # writes eval_set.json and prints a summary

Each chain gives the pages and line ranges of a cipher block and the sign counts per line counted on the master.
The records differ in how the counts were made, so every chain gets a tier:

  eye        counted by eye on the master (chains_0054_0077, chains_0078_0101, 22v.9)
  checked    segment.py counts corrected on its overlay, or by eye, +-2..6 per chain (chains_0006_0029)
  segmenter  segment.py counts (with forced-cipher lines) taken as they came (chains_0030_0053 except 22v.9):
             these measure agreement with the old segmenter, not truth, and are reported apart
  rough      a rough estimate (+-8): chain total only, not scored per line (1r.2, 1v.3)

Per-line counts are kept only when they are by eye: in chains_0054_0077 `signs_per_line` mixes segmenter and eye
counts, so a chain's per-line list is used only if it adds up to the by-eye total (`signs_corrected_by_eye`), or the
record has no correction and says the lines were counted by eye.  Otherwise only the chain total is scored.
Per-line divider counts exist only for blocks without dividers (22v.9, 31v.11: 0 on every line); elsewhere dividers
are scored per chain.  Line numbers are segment.py line indices (every text line counts), as the records use them;
where a record says the segmenter's indices differ from its page lines, the override below gives the indices.
The test set is chains_0078_0101 (held out); the other three files are the tuning set.
"""
import json, ast, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = [('chains_0006_0029.jsonl', 'tune'), ('chains_0030_0053.jsonl', 'tune'),
         ('chains_0054_0077.jsonl', 'tune'), ('chains_0078_0101.jsonl', 'test')]

# chain -> {image: [segment.py line indices]} where the record's page line numbers are not the segmenter's indices
LINE_OVERRIDE = {
    '4r.9': {12: [9, 11, 12, 13]},            # rows on l.9, 11, 12, 13 (l.10 is Arabic)
    '8v.10': {21: [9, 10, 11, 12, 13]},       # 'segmenter lines 9-13'
    '9r.7': {22: [6, 7, 8, 9, 10, 11]},       # 'segmenter lines 6-11'
    '9v.3': {23: [3, 4, 5, 6, 7, 8, 9]},      # 'segmenter lines 3-9'
    '12r.8': {28: [6, 7, 8, 9, 10, 11, 12]},  # 'segmenter lines 6-12'
    '36r.11': {76: []},                       # 36r l.11-13 repeat 36v l.1-3, counted once (on 36v)
    '35r.6': {74: [5, 6, 7, 8, 9, 10]},       # counted by eye on page lines 6-11 = segmenter lines 5-10 (the overlay of
                                              # image 74 shows four Arabic lines above the block, so l.6 is index 5)
}
# chains whose by-eye per-line counts copy the old segmenter's overlay (27v.3: 'on the overlay the signs are clean',
# counts equal to segment.py v1 line by line, including a facing-page box at the left of every line)
TIER_OVERRIDE = {'27v.3': 'checked'}
# chains whose per-line list has one extra entry that is not a text line (margin column), dropped per line
DROP_LAST_LINE = {'31v.11'}
# per-line lists that are by eye although they differ by one from the total (a margin sign outside the lines)
PERLINE_OK = {'34v.6', '35v.8'}
# per-line lists from the segmenter whose errors cancel in the total (29r.4: 'by eye 55 after offsetting its errors')
PERLINE_BAD = {'29r.4'}


def lit(v):
    if v is None or isinstance(v, (int, list, dict)):
        return v
    try:
        return ast.literal_eval(v)
    except Exception:
        return v


def tier_of(fn, r):
    cid = r['chain_id']
    if fn.startswith('chains_0006'):
        return 'rough' if cid in ('1r.2', '1v.3') else 'checked'
    if fn.startswith('chains_0030'):
        return 'eye' if cid == '22v.9' else 'segmenter'
    return 'eye'


def image_no(p):
    im = p['image']
    return int(str(im).split('_')[-1]) if isinstance(im, str) else int(im)


def build():
    chains = []
    for fn, split in FILES:
        for ln in open(os.path.join(HERE, fn), encoding='utf8'):
            if not ln.strip():
                continue
            r = json.loads(ln)
            cid = r['chain_id']
            pages = lit(r['pages'])
            spl = lit(r.get('signs_per_line'))
            st = lit(r.get('signs_total'))
            se = lit(r.get('signs_corrected_by_eye'))
            dt = lit(r.get('dividers_total'))
            de = lit(r.get('dividers_corrected_by_eye'))
            tier = TIER_OVERRIDE.get(cid, tier_of(fn, r))
            sig_tot = se if isinstance(se, int) else st
            div_tot = de if isinstance(de, int) else dt
            slots = []                                  # (image, line index) in reading order
            for p in pages:
                note = str(p.get('note', ''))
                if re.search(r'plaintext (only|line)', note):
                    continue
                im = image_no(p)
                ov = LINE_OVERRIDE.get(cid, {})
                if im in ov:
                    idx = ov[im]
                else:
                    a, b = p.get('segmenter_lines') or p['lines']
                    idx = list(range(a, b + 1))
                slots += [(im, i) for i in idx]
            lines = None
            why = ''
            if isinstance(spl, list) and spl and all(isinstance(x, int) for x in spl) and tier != 'rough':
                s = list(spl)
                if cid in DROP_LAST_LINE:
                    s = s[:-1]
                if len(s) != len(slots):
                    why = 'per-line list (%d) does not match the line ranges (%d)' % (len(s), len(slots))
                elif cid in PERLINE_BAD:
                    why = 'per-line counts are segmenter counts with cancelling errors'
                elif fn.startswith('chains_0054') and isinstance(se, int) and sum(s) != se and cid not in PERLINE_OK:
                    why = 'per-line counts are partly segmenter counts (sum %d, by eye %d)' % (sum(s), se)
                else:
                    zero_div = div_tot == 0
                    lines = [dict(image=im, line=li, signs=c, dividers=0 if zero_div else None)
                             for (im, li), c in zip(slots, s)]
            else:
                why = 'no per-line counts'
            chains.append(dict(chain_id=cid, file=fn, split=split, tier=tier, signs_total=sig_tot,
                               dividers_total=div_tot, slots=[list(x) for x in slots], lines=lines,
                               per_line_note=why))
    return chains


if __name__ == '__main__':
    ch = build()
    with open(os.path.join(HERE, 'eval_set.json'), 'w', encoding='utf8') as f:
        json.dump(dict(chains=ch), f, indent=1, ensure_ascii=False)
    from collections import Counter
    print('chains', len(ch), Counter((c['split'], c['tier']) for c in ch))
    print('with per-line counts', sum(1 for c in ch if c['lines']), 'lines', sum(len(c['lines']) for c in ch if c['lines']))
    for c in ch:
        if not c['lines']:
            print('  total only: %-8s %-9s %s' % (c['chain_id'], c['tier'], c['per_line_note']))

