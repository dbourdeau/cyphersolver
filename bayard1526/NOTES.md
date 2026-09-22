# Gilbert Bayard (Toledo) to Anne de Montmorency, 5 Jan 1526 (BnF Clairambault 325 f. 84; DECODE R2285)

The three cipher lines are still unread. There is no key, and no decipherment on the page or in print.
Outcome: attempted, open (22 Sept 2026).

## Source

- BnF, Clairambault 325 ("Mémoires du règne de François Ier", 1525–1526), f. 84r–v, p. 9467 of the collection.
  Gallica ark `btv1b90006916` (338 unlabelled canvases). DECODE R2285 images IMG_R2285_I16203/I16204 (fetched
  with the saved cookie; git-ignored).
- This is a **seventeenth-century copy**, not the original. The margin says "V. 41. f. 4", which points to the
  source volume. The copyist drew the cipher signs by imitation.
- Heading: "Lettre de M. Bayard a M. le Mal de Montmorency", "5. Janvier 1526". Signed "Gilbert Bayard",
  "A Tollede le v.e jo. de Janvier". Gilbert Bayard was secretary of the King and élu of Bas-Auvergne. He was one
  of the French negotiators at Toledo/Madrid for the release of Francis I (Champollion-Figeac 1847). He was not a
  relative of the Chevalier Bayard, which is what Tomokiyo guessed.

## The cipher

The cipher sits in the middle of the letter, on page 1, lines 17–19. The context is: "...et qu'il y avoit neuf moys
que je n'avoye salué celuy de Ferrare a Calatheu [CIPHER] comme j'espere vous dire dimanche. A ce soir j'ay esté
devers led. viceroy...". The sign labels are in `ct.txt`: 56 signs of 29 kinds, including "n y" at the head of
line 2.

    L1 PHI s 7 L D Z XI R 7 n o b TH XI x n CM d k
    L2 n y TRI e F mm q DEL ph x D 7 XI CM e mm x F CM tri g 7 w ph g DEL F b x n gam e
    L3 D XI Z Pt w

(D = ∂, TH = θ, XI = ξ-like zigzag, CM = circled m, TRI = filled triangle, DEL/tri = open triangles,
F = barred I, mm = m with superscript m, ph = φ, gam = γ, w = ω, Pt = dagger with caret.)
29 kinds in 56 tokens means homophones or code signs. The signs come from the same pool as Raince's 1526
key and Calvimont's 1525/26 alphabet: 7, R, n, θ, x, Δ, ε, ω, and the "ny" and K signs, which are nulls in
Raince's key.

## Prior art

- Tomokiyo, "French Ciphers during the Reign of Francis I" (cryptiana, section BnF Clair.325): lists it as
  unsolved. A commented-out attempt in his page source aligns it with the marginal note; it does not fit.
- DECODE R2285: Non-decrypted.
- **Champollion-Figeac, *Captivité du roi François Ier* (1847), no. CCXVIII, pp. 462–463**, prints the whole letter
  from "copie de Bréquigny, vol. 91". His text runs "...qu'il y avoit neuf mois que j'avoye salué celui de Ferrare.
  A ce soir..." and **drops the cipher without comment**. It also sets the Clairambault marginal note ("J'ay
  respondu que je n'avoye veu icy nul homme de par vous") into the body text, where it belongs: it is an omitted
  line restored by the copyist, not a decipherment. Archive.org `bub_gb_DdUWAAAAQAAJ`.

## What was tried (22 Sept 2026)

1. The images were viewed and the cipher transcribed. The signs match Tomokiyo's crop.
2. Biermann's Calvimont key (same volume, f. 67), matching signs by shape (7=m, ∂=a/o, ς=e, b=t, Ŧ=d, ω=l,
   ξ=i). The anneal with these pins scores worse than an unpinned one and gives no sense. Ruled out.
3. Raince's 1526 key (Tomokiyo, re-measured in `raince/CALIBRATION.md`), dropping the "ny"/K nulls: −3.5
   per sign against −1.4 unpinned, gibberish. Ruled out: same sign pool, different values.
4. Ciphertext-only anneal (fr-1530-despatches 5-gram): free homophonic (`solve.py`) and homophones limited to
   common letters (`solve4.py`, 24 restarts). The best restarts share no text. The problem is underdetermined
   at 56 signs.
5. Print: Champollion-Figeac 1847 (above); BnF archives search for Bayard's originals (Fr. 2945 holds the 1525
   Toledo procès-verbaux, a copy). No decipherment found.

## Remaining gaps
- cipher passage, f. 84r ll. 17-19 (56 signs) - blocker: no-key-material; no key for Bayard's cipher on DECODE, in Tomokiyo or in print, and the Calvimont and Raince keys do not fit
- same passage - blocker: too-short; 56 signs of 29 kinds, which a ciphertext-only homophonic attack cannot settle

## Escalation
- [x] siblings: Clairambault 325 f. 67 (Calvimont, Biermann key) and Raince fr. 2984 checked; neither key fits
- [x] clear-pages: f. 84v is clear text (the letter continues); no decipherment on either image
- [x] known-keys: Calvimont 1525/26 (Biermann) and Raince 1526 (Tomokiyo) tried, both ruled out
- [x] print: Champollion-Figeac 1847 CCXVIII prints the letter and omits the cipher; Tomokiyo lists it as unsolved
- [x] key-rebuild: constrained and free homophonic anneals, no stable solution
- [n/a] retry: nothing reads, so there is nothing to retry

## What would move it

- The original letter ("V. 41 f. 4": probably a Béthune or Brienne volume). The original signs would be cleaner
  than the copyist's imitations, and a decipherment might be written on it.
- Another Bayard letter from the 1525–26 Spanish embassy in cipher, or Montmorency's key for Bayard.
