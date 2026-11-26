"""check_lecture_o5.py (PREREG-O5 §7-8, 25/11/2026) - contrôle de forme et décompte d'une lecture par le sens.

usage : python3 -I check_lecture_o5.py DECODE-O5.txt LECTURE.txt [JUSTIFICATIONS.tsv] [--modele] [--json SORTIE.json]
  sans --json : contrôle de forme seulement (« FORME OK » ou la liste des erreurs) ;
  --modele    : imprime les identifiants J001... des mots non sûrs à justifier (modèle de JUSTIFICATIONS.tsv) ;
  --json      : écrit le décompte (mots S/P/R/I, nulles, vecteur de classes par caractère) pour verdict_o5.py.

Format de LECTURE.txt (voir BRIEF-LECTURE-O5.md) : lignes '#' = commentaires ; le reste est un texte continu, en
minuscules, qui reprend TOUTES les lettres du décodage dans l'ordre, sans en changer ni en omettre une.
  mot          sûr          : lettres du décodage seules, aucune lettre ajoutée, aucun ?
  {mot}        probable     : lettres du décodage ; au plus UNE lettre donnée par le sens (en MAJUSCULE) par mot, et au
                              moins 2 lettres du décodage dans ce mot
  [mot]        restitué     : contient des lettres données par le sens (MAJUSCULES) au-delà de la règle du probable,
                              ou un mot entier ajouté ; une majuscule remplit un ? du décodage ou s'insère entre deux
                              lettres ; elle ne remplace JAMAIS une lettre du décodage
  ‹lettres›    irrésolu     : lettres du décodage telles quelles (? permis), aucune majuscule ; compte 1 mot,
                              ou n mots avec ‹lettres|n›
  (xy)         nulle        : 1 à 3 caractères du décodage (? permis) jugés sans valeur (nulle, lettre doublée) ; pas un mot
  §6v-L01      repère       : facultatif ; vérifie que la ligne 6v L01 du décodage commence bien à cet endroit
Une marque { } [ ] ‹ › ( ) enserre des mots entiers ; à l'intérieur, l'espace, l'apostrophe et le trait d'union séparent
les mots (« {l'on} » = 2 mots probables). Pas d'accents, pas de ponctuation autre que ' et -.
Règles de décompte (PREREG-O5 §8) : lus = S + P + R ; total = S + P + R + I ; une nulle collée à un mot qui contient une
lettre donnée par le sens fait compter ce mot comme irrésolu (remplacement déguisé) ; si les caractères marqués nuls
dépassent 5 % des caractères du décodage, chaque nulle compte en plus comme 1 mot irrésolu."""
import sys, re, json
OPEN = {'{': ('}', 'P'), '[': (']', 'R'), '‹': ('›', 'I'), '(': (')', 'N')}
SEP = re.compile(r"[\s'’-]+")
def load_decode(p):
    rows = []
    for l in open(p, encoding='utf-8'):
        m = re.match(r'^(\d[rv] L\d\d): ([a-z?]*)$', l.rstrip('\n'))
        if m: rows.append((m.group(1), m.group(2)))
    return rows
def tokens(text):
    return re.findall(r'§\S+|\{[^}]*\}|\[[^\]]*\]|‹[^›]*›|\([^)]*\)|\S+', text)
