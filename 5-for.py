black_gf_age = 24
for i in range(3):
    guess = int(input("猜猜⿊姑娘多⼤了>>:"))
    if guess > black_gf_age:
        print("猜的太⼤了，往⼩⾥试试...")
    elif guess < black_gf_age:
        print("猜的太⼩了，往⼤⾥试试...")
    else:
        exit("恭喜你，猜对了...") # 退出程序

# 打印50-100间的奇数
for i in range(50, 100): # 可以定义区间
    if i % 2 == 1:
        print(i)

# ⼀栋楼有5层，每层8间屋⼦，要求你把本楼所有的房间号打印⼀遍， 格式“1层-104”
for i in range(1,6):
    for j in range(1,9):
        print(f"{i}层-{i}0{j}室")