# ADDENDUM 2 au PREREG code 1-246 — figé AVANT le run Fable (lot 13) et avant d'en voir la moindre sortie — 14/11/2026
Base : PREREG-CODE246.md (SHA 06ffce5f…) + ADDENDUM-1 (SHA e0873adf…, référence de H = gloses G05-G20 de 113 d.).
Contexte : les gloses G01-G18 lues par les sous-agents Opus sont surtout ‹…› ; la resubstitution échoue faute de texte de
référence lisible. Accord de Brice (14/11, « Bonde ok fable ») pour une lecture paléographique de G01-G20 par Fable 5.2
(paquet PISTES-AUTO/fable-api/lots/lot13/bonde-gloss/ : 15 crops d'image + consigne, AUCUN nombre transcrit, ni H-secret/,
ni clé brouillon, ni décodage, ni nos lectures antérieures des gloses). Les crops montrent les nombres (la glose est
écrite entre les lignes chiffrées), y compris ceux des lignes 19-20 de H : Fable ne doit lire que la glose ; tout nombre
présent dans sa sortie est ignoré sans être lu. L'agent principal (constructeur de clé) N'OUVRE PAS gloss_G19-20_*.jpg
ni overview_113R_lines01-20.jpg (nombres de H visibles) ; seuls Fable et le vérificateur de l'étape 2 les voient.

## Règle : la sortie de Fable ne devient la référence de la mesure unique sur H qu'après une 2ᵉ vérification indépendante
1. À réception, la sortie de Fable (GLOSS-113R-G01-G20.tsv + RAPPORT.md) est copiée dans code246-1411/fable-lot13/ et figée
   par SHA-256 AVANT tout usage.
2. Vérification indépendante (l'une des deux, fixée maintenant) :
   a. **Relecture aveugle Opus** par un sous-agent qui n'a vu ni la sortie de Fable en clair ni nos lectures antérieures,
      ni la clé, ni H-secret/ : pour CHAQUE lettre que Fable marque {x|y} ou ‹…› dans G05-G20, et pour un échantillon
      de 10 % de ses lettres « sûres » de G05-G20 (tirage graine 1676200), une vignette (le signe encadré + 2 lettres de
      contexte de chaque côté, masquées ou non selon la consigne « relecture aveugle ciblée ») avec, en ordre aléatoire,
      les options de Fable + « autre » + « illisible ». Le vérificateur ne voit pas l'ordre de préférence de Fable.
   b. **Planche de Brice** au même format (formes de signes, un signe encadré par question) ; si Brice la remplit,
      ses choix priment sur 2a.
3. Arbitrage (fixé maintenant) : lettre retenue = choix du vérificateur s'il coïncide avec une des options de Fable ;
   s'il choisit « autre », « illisible » ou contredit Fable, la lettre devient « # » (ne s'apparie à rien : compte
   CONTRE A, choix conservateur). ‹…› non résolus → « # » × estimation de Fable.
4. Garde-fou : si le désaccord sur l'échantillon de lettres « sûres » dépasse 10 %, la lecture Fable est REJETÉE comme
   référence (pas de mesure) jusqu'à une planche de Brice sur toute la référence.
5. Si la référence G05-G20 ainsi établie compte < 300 lettres hors « # », la mesure est IMPOSSIBLE (pas de repli).
6. Le texte de référence final (G05-G20 concaténées, normalisées comme mesure-1411/metric.py : minuscules, w=v, j=i,
   a-z å ä ö, « # » conservé) est figé par SHA-256 AVANT le gel de la clé et AVANT tout décodage de H.

## Inchangé
- Nombres de H = H_final.tsv (SHA d428dfd3…e391), jamais ouverts (colonne 2) par l'agent principal avant le gel de la clé.
- Clé construite sur l'apprentissage seulement (ADDENDUM-1), gelée par SHA avant le décodage de H.
- Préalable : resubstitution sur l'apprentissage ≥ 0,85 (règle de PREREG-FABLE-LOT5), sinon pas de mesure.
- Métrique : A = 1 − distance d'édition semi-globale / longueur décodée ; longueur décodée ≥ 0,8 × 301.
- Seuils : SUCCÈS si A ≥ 0,85 ET A ≥ max(témoins) + 0,30. Témoins : 200 clés mélangées, valeurs permutées À
  L'INTÉRIEUR des classes (lettres entre elles ; nulles conservées ; mots-codes entre eux s'il y en a), graines
  1676000-1676199. Une seule mesure ; H grillée ensuite.
