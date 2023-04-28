import time
import random
import signal
import os

from datetime import datetime, timedelta
from pynput.keyboard import Key, Controller
from pynput.mouse import Listener

keyboard = Controller()

press_list = {}

def sleep(mi, ma):
    dif = (ma-mi)*random.random()
    time.sleep(mi+dif)

def pnr(key, mi=0.05, ma=0.1):
    # print('p', key)
    keyboard.press(key)
    sleep(mi, ma)
    keyboard.release(key)
    # print('r', key)

def press(key):
    # print('press', key)
    keyboard.press(key)
    press_list[key] = True

def release(key):
    # print('release', key)
    keyboard.release(key)
    del press_list[key]

def clear_press():
    for key in press_list:
        keyboard.release(key)

def jump_attack(key, n=1, delay=0, dir=False):
    if dir:
        press(dir)
    for i in range(n):
        pnr(Key.space)
        sleep(0.1,0.15)
    if dir:
        release(dir)
    pnr(key)
    sleep(delay, delay)

def up_jump(key=Key.up):
    keyboard.press(key)
    sleep(0.1,0.15)
    pnr(Key.space)
    sleep(0.1,0.15)
    pnr(Key.space)
    sleep(0.1,0.15)
    keyboard.release(key)

def withProb(p=0.5):
    return random.random() <= p

class Interval:
    def __init__(self, inputs, limit=0):
        self.limit = limit
        self.inputs = [[key, cd, stamp, delay] for [key, cd, stamp, delay] in inputs]

    def do(self):
        cnt = 0
        i = 0
        now = datetime.now()

        for [key, cd, stamp, delay] in self.inputs:
            if not isinstance(stamp, datetime) or (now-stamp).seconds > cd:
                pnr(key)
                sleep(delay, delay+0.05)
                self.inputs[i][2] = now
                cnt+=1
                if self.limit > 0 and cnt >= self.limit:
                    return
            i+=1

def on_move(x, y):
    if x < 0 or y < 0:
        clear_press()
        os.kill(os.getpid(), signal.SIGINT)

Listener(on_move=on_move).start()