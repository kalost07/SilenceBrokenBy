import threading
import datetime
import roll
from config import config


def startTimer():
    threading.Timer(interval, startTimer).start()
    roll.roll()


interval = config["interval"]
print("Begin")
startTimer()
