"""Budgeted key-editing harness (prototype), after Weight-Space Programming (Takehi et al. 2026).

The key is the "weights": a token -> letters table. An editor (an LLM, or a baseline script) may read everything for
free (the decode, per-token contexts, counts) but every call to score() spends one unit of a fixed budget. Each
session is logged to <session>/log.jsonl so the run can be copied into profile.json solution steps.

CLI (state lives in a session dir):
  keyedit.py init   <session> <task.json> [--budget N]
  keyedit.py view   <session> [--tok T] [--lines a:b]      free: key, counts, decode
  keyedit.py set    <session> TOK=letters [TOK=letters ...] free: edit the key ('' = null)
  keyedit.py score  <session>                              costs 1: LM score of the whole decode
  keyedit.py status <session>
  keyedit.py grade  <session>                              only for the experimenter: accuracy vs truth key
"""
import os, sys, re, json, glob, time, collections
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm


class Task:
    def __init__(self, spec, root='.'):
        self.spec = spec
        self.segs = []
        for pat in spec['token_files']:
            for f in sorted(glob.glob(os.path.join(root, pat))):
                for line in open(f, encoding='utf-8'):
                    m = re.match(r'(C\d+):\s*(.*)', line)
                    if m:
                        self.segs.append(m.group(2).split())
        self.model = lm.load(spec['model'], spaces=spec.get('spaces', False))
        self.scheme = spec.get('norm', 'early')
        self.counts = collections.Counter(t for s in self.segs for t in s)

    def decode(self, key):
        return [''.join(key.get(t, '') for t in s) for s in self.segs]

    def raw_score(self, key):
        tot = n = 0
        for d in self.decode(key):
            d = lm.norm(d, self.scheme, spaces=False)
            if len(d) > 4:
                tot += self.model.score(d)
                n += len(d)
        return tot / max(n, 1)


class Session:
    def __init__(self, path):
        self.path = path
        st = json.load(open(os.path.join(path, 'state.json'), encoding='utf-8'))
        self.state = st
        self.task = Task(st['task'], st['root'])

    def save(self):
        json.dump(self.state, open(os.path.join(self.path, 'state.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    def log(self, **kw):
        kw['t'] = round(time.time(), 1)
        with open(os.path.join(self.path, 'log.jsonl'), 'a', encoding='utf-8') as f:
            f.write(json.dumps(kw, ensure_ascii=False) + '\n')

    def score(self):
        if self.state['spent'] >= self.state['budget']:
            raise SystemExit('BUDGET EXHAUSTED: no more score() calls')
        s = self.task.raw_score(self.state['key'])
        self.state['spent'] += 1
        self.state['history'].append([self.state['spent'], round(s, 4)])
        self.log(op='score', spent=self.state['spent'], score=round(s, 4))
        self.save()
        return s

    def set(self, edits):
        for tok, letters in edits.items():
            self.state['key'][tok] = letters
        self.log(op='set', edits=edits)
        self.save()

    def grade(self):
        truth = json.load(open(os.path.join(self.path, 'truth.json'), encoding='utf-8')); key = self.state['key']
        cnt = self.task.counts
        tot = sum(cnt.values())
        ok = sum(n for t, n in cnt.items() if key.get(t, '') == truth.get(t, ''))
        wrong = sorted(((n, t, key.get(t, ''), truth.get(t, '')) for t, n in cnt.items()
                        if key.get(t, '') != truth.get(t, '')), reverse=True)
        return ok / tot, wrong, self.task.raw_score(truth)


def init(path, task_json, budget):
    spec = json.load(open(task_json, encoding='utf-8'))
    root = os.path.dirname(os.path.abspath(task_json))
    os.makedirs(path, exist_ok=True)
    key, truth = dict(spec['start_key']), spec['truth_key']
    held = spec.get('heldout')
    if held is not None:
        json.dump(held, open(os.path.join(path, 'heldout.json'), 'w', encoding='utf-8'))   # grading only, like truth.json
    spec = {k: v for k, v in spec.items() if k not in ('truth_key', 'heldout')}
    state = dict(task=spec, root=root, budget=budget, spent=0, key=key, history=[], start_key=dict(key))
    json.dump(truth, open(os.path.join(path, 'truth.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    json.dump(state, open(os.path.join(path, 'state.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if os.path.exists(os.path.join(path, 'log.jsonl')):
        os.remove(os.path.join(path, 'log.jsonl'))
    print('session', path, 'budget', budget)


def view(s, tok=None, lines=None):
    key = s.state['key']; T = s.task
    if tok:
        print(f'token {tok}: key={key.get(tok, "")!r} count={T.counts[tok]}')
        shown = 0
        for i, seg in enumerate(T.segs):
            for j, t in enumerate(seg):
                if t == tok and shown < 12:
                    l = ''.join(key.get(x, '') for x in seg[max(0, j - 6):j])
                    r = ''.join(key.get(x, '') for x in seg[j + 1:j + 7])
                    print(f'  seg{i:3d}: {l}[{tok}]{r}')
                    shown += 1
        return
    print('KEY (token=letters count):')
    print('  ' + '  '.join(f'{t}={key.get(t, "")}({n})' for t, n in T.counts.most_common()))
    a, b = lines if lines else (0, 12)
    dec = T.decode(key)
    for i in range(a, min(b, len(dec))):
        print(f'seg{i:3d}: {dec[i]}')
    print(f'budget {s.state["spent"]}/{s.state["budget"]}')


def main():
    a = sys.argv[1:]
    cmd = a[0]
    if cmd == 'init':
        b = int(a[a.index('--budget') + 1]) if '--budget' in a else 25
        init(a[1], a[2], b); return
    s = Session(a[1])
    if cmd == 'view':
        tok = a[a.index('--tok') + 1] if '--tok' in a else None
        ln = tuple(int(x) for x in a[a.index('--lines') + 1].split(':')) if '--lines' in a else None
        view(s, tok, ln)
    elif cmd == 'set':
        e = {}
        for x in a[2:]:
            k, v = x.split('=', 1); e[k] = v
        s.set(e); print('ok', e)
    elif cmd == 'score':
        sc = s.score(); print(f'score {sc:.4f} per char   ({s.state["spent"]}/{s.state["budget"]} used)')
    elif cmd == 'status':
        print(s.state['spent'], '/', s.state['budget'], s.state['history'])
    elif cmd == 'grade':
        acc, wrong, ts = s.grade()
        print(f'token-weighted accuracy {acc:.3f}; truth-key score {ts:.4f}; spent {s.state["spent"]}')
        for w in wrong[:25]:
            print('  ', w)


if __name__ == '__main__':
    main()
