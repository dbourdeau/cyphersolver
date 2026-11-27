"""Hypothesis (d): is the block (part of) the compiler's answer verses 47v l.9-48r l.6 (read here by eye, medium)?
Same LCS climb as align_verses.py; argv = true|shuf seed."""
import sys, random
from align_verses import run, lines
A = ('يا سايلا برموز ترجمت واتت كانها الروض في حسن اذا كملا مدبجات بدر فابن بها بروق منطرها من ذاقها عسلا '
     'ان الوليد هلال والثياب بلا خيط لادم في الجنان قد حصلا او الدروع التي ختار من زرد من نسج داود او من بعده عملا '
     'والسيف ان سلها ابوه وساعة رمل بالزجاج جبان اسمع مثلا اوكان مقصد العينان باصرة فالحكم محتمل ان كانت المقلا '
     'اما الشوارب فالاشجار ثم مساكن فروج وريح لم تدع بللا ثم النجوم فصال فقد كرث فخذ نظما برد جواب قلته عجلا')
if __name__ == '__main__':
    mode, seed = sys.argv[1], int(sys.argv[2]); w = A.split()
    if mode == 'shuf': random.seed(200 + seed); random.shuffle(w)
    plain = ''.join(w); toks = [t for l in lines for t in l if t != '|']
    sc, _ = run(toks, plain, 20 + seed, 2500)
    print('answer', mode, seed, 'letters', len(plain), 'LCS', sc, 'share of signs', round(sc / len(toks), 3), flush=True)
