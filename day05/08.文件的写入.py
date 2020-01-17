file_name = 'demo.txt'
#使用open()打开文件时必须要指定打开文件所要做的操作(读、写、追加)
#如果不指定操作类型
#r 表示只读
#w 表示可写的 ;使用w来写入文件时，如果文件不存在则会创建，如果文件存在则会删除原来的重新写入
#a 追加
#x用来新建文件
#+ 为操作符增加功能
#r+ 既可读又可写
with open(file_name,'a',encoding='utf-8') as file_obj:
    #write()来写入内容
    file_obj.write("hello world4444444444")