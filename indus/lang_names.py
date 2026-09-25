"""Personal-name lists in candidate and control languages, segmented into elements, for comparing name structure
with the Indus names (sets 171-172). The source data are third-party and stay outside the repository; paths come from
the LANG_DATA environment variable (default: C:/Users/dbour/indus_data, outside the repository).

Corpora and elements:
- indus: distinct names on seals in F (R.names_in), elements = signs of body + ending.
- linb: Linear B persons (DAMOS words classed as anthroponyms by the Tiripode lexicon, predict_test152), elements =
  syllabograms.
- skt: Sanskrit names, Monier-Williams entries glossed 'N. of a man' / 'N. of a woman' (Cologne digitisation, SLP1);
  members = compound members (k2 split at the dash), syllables = vowels.
- pra: Prakrit donor names, EIAD (DHARMA, CC BY 4.0): the word before dāna / dānaṁ / deyadhama in Prakrit editions
  (genitive, mostly -sa); syllables by vowel.
- tam: Old Tamil names, Wikipedia 'List of Sangam poets' (Tamil-script column); words = space-separated, syllables
  = Tamil grapheme clusters (consonant + vowel sign or pulli).
- sum: Ur III seal-owner and father names (ORACC epsd2/admin/ur3, CC0): PN forms split at hyphens into signs.
"""
import csv
import json
import os
import re
import unicodedata
import zipfile

import rtools as R

SP = os.environ.get('LANG_DATA', 'C:/Users/dbour/indus_data')
SLP_V = set('aAiIuUfFxXeEoO')
IAST_V = re.compile(r'(ai|au|[aāiīuūeoṛṝḷ])')


def indus(F):
    return sorted({b + (e,) for r in F if r['type'].startswith('SEAL') for b, e in R.names_in(r) if b})


