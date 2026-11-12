"""POST HOC (not declared as the verdict): the same measure and keys as score_0178.py, truth = the clerk's full Explication on
frame 0179 (tests/explication_0179_transcribed.txt), which includes the paragraph ASP omits. Run after the declared result was known."""
from pathlib import Path
import json, importlib.util
OUT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('s', OUT / 'scripts/score_0178.py'); s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
t = '\n'.join(l for l in (OUT / 'tests/explication_0179_transcribed.txt').read_text().splitlines() if not l.startswith('#'))
res = s.main(t, label='0179 Explication, full (post hoc)')
(OUT / 'tests/0178_result_0179_posthoc.json').write_text(json.dumps(res, indent=1) + '\n')
