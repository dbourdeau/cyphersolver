"""Replay the frozen March test against a separate reading of the clear document."""
import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import calibrate

original_data = calibrate.source_data()
transcript = (HERE.parent / "plain_reader_two.txt").read_text().split("\n37r\n", 1)[1]
transcript = re.sub(r"^3[78][rv]$", "", transcript, flags=re.M)
starts = r"^(?=En lo de los cauallos|Significays nos|De las cosas de Sena|Vemos lo|En lo de las ~~)"
paragraphs = re.split(starts, transcript, flags=re.M)
assert len(paragraphs) == 6

def normalize(text):
    text = re.sub(r"~~.*?~~", "", text)
    text = text.replace(", inserted", "")
    for short, expanded in [("q̃","que"), ("Mᵗ","Magestad"), ("Antᵒ","Antonio"), ("vras","vuestras"), ("vra","vuestra")]:
        text = text.replace(short, expanded)
    return calibrate.norm(text)

second_reference = [normalize(p) for p in paragraphs]
base, groups, cipher, _, candidates = original_data
calibrate.source_data = lambda: (base, groups, cipher, second_reference, candidates)
calibrate.HERE = HERE
source = (HERE.parent / "assignments.tsv").read_bytes()
assert hashlib.sha256(source).hexdigest() == "96194a7090753441209671470f582981def06ea0617e34feceee3b1675adb5bc"
(HERE / "assignments.tsv").write_bytes(source)
calibrate.test()
