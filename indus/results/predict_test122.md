# Hundred-and-twenty-second registered predictions: the model as a predictor

- training lines 2177, test lines 545.

## GM1 the neighbour predicts the head
- accuracy 38.2% against 7.3% (commonest head); threshold +10 points.
- **GM1 holds.**

## GM2 the head predicts the ending
- accuracy 90.2% over 245 names; threshold 85%.
- **GM2 holds.**

## GM3 the head beats the opener
- head 90.2%, opener 82.4%; threshold +10 points.
- **GM3 fails.**

## GM4 the last sign tells the genre
- accuracy 76.7%; threshold 80%.
- **GM4 fails.**

## GM5 last beats first
- last 76.7%, first 43.8%; threshold +20 points.
- **GM5 holds.**

## GM6 the templates generalise
- test lines in the training top-10 templates: 260 of 545 (48%); threshold at least 45%.
- **GM6 holds.**

## GM7 order predicts
- unigram 8.21, bigram 6.38 bits per sign; threshold 1 bit gain.
- **GM7 holds.**

## GM8 longer context helps
- bigram 6.38, trigram 5.80; threshold 0.2 bit gain.
- **GM8 holds.**

## GM9 units generalise
- test bodies of 3+ with a training unit: 106 of 164 (65%); threshold at least 60%.
- **GM9 holds.**

## GM10 heads are a closed set
- test heads seen in training: 245 of 259 (95%); threshold at least 90%.
- **GM10 holds.**

## GM11 openers are mostly known
- test openers seen in training: 206 of 233 (88%); threshold at least 70%.
- **GM11 holds.**

## GM12 Mohenjo-daro heads predict Harappa endings
- accuracy 92.4% over 263 names; threshold 85%.
- **GM12 holds.**

## GM13 A heads predict B endings
- accuracy 93.4% over 302 names; threshold 85%.
- **GM13 holds.**

## GM14 the last sign tells the genre (B)
- accuracy 68.9%; threshold 80%.
- **GM14 fails.**

## GM15 order predicts (F')
- unigram 8.23, bigram 6.75; threshold 1 bit gain.
- **GM15 holds.**

## Summary

Held: GM1, GM2, GM5, GM6, GM7, GM8, GM9, GM10, GM11, GM12, GM13, GM15. Failed: GM3, GM4, GM14.
