def add(a, b):
    if a < 0 or b < 0:
        raise Exception('参数为负数')
    r = a + b
    return r


print(add(-1, 2))
