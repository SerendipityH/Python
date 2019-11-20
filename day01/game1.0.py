
player_name = '孙悟空'
boss_name = '白骨精'
#显示欢迎信息
print('-'*20,f'欢迎光临《{player_name}大战{boss_name}》','-'*20)
#显示身份选择信息
print('请选择你的身份:')
print(f'\t1.{player_name}')
print(f'\t2.{boss_name}')
#游戏的身份选择
player_choose = input('请选择[1-2]:')

#打印一条分割线
print("-"*67)
#根据用户的选择来显示不同的提示信息
if player_choose == '1':
    #选择1
    print(f'你已选择了1，你将以->{player_name}<-的身份来进行游戏！')
elif player_choose == '2':
    print(f'你竟然选择了{boss_name}，太不要脸了，你将以->{player_name}<-的身份来进行游戏')
    #选择2
else :
    #选择3
    print(f'你的输入有误，系统将自动分配身份，你将以->{player_name}<-的身份来进行游戏')



#进入游戏
#创建变量，来保存玩家的申明哲和攻击力
player_life = 2 #生命值
player_attach = 2 #攻击力


#创建变量，保存boss的生命值和攻击力
boss_life = 10
boss_attack = 10
#打印一条分割线
print("-"*67)
#显示玩家的信息（攻击力、生命值）
print(f'{player_name}，你的生命值是 {player_life}，你的攻击力是 {player_attach}')

#由于游戏选项是需要反复显示,
while True :

#显示游戏选项，游戏正式开始
  print('请选择你要进行的操作:')
  print('\t1.练级')
  print('\t2.打boss')
  print('\t3.逃跑')
  #打印一条分割线
  print("-"*67)
  game_choose=input('请选择你要进行的操作[1-3]:')

  #处理用户的选择
  if game_choose == '1':
    #增加玩家的生命值和攻击力
      player_life +=2
      player_attach +=2
      # 打印一条分割线
      print("-" * 67)
      print(f'恭喜你升级了，你的生命值是 {player_life}，你的攻击力是 {player_attach}')
  elif game_choose == '2':
      #玩家攻击boss
      #减去boss生命值，减去的生命值应该等于玩家的攻击力
      boss_life -=player_attach

      # 打印一条分割线
      print("-" * 67)
      print(f'->{player_name}<-攻击了 ->{boss_name}<-')
      #检查boss是否死亡
      if boss_life <=0 :
          #boss 死亡，player胜利，游戏结束
          print(f'-> {boss_name}<- 受到了{player_attach}点伤害')
          print('->游戏胜利<-')
          break
      #boss反击玩家
      player_life -= boss_attack
      # 打印一条分割线
      print("-" * 67)
      print(f'->{boss_name}<-攻击了 ->{player_name}<-')
      #检查玩家是否死亡
      if player_life <=0:
          #玩家死亡
          print(f'你受到了{boss_attack}点伤害，Game Over!')
          break
  elif game_choose == '3' :
      #逃跑，退出游戏
      print("Game Over !!!")
      break
  else :
      print('你的输入有误，请重新输入！！！！')