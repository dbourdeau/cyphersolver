import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collections import Counter, defaultdict
import difflib, json, random, shutil
from common import norm
import p5


def make_rows(half, rows, src):
  return [
      {"half": half, "i": i, "tag": r["tag"], "text": r["text"], "src": src}
      for i, r in enumerate(rows)
  ]


def get_tokens(rows):
  # same scan as the rewrite below (p5.NUM over the text), so positions line up one to one
  return [m.group(0) for r in rows if r["tag"] == "L" for m in p5.NUM.finditer(r["text"]) if m.group(0).isdigit()]


def nt(rows):
  return len(get_tokens(rows))


def gl(rows):
  return sum(len(norm(r["text"])) for r in rows if r["tag"] == "G")


def ok(new, old):
  return (
      abs(nt(new) - nt(old)) <= max(8, 0.2 * nt(old))
      and gl(new) <= 1.5 * gl(old) + 60
  )


def load_w(path):
  halves, by_half = [], defaultdict(list)
  with open(path, encoding="utf-8") as f:
    for line in f:
      if line.strip():
        r = json.loads(line)
        if r["half"] not in by_half:
          halves.append(r["half"])
        by_half[r["half"]].append(r)
  return halves, {h: make_rows(h, by_half[h], "W") for h in halves}


def load_strips(path):
  out = {}
  with open(path, encoding="utf-8") as f:
    for line in f:
      if line.strip():
        r = json.loads(line)
        if not r.get("error") and r.get("text") is not None:
          out[r["half"]] = p5.parse(r["text"])
  return out


def vote_half(base_rows, other_sources):
  base_tokens = get_tokens(base_rows)
  votes = defaultdict(list)
  for o_rows in other_sources:
    o_tokens = get_tokens(o_rows)
    sm = difflib.SequenceMatcher(None, base_tokens, o_tokens, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
      if tag == "equal" or (tag == "replace" and i2 - i1 == j2 - j1):
        for k in range(i2 - i1):
          votes[i1 + k].append(o_tokens[j1 + k])
  new_tokens = list(base_tokens)
  replaced = 0
  for idx, tok in enumerate(base_tokens):
    v = votes[idx]
    if len(v) >= 2 and len(set(v)) == 1 and v[0] != tok:
      new_tokens[idx] = v[0]
      replaced += 1
  it = iter(new_tokens)
  out = []
  for r in base_rows:
    txt = r["text"]
    if r["tag"] == "L":
      txt = p5.NUM.sub(
          lambda m: next(it) if m.group(0).isdigit() else m.group(0), txt
      )
    out.append({**r, "text": txt})
  return out, replaced


def build_pairs(by_half, half_list):
  pairs = []
  for h in half_list:
    pairs.extend(p5.gloss_pairs(by_half[h]))
  return pairs


def eval_subset(name, half_list, w_map, c_map, key):
  w_pairs = build_pairs(w_map, half_list)
  c_pairs = build_pairs(c_map, half_list)
  w_score = p5.gloss_score(key, w_pairs)
  c_score = p5.gloss_score(key, c_pairs)
  rng = random.Random(7)
  shuf = [p5.gloss_score(p5.shuffled(key, rng), c_pairs) for _ in range(200)]
  s_mean = sum(shuf) / len(shuf) if shuf else 0.0
  s_max = max(shuf) if shuf else 0.0
  g_lets = sum(gl(c_map[h]) for h in half_list)
  print(
      f"{name:12s} | W: {w_score:.4f} | chosen: {c_score:.4f} | "
      f"shuf_mean: {s_mean:.4f} | shuf_max: {s_max:.4f} | "
      f"pairs: {len(c_pairs)} | gloss_letters: {g_lets}"
  )


def main():
  halves, w_map = load_w("data/p5_lines.whole_page.jsonl")
  s25 = load_strips("data/strips_full.jsonl")
  s15 = load_strips("data/strips_retry.jsonl")
  key = p5.load_key("data/key_c04.json")

  a_map, b_map = {}, {}
  total_replaced = 0
  for h in halves:
    w_rows = w_map[h]
    ok25 = h in s25 and ok(s25[h], w_rows)
    ok15 = h in s15 and ok(s15[h], w_rows)
    if ok25:
      a_rows = make_rows(h, s25[h], "S25")
    elif ok15:
      a_rows = make_rows(h, s15[h], "S15")
    else:
      a_rows = make_rows(h, w_rows, "W")
    a_map[h] = a_rows
    if ok25 and ok15:
      b_rows, rep = vote_half(a_rows, [s15[h], w_rows])
      total_replaced += rep
    else:
      b_rows = [dict(r) for r in a_rows]
    b_map[h] = b_rows

  fit_halves = [h for h in halves if p5.fold(h) == "fit"]
  w_fit = p5.gloss_score(key, build_pairs(w_map, fit_halves))
  a_fit = p5.gloss_score(key, build_pairs(a_map, fit_halves))
  b_fit = p5.gloss_score(key, build_pairs(b_map, fit_halves))
  choice = "B" if b_fit > a_fit else "A"
  chosen_map = b_map if choice == "B" else a_map
  print(f"FIT scores | W: {w_fit:.4f} | RULE A: {a_fit:.4f} | RULE B: {b_fit:.4f}")
  print(f"Chosen rule: RULE {choice} | tokens replaced by vote: {total_replaced}")

  test_halves = [h for h in halves if p5.fold(h) == "test"]
  fresh_halves = [
      h
      for h in halves
      if h.split("/")[0] not in p5.TRAIN_VOLS and h[:-1] not in p5.SPENT
  ]
  eval_subset("test", test_halves, w_map, chosen_map, key)
  eval_subset("fresh", fresh_halves, w_map, chosen_map, key)
  vols = list(dict.fromkeys(h.split("/")[0] for h in halves))
  for v in vols:
    eval_subset(
        v, [h for h in halves if h.split("/")[0] == v], w_map, chosen_map, key
    )

  pass
  with open("data/p5_lines.jsonl", "w", encoding="utf-8") as f:
    for h in halves:
      for r in chosen_map[h]:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
  counts = Counter(chosen_map[h][0]["src"] for h in halves if chosen_map[h])
  print("Halves per src:", dict(counts))


if __name__ == "__main__":
  main()

