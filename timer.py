import time
from playsound import playsound

timer=int(input())

while timer!=0:
    timer-=1
    print(timer)
    time.sleep(60)

print("playing")
playsound('tense-cinematic-117406.mp3')