import threading
import random
from util import sleep, pnr

class RandomKeys (threading.Thread):
   def __init__(self, keys):
      threading.Thread.__init__(self)
      self.keys = keys
      self.isRun = True

   def run(self):
      print('start random keys thread')
      i = 0
      while self.isRun:
         key = random.choice(self.keys)
         pnr(key)
         print('pnr', key)
         sleep(0.1,3)
         i+=1
      print(f'stop random keys with {i} times')
   
   def exit(self):
      self.isRun = False
