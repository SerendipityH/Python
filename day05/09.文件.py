file_name = r'D:\Tools\wangyiyun\电台节目\-荼靡阿 - 余情未了（原唱）.mp3'
#读取模式
#t 读取文本文件（默认）
#b 读取二进制
with open(file_name,'rb') as file_obj:
    #print(file_obj.read(100))
    new_name = 'aa.mp3'
    with open(new_name,'wb') as new_obj:
        #定义每次读取的大小
        chunk = 1024*100
        while True:
            #从已有对象中读取数据
            content = file_obj.read(chunk)
            #内容读取完毕
            if not content:
                break
            #将读取的数据写入到新对象中
            new_obj.write(content)
