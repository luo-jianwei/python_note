#!/usr/bin/env python
# coding: UTF-8

import threading
import Queue
import time
import random

q = Queue.Queue()

def Producer(name):
    for i in range(20):
        q.put(i)
        print '\033[31;1mProducer %s has made %s\033[0m' % (name,i)
        # sleep4ÃëÄÚËæ»úÊı
        time.sleep(random.randrange(4))
        
def Consumer(name):
    count = 0
    while count < 20:
         data = q.get()
         print '\033[32;1mConsumer %s has get %s\033[0m' % (name,data)
         count += 1
         time.sleep(random.randrange(2))
         
p = threading.Thread(target=Producer,args=('Rose',))
c = threading.Thread(target=Consumer,args=('Jerry',))

p.start()
c.start()