def analyse(D, starts, text):
    err = []; toks = []; p = 0
    for raw in tokens(text):
        if raw.startswith('§'):
            m = re.match(r'^§(\d[rv])-(L\d\d)$', raw)
            if not m: err.append('repère mal formé : %s' % raw); continue
            k = '%s %s' % (m.group(1), m.group(2))
            if k not in starts: err.append('repère inconnu : %s' % raw)
            elif starts[k] != p: err.append('repère %s placé au caractère %d du décodage, la ligne commence au caractère %d' % (raw, p, starts[k]))
            continue
        cls, body, n_est = 'S', raw, None
        if raw[0] in OPEN:
            close, cls = OPEN[raw[0]]
            if raw[-1] != close or len(raw) < 3: err.append('marque mal fermée : %s' % raw); continue
            body = raw[1:-1]
            if cls == 'I' and '|' in body:
                body, _, n = body.rpartition('|')
                if not n.isdigit() or int(n) < 1: err.append('taille de trou invalide : %s' % raw); continue
                n_est = int(n)
        if re.search(r'[{}\[\]‹›()§|]', body): err.append('marque à l\'intérieur d\'un mot ou marques imbriquées : %s (une marque enserre des mots entiers)' % raw); continue
        if re.search(r"[^a-zA-Z?\s'’-]", body): err.append('caractère interdit (accent, ponctuation, chiffre) : %s' % raw); continue
        words = [w for w in SEP.split(body) if w]
        if not words: err.append('mot vide : %s' % raw); continue
        tok = dict(raw=raw, cls=cls, words=[], pos=[]); start_tok = p
        for w in words:
            ws = p; nsense = ndec = 0
            for c in w:
                if c == '?':
                    if cls not in 'IN': err.append('? laissé dans un mot %s : %s (remplir par une MAJUSCULE dans {} ou [], ou mettre en ‹›)' % ({'S': 'sûr', 'P': 'probable', 'R': 'restitué'}[cls], raw))
                    if p >= len(D) or D[p] != '?': err.append('? de la lecture ne correspond pas à un ? du décodage (caractère %d) : %s' % (p, raw)); return err, toks, p
                    tok['pos'].append(p); p += 1; ndec += 1
                elif c.islower():
                    if p >= len(D): err.append('lettre au-delà de la fin du décodage : %s' % raw); return err, toks, p
                    if D[p] == '?': err.append('le ? du décodage au caractère %d est rempli par une minuscule dans %s : une lettre donnée par le sens s\'écrit en MAJUSCULE' % (p, raw)); return err, toks, p
                    if D[p] != c: err.append('la lecture contredit ou saute une lettre du décodage au caractère %d (décodage « %s », lecture « %s ») dans %s' % (p, D[p], c, raw)); return err, toks, p
                    tok['pos'].append(p); p += 1; ndec += 1
                else:  # majuscule = lettre donnée par le sens
                    if cls in 'SIN': err.append('lettre donnée par le sens (majuscule) dans un mot %s : %s' % ({'S': 'sûr', 'I': 'irrésolu', 'N': 'nul'}[cls], raw))
                    nsense += 1
                    if p < len(D) and D[p] == '?': tok['pos'].append(p); p += 1
            if cls == 'P' and (nsense > 1 or ndec < 2): err.append('mot probable avec %d lettre(s) donnée(s) par le sens et %d lettre(s) du décodage : %s (au-delà : [restitué])' % (nsense, ndec, raw))
            tok['words'].append(dict(w=w, start=ws, end=p, sense=nsense, dec=ndec))
        if cls == 'N' and (len(words) != 1 or not 1 <= len(words[0]) <= 3): err.append('nulle de 1 à 3 caractères, un seul groupe : %s' % raw)
        tok['n_est'] = n_est; tok['start'] = start_tok; tok['end'] = p; toks.append(tok)
    if p != len(D): err.append('la lecture s\'arrête au caractère %d sur %d : toutes les lettres du décodage doivent être reprises' % (p, len(D)))
    return err, toks, p
