"""Look up the code groups of /49, /212 and /217 in Entick's New Spelling Dictionary (setting of the Internet Archive
copy ..._1795_0) and compare each value with this folder's 1798 table and proposals.

Rule: a group p,n is printed page p, printed line n (column a lines 1..k, continuation lines counted; column b goes
on from k + 1; k = 39 on almost every page). A third number k picks the k-th word of the line, part-of-speech
abbreviations not counted. On the name pages 442-443 (five columns) n is instead the n-th name on the page, down
the columns in turn, letter headings and blank rows not counted (found after the fact; entick_lines.tsv already holds
those rows by that count). The lines are in entick_lines.tsv (blind line counts of the page images; only the lines
the letters use, each with the line before and after), so nothing here needs the page images.

Inputs: entick_lines.tsv; ct_49_reread.txt and ct_212_reread.txt (blind re-readings of the digits, group boundaries
as in ct_49.txt / ct_212.txt; a trailing ? marks a group the readers left doubtful, kept with the digits of the
earlier transcription); ct_217.txt as it stands (not re-read); align_1798.tsv for the /49 words of the clear copy /51;
table_1798.tsv, proposals.tsv and apply.py's LETTERS_1802 for this folder's values in /212 and /217.

Writes entick_49.tsv, entick_212.tsv, entick_217.tsv (group by group: the dictionary line, the value used, this
folder's value and grade, the status), reading_49_entick.txt, reading_212_entick.txt, reading_217_entick.txt
(running text), cipher_words_49.tsv, cipher_words_212.tsv, cipher_words_217.tsv (read share by cipher words),
entick_217_suggest.tsv (/217 groups that fail as written and fit with one 2 read as 4) and
prints the counts. Standard library only; the output is the same byte for byte on every run.

    python targets/jones1802/entick.py
"""
import collections
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from apply import LETTERS_1802, load_proposals, load_table  # noqa: E402

SUFFIXES = {'ing', 'ed', 'es', 'est', 'o', 's', 'd'}
OVERRIDES = {'169,25': 'government', '327,66': 'said'}  # align.py's OVERRIDES
POS = {'v', 'a', 's', 'f', 'ad', 'pr', 'prep', 'pret', 'part', 'conj', 'interj', 'pron', 'n', 'pl'}
# Dictionary words that do not make sense in place. Kept in entick_<n>.tsv; in the readings they are marked
# [?word] and counted as holes. Probably a digit or a count problem; not resolved. Listed after the fact.
NOT_SENSE = {'180,31': 'Heresy for January? (doubtful re-reading: R1 read 188, R2 and R3 180)',
             '166,71': 'Glaver for difficulty? (doubtful re-reading of 106,71)',
             '160,30': 'Fugitive for General? (164,30 elsewhere)', '394,33': 'Trode for troops?',
             '387,24': 'Toad for to', '156,57': 'Fortunateness for fortnight?', '237,18': 'Mercifully for messenger?',
             '221,25': 'Levigate for letter? (Letter is 221,5)', '433,25': 'Where for whom?',
             '160,73': 'Fun for functions? (Function is the next line)',
             # /217 (digits not re-read)
             '221,15': 'Level for letter? (Letter is 221,5)', '249,61': 'Nameless for name? (Name is the next line)',
             '138,31': 'Exhorter(+d) for expelled?', '139,13': 'Expence for express?',
             # both letters: the line is Can ("v. n. to be able" / "s. a vessel"); Khan only by sound
             '50,66': 'Can for Khan, by sound only'}


# ---------- text matching (the same rules as the test of 15 Nov 2026) ----------

def norm(tok):
    t = unicodedata.normalize('NFKD', tok.replace('ſ', 's'))
    t = ''.join(ch for ch in t if not unicodedata.combining(ch))
    t = re.sub(r"[’'‘`´“”\"^]", '', t)
    t = re.sub(r'[^A-Za-z\-]', '', t)
    return t.lower().replace('-', '')


def roots(w):
    w = w.lower()
    r = {w}

    def add(x):
        if len(x) >= 2:
            r.add(x)
    for suf in ('s', 'es', 'ed', 'd', 'ing', 'ly', 'ness', 'ation'):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            base = w[:-len(suf)]
            add(base)
            add(base + 'e')
            if len(base) >= 2 and base[-1] == base[-2]:
                add(base[:-1])
    for a, b in (('ies', 'y'), ('ied', 'y'), ('ily', 'y'), ('iness', 'y')):
        if w.endswith(a):
            add(w[:-len(a)] + b)
    if w == 'made':
        r.add('make')
    if w == 'had':
        r.add('have')
    if w == 'went':
        r.add('go')
    return r


