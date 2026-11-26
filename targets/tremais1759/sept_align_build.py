# -*- coding: utf-8 -*-
"""Build sept_cipher_aligned.tsv and sept_key_from_pair.tsv from the hand-entered readings below.
Item syntax:  '#word'            sets the current plaintext word (evidence only)
              '"clear words"'    a clear-text slot (optionally |note)
              'token=plain'      a cipher slot; optional '|l' or '|m' or '|h' and '|note'
              @x                 shorthand for the usual stacked pair of letter x
"""
import re, collections, io, os
OUT = r'C:\Users\dbour\cypher\targets\tremais1759'
ST = {'p': '497/119', 'l': '362/279', 'a': '80/165', 's': '219/466', 't': '227/274', 'r': '108/229',
      'n': '427/149', 'e': '263/429', 'd': '176/169', 'm': '55/188', 'f': '270/117', 'y': '348/259',
      'o': '669/276', 'b': '492/138', 'c': '231/389'}
SI = '433=si|m|si group reads 4 + two identical hooked digits: 433 best, 499 or 477 possible'
I_ = '236=i'
TA = '315-437=ta'
D = [
('342r', '1-7', ['"J\'ai eu l\'honneur de vous informer ... sur les parties"|opening clear lines, not itemised; one struck passage at the start of line 8']),
('342r', 8, ['"qui m\'ont été confiées. Les"', '#autres', '89=au', '@t', '@r', '@e||at the line end, top number partly lost']),
('342r', 9, ['@s', '"[struck]"|a struck-out group', '#moyens', '210=moyens', '"d\'"', '#avoir', '311=avoir', '#des', '12-437=de', '@s', '#preuves', '@p', '@r', '@e', '137=u', '322=v', '@e', '@s||squeezed into the margin']),
('342r', 10, ['#juridiques', '34=ju', '74=ri', '110=di', '349-207=que||plural s not written', '"m\'ont"', '#manqué', '45=manqué', '"également. Je vous avouerai même, Monseigneur,"']),
('342r', 11, ['"que je ne prévois pas que"', '#quelques', '663=quelque||plural s not written', '#recherches', '298=re', '271=ch', '132=er', '271=ch', '339=es', '#que', '349-207=que', '#je', '131=je', '"puisse"']),
('342r', 12, ['#faire', '32=faire', '#je', '131=je', '#parvienne', '172=par', '360=vi', '126=en', '18=ne', '"à"', '#vous', '46-368=vous', '#en', '126=en', '"procurer. Les"', '#affaires', '491=affaire', '@s', '#frauduleuses', '@f', '@r']),
('342r', 13, ['89=au', '140-157=du', '15-287=le', '"[struck]"|heavy blot over a struck group', '137=u', '@s', '339=es', '#se', '101=se', '#traitent', '154=traite|l|15[46]; value by position', '248-197=nt||the same pair ends traitent, Intendant, traitant and argent: nt, or ent/ant', '"ordinairement"', '#sans', '260=sans', '#écriture', '336=éc|m|or 326', '74=ri', '176=tu|l|[12]7[46]; fortune has 274 for tu', '292=re|l|or 298']),
('342r', 14, ['"et il est naturel de croire que s\'il y en avoit eu icy; Les"', '#gens', '13=ge', '126=en', '@s', '#qui', '89-455=qui|m|first number squeezed at the edge: [38]9']),
('342r', 15, ['#en', '196=en', '"sont"', '#dépositaires', '12-437=dé', '54=po', SI, TA, I_, '298=re', '@s', '"ne seroient nullement disposés"']),
('342r', 16, ['#à', '@a', '#les', '15-287=le', '@s', '"[struck]"|a struck group', '#montrer', '440=mon', '@t', '132=er||the r of -trer not written separately', '"je me vois donc obligé de m\'arrêter"']),
('342r', 17, ['#aux', '306=aux', '#discours', '110=di', '@s', '410=co', '137=u', '@r', '@s', '"[struck: j\'en]"|struck clear words', '#généraux', '13=gé', '18=né', '20=ra', '137=u', '142=x', '"j\'en ai beaucoup"']),
('342r', 18, ['#recueillis', '298=re', '363=cu', '@e', I_, '@l', '120=li||plural s not written; 1[27]0', '#de', '12-437=de', '"gens qui m\'ont paru"', '#dignes', '110=di', '106=g', '18=ne', '#de', '12-437=de']),
('342r', 19, ['#foy', '463=fo', '@y|m|top [23]48, bottom [12]59', '"je les ai comparés ensemble et en les rapprochant de ce que"']),
('342r', 20, ['"j\'ai vû moi-même"']),
('342v', 1, ['"Une des premières qualités d\'un"', '#homme', '81-178=homme', '#en', '126=en', '#place', '@p', '@l', '@a', '151=ce']),
('342v', 2, ['"étant sans contredit le"', '#désintéressement', '12-437=dé', '@s', '261=in', '8=té', '298=re', '@s', '101=se', '162=ment', '"on ne peut"']),
('342v', 3, ['"disconvenir que"', '"[struck]"|a struck clear word', '#M. Bigot', '115=M. Bigot', '#n\'ait', '@n', '100=ai', '@t', '#mérité', '92=mé', '74=ri', '8=té', '"en faisant"']),
('342v', 4, ['#une', '137=u', '18=ne', '#fortune', '463=fo', '@r', '274=tu|l|a single 274 where tu is expected; écriture has 176', '18=ne', '#immense', '383=im', '92=me', '@n', '101=se', '#par', '172=par', '#le', '15-287=le', '#commerce', '384=commerce|m|38[46]', '"les"']),
('342v', 5, ['#reproches', '298=re', '@p', '@r', '@o|m|top [46]69, bottom 2[67]6', '271=ch', '339=es', '"qu\'on"', '#lui', '275=lui', '#a', '@a||partly blotted', '"faits: il y en a eu à la"']),
('342v', 6, ['"vérité beaucoup"', '"[struck]"|a blot', '#de', '12-437=de', '#calomnieux', '341=ca', '472=lo', '@m', '441=ni', '@e', '137=u', '142=x', '"mais"']),
('342v', 7, ['"enfin ils étoient tous"', '#excités', '@e', '142=x', '305=ci', '8=té', '@s', '"par les"', '#maux', '285=ma', '137=u', '142=x', '"que"']),
('342v', 8, ['"l\'on ne"', '#ressentoit', '298=re', '@s', '101=se', '@n', '268=to', I_, '@t', '#que', '349-207=que', '#depuis', '412=depuis|l|4[137]2', '#son', '66=so', '@n']),
('342v', 9, ['#administration', '@a', '@d', '294=mi', '441=ni', '@s', '@t', '@r', '@a', '262=ti', '156=on', '"où il faut avouer que"']),
('342v', 10, ['"tout a été dans une"', '#confusion', '86=con', '@f', '137=u', SI, '156=on', '"d\'où sont résultés"']),
('342v', 11, ['#mille', '342=mille|m|3[46]2', '#abus', '301=ab|m|', '137=u', '@s', '"différents. Il ne me siéroit certainement point"']),
('342v', 12, ['"Monseigneur, d\'essayer de développer aux yeux d\'un"']),
('342v', 13, ['"Ministre aussi éclairé que vous les"', '#désordres', '12-437=dé', '@s', '180=or', '@d', '@r', '?=es|l|one or two groups lost in the gutter; not read']),
('342v', 14, ['"qui me semblent devoir toujours"', '#naître', '16=na', I_, '@t', '@r', '@e', '#du', '140-157=du']),
('342v', 15, ['#commerce', '384=commerce|m|38[46]', '#que', '349-207=que', '#toute', '192=toute', '"espèce d\'"', '#officier', '136=officier|m|1[35]6', '"et surtout les"', '#chefs', '271=ch', '452=ef', '@s']),
('342v', 16, ['"pourront"', '#faire', '32=faire', '"mais je dois aussi à la confiance"', '"[struck]"|a struck word', '"dont"']),
('342v', 17, ['"vous voulez bien m\'honorer de ne vous point cacher"']),
('342v', 18, ['"que ce ne sont pas là les seuls dont"|"seuls" not checked on the image', '#le', '15-287=le', '#Canada', '209=Canada', '"ait été"']),
('342v', 19, ['#affligé', '@a', '@f', '@l', I_, '19=gé', '"Les"', '#troupes', '148=troupes', '#qui', '89-455=qui', '#en', '320=en', '#France', '11-299=France', '"sont"']),
('342v', 20, ['#insatiables', '241=in', '608=sa', '262=ti', '@a', '@b|m|top 49[27], bottom 1[23]8', '@l', '339=es', '"ont pensé que leurs"']),
('342v', 21, ['"prétentions ne devoient plus"', '#avoir', '311=avoir', '#de', '12-437=de', '#bornes', '283=bo|m|28[39]', '@r', '18=ne||plural s not written', '#en', '126=en']),
('342v', 22, ['#Amérique', '@a', '92=mé', '74=ri', '349-207=que', '"et surtout vis-à-vis d\'un"', '#Intendant', '241=in', '8=te', '@n||in the gutter']),
('342v', 23, ['361=da|m|value by position: da, or d if the pair is ant', '248-197=nt', '"qui dans l\'inquiétude que lui causoient les"']),
('342v', 24, ['#discours', '110=di', '@s', '367=cour|m|[23]67', '@s', '#publics', '33=pu|l|both digits look alike: 33 or 22', '394=bl', I_, '@c|m|bottom 3[38]9, could be 339; plural s not written', '"voulut"', '#acheter', '@a||inserted above the line', '271=ch||inserted above the line', '@e|l|inserted above the line, under a blot', '@t|m|inserted above the line', '132=er||inserted above the line', '"[struck]"|a struck word under the insertion', '"dans le"']),
('342v', 25, ['"principe"', '#leur', '469=leur', '"[struck]"|a blotted group', '#suffrage', '382=su', '@f', '20=ra', '19=ge', '"soit en les"', '#traitant', '@t', '@r', '?=ai|l|a stacked pair in the gutter, not read']),
('342v', 26, [TA, '248-197=nt', '#splendidement', '@s', '@p', '@l', '126=en', '110=di', '12-437=de', '162=ment', '"à"', '#sa', '608=sa', '#table', '315-=ta||second number of the pair lost in the gutter']),
('342v', 27, ['394=bl', '@e', '"soit en leur accordant"', '#toutes', '192=toute', '#leurs', '469=leur', '#demandes', '319=demande', '"[struck]"|a struck word at the line end']),
('342v', 28, ['"Il comptoit que"|sentence set in brackets in the original', '#la', '265-312=la', '#paix', '109=paix', '"viendroit bientôt"']),
('342v', 29, ['"Tant que les choses restèrent sur ce pied, tout retentit"']),
('342v', 30, ['"[blot]"', '#de', '12-437=de', '#ses', '101=se', '@s', '#éloges', '@e', '472=lo|m|4[79]2', '19=ge||plural s not written', '"mais dès que l\'épuisement"']),
('342v', 31, ['"des"', '#magazins', '285=ma', '225=ga', SI, '@n', '@s', '"l\'obligèrent à tenir une conduite"']),
('342v', 32, ['"différente, il devint alors tout à coup de"', '#l\'homme', '@l', '81-178=homme', '#le', '15-=le||second number of the pair lost in the gutter']),
('342v', 33, ['"plus"', '#aimable', '100=ai', '285=ma', '394=bl', '@e', '#le', '15-287=le', '#plus', '@p', '@l', '137=u', '@s', '#insigne', '241=in', '433=si|l|written under a bar; same shape as the other si groups. The clear copy has "inique"; the cipher gives in-si-g-ne', '10?=g|l|cut by the gutter, only 1.. seen; g = 106 expected']),
('342v', 34, ['18=ne', '#voleur', '72=vo', '469=leur', '"de la"', '#terre', '8=te', '@r', '298=re', '"ce qui ne pouvoit plus se"']),
('342v', 35, ['#délivrer', '12-437=dé', '120=li||1[27]0', '322=v', '@r', '132=er', '"des"', '#magazins', '449=magazins|m|4[24]9', '"fut"', '#exigé', '@e', '142=x', I_, '19=gé', '#en', '126=en', '#argent', '309=arge|l|30[29], at the gutter; value by position: ar, arg or arge (a group may be lost in the gutter)']),
('342v', 36, ['248-197=nt||carried over from line 35 with a = sign', '"il n\'y eut point"', '#à', '@a', '#résister', '298=ré||the clear copy has "reculer"; the cipher gives ré-si-s-t-er', '433=si|m|', '@s', '@t', '132=er', '"[struck]"|a struck group', '#M. de Montcalm', '69=M. de Montcalm|m|large figures written above the struck group; value by position']),
('342v', 37, ['"[struck]"|a long struck run of numbers, not read', '#parloit', '172=par', '472=lo', I_, '@t', '"De ces différentes causes"']),
('342v', 38, ['"est provenue en partie"|with strikings and an interlinear correction; not read closely', '#l\'augmentation', '@l', '89=au', '"[struck]"|a struck group', '106=g', '162=ment||au-g-ment-a-ti-on', '@a', '262=ti', '156=on', '"prodigieuse"']),
('342v', 39, ['"[struck]"|a struck group', '#des', '12-437=de', '@s', '#dépenses', '12-437=dé', '111=pe', '@n', '101=se||plural s not written', '"qui vous ont avec tant de"']),
('343r', 1, ['"raison"', '#effrayé', '452=ef', '@f||no r written', '100=ai', '@e', '"on peut bien"', '#accuser', '31=ac|m|', '363=cu', '101=se', '@r']),
('343r', 2, ['#M. Bigot', '3=M. Bigot|m|a bold single 3 at the line start; M. Bigot is 115 on f.342v', '"d\'avoir occasionné"', '#par', '172=par', '#le', '15-287=le', '#commerce', '384=commerce|m|38[46]', '"[blot]"', '#qu\'il', '325=qu\'', '98=il', '"a introduit"']),
('343r', 3, ['"dans"', '#la', '265-317=la|m|second number 31[27]; 265-312 on f.342v', '#colonie', '410=co', '472=lo', '441=ni', '@e', '"et encore plus par les"', '#abus', '@a', '375=bu', '@s']),
('343r', 4, ['#qu\'il', '325=qu\'', '98=il', '#y', '@y|m|bottom 25[79]', '"a laissé régner la cherté des marchandises et des"']),
('343r', 5, ['"denrées; mais la consommation qui en a été faite quelque énorme"']),
('343r', 6, ['"qu\'elle paroisse"', '"[struck]"', '"peut être regardée"', '#à', '@a', '"bien"|written above the line', '#peu', '174=peu|m|', '#de', '12-437=de', '#chose', '271=ch', '@o|m|top 66[39], bottom [12]76']),
('343r', 7, ['101=se||carried over with a = sign', '#près', '@p', '@r', '339=ès||an accent mark over the group', '"comme"', '#réelle', '298=ré', '216=elle|m|2[12]6', '"elle peut être aisément constatée"']),
('343r', 8, ['"par des"', '#pièces', '494=pi|m|4[39][46]', '@e', '151=ce', '@s', '"presque"', '#toutes', '192=toute', '#émanées', '@e', '285=ma', '18=né', '339=es', '#du', '140-157=du']),
('343r', 9, ['#militaire', '294=mi', '120=li|m|1[23]0', TA, I_, '298=re', '"même. Il y a, Monseigneur, des"', '"[cross mark]"|a cross after "des"']),
('343r', 10, ['#manœuvres', '285=ma', '18=ne', '137=u', '322=v', '@r', '339=es', '"dans tous les"', '#États', '@e', TA, '@t', '@s']),
('343r', 11, ['"J\'ai eu en particulier occasion de l\'apercevoir dans le détail que"']),
('343r', 12, ['"j\'avois à la suite de l\'armée. M. Bigot m\'avoit chargé"']),
('343r', 13, ['"de la partie des vivres et des hôpitaux; j\'ai mis"|"et des hôpitaux" added above the line', '#tout', '192=toute||stands for tout', '#en', '126=en', '#usage', '137=u', '608=sa', '19=ge', '#pour', '450=pour|l|first sign unclear: 450 or 160']),
('343r', 14, ['#y', '@y|m|', '#établir', '@e', TA, '394=bl', I_, '@r', '#l\'ordre', '@l', '180=or', '@d', '298=re', '"Les rations"']),
('343r', 15, ['"se délivroient uniquement"', '#sur', '230=sur', '#les', '15-287=le', '@s', '#billets', '214=bi', '@l', '15-287=le', '@t', '"s"|l|a small raised sign at the page edge, taken as clear s']),
('343r', 16, ['"des"', '#majors', '285=ma', '430=jo|l|4[03]0', '@r||plural s not written', '"et cependant la quantité en"', '#excédoit', '@e', '142=x', '151=cé', '224=do|m|', I_]),
('343r', 17, ['@t||carried over with a = sign', '#toujours', '353=toujours|m|35[39]', '#considérablement', '86=con', SI, '12-437=dé', '20=ra', '394=bl', '@e', '162=ment', '"le"', '#nombre', '333=nom', '194=br', '@e', '"des"']),
('343r', 18, ['#troupes', '148=troupes', '"dont je n\'ai jamais pu connoître"', '#l\'effectif', '@l', '452=ef', '336=ec|m|or 326', '262=ti', '@f']),
('343r', 19, ['"on n\'admet point ici l\'usage des"', '#Rôles', '298=re?|l|alignment uncertain: the clear copy has "Rôles", the groups read re-?-es (perhaps "revues")', '163=?|l|16[35]', '339=es|l|', '"je prendrai"']),
('343r', 20, ['"même la liberté de vous ajouter, Monseigneur, qu\'on"']),
('343r', 21, ['"y laisse"', '#périr', '111=pé', '74=ri', '@r', '"toute espèce de"', '#discipline', '110=di', '@s', '305=ci', '@p', '120=li', '18=ne']),
('343r', 22, ['#militaire', '294=mi', '120=li', TA, I_, '298=re', '#le', '15-287=le', '#soldat', '30=soldat', '"abandonné à la"']),
('343r', 23, ['#licence', '120=li|m|first digit at the edge', '151=ce', '@n', '101=se', '"la plus"', '#effrénée', '452=ef', '298=ré', '18=né', '@e', '#a', '@a||the clear copy has "vole"; the cipher gives a vo-le', '#volé', '72=vo', '15-287=lé']),
('343r', 24, ['"de toutes parts: jamais"', '#dégât', '12-437=dé', '225=ga', '@s||the clear copy has "dégât"', '"ne fut plus"', '#déplorable', '12-437=dé']),
('343r', 25, ['@p', '472=lo', '20=ra', '394=bl', '@e', '#moissons', '51=mo', I_, '@s', '66=so', '@n', '@s', '#bétail', '125=bé', TA]),
('343r', 26, ['98=il', '#volailles', '72=vo', '265-317=la|m|second number 31[27]', '98=il', '15-287=le||plural s not written', '"[struck]"|a struck group', '#légumes', '15-287=lé', '222=gu', '92=me', '"s"|l|a single sign like s or 5, taken as clear s']),
('343r', 27, ['#plantations', '@p', '@l', '@a', '@n', TA, '262=ti', '156=on', '"s"|l|a single sign like s or 8, taken as clear s', '"de"', '#tabac', TA, '321=ba', '@c|m|bottom 3[38]9, could be 339']),
('343r', 28, ['#tout', '192=toute||stands for tout', '"a été"', '#ravagé', '20=ra', '29=va', '19=gé', '#impitoyablement', '383=im', '494=pi|m|4[39]4', '268=to', '@y|m|', '@a', '394=bl', '@e', '162=ment']),
('343r', 29, ['"dans un pays qui éprouvoit déjà la plus grande disette et que"']),
('343r', 30, ['"la famine menaçoit."', '#Toutes', '192=toute||a small raised s after the group', '#représentations', '298=re', '@p', '298=ré||written under a struck group', '101=se', '@n', TA, '262=ti']),
('343r', 31, ['156=on||plural s not written', '"faites à ce sujet ont été"', '#inutiles', '241=in', '137=u', '262=ti', '15-287=le||plural s not written', '"vous"']),
('343r', 32, ['"ne serez pas surpris, Monseigneur, après cela de"']),
('343r', 33, ['#l\'évènement', '@l', '171=évènement', '#funeste', '87=fu', '18=ne', '@s', '8=te', '"qui nous a enfin fait parvenir au"']),
('343r', 34, ['#comble', '410=co', '@m', '394=bl', '@e', '"de"', '#l\'humiliation', '@l', '35=hu', '294=mi', '120=li|m|1[23]0', '@a', '262=ti', '156=on']),
('343r', '35-36', ['"Je crains bien, Monseigneur, que la précipitation avec laquelle je suis obligé de vous écrire n\'ait occasionné"|clear to the foot of the page']),
('343v', '1-', ['"autant de désordre dans l\'arrangement des caractères ... J\'ai l\'honneur d\'être"|all clear, no cipher on this page; not itemised']),
]

