"""
Converts any string to int without str() & int() funcs.
"""
def dig(str_):

    res = 0

    for i in str_:
        d = ord(i)
        cnt = 1

        while d // 10 != 0:
            d = d // 10
            cnt += 1

        res = res * (10 ** cnt) + ord(i)

    return res


if __name__ == '__main__':

    dig(input())
