"""Write the decryption / trial files listed in profile.json outcome.texts (14 Nov 2026). Standard library only.

    python trials.py

f10_decryption.txt       f10_transcription.txt with the fixed values of Digby key no. 129 (aaymeloglu_f10/key129.txt)
                         put over their groups, line by line; a partial decode, not a reading.
maurice1645_trials.txt, f9_trials.txt, trevor1645_trials.txt
                         the transcription under the two letter tables held in this folder that were tried on
                         9 Oct 2026 and do not fit (key 118 in keys.py, key 125 in test_letters.py). They record the
                         failed trials; they are not decryptions. The other keys tried (NOTES.md, Escalation) are on
                         DECODE or in sibling folders and are not replayed here.
"""
import os, re
import keys, test_letters

H = os.path.dirname(os.path.abspath(__file__))
BANDS = [('A', 91, 107), ('B', 109, 122), ('C', 123, 141), ('D', 142, 158), ('E', 159, 175), ('F', 176, 192),
         ('G', 193, 205), ('H', 209, 224), ('I/J', 225, 239), ('K', 241, 249), ('L', 257, 272), ('M', 273, 288),
         ('N', 289, 303), ('O', 304, 316), ('P', 317, 333), ('Q', 334, 343), ('R', 344, 361), ('S', 362, 379),
         ('T', 380, 393), ('V', 394, 408), ('W', 409, 422), ('Y', 423, 430), ('Z', 431, 434)]  # keys.py, key 118


def k118(n):
    if n in keys.K118_LET: return keys.K118_LET[n]
    if n in keys.K118_NULLS: return '·'
    for b, lo, hi in BANDS:
        if lo <= n <= hi: return '<%s-word %d>' % (b, n)
    return '<%d>' % n


def k125(n):
    v = test_letters.K125.get(n)
    return ('·' if v == '.' else v) if v is not None else '<%d>' % n


def apply(line, f):
    out = []
    for g in re.findall(r'\[[^\]]*\]|\S+', line):
        m = re.match(r'^(\d+)(\??)$', g)
        out.append(f(int(m.group(1))) + m.group(2) if m else g)
    return ' '.join(out)


def trials(src, dst, title):
    lines = [l.rstrip('\n') for l in open(os.path.join(H, src), encoding='utf8')]
    body = [l for l in lines if l.strip() and not l.startswith('#')]
    out = ['# %s' % title,
           '# Not a decryption: no key fits this text. Two failed trials are shown, made with the letter tables held in this folder',
           '# (trials.py, 14 Nov 2026, replaying the 9 Oct 2026 tests). [..] = clear words of the source, · = a null of the table,',
           '# <n> = a group the table gives no value, <X-word n> = a group in the word band of initial X of key 118.',
           '', '## Trial 1: key 118, "Cypher for Ormond & Prince Rupert" (Add MS 72438 ff. 59-60, R8655): letters 1-80, nulls 81-90, words 91-434']
    out += [apply(l, k118) for l in body]
    out += ['', '## Trial 2: letter table of key 125, "Mr Browne\'s cypher" (Add MS 72438 f. 70), numbers 2-79']
    out += [apply(l, k125) for l in body]
    open(os.path.join(H, dst), 'w', encoding='utf8', newline='').write('\n'.join(out) + '\n')


def f10():
    key = {}
    for line in open(os.path.join(H, 'aaymeloglu_f10', 'key129.txt'), encoding='utf8'):
        m = re.match(r'^(\d+) (\S+)', line)
        if m: key[int(m.group(1))] = m.group(2)
    n = hit = 0
    out = ['# BL Add MS 72438 f. 10 (DECODE R8624), 13 May 1646: f10_transcription.txt with the fixed values of Digby key no. 129',
           '# (aaymeloglu_f10/key129.txt, Andrew Aymeloglu, issue #554) put in place of their groups, line by line (trials.py, 14 Nov 2026).',
           '# A partial decode shown for checking, not a reading: groups with no value in the key stay as numbers.',
           '# [..] = clear words of the letter; ? = doubtful group; ... = torn or illegible.']
    for l in open(os.path.join(H, 'f10_transcription.txt'), encoding='utf8'):
        l = l.rstrip('\n')
        if l.startswith('#') or not l.strip():
            if l.startswith('# ---'): out.append(l)
            continue
        toks = []
        for g in re.findall(r'\[[^\]]*\]|\S+', l):
            m = re.match(r'^(\d+)(\??)$', g)
            if m:
                n += 1
                v = key.get(int(m.group(1)))
                if v: hit += 1
                toks.append((v + m.group(2)) if v else g)
            else:
                toks.append(g)
        out.append(' '.join(toks))
    out.insert(4, '# %d of %d whole groups take a value (%.1f%%).' % (hit, n, 100 * hit / n))
    open(os.path.join(H, 'f10_decryption.txt'), 'w', encoding='utf8', newline='').write('\n'.join(out) + '\n')


if __name__ == '__main__':
    f10()
    trials('maurice1645_groups.txt', 'maurice1645_trials.txt', 'Maurice to Rupert, Worcester, 7 July 1645 (Warburton iii. 133): failed key trials')
    trials('f9_transcription.txt', 'f9_trials.txt', 'BL Add MS 72438 f. 9r (DECODE R8623), 21 May 1646: failed key trials')
    trials('trevor1645_transcription.txt', 'trevor1645_trials.txt', 'BL Add MS 18982 ff. 51-52 (DECODE R8433), Trevor to Rupert, [28] April 1645: failed key trials')
