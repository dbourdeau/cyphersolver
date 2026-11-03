"""Decrypt a sign transcription with a frozen key.

usage: python decrypt.py <key.tsv> <transcription.txt> [page-prefix ...]
Prints, per line, the groups and their values; a group the key does not cover is printed as [n] (or [n_]),
and a token piece that cannot be parsed as a group (e.g. '#', illegible) as [?]. Nothing is dropped silently.

Token rules (see TRANSCRIPTION_RULES.md):
  * superscripts ^x (letters, digits, or [?]) are removed for lookup;
  * a token with inner dots, colons, '=' or commas ('8.4.3', 'c27.c2.8-', 'c26=^e') is split into its groups;
  * the curl prefix 'c' is dropped (see key header), as are dots above (') and hyphens at line ends;
  * '?' (doubtful digit) is ignored for lookup; with alternatives 'a|b' the first is used;
  * an underlined group (_) is looked up first with, then without, the underline.
"""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SUP = re.compile(r"\^(\[[^\]]*\]|[^\s.:=,;\-'^]+)")


def load_key(fn):
    k = {}
    for ln in open(fn, encoding='utf-8-sig'):
        if ln.startswith('#') or not ln.strip():
            continue
        p = ln.rstrip('\n').split('\t')
        k[p[0]] = p[1]
    return k


def groups(tok):
    """Split one transcription token into (group, underlined) pairs; (None, False) for an unparsable piece."""
    out = []
    t = SUP.sub('', tok)
    for piece in re.split(r'[.:=,;]', t):
        p = piece.strip("-'")
        if not p:
            continue
        p = p.lstrip('c')
        under = '_' in p
        p = p.replace('_', '').replace('?', '')
        if '|' in p:
            p = p.split('|')[0]
        out.append((p, under) if p.isdigit() else (None, False))
    return out


def norm(tok):
    """Older one-group form, still used by test_1722.py and solve_1722.py so that their recorded outputs can be
    rerun as they were made: (first group of the token or '', underlined). Not used for the 1719 reading."""
    g = groups(tok)
    return (g[0][0] or '', g[0][1]) if g else ('', False)


def lookup(g, under, key):
    if g is None:
        return None
    if under and g + '_' in key:
        return key[g + '_']
    return key.get(g)


def values(tok, key):
    """Values of the groups in a token: a key value, '[n]' for an uncovered group, '[?]' for an unparsable one."""
    res = []
    for g, under in groups(tok):
        v = lookup(g, under, key)
        if v is not None:
            res.append(v)
        elif g is None:
            res.append('[?]')
        else:
            res.append(f'[{g}{"_" if under else ""}]')
    return res


def lines(fn):
    for ln in open(fn, encoding='utf-8-sig'):
        m = re.match(r'\s*(\w+\.L\d+)\s*:?\s*(.*)', ln)
        if m:
            yield m.group(1), m.group(2)


def decrypt_line(body, key):
    out = []
    for part in re.split(r'(\{[^}]*\})', body):
        if part.startswith('{'):
            out.append(part[1:-1])
            continue
        for tok in part.split():
            out.extend(values(tok, key))
    return out


if __name__ == '__main__':
    key = load_key(sys.argv[1])
    pref = sys.argv[3:]
    for lid, body in lines(sys.argv[2]):
        if pref and not any(lid.startswith(p) for p in pref):
            continue
        print(lid, '|', ' '.join(decrypt_line(body, key)))
