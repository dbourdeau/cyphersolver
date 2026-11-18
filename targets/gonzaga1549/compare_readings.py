"""Compare the two independent readings of Charles V to Ferrante Gonzaga, 14 Nov 1549 (cc. 60r-62r), and recount each.

    python compare_readings.py            from this folder; standard library only

Reading 1 (the project's): 14nov1549_reading.txt and the sign files 14nov1549_*.tsv.
Reading 2 (WAINUT's, as filed): wainut/reading_ch1549_1114.md, wainut/transcription_ch1549_1114.txt, wainut/key.tsv.
Writes comparison_14nov1549.tsv (word by word), comparison_signs.tsv (WAINUT's key rows against the values the
project's sign files have at the aligned places), 14nov1549_reading_wainut_codes.md (reading 2 with the code values
settled on 14 Nov 2026 carried in; the filed reading is not changed) and comparison_summary.json.

Strict count (README Conventions, the read bar): a word counts as read only if it is sure. Reading 1: no (x?), no [.],
not inside ‹ ›, not an open {code}. Reading 2: no degree mark (repair), not [?word], not [...]. A settled code word
counts as read in both. The alignments are by similarity, so the cross-counts are close figures, not exact ones.
"""
import collections, difflib, json, re, unicodedata

G_FILES = ['14nov1549_60r_block1.tsv', '14nov1549_60r_block2.tsv', '14nov1549_60v.tsv', '14nov1549_61r.tsv',
           '14nov1549_61v.tsv', '14nov1549_62r.tsv']
# code values carried into reading 2 (NOTES.md, 14 Nov 2026): the filed text -> the text with the value
CARRY = [('[?la] [?Yglesia]', '[Su Santidad]'), ('[?Francia]', '[Francia]'), ('con el [...] Octauio', 'con el [Duque] Octauio')]
# Disagreements between two sure words, and how each stands. Anything not listed is open.
VERDICT = {
    ('ratificacion', 'gratificacion'): ('settled: gratificacion', 'the sign R is gra in the contemporary decipherments of Philip\'s letters (WAINUT\'s frozen key), and reading 1 needs gra for the same shape in desgracia'),
    ('tarde', 'de'): ('settled: tratar de', 'same signs ta r de in both; reading 1 had the sign before them unread and divided the words wrongly'),
    ('consta', 'constara'): ('settled: constara estar', 'same letters in both; only the word division differs'),
    ('re-estar', 'estar'): ('settled: constara estar', 'same letters in both; only the word division differs'),
    ('fines', 'fin'): ('settled: fin es que', 'same letters in both; only the word division differs'),
    ('bien', 'si'): ('settled: si', 'the sign (7 with two dots) is si in yglesia and quisiesse in reading 1 itself; reading 2 has si from its frozen key'),
    ('bien', 'en'): ('settled: si en', 'as above; same signs, si + en'),
    ('con', 'contra'): ('settled: contra', 'the sign file of reading 1 has an unread sign between con and la (c.60v line 1); reading 2 reads it tra'),
    ('hasta', 'hastaqui'): ('settled: hasta qui', 'same letters in both; only the word division differs'),
    ('de', 'no'): ('open', 'the signs for de and no (X and x in WAINUT\'s names) are exchanged at several places; the sense favours reading 1 here; image not looked at'),
    ('no', 'de'): ('open', 'the signs for de and no (X and x in WAINUT\'s names) are exchanged at several places; the sense favours reading 1 here; image not looked at'),
    ('hallarse', 'hallarnos'): ('open', 'one sign: se in reading 1, no + s in reading 2; the first person is expected after verniamos'),
    ('dezes', 'dezis'): ('open', 'one vowel mark'),
    ('seguro', 'segura'): ('open', 'one vowel mark; reading 1 has justificada ... seguro, reading 2 justificado ... segura'),
    ('curar', 'procurar'): ('open', 'reading 1 has de + curar, reading 2 pro + curar; xo = pro is in WAINUT\'s frozen key from the contemporary decipherments, x with an o-loop = de in the key as pictured on Cryptiana; the place on the image not looked at'),
    ('ottavio', 'octauio'): ('open', 'one sign: tt in Bertomeu Masia\'s key as pictured on Cryptiana (reading 1), ct in WAINUT\'s table (from this letter); the word is the same'),
    ('remittimos', 'remictimos'): ('open', 'the same sign as in Ottavio / Octauio'),
    ('apuntar', 'apontar'): ('open', 'one vowel mark'),
    ('pretende', 'pretiende'): ('open', 'one sign'),
    ('nombre', 'nonbre'): ('open', 'spelling; reading 1 writes nonbre elsewhere'),
    ('sobre', 'sobrello'): ('settled: sobre ello / sobrello', 'same letters; division'),
    ('mismo', 'assimismo'): ('settled: assi mismo', 'same letters; division'),
    ('haverlo', 'hauer'): ('settled: haver lo', 'same letters; division'),
}


