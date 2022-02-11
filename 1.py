# 线程写法一

from threading import Thread


def fuc():
    for i in range(20):
        print("func线程", i, "----")


if __name__ == '__main__':
    t = Thread(target=fuc)  # 创建线程并给线程安排任务
    t.start()    # 多线程状态为可以开始工作状态,具体的执行时间由CPU决定
    # fuc()
    for x in range(20):
        print("无线程", x)
