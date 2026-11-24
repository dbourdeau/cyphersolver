"""Count the cipher words of reading.md and its holes, document by document (README Conventions: cipher words only, sure
words only), and check the reading against the contributor's text and the transcription.

    python count_reading.py            counts per document; exit code 1 when a check fails
    python count_reading.py --write    also write words.tsv (one row per cipher word: runs, groups, class, why)

A cipher word is a word written wholly or partly in cipher (bold in reading.md), in the first of the two divisions where
the contributor's readers disagree, with a word broken at a line end counted once. It is a hole when any of these holds:
  marked      the contributor wrote it [?word]: the letters are as given but the word is not understood or uncertain;
  proposed    it has a group 29, 39 or 53, whose values k, p, x are proposed, not fixed by his test (K, P, X in reading.md);
  unreadable  it has a group he could not read (# in his text, º in reading.md);
  unresolved  it has one of the 18 groups his second pass left unresolved (UNRES below, from his list).
Checks: (1) the cipher words of reading.md are, in order, the cipher words of his full text in prior/; (2) their letters
are the decryption of the transcription under key.tsv, group for group (one place differs in his own text, EXC below);
(3) a word is bracketed in reading.md exactly when it is a hole.
"""
import io, re, sys, pathlib
import decode as dec

HERE = pathlib.Path(__file__).resolve().parent
PRIOR = HERE / 'prior' / 'issue784_SeldomPhooey_2026-11-18.md'
# his list of the 18 unresolved groups, as (run: positions). A056: "three groups of the faint run", not said which of the four.
UNRES = {'A056': [1, 2, 3, 4], 'A058': [3], 'A068': [6], 'A073': [5], 'A076': [2], 'A079': [1, 3], 'A081': [3], 'A110': [5],
         'B027': [2], 'B044': [11], 'B047': [1], 'B063': [6], 'B088': [6], 'B102': [3, 10]}
# where his full text and his table differ: the full text prints the faint run A056 as ### (then -en, run A057), the table as ##ig
EXC = {('A', 'ºººen'): 6}
HEADS = {'A': '### A.', 'B': '### B.'}


def split_words(inner):
    words, cur, depth = [], '', 0
    for ch in inner:
        depth += (ch == '[') - (ch == ']')
        if ch.isspace() and depth == 0:
            if cur: words.append(cur)
            cur = ''
        else: cur += ch
    return words + ([cur] if cur else [])


def wrapped(w):
    """One [? ... ] encloses the whole word, and it is not just a proposed letter such as [?k]."""
    if not (w.startswith('[?') and w.endswith(']')) or re.fullmatch(r'\[\?[kpx]\]', w): return False
    depth = 0
    for i, ch in enumerate(w):
        depth += (ch == '[') - (ch == ']')
        if depth == 0 and i != len(w) - 1: return False
    return True


def his_words(doc):
    """[(letters in reading.md's notation, marked by him?)] from the full text in the issue, first division."""
    part = PRIOR.read_text(encoding='utf-8').split('### Reading and English translation')[1]
    block = re.findall(r'```\n(.*?)```', part, re.S)['AB'.index(doc)]
    lines = []
    for l in block.split('\n'):
        m = re.match(r'\d\d\.[M\d]\d\s+(.*)', l)
        lines.append((m.group(1) if m else l).strip())
    s = '\n'.join(lines)
    s = re.sub(r'\{([^{}]*?) / ([^{}]*?)\}', lambda m: m.group(1), s, flags=re.S)
    s = re.sub(r'-\*\*\n\*\*', '', s)
    out = []
    for span in re.findall(r'\*\*(.+?)\*\*', s, re.S):
        for w in split_words(span):
            parts = [f'[?{x}]' for x in w[2:-1].split()] if wrapped(w) and ' ' in w else [w]
            for x in parts:
                marked = wrapped(x)
                core = x[2:-1] if marked else x
                core = re.sub(r'\[\?([kpx])\]', lambda m: m.group(1).upper(), core).replace('#', 'º')
                assert re.fullmatch(r'[a-zKPXº]+', core), x
                out.append((core, marked))
    return out


