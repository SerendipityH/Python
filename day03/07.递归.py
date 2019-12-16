#尝试求10的阶乘（10!）
#创建一个变量保存结果
# n = 10
# for i in range(1,10):
#     print(i)


#创建一个函数
# def factorial(n):
#     '''
#     :param n:要求阶乘的数字
#     :return:
#     '''
#     #创建一个变量，来保存结果
#     result = n
#     for i in range(1,n):
#         result *= i
#     print(result)
#
# factorial(5)



# def factorial(n):
#    '''
#    :param n: 要求阶乘的数字
#    :return:
#    '''
#    #基线条件
#    if n == 1:
#        # 1的阶乘就是1
#        return 1
#    return n * factorial(n-1)
#
# print(factorial(3))



#联系
# 创建一个函数power来为任意数字做幂运算 n ** i
def power(n , i):
    '''
    :param n:要做幂运算的数字
    :param i: 做幂运算的次数
    :return:
    '''
    if i == 1:
        return n
    return n * power(n,i-1)

# print(power(8,6))
# print(8 ** 6)
#创建一个函数，用来检查一个任意的字符串是否是回文字符串
def check(s) :
    '''
    该函数用来检查指定的字符串是否为回文字符串
    :return:
    '''
    if len(s) < 2 :
        #字符串的长度小于2
        return True
    elif s[0] != s[-1]:
        return False
    #递归 包括第一个 ，不包括最后一个
    return check(s[1:-1])

print(check("hello"))
print(check("aba"))