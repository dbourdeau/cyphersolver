# Mots de l'argot décodé par la clé qummī (c2) : attestation dans Lisān et Tāj (DESCRIPTIF, après la mesure c3)

Sources : OpenITI, *Lisān al-ʿArab* (0711IbnManzurIfriqi.LisanCarab.Shamela0001687-ara1, sha256 34fa5671…) et
*Tāj al-ʿarūs* (1205MurtadaZabidi.TajCarus.Shamela0007030-ara1, sha256 eb756c4c…), téléchargés le 28/11 vers
`SPOF_2/…/ljs51/corpus/` (30,7 + 40,1 Mo). Comptes = jetons normalisés (qummi_lib.normalize : sans voyelles, ة→ه, ى→ي,
hamza supprimée) ; « sans préf. » = après retrait de و/ب/ف/ل/ال. Script : `attestations_post_c3.py` ; données :
`ATTESTATIONS_post_c3.json`. **Une forme attestée n'est pas un sens attesté** : un homographe arabe ordinaire ne dit
rien du sens dans l'argot. Rien de ceci n'entre dans un critère.

| # | argot (38r) | décodage qummī | Lisān | Tāj | remarque (contexte trouvé, ou racine) |
|---|---|---|---|---|---|
| 1 | ركشذ | دمخت | 0 | 0 | racine دمخ attestée (« baisser la tête ») ; glossaire du compilateur : دمخنث |
| 2 | زوهشوثول | بالخاجاه | 0 | 0 | inconnu (خاجاه/خواجه ?) |
| 3 | هفهل | ليله | 462 | 476 | « nuit » ; mot courant |
| 4 | سزاو | عبوا | 2 | 0 | homographe (عبا المتاع, « ranger ») ; glossaire : عبواسر |
| 5 | رهنف | دلقي | 0 | 0 | racine دلق attestée (10) ; *dalq* = froc rapiécé du derviche, sens non attesté ici |
| 6 | اغوس | وضاع | 6 (14) | 10 (21) | « et (le musc) se répandit » ; aussi وضّاع « forgeur de ḥadīth » |
| 7 | ففع | ييس | 20 | 19 | = يئس « désespéra » (hamza normalisée) |
| 8 | طخفخف | حشيشي | 0 | 0 | حشيش attesté (13, « herbe sèche ») ; « mon haschich » ? non attesté |
| 9 | ابغراو | وزضدوا | 0 | 0 | inconnu |
| 10 | سهنف | علقي | 14 | 11 | homographe : plante (vers d'al-ʿAjjāj) |
| 11 | اوغطفذ | واضحيت | 0 (3) | 0 (2) | اضحيت « je devins » |
| 12 | نفدف | قيري | 0 | 0 | القير « poix » attesté (5) |
| 13 | كبيذ | مزفت | 2 | 1 | « enduit de poix (jarre à vin) » ; voisin sémantique de قير (12) |
| 14 | غون | ضاق | 68 | 78 | « devint étroit » |
| 15 | زو | با | 65 | 90 | particule/fragment |
| 16 | شهنف | خلقي | 11 | 9 | « mon caractère » ou « mes haillons » (خَلَق) |
| 17 | هو | لا | 18 797 | 18 787 | mot-outil |
| 18 | خف | شي | 4 345 | 4 061 | mot-outil |
| 19 | ومخ | اكش | 0 | 0 | **absent des deux dictionnaires** ; glosé اكل par le compilateur (38r, dernière ligne ; revérifié par Daniel) : mot d'argot |
| 20, 22 | اهو | ولا | 11 976 | 11 328 | mot-outil |
| 21 | وبيذ | ازفت | 2 | 3 | homographe coranique (أزفت الآزفة) ; ou « plus poisseux » (زفت) |
| 23 | وهنف | القي | 254 (15) | 252 (24) | « je jette » / ألقى |

Bilan descriptif : 6 mots pleins sur 18 au lexique du modèle (ليله وضاع ييس ضاق خلقي القي, remarque 4 de Daniel),
plus un petit champ « poix » (قيري, مزفت, ازفت) et deux racines d'habits/derviches (دلقي, خلقي) qui méritent la lecture
par le sens dans Bosworth 1976. اكش, absent des dictionnaires classiques mais glosé par le compilateur, est le meilleur
indice que le décodage donne l'argot lui-même. Aucun des 23 mots d'« argot » non décodés n'est un mot plein attesté
(seuls des homographes courts : هو, خف, زو, غون).
