
if __name__ == '__main__':
    with open('1.txt', mode='r', encoding="utf-8") as f:
        text = f.read()
        res = ""
        for i in text:
            res = res + i

        # print(res.replace())
        # print(type(res))
