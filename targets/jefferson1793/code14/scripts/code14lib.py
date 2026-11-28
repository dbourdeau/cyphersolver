"""Shared code for the Code No. 14 key build and held-out test (output/code14_2026-11-28)."""
import csv, re
def load_groups(path='transcription/code14_groups.tsv'):
    return [(int(r['pos']), r['group'], r['part']) for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t')]
def clean(num):
    """number, or None if a digit is doubtful"""
    return num if re.fullmatch(r'\d+', num) else None
def words_of(text):
    return [re.sub(r'[^a-z]', '', w.lower()) for w in text.split() if re.sub(r'[^a-z]', '', w.lower())]
def crib():
    return [l for l in open('plaintext/taylor_decipherment.txt', encoding='utf-8') if not l.startswith('#')][0]
