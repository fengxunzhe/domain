# 线程池写法一
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def func(name):
    for x in range(100):
        print(name, x)
    pass


if __name__ == '__main__':

    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(func, name=f"线程{i}")
