import multiprocessing
import random

q = multiprocessing.Queue(maxsize=5)

if __name__ == '__main__':
    q.put()


class Data:

    def __init__(self, data):
        self.oid = random.randint(10000, 99999)
        self.data = data
