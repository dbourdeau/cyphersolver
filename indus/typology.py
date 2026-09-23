"""Two grammar tests that need no sound values, against the candidate language families.

T1  Order in the possessive formula. On seals the name ends 'X 740 90': the ending, then the 'man'
    sign 90. If 740 marks the possessor and 90 is the head noun ('X's man'), the possessor comes
    first. Position of every 90 token: after 740, at the start of a text, elsewhere; and what
    follows it.
T2  Female names. Proto-Dravidian (masculine / non-masculine) would put a woman's title in the 520
    class; Tamil, Sumerian and Sanskrit (for a feminine title) differ. The woman-figure signs
    (Fairservis A-2 93, A-3 95/96) as the last sign of a name.
T3  The two tests with the ending class (noun_class.py) against the families' typology. The
    typological facts are textbook ones (Dravidian: Krishnamurti 2003, The Dravidian Languages;
    Sumerian: Thomsen 1984 / Jagersma 2010; Elamite: Stolper 2004 in the Cambridge Encyclopedia of
    the World's Ancient Languages; Munda: Hoffmann 1903 Mundari Grammar, read here; Burushaski:
    Berger 1998; Sanskrit: Whitney).

Writes results/typology.md.
"""
import os
from collections import Counter

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def split_end(t):
    if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
        return tuple(t[:-2]), t[-2]
    if len(t) >= 2 and t[-1] in ('740', '520'):
        return tuple(t[:-1]), t[-1]
    return None, None


def main():
    rows = [r for rs in (load(), load(only_m77=True)) for r in rs if r['flat']]
    say('# Word order and female names: two grammar tests')
    say()
    say('## T1 The possessive formula')
    say()
    pos, prev, nxt = Counter(), Counter(), Counter()
    for r in rows:
        for ln in r['seq']:
            for i, g in enumerate(ln):
                if g == '90':
                    pos['text-initial' if i == 0 else ('text-final' if i == len(ln) - 1 else 'inside')] += 1
                    prev[ln[i - 1] if i else '(start)'] += 1
                    nxt[ln[i + 1] if i < len(ln) - 1 else '(end)'] += 1
    n = sum(pos.values())
    say('- the man sign 90, %d tokens (ICIT-derived and M77 additions): %s. Before it: %s. After it: %s.' % (
        n, ', '.join('%s %d' % kv for kv in pos.most_common()), ', '.join('%s %d' % kv for kv in prev.most_common(6)),
        ', '.join('%s %d' % kv for kv in nxt.most_common(6))))
    say('- %d of %d tokens (%.0f%%) stand right after the ending 740; %d (%.0f%%) open a text. The formula is "X-740 '
        'man", the possessor (or the name with its personal suffix) first and the head noun last. A language that '
        'puts the head noun first and the possessor after it, "man X-GEN" (Sumerian lu2 X-ak; the cuneiform "lu2 '
        'me-luh-ha", man of Meluhha), would write the man sign first.' % (
            prev['740'], n, 100 * prev['740'] / n, pos['text-initial'], 100 * pos['text-initial'] / n))
    ini = Counter(' '.join(ln) for r in rows for ln in r['seq'] if ln and ln[0] == '90')
    man_first = [t for t in ini if len(t.split()) >= 3 and t.split()[-1] in ('740', '520') and t.split()[1] != '90']
    say('- the texts that open with 90: %s. A "man + name + ending" text, the head-first order: %d (%s).' % (
        '; '.join('%s x%d' % (t, k) for t, k in ini.most_common(6)), len(man_first), '; '.join(man_first) or 'none'))
    say()
    say('## T2 Female names')
    say()
    for g, lab in (('93', 'woman, ribbed hat (A-2)'), ('95', 'woman, hood (A-3)'), ('96', 'woman, variant (A-3)')):
        fin, any_ = Counter(), Counter()
        for r in rows:
            for ln in r['seq']:
                s, e = split_end(ln)
                if s and s[-1] == g:
                    fin[e] += 1
                if s and g in s:
                    any_[e] += 1
        say('- %s %s: %d tokens; as the last sign of a name: %s; anywhere in a name: %s.' % (
            g, lab, sum(r['flat'].count(g) for r in rows), dict(fin) or 'never', dict(any_) or 'never'))
    say('- Four names in all: too few to test whether women\'s titles take 520 (Proto-Dravidian) or 740 (Tamil, '
        'Sumerian).')
    say()
    say('## T3 The grammar tests against the families')
    say()
    say('| family | a class suffix on the singular noun, persons against stars (ending class, noun_class.py) | '
        'possessor before head ("X-740 man") | both |')
    say('|---|---|---|---|')
    say('| Dravidian | yes: gender-number suffixes on the noun itself (-an masc., -am / -tu non-masc.), rational / '
        'non-rational in Tamil | yes: the genitive precedes its head | **yes** |')
    say('| Indo-Aryan (Sanskrit) | in part: gender shows in the stem ending, but three genders across many declension '
        'endings, and the nakshatras are mostly feminine, some masculine and neuter | yes, as a rule (rajnah purusah) | '
        'in part |')
    say('| Munda | no: animacy shows only in dual and plural forms; heavenly bodies are animate like persons '
        '(Hoffmann 1903) | yes | no |')
    say('| Burushaski | no: four classes (human masc., human fem., x, y) shown by agreement and plural suffixes, not by '
        'a suffix on the singular noun | yes | no |')
    say('| Sumerian | no: human / non-human shows in pronouns, verb agreement and the human plural -ene, not on the '
        'singular noun | no: head first, lu2 X-ak | no |')
    say('| Elamite | yes: animate -r (3rd sg.) against inanimate -me | no: head first, modifiers and possessors '
        'after it | no |')
    say()
    say('On these two tests only Dravidian fits outright; Indo-Aryan fits in part. The result is conditional: it '
        'assumes that 740 and 520 are suffixes of the name (they are fixed per name, final, and bound to it, '
        'segment.py), that 90 is a head noun (the man sign) and that the fish names are stars. Each step has its own '
        'evidence in this folder; none is proven.')
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'typology.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
