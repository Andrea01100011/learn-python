# 300员工
# ⼀等奖3名
# ⼆等奖6名
# 三等奖30名
# 规则：
# 1. 共抽3次，第⼀次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖
# 2. 每个员⼯限中奖⼀次，不能重复
# 解题思路：
# 1. ⽣成⼀个员⼯列表，⽤random模块从⾥⾯取随机值
# 2. 取完值之后，⽴刻从员⼯⼤列表⾥把中奖⼈删掉，即可防⽌其再次中奖
import random
name_list = list(range(1, 301))

print("------------------抽取三等奖------------------")

third_prize = random.sample(name_list, 30)
print("三等奖中间号码: ", third_prize)
name_list = list(set(name_list).difference(set(third_prize)))

print("------------------抽取二等奖------------------")
second_prize = random.sample(name_list, 6)
print("二等奖中间号码: ", second_prize)
name_list = list(set(name_list).difference(set(second_prize)))

print("------------------抽取一等奖------------------")
first_prize = random.sample(name_list, 3)
print("一等奖中间号码: ", first_prize)

print("------------------抽奖总结------------------")
print("获得三等奖的有: ", third_prize)
print("获得二等奖的有: ", second_prize)
print("获得一等奖的有: ", first_prize)