"""Table T2 = T (gelée, work/table_T.py) + valeurs apprises des gloses de H (img 561, mesure 1 faite, H désormais grillé et versé à l'apprentissage).
Aucun feuillet H2 (553 L, 541 L, 638 R) regardé avant ce gel. Les lectures de 573 (non glosé) NE sont PAS versées à T2."""
import json, importlib.util, os
spec=importlib.util.spec_from_file_location('t1',os.path.join(os.path.dirname(os.path.abspath(__file__)),'table_T.py')); t1=importlib.util.module_from_spec(spec); spec.loader.exec_module(t1)
T=dict(t1.T)
ADD={'U4':'x','ff':'d','74':'lempereur','88':'leroydespagne','101':'lasuede','117':'lempire','118':'lespagne','150':'danois','152':'suedois',
     '165':'ambassade','180':'bon','207':'don','212':'ennemi','248':'roy','321':'paix','328':'prince','358':'satisfaction','386':'vaisseau',
     '61':'leroytreschrestien','92':'leroydangleterre'}
T.update(ADD)
if __name__=='__main__':
    import sys; json.dump({'T':T,'ajouts':sorted(ADD)},sys.stdout,ensure_ascii=False,indent=0,sort_keys=True)