def reading_words(doc):
    """[(letters, bracketed?)] of the bold words of one document's German in reading.md."""
    text = (HERE / 'reading.md').read_text(encoding='utf-8')
    sec = text.split('\n' + HEADS[doc], 1)[1]
    sec = re.split(r'\n#{2,4} ', sec, 1)[0]            # up to the English translation (####) or the next section
    out = []
    for span in re.findall(r'\*\*(.+?)\*\*', sec, re.S):
        for w in span.split():
            m = re.fullmatch(r'\[\?([a-zKPXº]+)\]|([a-z]+)', w)
            assert m, f'{doc}: unexpected cipher word {w!r}'
            out.append((m.group(1) or m.group(2), bool(m.group(1))))
    return out


def groups(doc, key):
    """[(run, position in run, group as transcribed, letter in reading.md's notation)] in page order."""
    out = []
    for run, gs in dec.runs(doc):
        for i, g in enumerate(gs, 1):
            seen = {'values': set(), 'uncertain': 0, 'unreadable': 0, 'proposed': 0}
            x = dec.decode_group(g, key, seen)
            out.append((run, i, g, {'#': 'º', '[?k]': 'K', '[?p]': 'P', '[?x]': 'X'}.get(x, x)))
    return out


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    key = dec.load_key()
    rows, bad = [], 0
    for doc in 'AB':
        his, mine, gs = his_words(doc), reading_words(doc), groups(doc, key)
        line = {r[0]: r[2] for r in dec.his(doc).values()}
        if [w for w, _ in his] != [w for w, _ in mine]:
            bad += 1
            print(f'{doc}: the cipher words of reading.md are NOT those of the issue text')
        pos = n = holes = stale = differ = 0
        why_n = {'marked': 0, 'proposed': 0, 'unreadable': 0, 'unresolved': 0}
        for (w, marked), (_, bracketed) in zip(his, mine):
            take = EXC.get((doc, w), len(w))
            g = gs[pos:pos + take]; pos += take
            if ''.join(x[3] for x in g) != w:
                differ += 1
                if (doc, w) not in EXC:
                    bad += 1
                    print(f'{doc}: {w} is not the decryption of {" ".join(x[2] for x in g)}')
            why = (['marked'] if marked else []) + (['proposed'] if re.search('[KPX]', w) else []) \
                + (['unreadable'] if 'º' in w else []) \
                + (['unresolved'] if any(x[1] in UNRES.get(x[0], []) for x in g) and 'º' not in w else [])
            if bool(why) != bracketed:
                bad += 1
                print(f'{doc}: {w} is {"" if bracketed else "not "}bracketed in reading.md but its reasons are {why}')
            n += 1; holes += bool(why)
            for k in why_n: why_n[k] += why[0] == k if why else 0
            doubt = sum(1 for x in g if re.fullmatch(r'\d\d\?', x[2]))
            stale += (not why) and doubt > 0
            runs = list(dict.fromkeys(x[0] for x in g))
            rows.append([doc, str(n), '/'.join(dict.fromkeys(line[r] for r in runs)), '+'.join(runs), w,
                         ' '.join(x[2] for x in g), 'hole' if why else 'sure', ', '.join(why), str(doubt)])
        if pos != len(gs):
            bad += 1
            print(f'{doc}: {len(gs) - pos} groups of the transcription are not covered by the reading')
        print(f'{doc}: {n} cipher words, {holes} holes, {n - holes} sure = {(n - holes) / n:.3f}'
              f'  (holes by first reason: {why_n["marked"]} marked [?word] by the contributor, {why_n["proposed"]} proposed value only, '
              f'{why_n["unreadable"]} unreadable group, {why_n["unresolved"]} unresolved group)')
        print(f'   {differ} word(s) where his full text and his table differ; {stale} sure words still carry an NN? mark in his table: '
              f'with those as holes too, {n - holes - stale} of {n} = {(n - holes - stale) / n:.3f}')
    if '--write' in sys.argv:
        head = ['doc', 'n', 'line', 'runs', 'word', 'groups', 'class', 'why a hole', 'groups marked NN?']
        (HERE / 'words.tsv').write_text('\n'.join('\t'.join(r) for r in [head] + rows) + '\n', encoding='utf-8', newline='\n')
        print(f'words.tsv: {len(rows)} rows')
    sys.exit(1 if bad else 0)
