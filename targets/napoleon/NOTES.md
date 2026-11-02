# Two Napoleonic cryptograms: Berthier to Napoleon (1812), and the letter to Marmont (1807)

Both are on Tomokiyo's unsolved list. Both come from a single source: J. Vilcoq, "Le Chiffre sous le
Premier Empire", *Revue Historique de l'Armée* no. 4 (1969). The task was to try the printed-edition
route — the same route that has turned several items on these lists from unsolved into solved.

**Result: neither is solved, and neither can be attacked as it stands. But the Berthier item has
moved a long way, and the reason each is blocked is now exact.**

---

## Berthier to Napoleon, 22 December 1812

### What is published

Tomokiyo prints the opening of the cryptogram: **325 code groups**, then "....". The letter carries
an archivist's note, *"Duplicata, Chiffre du Prince de Neufchâtel, La Primata a été déchiffrée"* — a
duplicate copy, in Berthier's own cipher, whose first copy had already been deciphered.

**A transcription discrepancy in the source.** Cryptiana prints this cryptogram on two pages, and
they disagree. In line 4, `unsolved.htm` has `… 844 1238 356 69 823 …` where `napoleon2.htm` has
`… 844 1238 656 69 823 …`. `unsolved.htm` carries 22 lines, `napoleon2.htm` only 7. Any future
decipherment has to resolve **356 vs 656** against Vilcoq. Recorded here because it is the kind of
thing that silently wrecks a known-plaintext alignment.

### Structure, and why it cannot be attacked

`python berthier.py`.

| | |
|---|---|
| code groups (printed portion) | 325 |
| distinct | 207 |
| **hapax** | **132 (64%)** |
| commonest code | 918 and 13, 8 times each — **2.5%** of tokens |
| range | 2–1388 |
| occupancy | near flat across 1–1199; only 3 groups above 1200 |

So the code book runs to about 1200 entries and is used across its whole span. With 64% of groups
occurring once against a book that size, there is no frequency signal to work with. This is not a
cipher that yields to analysis, and no amount of cleverness changes that.

Two repeated phrases exist and are worth recording for whoever gets the full text:
`918 1045 1100` twice, `168 854 1148` twice, and `821 791` three times.

### Where it lives, and where the plaintext is

This is the part that moved.

**Archive.** The Archives nationales répertoire of the Secrétairerie d'État war papers (N. Gotteri,
`FRAN_IR_003827`, AF/IV/1590–1670) places Berthier's reports to the Emperor for this date precisely:

> **AF/IV/1643, plaquette 1/VI.** "Lettres et rapports adressés à l'Empereur par le major général
> depuis Gumbinnen puis Koenigsberg, concernant la retraite de la Grande Armée : repli général sur
> les places de la Vistule ; pertes de l'artillerie et des bagages ; regroupement, réorganisation et
> positions des unités ; manque de fonds et de moyens de transport ; nominations et promotions ;
> malades et invalides ; poursuite de l'évacuation … ; mouvements du corps du maréchal Macdonald ;
> pression des troupes russes ; attitude de la Prusse. 17, 31 décembre 1812."

**Plaintext.** Arthur Chuquet, *1812, la guerre de Russie: notes et documents*, third series (1912),
section 45, pp. 165–219, prints Berthier's letters to Napoleon of 1–31 December 1812 **in clear**,
and states his source outright: *"tirées soit des archives de la guerre, soit des archives
nationales (A. F. iv. 1643)"* — the same carton. Two are dated 22 December 1812:

* **letter XIX**, a short letter proposing a pension for the widow of Colonel Bosset, who died at
  Smolensk (≈155 words)
* **letter XXIII**, sent at 9 in the evening, a long situation report (≈530 words): Lagrange taking
  command of Königsberg and Old Prussia, the collapse of the 34th division, battalion arrivals,
  Cossacks closing on Tilsit, Macdonald's retreat, what is left of the Guard at Insterburg, the
  impossibility of evacuating the siege artillery, and *"Nous n'avons jusqu'à ce moment qu'à nous
  louer des Prussiens."*

Letter XXIII tracks the inventory's topic list for that plaquette almost item by item, including the
attitude of Prussia, and its content is exactly what would justify encipherment a week before York's
defection at Tauroggen.

### What the printed extract can and cannot settle

Compared over the same 325 tokens:

| | ciphertext | Chuquet XXIII |
|---|---|---|
| distinct | 207 | 162 |
| hapax | 64% | 65% |
| commonest token | 2.5% | 7.4% |
| repeated bigrams | 16 | 29 |

The hapax rates agree closely. The distinct count and the peak frequency do not, in the direction
you would expect if the code gives its frequent words several alternative groups — which is normal
in a nomenclator of this size, and which Tomokiyo has separately shown for the related Berthier
cipher of May 1813, where *et* is 197, 413, 534 **and** 821. (Note that 821 occurs four times here,
three of them followed by 791.)

That is a consistency check, not an identification, and it is deliberately left there. With 325 code
groups and a free choice of plaintext, an alignment can always be manufactured; it would mean
nothing. **No alignment is proposed.**

### One further lead, not followed to the end

