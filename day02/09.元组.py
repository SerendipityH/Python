#创建元组
#使用（）来创建元组

#my_tuple = ()

#print(my_tuple,type(my_tuple))

my_tuple = (1,2,3,4,5)
#元组是不可变对象，不能尝试为元组中的元素重新赋值
#print(my_tuple[3])


#当元组不是空元组时，括号可以省略

my_tuple = 10,20,30,40



#如果元组不是空元组，他里边至少有一个，
my_tuple = 50,
#print(my_tuple,type(my_tuple))


my_tuple = 10 , 20 ,30 ,40 ,50

#元组的解包（解构）
#解包就是将元组当中的每一个元素都赋值给一个变量
a,b,c,d,e = my_tuple

# print('a=',a)
# print('b=',b)
# print('c=',c)
# print('d=',d)
# print('e=',e)


a = 100
b = 300

#print(a,b)

#交换 a 和 b 的值，这是可以利用元组的解包

a , b = b ,a

#print(a,b)



my_tuple = 10 , 20 ,30 ,40 ,50
#对一个元组进行解包时，变量的数量必须和元组中的元素的数量一致
#也可以在变量前边添加一个 *，这样变量将会获取元组中所有剩余的元素
a , b , *c=my_tuple

a , *b, c= my_tuple
print(a)
print(b)
print(c)