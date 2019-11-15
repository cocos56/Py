#import random
#secret = random.randint(1,10)
secret = 3
print("不妨猜一下python现在心里想的是哪个数字：")
print('你只有三次机会哦~')
count = 1
print('请进行第%d次尝试' % count)
temp = input()
guess = int(temp)
while count < 3:
	if(guess != secret):
		if guess > secret:
			print("哥，大了大了~~~")
		else:
			print("嘿，小了，小了~~~")
		count += 1
		print('请进行第%d/3次尝试' % count)
		temp = input()
		guess = int(temp)
	else:
		print("我草~，你是python的蛔虫吗？！")
		print("哼，猜中了也没有奖励！")
		break
else:
	if(guess != secret):
		print('你猜错次数已达三次')
	else:
		print("我草，你是python心里的蛔虫吗？！")
		print("哼，猜中了也没有奖励！")

print("游戏结束，不玩啦^_^")