word = ''
rows = []; occ = collections.defaultdict(list)  # number -> list of (value, partners, word, folio, line, conf)
seq = 0
for folio, line, items in D:
    for it in items:
        if it.startswith('#'):
            word = it[1:]; continue
        seq += 1
        if it.startswith('"'):
            m = re.match(r'"(.*)"(?:\|(.*))?$', it, re.S)
            txt, rest = m.group(1), (m.group(2) or '')
            parts = rest.split('|') if rest else []
            conf = 'clear'; note = ''
            if parts and parts[0] in ('l', 'm', 'h'):
                conf = {'l': 'low', 'm': 'medium', 'h': 'high'}[parts[0]]; note = '|'.join(parts[1:])
            else:
                note = rest
            rows.append([folio, line, seq, '"%s"' % txt, txt if not txt.startswith('[') else '', conf, note]); continue
        if it.startswith('@'):
            head, _, rest = it.partition('|')
            it = ST[head[1]] + '=' + head[1] + ('|' + rest if _ else '')
        tokval, _, rest = it.partition('|')
        tok, _, plain = tokval.partition('=')
        parts = rest.split('|') if rest else []
        conf = parts[0] if parts and parts[0] in ('l', 'm', 'h') else ''
        note = parts[1] if len(parts) > 1 else ''
        rows.append([folio, line, seq, tok, plain, conf, note, word])

