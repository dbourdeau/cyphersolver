# Vorarlberger Landesarchiv findbuch by script (16 Nov 2026): search POST, result list POST with keys, detail GET
# 1) POST php/rech_start.php?rech_nr=1  words=<term>&pics_only=false&op=and&truncate=false&signature=false&kind=&id=&name=&max=100&tab=&von_t=&von_m=&von_j=&bis_t=&bis_m=&bis_j=&complete=true&complete_date=true
#    -> JSON result_list with keys
# 2) POST php/rechergs.php?nr=1&switch_state=0  id=1_c_-1&content=<keys joined by ~>  -> open_rechdet('',ve_id,be_id,'ve_e')
# 3) GET  php/props.php?kind=ve_e&ve_id=<ve_id>&be_id=<be_id>&pag=-1&show_close=1&high=<term>  -> JSON .xml (full regest)
# keep one cookie jar across the three calls
