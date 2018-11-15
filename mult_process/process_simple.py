import multiprocessing
from random import randint


def func(mydict):
    mydict[randint(1, 10)] = randint(10, 100)  # 子进程改变dict,主进程跟着改变
    mydict[randint(10, 20)] = randint(10, 100)


if __name__ == "__main__":
    with multiprocessing.Manager() as MG:  # 重命名
        contend = multiprocessing.Manager().dict()  # 主进程与子进程共享这个字典

        p = multiprocessing.Process(target=func, args=(contend,))
        p2 = multiprocessing.Process(target=func, args=(contend,))
        p.start()
        p2.start()
        p.join()
        p2.join()

        print(contend)
