"""Reading of the re-read lines, written as word-level patches on Daniel's b34 (b) lines (old text asserted).
[x=v] = probable (tentative) value; everything else unchanged from b34."""
P = {
 ('141v','2'):[('Su Sd. [x','Su Sd. [x=r]-')], ('141v','3'):[('-r-o-l-ve]','-e-s-o-l-ve'),('con [ꝍ z q α] la','con s-o-l-a la')],
 ('141v','4'):[('c-a-l-do-[ꝍ]?','c-a-y-do-s')], ('141v','5'):[('que [ne] e-n-r-a-r','que p-e-n-s-a-r')],
 ('141v','11'):[('la [ꝍ] con','la-s con')], ('141v','13'):[('[pol] [ter]','[pol] no')], ('141v','14'):[('y e-r-o lo','y s-o-lo')],
 ('141v','21'):[('lo r que','lo-s que')], ('141v','25'):[('a otro r..','a otro-s ..')],
 ('142r','2'):[('t-a-e-a-p-a-r-c-u-a(?)','t-a-e-a p-a-s-c-u-a'),('el [⅄] es t-a-n-t-e-a','el [x=r]-es-t-a-n-t-e a')],
 ('142r','5'):[('el papa [ne]-i en-r-a','el papa p-i-en-s-a'),('de esto-r','de esto-s')],
 ('142r','6'):[('z-c-io','-r-c-io'),('con-se-r-va-r lo r en','con-se-r-va-r-lo-s en')],
 ('142r','8'):[('la en [ne]-r-e-r-a','la en-p-r-e-s-a')],
 ('142r','15'):[('y-n-[ne]-o si-b-i-l(?)-h-da-e','y-n-p-o-si-b-i-l-[ε=i]-da-d'),('le r-h-i-z(?)','le-s h-i-z-')],
 ('142r','16'):[('h-e-r-on(?) p-r-o-me-r-a','-[ε=i]-e-r-on p-r-o-me-s-a'),('le r mas','le-s mas')],
 ('142r','18'):[('[cas=tien] [⅄] es','[cas=tien]-e es')],
 ('142r','20'):[('c-[ꝺ]-p-i-e-r-[6]','c-u-p-i-e-r-e'),('esto-r otro-r','esto-s otro-s'),('[guf=puede] [⅄]-e-r','[guf=puede] [x=r]-e-s-')],
 ('142r','21'):[('o-l-ve cosa','-o-l-ve cosa'),('"tanbien" ...','"tanbien" s-u-s-p-en-de')],
 ('142r','22'):[('da-t-o(?)','da-ñ-o')], ('142r','24'):[('[ror]-r','[ror=ducado]-s'),('le r-e-i-o tiempo','le-s d-i-o tiempo')],
 ('142r','25'):[('[zir] [ne]-e-t-r-[ꝺ]-r-c-o','[zir=cardenal] P-e-t-r-u-[ɞ=c]-c-o')],
 ('142v','1'):[('[3 ꝺ 9]','q-u-e')], ('142v','3'):[('[b?]-a-r-t-a-do','b-a-s-t-a-do')],
 ('142v','6'):[('no r-an-a su-r-[ne]-i-c-io-n','no s-an-a su-s-p-i-c-io-n')], ('142v','11'):[('p-u-e-i-e-r-a','p-u-d-i-e-r-a')],
 ('142v','16'):[('por ve-r-u V.Md.','por [bog]-r V.Md.')], ('142v','17'):[('[ne]-e-e-ir lo','p-e-d-ir lo')],
 ('143r','8'):[('[ne]-i-r-r de p-r-u-n-t-o','p-i-e-r de p-u-n-t-o')], ('143r','10'):[('en-g-a-t-a-do-r','en-g-a-ñ-a-do-s')],
 ('143r','14'):[('[c-e-s-i-es?]','c-[xir=ardenal]-es V-o-l-t-e-[x=r]-a')], ('143r','16'):[('si n-a-[ꝺ]-e-o-r-i-da-e','si-n a-u-d-o-r-i-da-d')],
 ('143v','9'):[('con-[⅄]-[ꝺ3]-s-t-a-r','con-q-u-i-s-t-a-r')], ('144v','2'):[('[Jum] [Ɉ9⅄]','[Jum] [Ɉ9⅄=vez]')],
 ('144v','3'):[('si-n [Ɉ]-r-da','si-n d-u-da')], ('144v','7'):[('ha p-[Ɉ]-[gat]','ha p-u-esto')],
 ('144v','8'):[('[Jz x] [ges] t-i-t-[Ɉ] c-[boz]-n','[Jz] [x=r]-es-t-i-t-u-c-io-n')],
 ('144v','16'):[('a [Ɉ9⅄] [ges]','a [Ɉ9⅄=vez]-es')], ('144v','17'):[('[Jum] [Ɉ9⅄]','[Jum] [Ɉ9⅄=vez]')],
 ('144v','18'):[('no [Ɉ 9 x] mas','no v-e-e mas'),('no [Ɉ9','no [ꝺ9=ve]-')], ('144v','19'):[('-r-a] por','-r-a por')],
 ('144v','20'):[('el [ges] muy','el es muy')],
 ('145r','1'):[('[ꝺ]-o-c-o','[v=m]-o-c-o'),('[ꝑ ag Ɉ ꝺ3]-s-t-o','[ag] q-u-i-s-t-o')], ('145r','7'):[('c-u-[L]-','c-u-ñ-')],
 ('145v','17'):[('[ges] justo(mon)','es justo(mon)'),('da-[L]-a-r-ia','da-ñ-a-r-ia')],
 ('145v','18'):[('[ges] p-e-r-a-n-c-a-s','es-p-e-r-a-n-c-a-s')],
 ('145v','19'):[('[Ɉ3]-t-o','d-i-t-o'),('[gib] a-r-[Ɉ]-i-t-o-r','el a-u-d-i-t-o-r'),('[ges] es t-r-e-c-h-o','es es-t-r-e-c-h-o')],
 ('145v','20'):[('no le [ges] t-i-v-o','no le es-t-i-v-o')], ('145v','21'):[('[ges] s-on','es s-on')],
 ('146r','13'):[('[Ɉ]-o-[ꝗ]-t-e-z-a','V-o-l-t-e-[x=r]-a')], ('146r','14'):[('si g-[Ɉ]-e a [Ɉ]-o-[ꝗ]-t-e-z-a','si-g-u-e a V-o-l-t-e-[x=r]-a')],
 ('146r','15'):[('y n-r-[Ɉ]-i-e-t-[Ɉ]-e','y-n-q-u-i-e-t-u-[9=d]'),('[ƉƉ] [ges]','[ƉƉ] es')],
 ('146r','16'):[('de [Ɉ]-e da-r','de-v-e da-r')], ('146r','17'):[('c-r-[Ɉ]-s','c-r-u-z')],
 ('146r','18'):[('p-e-r-t-e-n-r-c-e','p-e-r-t-e-n-e-c-e')], ('146r','19'):[('[ges] c-[Ɉ]-s-a','es-c-u-s-a')],
 ('146r','20'):[('[ges] c-','es c-')], ('146r','21'):[('[ges] c-r-i-va p-i-[Ɉ]-h en-do','es-c-r-i-va p-i-d-[Є=i]-en-do')],
 ('146r','22'):[('p-o-[Ɉ]-r-a','p-o-d-r-a')], ('146v','2'):[('[ges] t-i-[Ɉ]-a-n','es-t-i-m-a-n')],
 ('146v','3'):[('c-r-e-c-[6]-n-[Ɉ]-e-v-o','c-r-e-c-e-n [Ɉ]-e-v-o')], ('146v','7'):[('su c-e-[Ɉ]-i-e-r-r','su-c-e-d-i-e-r-e')],
 ('146v','10'):[('de-s-p-e-[Ɉ] [bla]','de-s-p-e-d-ir'),('[qat]-s [Ɉ]-o-t-i-[Ɉ]-os','[qat]-s m-o-t-i-u-os')],
 ('146v','11'):[('[ꝛir] [ges]','[ꝛir] es')],
}
import json, sys
if __name__ == '__main__':
    recs = json.load(open(sys.argv[1])); keys = {(r['page'], r['line']) for r in recs}
    assert all(k in keys for k in P), [k for k in P if k not in keys]
    ch = {tuple(l.split('\t')[:2]) for l in open(sys.argv[2]).read().splitlines()[1:]}
    fo = {'before_portion': open(sys.argv[3] + '_before_portion.txt', 'w'), 'after_portion': open(sys.argv[3] + '_after_portion.txt', 'w'),
          'before_all': open(sys.argv[3] + '_before_all.txt', 'w'), 'after_all': open(sys.argv[3] + '_after_all.txt', 'w')}
    for i, r in enumerate(recs):
        k = (r['page'], r['line']); b = r['b']; nb = b
        for old, new in P.get(k, []):
            assert nb.count(old) == 1, (k, old, nb)
            nb = nb.replace(old, new)
        fo['before_all'].write(f'{i+1}b {b}\n'); fo['after_all'].write(f'{i+1}b {nb}\n')
        if k in ch or k in P:
            fo['before_portion'].write(f'{i+1}b {b}\n'); fo['after_portion'].write(f'{i+1}b {nb}\n')
    print('ok', sum(len(v) for v in P.values()), 'patches on', len(P), 'lines')
