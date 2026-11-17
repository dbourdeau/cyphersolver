"""Build journal_as_written.md and journal_modernized.md from reconciled_source.txt.

The word-by-word line file is the authority; the two running texts are generated from it so they cannot drift.
Entries are put in date order (the notebook pages were filmed out of order). Entries on pages that hold no cipher and
are not in the line file are given as fixed plain text below (PLAIN), read on the image by the first agents.

Usage (from targets/long1779): python scripts/build_journal.py
"""
import re, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent

# (heading, image label, ranges "img:side:first-last", fixed plain text before, fixed plain text after)
ENTRIES_1779 = [
    ("[Hopkinton] July ye 25th", "img 31, plain", [], "This day we began our march [to] Providence; stages at Mr Mullen's, New Boston, Dr Prescott's, Groton, Jonson's Sudbury, Sherborn, Attleborough; \"Providence Town\" (mileage list).", ""),
    ("Providence July ye 26th", "img 31, plain", [], "This day we arrived here about noon and drawed provision with ... Col. Mooney's Regt ...", ""),
    ("July ye 28th Wednesday", "img 31, plain", [], "... marched for [Tiverton] ... landed at [Howland's] ferry ... (faint; not read in full).", ""),
    ("Tiver-town July ye 29th at Howlands ferry", "img 30, plain", [], "A S.E. storm which wet us all before we got into our Barricks.", ""),
    ("Tivertown July ye 29th 1779", "img 11", ["11:-:1-3"], "", ""),
    ("July ye 31st", "img 30, plain", [], "We marched down ye river 4 m[iles] toward Seaconet.", ""),
    ("Guard roster, 31 July to about 12 August", "img 12 left", ["12:L:1-19"], "", ""),
    ("Augt ye 1st Sunday", "img 11", ["11:-:4-6"], "", ""),
    ("Augt 3d", "img 11", ["11:-:7-11"], "", ""),
    ("Augt 5th", "img 11", ["11:-:12-18"], "", ""),
    ("Augt ye 7th Saturday", "img 11", ["11:-:19-20"], "", ""),
    ("Sunday 8th", "img 11", ["11:-:21-24", "11:-:margin-margin"], "", ""),
    ("Augt ye 8th Sunday morning", "img 29", ["29:-:1-7"], "", ""),
    ("Augt ye 8th Sunday", "img 13 right", ["13:R:1-9"], "", ""),
    ("Augt ye 9th Monday", "img 13 right", ["13:R:10-16"], "", ""),
    ("Augt 10th to 13th", "img 13 right, plain", ["13:R:17-20"], "", ""),
    ("Augt ye 14th", "img 14 left", ["14:L:1-7"], "", ""),
    ("Augt ye 16th Monday", "img 14 left", ["14:L:10-13"], "", ""),
    ("Night of 16 Aug", "img 14 left - 14 right", ["14:L:14-31", "14:R:1-7"], "", ""),
    ("[17 Aug]", "img 14 right", ["14:R:8-10"], "", ""),
    ("Augt ye 18th", "img 14 right, plain", ["14:R:11-11"], "", ""),
    ("Augt ye 20th", "img 14 right", ["14:R:12-19"], "", ""),
    ("Augt ye 22nd Sunday", "img 14 right", ["14:R:20-22"], "", ""),
    ("Augt ye 24th", "plain", [], "Ye night before last two regulars deserted & swimming across ye river they ... one, ye other ... took in.", ""),
    ("Augt ye 24th, accounts", "img 19 left", ["19:L:1-17"], "", ""),
    ("Augt ye 26th", "img 15 left", ["15:L:1-7"], "", ""),
    ("Tivertown Augt 26th to 30th", "img 15 left", ["15:L:8-27"], "", ""),
    ("Sept 6th Monday", "img 15 right", ["15:R:1-15"], "", ""),
    ("Sept ye 8th", "img 15 right", ["15:R:16-18"], "", ""),
    ("[about 10-15 Sept]", "img 16 left", ["16:L:1-10"], "", ""),
    ("Sept 19th", "img 16 left", ["16:L:11-16"], "", ""),
    ("Sept 23rd", "img 16 left", ["16:L:17-21"], "", ""),
    ("Sept ye 22nd", "img 16 left", ["16:L:22-25"], "", ""),
    ("Sept ye 25th", "img 16 left, plain", ["16:L:26-26"], "", ""),
    ("Sept ye 26th Sunday", "img 16 right, plain, faint", ["16:R:1-2"], "", ""),
    ("Oct ye 4th 1779", "img 16 right; second alphabet", ["16:R:3-13"], "Long first writes two rows of signs and nothing else (18 + 7 = 25 signs, no letters beside them), taken as his new alphabet in order, a-s and t-z, with no sign for j; the letter values are inferred from that order and checked against words.", ""),
    ("Oct [8th?]", "img 16 right; second alphabet", ["16:R:14-22"], "", ""),
    ("Octr ye 6th", "img 17 left; second alphabet", ["17:L:1-6"], "", ""),
    ("Octr 7th", "img 17 left, plain", ["17:L:7-7"], "", ""),
    ("Sunday Octr 10th", "img 26, plain", [], "A small scirmish happend, we took 5 Hessians. Same night a fleet arrived from York. Wednesday Octr 13 the Enemy are embarking their Cannon and best Stores.", ""),
    ("Octr 12th Tuesday", "img 26; second alphabet", ["26:-:1-4"], "", ""),
    ("Wednesday 11th of Octr", "img 26, plain", [], "A deserter came down from Butts Hill to the Island ferry; they [pursued] him, shot him 5 or 6 times, left him for dead with a bayonet in him; our boat guard went and took him off. He is like to do well. Four more came with him by the Centries but never got off as I know of.", ""),
    ("Octr 16th and 21st", "plain", [], "Orders for 2 days allowance to be cooked on hand continually. 21st The Regt on fatigue putting plank & timber into the water at Howlands ferry; a number of cannon fired ... The enemy have been tearing their fort at Bristol ferry.", ""),
    ("Octr 22nd", "img 25 left; second alphabet", ["25:L:1-7"], "Last evening there was an express came to Capt. Runals to march to the ferry; this morning about 3 o'clock he marched his Company, left me with Voluntine Leighton, Theodore Fuller, Neal Cate & (the Waggoner) Ezekiel Flanders to take care of the Camp Equipage, his baggage & writings & to receive orders concerning the same. Yesterday being ye 21st of Octr according to Ensn Runals order our Company were put under Guard: Phineas Bean & Neal Cate remaind there the space of half a day.", ""),
    ("Octr 25th - Nov 1st", "img 25 right, plain", [], "Capt Runals returned the same day ... Octr 25th Capt Runals marched to the ferry this morning about 7 o'clock, joind the Regt and landed upon the Island in the afternoon. The Enemy retreated from Butts Hill about half past 12 o'clock A.M. I came after, got to the ferry towards night with the baggage. 26th towards night we crossed with our baggage (& joind the army). 27th we marched down to Newport, got there just at night. The nights of ye 26th & 27th ... over our baggage and conducted it to Newport. Newport Octr 29th Fatigue men drawn out to demolish the Enemy's fortification here. The Enemy embarked ye 25th Inst. about 8 o'clock P.M. and set sail immediately. Novr 1st Capt Runals began to make his abstracts.", ""),
    ("Novr 8th - Dec", "img 24; second alphabet in a few words", ["24:L:1-8"], "We marched to the lower part of the Town, went into an old house ...", "11th our Company mustered; 17th a Snow Storm, ye first snow that we've had. Novr 19th a Flag of Truce from York; 20th a Brig from Georgia arrived here thinking the Enemy were here, were made prisoners and sent to Providence. Decr 6th a smart snow storm ... the Majors house took fire ... put out by the engine ... 16th All the Company except Capt., Lieut., Sergt, Corpl & eleven privates marched to Tiverton this morning, snow storm."),
    ("Decr 1779 - Jan 1780", "img 23, plain", [], "Discharges (Nathl Patten, Isaac Clement); 23rd turned in our camp equipage and marched for Providence; stopt at Warren; I dreamd that we were in the army at Newport ...; 26th arrived at Providence and were put into the workhouse ...; 4th [Jan] some more set out; 6th Mr Hills and I set out for home ... 8th got to good quarters ... terrible times for poor soldiers, we have had to break a path almost all the way from Providence; 9th to the uppermost part of Wrentham; 10th to Dedham; ... Wilmington; ... Monday ... Tuesday ... Wednesday 18th got home.", ""),
]
ENTRIES_1780 = [
    ("June 28th 1780", "img 18 right (17 left upside down)", ["18:R:1-6"], "", ""),
    ("July 27th 1780", "img 22 left", ["22:L:1-22"], "", "Two struck lines follow."),
    ("Decr 22nd [1780]", "img 18 right", ["18:R:7-8"], "", ""),
    ("Accounts and road lists 1779-1780", "imgs 19-21, 27-28", ["28:-:1-4"], "Plain except a few cipher items. Image 28:", ""),
]

