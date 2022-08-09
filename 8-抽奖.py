# 集合  set    无序且不重复
#
# set1 = {1,2,3,4,5}


five_men_fight_bg = {"ian", "Alex", "佩奇", "Old_Shang", "智哥", "black_girl"}

happy_day = {"唐艺昕", "李孝利", "black_girl", "刘诗诗", "李沁", "柳岩", "ian"}

# 要找出，同时参演了，这两部电影的人，都有谁。（交集）
# print(five_men_fight_bg.intersection(happy_day))
#
# print(five_men_fight_bg & happy_day)
#
#
# # 这两部电影中，一共包含了有，哪些演员。(并集)
# print(five_men_fight_bg.union(happy_day))
#
# print(five_men_fight_bg | happy_day)
#
# # 参演了抗战片，五男大战黑姑娘的演员中，谁没有参演，开心的一天。(差集)
# print(five_men_fight_bg.difference(happy_day))
#
# print(five_men_fight_bg - happy_day)
#
# # 哪些演员，只参演了一部电影。(交叉补集)
# print(five_men_fight_bg.symmetric_difference(happy_day))
#
# print(five_men_fight_bg ^ happy_day)


# print(five_men_fight_bg[1])


# set1 = {1,2,3,4,5,1,2,3,4,5,6,6,6,6,6,6,6,7,8,9}
# print(set1)


# lis1 = [1,2,3,4,1,2,3,4,5,5,5,5,6,7,8,9,10]
#
# print(list(set(lis1)))


# 流程控制结构
# 一、顺序结构
# 二、选择结构  分支结构 条件语句
# 三、循环结构

# 3.1 循环嵌套

# flag = True  #生命体征
# #控制楼层
# for floor in range(1,6):
#     print(f"欢迎来到第{floor}层")
#
#     if floor == 3:
#         print("咋还不让进了呢，可惜啊可惜~~")
#         continue
#
#     #控制房间号
#     for room in range(1,9):
#         print(f"{floor}0{room}")
#
#         if floor == 4 and room == 4:
#             print("我的草原我的马呀，你咋能（*&*&……%%￥……%%（*")
#             flag = False
#             break
#             # exit()
#     if flag != True:
#         break

# 循环控制保留字
# continue:跳过本次循环，直接开始下一次循环
# break:直接跳出循环

# 算法
# hight = 100
# distance = 0
#
# for i in range(10):
#     # 记录下落长度
#     distance = distance + hight  # distance += hight
#
#     # 计算反弹高度
#     hight /= 2  # hight = hight / 2
#
#     if i == 9:
#         break
#
#     #记录反弹长度
#     distance += hight
#
# print(f"共经历了{distance}米")


# 年会抽奖
import faker  # pip install Faker
import random

alex = faker.Faker(locale="zh_CN")  # en_US

staff_list = []

for i in range(1, 301):
    staff_list.append(alex.name())

level = [30, 6, 3]

for i in range(3):
    winner_list = random.sample(staff_list, level[i])

    for w in winner_list:
        staff_list.remove(w)

    print(f"获得{3 - i}等奖的是：{winner_list}")

    print(f"还剩{len(staff_list)}个人")
