"""Decode the fol. 17 two-digit cipher with key_f17.json, line by line.

usage: python3 scripts/decode_f17.py c_f17.txt key_f17.json

Groups absent from the key print as <nn>; ':' and '.' are kept as marks.
"""
import json, sys


def main():
    key = json.load(open(sys.argv[2], encoding='utf-8'))
    unknown = 0
    total = 0
    for line in open(sys.argv[1], encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        lab, *toks = line.split()
        out = []
        for t in toks:
            if t in (':', '.'):
                out.append(t)
                continue
            total += 1
            if t in key:
                out.append(key[t] if len(key[t]) == 1 else ' %s ' % key[t])
            else:
                out.append('<%s>' % t)
                unknown += 1
        print(lab, ''.join(out))
    print('groups', total, 'unknown', unknown)


if __name__ == '__main__':
    main()
