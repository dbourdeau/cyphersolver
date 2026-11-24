"""Conservative comparison by line and word position of the two independent texts."""
from pathlib import Path
from collections import Counter
import re
import unicodedata

HERE = Path(__file__).resolve().parent


def words(line):
    # The struck-out token is one position in each diplomatic transcription.
    line = re.sub(r'\[tachado,.*?\]|⟦.*?⟧', '¤', line)
    return line.split()


def visible(word):
    # Remove editorial abbreviational supplies; keep visible superscript letters.
    text = re.sub(r'⟨[^⟩]*⟩|\([^)]+\)', '', word)
    text = unicodedata.normalize('NFD', text).replace('\u0304', '')
    return ''.join(c for c in unicodedata.normalize('NFC', text).casefold() if c.isalpha())


def collate():
    table = ['folio\tline\tslot\treader_one\treader_two\tstatus\tconsensus']
    lines = []
    stats = {}
    for folio in ('33r','33v'):
        counts = Counter()
        a,b = [[s for s in (HERE/f'{folio}_{r}.txt').read_text().splitlines() if s.strip()] for r in ('one','two')]
        assert len(a) == len(b)
        for n,(left,right) in enumerate(zip(a,b), 1):
            first,second = words(left),words(right)
            assert len(first) == len(second), (folio, n, first, second)
            agreed = []
            for slot,(p,q) in enumerate(zip(first,second),1):
                if '¤' in (p,q):
                    status = 'cancellation'
                elif '[?]' in p or '[?]' in q:
                    status = 'doubt'
                elif visible(p) == visible(q):
                    status = 'agreed'
                else:
                    status = 'variant'
                common = p if status == 'agreed' else '[…]'
                agreed.append(common)
                counts[status] += 1
                table.append('\t'.join(map(str, [folio,n,slot,p,q,status,common])))
            lines.append(f'{folio} {n:02d}\t'+' '.join(agreed))
        stats[folio] = dict(counts)
    return '\n'.join(table)+'\n', '\n'.join(lines)+'\n', stats


if __name__ == '__main__':
    table, lines, stats = collate()
    assert table == (HERE/'collation.tsv').read_text()
    assert lines == (HERE/'consensus.txt').read_text()
    print(stats)
