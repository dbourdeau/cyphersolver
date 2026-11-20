"""Single frozen evaluation using character centers on the 1807 French clear copy."""
import csv
import json
import random
import re
import unicodedata
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

p = Path(__file__).resolve().parent
with (p / 'vienna_groups.tsv').open() as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
ngroups = len(rows)
assert ngroups == 330
clear = (p / 'vienna_clear_copy.txt').read_text().lower()
clear = clear.replace('propo-\nsitions', 'propositions').replace('cho-\nses', 'choses')
clear = ''.join(c for c in unicodedata.normalize('NFD', clear) if not unicodedata.combining(c))
words = re.findall('[a-z]+',clear)
nletters = sum(map(len,words))
denom = 2 * ngroups * nletters
lo = 0
word_centers = {}
for i,w in enumerate(words,1):
    word_centers[i] = ngroups * (2*lo+len(w))
    lo += len(w)
groups = {int(r['ordinal']):r['strict_key'] for r in rows}
group_centers = {i:(2*i-1)*nletters for i in groups}
fit_c = defaultdict(list)
fit_w = defaultdict(list)
for i,c in groups.items():
    if c!='?' and 100*group_centers[i] <= 55*denom:
        fit_c[c].append(i)
for j,w in enumerate(words,1):
    if len(w)>=2 and 100*word_centers[j] <= 55*denom:
        fit_w[w].append(j)


def near(i,j):
    return 20*abs(group_centers[i]-word_centers[j]) <= denom


def fit_cost(indices, occurrences):
    costs = {0: 0}
    for i in indices:
        new_costs = {}
        for j in occurrences:
            if near(i,j):
                prior = [cost for jj,cost in costs.items() if jj < j]
                if prior:
                    new_costs[j] = min(prior) + abs(group_centers[i]-word_centers[j])
        costs = new_costs
    return min(costs.values()) if costs else None


key = {}
learned = ['code\ttrain_slots\tword\tmean_absolute_center_difference']
for code,indices in sorted(fit_c.items()):
    if len(indices) < 2:
        continue
    candidates = []
    for word,occurrences in fit_w.items():
        cost = fit_cost(indices,occurrences)
        if cost is not None:
            candidates.append((cost,len(occurrences),word))
    if candidates:
        cost,_,word = min(candidates)
        key[code] = word
        learned.append(f"{code}\t{','.join(map(str,indices))}\t{word}\t{cost/denom/len(indices):.6f}")
(p/'vienna_fitted.tsv').write_text('\n'.join(learned)+'\n')
held = [i for i in groups if 100*group_centers[i]>=65*denom]
prediction_slots = [i for i in held if groups[i] in key]
nearby = {i:[j for j in word_centers if 100*word_centers[j]>=60*denom and near(i,j)] for i in prediction_slots}


def best_matches(candidate):
    @lru_cache(maxsize=None)
    def visit(slot,last):
        if slot == len(prediction_slots):
            return ()
        i = prediction_slots[slot]
        choices = [visit(slot+1,last)]
        for j in nearby[i]:
            if j>last and words[j-1] == candidate[groups[i]]:
                choices.append(((i,j),)+visit(slot+1,j))
        return min(choices,key=lambda seq:(-len(seq),seq))
    return visit(0,0)


real = best_matches(key)
rng = random.Random(18070124)
codes = sorted(key)
counts = []
for _ in range(1000):
    values = [key[c] for c in codes]
    rng.shuffle(values)
    counts.append(len(best_matches(dict(zip(codes,values)))))
(p/'vienna_controls.tsv').write_text('shuffle\tordered_matches\n'+''.join(f'{i+1}\t{s}\n' for i,s in enumerate(counts)))
matched = dict(real)
pred = ['ordinal\tline\tline_position\tcode\tpredicted\tmatched_clear_word_index']
for i in prediction_slots:
    r=rows[i-1]
    pred.append(f"{i}\t{r['line']}\t{r['position']}\t{groups[i]}\t{key[groups[i]]}\t{matched.get(i,'')}")
(p/'vienna_predictions.tsv').write_text('\n'.join(pred)+'\n')
num_types=len({words[j-1] for _,j in real})
result=dict(cipher_slots=ngroups,clear_word_units=len(words),clear_letters=nletters,fit_group_slots=sum(100*x<=55*denom for x in group_centers.values()),fit_recurring_types=sum(len(v)>=2 for v in fit_c.values()),fit_types=len(key),held_slots=len(held),held_secure=sum(groups[i]!='?' for i in held),predictions=len(prediction_slots),ordered_matches=len(real),matched_types=num_types,control_histogram=dict(Counter(counts)),control_max=max(counts),controls_equal_or_better=sum(c>=len(real) for c in counts),passed=len(real)>=5 and num_types>=4 and len(real)>max(counts),march_values={c:[i for i in groups if groups[i]==c] for c in ('210o','718+')})
(p/'vienna_result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
