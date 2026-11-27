"""Word-by-word strict count of a system A letter: the key applied to the cipher, set against the decipherment of the time.

usage (from targets/duben1764/):
  python3 -I sysA_1616/close1616/scripts/strict_align.py <letter> <key.json> [<additions.json>] [--json out.json]
  <letter> is 1764-03-06 or 1765-11-15.

What it does, with nothing tuned on the result:
1. Cipher: the number groups of the transcription in order (tx/c1764-03-06.txt, or the C lines of tx/g1765-11-15.txt).
   Groups below 100 are nulls; 100, 400 and 508 carry an empty value in key_c01 and are dropped too (as sysA_place.py).
   A group marked '?' in the transcription is kept and flagged.
2. Witness: the decipherment of the time, as words (6 Mar: the clear 102R.01-103L.08, struck words out, insertions in;
   15 Nov: the G lines of the gloss in order, its abbreviations "L: L: M: M:" and "St" written out as "Leurs Majestés"
   and "Saint", as the cipher spells them; the T lines are clear text of the letter and are not cipher words).
   Words are runs of letters, as research/reading_audit/v10_relabel.py counts them (d'avoir = 2 words).
3. A monotone alignment (dynamic programming) of the groups' key values with the witness letters (a-z, accents
   stripped). Costs: a key value equal to its letters 0; a key value against other letters, edit distance + 0.5;
   a group with no value takes 0-8 letters at 0.6 + 0.15 per letter (1.0 for none); a witness letter with no group 1.0.
   For 6 Mar the end of the witness is free (the cipher stops at 103L.08).
4. Each witness word is classed from the groups that cover its letters:
   sure        every letter given by a group whose key value is exactly those letters, or the same word under two
               stated spelling conventions (y = i; a value spelling in full a word the witness elides, de / d');
   [restored]  some letters under a group with no value in the key, or under no group: the witness supplies them;
   {probable}  some letters under a group whose key value gives other letters (a gap between key and witness).
   ('irresolved' is left to the reading: the script never produces it.)
Additions (optional second key file, {"values": {"group": {"value": ...}}}) are read as key values with their own
tag, so that words resting on them can be counted apart; an addition for a group that key_c01 already values replaces
that value for this count only (key_c01.json is not changed).
"""
import json, re, sys, unicodedata

WORD = re.compile(r'[^\W\d_]+')
# line-end dashes of the gloss that close a word rather than split one (124R.08 "j'ai-" / "prise", 124R.11
# "malheureuses-" / "et"); the other line-end hyphens of the gloss (desagre-able, mena-ger, Raffer-missant) split a word
NOT_SPLIT = {"j'ai", 'malheureuses'}
ELIDED = {'d', 'l', 'qu', 'n', 'm', 's', 'j', 'c'}  # French words written elided before a vowel


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return re.sub(r'[^a-z]', '', s)


def clear_words_1764(path):
    """Witness words of 6 Mar 1764 with their line labels; [?] flags the word before it."""
    words = []
    lines = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        lab, _, body = line.rstrip('\n').partition(' ')
        if '[archivist note]' in body:
            continue
        lines.append((lab, body))
    # join hyphenation / '=' / trailing apostrophe across lines
    text = []
    for lab, body in lines:
        body = re.sub(r'\[del:[^\]]*\](\[\?\])?', '', body)
        body = re.sub(r'\{ins:([^}]*)\}', r'\1', body)
        text.append((lab, body))
    out = []
    carry = ''
    carry_lab = None
    for lab, body in text:
        toks = body.split()
        for ti, t in enumerate(toks):
            doubt = '[?]' in t
            t2 = t.replace('[?]', '')
            if carry:
                t2 = carry + t2
                lab_use = carry_lab
                carry = ''
            else:
                lab_use = lab
            if ti == len(toks) - 1 and (t2.endswith('-') or t2.endswith('=')) and len(t2) > 1:
                carry, carry_lab = t2[:-1], lab_use
                continue
            for w in WORD.findall(t2):
                out.append({'w': w, 'line': lab_use, 'doubt': doubt})
    return out


