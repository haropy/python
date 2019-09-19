# -- coding: utf-8 --
# 通过 Lock 来实现，在一个进程输出时，加锁，其他进程等待。等此进程执行结束后，释放锁，其他进程可以进行输出。
from multiprocessing import Process, Lock
import time


class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            # self.lock.acquire()
            print('Pid:' + str(self.pid) + 'LoopCount:' + str(count))
            # self.lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10, 15):
        p = MyProcess(i, lock)
        p.start()
