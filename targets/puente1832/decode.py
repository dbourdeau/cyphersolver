"""Vowel-mask key for CEHM I-2.5.340.1 (Puente Nacional, 6 Jun 1832). Consonants are written plain.
Usage: python decode.py transcription.txt   (or: python decode.py "p-r- l- ispir-nz-")
Capital X in the transcription is a real letter x; "V.E." is passed through; [..] is unread."""
import sys
KEY = {'-': 'a', 'i': 'e', 'x': 'i', '.': 'o'}   # u is written u
def dec(s):
    return ' '.join(w if w == 'V.E.' else ''.join(KEY.get(c, c) for c in w).replace('X', 'x') for w in s.split())
if __name__ == '__main__':
    a = sys.argv[1]
    try:
        for l in open(a, encoding='utf8'):
            if l[:1] == 'L':
                h, _, s = l.rstrip('\n').partition(' ')
                print(h, dec(s))
    except OSError:
        print(dec(a))
