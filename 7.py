#  异步协程实战一(爬虫)
import requests
import asyncio
import aiohttp

urls = [
    "sss",
    "yyy",
    "zzz"
]


async def download(url):
    print(url)
    pass


async def main():
    tasks = []
    for url in urls:
        tasks.append(download(url))  # 把 async def download(args)  加入到tasks任务列表中

    print("game over")
    print(tasks)  # [<coroutine object download at 0x0000020AB5AB99C8>, <coroutine object download at
    # 0x0000020AB5AB9A48>, <coroutine object download at 0x0000020AB5AB9AC8>]   此时的tasks是个协程

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
