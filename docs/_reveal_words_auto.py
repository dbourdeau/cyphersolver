"""Find word starts for reveal files by locating each passage in its target's reading files.

For every docs/reveal/<slug>.json without word starts, the letters of its tokens are searched for in the text files of
targets/<slug>/ (normalised: letters only, lower case, u/v and i/j/y merged). Where the passage is found, the word
breaks of that reading give the word starts. Prints a report; --write saves the files.

Usage: python _reveal_words_auto.py [--write] [slug ...]
"""
import difflib, json, pathlib, sys, unicodedata

HERE = pathlib.Path(__file__).parent
TARGETS = HERE.parent / 'targets'
FOLD = str.maketrans({'v': 'u', 'j': 'i', 'y': 'i', 'w': 'uu', 'ß': 'ss'})


def norm_char(c):
    c = unicodedata.normalize('NFD', c.lower())[0]
    return c.translate(FOLD) if c.isalpha() else ''


def letters(s):
    return ''.join(norm_char(c) for c in s)


def index_text(text):
    """Normalised letters of text, and for each one whether a word break comes before it."""
    out, brk, gap = [], [], True
    for c in text:
        n = norm_char(c)
        if not n:
            gap = gap or not c.isalnum()
            continue
        for k, ch in enumerate(n):
            out.append(ch); brk.append(gap and k == 0)
        gap = False
    return ''.join(out), brk


def locate(L, N, min_ratio=0.9):
    """Map positions of L to positions in N: exact match, else a fuzzy window anchored on a shared run."""
    at = N.find(L)
    if at >= 0:
        return {k: at + k for k in range(len(L))}
    for a in range(0, max(1, len(L) - 12), 6):
        anchor = L[a:a + 12]
        b = N.find(anchor)
        if b < 0:
            continue
        lo = max(0, b - a - 40); W = N[lo:b - a + len(L) + 40]
        sm = difflib.SequenceMatcher(None, L, W, autojunk=False)
        blocks = sm.get_matching_blocks()
        if sum(m.size for m in blocks) < min_ratio * len(L):
            return None
        return {m.a + k: lo + m.b + k for m in blocks for k in range(m.size)}
    return None


def sources(slug):
    folder = TARGETS / slug
    if not folder.is_dir():
        return []
    files = [p for p in folder.rglob('*') if p.suffix in ('.md', '.txt', '.tsv') and p.stat().st_size < 3_000_000]
    return sorted(files, key=lambda p: ('read' not in p.name.lower(), len(str(p))))


def solve(slug, d):
    toks = d['tokens']
    spans, L = [], ''
    for t in toks:
        p = letters(str(t.get('p') or ''))
        spans.append((len(L), len(p))); L += p
    if len(L) < 8:
        return None, 'too short'
    for src in sources(slug):
        try:
            text = src.read_text(encoding='utf-8', errors='ignore')
        except OSError:
            continue
        N, brk = index_text(text)
        pos = locate(L, N)
        if pos is None:
            continue
        starts = set()
        for i, (s, n) in enumerate(spans):
            if n and (i == 0 or (s in pos and brk[pos[s]])):
                starts.add(i)
        # clear words and word dividers start words of their own; the token after them does too
        for i, t in enumerate(toks):
            p = str(t.get('p') or '')
            if t.get('cls') == 'plain' or (p and not p.strip()):
                if i + 1 < len(toks):
                    starts.add(i + 1)
        words = sum(1 for i in starts if spans[i][1])
        if not words or not 2.8 <= len(L) / words <= 9:
            continue                                  # a sign-by-sign transcription or an unspaced decrypt: next file
        return starts, src.relative_to(TARGETS).as_posix()
    return None, 'passage not found in target text'


def main(argv):
    write = '--write' in argv
    only = [a for a in argv if not a.startswith('--')]
    found = missing = 0
    for f in sorted((HERE / 'reveal').glob('*.json')):
        if only and f.stem not in only:
            continue
        raw = f.read_text(encoding='utf-8'); d = json.loads(raw)
        if not isinstance(d, dict) or 'tokens' not in d or any(t.get('w') for t in d['tokens']):
            continue
        starts, why = solve(f.stem, d)
        if starts is None:
            missing += 1; print(f'-- {f.stem}: {why}'); continue
        found += 1; print(f'ok {f.stem}: {len(starts)} words from {why}')
        if write:
            for i, t in enumerate(d['tokens']):
                t.pop('w', None)
                if i in starts and str(t.get('p') or '').strip():
                    t['w'] = 1
            lines = raw.strip().split('\n')
            indent = len(lines[1]) - len(lines[1].lstrip(' ')) if len(lines) > 1 else None
            f.write_text(json.dumps(d, ensure_ascii=False, indent=indent) + '\n', encoding='utf-8')
    print(f'found {found}, not found {missing}')


if __name__ == '__main__':
    main(sys.argv[1:])
