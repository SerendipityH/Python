#作用域
#
a = 20
# def fn():
#     global a #全局变量a
#     a = 10
#     print('函数内部：','a = ',a)
#
# fn()
#
# print('函数外部','a = ',a)


scop = locals();
print(scop)