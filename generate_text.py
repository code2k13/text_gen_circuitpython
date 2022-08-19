import json
import time
from markov_chain_parser import generate_text

with open('dino_chain.json', 'r') as f:
    data=f.read()
dino_chain =  json.loads(data)

while True:
    a = generate_text(200,dino_chain);
    names = a.split("\n")
    for n in names:
        if len(n) > 4 and len(n) < 15:
            print(n)
    print("--------------------------------------")
    time.sleep(10)
