#创建两个集合
s = {1,2,3,4}
s2 = {3,4,5,6,7}

# &交集运算
result = s & s2


#|并集运算
result = s | s2


#-差集
result = s - s2 #{1, 2}


#亦或集
result = s ^ s2 #{1, 2, 5, 6, 7}

# <=检查一个集合是否是另一个集合的子集
#如果一个集合中的元素全部都在另一个集合中出现
a = {1,2,3}
b = {1,2,3,4,5}
result = a <= b


result = {1,2,3} <= {1,2,3} #True
result = {1,2,3,4,5} <= {1,2,3} #False
print('result = ',result)
print(s,s2)