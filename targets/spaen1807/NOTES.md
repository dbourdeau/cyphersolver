# Van Spaen’s marked numerical cipher in Vienna, 1807

Status: in progress. The historical French readings survive for all four documents. The tests establish transfer of a partial key. The exact alignment of most groups and the extent of the underlying code remain open. [Cipher positions and historical readings](vienna_contribution/TABLES.md)

G. C. van Spaen sent cipher dispatches from Vienna in March 1807. Contemporary French decipherments survive in Nationaal Archief, Foreign Ministry, inventory 248. This contribution reconstructs part of the numerical key from No. 23, dated 21 March, and measures what it predicts in Nos. 26 and 21. Of the tokens predicted by the same fixed key, 32 of 43 matched within the registered position window in the letter of 28 March, and 48 of 61 matched in the letter of 14 March. The best of 1,000 shuffled tables scored 16 and 20 respectively. The clerks had already read these letters. The new result concerns the marked numbers and their reuse. [Originals](https://www.nationaalarchief.nl/onderzoeken/archief/2.01.08/invnr/248) · [Sign counts, predictions and controls](vienna_contribution/NOTES.md)

Cross-marked 293 for *guerre*, double-dotted 224 for *aussi* and double-dotted 723 for *cette* each matched at every opportunity in the two held-out dispatches. The table has 93 candidate entries in total, including fragments. These three examples have stronger evidence than most entries. The material also preserves a January miss and a correction to the attribution of numerical notes in inventory 204A. [Independent annotation readings](vienna_contribution/appendix/NOTES_working_copy.md)

There is a related repository target for correspondence from Düsseldorf in 1808. Removing the superscripts of the Vienna numbers yielded only two testable word placements over 61 agreed, unmarked positions of the Düsseldorf annex. The predeclared minimum was eight. Its unread companion received no key application. [Düsseldorf archive](https://www.nationaalarchief.nl/onderzoeken/archief/2.01.08/invnr/281) · [Existing target](../spaen1808/)

Run `python3 -I -B vienna_contribution/verify.py` from this directory. It reconstructs the key from two archived alignment paths, verifies the two prospective March tests and the January miss, and checks their control tables. [Reader guide](vienna_contribution/README.md)

AI agents did this work; no person has checked it.
