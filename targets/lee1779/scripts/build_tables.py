"""Build the packaged occurrence table, key table, group files, decryption tables and validation pairs for
targets/lee1779 from the reader's decoding table, applying the independent check's corrections (OVR below).

  python build_tables.py <reader decoding.tsv> <targets/lee1779>

The input is the reader's frozen table (sha256 45c9a6fa...e05389 in tests/FREEZE.txt), kept with the working files and
not committed: its notes carry identifications and two edition claims that the check found unsupported. Every change
from it is listed in OVR and UNREAD_NOTE, so the packaged decoding.tsv shows what was changed and why."""
import csv, sys, pathlib, collections

SRC = pathlib.Path(sys.argv[1])          # reader's decoding.tsv
OUT = pathlib.Path(sys.argv[2])          # targets/lee1779

rows = list(csv.DictReader(open(SRC, encoding='utf-8'), delimiter='\t'))
assert len(rows) == 166

# id -> (lookup, entry, printed reading, grade, note). Grades: firm, doubtful, unread.
OVR = {
 8:  ('?4b9 (64b9 supplied)', 'Bishop, s. (at 64b9)', '[Bishop?]', 'doubtful',
      'page number cut off at the left edge of the scan; only "4" visible (p. 4 is front matter). 64b9 = Bishop supplied from sense; La Luzerne\'s brother was Bishop of Langres'),
 11: ('?68a30 (168a30 supplied)', 'Former, s./a. (at 168a30)', '[former?]', 'doubtful',
      'page number cut off at the left edge; 68a30 = Bore, 63a30 = Betoken do not fit; 168a30 supplied from sense. That "the former" is Gerard is inference'),
 14: ('390a15 as written (390a25 alternative)', 'Vendible, a. (390a15); Venerable, a. (390a25); Venal (390a9)', '[vendible? venerable?]', 'doubtful',
      'written 390a15 = Vendible; no sign of a lost X on the image (independent check). Venerable needs XXV. Not settled'),
 20: ('392b28', 'Villanous, a.', 'villanous', 'firm',
      'middle page digit overwritten; 392b28 as written is Villanous (the reader\'s 392b27 was a miscount, same word)'),
 21: ('170a25', 'Frenchified, a. (170a24 = French)', 'Frenchified [French?]', 'doubtful',
      'written XXV clearly = Frenchified; French (170a24) would be a slip of one line. Not settled'),
 30: ('243a17', 'Minister, s.', 'minister[s]', 'firm', 'no ending written; plural supplied'),
 39: ('108a37 as written (100a37 alternative)', 'Cowl, s. (108a37); Considerableness, s. (100a37)', '[considerableness?]', 'doubtful',
      'third page digit read as 8 by the check (108a37 = Cowl, nonsense); 100a37 rests on a changed digit'),
 44: ('63a32 (written 63a31?)', 'Betray, v. (63a32); Betook (63a31)', '[betray?]', 'doubtful',
      'numeral runs into the right edge; a second I may be lost'),
 48: ('134a6', 'Doctor, s.', 'Doctor', 'firm', 'presumably Franklin ("the old Doctor"): identification, not code'),
 50: ('101a35', 'Consul, s.', 'consul', 'firm', 'the code gives only "consul"; who is meant is not in the code'),
 56: ('?2b29 (132b29 supplied)', 'Distress, s. (at 132b29)', '[distress?]', 'doubtful',
      'page number cut off at the left edge; only "2" visible (p. 2 is preface); 132b29 supplied from sense'),
 59: ('?2b9-s (152b9 supplied)', 'Exertion, s. (at 152b9)', '[exertions?]', 'doubtful',
      'leading digits cut off at the left edge or under a blot; 152b9 supplied from sense'),
 67: ('82b21', 'Chaplain, s.', '[chaplain?]', 'doubtful', 'look-up clean, sense of "his chaplain is exceedingly reprobated" uncertain'),
 75: ('145a34', 'Enemy, s.', 'enem[ies]', 'firm', 'no ending written; plural supplied'),
 94: ('384b26-s', 'Trot, v. (Troop is 384b16)', '[troops?]', 'doubtful', '384b26 is Trot; troops is a guess from sense'),
 98: ('384b26-s', 'Trot, v. (Troop is 384b16)', '[troops?]', 'doubtful', 'as the first 384b26-s'),
 103: ('166b7', 'Footing, s.', 'footing', 'firm', '166b7 is Footing as written (independent check, on the 1776 image)'),
 106: ('28?a9-s (284a9 if the blotted digit is 4)', 'Politician, s. (284a9); reader\'s alternative Power, s. (287a10)', '[politicians?]', 'doubtful',
       'third page digit under a blot; keeping IX, 284a9 = Politician needs only the blotted digit; the reader\'s "powers" changes the digit and the line. Not settled'),
 109: ('454b14', 'Benjamin (Christian names, col. b)', 'Benjamin', 'firm', 'presumably Benjamin Franklin: identification, not code'),
 120: ('454?14 (454b14 assumed)', 'Benjamin (col. b); Ambrose (col. a)', '[Benjamin?]', 'doubtful', 'column letter under a blot; Benjamin by sense, not read'),
 125: ('455b11', 'John (Christian names, col. b)', 'John', 'firm', 'with the next group: John Adams'),
 126: ('454a5-s', 'Adam (Christian names, col. a)', 'Adams', 'firm', 'Adam + written -s: Adams'),
 128: ('455d27', 'Samuel (Christian names, col. d)', 'Samuel', 'firm', 'column letter a clear d on image 0041 (independent check); presumably Samuel Adams: identification, not code'),
 131: ('426b29 as written', 'Young, a. (426b29); You, pron. (426b28)', '[you?]', 'doubtful', 'written 29 = Young; You is entry 28 (Lee uses 426b28 elsewhere)'),
 158: ('455?14 (455e14 read)', 'Thomas (Christian names, col. e)', '[Thomas?]', 'doubtful',
       'digits and column letter under a blot; the letter looks more like e than a (independent check); col. a 14 = Gerard does not fit'),
 161: ('416b10? (416b19 supplied)', 'Wanness (416b10); War, s. (416b19)', '[war?]', 'doubtful', 'numeral runs off the edge after X; IX supplied'),
}
UNREAD_NOTE = {
 76: 'no entry within one line fits "almost ...ed the French" (331b6 = Seemly)',
 113: '100b36 = Conspicuously, 108b36 = Cramp: neither fits "render the representatives the ... of the represented"',
 144: 'group heavily corrected; column under a blot (250a12 Multipede, 250b12 Murder); may not be a valid group',
 149: '455a15 = German: names nobody known here',
 156: '293b13 = Profferer; "places of profit" would need 293b18',
}

