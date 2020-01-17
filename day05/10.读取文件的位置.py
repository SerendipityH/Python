with open('demo.txt','rb') as file_obj:
    #(file_obj.read(100))
    #seek可以修改当前读取的位置
    file_obj.seek(5)
    #tell()方法用来查看当前读取到的位置
    print('当前读取到了-->',file_obj.tell())