def ed1(a, b):
    if abs(len(a) - len(b)) > 1 or a == b:
        return a == b
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) <= 1
    if len(a) > len(b):
        a, b = b, a
    return any(b[:i] + b[i + 1:] == a for i in range(len(b)))


def match(word, tok):
    """tok: normalised headword. True if it is the word or one of its roots (one letter's tolerance at 6+ letters)."""
    if not tok:
        return False
    variants = {tok, tok.replace('f', 's')}
    if tok[0] == 'g':
        variants.add('c' + tok[1:])
    for rt in roots(word):
        for v in variants:
            if v == rt or (len(rt) >= 6 and ed1(v, rt)):
                return True
    return False


def variants(word, suf):
    w = word.lower().replace('’', "'")
    out = {w}
    if w.endswith("'s"):
        out.add(w[:-2])
    if suf and w.endswith(suf) and len(w) > len(suf) + 1:
        out |= {w[:-len(suf)], w[:-len(suf)] + 'e'}
    return out


def fits(word, headword, suf=''):
    t = norm(headword.split(' ')[0]) if headword else ''
    return bool(t) and any(match(v, t) for v in variants(word, suf))


def kth(text, k):
    ws = [w for w in re.findall(r"[A-Za-z']+", text) if w.lower().strip('.') not in POS]
    return ws[k - 1] if 0 < k <= len(ws) else None


# ---------- files ----------

def load_lines():
    pages, text, counted = collections.defaultdict(dict), {}, set()
    for row in (HERE / 'entick_lines.tsv').read_text(encoding='utf-8').splitlines():
        if row.startswith('# pages counted:'):
            counted = {int(x) for x in row.split(':', 1)[1].split()}
        if row.startswith('#') or row.startswith('page\t'):
            continue
        p, n, _c, _i, e, w, t = row.split('\t')
        pages[int(p)][int(n)] = (e, w)
        if t:
            text[(int(p), int(n))] = t
    return pages, text, counted


def tokens(path):
    """align.py's cipher_tokens, also keeping folio, manuscript line and a trailing ? (doubtful group)."""
    toks, folio, ln = [], None, 0
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        if line.startswith('# f.'):
            folio, ln = line.split()[2], 0
            continue
        if not line.strip() or line.startswith('#'):
            continue
        ln += 1
        for raw in re.findall(r'\d+(?:,\d+)*\??|[A-Za-z]+|[~+]', line.replace('(', ' ').replace(')', ' ')):
            doubt = raw.endswith('?')
            raw = raw.rstrip('?')
            if raw[0].isdigit() and (',' not in raw or re.fullmatch(r'\d{1,3},\d{3}', raw)):
                toks.append(['w', raw, '', folio, ln, False])
            elif raw[0].isdigit():
                nums = raw.split(',')
                if len(nums) == 4:
                    toks.append(['g', ','.join(nums[:2]), '', folio, ln, doubt])
                    toks.append(['g', ','.join(nums[2:]), '', folio, ln, doubt])
                else:
                    toks.append(['g', raw, '', folio, ln, doubt])
            elif raw.lower() in SUFFIXES and toks and toks[-1][0] == 'g':
                toks[-1][2] = raw.lower()
            else:
                toks.append(['w', raw.lower(), '', folio, ln, False])
    return toks


def positions_49():
    """/49 positions: re-read group, earlier group, the alignment move and the clear-copy word (align_1798.tsv)."""
    theirs, mine = tokens(HERE / 'ct_49.txt'), tokens(HERE / 'ct_49_reread.txt')
    assert len(theirs) == len(mine)
    moves = [l.split('\t') for l in (HERE / 'align_1798.tsv').read_text(encoding='utf-8').splitlines()[1:]]
    out, i = [], 0
    for mv in moves:
        if mv[0] == 'skipp':
            continue
        t, m = theirs[i], mine[i]
        i += 1
        assert (mv[1].split()[0] if mv[1] else '') == t[1], (mv, t)
        word = mv[2] if len(mv) > 2 else ''
        value = OVERRIDES.get(t[1], word) if mv[0] == 'word' else word
        out.append(dict(kind=t[0], folio=m[3], line=m[4], group=m[1], theirs=t[1], suf=t[2], doubt=m[5],
                        move=mv[0], word=word, value=value))
    assert i == len(theirs)
    return out


