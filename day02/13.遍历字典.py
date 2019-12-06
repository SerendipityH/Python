#遍历字典
#keys()会返回字典的所以key
d = {'name':'孙悟空','age':18,'gender':'n'}
#print(d.keys())

# #通过遍历keys()来获取的键
# for k in d.keys():
#     print(k,d.get(k))

#values()
#该方法返回一个序列，序列中保存有字典的值
# for v in d.values():
#     print(v)

print(d.items())
#该方法会返回字典中所有的项
for k,v in d.items():
    print(k,v)

