"""
2、  远程调用模型：

先在主进程中注册获取产品的方法，消费者在取用商品时调用取用商品的远程方法来获取。取用商品有一定的延迟，使得程序的整个运行速度比较慢。
"""
from multiprocessing import Process
from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer
import random
import time
import multiprocessing

q = multiprocessing.Queue(maxsize=5)


def produce(speed, q):
    while True:
        for i in range(speed):
            item = random.random()
            q.put(item)
            print("生产者", speed, "生产了", str(item))
        time.sleep(1)


def getAProduct():
    global q
    return q.get()


def consume(host, port):
    server = ServerProxy("http://" + host + ":" + str(port))
    count = 0
    time_start = time.clock()
    while True:
        speed = random.randint(1, 5)
        for i in range(speed):
            print("开始远程调用")
            item = server.getAProduct()
            print("消费者", "消费了", item)
            count = count + 1
            if (count == 20):
                time_end = time.clock()
                print("消费" + str(count) + "个资源所需要的时间: %f s" % (time_end - time_start))
        time.sleep(1)


if __name__ == '__main__':
    s = SimpleXMLRPCServer(('localhost', 8000))

    s.register_function(getAProduct)

    print('注册获取产品方法完成')

    Process(target=produce, args=(1, q)).start()

    Process(target=produce, args=(2, q)).start()

    Process(target=consume, args=('localhost', 8000)).start()

    s.serve_forever()
