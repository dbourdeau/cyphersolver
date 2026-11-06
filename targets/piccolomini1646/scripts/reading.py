"""Check the marked reading of a 2358 letter against the mechanical decryption, and count words. Stdlib only.

    python reading.py check <doc>      (doc = 24874 or 24876)

The marked block of reading_<doc>.md (between '<!-- marked -->' and '<!-- /marked -->') has one line per frame line,
'Lnn<TAB>' + one unit per decrypted word (same count, same order). A unit is:
    [...]          hole: the word is not read
    [?word]        a guess from context, not from the signs (several words joined with _)
    -              a word of nulls only
    text           letters read from the signs; '_' joins words, ' . , ; : are punctuation and ignored.
                   Marks inside the text:  {a/b} reads a where the signs give b;  {+a} a letter no sign gives;
                   {-b} a sign value the reading drops.
Unmarked letters must agree with the decryption: S (class s/5) may be read s or i; G (class g/q/9) may be read g, q,
u or v; u (from 9) may be read u or v. Case is ignored. Exit 1 on any unmarked departure.

Counts: verbatim (no mark), with a marked repair, guessed, holes. Verbatim words are also counted strictly: those whose
cipher word has no class sign S or G (no s/i or g/q/u/v choice), and those with no S, G or 5 (5 and s are hard to tell
apart on these photographs; SIGN_CONVENTIONS.md).
"""
import pathlib, re, subprocess, sys

sys.stdout.reconfigure(encoding='utf-8')

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
OK = {'S': set('si'), 'G': set('gquv'), 'u': set('uv')}


def decryption(doc):
    out = subprocess.run([sys.executable, '-I', str(HERE / 'decrypt.py'), str(ROOT / f'transcription_{doc}.txt'),
                          str(ROOT / 'key.tsv')], capture_output=True, text=True, encoding='utf-8').stdout
    return {l.split('\t')[0]: l.split('\t')[1].split() for l in out.splitlines() if '\t' in l}


def cipher_words(doc):
    out = {}
    for line in (ROOT / f'transcription_{doc}.txt').read_text(encoding='utf-8').splitlines():
        m = re.match(r'^(L\d\d)\t(.*)$', line)
        if m:
            out[m.group(1)] = m.group(2).split()
    return out


def marked(doc):
    t = (ROOT / f'reading_{doc}.md').read_text(encoding='utf-8')
    block = t.split('<!-- marked -->')[1].split('<!-- /marked -->')[0]
    return {m.group(1): m.group(2).split() for m in re.finditer(r'^(L\d\d)\t(.*)$', block, re.M)}


def check_unit(u, d):
    """Return (ok, kind, nmarks, nclass). kind: hole, guess, null, verbatim, marked."""
    if u == '[...]':
        return True, 'hole', 0, 0
    if u.startswith('[?') and u.endswith(']'):
        return True, 'guess', 0, 0
    if u == '-':
        return d == '-', 'null', 0, 0
    s = re.sub(r"[_'.,;:]", '', u)
    side, i, marks = [], 0, 0  # side: list of (char, literal)
    while i < len(s):
        if s[i] == '{':
            j = s.index('}', i); body = s[i + 1:j]; i = j + 1; marks += 1
            if body.startswith('+'):
                continue
            if body.startswith('-'):
                side += [(c, True) for c in body[1:]]; continue
            a, b = body.split('/')
            side += [(c, True) for c in b]
            continue
        side.append((s[i], False)); i += 1
    if len(side) != len(d):
        return False, 'len', marks, 0
    ncls = 0
    for (c, lit), dc in zip(side, d):
        if lit:
            if c.lower() != dc.lower() and not (c == dc):
                return False, 'mark', marks, ncls
            continue
        if c.lower() == dc.lower() and dc not in 'SG':
            continue
        if dc in OK and c.lower() in OK[dc]:
            ncls += dc in 'SG'
            continue
        return False, 'char', marks, ncls
    return True, 'marked' if marks else 'verbatim', marks, ncls


def main():
    doc = sys.argv[2]
    dec, rd, cw = decryption(doc), marked(doc), cipher_words(doc)
    bad = 0
    cnt = {'verbatim': 0, 'marked': 0, 'guess': 0, 'hole': 0}
    ncls = 0
    strict, strict5 = 0, 0  # verbatim words with no S/G; with no S/G/5
    for L in sorted(dec):
        units = rd.get(L)
        if units is None or len(units) != len(dec[L]):
            print(f'FAIL {L}: {0 if units is None else len(units)} units for {len(dec[L])} words'); bad += 1; continue
        for u, d, w in zip(units, dec[L], cw[L]):
            ok, kind, m, c = check_unit(u, d)
            ncls += c
            if not ok:
                print(f'FAIL {L}: reading "{u}" vs decryption "{d}" ({kind})'); bad += 1; continue
            if kind == 'null':
                continue
            n = 1 if kind == 'hole' else len([w for w in u.strip('[?]').split('_') if w])
            cnt[kind] += n
            if kind == 'verbatim' and not set(w) & set('SG'):
                strict += n
                strict5 += n if '5' not in w else 0
    tot = sum(cnt.values())
    pc = lambda k: f'{100 * k / tot:.1f}%'
    print(f'{doc}: words {tot}: verbatim from the signs {cnt["verbatim"]} ({pc(cnt["verbatim"])}), '
          f'of which with no S/G class choice {strict} ({pc(strict)}) and with no S, G or 5 {strict5} ({pc(strict5)}); '
          f'with a marked repair {cnt["marked"]}; guessed from context {cnt["guess"]}; holes {cnt["hole"]}; '
          f'class signs resolved by context {ncls}; verbatim plus marked repairs '
          f'{pc(cnt["verbatim"] + cnt["marked"])}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
