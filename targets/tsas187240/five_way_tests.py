"""Short, manuscript-motivated cribs. Run with UTF-8 stdout."""

from itertools import product
import random
import sys
from functools import lru_cache
from zipfile import ZipFile

from crib_windows import windows
from scan_bible import chapters
from test_psalm import HEBREW, TARGUM
from test_alphabet import FOLD
from test_alphabet import B1, B2, C2
from test_tafsir import discrepancies


PSALMS = [HEBREW.format(say=a, scribe=b) for a, b in
          product(('אמר','אומר'), ('ספר','סופר'))]
SCHOOL = ['הקץ עצל דיך מנום גרש כזב פן תסף חטא',
          'אתה גחי צור מבטן כל זעם סף קדשך נפץ',
          'אצלך חפץ גזר השם טוב מכסף קנין דעת']
NAMES = 'אלף בית גימל דלת הא וו זין חית טית יוד כף למד מם נון סמך עין פא צדי קוף ריש שין תו'


def report(label, texts):
    for gaps in (True, False):
        hits = set()
        for t in texts:
            for _, direction, excerpt, key in windows(t, gaps=gaps):
                pair = (3, 2) if direction == 1 else (2, 3)
                hits.add((excerpt, direction, ''.join(key[s] for s in pair)))
        print(label, 'two gaps' if gaps else 'ends only', len(hits), sorted(hits)[:10])


@lru_cache(maxsize=None)
def distance(a,b):
    last = list(range(len(b)+1))
    for i,c in enumerate(a,1):
        row = [i]
        for j,x in enumerate(b,1):
            row.append(min(last[j]+1, row[-1]+1, last[j-1]+(c!=x)))
        last = row
    return last[-1]


def rubric(path):
    target = 'בשמך מלכי אחוז בדף'.translate(FOLD).split()
    best, rows = 100, []
    with ZipFile(path) as z:
        for chapter in chapters(z):
            words = [w.translate(FOLD) for w,_ in chapter]
            for i in range(len(words)-3):
                sample = words[i:i+4]
                cost = sum(distance(a,b) for a,b in zip(target,sample))
                if cost < best:
                    best, rows = cost, []
                if cost == best:
                    rows.append((chapter[i][1],' '.join(sample)))
    print('rubric distance',best,rows)


def second_batch():
    for pe in ('פא','פה','פי'):
        suffix = (pe+' צדי קוף ריש שין תו').translate(FOLD).split()
        for signs in (B2,B2[:7]+B2[8:]):
            text = ''.join(suffix)[:len(signs)]
            print('next names',pe,len(signs),[len(discrepancies(signs[::d],text)) for d in (1,-1)])
    names = NAMES.split()
    paired = [' '.join(n for pair in zip(names[:11],tail) for n in pair)
              for tail in (names[11:],names[11:][::-1])]
    report('alternating letter names', paired)
    report('Shema and response', ['שמע ישראל יהוה אלהינו יהוה אחד ברוך שם כבוד מלכותו לעולם ועד'])
    report('Arabic invocation', ['בסם אללה אלרחמן אלרחים',
                                 'בסם אללה אלרחמן אלרחים אלחמד ללה רב אלעאלמין'])
    rng = random.Random(187240)
    successes = 0
    for _ in range(1000):
        shuffled = rng.sample(names,len(names))
        successes += bool(list(windows(' '.join(shuffled))))
    print('reordered names with a first-row fit',successes,'/ 1000')


def turned_name_hits(text):
    flat = text.replace(' ','').translate(FOLD)
    row = B2[:7]+B2[8:]
    for i,d,excerpt,key in windows(text):
        nxt = flat[i+len(excerpt):i+len(excerpt)+len(row)]
        if len(nxt) != len(row) or discrepancies(row[::-d],nxt):
            continue
        yield d,excerpt,nxt,key|dict(zip(row[::-d],nxt))


def third_batch():
    a = NAMES.split()
    ordered = ' '.join(n for pair in zip(a[:11],a[11:][::-1]) for n in pair)
    for d, excerpt, nxt, key in turned_name_hits(ordered):
        print('turned continuation',d,excerpt,nxt)
        print('C2 projection',''.join(key.get(s,'?') for s in C2[::-d]))
        print('loop values G03 G05 G13',[key[s] for s in (3,5,13)])
        pair = ''.join(key[i] for i in ((3,2) if d==1 else (2,3)))
        print('A2 pair',pair,'occurrences within B1+B2 text',(excerpt+nxt).count(pair))
        end = ordered.replace(' ','').translate(FOLD).index(excerpt)+len(excerpt+nxt)
        print('end at word boundary',end in {len(''.join(ordered.split()[:j])) for j in range(len(a)+1)})
    rng = random.Random(187240)
    count = sum(bool(list(turned_name_hits(' '.join(rng.sample(a,len(a))))))
                for _ in range(1000))
    print('reordered names fitting two turned rows',count,'/ 1000')


