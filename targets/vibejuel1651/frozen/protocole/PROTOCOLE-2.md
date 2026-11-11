# PROTOCOLE 2 — Vibe → Juel (n° 2527) — rédigé et gelé AVANT la mesure 2 (11/11/2026, agent Opus)

Contexte : la mesure 1 (PROTOCOLE.md) a échoué (ESSAI-OPUS.md) parce que la table d'ouvreurs varie d'une lettre à l'autre (N. 330).
Hypothèse testée ici : « chaque mot = ouvreur + corps, corps = rang + k (alphabet 23 lettres, 32-34 = 1-3), k fixé par l'ouvreur
selon une table PROPRE À CHAQUE LETTRE ». La table n'est pas donnée : elle est apprise sur la lettre elle-même (k ∈ −4…4 par valeur
d'ouvreur, maximum de vraisemblance du modèle de langue) — les contrôles subissent EXACTEMENT la même optimisation.

- Script : scripts/mesure2.py (gelé), modèle scripts/lm.py + corpus/ (inchangés, SHA dans PROTOCOLE.sha256).
- Calibrage sur données déjà vues (img 78 + réserve 1) : M1 −2,442 ; contrôles max −3,685 (marge 1,24).
- RÉSERVE 2 (jamais ouverte par moi) : images 81, 83, 84, 87 de l'unité 261583, une unité de mesure par image ; si < 300 nombres,
  ajout des images 90 puis 91. Transcription chiffre par chiffre AVANT tout déchiffrement, gelée (RESERVE-2.sha256), puis UNE exécution :
  `python3 scripts/mesure2.py corpus working/transcr/r2_081.txt … > protocole/MESURE-2.out`.
- Critères : C1 M1 ≥ max(300 contrôles C, D, E) + 0,30 ; S : le déchiffrement de la réserve 2 donne au moins deux phrases danoises
  suivies lisibles. VALIDÉ si C1 et S ; sinon ÉCHEC (ESSAI-OPUS.md complété).
- Décompte de lecture inchangé (règle de Daniel, restitués exclus).
