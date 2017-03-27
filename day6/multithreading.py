#!/usr/bin/env python
# coding: UTF-8

import threading
import time

def run(num):
    print 'I am thread %s !' %num
    time.sleep(2)
    print '*'*15
    
for i in range(10):
    t = threading.Thread(target=run,args=(i,))
    t.start()
#    t.join()