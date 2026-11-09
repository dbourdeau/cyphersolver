# PREREG — anker-christian-frederik-1811-1814 (Arkivverket RA-EA-5938), écrit le 09/11/2026 (agent Opus 5.5) AVANT toute transcription du chiffre de H

## État au moment de l'écriture
- Antériorité (09/11, gh api dbourdeau/cyphersolver, HEAD e0af29245b) : rien sur Anker / Christian Frederik / RA-EA-5938 dans
  catalogue.json, research/leads.json, targets/. Le balayage Arkivportalen de Daniel (research/sweep_2026-11_malta_nordic_baltic,
  02/11) conclut « No pre-1900 cipher letter » : ces unités lui ont échappé.
- Édition imprimée : C. J. Anker (éd.), *Christian Frederik og Carsten Anker's Brevveksling 1814 – samt Uddrag af deres Breve fra
  1801-13 og fra 1815-17* (Danmarks Breve, tekster.kb.dk, letters-002155169). Les passages chiffrés des lettres de 1814 y sont
  imprimés en clair (« [I Chifre] », « [Uden Chifre] »). Ex. : la dépêche chiffrée en code de 4 chiffres du 28/06/1814 (PDF 1814
  p. 42-48, duplicata p. 64-70) = lettre imprimée n° 21, en clair (vérifié : « Medens Hardenberg var hos mig i Formiddags »
  ↔ manuscrit « Madame 621303 … »). Je n'ai PAS lu les extraits 1801-13 de l'édition (seulement les lignes de date des 1814).
- Vu par moi : tout en vignettes 50 dpi ; à 110 dpi : 1811 p. 2, 4, 9, 10 ; 1814 p. 42, 50, 59, 64, 72 ; clés SK p. 4, 10, 11,
  39, 40, KN p. 4, 6, 7. 1811 p. 9 porte des gloses interlinéaires (déchiffrement d'époque) sur le haut de la page : je les ai
  entrevues à 110 dpi (quelques mots), d'où leur exclusion de H. 1811 p. 10 (chiffre à symboles, 2 colonnes, sans glose
  hormis quelques signes suscrits) : vu à 110 dpi, et les 3 premières lignes de la colonne droite à 250 dpi (coup d'œil sur
  l'inventaire des signes ; les premiers signes « M + ∝ » rappellent k-a-n de KN-06). 1811 p. 11-13 (clair danois, autre main ?)
  non lues (vignettes seules). 1814 p. 59 (« fr. 28 Junii 1814 », symboles mêlés de clair) vue à 220 dpi, haut de page.

## Clé mesurée K (une seule)
K = fiche au crayon KN-06 (« Kodenøkler », G/L0230/0005, PDF p. 6), transcrite dans `KEY-KN06.tsv`,
SHA-256 a5e419c6c4730d811785c93e270ee9b26adf28642a4fb10c0496f32ac6fcb371, gelée AVANT ce PREREG. Aucune valeur ne sera
ajoutée ni corrigée avant la mesure. Signes absents de K → « ? ».

## Partie tenue à l'écart H
**H = 1811 PDF p. 10, colonne de droite, lignes chiffrées 1 à 8 (comptées du haut de la colonne), en ordre de lecture.**
- Transcription signe à signe sur recadrages à ≥ 400 dpi, étiquettes = codes de `KEY-KN06.tsv` pour les signes de K
  (a, b, … AA, NORGE, JEG), `S1`, `S2`… pour tout autre signe (décrit dans `SIGNES.md`), `|` = séparation de mots visible
  dans le manuscrit, `:` `;` `,` `.` ponctuation, `[?]` signe illisible.
- Gel : `H-CHIFFRE.txt` + `H-CHIFFRE.sha256` AVANT toute lecture d'un clair possible de cette lettre (1811 p. 11-13, extraits
  1801-13 de l'édition imprimée) et avant tout décodage par script.
- Limite connue : je transcris avec la clé sous les yeux (étiquettes = lettres de K) ; un biais de lecture vers des mots
  danois est possible. Les témoins (permutations de K) ne corrigent pas ce biais ; je le signalerai.

## Décision d'appariement (fixée ici, prise APRÈS le gel de H, AVANT tout calcul)
Je lis ensuite 1811 p. 11-13 et les « Uddrag 1801-13 » de l'édition. Un clair est « le clair de la lettre chiffrée » si :
(a) c'est un texte danois de la même unité (1811) ou de l'édition, (b) daté du même jour que la lettre chiffrée (± 3 jours)
ou explicitement donné comme sa copie/son déchiffrement, (c) d'au moins 150 mots.
- **Route A (apparié)** : car = meilleure correspondance locale (Smith-Waterman, +1 égalité, −1 inégalité, −1 trou) entre le
  décodage de H (lettres seules, normalisées : minuscules, aa/å → a+a, æ ø gardés, j→i, w→v, signes « ? » = joker
  non concordant) et le clair entier normalisé de même ; car = Σ égalités alignées / nombre de lettres décodées de H.
- **Route B (non apparié)** : M = part des mots décodés de H d'au moins 3 lettres (séparations du manuscrit) présents dans
  un lexique danois bâti par script sur les SEULES lettres datées 1814 de l'édition (en-tête de date en 1814), mêmes
  normalisations ; un mot contenant « ? » compte comme absent.

## Mesure (une seule)
- 200 témoins : permutations aléatoires des valeurs de K entre les codes de K présents dans H (graine 1811) ; même
  calcul (A ou B) ; marge = score − max(témoins).
- Seuils habituels : Route A : car ≥ 0,85 ET marge ≥ 0,30 → VALIDÉ. Route B : M ≥ 0,60 ET marge ≥ 0,30 → VALIDÉ.
  Marge ≥ 0,30 seule → PARTIEL ; sinon ÉCHEC. Accord en mots rapporté, non décisif. Pas de seconde mesure (H grillée).

## Ensuite
- Cible de lecture = lettre(s) à symboles sans clair connu dont K rend compte : 1811 p. 9-10 si aucun clair n'existe
  (route B), sinon 1814 p. 59 (« fr. 28 Junii 1814 ») si K s'y applique et si l'édition ne l'imprime pas.
- Si VALIDÉ/PARTIEL : lecture au sens au compte de Daniel (sûrs / probables {x} / restitués [x] / irrésolus ‹…› ; seuil 95 %
  sans restitués), puis PR-PREP.md (statut exact, crédit Arkivverket/Riksarkivet ; licence des images vérifiée, sinon aucune
  image). Aucune PR, aucun envoi.
