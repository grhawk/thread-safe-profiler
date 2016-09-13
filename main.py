#!/usr/bin/env python2

import threading
import module1 as m1
import module2 as m2
import profiler
import time

reload(m1)
reload(m2)
reload(threading)
reload(profiler)

# main_lock = threading.Lock()


# threads = [threading.Thread(target=m1.start_threads), threading.Thread(target=m2.start_threads)]
# for t in threads:
#     t.start()

# for t in threads:
#     t.join()

# print profiler.profile

# for i in xrange(1000):
#     profiler.test('testing '+str(i))
# print profiler.profile


@profiler.timethis
def test():
    pass

test()
