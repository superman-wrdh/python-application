import time
import threading


class Consumer(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(1)
        print("spider url:{} detail success".format(self.url))
        self.sem.release()


class Producer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            url = "https://66super.com/{}".format(i)
            print("get url {}".format(url))
            self.sem.acquire()
            c = Consumer(url=url, sem=self.sem)
            c.start()


if __name__ == '__main__':
    se = threading.Semaphore(3)
    p = Producer(se)
    p.start()
    pass
