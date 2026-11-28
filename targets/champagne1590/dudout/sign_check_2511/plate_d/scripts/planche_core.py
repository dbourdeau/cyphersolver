# ---- noyau commun : construit planche.html (images en base64), crops/, cle-PRIVEE.json
# v2 (11/11/2026, consigne Brice) : ordre des options ÉQUILIBRÉ. Avant, chaque question mélangeait ses options
# indépendamment : sur Coloma FS1, les 6 cibles sont tombées en « forme 3 » (p ≈ 0,14 %), et sur Catinat lot 4 les deux
# contrôles étaient à la même place. Désormais la forme de référence (attendu du contrôle, sinon q['reference'],
# sinon la 1re option) est répartie à parts égales entre les places, les contrôles sont à des places différentes,
# et build() REFUSE de produire une planche déséquilibrée. Un exemple peut porter une 4e valeur « hauteur »
# (bas / moyen / haut) : des hauteurs mélangées dans une même forme sont signalées (remarque de Brice, Treviglio v3).
# Copie canonique : PLANCHES/_outils/planche_core.py (tests : test_planche_core.py). Les copies des anciens dossiers
# restent telles quelles (elles sont hachées avec leurs planches).
import os, io, json, base64, random, datetime
from PIL import Image, ImageOps, ImageDraw
RED = (215, 0, 0)
_cache = {}
def _img(path):
    if path not in _cache: _cache[path] = Image.open(path).convert('L')
    return _cache[path]
def _prep(im): return ImageOps.autocontrast(im, cutoff=1).convert('RGB')
def _boxed(path, crop, box, scale, width=3):
    I = _img(path); x0, y0, x1, y1 = [int(v) for v in crop]
    x0, y0 = max(0, x0), max(0, y0); x1, y1 = min(I.width, x1), min(I.height, y1)
    c = _prep(I.crop((x0, y0, x1, y1))); c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
    if box:
        b = [(box[0] - x0 - 2) * scale, (box[1] - y0 - 2) * scale, (box[2] - x0 + 2) * scale, (box[3] - y0 + 2) * scale]
        ImageDraw.Draw(c).rectangle(b, outline=RED, width=width)
    return c
def _b64(im):
    b = io.BytesIO(); im.save(b, 'JPEG', quality=88); return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
def _reference(q):
    return q.get('attendu') or q.get('reference') or q['options'][0][0]
def ordonner_options(QUESTIONS, rng):
    """Retourne, pour chaque question (même ordre que QUESTIONS), ses options réordonnées.
    La référence est placée à la place la moins utilisée jusque-là parmi les questions ayant le même nombre
    d'options (tirage au sort entre ex aequo) ; un contrôle évite les places déjà prises par les contrôles précédents."""
    ordres = [None] * len(QUESTIONS); comptes = {}; places_controles = set()
    visite = list(range(len(QUESTIONS))); rng.shuffle(visite)
    visite.sort(key=lambda i: not QUESTIONS[i].get('controle'))  # contrôles d'abord : places distinctes sans casser l'équilibre
    for i in visite:
        q = QUESTIONS[i]; opts = q['options'][:]; k = len(opts); ref = _reference(q)
        ir = next((j for j, op in enumerate(opts) if op[0] == ref), 0)
        c = comptes.setdefault(k, [0] * k); cand = list(range(k))
        if q.get('controle'):
            libres = [p for p in cand if p not in places_controles]
            cand = libres or cand
        m = min(c[p] for p in cand); cand = [p for p in cand if c[p] == m]
        place = rng.choice(cand); c[place] += 1
        if q.get('controle'): places_controles.add(place)
        autres = opts[:ir] + opts[ir + 1:]; rng.shuffle(autres)
        autres.insert(place, opts[ir]); ordres[i] = autres
    return ordres
