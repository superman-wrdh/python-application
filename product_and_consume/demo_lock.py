import random
import time
import threading

product = []
lock = threading.Condition()


class Producer(threading.Thread):
    speed = 1;

    def __init__(self, lock, speed):
        self._lock = lock
        self.speed = speed;
        threading.Thread.__init__(self)

    def run(self):
        global product
        while True:
            if self._lock.acquire():
                if len(product) + self.speed > 5:
                    self._lock.wait()
                else:
                    ProductThing = '';
                    for i in range(self.speed):
                        num = random.random()
                        ProductThing += str(num) + ' '
                        product.append(str(num))
                    print("product " + str(self.speed) + ", count=" + str(len(product)))
                    print('         product things:' + ProductThing)
                    self._lock.notify()
                self._lock.release()
                time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, lock):
        self._lock = lock
        threading.Thread.__init__(self)

    def run(self):
        global product
        time_start = time.clock()
        count = 0
        while True:
            if self._lock.acquire():
                if len(product) <= 0:
                    self._lock.wait()
                else:
                    speed = random.randint(1, len(product))
                    consumeThing = '';
                    for i in range(speed):
                        consumeThing += str(product[0]) + ' '
                        del product[0]
                        count = count + 1
                        if (count == 20):
                            time_end = time.clock()
                            print("消费 " + str(count) + "个商品所用时间: %f s" % (time_end - time_start))
                    print('consume ' + str(speed) + ', count=' + str(len(product)))
                    print('         consume things:' + consumeThing)
                    self._lock.notify()
                self._lock.release()
                time.sleep(1)


def test():
    p1 = Producer(lock, 1)
    p1.start()
    p2 = Producer(lock, 2)
    p2.start()
    s = Consumer(lock)
    s.start()


if __name__ == '__main__':
    """
    一、使用多线程实现生产者与消费者模型

    1、  锁模型：
    """
    test()
