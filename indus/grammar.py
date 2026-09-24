"""One explicit grammar for Indus lines, built from the registered findings (set 191). parse(t) returns the label of the
first rule that accounts for the whole line, or None. RULES can be switched off one by one (ablation).

LINE = [HEADING] NAME [POST] | COUNT | FORMULA | BARE | NUMBERS
  HEADING  817 / 820 / 861 + 2 / 60 / 1
  NAME     BODY ENDING; BODY = lexical signs or numerals; ENDING = 740 | 520 | closer | caged sign | 740 + stacking closer
  POST     400 / 90 after the ending
  COUNT    a numeral run + at most two signs
  FORMULA  705 / 706 + 33 + 520, alone or after a name body or name
  BARE     2+ lexical signs (numerals allowed) whose last sign is attested as a name head
  NUMBERS  numerals only
Set 192 adds (EXT_RULES): SHORT heading alone or + one sign; ONE one lexical sign + 400 / 90; U body + numeral + 700;
OPEN 705 / 706 + body; SEQ two consecutive units that each parse, the first of 2+ signs.
"""
import rtools as R
from predict_test103 import CL

CAGED = {'226', '232', '153', '236', '241', '144', '393', '895', '466', '804', '878', '689'}
STACK = {'151', '161', '527', '565', '621', '679'}
ALL_RULES = ('heading', 'post', 'closer', 'caged', 'stack', 'count', 'formula', 'bare', 'numbers')
NEW_RULES = ('short', 'one', 'u', 'open', 'seq')
EXT_RULES = ALL_RULES + NEW_RULES


def lexical(g):
    return g not in R.NUMS and g not in R.END and g not in CL and g not in CAGED and g not in ('400', '90')


def body_ok(b):
    return len(b) >= 1 and all(lexical(g) or g in R.NUMS for g in b)


def heads_from(lines):
    return {R.name_of(list(t))[0][-1] for t in lines if R.name_of(list(t)) and R.name_of(list(t))[0]}


def parse(t, heads, rules=ALL_RULES):
    t = tuple(t)
    if not t:
        return None
    lab = _parse(t, heads, rules)
    if lab is None and 'seq' in rules:
        sub = tuple(r for r in rules if r != 'seq')
        for k in range(2, len(t)):
            if _parse(t[:k], heads, sub) is not None and _parse(t[k:], heads, sub) is not None:
                return 'seq'
    return lab


def split_seq(t, heads, rules=EXT_RULES):
    """First split point k of a SEQ line, or None."""
    t = tuple(t)
    sub = tuple(r for r in rules if r != 'seq')
    if _parse(t, heads, sub) is not None:
        return None
    for k in range(2, len(t)):
        if _parse(t[:k], heads, sub) is not None and _parse(t[k:], heads, sub) is not None:
            return k
    return None


def _parse(t, heads, rules):
    if not t:
        return None
    if 'numbers' in rules and all(g in R.NUMS for g in t):
        return 'numbers'
    if 'one' in rules and len(t) >= 2 and lexical(t[0]) and all(g in ('400', '90') for g in t[1:]):
        return 'one'
    if 'post' in rules:
        while len(t) >= 2 and t[-1] in ('400', '90'):
            t = t[:-1]
    if 'short' in rules and t[0] in ('817', '820', '861') and len(t) >= 2 and t[1] in ('2', '60', '1') and (len(t) == 2 or (len(t) == 3 and lexical(t[2]))):
        return 'short'
    if 'heading' in rules and len(t) >= 3 and t[0] in ('817', '820', '861') and t[1] in ('2', '60', '1'):
        t = t[2:]
    if 'formula' in rules and len(t) >= 3 and t[-3] in ('705', '706') and t[-2] == '33' and t[-1] == '520':
        rest = t[:-3]
        if not rest or body_ok(rest) or _parse(rest, heads, rules) in ('name', 'bare'):
            return 'formula'
    if 'open' in rules and len(t) >= 2 and t[0] in ('705', '706') and body_ok(t[1:]):
        return 'open'
    if 'u' in rules and len(t) >= 3 and t[-1] == '700' and t[-2] in R.NUMS and body_ok(t[:-2]):
        return 'u'
    end = t[-1]
    if len(t) >= 2:
        if end in R.END and body_ok(t[:-1]):
            return 'name'
        if 'closer' in rules and end in CL and end not in STACK and body_ok(t[:-1]):
            return 'name'
        if 'caged' in rules and end in CAGED and body_ok(t[:-1]):
            return 'name'
        if 'stack' in rules and end in STACK and len(t) >= 3 and t[-2] == '740' and body_ok(t[:-2]):
            return 'name'
        if 'closer' in rules and end in STACK and body_ok(t[:-1]):
            return 'name'
    if 'count' in rules and t[0] in R.NUMS:
        j = 0
        while j < len(t) and t[j] in R.NUMS:
            j += 1
        if len(t) - j <= 2 and all(g not in R.END for g in t[j:]):
            return 'count'
    if 'bare' in rules and len(t) >= 2 and all(lexical(g) or g in R.NUMS for g in t) and t[-1] in heads:
        return 'bare'
    return None


def coverage(lines, heads, rules=ALL_RULES):
    ls = list(lines)
    return sum(parse(t, heads, rules) is not None for t in ls) / max(1, len(ls))