def positions_1802(name, reread):
    """/212 or /217 positions with this folder's value at each, by apply.py --retry's own order of precedence."""
    words, letters = load_table()
    props = load_proposals()
    theirs = tokens(HERE / f'ct_{name}.txt')
    mine = tokens(HERE / f'ct_{name}_reread.txt') if reread else theirs
    assert len(theirs) == len(mine)
    out = []
    for t, m in zip(theirs, mine):
        g = t[1]
        if t[0] == 'w':
            mv, v = 'clear', g
        else:
            base = ','.join(g.split(',')[:2])
            if g in letters:
                mv, v = '1798l', '[' + letters[g] + ']'
            elif g in LETTERS_1802:
                mv, v = '1802l', '[' + LETTERS_1802[g] + ']'
            elif g in props and props[g][0].startswith('['):
                mv, v = 'H', props[g][0]
            elif g in words or base in words:
                mv, v = '1798w', words.get(g) or words[base]
            elif g in props:
                mv, v = props[g][1], props[g][0]
            else:
                mv, v = 'open', ''
        out.append(dict(kind=t[0], folio=m[3], line=m[4], group=m[1], theirs=g, suf=t[2], doubt=m[5], move=mv,
                        word=v, value=v))
    return out


# ---------- look-up ----------

def look_up(name, pos, pages, ltext, counted):
    rows, run, words, meta, rung = [], [], [], [], []
    stat = collections.Counter()
    letter_at = {}
    if name == '49':  # which letter of the spelled word each letter group stands for
        cur, i = None, 0
        for k, P in enumerate(pos):
            if P['move'] == 'letter':
                if P['word'] != cur or i >= len(P['word']):
                    cur, i = P['word'], 0
                letter_at[k] = P['word'][i]
                i += 1
            else:
                cur, i = None, 0

    def flush():
        if run:
            words.append(''.join(ch[0].lower() if ch.endswith('\0') else ch.upper() for ch in run))
            meta.append(('name', P_at, ' '.join(g for g, _ in rung), sum(1 for _, x in rung if x)))
            run.clear()
            rung.clear()
    P_at = None
    for k, P in enumerate(pos):
        if P['kind'] == 'w':
            flush()
            words.append(P['word'])
            meta.append(('clear', P, '', 0))
            continue
        g, suf, move, theirs = P['group'], P['suf'], P['move'], P['value']
        nums = [int(x) for x in g.split(',')]
        p, n = nums[0], nums[1]
        kk = nums[2] if len(nums) > 2 else None
        L = pages.get(p, {})
        e, hw = L.get(n, ('', ''))
        kword = kth(ltext[(p, n)], kk) if kk and (p, n) in ltext else None
        chosen = kword if kk else (hw if e == 'E' else '')
        grade = (('letter (clear copy)' if move == 'letter' else 'clear copy /51' if move == 'word' else move)
                 if name == '49' else move)
        tw = theirs.strip('[]') if theirs else ''
        is_letter = theirs.startswith('[') or move == 'letter'
        bare2 = len(nums) == 2 and n == 2
        if p not in counted:
            status = 'page not counted'
        elif move == 'skipc':
            status = 'skipped in their alignment'
        elif is_letter:
            if name == '49':
                tw = letter_at.get(k)
                theirs = f"[{tw}] ({P['word']})"
            status = 'letter agrees' if hw and tw and norm(hw)[:1] == tw else 'letter does not fit'
        elif bare2:
            status = 'agrees' if tw and fits(tw, hw, suf) else 'does not fit (bare ,2)'
        elif tw and (fits(tw, chosen or hw, suf) or (kk and kword and fits(tw, kword, suf))):
            status = 'agrees'
        elif tw and (fits(tw, L.get(n - 1, ('', ''))[1], suf) or fits(tw, L.get(n + 1, ('', ''))[1], suf)):
            status = ('agrees within one line' if (name == '49' or move == '1798w') else
                      'corrects theirs (their word is on the next line)' if chosen else
                      'does not fit (continuation line)')
        elif not tw:
            status = 'fills a gap' if chosen else 'does not fit (no headword)'
        elif name == '49':
            status = 'does not fit'
        elif not chosen:
            status = 'does not fit (continuation line)'
        else:
            status = 'corrects theirs'
        if g != P['theirs'] and status in ('agrees', 'agrees within one line'):
            status += ' (re-read digits)'
        if P['doubt']:
            status += ' [doubtful digits]'
        stat[(grade, status.split(' (')[0].split(' [')[0])] += 1
        line_word = hw if e == 'E' else (f'(cont.) {hw}' if hw else '')
        rows.append([P['folio'], str(P['line']), g, P['theirs'], suf, line_word, chosen or '', kword or '',
                     theirs, grade, status])
        # running text
        if status.startswith('letter agrees'):
            if not run:
                P_at = P
            run.append(tw)
            rung.append((g, True))
            continue
        if status.startswith('letter does not fit'):
            if not run:
                P_at = P
            run.append((tw or '?').lower() + '\0')
            rung.append((g, False))
            continue
        flush()
        meta.append(('word', P, g + (f' {suf}' if suf else ''), 0))
        w = ''.join(c for c in unicodedata.normalize('NFKD', chosen or '') if not unicodedata.combining(c))
        w = w.replace("'", '').lower() + (f'+{suf}' if suf else '')
        if status.startswith(('does not fit', 'skipped', 'page not counted')) or not chosen:
            words.append(f'[{g}]')
        elif status.startswith('agrees within one line') or g in NOT_SENSE or P['doubt']:
            words.append(f'[?{w}]')
        else:
            words.append(w)
    flush()
    return rows, words, stat, meta


