"""Decipher the number cipher of GLC01523 (Burr to Alston) and measure the reading.

System: Vigenere over the alphabet numbered a=1 ... z=26, period 6, the key running on
continuously through the letters of a section (word spaces do not advance it; each ruled
section of img1 and the img2 sheet start again at the first key place).
    cipher = plain + shift (mod 26, written 1..26);  shifts = 6, 18, 22, 7, 24, 8
(as letters a=0: G S W H Y I).

Usage: python decrypt.py            print the deciphered lines
       python decrypt.py --measure  also count the cipher numbers that give sense
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
SHIFTS = [6, 18, 22, 7, 24, 8]          # recovered from the ciphertext (NOTES.md)
START = {'img1.A': 0, 'img1.B': 0, 'img1.C': 0, 'img2': 0}

# Readings that need a comment. key: (section, cipher group as written) -> (reading, note).
# 'emend' = one number disagrees with the key and the word is read from context;
# 'unread' = no sense.
NOTES = {
    ('img1.A', '15,16'): ('in', 'emend: 15,16 gives "ix"; the key needs 15,6 (Burr wrote 16 for 6, or a misreading)'),
    ('img1.A', '18,5'): ("j'y", 'Burr writes 18,5 = "jy" (French: j’y travaille)'),
    ('img1.B', '10,11,_,16'): ('be[s]t', 'Burr left out the s: 10,11,16 = b,e,t with the key moved on'),
    ('img1.B', '15,5,12,2,25,11,26,1,25,8,26,20,11'): ('impracticable', 'torn: 4th number torn at the edge after its 2; the key needs 25 for r, so 2[5]'),
    ('img1.B', '4,23,2'): ('for', 'torn: last number torn at the edge after its 2; the key needs 24 for r, so 2[4]'),
    ('img2', '16,7,11,1'): ('have', 'emend: 11 gives "hase"; the key needs 14 for v (11/14 misread or Burr’s slip)'),
    ('img2', '2,11,1,23'): (None, 'unread: middle number rubbed on a fold; the key falls back one place after it'),
    ('img2', '26,12,13,9,15,6,15'): ('detains', 'emend: 13 gives "deoains"; the key needs 18 for t (13/18 misread or Burr’s slip)'),
}


def parse(path=HERE / 'transcription.txt'):
    """Return {section: [(line_label, [word, ...]), ...]}; a word is a list of ints,
    with None for [om] (letter left out, key moves) and 'K-1' for a key fallback."""
    sections, carry = {}, None
    for raw in path.read_text(encoding='utf8').splitlines():
        if not raw.strip() or raw.startswith('#'):
            continue
        label, body = raw.split(':', 1)
        sec = label.rsplit('.', 1)[0] if label.count('.') == 2 else label.split('.')[0]
        body = re.sub(r'\[del [^\]]*\]', ' ', body)
        body = re.sub(r'\[above \d+\]', '', body)
        body = body.replace('[x]', ' ').replace('(', ' ').replace(')', ' ')
        body = re.sub(r'\[ins (\d+)\]', r'\1,', body)
        body = body.replace('[om]', 'OM').replace('[key -1]', ' KEYBACK ')
        words = []
        for tok in body.split():
            if tok == '-':
                continue
            if tok == 'KEYBACK':
                words.append('K-1')
                continue
            nums = [None if t == 'OM' else int(t) for t in re.findall(r'OM|\d+', tok)]
            if not nums:
                continue
            if tok.startswith('=') and carry is not None:
                nums, carry = carry + nums, None
            if tok.endswith('='):
                carry = nums
                continue
            words.append(nums)
        sections.setdefault(sec, []).append((label, words))
    return sections


def run(measure=False):
    secs = parse()
    tot = sense = 0
    out_lines = []
    for sec, lines in secs.items():
        k, wi = START[sec], 0
        for label, ws in lines:
            plain, cipher = [], []
            for w in ws:
                if w == 'K-1':
                    k -= 1
                    continue
                s = ''
                for n in w:
                    s += '_' if n is None else chr(97 + (n - 1 - SHIFTS[k % 6]) % 26)
                    k += 1
                nn = sum(n is not None for n in w)
                note = NOTES.get((sec, ','.join('_' if n is None else str(n) for n in w)))
                tot += nn
                if note and note[0] is None:
                    plain.append('{' + ','.join(map(str, w)) + '}')
                else:
                    sense += nn
                    plain.append(note[0] + '[?]' if note and note[1].startswith('emend') else
                                 (note[0] if note else s))
                cipher.append(','.join('_' if n is None else str(n) for n in w))
                wi += 1
            out_lines.append((label, ' '.join(cipher), ' '.join(plain)))
    for label, c, p in out_lines:
        print(f'{label:10s} {p}')
    if measure:
        print(f'\nnumbers: {tot}; giving sense: {sense} ({100 * sense / tot:.1f}%)')
        print('emended or annotated words:')
        for (sec, c), (r, n) in NOTES.items():
            print(f'  {sec} {c}: {r or "-"}  ({n})')
    return out_lines, tot, sense


if __name__ == '__main__':
    run('--measure' in sys.argv)
