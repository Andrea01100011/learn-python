# 需求：
# 1. 允许⽤户最多选3次
# 2. 每次放出20个⻋牌供⽤户选择
# 3. 京[A-Z]-[xxxxx], 可以是数字和字⺟在组合
import random, string

# 定义车牌号数字和字母池
car_num_sample = string.digits+string.ascii_uppercase
# 定义首字母A-Z
first_letter = random.choice(string.ascii_uppercase)

count = 3
while count > 0:
    count -= 1
    num_list = []
    for i in range(20):
        car_num = f"京{first_letter}-{''.join(random.sample(car_num_sample, 5))}"
        num_list.append(car_num)
        print(i, car_num)
    
    choice = input("请选择: ").strip()
    if choice in num_list:
        exit(f"恭喜选购成功，您的新⻋牌是{choice}")
    else:
        print(f"未选中，还有{count}次机会")