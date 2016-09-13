#!/usr/bin/env python2

import threading
from profiler import timethis

m2_counter = 0
m2_lock = threading.Lock()

@timethis
def testm2():
    global m2_counter
    m2_lock.acquire()
    try:
        for _ in xrange(2000):
            m2_counter += 1
    finally:
        m2_lock.release()

def start_threads():
    threads = [threading.Thread(target=testm2) for t in xrange(2)]
    
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()

    print 'm2: ', m2_counter
