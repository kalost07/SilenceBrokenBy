import threading
import datetime
from math import log, ceil

import roll

interval = 1


def timePrint(dif: datetime.timedelta):
    out = str(dif.seconds) + "." + str(int(dif.microseconds / 1000))
    print(out)


def startTimer():
    threading.Timer(interval, startTimer).start()

    now = datetime.datetime.now()
    # timePrint(now - start)
    roll.roll()


numdraws = ceil(log(0.5, 1 - roll.odds))
print("Draws for 50% chance: ", numdraws)
start = datetime.datetime.now()
startTimer()
