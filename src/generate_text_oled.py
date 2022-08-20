import json
import board
import busio as io
import microcontroller
import time
import adafruit_ssd1306
from markov_chain_parser import generate_text

i2c = io.I2C(board.GP5, board.GP4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

with open('dino_chain.json', 'r') as f:
    data=f.read()
dino_chain =  json.loads(data)

while True:
    a = generate_text(200,dino_chain);
    names = a.split("\n")
    oled.fill(0)
    text_y_pos = 5
    for n in names:
        if len(n) > 4 and len(n) < 15:
            oled.text(n, 5, text_y_pos,100)
            text_y_pos = text_y_pos + 10
    oled.show()
    time.sleep(6)
