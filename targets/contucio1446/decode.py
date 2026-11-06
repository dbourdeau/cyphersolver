"""Decipher the f. 148 cipher passages (transcription.txt) with ASMi cart. 1597 no. 14 (key.md).

python targets/contucio1446/decode.py            -> decryption.txt, cipher_tokens.txt, tokens.tsv, validation.tsv, counts on stdout
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent

# label -> value; word signs and codes in capitals in the decryption
KEY = {
    'a1': 'a', 'a2': 'a', 'a3': 'a', 'c1': 'c', 'c2': 'c', 'd1': 'd', 'd2': 'd', 'e1': 'e', 'e2': 'e',
    'f1': 'f', 'f2': 'f', 'g1': 'g', 'i1': 'i', 'i2': 'i', 'l1': 'l', 'l2': 'l', 'm1': 'm', 'n1': 'n', 'n2': 'n',
    'o1': 'o', 'p1': 'p', 'p2': 'p', 'q1': 'q', 'q2': 'q', 'r1': 'r', 'r2': 'r', 's1': 's', 's2': 's',
    't1': 't', 't2': 't', 'u1': 'u', 'u2': 'u', 'u3': 'u', 'u4': 'u',
    'et': '[ET]', 'per': '[PER]', 'che': '[CHE]', 'con': '[CON]', 'quale': '[QUALE]',
    'stat': '[DUCA DE MILANO]', 'pec': '[COSIMO]', 'utinam': '[utinam?]', 'null': '',
}
SOURCE = {'pec': 'interlinear gloss f. 148v', 'utinam': 'open code', 'null': 'null'}


def lines():
    for raw in (HERE / 'transcription.txt').read_text(encoding='utf-8').splitlines():
        if not raw.strip() or raw.startswith('#'):
            continue
        ref, body = raw.split('\t', 1)
        yield ref, body


def main():
    out, tsv, val, ct = [], ['line\ttoken\tvalue\tnote'], [], []
    n = unread = unsure = nulls = 0
    for ref, body in lines():
        parts = re.split(r'(\{[^}]*\})', body)
        dec = []
        for p in parts:
            if p.startswith('{'):
                dec.append(p)
                continue
            for tok in p.split():
                q = tok.endswith('?')
                lab = tok.rstrip('?')
                v = KEY[lab]
                if lab == 'null':
                    nulls += 1
                    tsv.append(f'{ref}\t{tok}\t\tnull')
                    continue
                n += 1
                unread += lab == 'utinam'
                unsure += q
                dec.append(v + ('?' if q else ''))
                tsv.append(f'{ref}\t{tok}\t{v}\t{SOURCE.get(lab, "key R5314") + (", shape uncertain" if q else "")}')
                if lab != 'utinam':
                    val.append(f'{lab}\t{v.strip("[]").lower().replace(" ", "")}')
        out.append(f'{ref}\t' + ' '.join(dec).replace('  ', ' '))
        ct.append(ref + ' ' + ' '.join(t.rstrip('?') for p in parts if not p.startswith('{')
                                       for t in p.split() if t != 'null'))
    (HERE / 'decryption.txt').write_text(
        '# Decryption of transcription.txt with key.md (decode.py). Letters as deciphered, one per sign, spaced by sign;\n'
        '# word signs and codes in [CAPITALS]; ? after a value = sign shape uncertain; clear text in braces.\n\n'
        + '\n'.join(out) + '\n', encoding='utf-8')
    (HERE / 'cipher_tokens.txt').write_text(
        '# Cipher tokens only (labels of transcription.txt, nulls dropped), one page line per row, ref first.\n'
        + '\n'.join(ct) + '\n', encoding='utf-8')
    (HERE / 'tokens.tsv').write_text('\n'.join(tsv) + '\n', encoding='utf-8')
    (HERE / 'validation.tsv').write_text('\n'.join(val) + '\n', encoding='utf-8')
    print(f'cipher tokens {n} (+{nulls} null); unread {unread}; given a value {n - unread} '
          f'({(n - unread) / n:.1%}); shape uncertain {unsure}')


if __name__ == '__main__':
    main()
