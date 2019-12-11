# def sum(*sums) :
#      result = 0
#      for n in sums:
#          result += n
#      print(result)
# sum(1,2,3,4)


#return 后边跟什么值，函数就会返回什么值
# def fn():
#     def fn2():
#         print('hello')
#     return fn2()
#
# r = fn()
# print(r)



# def fn3():
#     for i in range(5):
#         if i == 3:
#            # break
#            #continue
#             return
#         print(i)
#     print("循环执行完毕")
#
# fn3()


def fn4():
    return 10

print(fn4)#函数对象
print(fn4())#fn4()是在调用函数