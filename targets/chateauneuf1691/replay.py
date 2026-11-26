"""Adapter for docs/_replay.py: key.tsv applied to transcription.txt, against reading.md.

Only the values attested in the decipherments of the time count as the key's output (status KEY_v1 or KEY_v2 in
key.tsv). The values and nulls fixed from the sentences alone (status "context-only": 11, 43, 103, 355, 365-368) are
given no value here, as in decryption.txt, so the reading has to mark what it takes from them. Groups cut by the
binding (###) have no value either. The clear text of the letters is left out on both sides: reading.md quotes it
only in part. The cipher runs on without word division, so words are counted over the reading.

Three things follow the "Spelling" paragraph in the header of reading.md and the notes (NOTES.md, "Key replay"):
- 47 and 49 are s in key.tsv and also z in the glossed letters (trouuez, obligez, reputez, jugez, donnerez, auez):
  declared as polyphony.
- 110 is "che" in key.tsv and "he" in the three glossed words that hold it (Carat-c-he, tru-c-he-ment, a-c-he-ter):
  compared as "he".
- The word codes 145 (turc), 174 (republic) and 335 (vou) are printed in the reading as Turcs, République and vous;
  they are compared in the key's own form.
A word that reading.md prints in {braces} as probable is compared as a marked word.
Written at the write-up of 24 Nov 2026 (AI agent, for the maintainers).
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIVIDED = False
SOURCES = {'key': 'key.tsv', 'transcription': 'transcription.txt', 'reading': 'reading.md'}
POLYPHONY = {'47': ['z'], '49': ['z']}
GLOSS_VALUE = {'110': 'he'}
WORD_CODE_FORMS = [('Turcs', 'Turc'), ('République', 'Republic'), ('vous', 'vou')]
# the words reading.md prints in {braces} as probable; every other {brace} there is clear text of the letter
PROBABLE = ['ici', 'résolution', 'y', 'désister', 'consentement', "j'eusse", 'recevoir']


def _key():
    key = {}
    for line in open(os.path.join(HERE, 'key.tsv'), encoding='utf-8').read().split('\n')[1:]:
        c = line.rstrip('\r').split('\t')
        if len(c) >= 3 and 'context' not in c[2]:
            key[c[0]] = GLOSS_VALUE.get(c[0], c[1])
    return key


def mechanical():
    key, out, cur = _key(), [], None
    for line in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8'):
        line = line.rstrip('\r\n')
        m = re.match(r'# LETTER (f\.\d+)', line)
        if m:
            cur = []
            out.append((m.group(1).replace('f.', 'f. '), [cur]))
            continue
        if not re.match(r'^\d{4}\|', line) or cur is None:
            continue
        body = re.sub(r'\{[^}]*\}', ' ', line.split('|', 3)[3])
        for t in body.split():
            m = re.match(r'^(\d+)', t)
            n = m.group(1) if m else ''
            if '###' in t or not m:
                cur.append((n + '###', None))
            else:
                cur.append((n, key.get(n)))
    return out


def reading():
    txt = open(os.path.join(HERE, 'reading.md'), encoding='utf-8').read().replace('\r', '')
    out = {}
    for sec in re.split(r'\n## ', txt)[1:]:
        m = re.match(r'(f\. \d+)', sec)
        if not m:
            continue
        body = sec.split('\n', 1)[1]
        parts = []
        for para in re.split(r'\n(?=\d+\. )|\n\n', body):
            para = re.sub(r'^\d+\.\s+', '', para.strip())
            para = para.split('—')[0]                       # the count and the notes follow the dash
            if para.startswith('f. ') or not para.strip():
                continue
            parts.append(para)
        t = ' '.join(parts)
        for w in PROBABLE:
            t = t.replace('{%s}' % w, '[%s]' % w)           # probable words: marked
        t = re.sub(r'\{[^}]*\}', ' ', t)                    # clear text of the letter
        t = t.replace('‹na-64›', 'na #')
        t = re.sub(r'‹[^›]*›', '#', t)                      # groups with no value
        for printed, keyform in WORD_CODE_FORMS:
            t = re.sub(r'\b%s\b' % printed, keyform, t)
        out[m.group(1)] = t
    return out
