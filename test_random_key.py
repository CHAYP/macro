import time
import random
from datetime import datetime, timedelta
from pynput.keyboard import Key
import util
import random_key

if __name__ == '__main__':
    thr = random_key.RandomKeys(['a','b','c'])
    thr.start()

    try:

        util.sleep(10,10)

    except:

        thr.exit()