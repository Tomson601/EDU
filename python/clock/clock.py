import os
import time


def wait(i):
    time.sleep(i)


def clear_console():
    os.system('clear')


def clock(seconds, minutes, hours):
    while True:
        wait(0.5)
        seconds+=1
        print("%02d" %hours,':', "%02d" %minutes,':', "%02d" %seconds)          # "%02d"--> formating to double digit form xx-00
        if seconds == 59:
            minutes+=1
            seconds=0
        if minutes == 60:
            hours+=1
            minutes=0
        if hours == 24:
            seconds=minutes=hours=0
        wait(0.5)
        clear_console()

clock(55, 59, 23)
