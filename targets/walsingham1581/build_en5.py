"""Build a full-alphabet 5-gram model from the two Scottish state-paper calendars."""

from pathlib import Path
import re

import numpy as np

alpha = "abcdefghijklmnopqrstuvwxyz"
paths = [
    Path("CSP_Scotland_v5_1574-1581.txt"),
    Path("CSP_Scotland_v6_1581-1583.txt"),
]
text = "".join(p.read_text(encoding="utf-8", errors="ignore").lower() for p in paths)
# Remove Roman-numeral headings, pagination, and editorial apparatus before
# concatenating prose; the model is only an aid, not evidence of plaintext.
text = re.sub(r"\b[ivxlcdm]{2,}\b", " ", text)
text = re.sub(r"[^a-z]+", "", text)
codes = np.frombuffer(text.encode("ascii"), dtype=np.uint8) - ord("a")
k = 26
previous = None
for n in range(1, 6):
    shape = (k,) * n
    rolling = np.zeros(len(codes) - n + 1, dtype=np.int64)
    for j in range(n):
        rolling = rolling * k + codes[j : j + len(rolling)]
    count = np.bincount(rolling, minlength=k**n).reshape(shape).astype(np.float32)
    if n == 1:
        prob = (count + 0.1) / (count.sum() + 0.1 * k)
    else:
        lower = previous.reshape((1,) * (n - 1) + (k,)) if n == 2 else previous[None, ...]
        context = count.sum(axis=-1, keepdims=True)
        distinct = (count > 0).sum(axis=-1, keepdims=True)
        prob = np.where(
            context > 0,
            np.maximum(count - 0.75, 0) / np.maximum(context, 1)
            + 0.75 * distinct / np.maximum(context, 1) * lower,
            lower,
        ).astype(np.float32)
    previous = prob
    print(n, int(count.sum()), float(np.log(prob.max())), flush=True)
np.save("en5.npy", np.log(prob).astype(np.float32))
print("wrote en5.npy", len(text), flush=True)
