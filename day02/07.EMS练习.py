#显示系统的欢迎信息
print('-'*20, '欢迎使用员工管理系统','-'*20)

#创建一个列表，用来保存员工的信息
emps = ['\t孙悟空\t18\t男\t花果山']
#创建一个死循环
while True:
    #显示用户选项
    print('请选择要做的操作：')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')

    user_choose = input('请选择[1-4]:')
    # 打印分割线
    print('-' * 62)
    #根据用户的选择来做相关的操作
    if user_choose == '1':
        #打印表头
        print('\t序号\t姓名\t年龄\t性别\t住址')
        #创建一个变量，来表示员工的序号
        n = 1

        #显示员工信息
        for emp in emps:
            print(f'\t{n}\t{emp}')
            n += 1
        pass
    elif user_choose == '2':

        #添加员工
        #获取要添加员工的信息，姓名、年龄、性别、住址
        emp_name = input('请输入员工姓名：')
        emp_age = input('请输入员工的年龄：')
        emp_gender = input('请输入员工的性别：')
        emp_address = input('请输入员工的住址：')

        #创建员工信息
        emp = f'{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}'
        #显示提示信息
        print('以下员工将会被添加到系统中')
        print('姓名 年龄 性别 住址')
        print(emp)
        # 打印分割线
        print('-' * 62)
        user_confim = input('是否确认该操作[Y/N]')
        #判断
        if user_confim == 'y' or user_confim == 'yes':
            #确认
            emps.append(emp)
            print('添加成功！')
        else :
            #取消操作
            print('添加已取消')

    elif user_choose == '3':
        #删除员工，根据员工的序号来删除员工
        #获取要删除员工的序号
        del_num = int(input('请输入要删除员工的序号:'))
        if 0 < del_num <= len(emps):
            del_i = del_num -1
            #显示提示
            # 显示提示信息
            print('以下员工将会被添加到系统中')
            print('序号 姓名 年龄 性别 住址')
            print(f'\t{del_num}\t{emps[del_i]}')
            # 打印分割线
            print('-' * 62)
            user_confim = input('是否确认该操作[Y/N]')
            # 判断
            if user_confim == 'y' or user_confim == 'yes':
                emps.pop(del_i)

                print("员工已被删除！")
            else :
                print('操作取消！')
        else :
            print('您的输入有误，请重新操作！')

    elif user_choose == '4':
         # 退出

         print('欢迎使用！再见!')
         break
    else :
        print('你的输入有误，请重新选择！')

#打印分割线
    print('-'*62)