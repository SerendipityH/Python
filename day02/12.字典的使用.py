#使用dict()函数创建字典
#每一个参数都是一个键值对，这种方式创建的的字典，key都是字符串
d = dict(name = '孙悟空',age = 18 , gender ='男')


#也可以将一个
d = dict([('name','孙悟饭'),('age','18')])

#len()获取字典键值对的个数
#print(d,type(d))

#print(len(d))

#in 检查字典中是否包含指定的键

# not in 检查字典中是否不包含指定的键

#print('hello' in d)


#获取字典中的值，根据键来获取值
#语法 d[key]
#print(d["name"])

n = 'name'
#print(d[n])

#通过[] 来获取值时，如果键不存在，会抛出异常 key error

#get(key[.default])
#可以指定默认值，取不到值时会返回默认值
#print(d.get('hello'),'默认值')

#修改字典 存在覆盖，不存在则添加
#d[key] = value

d['name'] = 'sunwukong' #修改字典的key-value
d['address'] = '花果山' #向字典中添加key-value
#print(d)

#向字典中添加key-value
#如果key 已经存在与字典中，则返回key 的值，不会对字典做任何操作
#如果key 不存在，则向字典中添加这个key ，并设置value
result = d.setdefault('name','猪八戒')
print(result)


#将其他字典中的key-value 添加到当前字典中
#如果有重复 则会覆盖
# d = {'a':1,'b':2,'c':3}
# d2 = {'b':4,'e':5}
#
# d.update(d2)
#
# print(d)



#删除，可以使用del来删除

d = {'a':1,'b':2,'c':3}
#del d['a']
#print(d)

#popitem()
#删除字典的一个键值对，一般都会删除最后一个键值对
#删除空字典会报错
#删除之后，他将会删除的key-value 作为返回值
#result = d.popitem();
#print(result)


#pop
#根据key 删除字典中的key-value
#会将被删除的value 返回
#指定默认值，在删除不存在的key时，不会报错，会返回默认值
# result = d.pop('a')
# result = d.pop('z','默认值')
# print(result)

#clear()清空字典


#copy
#该方法用于对字典进行浅复制
#注意，浅复制会简单复制对象内部的值，如果值也是一个可变对象，这个可变对象不会复制
# d = {'a':1,'b':2,'c':3}
# d2 = d.copy()
# print(d2 ,id(d2))
# print(d,id(d))

d = {'a':{'name':'孙悟空','age':18},'b':2,'c':4}
d2 = d.copy();
d2['a']['name'] = '猪八戒'
d2['b'] = 5
print(d2 ,id(d2))
print(d,id(d))