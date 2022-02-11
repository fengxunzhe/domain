#  异步协程实战二(爬虫)
import json
import logging
import asyncio
import aiohttp
import requests
import aiofiles
from pypac import PACSession, get_pac


# http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"'+b_id+'","cid":"4306063500|1569782244","need_bookinfo":1}

async def download(cid, title, b_id):
    data = {
            "book_id": b_id,
            "cid": f"{b_id}|{cid}",
            "need_bookinfo": 1
    }
    data = json.dumps(data)  # 转换为JSON格式
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:  # 使用with as 表示用完之后自动关闭
        async with session.get(url, proxy="http://172.21.1.30:8080") as resp:     # 使用with as 表示用完之后自动关闭
            dic = await resp.json()  # 使用await代表等待返回结果中CPU继续运行其他的

            async with aiofiles.open("novel\\" + title, mode="w", encoding="utf-8") as f:  # 使用with as
                # 表示用完之后自动关闭，此处是异步存储aiofiles
                await f.write(dic['data']['novel']['content'])  # 加上await代表写入的时候空闲时间CPU去干其他的


async def getGids(arg_url):
    pac = get_pac(url='http://10.18.88.118/proxy.pac')
    st = PACSession(pac)

    logging.captureWarnings(True)
    result = st.get(arg_url, verify=False)
    ret = result.json()
    tasks = []
    for items in ret['data']['novel']['items']:
        title = items['title']
        cid = items['cid']
        # 开始执行同步任务IO读取操作
        tasks.append(download(cid, title, b_id))  # 存储异步任务列表,此处append的是一个个协程对象

    await asyncio.wait(tasks)  # 循环执行  CPU不等待,加await代表 CPU在IO操作中不等待,异步执行其他任务


if __name__ == '__main__':
    b_id = "4306063500"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(getGids(url))
