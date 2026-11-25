"""Second round, step 6: an adjusted score that accounts for page order, reference conventions and sign labels.

  python adjust2.py OUT_DIR [PASS]  -> scores2_adjusted.json

Three effects inflate the plain score without being misreadings, and each gets one rule:
  1. Order: blocks of 10 hypothesis lines are each fitted to their best place in the reference (score2.order_tolerant).
  2. Reference conventions (digit stratum): a letter the reference uses for a digit (R478 writes 1 as "i") is read as
     that digit, when it lines up with that one digit in the hypothesis in >= 80% of at least 5 aligned occurrences.
     Other letters are dropped from both sides, as in the plain digit score.
  3. Sign labels (letter stratum): a letter the hypothesis uses for a special sign is renamed to the reference's label
     for it, on the same rule (>= 80% of >= 5 aligned occurrences, the target a different letter).
Digits are never renamed: a misread digit stays an error. Guard against fitting the score: the hypothesis blocks are
split into two halves (alternate blocks), the rule is learned on each half separately, and a renaming is applied only
when both halves learn it. The denominator is the reference sign count after rule 2.
"""
import collections
import json
import re
import sys
from pathlib import Path

import score
import score2

HERE = Path(__file__).resolve().parent
BLOCK = 10


def fit_pairs(a, b):
    """Fitting alignment of a (block) into b (reference) with backtrace; returns (edits, start, end, aligned pairs
    (a_char, b_char) for match/substitution positions)."""
    n, m = len(a), len(b)
    prev = [0] * (m + 1)
    back = [None] * (n + 1)
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        bk = bytearray(m + 1)
        bk[0] = 2
        ai = a[i - 1]
        for j in range(1, m + 1):
            d = prev[j - 1] + (ai != b[j - 1])
            u = prev[j] + 1  # a char not in b
            l = cur[j - 1] + 1  # b char not in a
            if d <= u and d <= l:
                cur[j] = d
            elif u <= l:
                cur[j], bk[j] = u, 2
            else:
                cur[j], bk[j] = l, 3
        back[i] = bk
        prev = cur
    j = min(range(m + 1), key=lambda k: prev[k])
    e, end, i, pairs = prev[j], j, n, []
    while i > 0:
        mv = back[i][j] if j > 0 else 2
        if mv == 0:
            pairs.append((a[i - 1], b[j - 1]))
            i, j = i - 1, j - 1
        elif mv == 2:
            i -= 1
        else:
            j -= 1
    return e, j, end, pairs


GREEK = "αβγδεζηθικλμνξοπρστυφχψω"
# Hypothesis-side sign names, declared by the transcribing agent in its report (batch 6: "crossed d-like sign written
# `at`"); each is one sign, the mirror of the reference's spelled-out names, and is given one placeholder letter.
HYP_SIGN_TOKENS = {"at": "ω"}


def hyp_tokens(line, letter):
    if not letter:
        return line
    return " ".join(HYP_SIGN_TOKENS.get(tok.lower(), tok) for tok in line.split())


def ref_alnum(path, letter):
    """Reference stream on letters and digits. Letter stratum: the reference spaces its cipher letters ("i f", "c a f")
    but spells some special signs as a word ("Infinity", "fire"); an unspaced run of 3+ letters is one sign, given one
    placeholder letter per distinct name, so it counts as one sign, not eight."""
    t = "".join(l + " " for l in score.ref_lines(path))
    t = re.sub(r"CIPHERTEXT\s*\d*", "", t, flags=re.I)
    if not letter:
        t = re.sub(r"\^\S", "", t)
        return score.digits(t, alnum=True)
    names = {}

    def ph(m):
        w = m.group(0).lower()
        if w not in names:
            names[w] = GREEK[len(names) % len(GREEK)]
        return names[w]
    t = re.sub(r"(?<![A-Za-z])[A-Za-z]{3,}(?![A-Za-z])", ph, t)
    return re.sub(r"[^0-9a-z" + GREEK + "]", "", t.lower())


def learn(pairs, letter):
    """Renamings from aligned (hyp, ref) pairs. Digit stratum: ref letter -> hyp digit. Letter stratum: hyp letter ->
    a different ref letter."""
    cnt = collections.defaultdict(collections.Counter)
    for h, r in pairs:
        if letter and h.isalpha():
            cnt[h][r] += 1
        if not letter and r.isalpha():
            cnt[r][h] += 1
    out = {}
    for k, c in cnt.items():
        tot = sum(c.values())
        top, n = c.most_common(1)[0]
        if tot >= 5 and n / tot >= 0.8 and top != k and (top.isdigit() if not letter else top.isalpha()):
            out[k] = top
    return out


