# Reproducing the T-S 13J18.19 tests

The [research note](../../docs/ibnezra1139.html) sets out the working transcription and its uncertainties. With Python 3.10 or later, download the [PGP transcription archive at the tested revision](https://github.com/princetongenizalab/pgp-text/archive/bdab37ed37dbc63e2b6de2117d1f11e076f65821.zip). From this directory run

```sh
python crib_check.py
python corpus_check.py /path/to/pgp-text.zip
python verso_first.py /path/to/pgp-text.zip
python verso_first.py /path/to/pgp-text.zip --last-is-eight
```

The scripts exclude PGP 9097, normalize Hebrew final letters and skip damaged tokens. The archive includes multiple languages and editions. A word match counts as a spelling parallel. The last two commands should print six and eight distinct verso phrases respectively, each with an empty list of complete matches on the front. The contextual checks require the first front word after an article and the second before כמא elsewhere in the archive.
