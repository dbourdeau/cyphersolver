"""Apply the frozen key verification/key_v1.tsv to transcription_400.txt, sign by sign, nothing edited.

Case is ignored (V and B are the clerks' capitals). A sign whose key value is empty is a null, printed as '·'.
A sign with no value in the key is printed in angle quotes, ‹z›. Writes decryption_400.txt.
"""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
key = {}
for line in (HERE / 'verification' / 'key_v1.tsv').read_text(encoding='utf-8').splitlines():
    if not line or line.startswith('#'):
        continue
    c, _, p = line.partition('\t')
    key[c] = p
groups = [l for l in (HERE / 'transcription_400.txt').read_text(encoding='utf-8').splitlines()
          if l.strip() and not l.startswith('#')]
cipher = ''.join(groups).replace(' ', '')
out = []
for s in cipher.lower():
    if s not in key:
        out.append('‹' + s + '›')
    else:
        out.append(key[s] or '·')
text = ''.join(out)
(HERE / 'decryption_400.txt').write_text(
    '# HIL/64/400 (catalogue 2907): decryption, verification/key_v1.tsv applied to transcription_400.txt by\n'
    '# decode_400.py, sign by sign, nothing edited. · = null (empty key value); ‹x› = cipher sign with no value in the key.\n'
    + text + '\n', encoding='utf-8')
print(text)
