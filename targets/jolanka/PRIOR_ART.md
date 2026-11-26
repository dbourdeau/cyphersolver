# PRIOR_ART: jolanka postcard series (checked 24 Nov 2026)

Result: **no reading, key or cleartext found anywhere for this series**, as far as checked. Edited for filing on
26 Nov 2026 (working paths removed; findings unchanged), so this file differs from the stamped working copy.

## 1. DECODE records [measured]
- Public search `https://de-crypt.org/decrypt-web/RecordsList?search=jolanka&searchtype=` returns 121 rows: 120 named
  `..._jolanka-NN` (01 to 120) and one unrelated hit (R3235, Arad 1908). So the series is 120 cards.
- All 120 record pages fetched on 24 Nov 2026 (HTTP 200 x 120). Full enumeration, all 120:
  - Owner: Tobias Schrödel, 120 of 120. Created by: hedermisi (119 with the field filled).
  - Available Documents: empty, 120 of 120 (no Cleartext, Plaintext, Key or Decryption document). Sibling series in
    the same collection do carry "Cleartext" (e.g. R3258 Brühl), so the field is used when a reading exists.
  - Status: empty, 120 of 120. Inline Cleartext: No, 120. Inline Plaintext: No, 120. Cipher Type, Symbol Set: empty, 120.
  - Additional Information: "symbols adr" 117, "none adr" 2, empty 1.
  - Receiver: Tóth Jolánka at Jász Arokszálas 108 (four address forms), "Jászroksky" 2, Budapest 5 (István u. 5 three
    times, Petőfi u. 16 once, "helyben" once); Holecz Ferenc, Iskola utcza 37, Rákos Palota Újfalu 4; Tóth József,
    Újpest 1 (105+1+1+1+2+2+1+1+1+4+1 = 120 over the address forms). Sender field: "HU" 119, "Jasz HU" 1.
  - Private Ciphertext: True, 120. Access Mode: "Authentication required" 112, **"Public" 8** (R3524, 3525, 3526,
    3527, 3529, 3531, 3532, 3533).
- Image access: the 112 gated cards show "Insufficient permissions to so see the full image" to an ordinary DECODE
  account; their full images were not reached and no way round that was tried. The 8 Public records serve the full
  3445 x 2210 PNG with no login (IMAGE_ACCESS.md).

## 2. Cyphersolver [measured]
- Issues and pull requests (titles and bodies), catalogue, leads and targets: 0 hits for jolanka, Jolánka, Schrödel,
  Schrodel, cpc_, Arokszál, Holecz, R3524, RecordsView/35 (searched 24 Nov 2026).
- No `targets/` folder named jolanka on upstream main (checked 26 Nov 2026).

## 3. Literature and web [sourced]
- Tobias Schrödel, "Cryptographic postcards", HistoCrypt proceedings,
  https://ecp.ep.liu.se/index.php/histocrypt/article/view/166. Describes the collection; gives no reading of this set.
  Short quotes as returned by the fetch tool: "two large sets of 45 and 120 pieces"; "165 of the Hungarian cards are
  part of only two sets"; "For 76 cards, the plaintext is known." The paper does not say which cards those 76 are.
  120 + 45 = 165, so the two Hungarian sets are this one and the 45-card set (szomolya). The paper's table lists 71
  cards as simple substitution, fewer than 120, so this set is not among the solved ones on the paper's own numbers
  [derived, not stated by the author].
- Web searches (4): "Tóth Jolánka Jászárokszállás verschlüsselte Postkarten Schrödel"; Schmeh + Hungarian + Jolanka;
  Schrödel "Cryptographic postcards" Hungarian set; "Tóth Jolánka" titkosírás képeslap. No page about this series.
  Klaus Schmeh's blog posts returned are about other cards (German, Austrian, US).
- Not searched: Schrödel's own books and talks, Hungarian philately forums behind logins, HathiTrust and Google Books
  full text [unverified].

## 4. Risk that a reading exists unpublished
The owner has solved other sets in his collection and may hold a private solution. Nothing public says so. Malcolm
McBratney wrote to Tobias Schrödel about the key from the public cards; his reply of 25 Nov 2026 agreed to the work
going on GitHub [stated, Malcolm's correspondence]. Whether he holds a reading of this set is not recorded here.
