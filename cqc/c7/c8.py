# -- coding: utf-8 --
# deamon 每个线程都可以单独设置它的属性，如果设置为True，当父进程结束后，子进程会自动被终止。
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print('Pid:' + str(self.pid) + 'LoopCount:' + str(count))


if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        p.daemon = True
        p.start()

    print 'Main process Ended!'
#     如果这样写了，你在关闭这个主程序运行时，就无需额外担心子进程有没有被关闭了。
