from time import sleep
from threading import *     # Thread is a class here

class hello(Thread):
    def run(self):
        for i in range(10):
            print('hello')
            sleep(0.01)        # stop 1 sec, b4 exucting laters

class hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(0.01)

t1 = hello(); t2 = hi()

t1.start()
sleep(0.02)
t2.start()

t1.join()
t2.join()      # main thred is asked t1 & t2 to finish

print('BYE')    # it's printed by main thread