def linb():
    from predict_test152 import classes
    per, _ = classes()
    seen = set()
    with open(os.path.join(SP, 'linb', 'corpus_damos_words.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['word'] in per and r['status'] == 'complete':
                seen.add(tuple(r['word'].split('-')))
    return sorted(seen)


def skt():
    out = []
    cur = None
    for ln in open(os.path.join(SP, 'skt', 'mw.txt'), encoding='utf-8'):
        m = re.match(r'<L>[^<]*<pc>[^<]*<k1>([^<]*)<k2>([^<]*)', ln)
        if m:
            cur = m.groups()
            continue
        if cur and re.search(r'N\.</ab> of a (man|woman)', ln):
            k1, k2 = cur
            mem = tuple(x for x in re.split(r'[—\-]', k2) if x)
            syl = sum(ch in SLP_V for ch in k1)
            if mem and syl:
                out.append((k1, mem, syl))
            cur = None
    return sorted(set(out))


def pra():
    import glob
    out = []
    for fn in glob.glob(os.path.join(SP, 'lang', 'eiad', 'texts', 'xml', '*.xml')):
        s = open(fn, encoding='utf-8').read()
        for m in re.finditer(r'<div type="edition" xml:lang="pra-Latn"[^>]*>(.*?)</div>', s, re.S):
            t = re.sub(r'<!--.*?-->', '', m.group(1), flags=re.S)
            t = re.sub(r'<lb[^>]*break="no"[^>]*/>', '', t)
            t = re.sub(r'<[^>]+>', ' ', t)
            w = [x for x in re.split(r'\s+', t.lower()) if x]
            for i in range(1, len(w)):
                if re.match(r'(dāna|deyadhama)', w[i]) and re.search(r'[a-zāīūṁṅñṇ]', w[i - 1]):
                    nm = re.sub(r'[^a-zāīūṛṝḷṁṃṅñṇṭḍśṣḥ]', '', w[i - 1])
                    if len(nm) >= 3:
                        out.append(nm)
    return out


def iast_syl(w):
    return len(IAST_V.findall(w))


def tam():
    txt = open(os.path.join(SP, 'lang', 'sangam_poets.wiki'), encoding='utf-8').read()
    out = []
    for row in re.findall(r'^\|\d+\s*\|\|([^\n]*)', txt, re.M):
        cells = [c.strip() for c in row.split('||')]
        if len(cells) >= 2 and re.search('[\u0B80-\u0BFF]', cells[1]) and 'பெயர் தெரியாத' not in cells[1]:
            out.append(re.sub(r'\[\[|\]\]|\'\'', '', cells[1]))
    return out


def tam_syl(w):
    n = 0
    for ch in w:
        cat = unicodedata.category(ch)
        if '\u0B85' <= ch <= '\u0BB9':
            n += 1
        if ch == '\u0BCD':
            n -= 0
    return n


def sum_names():
    z = zipfile.ZipFile(os.path.join(SP, 'oracc', 'epsd2-admin-ur3.zip'))
    owners, fathers = [], []
    for n in z.namelist():
        if '/corpusjson/P' not in n:
            continue
        s = z.read(n).decode('utf-8')
        if '"seal' not in s:
            continue
        seq = []
        state = {'seal': None, 'line': None}

        def walk(x):
            if isinstance(x, dict):
                if x.get('node') == 'd':
                    if x.get('type') == 'surface':
                        lab = x.get('label') or ''
                        state['seal'] = lab if lab.startswith('seal') else None
                    elif x.get('type') == 'line-start':
                        state['line'] = x.get('n')
                if x.get('node') == 'l' and state['seal']:
                    f = x.get('f', {})
                    seq.append((state['seal'], state['line'], f.get('pos'), f.get('cf'), (f.get('form') or x.get('frag') or '')))
                for v in x.get('cdl', []):
                    walk(v)
        walk(json.loads(s))
        for i, (seal, line, pos, cf, form) in enumerate(seq):
            if pos == 'PN' and form:
                signs = tuple(x for x in re.split(r'[-.]', re.sub(r'[\[\]⸢⸣#!?*]', '', form)) if x)
                if line == '1' and (i == 0 or seq[i - 1][0] != seal or seq[i - 1][1] != '1'):
                    owners.append((cf, signs))
                elif i > 0 and seq[i - 1][3] == 'dumu':
                    fathers.append((cf, signs))
    return sorted(set(owners)), sorted(set(fathers))


if __name__ == '__main__':
    A, B, rowsA, recs, F = R.load_all()
    print('indus', len(indus(F)))
    print('linb', len(linb()))
    s = skt()
    print('skt', len(s), s[:5])
    p = pra()
    print('pra', len(p), len(set(p)), sorted(set(p))[:15])
    t = tam()
    print('tam', len(t), t[:8])
    o, fa = sum_names()
    print('sum owners', len(o), 'fathers', len(fa), o[:6])


SITES = (('Bhilsa Topes', 'Sanchi'), ('Sanchi', 'Sanchi'), ('Bharhut', 'Bharhut'), ('Mathura', 'Mathura'), ('Amaravati', 'Amaravati'),
         ('Nasik', 'Nasik'), ('Kanheri', 'Kanheri'), ('Junnar', 'Junnar'), ('Karle', 'Karle'))
TITLES = re.compile(r"^(the|a|an|of|monk|nun|lay|layman|laywoman|lay-woman|lay-man|merchant|banker|mother|father|son|daughter|wife|"
                    r"sister|brother|pupil|disciple|venerable|reverend|householder|elder|queen|king|prince|princess|lady|preacher)$", re.I)


def pra_luders():
    """Prakrit donor names from Lueders, List of Brahmi Inscriptions (Ep. Ind. X, 1912; OCR at the Internet Archive):
    'Gift of [titles] Name ...' in entries marked Prakrit. Returns (name, site, female) with the name lower-cased and
    macrons dropped by the OCR."""
    t = open(os.path.join(SP, 'lang', 'luders.txt'), encoding='utf-8').read()
    ents = re.split(r'\n\s*(\d{1,4})\.\s', t)
    out = []
    last = None
    for i in range(1, len(ents) - 1, 2):
        body = ents[i + 1]
        found = next((s for k, s in SITES if k in body), None)
        # the list is ordered by site: an entry without a site keyword takes the last site named before it
        last = found or last
        site = last
        if not re.search(r'Pr[a-z]krit', body):
            continue
        m = re.search(r'Gift of (.{0,160})', body.replace('\n', ' '))
        if not m:
            continue
        seg = re.sub(r'\{[^}]*\}|\([^)]*\)', ' ', m.group(1))
        words = re.findall(r"[A-Za-zÀ-ɏḀ-ỿ'\-]+", seg)
        name = None
        for w in words:
            if TITLES.match(w):
                continue
            if w[:1].isupper():
                name = w
            break
        if name and len(name) >= 3 and not re.search(r'[0-9]', name):
            fem = bool(re.search(r'\b(nun|bhichhuni|bhikhuni|wife|daughter|mother|sister|laywoman|lay-woman|queen|lady|princess)\b', m.group(1), re.I))
            out.append((name.lower().replace("'", ''), site, fem))
    return out


TAM_PLACE = re.compile(r'(ūr|ūril|kuṭi|nāṭu|nāṭṭu|paḷḷi|puram|mālai|malai|kōṭṭam|vaḷanāṭu|maṅkalam|cēri|pāḍi|pāṭi|kaṇṭam|pērur|'
                       r'eri|kōyil|kōṭi|paṭṭi|tuṟai|ttuṟai|kūṟṟam|vāyil|ppēṭu|nallūr|mēṭu)$')


def tam_records():
    """Tamil personal names from the English translations of the DHARMA Tamil inscriptions (tfa-* repositories, CC BY
    4.0; Pallava to Vijayanagara periods): capitalised words with Tamil diacritics ending in a personal suffix (-aṉ,
    -āṉ, -ār, -ar, -i, -ai, -aḷ), place-name endings excluded. Returns (name, repository) per occurrence."""
    import glob
    out = []
    for f in glob.glob(os.path.join(SP, 'lang', 'tfa-*', '**', '*.xml'), recursive=True):
        rep = os.path.relpath(f, os.path.join(SP, 'lang')).split(os.sep)[0]
        s = open(f, encoding='utf-8').read()
        if not re.search(r'<div type="edition" xml:lang="tam', s):
            continue
        for m in re.finditer(r'<div type="translation"[^>]*>(.*?)</div>', s, re.S):
            t = re.sub(r'<[^>]+>', ' ', m.group(1))
            for w in re.findall(r"\b[A-ZĀĪŪĒŌ][a-zāīūēōṉṇḷḻṟṭṅñśṣṛ\-]{2,}\b", t):
                if re.search('[ṉṇḷḻṟṭṅñāīūēō]', w) and re.search(r'(aṉ|āṉ|ār|ar|i|ai|aḷ)$', w) and not TAM_PLACE.search(w):
                    out.append((w, rep))
    return out


def tb_names():
    """Tamil-Brahmi personal names (cave-bed donors, c. 2nd century BCE - 4th century CE) from Mahadevan, Early Tamil
    Epigraphy (2003), Appendix II, transcribed by eye from the scan (lang/ete_personal_names.tsv). Returns (full name,
    personal name = last word with hyphens and paragogic -y/-i joins removed, fem)."""
    out = []
    for ln in open(os.path.join(SP, 'lang', 'ete_personal_names.tsv'), encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('name\t'):
            continue
        p = ln.rstrip('\n').split('\t')
        if len(p) >= 2 and p[0]:
            last = p[0].split()[-1].replace('-', '')
            out.append((p[0], last, p[1] == '1'))
    return out


def _hira(s):
    return ''.join(chr(ord(c) - 0x60) if 'ァ' <= c <= 'ヶ' else c for c in s)


def mora(r):
    out = []
    for c in _hira(r):
        if c in 'ゃゅょぁぃぅぇぉゎ' and out:
            out[-1] += c
        elif 'ぁ' <= c <= 'ゖ' or c in 'ー':
            out.append(c)
    return tuple(out)


def jp_names():
    """Japanese given names, JMnedict (EDRDG, CC BY-SA 4.0; lang/decoy/JMnedict.xml.gz): entries typed masc / fem,
    first kana reading, elements = morae. Returns (morae, fem)."""
    import gzip
    txt = gzip.open(os.path.join(SP, 'decoy', 'JMnedict.xml.gz'), 'rt', encoding='utf-8').read()
    out = set()
    for e in re.findall(r'<entry>(.*?)</entry>', txt, re.S):
        t = re.findall(r'<name_type>&(\w+);</name_type>', e)
        if 'masc' in t or 'fem' in t:
            r = re.search(r'<reb>(.*?)</reb>', e)
            if r:
                m = mora(r.group(1))
                if m:
                    out.add((m, 'fem' in t))
    return sorted(out)


def tr_syl(w):
    w = w.lower().replace('i̇', 'i')
    s = re.findall(r'[^aeıioöuü]*[aeıioöuü]', w)
    tail = re.sub(r'.*[aeıioöuü]', '', w)
    if s and tail:
        s[-1] += tail
    return tuple(s)


def tr_names(minc=100):
    """Turkish given names with their 2009 counts (github eoner/turkce_isimler; decoy/turkce_isimler), names borne by
    minc+ people; elements = syllables by vowel. Returns (syllables, fem)."""
    out = []
    for fn, fem in (('tr_isim_erkek.csv', False), ('tr_isim_kadin.csv', True)):
        for r in csv.reader(open(os.path.join(SP, 'decoy', 'turkce_isimler', fn), encoding='utf-8')):
            if r and r[1].isdigit() and int(r[1]) >= minc and ' ' not in r[0]:
                s = tr_syl(r[0])
                if s:
                    out.append((s, fem))
    return out