MODERN = {'ye': 'the', 'Ye': 'The', 'Augt': 'August', 'Octr': 'October', 'Oct': 'October', 'Novr': 'November', 'Decr': 'December',
          'Sept': 'September', 'Sergt': 'Sergeant', 'sergt': 'sergeant', 'Corpl': 'Corporal', 'corpl': 'corporal', 'Capt': 'Captain',
          'capt': 'captain', 'Col.': 'Colonel', 'Regt': 'regiment', 'Ensn': 'Ensign', 'joind': 'joined', 'remaind': 'remained',
          'dreamd': 'dreamed', 'dreamed=': 'dreamed', 'Tivertown': 'Tiverton', 'Tiver-town': 'Tiverton', 'Seaconet': 'Sakonnet',
          'Barricks': 'barracks', 'drawed': 'drew', 'Thirsday': 'Thursday', 'scirmish': 'skirmish', 'happend': 'happened',
          'Centries': 'sentries', 'Sentinal': 'sentinel', 'killd': 'killed', 'stopt': 'stopped', 'dressd': "dressed",
          'uper': 'upper', 'newbury': 'Newbury', 'kimball': 'Kimball', 'kimballs': "Kimball's", "kimball's": "Kimball's",
          'bartletts': "Bartlett's", 'uncle': 'uncle', 'Runals': 'Runnels', 'Enemys': "Enemy's", 'century': 'century [sentry]',
          'ask\'d': 'asked', "look'd": 'looked', 'nelly': 'Nelly', 'nessy': 'Nessy', 'Hannah': 'Hannah', 'Provi': 'Provi-'}