def clear_words_1765(path):
    out = []
    carry, carry_lab = '', None
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        lab, _, body = line.rstrip('\n').partition(' ')
        if not lab.endswith('G') or body.strip() == '-':
            continue
        # the glossator's abbreviations, written out as the cipher spells them (125R.11: 581 sa + 365 int = Saint)
        body = body.replace('L: L: M: M:', 'Leurs Majestés').replace('St André', 'Saint André')
        toks = body.split()
        for ti, t in enumerate(toks):
            if t == '-':
                continue
            if carry:
                t, lab_use, carry = carry + t, carry_lab, ''
            else:
                lab_use = lab[:-1]
            if ti == len(toks) - 1 and t.endswith('-') and len(t) > 1 and t[:-1] not in NOT_SPLIT:
                carry, carry_lab = t[:-1], lab_use
                continue
            for w in WORD.findall(t):
                out.append({'w': w, 'line': lab_use, 'doubt': False})
    return out


def cipher_groups(path, only_c):
    gs = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        lab, _, body = line.rstrip('\n').partition(' ')
        if only_c and not lab.endswith('C'):
            continue
        if only_c:
            lab = lab[:-1]
        body = re.sub(r'\[del:[^\]]*\]', '', body)
        for t in re.split(r'[\s.|]+', body):
            if not re.search(r'\d', t):
                if '???' in t:
                    gs.append({'g': '???', 'line': lab, 'doubt': True})
                continue
            g = re.sub(r'[^0-9]', '', t)
            gs.append({'g': str(int(g)), 'raw': t, 'line': lab, 'doubt': '?' in t})
    return gs


def lev(a, b):
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


ELIDABLE = {'de', 'le', 'la', 'que', 'ne', 'me', 'se', 'je', 'ce'}


def same(seg, v, j1, ends):
    """Stated spelling conventions, counted as the key giving the word: y = i (roi / Roy), and a key value that
    spells in full a word the witness elides (de / d', que / qu': the value ends one vowel after a witness word
    that is elided, j1 being that word's end)."""
    if seg.replace('y', 'i') == v.replace('y', 'i'):
        return True
    if v in ELIDABLE and v[:-1] == seg and j1 in ends:
        return True
    return False


def align(vals, clear, free_end, ends=frozenset()):
    """vals: list of (value or None). Returns per-group (j0, j1, kind) and per-letter owner."""
    n, m = len(vals), len(clear)
    INF = float('inf')
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    for j in range(1, m + 1):
        D[0][j] = D[0][j - 1] + 1.0
        B[0][j] = ('skip', 0)
    cache = {}
    for i in range(1, n + 1):
        v = vals[i - 1]
        Di, Dp, Bi = D[i], D[i - 1], B[i]
        for j in range(0, m + 1):
            best, bp = INF, None
            if j > 0 and Di[j - 1] + 1.0 < best:
                best, bp = Di[j - 1] + 1.0, ('skip', 0)
            if v is None:
                for L in range(0, 9):
                    if L > j:
                        break
                    c = Dp[j - L] + (1.0 if L == 0 else 0.6 + 0.15 * L)
                    if c < best:
                        best, bp = c, ('unk', L)
            else:
                lv = len(v)
                for L in range(max(0, lv - 2), lv + 3):
                    if L > j:
                        break
                    if Dp[j - L] == INF:
                        continue
                    seg = clear[j - L:j]
                    if seg == v:
                        c = Dp[j - L]
                        kind = 'exact'
                    elif same(seg, v, j, ends):
                        c = Dp[j - L] + 0.05
                        kind = 'conv'
                    else:
                        key = (seg, v)
                        if key not in cache:
                            cache[key] = lev(seg, v)
                        c = Dp[j - L] + cache[key] + 0.5
                        kind = 'mis'
                    if c < best:
                        best, bp = c, (kind, L)
            Di[j], Bi[j] = best, bp
    j = m
    if free_end:
        j = min(range(m + 1), key=lambda jj: D[n][jj])
    end = j
    i = n
    spans = [None] * n
    owner = [None] * m  # (group index, kind) per letter
    while i > 0 or j > 0:
        kind, L = B[i][j]
        if kind == 'skip':
            j -= 1
            continue
        spans[i - 1] = (j - L, j, kind)
        for q in range(j - L, j):
            owner[q] = (i - 1, kind)
        i -= 1
        j -= L
    return spans, owner, end, D[n][end]


