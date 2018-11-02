from multiprocessing import Process
import time
import random
import multiprocessing


def produce(speed, mutex, full, empty, product, pindex, cindex):
    while True:
        for i in range(speed):
            ProductThing = '';
            empty.acquire()
            mutex.acquire()
            num = random.random()
            ProductThing += str(num) + ' '
            product[pindex.value] = num
            pindex.value = (pindex.value + 1) % len(product)
            print('%s: product things:%s' % ("producer" + str(speed), ProductThing))
            mutex.release()
            full.release()
        time.sleep(1)


def consume(mutex, full, empty, product, pindex, cindex):
    count = 0
    time_start = time.clock()
    while True:
        speed = random.randint(1, 5)
        for i in range(speed):
            consumeThing = ""
            full.acquire()
            mutex.acquire()
            consumeThing += str(product[cindex.value]) + ' '
            cindex.value = (cindex.value + 1) % len(product)
            print('%s:  consume things:%s' % ("consumer", consumeThing))
            count = count + 1
            if (count == 20):
                time_end = time.clock()
                print("消费 " + str(count) + "个商品所用时间: %f s" % (time_end - time_start))
            mutex.release()
            empty.release()
        time.sleep(1)


if __name__ == '__main__':
    product = multiprocessing.Array('d', range(5))

    pindex = multiprocessing.Value('i', 0)

    cindex = multiprocessing.Value('i', 0)

    mutex = multiprocessing.Semaphore(1)

    full = multiprocessing.Semaphore(0)

    empty = multiprocessing.Semaphore(5)

    Process(target=produce, args=(1, mutex, full, empty, product, pindex, cindex)).start()

    Process(target=produce, args=(2, mutex, full, empty, product, pindex, cindex)).start()

    Process(target=consume, args=(mutex, full, empty, product, pindex, cindex)).start()