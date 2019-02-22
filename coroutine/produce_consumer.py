# coding: utf-8

"""
协成实现生产者消费者模型
"""
import time
import random


# 生产者、消费者例子
def consumer():  # 定义消费者，由于有yeild关键词，此消费者为一个生成器
    print("[消费者] 初始化消费者 ......")
    r = "初始化ok"  # 初始化返回结果，并在启动消费者时，返回给生产者
    while True:
        n = yield r  # r传递给生产者, n 生产者返回 消费者通过yield关键词接收生产者产生的消息，同时返回结果给生产者
        print("[消费者] 消费 n = %s, r = %s" % (n, r))
        r = "消费 %s OK" % n  # 消费者消费结果，下个循环返回给生产者
        print("\n\n")


def produce(c):  # 定义生产者，此时的 c 为一个生成器
    print("[生产者] 初始化生产者 ......")
    r = c.send(None)  # 启动消费者生成器，同时第一次接收返回结果
    print("[生产者] 开始消费, 返回 %s" % r)
    np = 0
    while np < 5:
        time.sleep(random.randint(1, 2))
        np += 1
        print("[生产者] 等待, 生产中 %s ......" % np)
        r = c.send(np)  # 向消费者发送消息，同时准备接收结果。此时会切换到消费者执行
        print("[生产者] 消费者返回: %s" % r)
        print("\n\n")
    c.close()  # 关闭消费者生成器
    print("[Producer] Close Producer ......")
    print("\n\n")


c = consumer()
produce(c)
