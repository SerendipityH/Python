import os
from pprint import pprint
#获取指定目录的结构
r =os.listdir()
#获取当前所在的目录
r = os.getcwd()
#切换目录
os.chdir('..')

#创建目录
os.mkdir('aaa')
#删除目录
os.rmdir('aaa')

#删除文件
os.remove('aa.mp3')

pprint(r)