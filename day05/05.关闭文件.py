# #打开文件
# file_name = 'demo.txt'
#
# #调用open()来打开文件
# # file_obj = open(file_name)
# #
# # #read()方法，用来读取文件中的内容
# # content = file_obj.read();
# # print(content)
# #
# # #关闭文件
# # #调用close()方法来关闭文件
# # file_obj.close()
#
#
# #with .. as 语句
# with open(file_name) as file_obj:
#     # 在with语句中可以直接使用file_obj做文件操作
#     print(file_obj.read())


file_name = 'hello.txt'
try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name}文件不存在')