# Regrades from the received copies (Lee Family Papers, University of Virginia, 1966 microfilm roll 6), made on
# 14 Nov 2026 after the frozen score in received/TEST_RESULT_received.md. The group as written in the letter book is
# unchanged; the look-up uses the group as written on the received copy, which settles a lost or blotted digit.
RECEIVED = {
 56: ('132b29 (received copy)', 'Distress, s.', 'distress', 'firm',
      'letter book shows only "2b29" (page digits lost at the gutter); the received copy writes 132,b,XXIX in full (roll 6 n75)'),
 59: ('152b9-s (received copy)', 'Exertion, s.', 'exertions', 'firm',
      'letter book page digits under a blot; the received copy writes 152,b,IX-s in full (roll 6 n75)'),
 67: ('82b21 (letter book); 82b31 (received copy)', 'Chaplain, s. (82b21); Character, s. (82b31)', '[chaplain? character?]', 'doubtful',
      'the two copies differ: letter book 82,b,XXI = Chaplain, received copy 82,b,XXXI = Character (roll 6 n110); the old interlining gives only "c-h-n" (last letter n or r). Not settled'),
 106: ('284a9-s (received copy)', 'Politician, s.', 'politicians', 'firm',
       'third page digit under a blot in the letter book; the received copy writes 284,a,IX-s (roll 6 n204)'),
 113: ('101b36 (received copy)', 'Contempt, s.', 'contempt', 'firm',
       'letter book 100 (last digit blotted) = Conspicuously, which does not fit; the received copy writes 101,b,XXXVI = Contempt (roll 6 n204): "render the representatives the contempt of the represented"'),
 120: ('454b14 (received copy)', 'Benjamin (Christian names, col. b)', 'Benjamin', 'firm',
       'column letter under a blot in the letter book; the received copy writes 454,b,XIV clearly (roll 6 n205)'),
}

