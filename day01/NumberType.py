import math
import random
#分类：整数、浮点数、复数

'''
整数：python可以处理任意大小的整数，当然包括负整数
'''

num1 = 10
num2 = num1

#连续定义多个变量
num3 = num4 = num5 =1
print(num3,num4,num5)

#交互式赋值定义变量
num6,num7 = 6,7
print(num6,num7)


'''
浮点数由整数部分和小数部分组成，浮点数运算可能会有四舍五入
'''
f1 = 1.1
f2 = 2.2

print(f1+f2)

'''
复数：实数部分和虚数部分构成
'''

'''
数字类型转换
'''
print(int(1.2))

print(float(3))

print(int("123"))

print(float("12.4"))

#print(int("abc"))

#print(int("123abc"))
#只有作为正负号才有意义
print(int("+123"))

#print(int("12+3"))

print(int("-123"))

#print(int("12-3"))


#返回数字的绝对值

a1 = -10
a2 = abs(a1)

print(a2)


#比较两个数的大小
print((6>9)-(6<9))

print((10>9)-(10<9))

print((9>9)-(9<9))

#
a3 = 4

a4 = 5

#返回给定参数的最大值
print(max(1,2,3,4,4,5))

#返回给定参数的最小值
print(min(1,2,3,34,45,5))


#求x的y次方  2^5
print(pow(2,5))


#round(四舍五入)返回

print(round(3.456))

print(round(3.56))

print(round(3.456,2))

print(round(3.546,2))


#向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))

#向下取整
print(math.floor(18.1))
print(math.floor(18.9))
#返回整数部分与小数部分（都是浮点数）
print(math.modf(22.3))

#开方
print(math.sqrt(16))

#随机数

print(random.choice([1,3,4,5,6]))

print(random.choice(range(5))) #range(5) == [0,1,2,3,4]

print(random.choice("python")) #"python" == ["p","y","t","h","o","n"]

#产生一个1-100之间的随机数
r1=random.choice(range(100))+1
print(r1)

#random.randrange([start] ,stop ,[step])
#start--指定范围的开始值，包含在范围内
#stop--指定范围的结束值，不包含在范围内
#step--步长（递增基数）
print(random.randrange(1,100,2))


#从0-99选取一个数 start默认是0 step默认是1
print(random.randrange(100))

#随机生成[0,1)之间的一个数（浮点数）
print(random.random())



list = [1,2,3,4,5]
#将序列的所有元素随机排序
random.shuffle(list)
print(list)

#随机生成一个实数，在[3,9]的范围内
print(random.uniform(3,9))