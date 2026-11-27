"""Word tables and marked texts of the strict count (catalogue 1616).

usage (from targets/duben1764/):
  python3 -I sysA_1616/close1616/scripts/make_tables.py
Runs strict_align.py twice per letter (key_c01 alone; key_c01 with key_c01_additions_1616.json) and writes, in
sysA_1616/close1616/:
  strict_<letter>.tsv          one row per witness word: line, word, class under key_c01, class with the additions,
                               groups and key values under it
  marked_<letter>.txt          the witness words in order, marked by the class with the additions:
                               word = sure; word° = sure on an added value; {word} = probable; [word] = restored
  gaps_<letter>.tsv            every group whose key value (key_c01, or an added value) gives other letters than the
                               decipherment of the time at that place, with the witness letters ('' = none)
  counts.json                  the counts
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SA = os.path.join(HERE, 'scripts', 'strict_align.py')
KEY = 'dudout/system_a/key_c01.json'
ADD = os.path.join(HERE, 'key_c01_additions_1616.json')
MARK = {'sure': '%s', 'sure_add': '%s°', 'probable': '{%s}', 'restored': '[%s]'}


def run(letter, extra):
    out = os.path.join(HERE, '.tmp_%s.json' % letter)
    subprocess.run([sys.executable, '-I', SA, letter, KEY] + extra + ['--json', out], check=True,
                   stdout=subprocess.DEVNULL)
    d = json.load(open(out))
    os.remove(out)
    return d


def main():
    counts = {}
    for letter in ('1764-03-06', '1765-11-15'):
        a, b = run(letter, []), run(letter, [ADD])
        wa, wb = a['words'], b['words']
        assert [w['w'] for w in wa] == [w['w'] for w in wb]
        rows = ['i\tline\tword\tclass_key_c01\tclass_with_additions\tgroups\tvalues']
        for x, y in zip(wa, wb):
            if y['class'] == 'outside':
                continue
            rows.append('\t'.join([str(y['i']), y['line'], y['w'], x['class'], y['class'], ' '.join(y['groups']),
                                   ' '.join(v or '?' for v in y['values'])]))
        open(os.path.join(HERE, 'strict_%s.tsv' % letter), 'w').write('\n'.join(rows) + '\n')
        lines, cur, buf = [], None, []
        for y in wb:
            if y['class'] == 'outside':
                continue
            if y['line'] != cur:
                if buf:
                    lines.append('%s %s' % (cur, ' '.join(buf)))
                cur, buf = y['line'], []
            buf.append(MARK[y['class']] % y['w'])
        lines.append('%s %s' % (cur, ' '.join(buf)))
        open(os.path.join(HERE, 'marked_%s.txt' % letter), 'w').write(
            '# %s: witness words in cipher order, classed with key_c01 + key_c01_additions_1616.json.\n'
            '# word = sure (key_c01); word° = sure on an added value; {word} = probable (key gives other letters);\n'
            '# [word] = restored (no key value, or no group: the decipherment of the time supplies it).\n' % letter
            + '\n'.join(lines) + '\n')
        g_rows = ['line\tgroup\tdoubtful\tkey_value\tsource\twitness_letters']
        for g in b['groups']:
            if g['kind'] == 'mis':
                g_rows.append('\t'.join([g['line'], g['g'], 'yes' if g['doubt'] else '', g['value'] or '',
                                          'key_c01' if g['src'] == 'key' else 'addition', g['witness']]))
        open(os.path.join(HERE, 'gaps_%s.tsv' % letter), 'w').write('\n'.join(g_rows) + '\n')
        counts[letter] = {'key_c01': a['summary']['counts'], 'key_c01_plus_additions': b['summary']['counts'],
                          'groups': a['summary']['groups']}
    open(os.path.join(HERE, 'counts.json'), 'w').write(json.dumps(counts, indent=1) + '\n')
    print(json.dumps(counts))


if __name__ == '__main__':
    main()
