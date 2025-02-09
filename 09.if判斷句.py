# https://youtu.be/z3cUEOyiQIw?si=yTv2_hPFlxFJNvmC

hungry = True
if hungry:
    print("吃點東西吧")
else:
    print("晚點再吃")


print("多狀況判斷")
score = 70
if score == 100:
    print("獎金1000")
elif score >= 80:
    print("獎金500") 
elif score >= 60:
    print("獎金100")
else:
    print("你給我300")

print("多條件 [且] and")
rainy = True
if score == 100 and rainy:
    print("我給你100")
else:
    print("你給我100")

print("多條件 [或] or")
rainy = True
if score == 100 or rainy:
    print("我給你100")
else:
    print("你給我100")

print("布林值反向 not")
rainy = False
if score == 100 or not(rainy):
    print("我給你100")
else:
    print("你給我100")

print("數值 [不等於] !=")
rainy = True
if score != 100 or not(rainy):
    print("我給你100")
else:
    print("你給我100")

def max_num(num1, num2):
    if (num1 > num2):
        return num1
    else:
        return num2
result = max_num(55, 88)
print(result)
