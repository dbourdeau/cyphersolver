"""Put the unread parts of entries removed on 2 Nov 2026 back in research/leads.json, one lead per key.

c4880d390a moved 129 entries to removed_2026-11-02.json. 88 had verdict partly_read, and some of those still held whole
ciphers with no key, or letters nobody had read. Each lead below keeps the removed entry's id where one key remains;
a second key gets a new id. removed_2026-11-02.json stays as the record of the original entries.

A lead whose block passes the gate carries verdict "open" and can go through docs/_check_catalogue.py --promote. Every
other lead drops the verdict and says in "needs" what is still missing.

    python research/vetting_2026-10/restore_residues_2026-11-02.py          dry run
    python research/vetting_2026-10/restore_residues_2026-11-02.py --write
"""
import copy, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
TODAY = '2026-11-02'
BY = ' Narrowed to the unread part and restored 2 Nov 2026.'

# new id: removed id; title, date, shelfmark, decode_ids, status, open, needs; verdict "open" only where the gate is met
R = [
 dict(id=166, frm=166, merge=167, verdict='open', decode=[9586, 9588], title='Principe di Castelcicala to Naples, two undated letters in a second code (R9586, R9588)',
      shelf='ASNa, Ministero degli affari esteri 2337 (DECODE R9586, R9588)',
      open_='All 969 groups (R9586 537, R9588 432); not attacked. The few pencil syllable glosses (about 20-30 groups on each letter) are an untried crib.',
      seen={'where': 'DECODE R9586 pp.1-3 and R9588 pp.1-2, fetched and viewed 2 Nov 2026 (batch L08); ASNa, Ministero degli affari esteri, busta 2337.',
            'extent': 'R9586: 537 groups on 3 pages. R9588: 432 groups on 2 pages. About 20-30 groups glossed on each letter.',
            'cipher': 'Plain numeric code (dot-separated groups 101-1858, a few 6000+), no clear text. A contemporary hand glossed a handful of groups with Italian syllables; no running decipherment is written on or with either letter.'}),
 dict(id=66, frm=66, needs='Edition check: CSP Venetian was not read for this letter. Annealing has not converged and no key is held.'),
 dict(id=74, frm=74, needs='A real literature search, and a re-transcription: small letters are written over many numbers, and how far they reach was never measured.'),
 dict(id=207, frm=207, decode=[4333, 4334, 4335], title='Johann Joachim von Rusdorff to Axel Oxenstierna, The Hague, 1628, three letters in cipher (R4333-R4335)',
      date='1628', shelf='Riksarkivet, Oxenstierna af Södermöre, Ser. B, E 701 (DECODE R4333-R4335)', writeup=None,
      open_='All cipher passages; surveyed only (targets/rusdorff1628). The rusdorff1625 key does not fit R4333.',
      needs="Whether R4333 (numeric) and R4334-R4335 (listed as alphabet) share one key; the key records R4259-R4329 not tried; print not finished (Oxenstierna's correspondence, series II); Rusdorff's copybook at UB Kassel not consulted."),
 dict(id=1614, frm=207, decode=[4338, 4339, 4340, 4341], title='Swedish letters to Axel Oxenstierna, June 1633, code numbers glossed in part (R4338-R4341)',
      date='June 1633', year=1633, shelf='Riksarkivet, Oxenstiernska samlingen E 708 (DECODE R4338-R4341)', writeup=None,
      open_='The unglossed code numbers; not transcribed or attacked (targets/oxenstierna1633).',
      needs='How much of R4339-R4341 is glossed: only R4338 p.1 was viewed. The glosses are a key source, so this may prove a lookup.'),
 dict(id=279, frm=279, verdict='open', decode=[4941], title='Keresdi Bethlen collection, letter of 1648 in a substitution of its own (R4941)',
      date='1648', year=1648, shelf='Romanian National Archives, Cluj, Keresdi_Bethlen_15-05 (DECODE R4941)', writeup=None, outcome='attempted, open',
      open_='The whole cipher: Hungarian annealing on a provisional extract of pp.1-2 gave no coherent text; pp.3-4 not inspected (targets/r4941).',
      seen={'where': 'DECODE R4941 images, fetched 23 Sept 2026 (targets/r4941, R4941-extract.txt from pp.1-2); thumbnails again in frame check d02, 30 Oct 2026.',
            'extent': 'R4941: 4 pp.; cipher extracted from pp.1-2, pp.3-4 not inspected.',
            'cipher': 'Letter-substitution cipher, listed on DECODE as alphabet, status N/A; a different substitution from the Bethlen family key. No decipherment is on the leaves seen.'},
      key_check='Bethlen family key (c=p, p=c, g=u, q=t, targets/transylvania1645) reads R4937, R4939, R4940 and R4942 but does not fit R4941, tested in targets/r4941. No other key held.',
      duplicates='known.py Keresdi / R4941 (2 Nov 2026): only targets/r4941, targets/transylvania1645 and the removed entry 279; no second record of this letter.'),
 dict(id=1615, frm=279, decode=[4933, 4935], title='Kemény collection cipher letters (R4933, R4935)',
      date='1628-1658', shelf='Romanian National Archives, Cluj, Kemény_XIX_1628 1 and 3 (DECODE R4933, R4935)', writeup=None, outcome='attempted, open',
      open_='R4933 (date conflict 1628/1658) and R4935, not transcribed (targets/kemeny1628). The interlinear decipherment on sibling R4934 is a key source.',
      needs='Viewing the leaves: R4935 was seen only as thumbnails and may be largely clear. The R4934 gloss has not been tried on either.'),
 dict(id=450, frm=450, title="Düben to Queen Lovisa Ulrika, system B ('Chiffer n:o 2'), 1764",
      date='5 Oct - 31 Dec 1764', year=1764, shelf='Riksarkivet, Kungliga arkiv, Drottning Lovisa Ulrika, Utgångna skrivelser, SE/RA/710003/02/008/b/K 259, images 118-124',
      open_='2,072 groups pooled, 291 distinct; no decipherment on the leaf. The annealer fails its control at this size (targets/duben1764).',
      needs='The key check is not finished: the tables at images 218-220 were range-checked but not tested group by group or with offsets.'),
 dict(id=1616, frm=450, title='Lovisa Ulrika correspondence, system A: 6 Mar 1764 and the glossed letter of 15 Nov 1765',
      date='6 Mar 1764; 15 Nov 1765', year=1764, shelf='Riksarkivet, Kungliga arkiv, Drottning Lovisa Ulrika, Utgångna skrivelser, SE/RA/710003/02/008/b/K 259, images 101-102, 124-126',
      open_='6 Mar 1764 (641 groups) with no gloss, and the 11 unglossed lines of 15 Nov 1765. The gloss on 36 of 47 lines fixes no single table: the values vary through the text.',
      needs='The variable-key model: additive, table switched at each stroke, or book code. The writer "C. F." is not identified.'),
 dict(id=390, frm=390, title="Marquês de Sande's papers: cipher B, Rome 1664",
      date='1664', year=1664, open_='Cipher B, numeric passages in Portuguese letters; located, not attacked (targets/sande1660). Cipher A is a separate key, recovered here and tracked in that target.',
      needs='The extent of cipher B: only m0063 was viewed, and the neighbouring leaves are listed as probable. The keys of catalogue 388 and 384 are not digitised.'),
 dict(id=465, frm=465, title="Conrad Biermann's copybook, 1675: letters outside key K55",
      open_='Letters to Lilienkron, Gioë, Schröder, Reetz, Lindenow, Klingenberg, Lincker and Lente, in other number families (targets/biermann1675).',
      needs="Whether these are key lookups: the chancery key volume has further keys naming these envoys (images 145-147, 305-308), not fully applied. May be more than one key; split when known."),
 dict(id=470, frm=470, title="Wallis's 'challenge' letters nos. 50, 51 and 53",
      open_='Nos. 50, 51 and 53, not seen. No. 52 is printed by Davys 1737 and is not part of this lead (targets/wallis1653).',
      needs='Images from the Bodleian (MS. e Mus. 203 pp. 218-226). BL Add MS 4200 Bordeaux 1653 may be a copy of no. 50: unchecked.'),
 dict(id=658, frm=658, title='German Minister at Lima: batches London could not decipher, and the Quito-Lima letter code',
      open_='The batches called undecipherable (M336 roll 64 f.0101) and the Quito letter code (f.0104). Batches with a London reply are cribs (targets/lima1917).',
      needs='Which batches are undecipherable: nothing is transcribed. Room 40 decrypts (HW 7, ADM 137) not checked.'),
 # ciphertext seen, nothing else tracks them
 dict(id=441, frm=441, decode=[7517], title='Jan Andrzej Morsztyn to Jerzy Sebastian Lubomirski, letter with digit runs (R7517)',
      shelf='Archiwum Narodowe w Krakowie, Archiwum Sanguszków (ASang), teka 247/13 (DECODE R7517)',
      open_='R7517, two digit runs of about 9 lines with no gloss. Siblings R7518 and R7519 are glossed.',
      needs='Rebuild values from the R7518 and R7519 glosses and apply them; this may prove a lookup.'),
 dict(id=444, frm=444, decode=[7532, 7533], title='Józef Paulin Sanguszko to Barbara Sanguszkowa, letter/digit blocks (R7532, R7533)',
      shelf='Archiwum Narodowe w Krakowie, ASang teka 408/17 (DECODE R7532, R7533)',
      open_='R7532 and R7533, 16-20 lines each of slash-separated letter and digit groups, no decipherment. R7523 is a different symbol cipher, read at the time.',
      needs='Transcription and a test of the Sanguszko key R7515.'),
 dict(id=599, frm=599, title='Swedish government of Bremen-Verden: symbol cipher, Rep. 5a Nr. 654',
      shelf='Niedersächsisches Landesarchiv Stade, Rep. 5a Nr. 654',
      open_='Pages of hand-drawn symbol cipher in rows, unglossed (aufn_0004, 0008, 0030). Nr. 670 is read (targets/stade1710), and its numeric key is a different type.',
      needs='Extent: a page-by-page pass. Nr. 643 has sheets not checked; Nr. 379, 636 and 915 were sampled only.'),
 dict(id=756, frm=756, title='Russian Foreign Ministry bigram circulars to the New York consulate, 1891-97',
      date='1891-1897', open_='Circulars with no filmed worksheet, such as 3902 of 1891 and 4945 and 5078 of 1895.',
      needs='Whether keys 356, 375 and 381 survive elsewhere; the worked examples on the roll are a partial crib. May be more than one key.'),
 dict(id=737, frm=737, title='Spanish despatches from St Petersburg, file on Russian America: unglossed digit pages',
      open_='The page of digits at image 79 and any others; letter 4 (1767) is deciphered between the lines.',
      needs='A page-by-page pass of the 215 images; the letter 4 gloss is a key sample to try.'),
 dict(id=859, frm=859, title="Landgrave Moritz of Hessen-Kassel's alchemical papers: Geheimschrift beyond Schmitz/Winkelmann 1961",
      open_='The pieces of about 50 pages not published in 1961.',
      needs='The 1961 article, to see what it covers, and the key in the volume (ff. 62r-62v, slip on f. 70v).'),
 dict(id=497, frm=497, title='Hieronymus Łaski to Ferdinand I: letters 5-2-20 and 5-2-24',
      shelf='HHStA Wien, StAbt Türkei I 5-2-20, 5-2-24',
      open_='5-2-20 and 5-2-24, not seen glossed. The other letters were read at the time and printed by Gevay.',
      needs='Viewing both items: they may be glossed too.'),
 dict(id=499, frm=499, title='Niccolò Ferducci to Ferdinand I: letters 5-4-11, 5-4-16 and 5-5-6',
      shelf='HHStA Wien, StAbt Türkei I 5-4-11, 5-4-16, 5-5-6',
      open_='5-4-11, 5-4-16 and 5-5-6, not seen. Glossed siblings 5-4-5 and 5-4-7 give the key.',
      needs='Viewing the three items: they may be glossed or read with the sibling values.'),
 # archive only, ciphertext never seen
 dict(id=553, frm=553, title="Dietrich von Schönberg and Grand Master Albrecht: letters 'in Chiffern' with no Auflösung noted",
      shelf='GStA PK, XX. HA, OBA Nr. 21069 (Beibrief), 21213, 22744, 22849, 25346, 25970',
      open_='The listed OBA pieces. The contemporary Auflösung filed with 22755 and others may give the key.',
      needs='Scans from GStA PK and the filed Auflösungen.'),
 dict(id=554, frm=554, title='Elector Joachim I and Grand Master Albrecht: ciphered letters with no Auflösung noted',
      shelf='GStA PK, XX. HA, OBA Nr. 22553, 22850, 23943',
      open_='22553, 22850 and 23943, unless the print of Joachim resolves them.',
      needs='Scans from GStA PK and a check against Joachim.'),
 dict(id=555, frm=555, title='Heydeck, Isenburg and Schönburg to Grand Master Albrecht: reports with no Auflösung noted',
      shelf='GStA PK, XX. HA, OBA Nr. 23484, 24365, 24382, Anlage of 23888',
      open_='23484, 24365, 24382 and the Anlage of 23888.',
      needs='Scans from GStA PK and the Auflösungen filed with 23888-24019.'),
 dict(id=556, frm=556, title='Dietrich von Schönberg and Daniel Gundelfinger at Lyon: letters with no Auflösung noted',
      shelf='GStA PK, XX. HA, OBA Nr. 26695, 26815, 26824, 26969',
      open_='26824 and 26969 in cipher; 26695 and 26815 partly.',
      needs='Scans from GStA PK and the alphabet filed in OBA 26859, which may read them; this may prove a lookup.'),
 dict(id=557, frm=557, title='Ordensbriefarchiv ciphered pieces with no key or translation noted',
      shelf='GStA PK, XX. HA, OBA Nr. 20039, 22717, 26976',
      open_='20039, 22717 and 26976.', needs='Scans from GStA PK. Different writers, so probably not one key: split when seen.'),
 dict(id=521, frm=521, title='Sieyès embassy: Wessenberg P 1839 5 and the Rivals letter of 10 Oct 1798',
      shelf='Stadtarchiv Konstanz, Wessenberg correspondence P 1839 5; Archives nationales 284AP/12',
      open_="P 1839 5 and the Rivals letter ('déchiffrement manque'). P 1839 21 carries clear text over the cipher and is a crib.",
      needs='Scans of both; neither has been seen.'),
 dict(id=493, frm=493, title='Gravelle enclosure, Kriegsakten 148-2-58',
      shelf='HHStA Wien, Kriegsakten 148-2-58', date='1672', open_='148-2-58, no clear twin. 148-2-70 has its clear text in 148-2-69 and is not part of this lead.',
      needs='A scan or a viewing of 148-2-58.'),
 dict(id=591, frm=591, title='Prussian cipher pieces: Rep. 91 A Nr. 86 and the Naples piece',
      shelf='GStA PK, I. HA Rep. 91 A Nr. 86; I. HA Rep. 81 Neapel nach 1807 Nr. 24',
      open_='Both unexamined. The three Werther letters have a Dechiffrierung filed with them and are not part of this lead.',
      needs='Scans of both; the Prussian keys of 1807-14 named in the original lead (III. HA MdA ZB Nr. 73, 76) are not held.'),
 dict(id=434, frm=434, title='St Petersburg to Ogrodzki, ciphered leaves of 1769-70',
      date='1769-1770', year=1769, open_='The 1769-70 leaves. The 1765 volume carries its own explained key and is a lookup once imaged.',
      needs='Images from AGAD, and a test of the 1765 key on these leaves.'),
 dict(id=697, frm=697, title="German agent message 'Tismera', Nov 1917",
      open_='The Tismera message, in progress with no recorded result; the other two were deciphered by MID.',
      needs='MID file 10270-81 itself: only the index card is online.'),
]


