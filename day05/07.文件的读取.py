import pprint

file_name = 'demo.txt'
with open(file_name,encoding='utf-8') as file_obj:
    #print(file_obj.readlines())
    #print(file_obj.readline())
    for t in file_obj:
        print(t)