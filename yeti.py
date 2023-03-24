import time
import random
from datetime import datetime, timedelta
from pynput.keyboard import Key
import util

if __name__ == '__main__':
    print('Start in')
    cd = 5
    for i in range(cd):
        print(5-i)
        time.sleep(1)

    # constant
    dir_1, dir_2 = [Key.left, Key.right]
    start_time = datetime.now()

    n = 3
    random_pool = [
        Key.down,
        Key.space,
         'u',
         'i',
         'j',
         ',',
         'k',
         'f',
         'f',
         'f'
        ]
    buffs = util.Interval([
        [Key.f9, 1*60, start_time, 0], # pet food
        # [Key.ctrl_l, 0.5*60, start_time, 0], # mp potion
        # ['1', 5*60, False, 1], # buff
        ['2', 3*60, False, 1], # buff
        ['3', 3*60, False, 1], # buff
        # [Key.f3, 15*60, False, 0], # maple warrior
    ])

    moves = util.Interval([
        ['a', 0.2*60, start_time, 2], # aoe skill
        ['s', 0.3*60, start_time, 2], # aoe skill
    ], 1)

    for i in range(300):
        dur = (datetime.now()-start_time).seconds
        print(f'round: {i+1} \t{dur // 60}:{dur % 60}')

        # before start round
        buffs.do()
        # after start round

        util.press(dir_1)
        for j in range(n):
            # before basic loop

            # basic loop
            util.pnr('f')
            util.sleep(1,1.1)
            util.jump_attack('f', 2, 0.5)
            util.sleep(1,1)

            # after basic loop
        
        util.release(dir_1)

        # before end round
        p = random.random()
        if p >= 0.60:
            for k in random.sample(
                random_pool, 
                k=random.randint(1, len(random_pool))
            ):
                util.pnr(k)

        # after end round
        util.sleep(1, 1)
        dir_1, dir_2 = dir_2, dir_1
        util.pnr(dir_1)
        moves.do()

        
    print('ended')