def norm(w):
    w = re.sub(r'\(([^)]*)\?\)', r'\1', w).lower()
    w = ''.join(c for c in unicodedata.normalize('NFD', w) if c.isalpha())
    w = w.replace('v', 'u').replace('y', 'i').replace('j', 'i').replace('z', 'c').replace('x', 's').replace('h', '')
    return re.sub(r'(.)\1', r'\1', w)


def reading1():
    out, sec, frag = [], '', False
    for ln in open('14nov1549_reading.txt', encoding='utf8').read().split('\n'):
        if ln.startswith('#') or not ln.strip():
            continue
        if re.match(r'c\.\d+[rv]', ln) and len(ln) < 140 and 'ver' not in ln.split(',')[0]:
            sec = ln
            continue
        ln = re.sub(r'\[((?:\. )+\.)\]', lambda m: ' '.join(['[.]'] * (m.group(1).count('.'))), ln)
        ln = re.sub(r'\{([^{}=]+) = ([^{}]+)\}', lambda m: ' '.join('{=%s}' % x for x in m.group(2).split()), ln)
        ln = re.sub(r'\{([^{}]+)\}', lambda m: ' '.join('{%s}' % x for x in m.group(1).split()), ln)
        ln = ln.replace('‹', ' ‹ ').replace('›', ' › ')
        for w in ln.split():
            if w in ',.;':
                continue
            if w == '‹':
                frag = True
            elif w == '›':
                frag = False
            else:
                c = ('frag' if frag else 'code' if w.startswith('{=') else 'opencode' if w.startswith('{') else
                     'hole' if '[' in w else 'doubt' if '?' in w else 'sure')
                out.append((sec, w.replace('{=', '').strip('{}') if c == 'code' else w, c))
    return out


def reading2():
    t = open('wainut/reading_ch1549_1114.md', encoding='utf8').read()
    for a, b in CARRY:
        assert a in t, a
        t = t.replace(a, b)
    head = ('<!-- Reading 2 (WAINUT), from wainut/reading_ch1549_1114.md as filed, with the code values settled on 14 Nov 2026 '
            'carried in by the project (compare_readings.py): inta = Su Santidad (twice), nep = Francia, saa = Duque. '
            'Nothing else is changed. [Word] = code word with its value. -->\n')
    open('14nov1549_reading_wainut_codes.md', 'w', encoding='utf8').write(head + t)
    out, sec, code = [], '', False
    for ln in t.split('## Spanish')[1].split('\n'):
        if ln.startswith('###'):
            sec = ln[4:]
            continue
        for w in ln.split():
            if w.startswith('[...'):
                c = 'hole'
            elif w.startswith('[?'):
                c = 'prop'
            elif w.startswith('[') or code:
                c = 'code'
                code = ']' not in w
            elif '°' in w:
                c = 'repair'
            else:
                c = 'sure'
            out.append((sec, w, c))
    return out


def align(a, b, sim, gap):
    n, m = len(a), len(b)
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    B = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        D[i][0] = i * gap; B[i][0] = 1
    for j in range(1, m + 1):
        D[0][j] = j * gap; B[0][j] = 2
    for i in range(1, n + 1):
        Di, Dp, ai = D[i], D[i - 1], a[i - 1]
        for j in range(1, m + 1):
            c0 = Dp[j - 1] + sim(ai, b[j - 1]); c1 = Dp[j] + gap; c2 = Di[j - 1] + gap
            if c0 >= c1 and c0 >= c2:
                Di[j] = c0
            elif c1 >= c2:
                Di[j] = c1; B[i][j] = 1
            else:
                Di[j] = c2; B[i][j] = 2
    i, j, al = n, m, []
    while i or j:
        k = B[i][j]
        if k == 0:
            al.append((i - 1, j - 1)); i -= 1; j -= 1
        elif k == 1:
            al.append((i - 1, None)); i -= 1
        else:
            al.append((None, j - 1)); j -= 1
    return al[::-1]


