#!/bin/sh
# after run_g: England, Poland, France/Spain and unlabelled Barberini letter volumes, every 16th canvas
while pgrep -f run_g.sh >/dev/null; do sleep 20; done
for n in 8615 8616 8618 8625 8626 6563 6564 6565 6649 6650 6651 6652 6653 6654 8105 8106 8175 8178 8268 8404 8458 8463 8464 8483 8535 8536 8563 8578 8586 8600 7196 7198 7206 7211 7213 7220 7223 7234 7252 7289 7412 7428 7789 7801 7943 7962 8015 9289 9291 9292 9293 9294 9295 9296; do python3 man.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Barb.lat.$n || exit 1; python3 sheet.py /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a8 Barb.lat.$n --step 16 --from 8; done
