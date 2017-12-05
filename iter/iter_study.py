# -*- coding:utf-8 -*-
"""
反向迭代 实现 __reverse__
"""


def my_reverse():
    list_a = [1, 2, 3]
    list_b = reversed(list_a)
    for i in list_b:
        print(i)


class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


if __name__ == '__main__':
    for x in FloatRange(1.0, 4.0, 0.5):
        print(x)
    print('*'*20)
    for x in reversed(FloatRange(1.0, 4.0, 0.5)):
        print(x)