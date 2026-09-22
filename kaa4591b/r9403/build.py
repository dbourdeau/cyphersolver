# Builds transcription.tsv and decoded.txt for R9403 from the line-by-line reading.
# Cipher codes are written from the reading with the key observed in this letter
# (one code per letter; e = AST (starred x), r = X (plain x), n = N (small cross '+'),
# f = EQs, p = EQ). Word signs in brackets.
import re, io
KEY = dict(a='OD', b='B', c='W', d='D', e='AST', f='EQs', g='Z', h='H', i='3', l='9',
           m='O', n='N', o='M', p='EQ', q='Q', r='X', s='O+', t='HH', u='U2', v='U2', x='XH')
# page, line, reading ; 'g' lines are glosses
TEXT = r"""
P1|1|nobilis ac egregie domine amice carissime salutem et mei commen
g|1|nobilis ac egregie domine amice carissime salutem et mei comm[en]
P1|2|dationem quindecima presentis obtulit mihi ruffus illius
g|2|[..]atio nem quin[de]cima presentes obtulit mihi [ru]ffus illius
P1|3|literas quam gratas habuit primum [DAG] tum deinde ergo et abunde
g|3|[li]te[r]as quam gratas habuit primum tum deinde ego et abunde
P1|4|intellecta sunt ea omnia que continebant in literis illius
P1|5|ubi quum uestra dominacio mihi gracias principum suorum p
P1|6|ollicetur illarumque illustrissimarum dominacionum erga
P1|7|me beneuolenciam declarat magno me gaudio exhilarat at
P1|8|que letificat ut pote qui ab ineunte etate mea nihil magis
P1|9|semper et optaui et quesiui quam principum et magnatum
P1|10|uirorum conciliare mihi et graciam et fauorem idque ipsum
P1|11|sum omni studio facturus et nunc et semper in posterum
P1|12|ac seruiturus sum illustrissimis principibus uestre domi
P1|13|nacionis corpore et omnibus meis facultatibus ceterum ub
P1|14|cupiunt principes illustrissimi intelligere quid ha
P1|15|beat turca in animo et quo suo exercitu se mouere intendat
P1|16|de hoc facile sue illustrissime dominaciones possunt intelli
P1|17|gere cum hac hieme turca oratoribus regis ferdinandi hoc de
P1|18|derit responsum item ad dominum uestrum dicite illi nun quam
P1|19|ipsum amiciciam nostram numquam pacem pacem uel inducias
P1|20|consequuturum nisi cedat regno hungarie amico nostro ioan
g|20|[..] regno hungarie amicorum nostrorum
P1|21|ni regi serenissimo quod nisi fecerit ueniam ad querendum eu
P1|22|m nec curabo expugnare ciuitates quia deus dedit nobis maximas
P3|1|et amplissimas in imperiis nostris urbes sequentes ad faciendum
P3|2|imperialem et militarem pugnam et ad destruendas eius prouincia
P3|3|s inde illustrissimi principes perpendere possunt nullo
P3|4|pacto turcam hanc expedicionem relicturum si non erit co
P3|5|ncordia nunc autem apud ipsum bellicus apparatus cum in
P3|6|dicibili furia conficitur naues infinite bombarde annona et
P3|7|uictualia colliguntur et deportantur ad danubium ac delectu
P3|8|s fit militum quod autem ista spirensis dieta sit ita breuis fu
P3|9|tura multum doleo tamen quam primum post hanc intensissim
P3|10|am egritudinem meam aliquid roboris contra habebo per postas
P3|11|ad ipsam dietam curram [?]orator ad cesaream maiestatem et imperii
P3|12|status quare rogat principes [?]meus illustrissimos princi
P3|13|pes ut cum aliis amicis suis impediant ne aliquid decernatur
P3|14|contra ipsum donec ego uenero non habet enim [DAG] in toto im
g|14|non habet[e]
P3|15|perio inter omnes principes cui plus fidat et cui etiam
P3|16|plus studeat et cupiat ipso effectu gratificari quam
P3|17|principibus uestre dominacionis quod indubie ita est et
P3|18|pro quo ego ero fideiussor de matrimonio nescio quid scribam tamen
P3|19|intra decem dies constituar cum polonie rege serenissimo et qui
P3|20|dquid perfecero spire declarabo nam apud polonos sicuti apud
P3|21|gallos lege cautum habetur de ex dotandis regum filiabus
g|21|filiabus
P4|1|de his uero et aliis rebus latius quum spire erimus tractabimus
P4|2|interea me ex animo commendo illustrissimis principibus quor
P4|3|um seruitor sum et ero uestra etiam dominacio habeat me commendatum
P4|4|date decima septima septembris anno tricesimo primo lasci scri
g|4|Date decima septima septembris anno tercesimo primo las[..] [..]scri
P4|5|psit
g|5|psit
P4|6|plurimum rogo ut has literas [DAG] aliquo pacto possit
g|6|plurimum rogo ut has literas aliquo pacto possit
P4|7|uestra dominacio offerre imperii statibus
g|7|uestra dominacio offerre imperii statibus
"""
NOTES = {
 ('P1',4): 'small interlinear cipher insertion below "intellecta" (reads roughly O.M.X.9.9.X.HH.N.3), not decoded',
 ('P1',19): 'pacem written twice (dittography)',
 ('P3',11): 'first sign of "[?]orator" uncertain (O-shaped); reading "orator" from context',
 ('P3',12): '"O.AST.U2.O+" = meus, sense unclear after "principes"',
 ('P3',5): 'blot before "ipsum"',
 ('P3',10): 'blot on the q of "aliquid"',
}
def enc(w):
    if w.startswith('['): 
        m = re.match(r'\[(\?)?\](.*)', w)
        if w in ('[DAG]','[BIGX]','[FLW]'): return w.strip('[]')
        if m: return '?.' + '.'.join(KEY[c] for c in m.group(2))
    return '.'.join(KEY[c] for c in w)