def verifier_equilibre(QUESTIONS, ordres):
    """Contrôle indépendant de l'ordre produit : répartition des références et des contrôles, hauteurs d'exemples."""
    import math
    par_k = {}; ctrl = []; incoh = []
    for q, ordre in zip(QUESTIONS, ordres):
        ref = _reference(q); pos = [op[0] for op in ordre].index(ref); k = len(ordre)
        par_k.setdefault(k, []).append(pos)
        if q.get('controle'): ctrl.append(pos)
        for fkey, _lect, exs in q['options']:
            h = {ex[3] for ex in exs if len(ex) > 3 and ex[3]}
            if len(h) > 1: incoh.append((q['code'], fkey))
    pb = []
    for k, L in par_k.items():
        plafond = math.ceil(len(L) / k) + 1
        for p in range(k):
            if L.count(p) > plafond: pb.append('k=%d : place %d prise %d fois sur %d (plafond %d)' % (k, p + 1, L.count(p), len(L), plafond))
    if len(ctrl) >= 2 and len(set(ctrl)) == 1: pb.append('tous les contrôles à la même place (%d)' % (ctrl[0] + 1))
    return {'ok': not pb, 'problemes': pb, 'places_references': {k: [p + 1 for p in L] for k, L in par_k.items()},
            'places_controles': [p + 1 for p in ctrl], 'hauteurs_incoherentes': incoh}
def build(HERE, IMG, QUESTIONS, PLANCHE, TITRE, SEED_Q, SEED_O, CLAMP, SOURCE_NOTE, HALF=230, VPAD=30):
    os.makedirs(os.path.join(HERE, 'crops'), exist_ok=True)
    rq = random.Random(SEED_Q); ro = random.Random(SEED_O)
    order = list(range(len(QUESTIONS))); rq.shuffle(order)
    key = {'_note': 'CORRESPONDANCE PRIVÉE — ne jamais charger dans la page ni montrer avant l’export des réponses. Images privées : usage local seulement.',
           'planche': PLANCHE, 'source': SOURCE_NOTE, 'graine_ordre_questions': SEED_Q, 'graine_ordre_options': SEED_O,
           'construit_le': datetime.date.today().isoformat(), 'questions': {}}
    ordres = ordonner_options(QUESTIONS, ro); eq = verifier_equilibre(QUESTIONS, ordres)
    if not eq['ok']: raise SystemExit('REFUS : planche déséquilibrée : ' + ' ; '.join(eq['problemes']))
    if eq['hauteurs_incoherentes']: raise SystemExit('REFUS : exemples de hauteurs mélangées dans une même forme : %s' % eq['hauteurs_incoherentes'])
    key['equilibre_positions'] = {'version_core': 2, 'places_references': eq['places_references'], 'places_controles': eq['places_controles']}
    items = []; contact = []
    for n, qi in enumerate(order, 1):
        q = QUESTIONS[qi]; qid = 'q%02d' % n; page, box = q['cible']; path = IMG[page]; lo, hi = CLAMP[page]
        cx = (box[0] + box[2]) / 2; sx0 = max(lo, cx - HALF); sx1 = min(hi, cx + HALF)
        strip = _boxed(path, (sx0, box[1] - VPAD, sx1, box[3] + VPAD), box, min(2.2, 1000 / (sx1 - sx0)), 3)
        sign = _boxed(path, (box[0] - 14, box[1] - 10, box[2] + 14, box[3] + 10), box, 4.0 if (box[3] - box[1]) < 70 else 3.0, 3)
        strip.save(os.path.join(HERE, 'crops', '%s_ligne.jpg' % qid), quality=90); sign.save(os.path.join(HERE, 'crops', '%s_signe.jpg' % qid), quality=90)
        opts = ordres[qi]
        key['questions'][qid] = {'code': q['code'], 'lieu': q['lieu'], 'image': os.path.basename(path), 'boite_signe': box,
                                 'question_fable': q.get('question', ''), 'controle': q.get('controle', False),
                                 'reponse_attendue_controle': None, 'formes': {}}
        ohtml = []; ovig = []
        for k, (fkey, lecture, exs) in enumerate(opts, 1):
            lab = 'forme %d' % k; vigs = []
            for j, ex in enumerate(exs, 1):
                p2, b2, src = ex[:3]
                v = _boxed(IMG[p2], (b2[0] - 16, b2[1] - 12, b2[2] + 16, b2[3] + 12), b2, 3.0 if (b2[3] - b2[1]) < 70 else 2.4, 3)
                v.save(os.path.join(HERE, 'crops', '%s_forme%d_%d.jpg' % (qid, k, j)), quality=90); vigs.append(v)
            key['questions'][qid]['formes'][lab] = {'forme': fkey, 'lecture': lecture, 'exemples': [{'image': os.path.basename(IMG[ex[0]]), 'boite': ex[1], 'lieu': ex[2], 'hauteur': (ex[3] if len(ex) > 3 else None)} for ex in exs]}
            if q.get('controle') and fkey == q['attendu']: key['questions'][qid]['reponse_attendue_controle'] = lab
            ohtml.append('<label class="opt"><input type="radio" name="%s" value="%s"><span class="lab">%s</span><span class="v">%s</span></label>'
                         % (qid, lab, lab, ''.join('<img src="%s" alt="%s, exemple %d">' % (_b64(v), lab, j) for j, v in enumerate(vigs, 1))))
            ovig += vigs
        for t in ('aucune / autre forme', 'illisible', 'pas un signe (tache, trait)'):
            ohtml.append('<label class="opt txt"><input type="radio" name="%s" value="%s"><span class="lab">%s</span></label>' % (qid, t, t))
        items.append('''<section class="q" id="%s"><h2>Question %d / %d</h2>
<p class="mut">La ligne (le signe à examiner est encadré en rouge) :</p><img class="ctx" src="%s" alt="ligne, signe encadré">
<p class="mut">Le même signe, agrandi :</p><img class="big" src="%s" alt="signe agrandi">
<p class="mut">Quelle forme lui ressemble le plus&nbsp;? (exemples pris ailleurs dans la même écriture)</p>
<div class="opts">%s</div>
<input class="rem" type="text" data-q="%s" placeholder="remarque (facultatif)">
</section>''' % (qid, n, len(order), _b64(strip), _b64(sign), ''.join(ohtml), qid))
        # planche-contact de vérification (locale)
        row = [strip, sign] + ovig; W = sum(r.width + 8 for r in row); H = max(r.height for r in row) + 18
        R = Image.new('RGB', (W, H), (230, 230, 230)); ImageDraw.Draw(R).text((3, 2), '%s %s' % (qid, q['code']), fill=(0, 0, 0)); x = 0
        for r in row: R.paste(r, (x, 16)); x += r.width + 8
        contact.append(R)
    json.dump(key, open(os.path.join(HERE, 'cle-PRIVEE.json'), 'w'), ensure_ascii=False, indent=1)
    tpl = TEMPLATE.replace('{{TITRE}}', TITRE).replace('{{N}}', str(len(order))).replace('{{PLANCHE}}', PLANCHE)
    tpl = tpl.replace('{{IDS}}', json.dumps(['q%02d' % i for i in range(1, len(order) + 1)])).replace('{{ITEMS}}', '\n'.join(items))
    open(os.path.join(HERE, 'planche.html'), 'w').write(tpl)
    Wc = min(2400, max(r.width for r in contact)); S = Image.new('RGB', (Wc, sum(r.height for r in contact)), 'white'); y = 0
    for r in contact: S.paste(r, (0, y)); y += r.height
    S.save(os.path.join(HERE, 'crops', '_contact.jpg'), quality=70)
    return len(order)