# Re-read on the full-size letter-book images (National Archives Catalog IIIF "max", about 2,700 px wide; fetched
# 15 Nov 2026; local copies in the project's sources/raw/lee1779_push_2026-11-15/lb102v3/, not in this repository).
# Read by an AI worker; no person has checked them. Only one group changes grade.
FULLSIZE = {
 44: ('63a32', 'Betray, v. (63a32)', 'betray', 'firm',
      'at full size the numeral reads XXXII, then a stop, before the paper edge (image 0019); 63a32 = Betray as written'),
}
FULLSIZE_NOTE = {
 14: '; at full size (15 Nov) the XV begins a line at the cut left edge, where neighbouring lines lose their first figure ("[6]4", "[1]68"), so a lost X (XXV = Venerable) is possible but not seen',
 39: '; at full size (15 Nov) the third figure is an open loop with a tail, unlike the closed 8 of "80" on the same page; 100a37 = Considerableness ("importance, value") fits; still not read with certainty',
 158: '; at full size (15 Nov) still under the blot',
 161: '; at full size (15 Nov) the numeral still runs off the edge after X',
}

# Double reading of every figure (15 Nov 2026; double_read/, plan frozen first). Two blind Opus readers transcribed
# all 166 groups from strips of the 1610-px letter-book images. Rule: a group is firm only if at least two independent
# readings (ours, reader A, reader B; the received copy as a further witness for letters 2-4) agree on page, column
# and line AND the entry fits; where the readings give two words, both are printed. Applied last.
DOUBLE_READ = {
 18: ('82b37-s (our reading); 12b37 (both blind readers)', 'Charge, s. (82b37); no entry at 12b37 (no arabic p. 12)', '[charges?]', 'doubtful',
      'first figure at the gutter: we read 82, both blind readers 12; 12b37 has no entry and 82b37 rests on our reading alone (double read, 15 Nov)'),
 59: ('?2b9-s (letter book); 152b9-s (received copy); 102b9 (one blind reader)', 'Exertion, s. (152b9); Continuous, a. (102b9)', '[exertions?]', 'doubtful',
      'page figures under a blot in the letter book: we and reader B read only "2", reader A 102 (Continuous, no fit); 152b9 rests on the received copy alone (double read, 15 Nov)'),
 113: ('100b36 (letter book, three readings); 101b36 (received copy)', 'Conspicuously, ad. (100b36); Contempt, s. (101b36)', '[contempt?]', 'doubtful',
       'the two copies differ: the letter book reads 100,b,XXXVI on all three readings (Conspicuously, no fit), the received copy 101,b,XXXVI (Contempt); contempt rests on the received copy alone (double read, 15 Nov)'),
 158: ('455?14: 455a14 (our reading, reader A); 445a14 (reader B); 455e14 (earlier check)', 'Gerard (455a14); Thomas (455e14)', '[Gerard? Thomas?]', 'doubtful',
       'middle figures overwritten under a blot; two readings give 455,a,XIV = Gerard, which reads oddly here; 455e14 = Thomas rests on one earlier look; both printed (double read, 15 Nov)'),
}
DOUBLE_READ_NOTE = {
 44: '; double read 15 Nov: both blind readers 63,a,XXXII',
 128: '; double read 15 Nov: both blind readers d (our transcription had written a?)',
 163: '; double read 15 Nov: reader A 322, reader B 822 (no such page)',
}

out = []
for r in rows:
    i = int(r['id'])
    g = {'F': 'firm', 'G': 'doubtful', 'U': 'unread'}[r['grade']]
    lookup, entry, reading, note = r['lookup_used'], r['entick_1776_entry'], r['reading'], r['note']
    if i in FULLSIZE:
        lookup, entry, reading, g, note = FULLSIZE[i]
    elif i in RECEIVED:
        lookup, entry, reading, g, note = RECEIVED[i]
    elif i in OVR:
        lookup, entry, reading, g, note = OVR[i]
    elif g == 'unread':
        reading, note = '[...]', UNREAD_NOTE[i]
    else:
        # strip identifications in brackets from the printed word; keep them in the note
        if '[' in reading:
            base, ident = reading.split('[', 1)
            reading = base.strip()
            note = (note + '; ' if note else '') + 'identification [' + ident + ' is inference'
        if reading.startswith('Rus-sia'):
            reading = 'Russia'
        if reading == 'considerableness (importance)':
            reading = 'considerableness'
    if i in FULLSIZE_NOTE:
        note = note + FULLSIZE_NOTE[i]
    if i in DOUBLE_READ:
        lookup, entry, reading, g, dnote = DOUBLE_READ[i]
        note = note + '; ' + dnote
    if i in DOUBLE_READ_NOTE:
        note = note + DOUBLE_READ_NOTE[i]
    if g == 'doubtful' and not reading.startswith('[') and '[' not in reading:
        raise SystemExit(f'doubtful {i} not bracketed: {reading}')
    out.append(dict(id=i, letter=r['letter'], image=r['image'], group_as_written=r['group_as_transcribed'],
                    lookup=lookup, entick_1776_entry=entry, reading=reading, grade=g, note=note))

