"""
3、Queue模型



1.创建一个 Queue.Queue() 的实例，来表示缓冲池。

2.每次从使用生产者线程对队列中的数据进行填充，使用消费者线程取出队列中的数据。
"""
import threading
import queue
import time
import random


class Producer(threading.Thread):
    def __init__(self, speed, queue):
        threading.Thread.__init__(self)
        self.speed = speed
        self.queue = queue

    def run(self):
        while True:
            for i in range(self.speed):
                item = random.random()
                self.queue.put(item)
                print("生产者", self.speed, "生产了：", str(item))
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        time_start = time.clock()
        count = 0
        while True:
            speed = random.randint(1, 5)
            for i in range(speed):
                item = self.queue.get()
                print("消费者", "消费：", item)
                count = count + 1
                if (count == 20):
                    time_end = time.clock()
                    print("消费 " + str(count) + "个商品所用时间: %f s" % (time_end - time_start))
            time.sleep(1)


q = queue.Queue(maxsize=5)

if __name__ == '__main__':
    Producer(1, q).start()

    Producer(2, q).start()

    Consumer(q).start()
