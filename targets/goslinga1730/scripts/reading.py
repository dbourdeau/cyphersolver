"""Check the marked reading of catalogue 2534 against the mechanical decryption and count words. Standard library only.
    python scripts/reading.py check [doc ...]       (default doc: goslinga1730)

reading_<doc>_marked.md holds a fenced block ```marked ... ``` with one 'Lxx.y: text' line per decryption line.
Marks: {x/y} = the signs give x, read y;  {+a} = letter a added;  {-a} = letter a given by the signs, dropped;
[?guess=mech] = guess for a stretch whose signs give mech;  [#n] = group n not in the key (hole);
[value] = word or name group of the key (counted as a code word).  Clear words of the letter stay in «...» and must be
identical to the decryption. Comparison ignores case, spaces, underscores and punctuation.
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent


def norm(s):
    return re.sub(r'[^a-z0-9#\[\]]', '', s.lower())


def to_mech(m):
    m = re.sub(r'\{([^/{}]*)/([^/{}]*)\}', r'\1', m)
    m = re.sub(r'\{\+[^{}]*\}', '', m)
    m = re.sub(r'\{-([^{}]*)\}', r'\1', m)
    m = re.sub(r'\[\?[^=\]]*=([^\]]*)\]', r'\1', m)
    return m


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
    if '[#' in w or '[...]' in w:
        return 'hole'
    if '[?' in w:
        return 'guess'
    if '{' in w:
        return 'repaired'
    if w.startswith('['):
        return 'code'
    return 'verbatim'


RANK = ['verbatim', 'code', 'repaired', 'guess', 'hole']


def check(doc):
    dec = {}
    for line in open(ROOT / f'decryption_{doc}.txt', encoding='utf-8'):
        m = re.match(r'(L[\d.]+):\s*(.*)$', line.rstrip('\n'))
        if m:
            dec[m.group(1)] = m.group(2)
    text = (ROOT / f'reading_{doc}_marked.md').read_text(encoding='utf-8')
    block = re.search(r'```marked\n(.*?)```', text, re.S).group(1)
    ok, seen, cnt, joined, last = True, set(), dict.fromkeys(RANK, 0), False, 'verbatim'
    for line in block.splitlines():
        m = re.match(r'(L[\d.]+):\s*(.*)$', line)
        if not m:
            continue
        lid, marked = m.groups()
        seen.add(lid)
        if lid not in dec:
            print('FAIL', doc, lid, 'not in decryption')
            ok = False
            continue
        pr, pd = re.findall(r'«[^»]*»', marked), re.findall(r'«[^»]*»', dec[lid])
        rr, rd = re.sub(r'«[^»]*»', ' ', marked), re.sub(r'«[^»]*»', ' ', dec[lid])
        if pr != pd:
            print('FAIL', doc, lid, 'clear words differ', pr, pd)
            ok = False
        if norm(to_mech(rr)) != norm(rd):
            print(f'FAIL {doc} {lid}: unmarked departure\n  reading -> {norm(to_mech(rr))}\n  signs   -> {norm(rd)}')
            ok = False
        ws = words(rr)
        for i, w in enumerate(ws):
            c = category(w)
            if i == 0 and joined:
                if RANK.index(c) > RANK.index(last):
                    cnt[last] -= 1
                    cnt[c] += 1
                    last = c
                continue
            last = c
            cnt[c] += 1
        joined = bool(ws) and ws[-1].endswith('-')
    if set(dec) - seen:
        print('FAIL', doc, 'lines missing', sorted(set(dec) - seen))
        ok = False
    tot = sum(cnt.values())
    sense = cnt['verbatim'] + cnt['code']
    print(f'{doc}: {tot} cipher words: {cnt["verbatim"]} spelled verbatim from letter groups, {cnt["code"]} word/name '
          f'groups of the key, {cnt["repaired"]} with a marked repair, {cnt["guess"]} guesses, {cnt["hole"]} holes; '
          f'read from the signs without repair {sense}/{tot} = {100 * sense / max(1, tot):.1f}%')
    return ok


if __name__ == '__main__':
    docs = sys.argv[2:] or ['goslinga1730']
    good = all([check(d) for d in docs])
    print('PASS' if good else 'FAIL')
    sys.exit(0 if good else 1)