cnt = collections.Counter(o['grade'] for o in out)
print('grades', dict(cnt))

OUT.mkdir(parents=True, exist_ok=True)
cols = list(out[0])
with open(OUT / 'decoding.tsv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, cols, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(out)

# key: distinct group (normalised, ending stripped) -> headword, grade, occurrences
def norm(g):
    g = g.split('?')[0] if not g.startswith('?') else g
    return g
key = collections.OrderedDict()
for o in out:
    k = o['lookup'].split(' ')[0]
    k = k.split('-')[0] if not k.startswith('?') else k
    e = key.setdefault(k, dict(group=k, entick_1776_entry=o['entick_1776_entry'], readings=[], grades=[], ids=[]))
    e['readings'].append(o['reading']); e['grades'].append(o['grade']); e['ids'].append(str(o['id']))
with open(OUT / 'key.tsv', 'w', encoding='utf-8') as f:
    f.write('# Distinct groups as looked up (page, column, entry), endings stripped. grade: firm / doubtful / unread\n')
    f.write('# per occurrence (see decoding.tsv). Dictionary: Entick, New Spelling Dictionary, London 1776.\n')
    f.write('group\tentick_1776_entry\treadings\tgrades\toccurrences\tids\n')
    for e in key.values():
        f.write('\t'.join([e['group'], e['entick_1776_entry'], ' | '.join(dict.fromkeys(e['readings'])),
                           ' | '.join(dict.fromkeys(e['grades'])), str(len(e['ids'])), ','.join(e['ids'])]) + '\n')
print('distinct groups', len(key))

# group files for measuring (as written, normalised, one letter per file)
for L in '123456':
    gs = [o['group_as_written'] for o in out if o['letter'] == L]
    (OUT / f'code_groups_l{L}.txt').write_text(
        '# Normalised code groups as written (transcription.md), one letter, in order; not the diplomatic text.\n'
        + ' '.join(g.replace(' ', '') for g in gs) + '\n', encoding='utf-8')

# decryption tables
DATES = {'1': '[29 March 1779]', '2': '22 April 1779', '3': '27 April 1779', '4': '21 May 1779 (received copy; begun in the letter book before 9 May)',
         '5': '27 September 1779', '6': '29 February 1780'}
for L in '123456':
    lines = [f'# Letter {L}, {DATES[L]}: occurrence-by-occurrence decryption', '',
             'Every code group in order. "As written" is the transcription; "Looked up" is the entry used in Entick, London 1776',
             '(page, column, entry counted from the top of the column). Grade: firm, doubtful (printed in brackets with a ?),',
             'unread ([...]). The full table with notes is decoding.tsv.', '',
             '| No. | Image | As written | Looked up | Entick 1776 entry | Reading | Grade |', '|---|---|---|---|---|---|---|']
    for o in out:
        if o['letter'] == L:
            lines.append(f"| {o['id']} | {o['image']} | {o['group_as_written']} | {o['lookup']} | {o['entick_1776_entry']} | {o['reading']} | {o['grade']} |")
    (OUT / 'letters').mkdir(exist_ok=True)
    (OUT / 'letters' / f'l{L}_decryption.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

# validation pairs: cipher token = group as looked up (ending stripped); reading = word, unread '?'
with open(OUT / 'validation.tsv', 'w', encoding='utf-8') as f:
    f.write('# model: en-modern\n# source: decoding.tsv (all 166 groups; doubtful readings given without brackets, unread as ?)\n')
    f.write(f'# note: a dictionary code with about {len(out)/len(key):.1f} occurrences per group ({len(out)} occurrences, {len(key)} groups); the letter model is not expected to separate a word-level reading from a key fitted to shuffled groups.\n')
    for o in out:
        k = o['lookup'].split(' ')[0]
        k = k.split('-')[0] if not k.startswith('?') else k
        rd = o['reading']
        if o['grade'] == 'unread':
            rd = '?'
        else:
            rd = rd.split('[')[-1] if rd.startswith('[') else rd
            rd = rd.replace('[', '').replace(']', '').replace('?', '').split(' ')[0].lower()
        f.write(f'{k}\t{rd}\n')
