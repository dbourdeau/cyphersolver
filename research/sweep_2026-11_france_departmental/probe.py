import subprocess,re,sys
doms="""archives.gironde.fr archives.hauts-de-seine.fr archives.landes.fr archives.lamayenne.fr archives.sarthe.fr archives.maine-et-loire.fr archives.vendee.fr archives.loiret.fr archives.charente.fr archives.charente-maritime.fr archives.deux-sevres.fr archives.lavienne86.fr archives.haute-vienne.fr archives.dordogne.fr archives.lotetgaronne.fr archives.tarn.fr archives.aude.fr archives.pyrenees-orientales.fr archives.morbihan.fr archives.finistere.fr archives.cotesdarmor.fr archives.calvados.fr archives.manche.fr archives.orne.fr archives.eure.fr archives.seine-maritime.fr archives.somme.fr archives.oise.fr archives.aisne.fr archives.marne.fr archives.ardennes.fr archives.meuse.fr archives.vosges.fr archives.moselle.fr archives.bas-rhin.fr archives.haut-rhin.fr archives.cotedor.fr archives.yonne.fr archives.nievre.fr archives.saone-et-loire.fr archives.jura.fr archives.allier.fr archives.puy-de-dome.fr archives.cantal.fr archives.loire.fr archives.drome.fr archives.ardeche.fr archives.ain.fr archives.savoie.fr archives.var.fr archives.vaucluse.fr archives.alpes-maritimes.fr archives.gard.fr archives.lozere.fr archives.aveyron.fr archives.lot.fr archives.gers.fr archives.hautes-pyrenees.fr archives.ariege.fr archives.corrèze.fr archives.creuse.fr archives.indre.fr archives.cher.fr archives.loir-et-cher.fr archives.eure-et-loir.fr archives.essonne.fr archives.yvelines.fr archives.valdoise.fr archives.seine-et-marne.fr archives.valdemarne.fr archives.seinesaintdenis.fr archives.cd54.fr archives.haute-marne.fr archives.aube.fr archives.haute-saone.fr archives.territoiredebelfort.fr archives.pas-de-calais.fr archives.alpes-de-haute-provence.fr archives.hautes-alpes.fr archives.corse.fr archives.guadeloupe.fr archives.martinique.fr archives.reunion.fr""".split()
import concurrent.futures as cf
def f(d):
    try:
        o=subprocess.run(['curl','-s','-m','12','-L','-A','Mozilla/5.0','https://'+d+'/'],capture_output=True).stdout.decode('utf8','ignore')
    except Exception as e: return d,'err'
    if not o: return d,'none'
    lig='ligeo' in o.lower()
    m=re.findall(r'recherche/transversale/n:\d+',o)
    return d,('LIGEO ' if lig else '')+(m[0] if m else '')+' len=%d'%len(o)
with cf.ThreadPoolExecutor(8) as ex:
    for d,r in ex.map(f,doms): print(d,r)