GRADES = ('# folder_grade: H, M, L = grade in proposals.tsv; 1798w / 1798l = word / letter value of table_1798.tsv; '
          '1802l = letter fixed by the 1802 names (apply.py LETTERS_1802); open = no value; for /49 "clear copy /51" '
          '(word) or "letter (clear copy)"; skipc = the group align.py skipped.\n'
          '# Pages 442-443 (names list): line n = the n-th name on the page, a separate count found after the fact.\n')
HEAD = ['folio', 'ms_line', 'group', 'group_ct', 'suffix', 'dictionary_line_n', 'value', 'third_number_word',
        'folder_value', 'folder_grade', 'status']
NOTE = {
    '49': '/49 (Jones to Dundas, 17 Dec 1798) with the re-read digits (ct_49_reread.txt). The words of the clear copy '
          '/51 test the rule; this is not a new reading of the letter, which is read from /51.',
    '212': "/212 (Karapet's letter, Erzeroum, 20 Nov [1801]) with the re-read digits (ct_212_reread.txt).",
    '217': "/217 (Karapet's letter, Erzeroum, 19 Dec [1801]) with the digits of ct_217.txt as they stand (not re-read).",
}


def cipher_words(name, words, meta):
    """Read share by cipher words (16 Nov 2026 convention): clear words are left out. Each coded word group is one
    word (a three-number group too; a bare ,2 group too); each run of letter groups between clear words is one
    word (a spelled name or a spelled common word), and the parts of a name written with x, + or ~ between them
    count as one word. A word is read when its reading is a plain word: [p,n] and [?word] are holes. A name is
    read when every letter group has a value; the strict column also asks that every letter's dictionary line start
    with that letter. Writes cipher_words_<n>.tsv and returns the counts."""
    items = list(zip(words, meta))
    merged = []  # a name written in parts with x, + or ~ between them (EECH x MIASIN) is one word
    i = 0
    while i < len(items):
        w, m = items[i]
        if m[0] == 'name':
            while (i + 2 < len(items) and items[i + 1][1][0] == 'clear' and items[i + 1][0] in ('x', '+', '~')
                   and items[i + 2][1][0] == 'name'):
                w2, m2 = items[i + 2]
                w = f'{w} {items[i + 1][0]} {w2}'
                m = ('name', m[1], m[2] + ' ' + m2[2], m[3] + m2[3])
                i += 2
        merged.append((w, m))
        i += 1
    out, n, read, strict = [], 0, 0, 0
    for w, (kind, P, groups, nexpl) in merged:
        if kind == 'clear':
            continue
        n += 1
        if kind == 'word':
            ok = not w.startswith('[')
            why = 'read' if ok else ('doubtful: ' + NOT_SENSE[groups.split()[0]] if groups.split()[0] in NOT_SENSE
                                     else 'doubtful' if w.startswith('[?') else 'unread')
            ok_strict = ok
        else:
            ng = len(groups.split())
            ok = '?' not in w
            ok_strict = ok and nexpl == ng
            why = (f'{ng} letter group' + ('s' if ng > 1 else '') +
                   ('' if nexpl == ng else f', {ng - nexpl} not on a line starting with its letter'))
            if not ok:
                why += ', a letter without value'
        read += ok
        strict += ok_strict
        out.append([str(n), P['folio'] or '', str(P['line']), 'spelled' if kind == 'name' else kind, groups, w, 'yes' if ok else 'no',
                    'yes' if ok_strict else 'no', why])
    with open(HERE / f'cipher_words_{name}.tsv', 'w', encoding='utf-8', newline='\n') as o:
        o.write(f'# /{name}: cipher words of reading_{name}_entick.txt (entick.py). Clear words are not counted. One row per '
                'coded word group (three-number and bare ,2 groups included) and per spelled word (a run of letter groups '
                'between clear words; name parts joined by x, + or ~ count as one).\n'
                f'# read share: {read} of {n} = {read / n:.3f}; strict (every letter of a name explained by its dictionary '
                f'line): {strict} of {n} = {strict / n:.3f}.\n')
        o.write('n\tfolio\tms_line\tkind\tgroups\treading\tread\tread_strict\tnote\n')
        for r in out:
            o.write('\t'.join(r) + '\n')
    print(f'/{name} cipher words: read {read} of {n} = {read / n:.3f}; strict {strict} of {n} = {strict / n:.3f}')


