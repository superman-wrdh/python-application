"""
2、  Condition模型
"""
import multiprocessing
import random
import time


def produce(speed, cond, product):
    while True:
        for i in range(speed):
            cond.acquire()
            while len(product) >= 5:
                cond.wait();
            num = random.random();
            product.append(num)
            print("生产者" + str(speed) + ",生产了：" + str(num))
            cond.notify()
            cond.release()
        time.sleep(1)


def consume(cond, product):
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


if __name__ == '__main__':
    c = multiprocessing.Condition();

    product = multiprocessing.Manager().list()

    p1 = multiprocessing.Process(target=produce, args=(1, c, product))

    p1.start()

    p2 = multiprocessing.Process(target=produce, args=(2, c, product))

    p2.start()

    c1 = multiprocessing.Process(target=consume, args=(c, product))

    c1.start()

    p1.join()

    p2.join()

    c1.join()
