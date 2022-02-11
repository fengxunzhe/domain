import json
import logging
import subprocess

import requests
from pypac import PACSession, get_pac
from requests_ntlm import HttpNtlmAuth

surl = "https://www.pearvideo.com/video_1750709"
surl = surl.split("_")[1]
print(surl)
# spilt函数的用法  spilt(p1, p2)  return list列表   p1为分隔符, p2为分割成几部分


d_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={surl}&mrd=0.30104970988192226"
# 字符串前加f  代表格式化字符串  字符串加r  代表不转换原有字符格式
print(d_url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.116 Safari/537.36 ",
    "Referer": "https://www.pearvideo.com/video_1750709"
}
pac = get_pac(url='http://10.18.88.118/proxy.pac')
print("获取pac脚本文件---", pac)
st = PACSession(pac)

print("调用PACSession---", st)
logging.captureWarnings(True)
result = st.get(d_url, verify=False, headers=headers)
print("返回结果response对象---", type(result))
print(result.text)
ret = result.json()
time = ret["systemTime"]
link = ret["videoInfo"]["videos"]["srcUrl"]
link = link.replace(time, f"cont-{surl}")
print(link)


with open("a.mp4", mode="wb") as f:
    f.write(requests.get(link).content)

print("----end")

