A = list(range(90, 101))
B = list(range(80, 90))
C = list(range(60, 80))
D = list(range(40, 60))
E = list(range(0, 40))

point = int(input("输入你的成绩: "))
if point in A:
    print("你的成绩是A")
elif point in B:
    print("你的成绩是B")
elif point in C:
    print("你的成绩是C")
elif point in D:
    print("你的成绩是D")
else:
    print("你的成绩是E")