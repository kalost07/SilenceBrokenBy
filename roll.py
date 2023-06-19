import json
import os
from playsound import playsound
import random


def roll():
    if random.random() < odds:
        name, file = random.choice(list(sounds.items()))
        # print("  playing", name)
        playsound(file)


f = open("config.json")
config = json.load(f)
sounds = config["sounds"]
odds = config["odds"]
