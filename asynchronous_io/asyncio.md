# asyncio 介绍

### 参考文档 https://docs.python.org/3/library/asyncio.html

asyncio是一个用与写高并发代码的库，主要语法为**async/await** 关键字

主要用途有高性能网络和web服务，数据库连接库，任务分发队列等。

## 用法



## 高级api

- [Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)

```
协程（Coroutines ） 语法使用async/await 关键字 以下代码再python3.7下间隔1秒打印hello world
```
```python
import asyncio

async def main():
     print('hello')
     await asyncio.sleep(1)
     print('world')

>>> asyncio.run(main())
hello
world

```

```
注意调用一个协程并不是简单的执行
运行一个协程 asyncio提供了3种方式
```

* 方式1   asyncio.run() 是一种高级的api

* 方式2 使用 awaite 语法 

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

```

*  运行结果 注意运行花费的时间
```
started at 17:13:52
hello
world
finished at 17:13:55
```

* 方式3  使用 [`asyncio.create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task) 

```python
# 上面代码改进后
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
```
####  运行结果 注意花费时间不在是3s 而是2s
```
started at 17:14:32
hello
world
finished at 17:14:34
```

## Awaitables

```
什么是 awaitable？一个对象只有是可以 awaitable对象才能使用awaite关键字
常见的3种 awaitable对象 为coroutines, Tasks, and Futures.
```

* Coroutines

```
Python coroutines 是awaitables 因此可以被被其他协程 awaited 
```
```python
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
```
```
注意这里的协程 coroutine 包含两种概念 
a coroutine function: an async def function;
a coroutine object: an object returned by calling a coroutine function.

同样也支持python2的基于生成器的协程
asyncio also supports legacy generator-based coroutines.
```


* Tasks

```
Tasks 一般用于协程的并发
当协程被task相关的函数包裹，例如asyncio.create_task() 协程会被自动的被安排计划运行
```

```python
import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())
```






* Futures
```
Future 一个特殊的低级awaitable对象代表了一个异步操作的最终结果。

一个Future 是可以awaited  意味着coroutine 将会等待直到处理完成

Future 在异步io中使用回调机制
```

```python
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```

### 详细例子

[`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor)



## 并发运行 task

```python
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())

# Expected output:
#
#     Task A: Compute factorial(2)...
#     Task B: Compute factorial(2)...
#     Task C: Compute factorial(2)...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3)...
#     Task C: Compute factorial(3)...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4)...
#     Task C: factorial(4) = 24
```





## 超时机制

```python
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
#     timeout!
```



## task基本api及用法

```
class* `asyncio.``Task`(*coro*, ***, *loop=None*, *name=None*)

1 cancel()
2 cancelled()  Return True if the Task is cancelled.
3 done() Return True if the Task is done.
3 result() Return the result of the Task.
4 exception() Return the exception of the Task.
5 add_done_callback(callback, *, context=None) Add a callback to be run when the Task is done.
6 remove_done_callback(callback) Remove callback from the callbacks list.
```

### 相关代码示例

####  task停止 

```python
# 下面代码展示如何打断一个运行的协程
async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())

# Expected output:
#
#     cancel_me(): before sleep
#     cancel_me(): cancel sleep
#     cancel_me(): after sleep
#     main(): cancel_me is cancelled now
```

##### add_done_callback 添加完成回调
```python 
import asyncio
import time


async def calculate_task(a, b, t):
    print("start calculate at {}".format(time.time()))
    await asyncio.sleep(t)
    print("finished")
    return a + b


def done_callback(*args):
    print("finished callback")
    r = args[0].result()
    print("result is {}".format(r))
    print("now is {}".format(time.time()))


async def main():
    task1 = asyncio.create_task(calculate_task(1, 3, 5))
    task2 = asyncio.create_task(calculate_task(1, 6, 3))
    try:
        task1.add_done_callback(done_callback)
        task2.add_done_callback(done_callback)
        await task1
        await task2
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")


t = time.time()
asyncio.run(main())
print("total time is {}".format(time.time() - t))

```

#### 









- [Streams](https://docs.python.org/3/library/asyncio-stream.html)
- [Synchronization Primitives](https://docs.python.org/3/library/asyncio-sync.html)
- [Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html)
- [Queues](https://docs.python.org/3/library/asyncio-queue.html)
- [Exceptions](https://docs.python.org/3/library/asyncio-exceptions.html)



## 低级api








