# Rank candidate words for code groups blank on the R9115 key, by en-1640s LM score in context.
# Candidates: words that fit the group's alphabetical slot between key neighbours (if any) plus context-plausible ones.
from lang import lm
M=lm.load('en-1640s')
def sc(t):
    s=M.norm(t) if hasattr(M,'norm') else lm.norm(t)
    return M.score(s)
cases={
 '160 (case 153 < x < condition 163)':("the only way is {} to be that his majesty will please to prevent",['conceived','considered','commanded','concluded','certain','chosen','come']),
 '539 (such 537 < x < should 540)':("pressing that mr forster {} give in his answer",['should','shall','so','such','still','say','must','would','may']),
 '319 (have 318 < x < him 323)':("to be that {} will please to prevent that cause",['his highness','his majesty','he','heaven','her','hee','the king']),
 '650 (wise 648 < x ; 652 you)':("the only {} is conceived to be that",['way','wise','work','worth','wish','means','remedy','hope']),
 '359 (instruction 354 < x < know 361)':("i am {} he has done mr forster no good offices here",['informed','intended','judged','told','invited','inclined','just']),
 '444 (only 441 < x < offered 449)':("he has done mr forster no good {} here",['offices','office','opinion','order','others','offers','occasion']),
 '452 (out 451 < x < our 456)':("they have an eye {} him",['over','upon','on','out','of','after','our']),
}
for k,(ctx,c) in cases.items():
    r=sorted(((sc(ctx.format(w)),w) for w in c),reverse=True)
    print(k,' | '.join(f'{w} {s:.1f}' for s,w in r[:4]))
