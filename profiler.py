#!/usr/bin/env python2

import threading
import time
import sys

timing = time.time
prof_lock = threading.Lock()

profile = {}

def start(name):
    prof_lock.acquire()
    if name in profile.keys():
        profile[name][0] += 1
        profile[name][1] -= timing()
    else:
        profile[name] = [1, -timing()]
    prof_lock.release()

def stop(name):
    prof_lock.acquire()
    try:
        profile[name][1] += timing()
    except KeyError as e:
        sys.stderr.write('@PROFILING: Trying to stop a non-started clock\n')
        sys.stderr.write(e)
        raise
    prof_lock.release()

