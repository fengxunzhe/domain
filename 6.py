#  协程实例  (cpu在进行IO读取操作时会中断等待(同步), 协程可以在IO中让CPU切换到其他任务,不间断的工作)

#  asyncio前面都要加上await   函数前面加代表是协程函数
import asyncio
import time


async def func1():
    print("张三在工作中")
    await asyncio.sleep(3)  # 等待3秒再执行下面的,此时CPU不干等着，执行其他任务
    print("张三在工作中")


async def func2():
    print("李四在工作中")
    await asyncio.sleep(4)
    print("李四在工作中")


async def func3():
    print("王五在工作中")
    await asyncio.sleep(5)
    print("王五在工作中")


async def mainfuc():
    tasks = [
        func1(),
        func2(),
        func3()
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(mainfuc())
    t2 = time.time()
    print(t2 - t1)
