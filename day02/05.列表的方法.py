#列表的方法
stus = ['孙悟空','猪八戒','沙和尚']

#print('原列表',stus)

#append()
#stus.append('唐僧')


#insert()
#向列表的指定位置插入一个元素
#stus.insert(2,'唐僧')


#extend
#使用新的序列来扩展当前序列
#需要使用一个序列作为参数
#stus.extend(['唐僧','白骨精'])
#stus +=['唐僧','白骨精']



#clear()
#清空序列
#stus.clear();


#pop()
#根据索引删除元素并返回被删除元素
#result = stus.pop(2)
#result =stus.pop(); #删除最后一个
#print("result" ,result)


#remove()
#删除指定值的元素，如果相同的值有多个，只会删除第一个
#stus.remove("猪八戒")

#reverse
#反转序列
#stus.reverse()



#sort()
#用来对列表中的元素进行排序，默认是升序
#如果降序排列，传入reverse=True作为参数
my_list= list("adbrmoemrbopemrpb")
print('修改前',my_list)
my_list.sort(reverse=True)
print('修改后',my_list)
