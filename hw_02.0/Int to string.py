def dig():
    a = input()
    if type(a) is str:
        res = 0
        for i in a:

            cnt = 1
            d = ord(i)
            while d // 10 != 0:
                d = d // 10
                cnt += 1
            res = res * (10 ** cnt) + ord(i)

        return res
    elif type(a) is int:
        return a
    else:
        return

dig()
