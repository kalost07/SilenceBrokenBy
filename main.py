import threading
import datetime
import roll
from config import config


def timePrint(dif: datetime.timedelta):
    out = str(dif.seconds) + "." + str(int(dif.microseconds / 1000))
    print(out)


def startTimer():
    threading.Timer(interval, startTimer).start()

    now = datetime.datetime.now()
    # timePrint(now - start)
    roll.roll()


interval = config["interval"]
print("Begin")
start = datetime.datetime.now()
startTimer()
