"""Replay both blind transfers, calibration, alignment, and read share."""
from pathlib import Path
import argparse, csv, hashlib, shutil, subprocess, sys, tempfile

here=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--repository',type=Path,default=here.parents[1],help='upstream project root')
parser.add_argument('--work-dir',type=Path,default=here,help='writable workspace for temporary replay')
args=parser.parse_args()
repo=args.repository.resolve()
external={
    'targets/rubio1913/key.tsv':'77cb440bedac8e21df5109cae12528867ea9f60d72d6aee358c2bf66fdb9302d',
    'targets/rubio1913/transcription.txt':'f41fb6342baf1882e29ad1119a709b1eab0af574d9d9645a766beb098e406732',
    'targets/esp318/lit/quijote.txt':'27f5064a245209b6d83f7d95e51b2cb6a15ebec02b2518c80cbc1d2cd036429e',
}
for name,digest in external.items():
    f=repo/name
    if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=digest:
        parser.error(f'Expected original source absent or changed: {f}')
if not args.work_dir.is_dir():
    parser.error(f'Workspace directory missing: {args.work_dir}')
def check(actual,gold):
    if actual!=gold.read_bytes():raise SystemExit(f'Replay differs: {gold.name}')
with tempfile.TemporaryDirectory(dir=args.work_dir,prefix='clave109-replay-') as tmp:
    root=Path(tmp).resolve();run=root/'batch18b'/'war_ministry';run.mkdir(parents=True)
    old=root/'crawford_rebase';old.mkdir();(old/'targets').symlink_to(repo/'targets',target_is_directory=True)
    for f in ['test.py','align.py','words.py']:shutil.copyfile(here/f,run/f)
    for d in ['read_one','read_two']:(run/d).symlink_to(here/d,target_is_directory=True)
    subprocess.run([sys.executable,'-I',str(run/'align.py')],check=True)
    for name in ['may19.runs','march25.runs','may19.alignment.tsv','march25.alignment.tsv']:
        check((run/name).read_bytes(),here/name)
    print('Both consensus alignments match byte for byte')
    for mode,name in [('calibrate','calibration.json'),('may19','may19.json'),('march25','march25.json')]:
        got=subprocess.check_output([sys.executable,'-I',str(run/'test.py'),mode])
        check(got,here/name)
        (run/name).write_bytes(got)
        print(f'{name} matches byte for byte')
    got=subprocess.check_output([sys.executable,'-I',str(run/'words.py')]);check(got,here/'may19_words.tsv')
    rows=tuple(csv.DictReader(got.decode().splitlines(),delimiter='\t'))
    if len(rows)!=25 or sum(r['status']=='sure' for r in rows)!=15:
        raise SystemExit('Word inventory mismatch')
    print('May 19 word inventory matches byte for byte: 15 sure of 25 provisionally segmented words')