def wsim(a, b):
    if not a or not b:
        return -0.3
    r = difflib.SequenceMatcher(None, a, b).ratio()
    return 2 * r - 1.0 if r >= 0.5 else -0.6


def words():
    g, f = reading1(), reading2()
    gn, fn = [norm(w) for _, w, _ in g], [norm(w) for _, w, _ in f]
    al = align(gn, fn, wsim, -0.35)
    READ1, READ2 = {'sure', 'code'}, {'sure', 'code'}
    rows, cat = [], collections.Counter()
    for a, b in al:
        gs, gw, gc = g[a] if a is not None else ('', '', '-')
        fs, fw, fc = f[b] if b is not None else ('', '', '-')
        x, y = norm(gw), norm(fw)
        same = bool(x) and x == y
        near = bool(x and y) and difflib.SequenceMatcher(None, x, y).ratio() >= 0.75
        r1, r2 = gc in READ1, fc in READ2
        note = ''
        if r1 and r2 and same:
            k = 'A both sure, same word'
        elif r1 and r2 and near:
            k = 'B both sure, spelling or division differs'
            v = VERDICT.get((re.sub(r'[.,;]', '', gw.lower()), re.sub(r'[.,;]', '', fw.lower())))
            note = ' | '.join(v) if v else 'open'
        elif r1 and r2:
            k = 'E both sure, different words'
            v = VERDICT.get((re.sub(r'[.,;]', '', gw.lower()), re.sub(r'[.,;]', '', fw.lower())))
            note = ' | '.join(v) if v else 'open'
        elif (r1 or r2) and (same or near) and gw and fw:
            k = 'C sure in one, the other gives the same word with a mark'
        elif r1 and not fw:
            k = 'D1 sure in reading 1, no word aligned in reading 2'
        elif r2 and not gw:
            k = 'D2 sure in reading 2, no word aligned in reading 1'
        elif r1:
            k = 'D1 sure in reading 1, reading 2 unsure or different'
        elif r2:
            k = 'D2 sure in reading 2, reading 1 unsure or different'
        elif (same or near) and gw and fw:
            k = 'F same word, marked in both'
        else:
            k = 'G sure in neither'
        cat[k[:2].strip()] += 1
        rows.append((gs.split(',')[0][:6] if gs else '', fs.split(',')[0] if fs else '', gw, gc, fw, fc, k, note))
    with open('comparison_14nov1549.tsv', 'w', encoding='utf8') as o:
        o.write('# The two readings of 14 Nov 1549 word by word (compare_readings.py). Reading 1: the project. Reading 2: WAINUT, codes carried.\n')
        o.write('# place_1\tplace_2\tword_1\tclass_1\tword_2\tclass_2\tcategory\tverdict\n')
        for r in rows:
            o.write('\t'.join(r) + '\n')
    c1, c2 = collections.Counter(c for _, _, c in g), collections.Counter(c for _, _, c in f)
    return rows, cat, c1, c2


