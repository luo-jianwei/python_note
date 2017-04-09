#!/usr/bin/env python
# coding: UTF-8

import time
#import multiprocessing
from multiprocessing import Process,Lock

l = Lock()

def sayHi(name):
    l.acquire()
    print 'Hello, my name is %s' %i
    l.release()    
    time.sleep(1)
        
if __name__ == '__main__':
    for i in range(20):
        #p = multiprocessing.Process(target=run,args=('Roy',))
        p = Process(target=sayHi,args=(i,))
        p.start()