def build(spec, removed):
    e = copy.deepcopy(removed[spec['frm']])
    e['id'] = spec['id']
    e['restored_from'] = 'removed_2026-11-02 #%d' % spec['frm'] + (', #%d' % spec['merge'] if spec.get('merge') else '')
    for k, f in (('title', 'title'), ('date', 'date'), ('year', 'year'), ('shelfmark', 'shelf'), ('open', 'open_')):
        if spec.get(f) is not None:
            e[k] = spec[f]
    if 'decode' in spec:
        e['decode_ids'] = spec['decode']
        names = {'R%d' % d for d in spec['decode']}
        e['links'] = [l for l in e.get('links', []) if not l['label'].startswith('DECODE') or l['label'].split()[-1] in names]
    if 'writeup' in spec:
        e.pop('writeup', None)
    if spec.get('outcome'):
        e['outcome'] = spec['outcome']
    e['status'] = (e.get('status') or '') + BY
    v = e['vetting']
    v.pop('closed', None)
    v['date'] = TODAY
    v['by'] = v['by'] + '; narrowed 2 Nov 2026'
    v['seen'].update(spec.get('seen', {}))
    for k in ('key_check', 'duplicates'):
        if spec.get(k):
            v[k] = spec[k]
    if spec.get('verdict') == 'open':
        v['verdict'] = 'open'
    else:
        v.pop('verdict', None)
        e['needs'] = spec['needs']
    return e


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    removed = {e['id']: e for e in json.loads((ROOT / 'research/vetting_2026-10/removed_2026-11-02.json').read_text(encoding='utf-8'))}
    path = ROOT / 'research/leads.json'
    d = json.loads(path.read_text(encoding='utf-8'))
    cat = json.loads((ROOT / 'catalogue.json').read_text(encoding='utf-8'))['entries']
    used = {e['id'] for e in d['leads']} | {e['id'] for e in cat}
    new = [build(s, removed) for s in R]
    clash = [e['id'] for e in new if e['id'] in used]
    if clash:
        sys.exit('ids already in use: %s' % clash)
    for e in new:
        print('#%-5d %-5s %s' % (e['id'], (e['vetting'].get('verdict') or 'lead'), e['title'][:90]))
    print(len(new), 'leads')
    if '--write' in sys.argv:
        d['leads'] += new
        path.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