def main():
    pages, ltext, counted = load_lines()
    sets = {'49': positions_49(), '212': positions_1802('212', True), '217': positions_1802('217', False)}
    for name, pos in sets.items():
        rows, words, stat, meta = look_up(name, pos, pages, ltext, counted)
        cipher_words(name, words, meta)
        with open(HERE / f'entick_{name}.tsv', 'w', encoding='utf-8', newline='\n') as o:
            o.write(f'# {NOTE[name]} Written by entick.py.\n' + GRADES + '\t'.join(HEAD) + '\n')
            for r in rows:
                o.write('\t'.join(r) + '\n')
        holes = sum(1 for w in words if w.startswith('[') and not w.startswith('[?'))
        doubt = sum(1 for w in words if w.startswith('[?'))
        text = re.sub(r'(.{1,110})(?:\s+|$)', r'\1\n', ' '.join(words))
        with open(HERE / f'reading_{name}_entick.txt', 'w', encoding='utf-8', newline='\n') as o:
            o.write(f'# {NOTE[name]}\n'
                    '# Each code word is the word of its Entick line (entick.py). [p,n] = a group that does not fit '
                    'the rule (one unread word);\n# [?word] = the line gives this word but it is doubtful (within one '
                    'line of the clear word in /49, no sense in place, or doubtful digits). Spelled names are joined '
                    'in capitals;\n# a lowercase letter inside a name is a letter code whose line does not start with '
                    'that letter (value from the spelled names, not explained by the dictionary).\n'
                    f'# Unread groups {holes}, doubtful words {doubt}.\n' + text)
        print(f'/{name}: {len(rows)} groups; unread {holes}; doubtful {doubt}')
        for (grade, status), v in sorted(stat.items()):
            print(f'   {grade}\t{status}\t{v}')
    suggest(sets['217'], pages, counted)


def suggest(pos, pages, counted):
    """/217: groups that do not fit as written but fit with one figure 2 read as 4. Suggestions to check on the
    manuscript; ct_217.txt is not changed."""
    out = []
    for P in pos:
        if P['kind'] != 'g' or not P['value']:
            continue
        g, tw = P['group'], P['value'].strip('[]')
        is_letter = P['value'].startswith('[')

        def ok(gr):
            nums = [int(x) for x in gr.split(',')]
            if nums[0] not in counted or len(nums) > 2:
                return None
            e, hw = pages.get(nums[0], {}).get(nums[1], ('', ''))
            if is_letter:
                return bool(hw) and norm(hw)[:1] == tw
            return e == 'E' and fits(tw, hw, P['suf'])
        if ok(g) is not False:
            continue
        for i, ch in enumerate(g):
            if ch == '2':
                alt = g[:i] + '4' + g[i + 1:]
                if ok(alt):
                    nums = [int(x) for x in alt.split(',')]
                    out.append([P['folio'], str(P['line']), g, alt, P['value'], P['move'],
                                pages[nums[0]][nums[1]][1]])
    with open(HERE / 'entick_217_suggest.tsv', 'w', encoding='utf-8', newline='\n') as o:
        o.write('# /217 groups that do not fit as written (ct_217.txt) and fit with one figure 2 read as 4. Found '
                'after the fact; to be checked on the manuscript. ct_217.txt is not changed.\n')
        o.write('folio\tms_line\tgroup_ct\tgroup_with_4\tfolder_value\tfolder_grade\tdictionary_line_n\n')
        for r in out:
            o.write('\t'.join(r) + '\n')
    print(f'/217 suggestions (2 read as 4): {len(out)}')


if __name__ == '__main__':
    sys.exit(main())
