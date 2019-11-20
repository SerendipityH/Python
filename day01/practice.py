#水仙花数
num1=int(input("输入一个三位数"))



i= num1//100
j= num1//10%10
k= num1%10

print(i,j,k)
if pow(i,3)+pow(j,3)+pow(k,3) == num1:
    print("true")
else:
    print("false")