def load_lines():
    L = {}
    for line in open(HERE / 'reconciled_source.txt', encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        img, side, ln, alph, toks = line.rstrip('\n').split('\t', 4)
        L[(img, side, ln)] = (alph, toks)
    return L


def tokens(alph, toks):
    """Yield (kind, text): kind plain, cipher, note, mark."""
    if alph == '-' or toks.startswith('('):
        for p in re.findall(r'\{[^}]*\}|\([^)]*\)|\S+', toks):
            if p.startswith('{'):
                yield from plain_parts(p[1:-1])
            elif p.startswith('('):
                yield ('note', p)
            else:
                yield ('plain', p)
        return
    for p in re.findall(r'\{[^}]*\}|<del:[^>]*>|<ins:[^>]*>|<box:[^>]*>|\([^)]*\)|\S+', toks):
        if p[:5] in ('<ins:', '<del:', '<box:'):
            tag = {'ins': 'ins', 'del': 'struck', 'box': 'box'}[p[1:4]]
            yield ('open', tag)
            for w in re.findall(r'\{[^}]*\}|\S+', p[5:-1]):
                if w.startswith('{'):
                    yield ('plain', w[1:-1])
                else:
                    yield from word(w)
            yield ('close', tag)
        elif p.startswith('{'):
            yield from plain_parts(p[1:-1])
        elif p.startswith('('):
            yield ('note', p)
        else:
            yield from word(p)


def plain_parts(s):
    for m in re.findall(r'<del:[^>]*>|<ins:[^>]*>|\S+', s):
        if m.startswith('<'):
            yield ('plain', '[%s: %s]' % ({'del': 'struck', 'ins': 'ins'}[m[1:4]], m[5:-1]))
        else:
            yield ('plain', m)


def word(w):
    if w.startswith('{'):
        yield ('plain', w.strip('{}'))
        return
    if w in (',', ';', '&', '---', '----', ':', '.', ')'):
        yield ('mark', w)
        return
    if w == '?':
        yield ('cipher', '[?]')
        return
    if w.startswith('#'):
        yield ('cipher', '[nonsense]')
        return
    q = ''
    if w.endswith('??'):
        q, w = '??', w[:-2]
    elif w.endswith('?'):
        q, w = '?', w[:-1]
    if w.startswith('='):                      # continuation of a word split at the line end
        dec = w[1:].split('=', 1)[0]
    elif w.endswith('=') and w.count('=') == 1:  # first half of a split word
        dec = w[:-1] + '-'
    else:
        dec = w.split('=', 1)[0]
    yield ('cipher', '[%s%s]' % (dec, q) if q else dec)


UNREAD = '[?]'          # one unread cipher word, as it comes from reconciled_source.txt ("?")
PLAIN_GAP = '[...]'     # plain words the first agents did not transcribe: extent unknown (README, 14 Nov 2026)


def hole(n):
    """Holes are counted by words (README Conventions, 14 Nov 2026): [...] is one unread word, [... n] is n."""
    return '[...]' if n == 1 else '[... %d]' % n


def size_holes(out):
    """Merge each run of consecutive unread cipher words into one mark carrying the number of words. A run is broken
    by anything else (a read word, plain text, a mark, an interlineation or a struck word), so the size is exactly the
    number of "?" tokens of reconciled_source.txt under it."""
    res, run = [], 0
    for t in out + [None]:
        if t == UNREAD:
            run += 1
            continue
        if run:
            res.append(hole(run))
            run = 0
        if t is not None:
            res.append(t)
    return res


def plain_gaps(text):
    """A bare '...' in plain text (words not transcribed in full) becomes the bare mark [...], extent unknown."""
    return re.sub(r'(?<!\[)\.\.\.(?!\])', PLAIN_GAP, text)


def render(entry_ranges, L, modern):
    # \x01 opens and \x02 closes a cipher run
    out = []
    incipher = False
    for rng in entry_ranges:
        img, side, span = rng.split(':')
        a, b = span.split('-')
        keys = [k for k in L if k[0] == img and k[1] == side and (
            (a == 'margin' and k[2] == 'margin') or (a != 'margin' and k[2] != 'margin' and int(a) <= int(k[2]) <= int(b)))]
        keys.sort(key=lambda k: (k[2] == 'margin', k[2]))
        for k in keys:
            alph, toks = L[k]
            tl = list(tokens(alph, toks))
            for i, (kind, text) in enumerate(tl):
                look = tl[i + 1][0] if kind == 'open' and i + 1 < len(tl) else None
                if modern and kind in ('plain', 'cipher'):
                    core = text.strip('[]?')
                    if core in MODERN:
                        text = text.replace(core, MODERN[core], 1)
                if (kind == 'cipher' or look == 'cipher') and not incipher:
                    out.append('\x01')
                    incipher = True
                elif (kind in ('plain', 'note') or look in ('plain', 'note')) and incipher:
                    out.append('\x02')
                    incipher = False
                if kind == 'open':
                    out.append('[%s: ' % text)
                elif kind == 'close':
                    out.append(']')
                else:
                    out.append(plain_gaps(text) if kind == 'plain' else text)
    if incipher:
        out.append('\x02')
    out = size_holes(out)
    s = ''
    for t in out:
        if t == '\x02':
            s = s.rstrip(' ') + ('*' if modern else '⟧') + ' '
        elif t == '\x01':
            s += '*' if modern else '⟦c: '
        elif t == ']':
            s = s.rstrip(' ') + '] '
        elif t in ('⟦c: ',) or t.startswith('['):
            s += t if t.startswith('[') and t.endswith(': ') else t + ('' if t.endswith(' ') else ' ')
        else:
            s += t + ' '
    s = re.sub(r'- ([a-z])', r'-\1', s)          # words split at a line end (beau- ty)
    s = re.sub(r'\*\s+\*', ' ', s)
    s = re.sub(r'\s+([,.;:)])', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


HEAD_W = """# Enoch Long's journal, July 1779 - December 1780: day-by-day text

Generated by `scripts/build_journal.py` from `reconciled_source.txt` (the word-by-word reading; do not edit this file by
hand). Source: National Archives, M804 roll 1580, pension file W. 16138 (Enoch Long, widow Molly), images 11-31. The
notebook pages are photographed out of order; entries are put in date order here, with the image number.

Conventions: plain text as written, his spelling kept. ⟦c: ...⟧ = written in cipher, deciphered by our agents. A word in
brackets with one question mark, [word?], is probable; with two, [word??], doubtful. Holes are counted by words: in
cipher, [...] is one word not read and [... n] is n words not read in a row, counted from the "?" tokens of
`reconciled_source.txt` (one per unread cipher word; 206 in all). In plain text a bare [...] marks words the first
agents did not transcribe: extent unknown; so are the struck heading of image 19 left and the margin column of image 11
(about 30 signs, not counted in words). [struck: ...] and [ins: ...] are struck and interlined words. "a/b" gives two
words the signs allow. Read by AI agents only, from the microfilm; no person has checked these readings against the
images. See NOTES.md, "How sure the reading is".

"""
HEAD_M = """# Enoch Long's journal, 1779-1780, modernized for reading

Generated by `scripts/build_journal.py` from `reconciled_source.txt`, the same source as `journal_as_written.md`. Only
spelling and abbreviations are changed; passages he wrote in cipher are in *italics*, and every gap and doubt mark is
kept: [word?] probable, [word??] doubtful. Holes are counted by words: in cipher, [...] is one word not read and
[... n] is n words not read in a row (counted from `reconciled_source.txt`, 206 in all); in plain text a bare [...]
marks words not transcribed, extent unknown, as are the struck heading of image 19 left and the margin column of image
11. Read by AI agents only; no person has checked these readings against the images.

"""


def build(modern):
    L = load_lines()
    parts = [HEAD_M if modern else HEAD_W]
    for year, ents in (('1779', ENTRIES_1779), ('1780', ENTRIES_1780)):
        parts.append('## %s\n\n' % year)
        for head, where, ranges, before, after in ents:
            body = ' '.join(x for x in (plain_gaps(before), render(ranges, L, modern) if ranges else '', plain_gaps(after)) if x)
            h = head
            if modern:
                for k, v in MODERN.items():
                    h = re.sub(r'\b%s\b' % re.escape(k), v, h)
            parts.append('- **%s** (%s). %s\n' % (h, where, body))
        parts.append('\n')
    return ''.join(parts).rstrip('\n') + '\n'


if __name__ == '__main__':
    (HERE / 'journal_as_written.md').write_text(build(False), encoding='utf-8')
    (HERE / 'journal_modernized.md').write_text(build(True), encoding='utf-8')
    print('wrote journal_as_written.md and journal_modernized.md')
