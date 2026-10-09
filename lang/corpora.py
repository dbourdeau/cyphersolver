"""lang/corpora.py - fetch and cache the corpora named in sources.json.

Each source is resolved to lang/corpora/<id>.txt (git-ignored). A recipe may give any of:
    gutenberg  [ids]      Project Gutenberg plain text, header and licence stripped
    ia         [ids]      Internet Archive full text (<id>_djvu.txt)
    url        [urls]     any plain-text URL
    dta        [ids]      Deutsches Textarchiv plain text (book/download_txt/<id>), cookie gate passed, markup cleaned
    local      [globs]    files a target already downloaded, relative to the repository root
    dehyphenate true      join words hyphenated across line breaks (raw OCR)
'local' is tried first, so nothing is downloaded twice. Because corpora are git-ignored they exist only in the
checkout that fetched them: set CYPHER_CORPUS_ROOTS (os.pathsep-separated) to search other checkouts too.
    python -m lang.corpora                 # status of every source
    python -m lang.corpora fr-henri4       # fetch one
"""
import glob, json, os, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
STORE = os.path.join(HERE, 'corpora')
UA = {'User-Agent': 'cyphersolver-corpus/1.0 (research)'}


def _roots():
    extra = [p for p in os.environ.get('CYPHER_CORPUS_ROOTS', '').split(os.pathsep) if p]
    sib = os.path.join(os.path.dirname(ROOT), 'cypher')       # the main checkout, seen from a worktree
    return [ROOT] + extra + ([sib] if os.path.isdir(sib) and os.path.abspath(sib) != ROOT else [])


def strip_gutenberg(t):
    a = re.search(r'\*\*\* ?START OF (THE|THIS) PROJECT GUTENBERG[^\n]*\n', t)
    b = re.search(r'\*\*\* ?END OF (THE|THIS) PROJECT GUTENBERG', t)
    return t[a.end() if a else 0:b.start() if b else len(t)]


def _get(url):
    for attempt in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode('utf-8', 'replace')
        except Exception as e:
            err = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f'{url}: {err}')


def clean_dta(t):
    t = re.sub(r'\[\d{4}\]|\[Abbildung[^\]]*\]', ' ', t)
    t = t.replace('¬\n', '').replace('ſ', 's').replace('ꝛ', 'r').replace('ͤ', 'e')
    return re.sub(r'-\n(?=[a-zäöü])', '', t)


def _get_dta(i):
    req = urllib.request.Request(f'https://www.deutschestextarchiv.de/book/download_txt/{i}', headers={**UA, 'Cookie': 'verified=1'})
    return clean_dta(urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace'))


def _local(globs):
    for root in _roots():
        hits = {g: sorted(glob.glob(os.path.join(root, g))) for g in globs}
        files = [f for g in globs for f in hits[g]]
        if files:
            for g in globs:
                if not hits[g]:
                    print(f'  warning: {g} matched nothing under {root}; corpus is partial', file=sys.stderr)
            return [strip_gutenberg(open(f, encoding='utf-8', errors='replace').read()) for f in files]
    return None


def fetch(sid, force=False):
    out = os.path.join(STORE, sid + '.txt')
    if os.path.exists(out) and not force:
        return out
    src = json.load(open(os.path.join(HERE, 'sources.json'), encoding='utf-8'))[sid]
    parts = _local(src.get('local', []))
    if parts is None:
        parts = []
        for g in src.get('gutenberg', []):
            parts.append(strip_gutenberg(_get(f'https://www.gutenberg.org/cache/epub/{g}/pg{g}.txt')))
        for i in src.get('ia', []):
            parts.append(_get(f'https://archive.org/download/{i}/{i}_djvu.txt'))
        for u in src.get('url', []):
            parts.append(_get(u))
        for i in src.get('dta', []):
            parts.append(_get_dta(i))
    if src.get('dehyphenate'):
        parts = [re.sub(r'-\s*\n\s*', '', p) for p in parts]   # OCR text: join words split at line ends
    if not parts:
        raise RuntimeError(f"source {sid}: no local copy found and no remote recipe; see its 'note' in sources.json")
    os.makedirs(STORE, exist_ok=True)
    open(out, 'w', encoding='utf-8').write('\n\n'.join(parts))
    return out


def text(sids):
    return '\n\n'.join(open(fetch(s), encoding='utf-8').read() for s in sids)


if __name__ == '__main__':
    srcs = json.load(open(os.path.join(HERE, 'sources.json'), encoding='utf-8'))
    for sid in sys.argv[1:] or sorted(srcs):
        if len(sys.argv) > 1:
            p = fetch(sid, force='--force' in sys.argv)
            print(sid, os.path.getsize(p), 'bytes')
        else:
            p = os.path.join(STORE, sid + '.txt')
            print(f"{sid:24} {'cached' if os.path.exists(p) else '-':7} {srcs[sid]['language']:3} {srcs[sid]['title']}")
