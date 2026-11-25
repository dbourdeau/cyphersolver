"""Decode the glossed letters 438R-440L and 444R mechanically (14 Nov 2026). Standard library only.

    python decode_glossed.py        writes decryption_438-440.txt and decryption_444R.txt

Each cipher element (# followed by numbers or signs, joined by dots) of transcription_438R/439L/439R/440L/444R.txt is replaced:
a number 10-99 by its letter in key.tsv (nulls dropped), a code group or sign by the gloss of the time recorded for it on the same image in
codes_438-444.tsv, else on another image of that file, else in codes.tsv. Marks: {x} = from a gloss (x? when its status is not 'sure' or it comes
from another image); ‹n› = no value; ‹+x› = a raised ending or half sign written with the group. Clear text is left as transcribed. Nothing is inflected or repaired: this is a check, not a reading.
"""
import pathlib, re

H = pathlib.Path(__file__).resolve().parent
LET, NULL = {}, set()
for l in (H / 'key.tsv').read_text(encoding='utf8').splitlines():
    m = re.match(r'# nulls: ([\d ]+)', l)
    if m: NULL = set(m.group(1).split())
    m = re.match(r'(\d\d)\t([a-z])', l)
    if m: LET[m.group(1)] = m.group(2)
G = {}   # (code, image) -> (gloss, status)
for l in (H / 'codes_438-444.tsv').read_text(encoding='utf8').splitlines():
    if l.startswith('#') or l.startswith('code\t') or not l.strip(): continue
    c, g, im, st = (l.split('\t') + ['', '', ''])[:4]
    G.setdefault((c, im), (g, st)); G.setdefault((c, None), (g, st))
G2 = {}
for l in (H / 'codes.tsv').read_text(encoding='utf8').splitlines():
    if l.startswith('#') or l.startswith('code\t') or not l.strip(): continue
    c, g = l.split('\t')[:2]
    G2[c] = g


def elem(e, image):
    out = ''
    for part in e.split('.'):
        if not part: continue
        if re.fullmatch(r'\d\d', part) and (part in LET or part in NULL):
            out += LET.get(part, '')
            continue
        m = re.fullmatch(r'(\d+)([^\d.]+)', part)   # a code written with a raised ending or a half sign: try the whole, then the bare number
        suf = ''
        if m and (part, image) not in G and (part, None) not in G and part not in G2:
            part, suf = m.group(1), '‹+%s›' % m.group(2)
        if (part, image) in G:
            g, st = G[(part, image)]; out += ' {%s%s} ' % (g, '' if st == 'sure' else '?')
        elif (part, None) in G:
            out += ' {%s?} ' % G[(part, None)][0]
        elif part in G2:
            out += ' {%s?} ' % G2[part]
        else:
            out += ' ‹%s› ' % part
        out = out.rstrip() + suf + ' ' if suf else out
    return out.strip()


def run(files, dst, title):
    out = ['# ' + title,
           '# Mechanical decode by decode_glossed.py (14 Nov 2026) for checking; not a reading. {x} = gloss of the time for the code group (x? = gloss not sure,',
           '# or taken from another image or from codes.tsv); ‹n› = no value; spelled words from the letter table of key.tsv as they come.']
    for f in files:
        image = re.search(r'_(\d+[LR])', f).group(1)
        out.append('## image ' + image)
        for l in (H / f).read_text(encoding='utf8').splitlines():
            out.append(re.sub(r'#([^\s,;:)]+)', lambda m: elem(m.group(1).rstrip('.'), image) + ('.' if m.group(1).endswith('.') else ''), l))
    (H / dst).write_text('\n'.join(out) + '\n', encoding='utf8', newline='')


run(['transcription_438R.txt', 'transcription_439L.txt', 'transcription_439R.txt', 'transcription_440L.txt'], 'decryption_438-440.txt',
    'Images 438R, 439L, 439R, 440L: letter and postscript to Gustav II Adolf, The Hague, 20/30 Sept 1630 (glossed original)')
run(['transcription_444R.txt'], 'decryption_444R.txt', 'Image 444R: to the Swedish secretary L. Grubbe, 20/30 Sept 1630 (glossed)')