def score(D, toks):
    N = len(D); classes = ['-'] * N; warn = []
    for i, t in enumerate(toks):
        t['eff'] = t['cls']
    for i, t in enumerate(toks):
        if t['cls'] != 'N': continue
        for j in (i - 1, i + 1):
            if 0 <= j < len(toks) and toks[j]['cls'] in 'PR' and any(w['sense'] for w in toks[j]['words']):
                toks[j]['eff'] = 'I'; warn.append('nulle %s collée à %s : ce mot compte comme irrésolu' % (t['raw'], toks[j]['raw']))
    cnt = dict(S=0, P=0, R=0, I=0); null_chars = 0; nnull = 0
    for t in toks:
        for q in t['pos']: classes[q] = t['eff']
        if t['cls'] == 'N': null_chars += len(t['pos']); nnull += 1; continue
        if t['eff'] == 'I' and t['cls'] == 'I' and t['n_est']: cnt['I'] += t['n_est']
        else: cnt[t['eff']] += len(t['words'])
    over = N and null_chars / N > 0.05
    if over: cnt['I'] += nnull; warn.append('nulles %d caractères > 5 %% du décodage : %d mots irrésolus ajoutés' % (null_chars, nnull))
    tot = sum(cnt.values()); lus = cnt['S'] + cnt['P'] + cnt['R']
    spans = [[w['start'], w['end'], w['w'], t['eff']] for t in toks if t['cls'] != 'N' for w in t['words']]
    upp = sum(sum(1 for c in w['w'] if c.isupper()) for t in toks for w in t['words'])
    return dict(decode_chars=N, decode_unknown=D.count('?'), words=cnt, words_total=tot, words_read=lus,
                share_read=round(lus / tot, 4) if tot else 0.0, share_restored=round(cnt['R'] / tot, 4) if tot else 0.0,
                share_probable=round(cnt['P'] / tot, 4) if tot else 0.0, null_tokens=nnull, null_chars=null_chars,
                null_share=round(null_chars / N, 4) if N else 0.0, null_cap_exceeded=bool(over), sense_letters=upp,
                classes=''.join(classes), spans=spans, warnings=warn)
def justif(path, toks):
    need = [t for t in toks if t['cls'] != 'S']; err = []; got = {}
    for l in open(path, encoding='utf-8'):
        if not l.strip() or l.startswith('#'): continue
        f = l.rstrip('\n').split('\t')
        if len(f) < 3: err.append('justification mal formée (id<TAB>mot<TAB>justification) : %s' % l.strip()); continue
        got[f[0]] = (f[1], f[2])
    for i, t in enumerate(need, 1):
        j = 'J%03d' % i
        if j not in got: err.append('%s %s : justification manquante' % (j, t['raw']))
        elif got[j][0] != t['raw']: err.append('%s : le mot de la fiche « %s » n\'est pas « %s »' % (j, got[j][0], t['raw']))
        elif len(got[j][1].strip()) < 10: err.append('%s %s : justification trop courte' % (j, t['raw']))
    extra = set(got) - {'J%03d' % i for i in range(1, len(need) + 1)}
    if extra: err.append('identifiants en trop : %s' % ' '.join(sorted(extra)))
    return err, need
def main():
    a = sys.argv[1:]; js = None
    if '--json' in a: i = a.index('--json'); js = a[i + 1]; del a[i:i + 2]
    modele = '--modele' in a; a = [x for x in a if x != '--modele']
    rows = load_decode(a[0]); D = ''.join(s for _, s in rows); starts = {}; q = 0
    for k, s in rows: starts[k] = q; q += len(s)
    text = '\n'.join(l for l in open(a[1], encoding='utf-8').read().split('\n') if not l.startswith('#'))
    err, toks, _ = analyse(D, starts, text)
    if modele and not err:
        for i, t in enumerate([t for t in toks if t['cls'] != 'S'], 1): print('J%03d\t%s\t' % (i, t['raw']))
        return
    if not err and len(a) > 2: err += justif(a[2], toks)[0]
    elif not err: err.append('fiche de justifications non fournie')
    if err:
        print('ERREURS DE FORME (%d) :' % len(err)); [print(' -', e) for e in err[:60]]; sys.exit(1)
    print('FORME OK')
    if js:
        r = score(D, toks); json.dump(r, open(js, 'w', encoding='utf-8'), ensure_ascii=False)
        print(json.dumps({k: v for k, v in r.items() if k not in ('classes', 'spans')}, ensure_ascii=False))
if __name__ == '__main__': main()
