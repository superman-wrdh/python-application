"""
5、  Event模型

生产者生产完商品会立即通知消费者去消费，消费者消费完商品后会立即通知生产者去生产，适用于产品池数目为一的情况。
"""
import multiprocessing
import random
import time


def produce(speed, e_p1, e_p2, e_c, product):
    while True:
        for i in range(speed):
            if (speed == 1):
                e_p1.wait();
            if (speed == 2):
                e_p2.wait();
            num = random.random();
            product.append(num)
            print("生产者" + str(speed) + ",生产了" + str(num))
            e_c.set();
            if (speed == 1):
                e_p1.clear();
            if (speed == 2):
                e_p2.clear();
        time.sleep(1)


def consume(e_p1, e_p2, e_c, product):
    count = 0
    time_start = time.clock()
    while True:
        speed = random.randint(1, 5);
        for i in range(speed):
            e_c.wait();
            num = product[0];
            del product[0]
            print("消费者，消费了" + str(num))
            count = count + 1
            if (count == 20):
                time_end = time.clock()
                print("消费 " + str(count) + "个商品所用时间: %f s" % (time_end - time_start))
            r = random.randint(1, 2)
            if (r == 1):
                e_p1.set()
            if (r == 2):
                e_p2.set()
            e_c.clear()
        time.sleep(1)


if __name__ == '__main__':
    e_p1 = multiprocessing.Event();

    e_p2 = multiprocessing.Event();

    e_c = multiprocessing.Event();

    e_p1.set()

    product = multiprocessing.Manager().list()

    p1 = multiprocessing.Process(target=produce, args=(1, e_p1, e_p2, e_c, product))

    p1.start()

    p2 = multiprocessing.Process(target=produce, args=(2, e_p1, e_p2, e_c, product))

    p2.start()

    c1 = multiprocessing.Process(target=consume, args=(e_p1, e_p2, e_c, product))

    c1.start()

    p1.join()

    p2.join()

    c1.join()
