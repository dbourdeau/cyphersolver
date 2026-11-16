"""Apply the Morier 1808 key (key.json) to the transcriptions; writes decryption_*.txt.
'.' ends a word, ',' joins figures within a word. 3-4 figure groups are nomenclator words: 8674 = Persia,
4040 = French (probable), 630 = Bombay (probable). Unknown figures print as [n].   python3 decode.py"""
import json, re, pathlib
D = pathlib.Path(__file__).resolve().parent
KEY = json.load(open(D / 'key.json'))['map']
KEY.update({'88': 'z', '94': 'e'})  # added after the measures: authori[z]ed (88), therefor[e] (94); see NOTES.md
CODE = {'8674': '{PERSIA}', '4040': '{FRENCH?}', '630': '{BOMBAY?}', '24': '24'}
def decode(path):
    out = []
    for line in open(path):
        if line.startswith('#'): out.append(line.rstrip()); continue
        if line.startswith('@'): out.append(line.rstrip()); continue
        s = ''
        for t in re.findall(r'\[del\]|\d+|\.|,', line.replace('?', '')):
            s += {'.': ' ', ',': ''}.get(t, '_' if t == '[del]' else CODE.get(t, KEY.get(t, '[' + t + ']')))
        out.append(s.rstrip())
    return '\n'.join(out) + '\n'
for src, dst in [('transcription_18_part1.txt', 'decryption_18_part1.txt'),
                 ('transcription_18_f6v-f7v.txt', 'decryption_18_f6v-f7v.txt'),
                 ('transcription_20.txt', 'decryption_20.txt'), ('transcription_21.txt', 'decryption_21.txt')]:
    (D / dst).write_text(decode(D / src))
