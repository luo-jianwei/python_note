#!/usr/bin/env python
# coding: UTF-8

import threading
import time

number = 0

lock = threading.RLock()

def run(num):
    # ¼ÓËø
    lock.acquire()
    
    global number
    number += 1
    # ËøÊÍ·Å
    lock.release()
    
    print number
    time.sleep(1)
    
for i in range(30):
    t = threading.Thread(target=run,args=(i,))
    t.start()
    