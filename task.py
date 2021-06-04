from decimal import Decimal


def task1(postal_code_start, postal_code_end):
    def remove_dash(x):
        return int(x.replace('-', ''))
    postal_code_start, postal_code_end \
        = remove_dash(postal_code_start), remove_dash(postal_code_end)
    postal_code = []
    for x in range(postal_code_start, postal_code_end):
        # exclude postal codes xx-000
        if x % 1000 == 0:
            pass
        else:
            postal_code.append("%02d-%03d" % divmod(x, 1000))
    return print(postal_code)


def task2(ns, n):
    return print(list(set(range(1, n+1)) - set(ns)))


def task3():
    return print([Decimal(20 + x * 5) / 10 for x in range(8)])

#task1("79-900", "80-155")
#task2([2,3,7,4,9], 10)
#task3()