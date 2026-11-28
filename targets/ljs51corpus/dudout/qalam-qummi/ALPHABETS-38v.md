# LJS 51, f. 38v l.3-7 et f. 38r l.8-11 — transcription (gelée avant toute comparaison)

Image : University of Pennsylvania, LJS 51, OPenn (IIIF Penn 2343 × 2964, PDM 1.0).
f38v_2343.jpg sha256 7bbaa144f9ed6abcb7e4a4cf9fca6e9c3338c1db7cef6581fb43f1caffbc7860 ;
f38r_2343.jpg sha256 079a5af88da50e398318a0bec084444e5cb678e5b9eb369905b7458fff86f6d0.
Lecture : agent ljs51-qummi, 28/11/2026, trois passes (vue de page 900 px, ligne à 1,5×, fins de ligne à 3×).

## Constat d'abord : ce ne sont PAS des suites de signes

Les « deux suites » de 38v l.4 (« pahlavi ») et l.6 (« qummī ») sont écrites **en lettres arabes ordinaires**,
de la même main et de la même encre que le texte courant, pointées. Il n'y a aucun signe inventé sur ces deux lignes.
Les signes inventés de 38v sont ailleurs : l.10-13 (un autre chiffre, « من نظمه », hors de cette piste).
Conséquence : la comparaison « forme à forme » avec des tables de signes imprimées (brief, point b) n'a pas d'objet
telle quelle ; ce qu'on peut comparer, c'est l'inventaire et l'ordre des lettres.

## 38v l.3-7 (texte courant, lecture concordante avec Daniel, chains_all.json 37v.12)

- l.3 والقلم القمي غير الفهلوي فالفهلوي
- l.4 **[chaîne « pahlavi »]**
- l.5 والقمي حسبه اكثر الناس الفهلوي وليس كذلك وهو
- l.6 **[chaîne « qummī »]**
- l.7 سقط منه الظا يكتفى عنها بالضاد فليقرا البيتين من / l.8 يفهمه …

## Chaîne l.4 (« pahlavi »), lettre par lettre, de droite à gauche

Groupes (espaces = blancs du copiste) ; {x} = lecture probable ; x/y = variante.

1. ق{د} — ق : deux points en colonne au-dessus ; Daniel lit ن (un point). Variante ن/ف.
2. ضح — boucle de ṣād avec un point = ض ; suivi d'une queue ح/ج/خ (point non vu) → ح.
3. زحو — ز (un point) ح و.
4. شكا{ث}ه — ش (trois points) ك ا ; puis trois points au-dessus d'une dent → ث (Daniel ش) ; ه final.
5. مذ — م ذ (point).
6. سخطت — س خ (point) ط ت (deux points). Variante سحطت.
7. غصن — غ (point) ص ن (point).
8. على — ع ل ى (le point sous la ligne est probablement celui d'un ي).
9. لا — lām-alif.
10. اقط — ا ق (deux points) ط.

Chaîne normalisée (lettres seules) : ق د ض ح ز ح و ش ك ا ث ه م ذ س خ ط ت غ ص ن ع ل ي ل ا ا ق ط (29 lettres).
Lettres distinctes (23) : ا ث ح خ د ذ ز س ش ص ض ط ع غ ق ك ل م ن ه و ي ت.
Absentes : ب ج ر ف ظ.

## Chaîne l.6 (« qummī »), de droite à gauche

1. كمر — ك م ر.
2. او — ا و.
3. حيط — ح ي (deux points dessous) ط.
4. صلاله — ص ل ا ل ه.
5. در — د ر (pas de point visible ; variante دز).
6. سع — س ع.
7. {تي} — dent avec deux points dessus, ى final avec deux points dessous ; Daniel يغي. Variante ثي/ني.
8. برخش — ب (point dessous) ر خ (point) ش (trois points).
9. غض — غ (point) ض (point).
10. ثج — trois points sur une dent + ج (point dessous) ; Daniel نج.
11. {تذ} — dent à deux points + د/ذ (un point au-dessus) ; Daniel تدنو. Variante ثد.
12. {ق} — finale à boucle et longue queue, deux points déplacés à gauche ; variante ف (un point au-dessus de la boucle) ou نو (Daniel).

Chaîne normalisée : ك م ر ا و ح ي ط ص ل ا ل ه د ر س ع ت ي ب ر خ ش غ ض ث ج ت ذ ق (30 lettres).
Lettres distinctes (24) : ا ب ت ث ج ح خ د ذ ر س ش ص ض ط ع غ ق ك ل م ه و ي.
Absentes : ز ف ن ظ. Le copiste dit « le ẓāʾ en est absent » : ظ manque bien ; ز, ف, ن manquent aussi
dans ma lecture (ou sont cachés sous les variantes در→دز, ق→ف, ثج/تذ→نج/نو).

## 38r l.8-11 : les deux vers (« argot »), relus à 3×

Ma relecture concorde avec `plaintext_record` de Daniel (keys_eye/37v.12.json) mot pour mot :
ركشذ زوهشو ثول هفهل سزاور هنف / اغوس ففع [trou de ver] طخهنخف? ابغرا و سهنف /
اوغطفذ نفد ف كبيذ غون زو شهنف / هوخف ومخ اهو ويزاهو وهنف.
Sur la page, طخفخف se lit bien ط خ ف خ ف (trois dents pointées), comme Daniel l'a corrigé ; « ويزاهو » porte
deux points puis un point sous les dents, compatible avec وبيذ اهو (correction de Daniel par le chiffre).
Je ne propose aucune correction nouvelle. Texte retenu pour la mesure (c) : le clair corrigé par Daniel
(`plaintext` de keys_eye/37v.12.json, 90 lettres, 23 mots), gelé dans `donnees/cant_90.txt`.