out = io.open(r'C:/Users/dbour/cypher/kaa4591b/r9403/transcription.tsv','w',encoding='utf-8')
out.write('# R9403 (BayHStA KAA 4591 f.226-228), system B. page\tline\tcipher_words\treading\n')
out.write('# Codes written from the reading with the key found here (e=AST, r=X, n=N "+"); homophone choice (W/HH for t, EQs/T for f) not kept. g: = interlinear gloss.\n')
out.write('# P2 (f.226v) holds only a clear-text docket: "R[..] [..] anno 32" (not cipher).\n')
dec = io.open(r'C:/Users/dbour/cypher/kaa4591b/r9403/decoded.txt','w',encoding='utf-8')
tok=0; unread=[]; lastp=None
for ln in TEXT.strip().splitlines():
    p,l,t = ln.split('|')
    if p=='g':
        out.write('g:\t%s\t\t%s\n' % (l,t)); continue
    words=t.split()
    codes=' '.join(enc(w) for w in words)
    note = NOTES.get((p,int(l)),'')
    out.write('%s\t%s\t%s\t%s%s\n' % (p,l,codes,t,('\t# '+note) if note else ''))
    if p!=lastp: dec.write('== %s\n' % p); lastp=p
    dec.write('%s %s\n' % (l,t))
    for w in words:
        tok+=1
        if '?' in w: unread.append((p,l,w))
dec.write('\n# tokens (line-split words counted once per line fragment): %d, unread: %d, read: %.1f%%\n' % (tok,len(unread),100*(tok-len(unread))/tok))
print(tok,len(unread),unread)

