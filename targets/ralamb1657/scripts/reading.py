"""Check a marked reading against the mechanical decryption and count words. Standard library only.

    python reading.py <reading_xxx.md> <decryption_xxx.txt>

The marked block of the reading lies between '<!-- marked -->' and '<!-- /marked -->', one line per cipher run:
'Lnn<TAB>marked text'. Marks:
    {x/y}     the reading has x, the signs give y            changed value
    {+a}      the reading has a, no sign gives it             added
    {-a}      a sign gives a, the reading drops it            dropped
    [nn]      unidentified code nn, left as it stands         hole
    [...]     groups lost in the binding ([gutter])           hole
    [?word]   proposed word for the hole before it            comment, not compared
A word with no mark and no hole is verbatim from the signs. Comparison ignores spaces and case.
Exit 1 on any unmarked departure.
"""
import pathlib, re, sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

def block(path):
    t = open(path, encoding='utf-8').read()
    t = t.split('<!-- marked -->', 1)[1].split('<!-- /marked -->', 1)[0]
    out = {}
    for line in t.splitlines():
        m = re.match(r'^(L\d+)\t(.*)$', line)
        if m:
            out[m.group(1)] = m.group(2)
    return out

def signs_side(text):
    text = re.sub(r'\[\?[^\]]*\]', '', text)
    text = re.sub(r'\{(.)/(.)\}', r'\2', text)
    text = re.sub(r'\{\+[^}]*\}', '', text)
    text = re.sub(r'\{-([^}]*)\}', r'\1', text)
    text = text.replace('[...]', '[gutter]')
    return re.sub(r'\s+', '', text).lower()

def main():
    rd = block(sys.argv[1])
    dec = {}
    for line in open(sys.argv[2], encoding='utf-8'):
        m = re.match(r'^(L\d+)\t(.*)$', line.rstrip('\n'))
        if m:
            dec[m.group(1)] = re.sub(r'\s+', '', m.group(2)).lower()
    fails = []
    words = verb = marked = holes = 0
    for lab in dec:
        if lab not in rd:
            fails.append(f'{lab}: no marked reading'); continue
        if signs_side(rd[lab]) != dec[lab]:
            fails.append(f'{lab}: reading implies {signs_side(rd[lab])!r}, signs give {dec[lab]!r}')
        for w in re.sub(r'\[\?[^\]]*\]', '', rd[lab]).split():
            words += 1
            if '[' in w:
                holes += 1
            elif '{' in w:
                marked += 1
            else:
                verb += 1
    for lab in rd:
        if lab not in dec:
            fails.append(f'{lab}: reading line with no decryption line')
    print(f'{pathlib.Path(sys.argv[1]).name}: words {words}; verbatim from the signs {verb} ({verb / words:.1%}); '
          f'with a marked repair {marked}; with a hole {holes}')
    for f in fails:
        print('FAIL', f)
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(main())
