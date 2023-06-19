from playsound import playsound
import threading
import random
import datetime
from math import log, ceil, pow

interval = 1
counter = 0
odds = 0.0076

list = ["megalovania"]
filename = {
    "megalovania":"sounds/megalovania.mp3"
}

def timePrint(dif: datetime.timedelta):
    print("  ",dif.seconds,"sec")

def myPeriodicFunction(ct=counter):
    if random.random()<odds: 
        sound=random.choice(list)
        #print("playing ",sound)
        end=datetime.datetime.now()
        dif=end-start
        playsound(filename[sound])
        timePrint(dif)
    ct += 1

def startTimer():
    threading.Timer(interval, startTimer).start()
    myPeriodicFunction()
    
numdraws=ceil(log(0.5,1-odds))
print("Draws for 50% chance: ",numdraws)
start=datetime.datetime.now()
startTimer()
