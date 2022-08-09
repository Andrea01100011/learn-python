# 猜数字小游戏游戏
 
"""
介绍：
    猜数字游戏是一个古老的密码破译类、益智类小游戏，通常由两人参与，一个设置一个数，另一个人猜数字。
知识点：
    1、数据类型转换
    2、随即模块 random 使用
    3、while 循环语句
    4、if/elif/else 条件语句
    5、字符串拼接
"""
 
 
import random   # 导入随机数random模板
 
# 定义变量
top = 100
bottom = 1
 
i = 1       # 记录输入次数
 
random_num = random.randint(1, 100)  # 随机产生一个1-100之间的数
print('答案：', random_num) 
 
print('=====欢迎来到猜数字游戏=====')
 
while True:
 
    # 带提示字符串拼接输入
    num = float(input('请输入一个' + str(bottom) + '-' + str(top) + '的整数：'))
 
    # 重新输入
    if num > int(num) or num < 0:
        print('请输入正整数！！！')
        continue
 
    # 结束游戏
    if num == 0:
        print(' ========退出游戏========')
        break
 
    # 根据输入的数字给予提示
    if random_num == num:
        print('恭喜您猜对了')
        break
 
    elif random_num > num:
        print('您猜的数字小了')
        bottom = int(num)
 
    elif random_num < num:
        print('您猜的数字大了')
        top = int(num)
 
    # 提示语
    if i % 5 == 0:
        print('不是吧！您太水了！')
 
    i += 1