# PREREG — vaudreuil-aout-1760 (écrit et haché AVANT tout calcul, 23/11/2026)

## Objet
ANOM COL F3 16 ff. 115–119 (vues FRANOM82_247MIOM013_F3_016_187–195), Vaudreuil au ministre (Berryer), Montréal,
29 août 1760, lettre chiffrée avec déchiffrement d'époque interlinéaire (= EXISTING ; lead Bourdeau 1208 ; Parkman,
Montcalm and Wolfe II (1884) pp. 380–381 en traduit des passages). Question : est-elle dans la table Vaudreuil 1757
(ANOM C11E 10, LAC e001295274), déjà validée sur la lettre du 8/5/1759 (vaudreuil-1759) ?

## Clé (gelée, non modifiée)
cle/KEY_v2.tsv = ../vaudreuil-1759/cle/KEY_v2.tsv, SHA-256 7b5aecb24dd0325f3fc59a56f90c6d12ba75e7107d8e97c8acd3107f5d8f6be6
(v1 + 20 corrections du 04/11, toutes antérieures et étrangères à cette lettre). Colonne « valeur » ; « ? » et vide =
vide ; si plusieurs valeurs « / », la première.

## Portion mesurée
Les DEUX premières pages chiffrées : f. 115 r° et v° (vues 187 et 188), entières. Le reste de la lettre (vues 189–195)
n'est pas mesuré (lu par la glose). Regards déclarés : vue 187 vue en vignette le 23/11 par l'agent de récolte (C08)
et décrite dans PROVENANCE.md ; aucun décodage fait. Transcription après ce PREREG et avant calcul :
validation/chiffre.txt et validation/glose.txt, gelées par SHA-256 (validation/SHA256.txt).

## Mesure (une seule) — identique à vaudreuil-1759
- Décodage nombre → valeur ; mots en clair du chiffré conservés ; groupes illisibles « ? » ignorés.
- Normalisation : minuscules, accents ôtés, lettres a-z.
- Accord = difflib.SequenceMatcher(None, décodé, glose, autojunk=False).ratio() sur la portion.
- Témoins : 200 permutations des valeurs sur les nombres, random.Random(20261123).
- Critère : TABLE CONFIRMÉE si accord ≥ 0,85 ET ≥ meilleur témoin + 0,30 ; < 300 lettres → non mesurable.
- Accord en mots rapporté, non décisif. Portion mesurée = grillée.
