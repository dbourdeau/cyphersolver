"""Series-limited harvest (sps.recordSeries) for Barbary/Africa series. Appends to raw.jsonl via harvest.run"""
import sys
from harvest import run
SERIES = ["SP 71","SP 72","SP 73","SP 74","SP 75","SP 102","SP 103","SP 99","FO 2","FO 3","FO 8","FO 27","FO 84","FO 93","FO 97","FO 99","FO 101","FO 107","FO 108","FO 160","FO 195","FO 1","FO 4","FO 6","FO 7","FO 63","FO 64","FO 65","FO 83","FO 78","FO 76","FO 633","CO 96","CO 267","CO 179","CO 48","CO 49","CO 291","CO 82","CO 98","CO 87","CO 700","T 70","T 1","WO 1","WO 32","WO 33","WO 106","WO 108","WO 135","WO 78","WO 147","CO 4","CO 5","CO 391","CO 217","CO 806","CO 1","CO 2","CO 3","CO 879","CO 537","CO 533","CO 536","CO 525","CO 521","CO 468","CO 520","CO 444","CO 445","CO 446","CO 417","CO 427","CO 460","CO 465","CO 466","CO 468","CO 859","CO 850","CO 855"]
TERMS = ["cipher","cypher","decipher","decypher"]
for s in SERIES:
    for t in TERMS:
        run(t, extra={"sps.recordSeries": s})
