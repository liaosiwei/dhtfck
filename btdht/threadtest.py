# -*- coding: utf-8 -*-
import threading
import time

def join(seconds):
    x = seconds
    x += 1
    time.sleep(seconds)
    print str(x)

tJoin = threading.Thread(target=join, args=(1,))
tContext = threading.Thread(target=join, args=(2,))
tJoin.start()
tContext.start()
tJoin.join()
tContext.join()