"""2、Condition模型

可以认为Condition对象维护了一个锁（Lock/RLock)和一个waiting池。线程通过acquire获得Condition对象，当调用wait方法时，线程会释放Condition内部的锁并进入blocked状态，同时在waiting池中记录这个线程。当调用notify方法时，Condition对象会从waiting池中挑选一个线程，通知其调用acquire方法尝试取到锁，但是notify and notifyall本身是不会释放占有的Condition内部的锁，所以随后需要condition.release()来显示的释放锁。

Condition对象的构造函数可以接受一个Lock/RLock对象作为参数，如果没有指定，则Condition对象会在内部自行创建一个RLock。
"""
import threading
import time, random

product = [];
cond = threading.Condition()


class Producer(threading.Thread):
    def __init__(self, speed):
        threading.Thread.__init__(self)
        self.speed = speed

    def run(self):
        while True:
            for i in range(self.speed):
                cond.acquire()
                while len(product) >= 5:
                    cond.wait();
                num = random.random();
                product.append(num)
                print("生产者" + str(self.speed) + "生产了：" + str(num))
                cond.notifyAll()
                cond.release()
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        count = 0
        time_start = time.clock()
        while True:
            speed = random.randint(1, 5);
            for i in range(speed):
                cond.acquire()
                while len(product) <= 0:
                    cond.wait()
                num = product[0];
                del product[0]
                print("消费者，消费了" + str(num))
                count = count + 1
                if (count == 20):
                    time_end = time.clock()
                    print("消费 " + str(count) + "个商品所用时间: %f s" % (time_end - time_start))
                cond.notify()
                cond.release()
            time.sleep(1)


Producer(1).start();
Producer(2).start();
Consumer().start();