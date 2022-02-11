# 线程池案例
import logging
from concurrent.futures import ThreadPoolExecutor
import csv
import requests
from pypac import get_pac, PACSession

f = open('main.csv', 'w', encoding='utf-8')
# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)


def down_pages(arg):
    pac = get_pac(url='http://10.18.88.118/proxy.pac')
    st = PACSession(pac)
    logging.captureWarnings(True)
    data = f"limit=20&current={arg}&pubDateStartTime=&pubDateEndTime=&prodPcatid=&prodCatid=&prodName="
    result = st.post("http://www.xinfadi.com.cn/getPriceData.html", verify=False, data=data)
    # print(arg, result.text)
    ret = result.json()

    print(ret)
    data = ret[list]

    # csv_writer.writerow()


if __name__ == '__main__':
    with ThreadPoolExecutor(5) as t:  # 创建5个线程池
        for i in range(1, 20):  # 工作
            t.submit(down_pages, i)

        f.close()

