import re
from collections import Counter
import json

#You will need the supply a text file containing one name per line.
#A sample one can be downloaded from  https://raw.githubusercontent.com/junosuarez/dinosaurs/master/dinosaurs.csv
with open("dinosaurs.csv") as f:
    txt = f.read()
unique_letters = set(txt)


chain = {}
for l in unique_letters:
    next_chars = []
    try:
        for m in re.finditer(l, txt):
             start_idx = m.start()
             if start_idx+1 < len(txt):
                next_chars.append(txt[start_idx+1])
        chain[l] = dict(Counter(next_chars))
    except:
        continue 


with open("dino_chain.json", "w") as i :
   json.dump(chain, i)