def screen(label, strings, enforce_gaps=True):
    fits, verified = set(),set()
    for text in strings:
        words=text.translate(FOLD).split()
        flat=''.join(words)
        edges={len(''.join(words[:i])) for i in range(len(words)+1)}
        for first, second, da, db in product((B1,B1[1:]), (B2,B2[:7]+B2[8:]), (1,-1),(1,-1)):
            tags=first[::da]+second[::db]
            for i in range(len(flat)-len(tags)+1):
                mid=i+len(first)
                cuts=(i+3,i+11) if da==-1 else (mid-3,mid-11)
                if enforce_gaps and not {i,mid,i+len(tags),*cuts}<=edges:
                    continue
                excerpt=flat[i:i+len(tags)]
                if discrepancies(tags,excerpt):
                    continue
                key=dict(zip(tags,excerpt))
                fits.add((tags,excerpt))
                target=iter(flat[mid:i+len(tags)])
                # Unknown C2 signs consume one letter each. The rest must occur
                # in order, with only losses allowed in this comparison copy.
                if all(any(tag not in key or key[tag]==ch for ch in target) for tag in C2[::db]):
                    verified.add((tags,excerpt))
    print(label,'distinct row fits',len(fits),'also passing C2',len(verified))
    return verified


def fourth_batch(path):
    with ZipFile(path) as z:
        ps=next(w for w in chapters(z) if w[0][1].startswith('Ps.45.'))
    words=[w for w,_ in ps]
    for idx,label in [(0,'Psalm 45 word initials'),(-1,'Psalm 45 word endings')]:
        screen(label,[''.join(w[idx] for w in words)],False)
    psalm=' '.join(words)
    screen('divine-name abbreviations',[psalm.replace('יהוה',y).replace('אלהים',e)
                                       for y,e in product(('יי','י'),('אל','ה'))])
    abc='אבגדהוזחטיכלמנסעפצקרשת'
    screen('paired alphabet drills',[' '.join(x+y for x,y in zip(abc[:11],tail))
                                    for tail in (abc[11:],abc[11:][::-1])]+
           [' '.join(x+y for x,y in zip(abc,abc[1:]+abc[:1]))])
    def numeral(n):
        if n in (15,16):
            return ('טו','טז')[n-15]
        tens,ones=divmod(n,10)
        return ('יכלמנסעפצ'[tens-1] if tens else '')+(abc[ones-1] if ones else '')
    screen('Hebrew numbers 1 to 99',[' '.join(numeral(n) for n in range(1,100))])


def fifth_batch(path):
    from itertools import accumulate, zip_longest
    from test_tafsir import ENDING
    with ZipFile(path) as z:
        ps=next(w for w in chapters(z) if w[0][1].startswith('Ps.45.'))
    sources=[' '.join(w for w,_ in ps),TARGUM,ENDING,NAMES,*SCHOOL]
    for mode in ('lower row first','interleaved columns','reverse each word',
                 'reverse word order','shift row boundary by one'):
        fits,passed=set(),set()
        for source in sources:
            words=source.translate(FOLD).split()
            if mode=='reverse each word':
                words=[w[::-1] for w in words]
            if mode=='reverse word order':
                words=words[::-1]
            text=''.join(words)
            edges=set(accumulate(map(len,words),initial=0))
            for first,second,da,db in product((B1,B1[1:]),(B2,B2[:7]+B2[8:]),(1,-1),(1,-1)):
                top,bottom=first[::da],second[::db]
                tags=top+bottom
                top_start=0
                if mode=='lower row first':
                    tags=bottom+top
                    top_start=len(bottom)
                if mode=='interleaved columns':
                    tags=tuple(v for pair in zip_longest(top,bottom) for v in pair if v is not None)
                gaps=(3,11) if da==-1 else (len(top)-3,len(top)-11)
                for start in edges:
                    end=start+len(tags)
                    if end not in edges:
                        continue
                    if mode!='interleaved columns':
                        if any(start+top_start+i not in edges for i in gaps):
                            continue
                        midpoint=start+(len(bottom) if top_start else len(top))
                        offsets=(-1,1) if mode=='shift row boundary by one' else (0,)
                        if not any(midpoint+j in edges for j in offsets):
                            continue
                    excerpt=text[start:end]
                    if discrepancies(tags,excerpt):
                        continue
                    key=dict(zip(tags,excerpt))
                    fits.add((tags,excerpt))
                    prediction=iter(key[tag] for tag in bottom)
                    if all(any(tag not in key or key[tag]==ch for ch in prediction) for tag in C2[::db]):
                        passed.add((tags,excerpt))
        print(mode,'distinct row fits',len(fits),'also passing C2',len(passed))


if __name__ == '__main__':
    report('single row', PSALMS+[TARGUM]+SCHOOL)
    report('letter names', [NAMES, NAMES.replace('גימל','גמל').replace('פא','פה')])
    second_batch()
    third_batch()
    if len(sys.argv)>1:
        rubric(sys.argv[1])
        fourth_batch(sys.argv[1])
        fifth_batch(sys.argv[1])
