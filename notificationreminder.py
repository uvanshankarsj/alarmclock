from datetime import datetime
from playsound import playsound
import time
import os

now = datetime.now()
alarm=str(input())
string=str(input())
while now.strftime("%H:%M:%S")!=alarm:
    now = datetime.now()
    print(now.strftime("%H:%M:%S"))
    time.sleep(1)
# file='Venpura-StarMusiQ.Fun.mp3'
os.system("notify-send "+string)
playsound('tense-cinematic-117406.mp3')
