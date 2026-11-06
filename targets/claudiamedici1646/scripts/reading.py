"""Check the marked readings of 2354 against the mechanical decryptions and count words. Standard library only.

    python reading.py check

reading_<doc>.md holds a fenced block ```marked ... ``` with one 'Lnn: text' line per transcription line.
Marks: {x/y} = the signs give x, read y;  {+a} = letter a added;  {-a} = letter a given by the signs, dropped;
{?x} = the signs give x only from a sign whose shape is near, not equal to, the key's sign (the decryption prints
it '(x)'; every '(x)' of a line must be marked {?x}, in order);
[?guess=mech] = guess for a stretch whose signs give mech;  [...] = hole (only where the signs give '?').
Comparison ignores case, accents, spaces, apostrophes, punctuation and hyphens, and treats v as u.
Plain script in <...> must be identical in reading and decryption.

Word classes: verbatim (no mark), doubtful sign ({?x}), repaired ({x/y}, {+a}, {-a}), guess ([?...]), hole.
Code groups ([Re], [V.E.] ...) are counted as cipher words, since their values come from glosses on sibling
letters; the verbatim share without them is printed as well.
"""
import pathlib
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ['24793', '24800']
DOUBT = re.compile(r'\{\?([^{}]*)\}')
REPAIR = re.compile(r'\{(?!\?)')


def norm(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower().replace('v', 'u')
    return re.sub(r"[^a-z\[\]?]", '', s)


def to_mech(marked):
    s = DOUBT.sub(r'\1', marked)
    s = re.sub(r'\{([^/{}]*)/([^/{}]*)\}', r'\1', s)
    s = re.sub(r'\{\+[^{}]*\}', '', s)
    s = re.sub(r'\{-([^{}]*)\}', r'\1', s)
    s = re.sub(r'\[\?[^=\]]*=([^\]]*)\]', r'\1', s)
    s = s.replace('[...]', '?')
    return s


def split_plain(line):
    plain = re.findall(r'<[^>]*>', line)
    rest = re.sub(r'<[^>]*>', ' ', line)
    return plain, rest


def words(rest):
    toks, buf, depth = [], '', 0
    for ch in rest:
        if ch in '[{':
            depth += 1
        elif ch in ']}':
            depth -= 1
        if ch.isspace() and depth == 0:
            if buf:
                toks.append(buf)
            buf = ''
        else:
            buf += ch
    if buf:
        toks.append(buf)
    return toks


def category(w):
    if '[...]' in w or '?' in norm(to_mech(w)).replace('[?', ''):
        return 'hole'
    if '[?' in w:
        return 'guess'
    if REPAIR.search(w):
        return 'repaired'
    if DOUBT.search(w):
        return 'doubtful'
    return 'verbatim'


RANK = ['verbatim', 'doubtful', 'repaired', 'guess', 'hole']


def check_doc(doc):
    dec = {}
    for line in open(ROOT / f'decryption_{doc}.txt', encoding='utf-8'):
        m = re.match(r'(L\d+):\s*(.*)$', line.rstrip('\n'))
        if m:
            dec[m.group(1)] = m.group(2)
    text = (ROOT / f'reading_{doc}.md').read_text(encoding='utf-8')
    block = re.search(r'```marked\n(.*?)```', text, re.S).group(1)
    ok = True
    cnt = dict(verbatim=0, doubtful=0, repaired=0, guess=0, hole=0)
    codes = 0
    seen = set()
    joined_prev = False
    last_cat = 'verbatim'
    for line in block.splitlines():
        m = re.match(r'(L\d+):\s*(.*)$', line)
        if not m:
            continue
        lid, marked = m.groups()
        seen.add(lid)
        if lid not in dec:
            print(f'FAIL {doc} {lid}: no such line in decryption'); ok = False; continue
        pr, rr = split_plain(marked)
        pd, rd = split_plain(dec[lid])
        if pr != pd:
            print(f'FAIL {doc} {lid}: plain script differs: {pr} vs {pd}'); ok = False
        if norm(to_mech(rr)) != norm(rd):
            print(f'FAIL {doc} {lid}: unmarked departure\n  reading -> {norm(to_mech(rr))}\n  signs   -> {norm(rd)}'); ok = False
        if re.findall(r'\(([^()]*)\)', rd) != DOUBT.findall(rr):
            print(f'FAIL {doc} {lid}: doubtful sign shape(s) {re.findall(r"[(][^()]*[)]", rd)} not marked {{?x}} in order')
            ok = False
        ws = words(rr)
        for i, w in enumerate(ws):
            if i == 0 and joined_prev:
                # second half of a word split at the line end: counted once, with the worse category of the two halves
                c2 = category(w)
                if RANK.index(c2) > RANK.index(last_cat):
                    cnt[last_cat] -= 1; cnt[c2] += 1; last_cat = c2
                continue
            last_cat = category(w)
            if last_cat == 'verbatim' and w.startswith('[') and not w.startswith('[?'):
                codes += 1
            cnt[last_cat] += 1
        last = ws[-1] if ws else ''
        joined_prev = last.endswith('-') and not rr.rstrip().endswith('>')
    missing = set(dec) - seen
    if missing:
        print(f'FAIL {doc}: lines missing from reading: {sorted(missing)}'); ok = False
    tot = sum(cnt.values())
    v = cnt['verbatim']
    print(f'{doc}: {tot} cipher words: {v} verbatim from the signs, {cnt["doubtful"]} with a doubtful sign shape, '
          f'{cnt["repaired"]} with a marked repair, {cnt["guess"]} guesses, {cnt["hole"]} holes; '
          f'verbatim share {v}/{tot} = {100 * v / tot:.1f}%; '
          f'without the {codes} code groups {v - codes}/{tot - codes} = {100 * (v - codes) / (tot - codes):.1f}%')
    return ok


if __name__ == '__main__':
    good = all([check_doc(d) for d in DOCS])
    print('PASS' if good else 'FAIL')
    sys.exit(0 if good else 1)
