"""Fourth pass helper (64r.16-64v.22): where does a crib phrase encode the digits, allowing at most one wrong
digit per word (probe.slip_options)? Nulls 11 are free between words.

  python slip64_fit.py 64v.12 "non si possa"          search the line and the next
  python slip64_fit.py 64v.12 "possa" 43 49           only starts in line positions 43..49
Prints each exact span (start..end, codes, slipped code marked !).
"""
import sys
import probe


def enc_word(i, w, lim, slips=1):
    """yield (end, path, nslips) for word w spelled from FLAT[i]"""
    stack = [(i, 0, [], 0)]
    while stack:
        j, k, path, ns = stack.pop()
        if k == len(w):
            yield j, path, ns
            continue
        if j >= lim:
            continue
        opts = probe.options(j) + (probe.slip_options(j) if ns < slips else [])
        for n, c, o, f in opts:
            if c == '_':
                stack.append((j + 1, k + 1, path + ['_'], ns))
                continue
            if o and w.startswith(o, k) and j + n <= lim:
                stack.append((j + n, k + len(o), path + [f'{c}={o}{f}'], ns + (f == '!')))


def enc_phrase(i, words, lim):
    if not words:
        yield i, []
        return
    js = [i]
    if i + 1 < lim and probe.FLAT[i][2] == 1 and probe.FLAT[i + 1][2] == 1:
        js.append(i + 2)
    for j0 in js:
        for e, p, ns in enc_word(j0, words[0], lim):
            for e2, rest in enc_phrase(e, words[1:], lim):
                yield e2, [(words[0], p, ns)] + rest


def main():
    lab, crib = sys.argv[1], sys.argv[2].lower().split()
    i0, i1 = probe.span(lab)
    lim = min(len(probe.FLAT), i1 + 70)
    a = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    b = int(sys.argv[4]) if len(sys.argv) > 4 else i1 - i0 + 60
    seen = set()
    for s in range(i0 + a - 1, min(lim, i0 + b)):
        for e, parts in enc_phrase(s, crib, lim):
            key = (s, e, str(parts))
            if key in seen:
                continue
            seen.add(key)
            tot = sum(ns for _, _, ns in parts)
            t0, t1 = probe.FLAT[s], probe.FLAT[e - 1]
            print(f'{t0[0]}:{t0[1]}-{t1[0]}:{t1[1]} slips={tot} ' +
                  ' | '.join(f'{w}[{" ".join(p)}]' for w, p, _ in parts))


if __name__ == '__main__':
    main()
