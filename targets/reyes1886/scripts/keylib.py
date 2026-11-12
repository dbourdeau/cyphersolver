"""Shared helpers for target 1447 (Reyes-Revueltas War Ministry key). Standard library only."""
import collections
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def pairs_524(segs=None):
    """(seg, group, letter) for every usable row of transcription_524.txt (rows tagged '!' are skipped)."""
    out = []
    for line in (ROOT / 'transcription_524.txt').read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        f = line.split('\t')
        seg = f[0]
        if seg.endswith('!'):
            continue
        plain = f[1].split('>')[-1].strip()
        groups = f[2].split()
        if len(plain) != len(groups):
            raise SystemExit(f'row {seg}: {len(plain)} letters, {len(groups)} groups')
        n = int(''.join(c for c in seg if c.isdigit()))
        if segs and n not in segs:
            continue
        for g, p in zip(groups, plain):
            if '?' in g:
                continue
            out.append((seg, g, p))
    return out


def build(pairs):
    """group -> letter by majority over the pairs; also returns the conflicts."""
    c = collections.defaultdict(collections.Counter)
    for _, g, p in pairs:
        c[g][p] += 1
    key = {g: cnt.most_common(1)[0][0] for g, cnt in c.items()}
    conf = {g: dict(cnt) for g, cnt in c.items() if len(cnt) > 1}
    return key, conf, c


def load_key(path):
    k = {}
    for line in open(path, encoding='utf-8'):
        if not line.strip() or line.startswith('#'):
            continue
        g, v = line.rstrip('\n').split('\t')[:2]
        k[g] = v
    return k
