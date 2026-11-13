"""readings.py : write readings/<slip>.md from units/*.tsv. Mechanical: a word labelled S is printed as decoded; every
word labelled E is a hole '[...]' in its place (its decoded string stays in decryptions/ and units/). The only change
to an S word is word division: words written together in the cipher are split by the table DIV below, which is
printed in each file. No letter is changed, supplied or emended. Spelling is the decode's (u for v, period forms)."""
import csv, collections, pathlib
DIV = {'sieihme': 'sie ihme', 'erihme': 'er ihme', 'beywelcher': 'bey welcher', 'uoneinem': 'uon einem', 'alswan': 'als wan',
       'weilaber': 'weil aber', 'alsauch': 'als auch', 'aneinem': 'an einem', 'wasie': 'was sie', 'groszuthun': 'gros zu thun',
       'grosglogaw': 'gros glogaw', 'procerto': 'pro certo', 'dasman': 'das man', 'inpari': 'in pari', 'alsder': 'als der',
       'zuschertzen': 'zu schertzen', 'wieer': 'wie er', 'undtauch': 'undt auch', 'bissich': 'bis sich', 'zuschertzen': 'zu schertzen'}
SLIPS = [('f7', 'frame 11, left leaf', 'R1', 'R2'), ('f101', "frame 117, 'ad Diarium No. 54'", 'R2', None),
         ('f102', "frame 118, 'ad Appendicem Diarii No. 22'", 'R1', 'R2'), ('f104', "frame 121, 'ad Diarium No. 22'", 'R1', 'R2'),
         ('f204', "frame 233, 'Annotata ad No. 40'", 'R1', 'R2')]
NOTFIRST = {'f7': "**Content not first.** The clear draft of this passage is in LASA A 1 Nr. 529, frame 882 left (fol. 807v), continuing 'ad Diarium No. 32' (see nr529/README.md). It was found on 13 Nov 2026, after this slip had been frozen and decoded. This reading stays here as a check of key and transcription.",
            'f101': "**Content not first.** The clear draft of this passage is in LASA A 1 Nr. 529, frame 532 right (fol. 484r), 'ad Diarium No. 54' (see nr529/README.md). It was found on 13 Nov 2026, after this slip had been frozen and decoded. This reading stays here as a check of key and transcription."}
def lines(name):
    r = list(csv.DictReader(open(f'units/{name}.tsv', encoding='utf-8'), delimiter='\t')); by = collections.defaultdict(list)
    for x in r: by[int(x['line'])].append(DIV.get(x['decoded'], x['decoded']) if x['label'] == 'S' else '[...]')
    S = sum(x['label'] == 'S' for x in r); return [(l, ' '.join(by[l])) for l in sorted(by)], S, len(r), [k for k in DIV if any(x['decoded'] == k and x['label'] == 'S' for x in r)]
for slip, where, rec, other in SLIPS:
    L, S, N, used = lines(f'{slip}_{rec}')
    o = [f'# {slip} ({where}), LASA A 1 Nr. 530: reading with holes', ''] + ([NOTFIRST[slip], ''] if slip in NOTFIRST else []) + [
         f'Reader of record: {rec} ({"b160" if rec == "R1" else "b162"}), first pass, frozen KEY_v2 (md5 c8fade56), decoded once. Strict {S}/{N} = {100*S/N:.2f}%.',
         'Language: German, with Latin phrases. Every [...] is one cipher word that does not read as decoded (label E in units/). Nothing is supplied or emended.',
         'This is not connected prose: holes fall in almost every line. It is offered so the readable words can be checked, not as a translation-ready text.', '',
         'Word division applied (cipher words written together, split here; letters unchanged): ' + (', '.join(f'{k} -> {DIV[k]}' for k in used) or 'none'), '',
         '| line | reading |', '|---|---|'] + [f'| {l} | {t} |' for l, t in L]
    if other:
        L2, S2, N2, _ = lines(f'{slip}_{other}')
        o += ['', f'## Second reader ({other}, b162), same rule, for comparison: strict {S2}/{N2} = {100*S2/N2:.2f}%',
              'Line numbers are the second reader\'s own and need not match the first reader\'s.', '', '| line | reading |', '|---|---|'] + [f'| {l} | {t} |' for l, t in L2]
    pathlib.Path(f'readings/{slip}.md').write_text('\n'.join(o) + '\n', encoding='utf-8')
    print(slip, rec, S, N)
