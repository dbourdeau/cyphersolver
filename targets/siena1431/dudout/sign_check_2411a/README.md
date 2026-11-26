# Siena, Concistoro 2308 no. 24 (DECODE R4812 P2): the merged "t" sign, blind sheet 2411a (24 Nov 2026, Brice Dudout, with Claude)

Images: DECODE R4812 (private study; not republished). No image or crop is in this folder.

Our transcription (`../../project_attempt/no06_24all.tok`) uses one label, "t", for three signs of George Lasry's key
R4755: + (o), t with a curled foot (q), and the o+t ligature (f). There are 162 "t" places in all.

Brice Dudout looked at 12 places on line-sorted crops of R4812 P2. The sheet was blind, with no values. It had 9
targets and 3 controls (the o+t ligature, the t with a foot and a plain cross), and all 3 controls passed. The rule
was hashed before the thumbnails (`sheet-2411a-rule.md`, in French as hashed, SHA-256 1a4d06d9...). The key was opened
only after the answers were exported.

## Results (`sheet-2411a-results.tsv`)
- **Plain "+" (o) at 5 targets** (lines m.02-m.06). All fall either on letters the reading already has (con, di,
  vegno, posesa) or inside runs that stay unread.
- **"+o" (i), one sign: 3 places.** At m.03 "THETA t 0", m.03 "c 0 t 0" and m.05 "a t u", the cross carries a round
  attached to its right arm. This is the key's i-sign "+o" (column i of R4755), not "+" followed by o or a.
  - The first two were decided from the reader's remark. The third (m.05) was decided on the image, so it is
    **{probable}**: the reader was "not sure, the characters are often joined".
  - These give "sare' disposto" and "venire", as already read.
  - At m.03 "c 0 t 0" the unread run ‹adenanfaalag› becomes ‹adenanaialag›, which is still unread.
- **m.04, line end ("COLON t"):** a cross with two dots on its left arm, one sign (label COLPLUS). It is not on the key
  sheet, so no value is assigned.

New labels used in `no06_24all_2411a.tok`, which is a copy of the transcription with these 12 places relabelled:
- PLUS (+, o);
- TQ (t with a foot, q);
- OPLUS (o+t ligature, f; absorbs the 0 transcribed before it);
- IPLUS (+o, i; absorbs the 0/u transcribed after it);
- COLPLUS (no value).

`reading_no24_rev_2411a.txt` is the revised reading with the one changed run. The transcription and reading files of
the target are unchanged.

## Effect
Under the `understood` rule of `verify.py`: 1,815 of 2,279 decrypted letters understood (79.6%), **unchanged**. No word
of the reading changes, and no. 24 stays "decoded, not read". The hand does keep the forms apart, so the next useful
step is a sign-by-sign pass over the 162 "t" places, starting with those inside unread runs.

## Credit
- Reading and key: George Lasry.
- Reviewer (form check): Brice Dudout.
- Sheet built, scored and integrated by Claude (AI agent).
- Images: DECODE R4812.
