# 多进程写法
from multiprocessing import Process


def func(a, b):
    print("参数", a, b)
    for x in range(20):
        print("func", x)


if __name__ == '__main__':
    t = Process(target=func, args=("today1", 111))
    t.start()

    for y in range(30):
        print("main", y)



