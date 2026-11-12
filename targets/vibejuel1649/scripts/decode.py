"""vibejuel1649 - mechanical decoder for transcription.txt (no language model, fixed tables).

Each cipher word = OPENER + BODY. The opener (first number) gives a shift k; each body number n stands for the letter
of rank n - k (1-based) in the alphabet in force.
  "gamle Ciffres" (old cipher, 1648-1651): 23 letters a b c d e f g h i k l m n o p q r s t u x y z (i = j, u = v/w),
      CYCLIC mod 23; k = -(opener mod 3): openers 24/27/30/... -> 0, 25/28/31 -> -1, 26/29/32 -> -2.
  "ny Alphabet" (new alphabet, 1651-1655): 25 letters a ... u w x y z oe (w = 21, x = 22, y = 23, z = 24, oe = 25),
      not cyclic; openers 24-29 -> 0, 30-34 -> 1, 35-39 -> 2, 1-3 -> 3.
In both, a body number 32/33/34 stands for 1/2/3.
Transcription conventions: numbers of one word joined by "."; "=" at the end of a token = word continues on the next
line; "C<n>" = nomenclator code (left as {n}); [ ... ] = clear text of the letter; "!" before a token = doubtful word
(decoded all the same). A line "#A <alphabet>" selects the alphabet (B = ny Alphabet, A23x = gamle Ciffres) and
"#K {opener: k, ...}" the opener table; "#S <label>" starts a new section. Other "#" lines are comments.
usage: python3 scripts/decode.py transcription.txt > decryption.txt"""
import ast, re, sys

ALPHS = {'B': ('abcdefghiklmnopqrstuwxyzø', False), 'A23x': ('abcdefghiklmnopqrstuxyz', True)}


def dec(nums, k, alph, cyc):
    out = ''
    for n in nums[1:]:
        if 32 <= n <= 34:
            n -= 31
        i = n - 1 - k
        if cyc:
            i %= len(alph)
        out += alph[i] if 0 <= i < len(alph) else '?%d' % n
    return out


def main(path):
    alph, cyc = ALPHS['B']; tab = None; carry = None; out = []
    for line in open(path, encoding='utf-8').read().splitlines():
        if line.startswith('#S '):
            out.append('\n== ' + line[3:].strip()); tab = None; continue
        if line.startswith('#A '):
            alph, cyc = ALPHS[line.split()[1]]; continue
        if line.startswith('#K'):
            tab = ast.literal_eval(line[2:].strip()); continue
        if line.startswith('#') or not line.strip():
            continue
        res = []
        for tok in re.findall(r'\[[^\]]*\]|\S+', line):
            if tok.startswith('['):
                res.append(tok); continue
            if tok.startswith('C'):
                res.append('{%s}' % tok[1:]); continue
            t = tok.lstrip('!'); hy = t.endswith('='); t = t.rstrip('=')
            nums = [int(x) for x in t.split('.') if x.isdigit()]
            if carry is not None:
                nums = carry + nums; carry = None
            if hy:
                carry = nums; continue
            k = tab.get(nums[0]) if tab else None
            res.append(dec(nums, k, alph, cyc).upper() if k is not None and len(nums) > 1
                       else '<%s>' % '.'.join(map(str, nums)))
        out.append(' '.join(res))
    print('\n'.join(out).strip())


if __name__ == '__main__':
    main(sys.argv[1])