# confidence default: high when the same token with the same value (accents ignored) occurs 2+ times, else medium
import unicodedata
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.rstrip('?')
cnt = collections.Counter((r[3], norm(r[4])) for r in rows if len(r) == 8)
for r in rows:
    if len(r) == 8:
        if not r[5]:
            r[5] = 'h' if cnt[(r[3], norm(r[4]))] >= 2 and '?' not in r[3] else 'm'
        r[5] = {'l': 'low', 'm': 'medium', 'h': 'high'}[r[5]]
        nums = [n for n in re.split(r'[/-]', r[3]) if n and n != '?']
        for n in nums:
            occ[n].append((r[4], [x for x in nums if x != n], r[7], r[0], r[1], r[5], '/' in r[3], '-' in r[3]))

with io.open(os.path.join(OUT, 'sept_cipher_aligned.tsv'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('folio\tline\tseq\ttoken\tplain\tconf\tnote\n')
    for r in rows:
        f.write('\t'.join(str(x) for x in r[:7]) + '\n')

def keyf(n):
    m = re.match(r'\d+', n); return (int(m.group()) if m else 9999, n)
conflicts = []
with io.open(os.path.join(OUT, 'sept_key_from_pair.tsv'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('number\tvalue\tn_occurrences\thomophone_partner(s)\tconf\tevidence\n')
    for n in sorted(occ, key=keyf):
        L = occ[n]
        vals = collections.Counter(norm(v[0]) for v in L)
        shown = collections.OrderedDict()
        for v in L: shown.setdefault(norm(v[0]), v[0])
        value = ' / '.join('%s (%d)' % (shown[k], c) if len(vals) > 1 else shown[k] for k, c in vals.most_common())
        partners = collections.Counter()
        for v in L:
            for p in v[1]: partners[('stack ' if v[6] else 'dash ') + p] += 1
        ps = ', '.join('%s x%d' % (p, c) for p, c in partners.most_common())
        confs = [v[5] for v in L]
        if len(vals) > 1: conf = 'CONFLICT'; conflicts.append((n, value))
        elif 'low' in confs and confs.count('low') * 2 >= len(confs): conf = 'low'
        elif len(L) >= 2 and confs.count('high') * 2 >= len(confs): conf = 'high'
        else: conf = 'medium' if 'low' not in confs else 'low'
        ev = collections.OrderedDict()
        for v in L: ev.setdefault('%s (f.%s l.%s)' % (v[2], v[3], v[4]), 1)
        f.write('\t'.join([n, value, str(len(L)), ps, conf, '; '.join(list(ev)[:4])]) + '\n')

ciph = [r for r in rows if len(r) == 8]
print('rows', len(rows), 'cipher slots', len(ciph), 'clear slots', len(rows) - len(ciph))
print('conf', collections.Counter(r[5] for r in ciph))
print('distinct numbers', len(occ))
kc = collections.Counter()
import csv
for line in io.open(os.path.join(OUT, 'sept_key_from_pair.tsv'), encoding='utf-8').read().split('\n')[1:]:
    if line: kc[line.split('\t')[4]] += 1
print('key conf', kc)
print('conflicts', conflicts)
print('stacks', sum(1 for r in ciph if '/' in r[3]), 'dash', sum(1 for r in ciph if '-' in r[3]), 'single', sum(1 for r in ciph if '/' not in r[3] and '-' not in r[3]))
