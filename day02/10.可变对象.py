# #可变对象
# a = [1,2,3]
# print('修改前',a,id(a))
#
# a[0] = 10
# print('修改后',a,id(a))
# #
# a = [4,5,6]
# print('修改后',a,id(a))


a = [1,2,3]
b = a
#b[0] = 10
b = [3,4,5]
# print('a',a,id(a))
# print('b',b,id(b))


# == != is is not
# == != 比较的是对象的值是否相等
#is is not 比较的是对象的id 是否相等 （比较两个对象是否为同一个对象）
a = [1,2,3]
b = [1,2,3]
print(a,b)
print(a==b)
print(a is b)

