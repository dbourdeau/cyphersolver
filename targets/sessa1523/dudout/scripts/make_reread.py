"""Build the sign-by-sign re-read transcription of R9660 ff.141v-146v from Daniel Bourdeau's b34 (a) lines.
Every change asserts the old text. Sign names (this re-read):
  ɞ  six-shaped sign with a bar (b34 part 1: one of the two shapes written ꝍ; part 2: written ꝺ)
  ꝛo z-hook over o (b34 part 1: the other ꝍ shape; part 2: ꝛo)
  ꝺ  looped open ∂ (part 1: ꝺ; part 2: part of the signs written Ɉ)
  ꝗ  flat-topped g with a flag (b34: written g or Ɉ or ꝑ)
  ɔ  reversed c with a stroke (b34: 3, ⅄ or Ɉ)
  6  six-shaped sign without bar (b34: 6 or ꝺ)
  ∠  angle with o (b34: ⅄ or L)
Usage: make_reread.py b34_lines.json out_transcription.txt out_changes.tsv"""
import json, sys, re
P1 = ('141v', '142r', '142v', '143r')
SEQ = {  # class of each b34 'ꝍ' in order (part 1 only): R = ɞ, S = ꝛo
 ('141v','1'):'R',('141v','2'):'R',('141v','3'):'SSSS',('141v','4'):'SR',('141v','5'):'SRR',('141v','6'):'RS',
 ('141v','7'):'R',('141v','8'):'R',('141v','9'):'SR',('141v','10'):'R',('141v','11'):'RS',('141v','12'):'SR',
 ('141v','13'):'SR',('141v','14'):'R',('141v','15'):'RSRR',('141v','16'):'R',('141v','19'):'R',('141v','20'):'SS',
 ('141v','21'):'S',('141v','23'):'RR',('141v','25'):'SRSS',
 ('142r','2'):'S',('142r','3'):'RRR',('142r','4'):'S',('142r','5'):'SRS',('142r','6'):'RRS',('142r','7'):'R',
 ('142r','8'):'RRS',('142r','9'):'R',('142r','11'):'S',('142r','12'):'RRS',('142r','13'):'SRR',
 ('142r','14'):'SS',('142r','15'):'RS',('142r','16'):'RRSRS',('142r','18'):'RSR',('142r','19'):'RR',
 ('142r','20'):'RSSS',('142r','21'):'SSSS',('142r','22'):'SS',('142r','24'):'SSS',('142r','25'):'RR',
 ('142v','1'):'R',('142v','2'):'R',('142v','3'):'S',('142v','4'):'R',('142v','5'):'RS',('142v','6'):'SS',
 ('142v','7'):'RS',('142v','8'):'R',('142v','9'):'R',('142v','10'):'SSRR',('142v','11'):'RRS',('142v','12'):'SR',
 ('142v','13'):'RRSR',('142v','14'):'R',('142v','15'):'RRSR',('142v','16'):'R',('142v','17'):'SSRR',
 ('142v','18'):'SS',('142v','19'):'S',
 ('143r','2'):'SS',('143r','3'):'RRR',('143r','4'):'R',('143r','7'):'R',('143r','8'):'RSRR',('143r','10'):'SS',
 ('143r','11'):'S',('143r','13'):'S',('143r','15'):'R',('143r','16'):'R',
}
# (page, line): [(old, new), ...]  -- substitutions on the b34 (a) text, applied before the ꝍ classes / part-2 notation.
# In part 2, 'Ü' marks this re-read's looped ∂ (u/v) and is turned into ꝺ after b34's part-2 ꝺ (= ɞ) is renamed.
ED = {
 ('141v','4'):[('q ram','q̃ ram')], ('141v','6'):[('x ⅄ α','x z α')], ('141v','11'):[('Jep 4 bob','Jez 4 bob')],
 ('141v','13'):[('pol ter le','pol ler le')], ('141v','14'):[('q̃ x ꝍ z','q̃ ꝛo z')], ('141v','15'):[('3i do','li do')],
 ('141v','19'):[('ka g 3 α','ka ꝗ 3 α')], ('141v','24'):[('nf α ⅄ 3 α','nf α ∠ 3 α')],
 ('142r','2'):[('qib ⅄ qes','qib x qes')], ('142r','3'):[('qib boz ꝺ 9','qib loz ꝺ 9')],
 ('142r','5'):[('sof x 4 ꝍ α mus sit','sof xoc ꝍ α mus sir')], ('142r','6'):[('⅄ ttt boz hag','ɞ ttt boz hag')],
 ('142r','7'):[('suf α cap','suf α cep')],
 ('142r','11'):[('do ttt α ttt boz','do ott α ttt boz')], ('142r','14'):[('pu3 ⅄an','puc 3an')],
 ('142r','15'):[('sad g f~','sad ꝗ f~')], ('142r','18'):[('cas ⅄ qes','cas x qes'),('z y # 3 ram','z y ꝗ 3 ram')],
 ('142r','20'):[('guf ⅄ 9','guf x 9')], ('142r','22'):[('α z om qes','α zom qes')], ('142r','24'):[('ka ꝍ g 3 4','ka ꝍ ꝗ 3 4')],
 ('142v','1'):[('ott 4 3 ꝺ 9','ott 4 ɔ ꝺ 9')], ('142v','4'):[('tto ꝺ q x dim','tto ꝺ q̃ x dim')],
 ('142v','5'):[('f~ bdl lorot','f~ bid lorot')], ('142v','7'):[('q̃ do ⅄ g ꝍ 4','q̃ do x 9 ꝍ 4')],
 ('142v','11'):[('sad g gap dim nf ꝺ g 3 x','sad ꝗ gap dim nf ꝺ ꝗ 3 x')], ('142v','16'):[('hef boe ꝍ ꝺ bas','hef bog ꝍ f~ bas')],
 ('142v','17'):[('ne g g bla','ne 9 ꝗ bla'),('q ⅄ g gap','q x 9 gap')],
 ('143r','8'):[('sof nf ꝍ ꝺ do','sof nf ꝺ do')], ('143r','13'):[('q̃ ⅄ 9 ⅄ 4','q̃ x 9 ⅄ 4')],
 ('143r','14'):[('ttt x 3 qes','ttt xir qes'),('ott 9 ⅄ α','ott 9 x α')], ('143r','16'):[('ꝺ g z','ꝺ ꝗ z'),('sad g sof','sad ꝗ sof')],
 ('143v','9'):[('tac ⅄ ꝺ3 ꝛo','tac ɔ Ü 3 ꝛo')],
 ('144v','2'):[('Jum Ɉ9⅄ oug','Jum Ü9⅄ oug')], ('144v','3'):[('cob do Ɉ ꝺ sad','cob do ꝗ Ü sad')],
 ('144v','6'):[('f~ Ɉ z q ott','f~ Ü z q ott')], ('144v','7'):[('njn nf Ɉ gat','njn ne Ü gat')],
 ('144v','8'):[('Ɉ 4 9 ott 9 x α Jz x ges ott 3 ott Ɉ ttt','Ü 4 q ott 9 x α Jz x qes ott 3 ott Ü ttt')],
 ('144v','9'):[('qib Ɉ 9 do x','qib Ü 9 do x')], ('144v','11'):[('Ɉ ꝛo α ꝺ kef','9 ꝛo α ꝺ kef')],
 ('144v','13'):[('f~ Ɉ z q ott','f~ Ü z q ott'),('ꝛo Ɉ α q dim','ꝛo Ü α q dim')],
 ('144v','16'):[('f~ v:db Ɉ z q','f~ v:db Ü z q'),('Ɉ9⅄ ges','Ü9⅄ qes'),('ttt ꝺ x Ɉ 3 ott','ttt ꝺ x ꝗ 3 ott')],
 ('144v','17'):[('Jum Ɉ9⅄ d la','Jum Ü9⅄ d la')], ('144v','18'):[('lex Ɉ 9 x kah','lex Ü 9 x kah'),('ler Ɉ9','ler Ü9')],
 ('144v','19'):[('dim α b α L d sof','dim α b α ∠ d sof')], ('144v','20'):[('qib ges log','qib qes log')],
 ('144v','23'):[('ott ꝺ Ɉ ttt 4','ott ꝺ Ü ttt 4')],
 ('145r','1'):[('f~ ꝺ 4 ttt z','f~ v 4 ttt z'),('ꝑ ag Ɉ ꝺ3 ꝛo','ꝛo ag ɔ Ü 3 ꝛo')], ('145r','2'):[('ott Ɉ ꝺ α','ott Ü ꝺ α')],
 ('145r','3'):[('9 3 sad ꝺ','9 3 sad ꝗ')], ('145r','4'):[('ott ꝺ Ɉ ꝺ ttt z','ott ꝺ Ü ꝺ ttt z')],
 ('145r','5'):[('tto Ɉ ꝺ # Ɉ ges','tto Ü ꝺ # Ü ges'),('qus ges log','qus qes log')],
 ('145r','7'):[('gap α Jz ⅄ Ɉ3 ꝺ boz ꝛo Ɉ α 9 ꝺ x f~ hag ges log','gap α ꝗ ɔ Ü 3 ꝺ boz ꝛo Ü α 9 ꝺ x f~ hag qes log'),('ttt Ɉ L','ttt Ü ∠')],
 ('145r','10'):[('q3 sad ꝑ pu3','q3 sad ꝗ pu3')], ('145r','11'):[('# Ɉ α','# Ü α')], ('145r','12'):[('ott b Ɉ 4','ott b Ü 4')],
 ('145r','13'):[('# Ɉ ꝺ α Ɉ suf','# Ü ꝺ α Ü suf')], ('145r','14'):[('suf nf Ɉ 9 tto','suf ne Ü 9 tto')],
 ('145r','16'):[('ttt 3 Ɉ sad','ttt 3 Ü sad'),("nf Ɉ ''","nf Ü ''")], ('145r','19'):[('Jim ꝛo Ɉ 4 ꝺ α ꝛo','Jim ꝛo dor α ꝛo')],
 ('145r','21'):[('vod Ɉ ꝺ cob','vod Ü ꝺ cob'),('gap ꝺ x Ɉ x 9 Ɉ Ɉ ⅄ bla','gap ꝺ x Ü x 9 ꝗ Ü ⅄ bla')],
 ('145v','3'):[('suf α Ɉ 3 oo 3 ttt Ɉ 9','suf α ꝗ 3 oo 3 ttt Ü 9')], ('145v','5'):[('ttt 9 Ɉ bla','ttt 9 Ü bla')],
 ('145v','17'):[('ges mon','qes mon'),('sad L α','sad ∠ α')], ('145v','18'):[('α ꝛo ges nꝑ','α ꝛo qes nꝑ')],
 ('145v','19'):[('Ɉ3 ott 4 f~ gib d ꝺ Ɉ 3 ott','ꝗ 3 ott 4 f~ qib d Ü ꝗ 3 ott'),('ges ges ott','qes qes ott')],
 ('145v','20'):[('ka ges ott 3 b 4','ka qes ott 3 b 4')], ('145v','21'):[('ott ꝺ ges ꝛo z y','ott ꝺ qes ꝛo z y')],
 ('146r','13'):[('lep Ɉ 4 ka ꝛo f~ Ɉ 4 ꝗ ott 9 ⅄ α ꝑ njn Ɉ ꝛo','lep Ü 4 ka ꝛo f~ Ü 4 q ott 9 x α ꝑ njn Ü ꝛo')],
 ('146r','14'):[('cob # Ɉ 9 d Ɉ 4 ꝗ ott 9 ⅄ α','cob # Ü 9 d Ü 4 q ott 9 x α')],
 ('146r','15'):[('do ꝺ Ɉ 3 9 ott Ɉ 9 dim','do ɔ Ü 3 9 ott Ü 9 dim'),('gap Ɉ Ɉ ges ott','gap Ü qes ott')],
 ('146r','16'):[('sof Ɉ g sad','sof Ü 9 sad')], ('146r','17'):[('ttt ꝺ Ɉ ꝛo b 4','ttt ꝺ Ü ⅄ b 4')],
 ('146r','18'):[('ott x do ꝺ ttt x','ott x do 6 ttt x')], ('146r','19'):[('ges ttt Ɉ ꝛo α','qes ttt Ü ꝛo α')],
 ('146r','20'):[('α ges ttt','α qes ttt')], ('146r','21'):[('kef ges ttt ꝺ 3 bad nꝑ 3 Ɉ Є','kef qes ttt ꝺ 3 bad nꝑ 3 ꝗ Є')],
 ('146r','22'):[('nꝑ 4 Ɉ ꝺ α','nꝑ 4 ꝗ ꝺ α')],
 ('146v','2'):[('ka ges ott 3 Ɉ α do','ka qes ott 3 v α do'),('lep Ɉ 4','lep v 4')], ('146v','3'):[('do Ɉ 9 b 4','do Ü 9 b 4')],
 ('146v','7'):[('ttt 9 Ɉ 3 x ꝺ ꝺ d bol','ttt 9 ꝗ 3 x ꝺ 6 d bol')],
 ('146v','10'):[('nꝑ 9 Ɉ bla','nꝑ 9 ꝗ bla'),('qat ꝛo Ɉ 4 ott 3 Ɉ Jim','qat ꝛo v 4 ott 3 Ü Jim')], ('146v','11'):[('ꝛir ges ka','ꝛir qes ka')],
}
def apply(r):
    k = (r['page'], r['line']); a = r['a']
    for old, new in ED.get(k, []):
        assert a.count(old) == 1, (k, old, a)
        a = a.replace(old, new)
    if r['page'] in P1:
        seq = SEQ.get(k, '')
        assert a.count('ꝍ') == len(seq), (k, a.count('ꝍ'), seq, a)
        for c in seq:
            a = a.replace('ꝍ', 'ɞ' if c == 'R' else 'ꝛo', 1)
    else:
        a = a.replace('ꝺ', 'ɞ').replace('Ü', 'ꝺ')
    return a
def norm_old(r):  # b34 (a) line with only the part-2 renaming (ꝺ -> ɞ), for comparison
    return r['a'] if r['page'] in P1 else r['a'].replace('ꝺ', 'ɞ')
if __name__ == '__main__':
    recs = json.load(open(sys.argv[1]))
    used = set()
    out = open(sys.argv[2], 'w'); ch = open(sys.argv[3], 'w')
    ch.write('page\tline\tb34 (a)\tre-read\n')
    for r in recs:
        new = apply(r); k = (r['page'], r['line'])
        out.write(f"{r['page']}.{r['line']}\t{new}\n")
        if new != norm_old(r): ch.write(f"{r['page']}\t{r['line']}\t{norm_old(r)}\t{new}\n")
    missing = [k for k in list(ED) + list(SEQ) if k not in {(r['page'], r['line']) for r in recs}]
    assert not missing, missing
    print('ok')
