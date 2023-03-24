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

    n = 1
    random_pool = [
        Key.down,
        Key.space,
         'u',
         'i',
         'j',
         ',',
         'k'
        ]
    buffs = util.Interval([
        [Key.f9, 5*60, start_time, 0], # pet food
        # [Key.ctrl_l, 0.5*60, start_time, 0], # mp potion
        ['1', 220, False, 1], # bird
        [Key.f3, 15*60, False, 0], # maple warrior
    ])

    moves = util.Interval([
        ['s', 0.2*60, start_time, 1], # up skill
        ['d', 0.3*60, start_time, 1], # up skill
        ['w', 1*60, start_time, 1], # up skill
        # ['q', 0.7*60, start_time, 1], # aoe skill
    ], 1)

    for i in range(300):
        dur = (datetime.now()-start_time).seconds
        print(f'round: {i+1} \t{dur // 60}:{dur % 60}')

        # before start round
        buffs.do()
        # after start round

        util.pnr(dir_1)
        for j in range(n):
            # before basic loop

            # basic loop
            util.pnr('f')
            util.sleep(1,1.1)
            util.up_jump()
            util.sleep(0.3,0.31)
            util.pnr('f')
            util.sleep(1,1.5)
            util.pnr('f')
            util.sleep(1,1.1)
            util.up_jump(Key.down)

            # after basic loop
        

        # before end round
        p = random.random()
        if p >= 0.6:
            for k in random.sample(
                random_pool, 
                k=random.randint(1, len(random_pool))
            ):
                util.pnr(k)

        # after end round
        util.sleep(2, 2)
        dir_1, dir_2 = dir_2, dir_1
        # moves.do()

        
    print('ended')