"""Read share of the cipher reading, the repository's way, two ways.

Uses research/reading_audit/v10_relabel.share (the function behind the read bar: holes counted by words after
research/reading_audit/v2_score.holes; every [?word], supplied [word] and word(?) is not read) on reading_fr.txt:

  strict            as written: words resting on an inferred value ([?word]), emended words (word(?)) and supplied
                    words ([word]) are all unread
  inferred accepted the 14 inferred values taken as right: [?word] -> word; emended and supplied words stay unread
  all accepted      also the emendations taken as right: word(?) -> word; supplied words stay unread

Writes results/read_share.json.   python measure_read_share.py   (from anywhere inside the repository checkout)
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
import v10_relabel as v10  # noqa: E402


def measure(text):
    words, holes, doubtful = v10.share(text)
    return {'words': words, 'holes': holes, 'doubtful': doubtful,
            'read_share': round(1 - (holes + doubtful) / (words + holes), 3)}


def main():
    text = (HERE / 'reading_fr.txt').read_text(encoding='utf-8')
    accepted = re.sub(r'\[\?([^\]]+)\]', r'\1', text)
    all_acc = accepted.replace('(?)', '')
    res = {'file': 'reading_fr.txt', 'unit': 'words of the cipher passages only',
           'strict': measure(text), 'inferred_accepted': measure(accepted), 'all_accepted': measure(all_acc)}
    (HERE / 'results').mkdir(exist_ok=True)
    (HERE / 'results' / 'read_share.json').write_text(json.dumps(res, indent=1) + '\n', encoding='utf-8')
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
