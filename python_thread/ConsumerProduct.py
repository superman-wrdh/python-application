# -*- encoding: utf-8 -*-
import threading
import queue
import random
import time


class Producter(threading.Thread):
    """生产者线程"""

    def __init__(self, t_name, queue):
        self.queue = queue
        threading.Thread.__init__(self, name=t_name)

    def run(self):
        for i in range(100):
            #random_num = random.randint(1, 99)
            self.queue.put(i)
            print('put num in Queue %s' % i)
            time.sleep(1)

        print('put queue done')


class ConsumeEven(threading.Thread):
    """消费线程"""

    def __init__(self, t_name, queue):
        self.queue = queue
        threading.Thread.__init__(self, name=t_name)

    def run(self):
        while True:
            v = self.queue.get()
            print(self.name + " " + str(v))


if __name__ == '__main__':
    q = queue.Queue()
    pt = Producter('producter', q)
    ce = ConsumeEven('consumeeven-1', q)
    ce2 = ConsumeEven('consumeeven-2', q)
    ce.start()
    ce2.start()
    pt.start()
    pt.join()
    ce.join()
    ce2.join()
