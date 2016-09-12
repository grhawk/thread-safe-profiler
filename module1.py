#!/usr/bin/env python2

import threading
import profiler
import time

m1_counter = 0
m1_lock = threading.Lock()

def testm1():
    profiler.start('testm1')
    global m1_counter
    m1_lock.acquire()
    try:
        for _ in xrange(2):
            profiler.start('adding_m1')
            m1_counter += 1
            time.sleep(2)
            profiler.stop('adding_m1')
    finally:
        m1_lock.release()
    profiler.stop('testm1')

def start_threads():
    threads = [threading.Thread(target=testm1) for t in xrange(2)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print 'm1: ', m1_counter
