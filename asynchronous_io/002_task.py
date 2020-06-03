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
