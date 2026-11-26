#!/usr/bin/env python3
"""make_data_files.py SRC_DIR OUT_DIR      (run from anywhere: python3 scripts/make_data_files.py . rebuilt)
(Written by an AI model, claude-fable-5-2, at the contributor's direction, 20 Nov 2026. Standard library only.)

Writes this folder's transcription files and counts from the copy of the numerals. It reads SRC_DIR/numerals_v4.tsv
(the copy) and SRC_DIR/sources.tsv (for each telegram, what the archive's listing says of it and where its images
are). It reads no key, no translation and no image, and it writes no value of any group. Run it into an empty
directory and compare with the folder's own files: they should be the same.

  <telegram>_transcription.txt .. one for each telegram: header lines beginning with "#", then the message line by
                                  line. A group is written by the reading that stands first; "~" follows a group with
                                  a small stroke above it in the first reading; "?" follows a group that has another
                                  reading on record; then the mark written after the group, where both readings agree
                                  on it. cs and q' are the two signs as the copy writes them.
  open_groups.tsv ............... every group with another reading, and every group whose stroke or mark the two
                                  readings give differently
  groups_output.txt ............. counts: by telegram, by width of group, the groups that stand in more than one
                                  telegram
It writes into OUT_DIR, never over a file, and prints counts only."""
import collections
import csv
import os
import sys

SIGN_NOTE = {'q': "q'", 'cs': 'cs'}


