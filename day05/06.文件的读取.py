# file_name = 'demo2.txt'
# try:
#     with open(file_name,encoding='utf-8') as file_obj:
#         #默认值为-1
#         print(file_obj.read())
# except FileNotFoundError:
#     print(f'{file_name}文件不存在')


#读取大文件的方式
file_name = 'demo.txt'
try:
    with open(file_name,encoding='utf-8') as file_obj:
        #定义一个变量，来保存文件的内容
        file_content = ''
        #默认值为-1
        #定义一个变量，来指定每次读取的大小
        chunk = 100;
        #创建一个循环来读取文件的内容
        while True:
            content = file_obj.read(chunk)
            #检查是否读取到了内容
            if not content:
                # 内容读取完毕，退出循环
                break
            #print(content,end='')
            file_content += content
except FileNotFoundError:
    print(f'{file_name}文件不存在')


print(file_content)