Tomokiyo notes that the cryptogram "may correspond to *votre note chiffrée*, which is acknowledged,
together with Berthier's letter of the 21st, in Napoleon's letter to Berthier dated 30 December
1812." If so, the item is a separate ciphered note rather than one of the ordinary letters Chuquet
printed, and Napoleon's reply may describe its subject. I could not retrieve that letter: the
Google Books API and the Internet Archive full-text search endpoint both refused requests from here.
It is in *Correspondance de Napoléon Ier* vol. 24 and should be quick for anyone who can reach it.

### The blocker, exactly

The plaintext has been in print since 1912. What is missing is **the rest of the ciphertext**, which
exists only in Vilcoq's 1969 article. *Revue Historique de l'Armée* no. 4 (1969) is not on Gallica,
not on the Internet Archive, and not on Google Books. It is a Service historique de la Défense
journal; a library copy or an SHD request is the route.

Get that article and this stops being a cipher problem. It becomes a known-plaintext alignment that
would recover a large part of the *chiffre du Prince de Neuchâtel* — which is itself worth more than
the one letter, because it is the predecessor of the chief-of-staff ciphers of 1813.

---

## Encoded letter to Marshal Marmont, 1807

**There is nothing to work on. The ciphertext is not published anywhere I can reach.**

Tomokiyo's entry gives only the opening line, which is in clear:

> "Vous avez du recevoir Monsieur le General Marmont mes lettres des 8. 14 et 20 courant"

and then says "the rest is wholly in code. The code consists of two-digit figures as well as
alphabetical letters and other symbols." **No code groups are printed** — not on the unsolved page,
not on his Napoleonic ciphers page. The only source is again Vilcoq 1969.

So unlike the Berthier item, this one cannot be advanced by any amount of analysis or of
printed-edition work: there is no cryptogram in hand. Stating that plainly is the honest outcome.

What can be recorded for when the text is obtained:

* **The system is small.** Two-digit figures mixed with plain letters and symbols. Tomokiyo notes
  Marmont used a code of only about 150 entries in 1811, and infers this would not be complex. A
  message of any length in a 150-entry system with letters mixed in is a realistic target, unlike
  the 1200-entry Berthier code.
* **Where the papers are.** Marmont commanded in Dalmatia in 1807. Per the Archives nationales
  répertoire, the series "Armée de Dalmatie et Provinces Illyriennes, lettres du vice-roi et du
  général Marmont, 1806–1814" was transferred out of AF/IV to the dépôt de la Guerre on 5 October
  1830. So Marmont's 1807 correspondence is at the **Service historique de la Défense**, not the
  Archives nationales — which is consistent with Vilcoq, an army journal author, having had it.
* **Printed route.** Marmont's *Mémoires du duc de Raguse* (9 vols) print many letters of the
  Dalmatian command and are the place to look for the plaintext once a date and a sender are fixed.
  The opening line says the writer had written on the 8th, 14th and 20th of the same month, which
  will date it tightly once the month is known.

---

## Summary

| | Berthier 1812 | Marmont 1807 |
|---|---|---|
| ciphertext available | opening only, 325 groups, with a variant reading | **none** |
| plaintext located | **yes — Chuquet 1912, from the same carton** | not attempted, no ciphertext |
| archive identified | AF/IV/1643 plaquette 1/VI | SHD (ex-dépôt de la Guerre) |
| attackable by analysis | no — 64% hapax against ~1200 entries | unknown, but likely yes if obtained |
| blocker | Vilcoq 1969 for the full ciphertext | Vilcoq 1969 for any ciphertext |

Both reduce to one 1969 journal article. That is a better place to be than "unsolved", and it is a
concrete errand rather than a research problem.

### Files

| file | what it does |
|---|---|
| `berthier_ct.txt` | the 325 printed code groups, as cryptiana's fuller page gives them |
| `berthier_chuquet.txt` | Chuquet's December 1812 Berthier letters, extracted from the 1912 text |
| `berthier.py` | structure of the cryptogram, and the compatibility check against the printed letters |
| `an_ir.pdf` / `an_ir.txt` | the Archives nationales répertoire for AF/IV/1590–1670 |
| `napoleon2.txt` | Tomokiyo's survey of Napoleonic ciphers, source of the variant reading |

## Berthier 1812 read with the Great Cipher of 1812: a letter of King Joseph (Brice Dudout, 12 Oct 2026; added 29 Oct 2026)

The 325 groups read with the deciphering table of the Great Cipher of 1812 (SHD "B n° 30", photographed by J.-F. Bouchaudy).
The text is French, written in Spain by a king to the Emperor (Reille's dispatch enclosed, the Army of the North, the
Salamanca dispatches): King Joseph, not Berthier; Joseph's letter to the Minister of War of 23 Dec 1812 (Du Casse IX) covers
the same matter. Ilia Chirtulov found key and writer first (reported by Tomokiyo on Cryptiana, 12 Oct 2026); ours is an
independent re-reading: 8 groups corrected on Vilcoq's plate (the plate reads 356, the sense requires 656), permutation
control 0/1,000, 233 of 233 words read in their sense (225 certain, 3 probable, 5 restored). See `dudout/README.md`.
