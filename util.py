import time
import random
from datetime import datetime, timedelta
from pynput.keyboard import Key, Controller

keyboard = Controller()

def sleep(mi, ma):
    dif = (ma-mi)*random.random()
    time.sleep(mi+dif)

def pnr(key):
    keyboard.press(key)
    sleep(0.05, 0.1)
    keyboard.release(key)

def press(key):
    keyboard.press(key)

def release(key):
    keyboard.press(key)

def macro(arr):
    for key in arr:
        pnr(key)
        sleep(0.15, 0.2)

def jump_attack(key, n=1, delay=0, dir=False):
    if dir:
        keyboard.press(dir)
    for i in range(n):
        pnr(Key.space)
        sleep(0.1,0.15)
    if dir:
        keyboard.release(dir)
    pnr(key)
    sleep(delay,delay)

def create_intervals(arr):
    return [[i[0], i[1], False] for i in arr]

def do_update_intervals(arr):
    now = datetime.now()
    for i in range(len(arr)):
        key, cd, ts = arr[i]
        if ts == False or (now-ts).seconds > cd:
            pnr(key)
            arr[i][2] = now