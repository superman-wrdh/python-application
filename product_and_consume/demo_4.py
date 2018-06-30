"""
4、信号量模型
"""
import sys, time
import random
from threading import Thread, Semaphore

product = []

mutex = Semaphore(1)
full = Semaphore(0)
empty = Semaphore(5)


class Producer(Thread):
    def __init__(self, speed):
        Thread.__init__(self);
        self.speed = speed;

    def run(self):
        while True:
            for i in range(self.speed):
                ProductThing = '';
                empty.acquire()
                mutex.acquire()
                num = random.random()
                ProductThing += str(num) + ' '
                product.append(str(num))
                print('%s: count=%d' % ("producer" + str(self.speed), len(product)))
                print('         product things:' + ProductThing)
                mutex.release()
                full.release()
            time.sleep(1)


class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self);

    def run(self):
        count = 0
        time_start = time.clock()
        while True:
            speed = random.randint(1, 5)
            for i in range(speed):
                consumeThing = ""
                full.acquire()
                mutex.acquire()
                consumeThing += str(product[0]) + ' '
                del product[0]
                print('%s: count=%d' % ("consumer", len(product)))
                print('         consume things:' + consumeThing)
                count = count + 1
                if (count == 20):
                    time_end = time.clock()
                    print("消费 " + str(count) + "个商品所用时间: %f s" % (time_end - time_start))
                mutex.release()
                empty.release()
            time.sleep(1)


if __name__ == '__main__':
    Producer(1).start()

    Producer(2).start()

    Consumer().start()