def order_tolerant_raw(a, hl, letter):
    """score2.order_tolerant, but on lines already reduced to signs (placeholders kept in the letter stratum)."""
    import human_ceiling
    covered = bytearray(len(a))
    edits = 0
    for i in range(0, len(hl), BLOCK):
        s_ = "".join(hl[i:i + BLOCK])
        b = re.sub(r"[^0-9a-z?" + GREEK + "]", "", s_.lower()) if letter else score.digits(s_, keep_q=True)
        if not b:
            continue
        e, s, t = human_ceiling.fit(b, a)
        edits += e
        for k in range(s, t):
            covered[k] = 1
    return edits + covered.count(0)


def learn_hand(pairs):
    """Bound only, not an adjustment: consistent digit-for-digit swaps (the hand's 9 read as 4), hyp digit -> ref digit,
    same rule (>= 80% of >= 5 aligned occurrences). These are misreadings; the bound shows how much one fact about the
    hand's shapes would fix."""
    cnt = collections.defaultdict(collections.Counter)
    for h, r in pairs:
        if h.isdigit():
            cnt[h][r] += 1
    out = {}
    for k, c in cnt.items():
        tot = sum(c.values())
        top, n = c.most_common(1)[0]
        if tot >= 5 and n / tot >= 0.8 and top != k and top.isdigit():
            out[k] = top
    return out


def main(out_dir, pas="pass1"):
    pages = json.load(open(HERE / "frame2" / "pages2.json"))
    plain = {r["doc"]: r for r in json.load(open(HERE / "scores2.json"))["rows"]}
    rows = []
    for d, v in sorted(pages.items(), key=lambda x: int(x[0][1:])):
        hyp = Path(out_dir) / f"{pas}_{d}.txt"
        if not hyp.exists():
            continue
        letter = v["stratum"] == "letter"
        ref = ref_alnum(v["reference"], letter)
        hl = [hyp_tokens(l.rstrip("! "), letter) for l in score.hyp_lines(str(hyp))]
        keep = r"[^0-9a-z?" + GREEK + "]"
        blocks = [re.sub(keep, "", "".join(hl[i:i + BLOCK]).lower()) if letter else
                  score.digits("".join(hl[i:i + BLOCK]), keep_q=True, alnum=True) for i in range(0, len(hl), BLOCK)]
        halves = ([], [])
        for k, b in enumerate(blocks):
            if b:
                halves[k % 2].extend(fit_pairs(b, ref)[3])
        m0, m1 = learn(halves[0], letter), learn(halves[1], letter)
        rules = {k: t for k, t in m0.items() if m1.get(k) == t}
        h0, h1 = learn_hand(halves[0]), learn_hand(halves[1])
        hand = {k: t for k, t in h0.items() if h1.get(k) == t}
        if letter:
            ref_s = ref
            hyp_l = ["".join(rules.get(ch, ch) for ch in re.sub(keep, "", l.lower())) for l in hl]
        else:
            ref_s = score.digits("".join(rules.get(ch, ch) for ch in ref))  # mapped letters -> digits, rest dropped
            hyp_l = hl
        hyp_s = "".join(hyp_l) if letter else score.digits("".join(hyp_l), keep_q=True)
        hyp_s = re.sub(r"[^0-9a-z?" + GREEK + "]", "", hyp_s.lower()) if letter else hyp_s
        strict = score.lev_ops(ref_s, hyp_s)[3]
        eo = min(strict, order_tolerant_raw(ref_s, hyp_l, letter))
        eh = eo
        if hand:
            hyp_h = ["".join(hand.get(ch, ch) for ch in l) for l in hyp_l]
            hs = "".join(hand.get(ch, ch) for ch in hyp_s)
            eh = min(score.lev_ops(ref_s, hs)[3], order_tolerant_raw(ref_s, hyp_h, letter))
        rows.append({"doc": d, "stratum": v["stratum"], "source": v["source"], "ref_signs": len(ref_s),
                     "edits": eo, "cer_adjusted": round(eo / max(1, len(ref_s)), 4), "rules": rules,
                     "hand_swaps": hand, "edits_hand_bound": eh, "cer_hand_bound": round(eh / max(1, len(ref_s)), 4),
                     "rules_half_only": {k: t for k, t in {**m0, **m1}.items() if k not in rules},
                     "cer_plain_strict": plain[d]["cer"], "cer_plain_order_tolerant": plain[d]["cer_order_tolerant"]})
        print(f"{d:7} {v['stratum']:6} strict {100 * plain[d]['cer']:6.2f}%  order {100 * plain[d]['cer_order_tolerant']:6.2f}%"
              f"  adjusted {100 * rows[-1]['cer_adjusted']:6.2f}%  rules {rules}")
    json.dump({"pass": pas, "rows": rows}, open(HERE / "scores2_adjusted.json", "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1], *(sys.argv[2:3]))
