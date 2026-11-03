"""usage: chain.py SRC_SESSION DST_SESSION [budget]  -- new session whose start key is SRC's final key (fresh budget); truth/heldout copied"""
import json, os, shutil, sys
src, dst = sys.argv[1], sys.argv[2]; b = int(sys.argv[3]) if len(sys.argv) > 3 else 25
st = json.load(open(os.path.join(src, 'state.json'), encoding='utf-8'))
os.makedirs(dst, exist_ok=True)
for f in ('truth.json', 'heldout.json'):
    if os.path.exists(os.path.join(src, f)): shutil.copy(os.path.join(src, f), dst)
st.update(budget=b, spent=0, history=[], start_key=dict(st['key']))
json.dump(st, open(os.path.join(dst, 'state.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('chained', src, '->', dst)
