#高阶函数
#接受函数作为参数，或者将函数作为返回值的函数就是高阶函数
#创建一个列表
l = [1,2,3,4,5,6,7,8,9,10]


# 定义一个函数，用来检查
def fn2(i):
    if i % 2 == 0:
        return True
    return False


def fn3(i):
    if i > 5:
        return True
    return False
#定义一个函数
def fn(func,list) :


    '''
    
    :param list: 
    :return: 
    '''
    #创建一个新列表
    new_list = []

    #对列表进行筛选
    for n in list :
        # if n % 2 == 0 :
        #     new_list.append(n)
        if func(n) :
            new_list.append(n)
    #返回新列表
    return new_list

#print(fn(fn3,l))


#print(list(filter(fn3,l)))


#lambda函数表达式 匿名函数
#语法 :lambda 参数列表:返回值
def fn5(a , b):
    return a + b

lambda a,b : a+b

r = filter(lambda i : i > 5,l)
print(list(r))

#map()
#map()函数可以对迭代对象中的所有元素做指定的操作
r = map(lambda i : i+1,l)
print(list(r))