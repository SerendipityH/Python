#集合
#使用{}来创建集合
#只能存储不可变对象
s = {1,4,5,2,3,9,7,6}



#使用set()函数来创建
s = set()#空集合
#可以通过set()来将序列和字典转换为集合
s = set([1,2,3,34,5,5,56,67])
s = set('hello')
s = set({'a':1,'b':2,'c':3}) #使用set转集合时 ，只会转键


#创建集合
s = {'a','b',1,2,3}
#使用add()向集合中添加元素
#s.add(30)




#使用update()将一个集合中的元素添加到当前集合中

s2 = set('hello')
s.update(s2)
s.update((10,20,30,40,50))
s.update({10:'ab',20:'bc',1000:'ef'})


#pop()随机删除一个集合中的元素
result = s.pop()
print(result)
print(s,type(s))