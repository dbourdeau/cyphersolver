"""Split ocr_frames.jsonl into messages: messages_ocr.jsonl.

A message is a run of 4- or 5-digit groups, broken by any line or stretch of clear words. The clear words before the
run (route, address, discriminant) and after it (date, number, signature) are kept. Counter groups 00025, 00050 ... are
marked out and removed from `groups`. OCR only: provisional, frames are checked by eye before anything is claimed.
"""
import collections, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DISC = ['SWET', 'SVET', 'SVBT', 'MISTERIA', 'PALLADA', 'ANCHAR', 'ANTCHAR', 'ANTSCHAR', 'FORUM', 'SIRIUS', 'LIKOWU',
        'DELEGAT', 'AZIYA', 'BUNEL', 'WIEDERHOLUNG']
NORM = {'SVET': 'SWET', 'SVBT': 'SWET', 'ANTCHAR': 'ANCHAR', 'ANTSCHAR': 'ANCHAR'}
BOILER = re.compile(r"CLASSIFICATION CANCELED.*?\n.*?\n.*?(19\d*|\d+)\s*\n", re.S)
GROUP = re.compile(r'^[0-9IlOo]{4,5}$')


def tokens(text):
    return text.replace('\n', ' \n ').split(' ')


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    msgs = []
    for line in open(os.path.join(HERE, 'ocr_frames.jsonl'), encoding='utf-8'):
        fr = json.loads(line)
        t = BOILER.sub('', fr['text'], count=1)
        clear, run, prev = [], [], ''
        def flush():
            nonlocal clear, run, prev
            if len(run) >= 8:
                msgs.append({'file': fr['file'], 'head': prev[-160:], 'groups': run})
                prev = ''
                clear = []
            elif run:
                clear += run
            run = []
        for w in t.split():
            s = w.strip('.,;:-"\'')
            if s and GROUP.match(s) and any(c.isdigit() for c in s):
                run.append(s.replace('I', '1').replace('l', '1').replace('O', '0').replace('o', '0'))
            elif re.fullmatch(r'\d{1,3}', s or 'x') and run:
                continue  # stray number inside a run: interlinear correction or OCR split
            else:
                flush()
                prev = (prev + ' ' + w)[-200:]
        flush()
    for m in msgs:
        head = m['head'].upper().replace(' ', '')
        disc = [d for d in DISC if d in head]
        m['disc'] = NORM.get(disc[-1], disc[-1]) if disc else ''
        m['counters'] = [g for g in m['groups'] if re.fullmatch(r'00(025|050|075|100|125|150|175|200|225|250)', g)]
        m['groups'] = [g for g in m['groups'] if g not in m['counters']]
        L = collections.Counter(len(g) for g in m['groups'])
        m['len'] = L.most_common(1)[0][0]
        m['n'] = len(m['groups'])
    with open(os.path.join(HERE, 'messages_ocr.jsonl'), 'w', encoding='utf-8') as f:
        for m in msgs:
            f.write(json.dumps(m, ensure_ascii=False) + '\n')
    c = collections.Counter((m['disc'], m['len']) for m in msgs)
    g = collections.Counter()
    for m in msgs:
        g[(m['disc'], m['len'])] += m['n']
    print(len(msgs), 'messages', sum(g.values()), 'groups')
    for k, v in sorted(c.items(), key=lambda x: -g[x[0]]):
        print(k, v, g[k])


if __name__ == '__main__':
    main()
