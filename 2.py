# 线程写法二

from threading import Thread


class func(Thread):
    def run(self):
        for i in  range(20):
            print("func", i)


if __name__ == '__main__':
    t = func()
    t.start()

    for x in range(20):
        print("mian", x)
