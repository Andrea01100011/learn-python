# ⼀句代码打印10⾏“Alex⾦⻆⼤王是沙河最靓的仔”
print(10 * "Alex⾦⻆⼤王是沙河最靓的仔\n")

# 写⼀个列表，把你和你身边前后6个同桌的名字存进去，把Alex插⼊到你后⾯
class_mates = ["lbn", "zyt", "abc", "def", "haha", "xixi"]
print(class_mates)
class_mates.insert(1, "alex")
print(class_mates)

# 把上⼀题列表⾥的你⾃⼰删除掉，然后再追加到列表尾部
class_mates.remove("lbn")
print(class_mates)
class_mates.append("lbn")
print(class_mates)