def main():
    args = sys.argv[1:]
    out_json = None
    if '--json' in args:
        k = args.index('--json')
        out_json = args[k + 1]
        del args[k:k + 2]
    letter, keyf = args[0], args[1]
    addf = args[2] if len(args) > 2 else None
    key = {g: (v[0] if v else '') for g, v in json.load(open(keyf)).items()}
    add = {}
    if addf:
        a = json.load(open(addf))
        add = {g: (e['value'] if isinstance(e, dict) else e[0]) for g, e in a.get('values', a).items()}
    if letter == '1764-03-06':
        words = clear_words_1764('tx/p1764-03-06.txt')
        groups = cipher_groups('tx/c1764-03-06.txt', False)
        free_end = True
    else:
        words = clear_words_1765('tx/g1765-11-15.txt')
        groups = cipher_groups('tx/g1765-11-15.txt', True)
        free_end = False
    groups = [g for g in groups if g['g'] == '???' or (int(g['g']) >= 100 and g['g'] not in ('100', '400', '508'))]
    vals, src = [], []
    for g in groups:
        if g['g'] in add and add[g['g']]:  # an addition, or a value that replaces key_c01's
            vals.append(norm(add[g['g']])); src.append('add')
        elif g['g'] in key and key[g['g']] != '':
            vals.append(norm(key[g['g']])); src.append('key')
        else:
            vals.append(None); src.append(None)
    clear, wpos = '', []
    for w in words:
        n = norm(w['w'])
        wpos.append((len(clear), len(clear) + len(n)))
        clear += n
    ends = {b for w, (a, b) in zip(words, wpos) if norm(w['w']) in ELIDED}
    spans, owner, end, cost = align(vals, clear, free_end, ends)
    res = []
    for wi, (w, (a, b)) in enumerate(zip(words, wpos)):
        if a >= end:
            cls = 'outside'
            gi = []
        else:
            own = owner[a:b]
            gi = sorted({o[0] for o in own if o})
            kinds = [o[1] if o else 'none' for o in own]
            srcs = {src[o[0]] for o in own if o and o[1] == 'exact'}
            srcs |= {src[o[0]] for o in own if o and o[1] == 'conv'}
            if all(k in ('exact', 'conv') for k in kinds):
                cls = 'sure_add' if 'add' in srcs else 'sure'
            elif any(k == 'mis' for k in kinds):
                cls = 'probable'
            else:
                cls = 'restored'
        res.append({'i': wi, 'w': w['w'], 'line': w['line'], 'doubt_witness': w['doubt'], 'class': cls,
                    'groups': [groups[g]['g'] + ('?' if groups[g]['doubt'] else '') for g in gi],
                    'values': [vals[g] for g in gi], 'gi': gi})
    counts = {}
    for r in res:
        counts[r['class']] = counts.get(r['class'], 0) + 1
    gl = []
    for gi, (g, v, s) in enumerate(zip(groups, vals, spans)):
        j0, j1, kind = s
        gl.append({'gi': gi, 'g': g['g'], 'doubt': g['doubt'], 'line': g['line'], 'value': v, 'src': src[gi],
                   'kind': kind, 'witness': clear[j0:j1], 'j0': j0, 'j1': j1})
    summary = {'letter': letter, 'groups': len(groups), 'witness_letters_aligned': end, 'cost': round(cost, 2),
               'counts': counts}
    print(json.dumps(summary, ensure_ascii=False))
    if out_json:
        json.dump({'summary': summary, 'words': res, 'groups': gl}, open(out_json, 'w'), ensure_ascii=False, indent=0)


if __name__ == '__main__':
    main()
