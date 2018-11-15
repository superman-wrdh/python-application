from multiprocessing import Pool, cpu_count
import threading
import time

lock = threading.Lock()


def task1(a, b, c):
    time.sleep(5)
    return a + b + c


def task2(a, b, c):
    time.sleep(8)
    return a + b + c, a * b * c


def task3(a, b, c):
    time.sleep(15)
    return a + b + c, a * b * c


def get_task():
    task_queen = [
        {
            "task_name": "task1",
            "function": task1,
            "args": [1, 2, 3]
        },

        {
            "task_name": "task2",
            "function": task2,
            "args": [1, 2, 3]
        },
        {
            "task_name": "task3",
            "function": task3,
            "args": [1, 2, 3]
        }
    ]
    return task_queen


def calculate_indicator(params):
    try:
        with lock:
            s = time.clock()
            fun = params.get("function")
            print("start run task {}".format(fun.__name__))
            args = params.get("args")
            task_name = params.get("task_name")
            content = params.get("content")
            result = fun(*args)
            content.update({task_name: result})
            e = time.clock()
            print("task {} finished,take times {}".format(fun.__name__, e - s))
    except Exception as e:
        pass


def main():
    print("start multi process ")
    ss = time.clock()
    data = get_task()
    import multiprocessing
    from pprint import pprint
    with multiprocessing.Manager() as MG:  # 重命名
        content = multiprocessing.Manager().dict()  # 主进程与子进程共享这个字典
        [d.update({"content": content}) for d in data]

        pool = Pool(processes=cpu_count())
        try:
            pool.map(calculate_indicator, data)
            ee = time.clock()
            print("all task finished take times {}".format(ee - ss))
            print("result")
            pprint(str(content))
        except Exception as e:
            print(str(e))
            pass


if __name__ == '__main__':
    main()