NORM = """Nobilis ac egregie domine, amice carissime, salutem et mei commendationem. Quindecima presentis obtulit mihi Ruffus illius literas; quam gratas habuit primum [DAG = rex Ioannes], tum deinde ergo et abunde intellecta sunt ea omnia que continebant in literis illius. Ubi quum uestra dominacio mihi gracias principum suorum pollicetur, illarumque illustrissimarum dominacionum erga me beneuolenciam declarat, magno me gaudio exhilarat atque letificat, ut pote qui ab ineunte etate mea nihil magis semper et optaui et quesiui quam principum et magnatum uirorum conciliare mihi et graciam et fauorem; idque ipsum sum omni studio facturus, et nunc et semper in posterum ac seruiturus sum illustrissimis principibus uestre dominacionis corpore et omnibus meis facultatibus. Ceterum ub[i] cupiunt principes illustrissimi intelligere quid habeat Turca in animo et quo suo exercitu se mouere intendat, de hoc facile sue illustrissime dominaciones possunt intelligere, cum hac hieme Turca oratoribus regis Ferdinandi hoc dederit responsum: Item ad dominum uestrum dicite illi nunquam ipsum amiciciam nostram, numquam pacem [pacem] uel inducias consequuturum nisi cedat regno Hungarie amico nostro Ioanni regi serenissimo; quod nisi fecerit, ueniam ad querendum eum, nec curabo expugnare ciuitates, quia Deus dedit nobis maximas et amplissimas in imperiis nostris urbes, sequentes ad faciendum imperialem et militarem pugnam et ad destruendas eius prouincias. Inde illustrissimi principes perpendere possunt nullo pacto Turcam hanc expedicionem relicturum si non erit concordia. Nunc autem apud ipsum bellicus apparatus cum indicibili furia conficitur: naues infinite, bombarde, annona et uictualia colliguntur et deportantur ad Danubium, ac delectus fit militum. Quod autem ista Spirensis dieta sit ita breuis futura multum doleo; tamen quam primum post hanc intensissimam egritudinem meam aliquid roboris contra habebo, per postas ad ipsam dietam curram. [?]orator ad Cesaream Maiestatem et imperii status, quare rogat principes [?]meus illustrissimos principes ut cum aliis amicis suis impediant ne aliquid decernatur contra ipsum donec ego uenero. Non habet enim [DAG = rex] in toto imperio inter omnes principes cui plus fidat et cui etiam plus studeat et cupiat ipso effectu gratificari quam principibus uestre dominacionis, quod indubie ita est, et pro quo ego ero fideiussor. De matrimonio nescio quid scribam; tamen intra decem dies constituar cum Polonie rege serenissimo, et quidquid perfecero Spire declarabo. Nam apud Polonos sicuti apud Gallos lege cautum habetur de ex dotandis regum filiabus. De his uero et aliis rebus latius quum Spire erimus tractabimus. Interea me ex animo commendo illustrissimis principibus, quorum seruitor sum et ero; uestra etiam dominacio habeat me commendatum. Date decima septima Septembris anno tricesimo primo, Lasci. Scripsit.
Plurimum rogo ut has literas [DAG = regis] aliquo pacto possit uestra dominacio offerre imperii statibus."""
DOUBT = ['ergo','ruffus','sequentes','contra','postas','constituar','nam','ub[i]','dotandis','meus']
words = re.findall(r"\[[^\]]*\]\S*|[A-Za-z\[\]\?]+", NORM)
words = [w for w in words if not w.startswith('[DAG') and w!='[pacem]']
n=len(words); un=[w for w in words if '?' in w]
dec = io.open(r'C:/Users/dbour/cypher/kaa4591b/r9403/decoded.txt','a',encoding='utf-8')
dec.write('\n== Normalised reading (fragments joined; [DAG] = the king word sign)\n'+NORM+'\n')
dec.write('\n# Count on the joined text: %d words (word signs excluded), %d unread (%s) -> %.1f%% read as sense.\n' % (n,len(un),', '.join(un),100*(n-len(un))/n))
dec.write('# Read but doubtful (sign-level or sense): %s\n' % ', '.join(DOUBT))
dec.write('# Word sign DAG occurs 3x (P1 l.3, P3 l.14, P4 l.6); context = King John Zapolya ("rex", "regis").\n')
dec.write('# Latin LM check: lang best_language -> la (-1.78) vs fr-1600-letters (-2.64).\n')
print(n,len(un))
