"""
三、不同主机上生产者消费者模型：



1、  socketTCP模型：
"""
from multiprocessing import Process
import queue
import threading
import socket
import random
import time

MaxSize = 5


def produce(speed, host, port):
    A = (host, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, MaxSize * 3)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, MaxSize * 3)
    s.connect(A)
    item = 1;
    while True:
        for i in range(speed):
            if (speed == 1):
                print("生产者", speed, ",生产了", "{0:0=3}".format(item))
                s.send(bytes("{0:0=3}".format(item), encoding="utf8"))
            else:
                print("生产者", speed, ",生产了", "{0:x=3}".format(item))
                s.send(bytes("{0:x=3}".format(item), encoding="utf8"))
            item = item + 1
        time.sleep(1)
    s.close()


def consume(host1, port1, host2, port2):
    q = queue.Queue(maxsize=MaxSize);
    threading.Thread(target=getMessage, args=(q, host1, port1)).start()
    threading.Thread(target=getMessage, args=(q, host2, port2)).start()
    count = 0
    time_start = time.clock()
    while True:
        speed = random.randint(1, MaxSize)
        for i in range(speed):
            item = q.get()
            print("消费者", " 消费了", item)
            count = count + 1
            if (count == 20):
                time_end = time.clock()
                print("消费" + str(count) + "个商品所用的时间: %f s" % (time_end - time_start))
        time.sleep(1)


def getMessage(q, host, port):
    A = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, MaxSize * 3)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, MaxSize * 3)
    sock.bind(A)
    sock.listen(0)
    tcpClientSock, addr = sock.accept()
    while True:
        try:
            data = tcpClientSock.recv(3)
            q.put(str(data, encoding="utf8"))
            print("count=" + str(q.qsize()))
        except:
            print("exception")
    tcpClientSock.close()
    sock.close()


if __name__ == '__main__':
    Process(target=produce, args=(1, 'localhost', 8080)).start()

    Process(target=produce, args=(2, 'localhost', 8090)).start()

    Process(target=consume, args=('localhost', 8080, 'localhost', 8090)).start()
