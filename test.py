import time
import random
from datetime import datetime, timedelta
from pynput.keyboard import Key
import util

def create_intervals(arr):
    return [[i[0], i[1], False] for i in arr]

def do_update_intervals(arr):
    now = datetime.now()
    for i in range(len(arr)):
        key, cd, ts = arr[i]
        if ts == False or (now-ts).seconds > cd:
            util.pnr(key)
            arr[i][2] = now

if __name__ == '__main__':
    print('start in')
    cd = 5
    for i in range(cd):
        print(5-i)
        time.sleep(1)

    dir1, dir2 = [Key.left, Key.right]
    basic = [Key.space, Key.space, 'f']
    n = 3
    random_pool = [Key.down, 'i', ',', 'k']
    buffs = [(Key.f9, 5*60),('d', 60)]
    start_time = datetime.now()
    tmp = create_intervals(buffs)

    for i in range(1000):
        dur = (datetime.now()-start_time).seconds
        print(f'round: {i+1} \t{dur // 60}:{dur % 60}')

        # before start round
        # after start round

        util.press(dir1)
        for j in range(n):
            # before basic loop

            # basic loop
            util.jump_attack('f',2,0.5)

            # after basic loop

            util.release(dir1)
            do_update_intervals(tmp)
            util.press(dir1)

        
        util.release(dir1)

        # before end round
        p = random.random()
        if p >= 0.95:
            for k in random.sample(
                random_pool, 
                k=random.randint(1, len(random_pool))
            ):
                util.pnr(k)

        # after end round
        sleep(0.5, 1)
        dir1, dir2 = dir2, dir1
        
    print('ended')