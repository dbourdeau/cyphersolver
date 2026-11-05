# Image screening of Z 44 A 9a Ic: Nr. 2 Bd. III–IV, Nr. 5, Nr. 6

Contributed by Jozef Krajčovič ([@kjfriedo](https://github.com/kjfriedo)) to issue [#128](https://github.com/dbourdeau/cyphersolver/issues/128). Licence: CC BY 4.0, with credit. The archival images remain © Landesarchiv Sachsen-Anhalt.

## File

`screening_catalogue597.csv` has one row per image. Its columns are `volume, image, url, sha256, result, note`.

- 463 data rows plus a header, 464 lines, 120,922 bytes.
- Rows per volume: Nr_2_Bd_III 16 (images 1–16), Nr_2_Bd_IV 34 (1–34), Nr_5 322 (1–322), Nr_6 90 (1–90), Nr_1_Bd_III 1 (image 80, the last row).
- SHA-256 of the CSV: `4dbcea51c24ab74e77e12485030595e5cfacbb47dde3719ec1067b68195bb15d`.
- The `sha256` column holds the hash of each image file as downloaded on 29 Oct 2026, at `default` size.

## Method

All images were downloaded at `default` size (1499 px wide), checked on contact sheets, and zoomed where anything looked doubtful. The search looked for passages in three things: the prince's symbol alphabet (Nr. 2 Bd. I, image 6), the signs of the slip key (Nr. 2 Bd. II, image 184), and the code numbers 10–70.

The counts include covers, blank versos and double-page shots. Beyond the last numbers the server returns only the "Digitalisat nicht verfügbar" card, and the closing covers are in the sequence.

## Result

None of the images has a passage in either key.

Three images looked like possible hits and are not ciphers. They are explained in the `note` column:
- Nr. 5/207: a French list of troops;
- Nr. 5/210: ordinary German script;
- Nr. 2 Bd. IV/19: sums in an account.

Nr. 1 Bd. III image 80 now loads at `default` size; `max` still returns HTTP 500. It is a verso with only the endorsement *Moravi ad Bohemos*, and the facing page is blank.

## Limits

The search used `default` images, not `max`. A single code word or sign inside a line of Kurrent could be missed, but a continuous passage could not. A negative result means that no letter using the keys was found in these images. It does not mean that no such letters were ever written.
