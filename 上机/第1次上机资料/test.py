name=input("请输入您的姓名：")
chinese=float(input("请输入语文成绩："))
math=float(input("请输入数学成绩："))
english=float(input("请输入英语成绩："))
average=(chinese+math+english)/3
if average>=85:
    print(name," 获一等奖")
elif average>=75:
    print(name," 获二等奖")
elif average>=60:
    print(name," 获三等奖")
else:
    print(name,"没有获奖")
