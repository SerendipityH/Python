#创建几个函数

def add(a, b):
    '''
    求任意两个数的和
    :param a:
    :param b:
    :return:
    '''
    return a + b

def mul(a ,b):
    '''
    求任意两个数的积
    :param a:
    :param b:
    :return:
    '''
    return a * b


#r = mul(123,456)
#print(r)


#希望函数可以在计算前，打印开始计算，计算结束后打印计算完毕
def fn():
    print('我是fn函数...')

def fn2():
    print('函数开始执行。。。')
    fn()
    print('函数执行结束。。。')

#fn2()

def new_add():
    print('函数开始执行。。。')
    add()
    print('函数执行结束。。。')


def begin_end(old):
    '''
    用来对其他函数进行扩展，使其他函数在可以在执行前开始执行，执行后打印执行结束
    old 要扩展的参数
    :return:
    '''
    def new_function(*args, **kwargs):
        print('开始执行。。。。')
        result = old(*args, **kwargs)
        print('执行结束。。。。')
        return result
    return new_function

#f = begin_end(fn)
f2 = begin_end(add)
f3 = begin_end(mul)
#r = f2(123,456)
#r =f3(1,2)

#print(r)

@begin_end
def say_hello():
    print('大家好')

say_hello()