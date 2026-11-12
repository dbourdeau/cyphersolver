"""Align the blind transcriptions of 28 Jan 1794 (M30-002-0196), 26 Feb 1794 (0208) and 1 Oct 1795 (M31-007-0020/0021)
to the printed texts with key v4, using the round-1 aligner unchanged (scripts/code16_align_cribs_2026_11_10.py:
align, harvest). Doubtful groups (?) and hidden ones (_) enter as unknowns and are never harvested.
Writes alignment_<letter>.tsv (one row per group: group, marks, piece of print it took, kind) and prints harvests."""
from pathlib import Path
import csv, re, json, importlib.util, sys

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'output/code16_pinckney_2026-11-11'
spec = importlib.util.spec_from_file_location('al', ROOT / 'scripts/code16_align_cribs_2026_11_10.py')
al = importlib.util.module_from_spec(spec); spec.loader.exec_module(al)
ED = ROOT / 'sources/raw/pinckney_edition_texts_2026-11-10'
ASP = ROOT / 'sources/raw/code16_pinckney_2026-11-11/asp_fr1/americanstatepap_c11unit_djvu.txt'


def seq_from_spans(path, frame_label):
    out = []
    for r in csv.DictReader(Path(path).open(), delimiter='\t'):
        if r['frame'] in ('0020', '0021') or frame_label.startswith('M30'):
            for t in r['groups'].split():
                if t.startswith('<'): continue                       # struck by the writer
                t = t.strip('[]')
                d = re.sub(r'\D', '', t)
                ok = d and '?' not in t and '_' not in t
                out.append(dict(frame=frame_label if frame_label.startswith('M30') else 'M31-007-' + r['frame'], line=r['line'], raw=t,
                                g=int(d) if ok else None, plus='+' in t, inter=r['interlinear'], placement=r['placement']))
    return out


def text_0196():
    t = (ED / '1794-01-28b_TP_to_Randolph_PNKY.txt').read_text().split('=' * 20)[-1]
    i = t.index('In addition to my letter'); j = t.index('events in flanders', i) + len('events in flanders')
    return re.sub(r'°|\[|\]', '', t[i:j])


def text_0208():
    t = (ED / '1794-02-26_TP_to_Randolph_PNKY.txt').read_text().split('=' * 20)[-1]
    i = t.index('This plan consists'); j = t.index('procure his evasion', i) + len('procure his evasion')
    return re.sub(r'°|\^', '', t[i:j])


def text_1oct():
    t = ' '.join(ASP.read_text().split())
    i = t.index('San Ildefonso, 1st October, 1795.')
    a = t.index('where measures are', i) + len('where measures are'); b = t.index('wildly hazarded', a) + len('wildly hazarded')
    c = t.index('to induce a', b) + len('to induce a'); d = t.index('towards us', c) + len('towards us')
    return t[a:b], t[c:d]


def run(name, seq, text, key, vocab):
    owned = set(key.values())
    T, path, cost, end = al.align(seq, text, key, vocab, owned, beam=600)
    acc, cand = al.harvest(seq, T, path, key, vocab, owned)
    with (OUT / f'alignment_{name}.tsv').open('w') as f:
        f.write('frame\tline\tgroup\tpiece\tkind\tkey_v4\tinterlinear\n')
        for it, (p, L, kind) in zip(seq, path):
            f.write(f"{it['frame']}\t{it['line']}\t{it['raw']}\t{T[p:p+L]}\t{kind}\t{key.get(it['g'], '') if it['g'] else ''}\t{it['inter']}\n")
    return dict(letters=len(T), reached=end, cost=round(cost, 1), accepted={g: v for g, v in acc.items()},
                candidates={g: v for g, v in cand.items()})


def main():
    vocab = al.load_vocab()
    key = al.load_key(ROOT / 'output/code16_merged_2026-11-10/code16_key_v4.tsv')
    tr = OUT / 'transcriptions'
    jobs = [('17940128_0196', seq_from_spans(tr / 'M30-002-0196/spans.tsv', 'M30-002-0196'), text_0196()),
            ('17940226_0208', seq_from_spans(tr / 'M30-002-0208/spans.tsv', 'M30-002-0208'), text_0208())]
    s = seq_from_spans(ROOT / 'output/pinckney1795_code16_2026-11-10/spans.tsv', 'M31')
    f1, f2 = text_1oct()
    jobs.append(('17951001_a', [x for x in s if not (x['frame'].endswith('0021') and x['line'] == 'L03')], f1))
    jobs.append(('17951001_b', [x for x in s if x['frame'].endswith('0021') and x['line'] == 'L03'], f2))
    res = {}
    for name, seq, text in jobs:
        r = run(name, seq, text, key, vocab)
        res[name] = dict(groups=len(seq), letters=r['letters'], reached=r['reached'], cost=r['cost'],
                         accepted={str(g): list(v) for g, v in r['accepted'].items()},
                         candidates={str(g): v for g, v in r['candidates'].items()})
        print(name, len(seq), r['letters'], r['reached'], r['cost'], r['accepted'])
    (OUT / 'alignment_summary.json').write_text(json.dumps(res, indent=1) + '\n')


if __name__ == '__main__':
    main()
