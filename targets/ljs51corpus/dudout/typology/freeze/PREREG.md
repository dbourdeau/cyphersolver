# PREREG — ljs51-typologie (28/11/2026)

Protocole complet : `gel/GRILLE.md` (grille v1) et `gel/CONSIGNE-CODEURS.md`. Rien n'a été codé avant ce gel.

- Hypothèse de travail (descriptive) : les 207 chiffres de LJS 51 se répartissent en familles de systèmes que l'on peut
  coder de façon reproductible à partir des seuls fichiers de Daniel Bourdeau (d8ac608093) ; la grille v1 est
  reproductible si deux codeurs aveugles obtiennent κ ≥ 0,80 sur chaque dimension B1-B7.
- Mesure unique : kappa de Cohen A–B sur les 30 unités de `data/echantillon_30.json` (graine 3030), `scripts/kappa.py`.
- Critère : κ ≥ 0,80 par dimension ; en dessous, dimension déclarée non fiable (pas de re-mesure rétroactive sur cet échantillon).
- Pas de témoins aléatoires (ce n'est pas un déchiffrement : la statistique est un accord inter-codeurs corrigé du hasard).
- Graine : 3030. Codeurs : deux sous-agents Sonnet indépendants, lancés après publication de l'empreinte.
