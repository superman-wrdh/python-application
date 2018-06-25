# -*- encoding: utf-8 -*-
from queue import deque, Queue, LifoQueue, PriorityQueue


def deque_learn():
    """双端队列"""
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)

    # 1, 2, 3
    while (len(q)):
        print(q.popleft())  # 1 2 3
        # print(q.pop())   # 3 2 1


if __name__ == '__main__':
    deque_learn()
