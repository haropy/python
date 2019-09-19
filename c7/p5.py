# -- coding: utf-8 --
# Pool Pool的用法有阻塞和非阻塞两种方式。非阻塞即为添加进程后，不一定非要等到改进程执行完就添加其他进程运行，阻塞则相反。
# 非阻塞
from multiprocessing import Lock, Pool
import time


def function(index):
    print 'Start process:', index
    time.sleep(3)
    print 'End process', index


if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in xrange(4):
        pool.apply_async(function, (i,))

    print "Start process"
    pool.close()
    pool.join()
    print "Subprocess done"
