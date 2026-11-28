"""Write ct/<id>.txt, texts/<id>_decryption.txt and validation.tsv from the transcription, key v3 and the round-3
alignment. Run from targets/jefferson1793: python3 scripts/make_texts.py (Python 3.9+, standard library only)."""
import csv, collections, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from code15lib import parse

DOCS = {'tj_17930101': (['A'], 'Jefferson to Thomas Pinckney, Philadelphia, 1 Jan 1793',
                        'Library of Congress, Thomas Jefferson Papers, series 1, mtj1 017 image 0559 (https://www.loc.gov/item/mtjbib006744/)',
                        'the State Department file copy, entirely en clair (DNA RG 59 DCI), as printed in PTJ 25 and on Founders Online (Jefferson/01-25-02-0005)'),
        'tp_17930405': (['B', 'C'], 'Thomas Pinckney to Jefferson, London, 5 Apr 1793',
                        'NARA RG 59, Despatches from U.S. Ministers to Great Britain, M30 roll 2 frames 0077 (right page) and 0078 (left page)',
                        "George Taylor Jr.'s interlinear decipherment on the page"),
        'tp_17930410': (['D'], 'Thomas Pinckney to Jefferson, London, 10 Apr 1793',
                        'NARA M30 roll 2 frame 0083 (right page)', "George Taylor Jr.'s interlinear decipherment on the page"),
        'tp_17930427': (['E'], 'Thomas Pinckney to Jefferson, London, 27 Apr 1793',
                        'NARA M30 roll 2 frame 0086 (right page)', "Jefferson's (first sentence) and George Taylor Jr.'s interlinear decipherment on the page")}

rows = list(csv.DictReader(open('transcription/code15_groups_v3.tsv', encoding='utf-8'), delimiter='\t'))
key = {r['group']: r for r in csv.DictReader(open('key/code15_key_v3.tsv', encoding='utf-8'), delimiter='\t')}
pieces = {}   # (doc, n-th token) -> piece from the round-3 alignment
order = collections.defaultdict(list)
for line in open('key/hand_alignment_v3.txt', encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    seg, rest = line.split(':', 1)
    for it in rest.split():
        g, p = it.rsplit(':', 1); order[seg[0]].append((g, p.rstrip('?')))
    if seg in ('E1',):
        order['E'].append(('[del]', None))
os.makedirs('ct', exist_ok=True); os.makedirs('texts', exist_ok=True)
val = ['# model: en-modern', '# source: transcription/code15_groups_v3.tsv with key/hand_alignment_v3.txt (decipherments of the time)',
       '# note: one line per code group; "?" = digits lost or doubtful, or a struck group; "-" = a group with no letters under it']
for doc, (letters, title, where, words) in DOCS.items():
    ct = [f'# {title}: Code No. 15 groups as transcribed, one line per manuscript line. ? = leading digit(s) lost in the binding',
          f'# gutter; [38] = doubtful digit, the two readings; = + x # are marks written with the group. Source: {where}.',
          '# Transcription: two AI agents (Claude Opus 5.5) blind and independently, 27 Nov 2026; see transcription/.']
    dec = [f'# {title}: unedited output of key/code15_key_v3.tsv, one line per manuscript line: group=value.',
           '# "=?" = no value in the key (lost or doubtful digits, or a group seen once with no sure value); values marked * are',
           '# "unsure" in the key (an uncertain split inside a word), ** "conflict", ^ "probable" (seen only in the 1 Jan letter).',
           f'# Words over the groups at the time: {words}.']
    for L in letters:
        al = order[L]; k = 0
        lines = collections.OrderedDict()
        for r in rows:
            if r['doc'] == L: lines.setdefault(r['line'], []).append(r['group'])
        for ln, gs in lines.items():
            ct.append(f'{L}{ln}: ' + ' '.join(gs))
            out = []
            for g in gs:
                num, mark, dl = parse(g)
                v = key.get(num) if num else None
                tag = '' if not v else {'sure': '', 'unsure': '*', 'conflict': '**', 'probable': '^'}[v['status']]
                out.append(f'{g}=' + (v['value'] + tag if v else '?'))
                if L in order:
                    ag, piece = al[k] if k < len(al) else (None, None); k += 1
                    val.append(f'{g}\t' + ('?' if (num is None or piece is None) else ('-' if piece == '-' else piece.replace('_', ''))))
            dec.append(f'{L}{ln}: ' + ' '.join(out))
    open(f'ct/{doc}.txt', 'w', encoding='utf-8', newline='\n').write('\n'.join(ct) + '\n')
    open(f'texts/{doc}_decryption.txt', 'w', encoding='utf-8', newline='\n').write('\n'.join(dec) + '\n')
open('validation.tsv', 'w', encoding='utf-8', newline='\n').write('\n'.join(val) + '\n')
print('written', len(val) - 3, 'validation pairs')
