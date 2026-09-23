# lang/ — shared language models

Every target used to build its own character n-gram model: about 25 `lm.py` / `build_lm.py` scripts, each with its own
normaliser and smoothing, several reaching into another target's folder for its corpus (`../beale/lmcorpus`,
`../bethune/xivrey`, `../adfgvx/corpus`). This directory replaces that with one registry and one engine. New targets
should start here; the old per-folder scripts stay where they are so past results reproduce exactly.

| file | what it is |
|---|---|
| `sources.json` | every corpus: language, period, genre, and how to get it (Gutenberg ids, Internet Archive ids, URLs, or files a target already downloaded) |
| `models.json` | every model: which sources, which normalisation, order, spaces or not, what it is for, which old scripts it replaces |
| `lm.py` | normaliser, the two engines (`DenseLM` numpy, order ≤ 5; `SparseLM` dict, order 6–8), `load()` and `best_language()` |
| `corpora.py` | fetches a source into `lang/corpora/<id>.txt` |
| `corpora/`, `cache/` | fetched text and built tables; git-ignored, rebuilt on demand |

## Using it from a target

```python
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lang import lm

m = lm.load('fr-1600-letters')           # first call fetches + builds (seconds), later calls load the cache
m.per_char(lm.norm(decrypt, 'early'))     # mean log-prob per char: real text ≈ -1.1 to -1.8, gibberish ≈ -6
x = m.encode(candidate); m.score_idx(x)   # int-array form for annealing inner loops
lm.best_language(decrypt)                 # [(score, model), ...] over the language-ID set
lm.load('it-modern', order=4, spaces=False)   # any order/spacing variant, cached separately
```

From the shell: `python -m lang.lm <model> "some text"` scores text; `python -m lang.corpora` lists sources and which
are cached; `python -m lang.lm <model> --rebuild` rebuilds.

## Normalisation schemes (`lm.norm`)

| scheme | rule | use for |
|---|---|---|
| `modern` | lowercase, accents stripped, a–z | anything after c. 1700; WW1/WW2 |
| `early` | as modern, plus j→i, v→u | 15th–17th-c. vernacular: the cipher clerks did not distinguish them |
| `latin` | as early, plus k→c, y→i, w→u | Latin |
| `enigma` | umlauts ae/oe/ue, ß→sz, ch/ck→q | German Enigma/Wehrmacht traffic |

Always normalise candidate plaintext with the same scheme as the model (`models.json` → `norm`).

## The models

| id | language, period | corpus | use for |
|---|---|---|---|
| `en-modern` | English 1600–1920 | 24 Gutenberg classics, 15 M | default English |
| `en-1640s` | English 1640–1700 | Carisbrooke histories + above | Civil War / Restoration |
| `fr-modern` | French 1700–1920 | 28 Gutenberg texts, 11 M | later French, language ID |
| `fr-1530-despatches` | French 1525–1600 | Du Bellay, Nevers, League letters + fr-modern | François I – Henri III despatches |
| `fr-1600-letters` | French 1570–1640 | Lettres missives de Henri IV, 7.9 M | default for 1570–1640 French |
| `fr-1650-rome` | French 1600–1670 | Guizot's Bordeaux despatches + Henri IV, order 7, no spaces | code-group work, mid-17th c. |
| `fr-grand-siecle` | French 1630–1700 | Sévigné, Retz, Pascal, Corneille, quadgram | literary 17th-c. French |
| `de-modern` | German 1780–1945 | Gutenberg, 3.2 M | ADFGVX, Abwehr, Orpo |
| `de-1500s` | German 1470–1610 | DTA prints 1472–1609 | 16th-c. chancery German |
| `de-1640s` | German 1600–1670 | DTA: Theatrum Europaeum I (1635), Olearius (1647), Simplicissimus (1669) + the 1470–1610 prints | Thirty Years' War letters (baner1640) |
| `de-enigma` | German 1930–1945 | same, Enigma conventions | Wehrmacht traffic |
| `nl-modern` | Dutch | Gutenberg | Thurloe, Abwehr |
| `es-modern` | Spanish | Gutenberg incl. Quijote, 6 M | default Spanish |
| `es-golden-age` | Spanish 1490–1650 | Quijote + Memorias (Villa) | Habsburg-era Spanish |
| `ca-modern` | Catalan | Gutenberg + Tirant lo Blanc | Crown of Aragon |
| `it-modern` | Italian 1800–1920 | Gutenberg, 9.4 M | default Italian |
| `it-cinquecento` | Italian 1490–1620 | Guicciardini/Machiavelli + Nuntiaturberichte, 31 M | Renaissance diplomatic Italian |
| `la` | Latin | 27 Gutenberg texts, 6.8 M | papal, imperial, humanist |
| `pt-`, `da-`, `sv-`, `pl-`, `hu-`, `cy-modern` | | ~1–6 M each | language ID, northern/eastern targets |

## Known gaps

- `fr-rome-1600s`: the 6.1 M-char Recueil des instructions … Rome t. II text that `chaulnes/lm.py` was trained on is no
  longer on disk in any checkout. `fr-1650-rome` is Guizot + Henri IV until it is re-fetched (then add an `ia`/`url`
  recipe to `sources.json` so it survives).
- `fr-1520s-diplomatic` and `fr-rome-1600s` have no remote recipe; they build only in a checkout that has the files.
  Corpora are found in this checkout, in `../cypher` (so worktrees see the main checkout's downloads), and in any
  directory listed in `CYPHER_CORPUS_ROOTS`.
- Not migrated, because they are not character n-gram models: `sunyatsen/` (Chinese word dictionary),
  `milroy/word_lm.json` and `bethune/lm.py`'s word model, `enigma/lm_build.py` (built from the bomm Enigma trigram
  tables).

## Adding a corpus or a model

1. Add the source to `sources.json`, with a remote recipe if one exists (so it rebuilds on a fresh clone) and a
   `local` glob if a target already holds the file.
2. Add the model to `models.json`: `language`, `period`, `norm`, `order`, `spaces`, `sources`, `use_for`, `replaces`.
   Set `"language_id": false` for period- or genre-specific models so `best_language()` compares one model per language.
3. `python -m lang.lm <id> "a sentence you expect to score well"` and a line of gibberish as the control.
