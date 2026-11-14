"""morris1813: independent check (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

1. Decoder: reads ONLY beling/key/codebook_M97_13_transcription.csv (Morris number -> reading) and each
   beling/letters/*/transcription.txt, and compares group by group with line_by_line_decode.txt; No. 13 (no
   line-by-line file) is decoded from the second reader's copy A and printed.
2. Read share: the coded words of each letter reading counted as word_share.py counts them, then again with the
   sign 370 left out. 370 stands in the punctuation run of the code sheet (361 , 362 ; 363 : 364 . 365 ! 366 ? 367 -
   368 ( ) 369 " 370), the sheet's numerical reading is "[PARAGRAPH SIGN?]", and in the letters it follows 364 (.)
   in 19 of 21 places: it is a punctuation sign, not an unread word.
3. Why v10 measures more: v10_relabel.share counts every word of reading.txt, including the heading, summary,
   conventions and notes in clear.

    python3 verify_dudout_20261114.py [target_dir]      (part 3 imports research/reading_audit/v10_relabel.py; numpy)
"""
import csv, re, sys, os, pathlib
T = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
L = T / 'beling' / 'letters'
key = {r['morris_number_after_reversal'].strip(): r['reading'].strip()
       for r in csv.DictReader(open(T / 'beling/key/codebook_M97_13_transcription.csv', encoding='utf8'))}
print('1. Decoder')
print('   key rows 361-370:', ' '.join(f'{n}={key[str(n)]}' for n in range(361, 371)))
tot = agree = 0
for d in sorted(L.iterdir()):
    tf, df = d / 'transcription.txt', d / 'line_by_line_decode.txt'
    if not (tf.exists() and df.exists()): continue
    pub = {}
    for l in df.read_text(encoding='utf8').splitlines():
        if l.startswith('#') or ':' not in l: continue
        lab, rest = l.split(':', 1)
        pub[lab.strip()] = [x.strip().split('=', 1) for x in rest.split('|') if re.match(r'\s*\d+=', x)]
    n = a = 0; bad = []
    for l in tf.read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not re.match(r'[\w.]+:', l): continue
        lab, rest = l.split(':', 1); lab = lab.strip()
        if lab not in pub: continue
        rest = re.sub(r'\{[^}]*\}|\|[^|]*\|', ' ', rest)
        rest = re.sub(r'\[[^\]]*\]', '', rest)                      # marks and alternatives in brackets
        groups = re.findall(r'\d+', rest)
        for i, g in enumerate(groups):
            n += 1
            p = pub[lab][i] if i < len(pub[lab]) else ['', '']
            pv = re.sub(r'\[[^\]]*\]$', '', p[1].strip()).rstrip('?').strip()
            mine = key.get(g, '#')
            if p[0].strip() == g and (pv.lower() == mine.lower() or mine.startswith('[') or pv.startswith('[')): a += 1
            else: bad.append((lab, i + 1, g, mine, p))
    tot += n; agree += a
    print(f'   {d.name}: {a}/{n}' + (f'  {bad[:3]}' if bad else ''))
print(f'   total {agree}/{tot}')
t = (L / '1814-04-11_No13/second_reader_both_short_letters_transcription.txt').read_text(encoding='utf8').split('=== B.')[0]
print('   No. 13 copy A:', ' '.join(key.get(g, '#' + g) for l in t.splitlines() if re.match(r'(L\d|SIG):', l)
                                for g in re.findall(r'\d+', l.split(':', 1)[1])))

print('\n2. Read share of the coded words (word_share.py rule), with and without 370')
SKIP = ('Morris to Monroe', 'Pedro de Cevallos to', 'Summary and context', 'Conventions')
def coded_words(path):
    t = path.read_text(encoding='utf-8').split('\nNotes.')[0]
    b = ' '.join(p for p in re.split(r'\n\s*\n', t) if p.strip() and not p.strip().startswith(SKIP))
    b = re.sub(r'\*[^*]*\*|\{[^}]*\}', ' ', b)
    b = re.sub(r'\((?:B:|plain text|Extract)[^)]*\)', ' ', b).replace('[1407[555]^]', '[1407]')
    b = re.sub(r'\[[^\]]*\]', lambda m: m.group(0).replace(' ', '_'), b)
    return [w for w in b.split() if re.search(r'[A-Za-z0-9]', w)]
rows = []
for d in sorted(L.iterdir()):
    f = d / 'reading.txt'
    if not f.exists(): continue
    w = coded_words(f); h = [x for x in w if '[' in x]
    w2 = [x for x in w if not re.fullmatch(r'\[370\][.,;]?', x)]; h2 = [x for x in w2 if '[' in x]
    rows.append((d.name, len(w), len(h), 1 - len(h) / len(w), len(w2), len(h2), 1 - len(h2) / len(w2)))
    print(f'   {d.name:22} {len(w):4} words {len(h):3} holes {1 - len(h) / len(w):.3f}   |  370 left out: '
          f'{len(w2):4} words {len(h2):3} holes {1 - len(h2) / len(w2):.3f}' + ('   <- crosses 0.95' if (1 - len(h) / len(w) < 0.95) != (1 - len(h2) / len(w2) < 0.95) else ''))

print('\n3. v10_relabel.share on the same files (whole file)')
try:
    sys.path[:0] = [str(T.parents[1] / 'research/reading_audit'), str(T.parents[1] / 'docs')]
    cwd = os.getcwd(); os.chdir(T.parents[1]); import v10_relabel as v; os.chdir(cwd)
    for name in ('1814-04-11_No13', '1814-06-21_No17', '1814-10-27_No19'):
        w, h, dd = v.share((L / name / 'reading.txt').read_text(encoding='utf8'))
        print(f'   {name}: {w} words, {h} holes -> {round(1 - (h + dd) / (w + h), 3)} (coded words only: see part 2)')
except Exception as e:
    print('   v10_relabel not loaded:', e)