TEMPLATE = r'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITRE}}</title>
<style>
:root{--bg:#f6f4ef;--fg:#1d1d1d;--mut:#555;--card:#fff;--line:#d8d4cb;--acc:#1d6b2f;--btn:#222}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#1b1b1d;--fg:#eee;--mut:#aaa;--card:#26262a;--line:#444;--acc:#58c26f;--btn:#444}}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.45 system-ui,-apple-system,sans-serif}
header{position:sticky;top:0;z-index:5;background:var(--card);border-bottom:1px solid var(--line);padding:8px 16px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}
header h1{font-size:17px;margin:0 12px 0 0}
button{font:inherit;padding:6px 14px;border:1px solid #444;border-radius:6px;background:var(--btn);color:#fff;cursor:pointer}
#msg{font-weight:600;color:var(--acc)} .mut{color:var(--mut);font-size:14px;margin:6px 0 4px}
main{max-width:1100px;margin:0 auto;padding:12px 16px 60px}
.intro,.q{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 14px;margin:14px 0}
.q.done{border-color:var(--acc)} .q h2{font-size:16px;margin:0 0 4px}
img{display:block;max-width:100%;height:auto;background:#fff;border-radius:3px}
.big{max-height:220px;width:auto}
.opts{display:flex;flex-wrap:wrap;gap:12px;margin:10px 0 8px;align-items:stretch}
.opt{display:flex;flex-direction:column;gap:6px;border:2px solid var(--line);border-radius:8px;padding:8px;cursor:pointer;background:var(--card)}
.opt .v{display:flex;gap:8px;flex-wrap:wrap} .opt .v img{max-height:190px;width:auto}
.opt.sel{border-color:var(--acc);box-shadow:0 0 0 2px var(--acc) inset}
.opt.txt{justify-content:center;min-height:50px}
.rem,#generale{width:100%;box-sizing:border-box;padding:6px;font:inherit;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--fg)}
#secours{width:100%;height:70px;font:12px monospace;display:none;margin-top:6px}
</style></head><body>
<header><h1>{{TITRE}}</h1><button id="exp" type="button">Exporter les réponses</button><span id="count"></span><span id="msg" role="status"></span>
<textarea id="secours" readonly aria-label="copie de secours des réponses"></textarea></header>
<main>
<div class="intro"><p>{{N}} questions. Pour chacune : une bande de la ligne, le signe à examiner encadré en rouge, puis le même signe agrandi.
Choisissez la <b>forme</b> qui lui ressemble le plus ; chaque forme est montrée par un ou deux exemples découpés ailleurs dans la même écriture (l’exemple est encadré en rouge).
Si aucune ne convient : « aucune / autre forme » ; si le signe ne se lit pas : « illisible » ; si ce n’est pas un signe : « pas un signe ». Une remarque peut préciser.
Les réponses restent dans ce navigateur ; « Exporter » télécharge <code>reponses-{{PLANCHE}}.json</code> et le copie dans le presse-papiers.</p></div>
{{ITEMS}}
<div class="intro"><p class="mut">Remarque générale (facultatif) :</p><textarea id="generale" rows="3"></textarea></div>
</main>
<script>
(function(){
var IDS={{IDS}}, KEY='{{PLANCHE}}', FILE='reponses-{{PLANCHE}}.json', st={};
try{st=JSON.parse(localStorage.getItem(KEY)||'{}')||{};}catch(e){st={};}
function save(){try{localStorage.setItem(KEY,JSON.stringify(st));}catch(e){}}
function paint(id){var sec=document.getElementById(id),v=(st[id]||{}).choix;
  sec.querySelectorAll('.opt').forEach(function(l){var i=l.querySelector('input');i.checked=(i.value===v);l.classList.toggle('sel',i.value===v);});
  sec.classList.toggle('done',!!v);}
function count(){var n=IDS.filter(function(i){return st[i]&&st[i].choix;}).length;document.getElementById('count').textContent=n+'/'+IDS.length+' répondues';}
IDS.forEach(function(id){var sec=document.getElementById(id);
  sec.querySelectorAll('input[type=radio]').forEach(function(r){r.addEventListener('change',function(){st[id]=st[id]||{};st[id].choix=r.value;save();paint(id);count();});});
  var rem=sec.querySelector('.rem'); if(st[id]&&st[id].remarque) rem.value=st[id].remarque;
  rem.addEventListener('input',function(){st[id]=st[id]||{};st[id].remarque=rem.value;save();}); paint(id);});
var g=document.getElementById('generale'); if(st._generale) g.value=st._generale; g.addEventListener('input',function(){st._generale=g.value;save();});
count();
function payload(){var r={};IDS.forEach(function(id){r[id]={choix:(st[id]||{}).choix||null,remarque:(st[id]||{}).remarque||''};});
  return JSON.stringify({planche:KEY,date:new Date().toISOString(),reponses:r,remarque_generale:st._generale||''},null,1);}
document.getElementById('exp').addEventListener('click',function(){
  var txt=payload(),msg=document.getElementById('msg'),sec=document.getElementById('secours'),parts=[];
  sec.value=txt; sec.style.display='block';
  try{var b=new Blob([txt],{type:'application/json'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=FILE;document.body.appendChild(a);a.click();a.remove();parts.push('fichier téléchargé');}catch(e){}
  var done=function(ok){if(ok)parts.push('copié dans le presse-papiers');msg.textContent=(parts.length?parts.join(' + '):'copiez le texte ci-dessous')+'.';};
  try{if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(function(){done(true);},function(){sec.select();try{done(document.execCommand('copy'));}catch(e){done(false);}});}
      else{sec.select();try{done(document.execCommand('copy'));}catch(e){done(false);}}}catch(e){done(false);}
});
})();
</script>
</body></html>'''
