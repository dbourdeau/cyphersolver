"""Calibrate blind substitution search on 43-letter Arabic passages and figure 69.

Supply OpenITI training texts and a separate UTF-8 Arabic control passage.
The controls have perfect sign identities at all positions outside the faded areas.
A trigram score ranks letter assignments; its output is not a translation.
"""
import argparse
from pathlib import Path
import re

import numpy as np
from numba import njit
from check_passages import words

ALPHABET = "ءابتثجحخدذرزسشصضطظعغفقكلمنهوي" + "ة"
N = len(ALPHABET)
INDEX = {ch: i for i, ch in enumerate(ALPHABET)}
UNKNOWN = N
TOP = "ABCDEFGbJk???mnoPqHCI"
BOTTOM = "JvLldfgTiU???sdyzdwAhT"
assert (len(TOP), len(BOTTOM)) == (21, 22)


@njit
def diversity_histogram(seq, visible, length):
    hist = np.zeros(len(visible)+1, dtype=np.int64)
    for start in range(len(seq)-length+1):
        seen = np.zeros(N, dtype=np.uint8)
        for offset in visible:
            seen[seq[start+offset]] = 1
        hist[seen.sum()] += 1
    return hist


def diversity(paths):
    from check_shapes import lines
    transcript = TOP + BOTTOM
    visible = np.array([i for i,c in enumerate(transcript) if c != "?"])
    for path in paths:
        hist = np.zeros(len(visible)+1, dtype=np.int64)
        for _, text in lines(path):
            seq = np.array([INDEX[c] for c in text], dtype=np.uint8)
            hist += diversity_histogram(seq, visible, len(transcript))
        print(path.name, int(hist.sum()), "windows;", {
            i:int(n) for i,n in enumerate(hist) if i >= 20 and n})


def train(paths):
    unigrams = np.ones(N)
    bigrams = np.zeros((N, N))
    trigrams = np.zeros((N, N, N))
    for p in paths:
        body = p.read_text(encoding="utf-8-sig").split("#META#Header#End#")[-1]
        for para in re.split(r"\n#+", re.sub(r"PageV\d+P\d+|ms\d+", " ", body)):
            chars = [INDEX[c] for c in "".join(words(para))]
            seq = np.asarray(chars, dtype=np.int32)
            unigrams += np.bincount(seq, minlength=N)
            bigrams += np.bincount(seq[:-1]*N + seq[1:], minlength=N*N).reshape(N,N)
            tri = (seq[:-2]*N + seq[1:-1])*N + seq[2:]
            trigrams += np.bincount(tri, minlength=N**3).reshape(N,N,N) if len(tri) else 0
    p1 = unigrams / unigrams.sum()
    p2 = (bigrams + 15*p1) / (bigrams.sum(axis=1, keepdims=True) + 15)
    p3 = (trigrams + 30*p2) / (trigrams.sum(axis=2, keepdims=True) + 30)
    logp = np.zeros((N+1,N+1,N+1))
    logp[:,:, :N] = np.log(p1)
    logp[:, :N, :N] = np.log(p2)
    logp[:N,:N,:N] = np.log(p3)
    return logp


@njit
def fitness(seq, key, logp):
    a = b = UNKNOWN
    total = 0.
    for token in seq:
        c = key[token]
        total += logp[a,b,c]
        a,b = b,c
    return total


@njit
def optimize(seq, n_used, logp, restarts, seed):
    np.random.seed(seed)
    best_score = -1.e20
    best_key = np.arange(N+1)
    for r in range(restarts):
        key = np.arange(N+1)
        key[:N] = np.random.permutation(N)
        score = fitness(seq, key, logp)
        for iteration in range(10000):
            i = np.random.randint(n_used)
            j = np.random.randint(N)
            if i == j:
                continue
            key[i], key[j] = key[j], key[i]
            proposal = fitness(seq, key, logp)
            temp = 3.0 * (1 - iteration/10000.)**2 + 0.04
            if proposal >= score or np.random.random() < np.exp((proposal-score)/temp):
                score = proposal
                if score > best_score:
                    best_score, best_key = score, key.copy()
            else:
                key[i], key[j] = key[j], key[i]
    return best_score, best_key


def solve(label, text, model, restarts, truth=None):
    signs = list(dict.fromkeys(text.replace("?", "")))
    assert len(signs) <= N
    seq = np.array([UNKNOWN if c=="?" else signs.index(c) for c in text], dtype=np.int64)
    runs = []
    for seed in (101, 202):
        score,key = optimize(seq, len(signs), model, restarts, seed)
        output = "".join("?" if token==UNKNOWN else ALPHABET[key[token]] for token in seq)
        runs.append((score,output))
    score,output = max(runs)
    valid = [i for i,c in enumerate(text) if c!="?"]
    agree = sum(runs[0][1][i]==runs[1][1][i] for i in valid)
    print(label, "visible", len(valid), "classes",len(signs),"agreement",agree,"best",round(score,2),output)
    if truth:
        correct = sum(output[i]==truth[i] for i in valid)
        key = np.arange(N+1)
        for i,sign in enumerate(signs):
            key[i] = INDEX[sign]
        print("correct", correct, "true score", round(fitness(seq,key,model),2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("control", type=Path)
    parser.add_argument("training",type=Path,nargs="+")
    parser.add_argument("--restarts",type=int,default=35)
    args = parser.parse_args()
    model = train(args.training)
    transcript = TOP + BOTTOM
    passage = "".join(words(args.control.read_text(encoding="utf-8-sig")))
    for i in range(0,min(430,len(passage)-42),43):
        truth = passage[i:i+43]
        visible = "".join("?" if c=="?" else t for t,c in zip(truth,transcript))
        solve(f"control {i}",visible,model,args.restarts,truth)
    # Lowercase and uppercase labels are separate signs by default. In the
    # base-shape model ignore the small marks in the explicitly listed families.
    base_top = TOP.translate(str.maketrans("bPn", "BJJ"))
    base_bottom = BOTTOM.translate(str.maketrans("lh", "LH"))
    for label, top, bottom in (("tailed signs grouped", TOP.replace("P","n"), BOTTOM),
            ("base", base_top, base_bottom),
            ("wavy signs grouped", base_top.replace("q", "k"),
             base_bottom.translate(str.maketrans("zs", "kD")))):
        for direction,upper,lower in (("RTL",top,bottom),("LTR",top[::-1],bottom[::-1])):
            for order,s in (("upper first",upper+lower),("lower first",lower+upper)):
                solve(f"Berlin {label} {direction} {order}",s,model,args.restarts)