def main():
    src, out = sys.argv[1:3]
    os.makedirs(out, exist_ok=True)
    rows = list(csv.DictReader(open(os.path.join(src, 'numerals_v4.tsv'), encoding='utf-8'), delimiter='\t'))
    leaves = list(collections.OrderedDict((r['leaf'], 1) for r in rows))
    lst, frames = {}, collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(src, 'sources.tsv'), encoding='utf-8'), delimiter='\t'):
        lst[r['telegram']] = r
        frames[r['telegram']].append(r)
    by = collections.OrderedDict((l, []) for l in leaves)
    for r in rows:
        by[r['leaf']].append(r)
    opens, stats = [], []
    for leaf, rs in by.items():
        rs.sort(key=lambda r: (int(r['page']), int(r['line']), int(r['pos'])))
        L = lst[leaf]; fr = sorted(frames[leaf], key=lambda r: r['image_address'])
        pages = sorted({int(r['page']) for r in rs})
        assert len(fr) >= len(pages), leaf
        g = [r for r in rs if r['kind'] == 'group']
        hands = sorted({r['hand'] for r in rs})
        twice = sum(1 for r in g if r['sample'] or r['sample2'])
        head = ['# CEHM-Carso, Fondo DLI (Archivo del General Bernardo Reyes), %s. %s, by hand; no translation on the leaf.' % (leaf, L['type_in_the_listing']),
                '# In the archive\'s listing: %s; signed %s; to %s. CEHM record %s.' % (L['place_and_date_in_the_listing'], L['signed_by'], L['to'], L['cehm_record'])]
        for f in fr[:len(pages)]:
            head.append('# Image: %s (fetched %s, %s bytes, SHA-256 %s)' % (f['image_address'], f['fetched_utc'], f['bytes'], f['sha256']))
        head += ['# The message only: the form\'s printed heading, the address and the signature are not copied.',
                 '# Hand %s of this folder\'s three (NOTES.md, section 3). %d groups: %d read twice, %d read once.' % ('/'.join(hands), len(g), twice, len(g) - twice),
                 '# A group is written by the reading that stands first. ~ a small stroke stands above the group. ? another reading is on record (open_groups.tsv).',
                 '# cs: a small mark after a low number, read cs or es. q\': a doubled mark. {n}: a number read as standing in clear. [..]: a note, not a reading.']
        lines, cur, text, notebuf = [], None, [], []
        for r in rs:
            key = (int(r['page']), int(r['line']))
            if key != cur:
                if text or notebuf:
                    if notebuf:
                        text.append(' '.join(notebuf)); notebuf = []
                    lines.append(' '.join(text)); text = []
                if cur is not None and key[0] != cur[0]:
                    lines.append('# page %d' % key[0])
                cur = key
            if r['kind'] == 'note':
                notebuf.append(r['as_written']); continue
            if notebuf:
                text.append(' '.join(notebuf)); notebuf = []
            if r['kind'] == 'group':
                other = r['v4_other_readings']
                t = r['p_first'] + ('~' if r['v4_tick'] == '1' else '') + ('?' if other else '') + (r['v4_after'] if not r['v4_after'].startswith('open') else '')
                text.append(t)
                if other or r['v4_tick'].startswith('open') or r['v4_after'].startswith('open'):
                    opens.append([leaf, r['page'], r['line'], r['pos'], r['p_first'], other, r['v4_tick'] if r['v4_tick'].startswith('open') else '',
                                  r['v4_after'] if r['v4_after'].startswith('open') else '', r['v4_status'], r['v4_note']])
            elif r['kind'] in SIGN_NOTE:
                text.append(SIGN_NOTE[r['kind']])
            else:
                text.append(r['as_written'])
        if notebuf:
            text.append(' '.join(notebuf))
        if text:
            lines.append(' '.join(text))
        with open(os.path.join(out, '%s_transcription.txt' % leaf), 'x', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(head + lines) + '\n')
        w = collections.Counter(len(r['p_first']) for r in g)
        stats.append(dict(leaf=leaf, groups=len(g), small=w[1] + w[2], three=w[3], four=w[4], other=sum(v for k, v in w.items() if k > 4),
                          distinct=len({r['p_first'] for r in g}), open=sum(1 for r in g if r['v4_other_readings']), twice=twice,
                          words=sum(1 for r in rs if r['kind'] == 'word'), cs=sum(1 for r in rs if r['kind'] == 'cs'), q=sum(1 for r in rs if r['kind'] == 'q'),
                          lines=len({(r['page'], r['line']) for r in rs}), pages=len(pages), hands='/'.join(hands)))
    with open(os.path.join(out, 'open_groups.tsv'), 'x', encoding='utf-8', newline='\n') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['telegram', 'page', 'line', 'token', 'reading_that_stands_first', 'other_readings', 'stroke_above', 'mark_after', 'status_in_the_copy', 'note'])
        w.writerows(opens)
    G = [r for r in rows if r['kind'] == 'group']
    where = collections.defaultdict(set)
    for r in G:
        if len(r['p_first']) >= 3:
            where[r['p_first']].add(r['leaf'])
    shared = sorted((k for k, v in where.items() if len(v) > 1), key=lambda k: (-len(where[k]), int(k)))
    low_next = collections.Counter(); qpair = 0
    for leaf, rs in by.items():
        for i, r in enumerate(rs):
            nxt = rs[i + 1]['kind'] if i + 1 < len(rs) else 'end'
            if r['kind'] == 'group' and len(r['p_first']) <= 2:
                low_next[nxt] += 1
            if r['kind'] == 'q' and nxt == 'q':
                qpair += 1
    o = ['Counts from numerals_v4.tsv, on the reading that stands first (written by scripts/make_data_files.py; no value of any group is used).', '',
         'telegram\tgroups\tof_1_or_2_figures\tof_3\tof_4\tlonger\tdistinct\topen\tread_twice\twords_in_clear\tsign_cs\tsign_q\tlines\tpages\thand']
    for s in stats:
        o.append('%(leaf)s\t%(groups)d\t%(small)d\t%(three)d\t%(four)d\t%(other)d\t%(distinct)d\t%(open)d\t%(twice)d\t%(words)d\t%(cs)d\t%(q)d\t%(lines)d\t%(pages)d\t%(hands)s' % s)
    tot = {k: sum(s[k] for s in stats) for k in ('groups', 'small', 'three', 'four', 'other', 'open', 'twice', 'words', 'cs', 'q', 'lines')}
    o.append('ALL TEN\t%(groups)d\t%(small)d\t%(three)d\t%(four)d\t%(other)d\t\t%(open)d\t%(twice)d\t%(words)d\t%(cs)d\t%(q)d\t%(lines)d\t\t' % tot)
    d3 = {r['p_first'] for r in G if len(r['p_first']) == 3}; d4 = {r['p_first'] for r in G if len(r['p_first']) == 4}
    small_rows = [r for r in G if len(r['p_first']) <= 2]
    o += ['', 'distinct groups of three figures: %d (lowest %s, highest %s); of four figures: %d (lowest %s, highest %s)' % (
        len(d3), min(d3, key=int), max(d3, key=int), len(d4), min(d4, key=int), max(d4, key=int)),
        'distinct groups of three or four figures over the ten telegrams: %d' % len(d3 | d4),
        'low numbers of one or two figures: %d, distinct %d' % (len(small_rows), len({r['p_first'] for r in small_rows})),
        'what stands directly after a low number: %s' % ', '.join('%s %d' % (k, v) for k, v in sorted(low_next.items(), key=lambda kv: -kv[1])),
        'the sign q\' stands %d times; %d times it is directly followed by another' % (tot['q'], qpair),
        'groups read twice: %d (same digits in both readings %d, different %d); read once: %d' % (
            tot['twice'], sum(1 for r in G if (r['sample'] and r['blind_digits'] == r['digits_without_strokes']) or (r['sample2'] and r['blind2_digits'] == r['digits_without_strokes'])),
            sum(1 for r in G if (r['sample'] and r['blind_digits'] != r['digits_without_strokes']) or (r['sample2'] and r['blind2_digits'] != r['digits_without_strokes'])), tot['groups'] - tot['twice']),
        'groups of three or four figures that stand in more than one telegram: %d' % len(shared)]
    for k in shared:
        o.append('  %s\tin %d telegrams\t%s' % (k, len(where[k]), ', '.join(sorted(where[k]))))
    open(os.path.join(out, 'groups_output.txt'), 'x', encoding='utf-8', newline='\n').write('\n'.join(o) + '\n')
    print('telegrams %d; groups %d (of 1 or 2 figures %d, of 3 %d, of 4 %d, longer %d); open %d; read twice %d; rows in open_groups.tsv %d; shared groups %d' % (
        len(stats), tot['groups'], tot['small'], tot['three'], tot['four'], tot['other'], tot['open'], tot['twice'], len(opens), len(shared)))


if __name__ == '__main__':
    main()
