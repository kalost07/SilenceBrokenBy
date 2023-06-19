from config import config
from playsound import playsound
import random


def roll():
    global curr_odds
    if curr_odds < base_odds:
        curr_odds += base_odds / rest_period
        curr_odds = min(curr_odds, base_odds)

    if random.random() < curr_odds:
        curr_odds = base_odds / rest_period
        name, file = random.choice(list(sounds.items()))
        playsound(file)
        print("  playing", name)


sounds = config["sounds"]
base_odds = config["base_odds"]
rest_period = config["rest_period"]
curr_odds = base_odds