def signs():
    key = {}
    for l in open('wainut/key.tsv', encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        p = l.rstrip('\n').split('\t')
        key[p[0]] = (p[1], p[2] if len(p) > 2 else '')
    F = []
    for l in open('wainut/transcription_ch1549_1114.txt', encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        t = l.split()
        for s in t[1:]:
            if s == '#':
                continue
            w = s.strip('{}')
            F.append((t[0], w, 'null' if s.endswith('_') else key[w][0] if w in key else '?'))
    G = []
    for f in G_FILES:
        for l in open(f, encoding='utf8'):
            if l.startswith('#') or not l.strip():
                continue
            p = l.rstrip('\n').split('\t')
            if len(p) >= 3:
                G.append((f[10:-4] + ' L' + p[0], p[1], p[2]))

    def nv(v):
        v = v.rstrip('?').lower()
        if v.startswith('null'):
            return 'null'
        return re.sub(r'[\[\]?]', '', v).replace('v', 'u')

    def sim(a, b):
        if a == b and a not in ('', 'null'):
            return 1.0
        if a == b:
            return 0.4
        if not a or not b:
            return -0.2
        if 'null' in (a, b):
            return -0.3
        return 0.1 if a[0] == b[0] or a[-1] == b[-1] else -0.6
    gv, fv = [nv(x[2]) for x in G], [nv(x[2]) for x in F]
    al = align(gv, fv, sim, -0.4)
    pairs = [(G[a], F[b]) for a, b in al if a is not None and b is not None]
    same = sum(1 for g, f in pairs if nv(g[2]) == nv(f[2]))
    t = collections.defaultdict(collections.Counter)
    for g, f in pairs:
        t[f[1]][(nv(g[2]) or 'unread') + ('?' if g[2].endswith('?') and g[2] != '?' else '')] += 1
    with open('comparison_signs.tsv', 'w', encoding='utf8') as o:
        o.write('# WAINUT\'s key rows (wainut/key.tsv) against the values the project\'s sign files give at the aligned places of the 14 Nov letter (compare_readings.py).\n')
        o.write('# sign (WAINUT\'s name)\tvalue (WAINUT)\tstatus (WAINUT)\tplaces aligned\tsame value in the project\'s files\tvalues in the project\'s files\n')
        for s, (v, st) in key.items():
            c = t.get(s, {})
            o.write('\t'.join([s, v, st.split(';')[0].split(':')[0], str(sum(c.values())), str(c.get(nv(v), 0)),
                               ', '.join(f'{k} {n}' for k, n in sorted(c.items(), key=lambda x: -x[1]))]) + '\n')
    return {'signs_reading1': len(G), 'signs_reading2': len(F), 'aligned': len(pairs), 'same_value': same,
            'only_reading1': sum(1 for a, b in al if b is None), 'only_reading2': sum(1 for a, b in al if a is None)}


def short(path):
    """Strict count of one of the short readings of the project: body lines, clear lead-ins in (clear: ...) left out."""
    n = read = 0
    for ln in open(path, encoding='utf8').read().split('\n'):
        if ln.startswith('#') or not ln.strip():
            continue
        ln = re.sub(r'\(c\.64r, clear:[^)]*\)|\(clear:[^)]*\)', ' ', ln)
        ln = re.sub(r'\[2 lines of signs[^\]]*\]', ' ', ln)          # the unread lines of c.64r: listed as a gap, not counted as words
        ln = re.sub(r'^[a-d0-9]\. ', '', ln)
        ln = re.sub(r'\{[^{}=]+ = ([^{}]+)\}', r'\1', ln)
        frag = False
        for w in ln.replace('‹', ' ‹ ').replace('›', ' › ').split():
            if w == '‹':
                frag = True
            elif w == '›':
                frag = False
            elif w not in ',.;':
                n += 1
                read += not (frag or '?' in w or '[.' in w or '.]' in w or '{' in w)
    return {'words': n, 'read': read, 'share': round(read / n, 4)}


if __name__ == '__main__':
    rows, cat, c1, c2 = words()
    n1, n2 = sum(c1.values()), sum(c2.values())
    s = {'reading1': {'words': n1, 'classes': dict(c1), 'read': c1['sure'] + c1['code'], 'share': round((c1['sure'] + c1['code']) / n1, 4)},
         'reading2': {'words': n2, 'classes': dict(c2), 'read': c2['sure'] + c2['code'], 'share': round((c2['sure'] + c2['code']) / n2, 4)},
         'word_categories': dict(sorted(cat.items())),
         'differences_between_sure_words': [{'reading1': r[2], 'reading2': r[4], 'verdict': r[7]} for r in rows if r[6][0] in 'BE'],
         'signs': signs(),
         'short_readings_project': {f: short(f) for f in ('13may1549_reading_signs.txt', '30sep1549_reading.txt', '20nov1549_reading.txt', '23dec1549_reading.txt')}}
    json.dump(s, open('comparison_summary.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(json.dumps(s, ensure_ascii=False, indent=1))
