# Text generation in microcontrollers using CircutPython and  Markov Chains
A program written for circuitpython that generates random text (dinosaur names) using charactor level Markov Chains


## Steps to run

- Download the file https://raw.githubusercontent.com/junosuarez/dinosaurs/master/dinosaurs.csv
- Generate a markov chain model from your text file using **generate_chain.py**.  
- Copy **generate_text.py**, **marker_chain_parser.py** and **dino_chain.json** to your CircuitPython device.
- Check output on a serial monitor.

> Alternatively you skip steps 1 and 2 and   run the 'cp_text_gen.ipyb' Jupyter notebook to generate **dino_chain.json**.
