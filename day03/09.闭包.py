#将函数作为返回值返回，也是一种高阶函数
# def fn() :
#     a = 10
#     #函数内部在定义一个函数
#     def inner() :
#         print('我是一个fn2',a)
#     return inner()
#
# r = fn()
#






#求多个平均值
# nums = [50,30,20,10,77]
#
# #sum()用来求一个列表中所有元素的和
# print()


#形成闭包的条件
# 1.函数嵌套
# 2.将内部函数作为返回值返回
# 3.内部函数必须要使用到外部函数的变量
def make_averager() :
    #创建一个列表，用来保存数值
    nums = []

    #创建一个函数
    def averager(n) :
        #将n添加到列表中
        nums.append(n)

        #求均值
        return sum(nums)/len(nums)
    return averager

averager = make_averager()

print(averager(1))
print(averager(2))
print(averager(3))