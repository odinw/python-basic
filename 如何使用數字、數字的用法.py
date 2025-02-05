from math import *


# 3.如何使用數字、數字的用法
# https://youtu.be/eRnRi3n0gIM?si=wFbiKNYgUiJcBsDN

print("基本")
print(7)
print(7.2)
print(-7)
print(2*3)
print(6/3)

print("取商")
print(8//2)
print(8//3)
print(8//4)
print(8//5)

print("先乘除 後加減")
print(8+8*5)

print("括號優先")
print((8+8)*5)

number = 10
print("取餘數")
print(number/5);

print("數字 轉 字串")
print("印出數字" + str(number))

#不合法
#print("印出數字" + number)

print("絕對值")
print(abs(-8))

print("次方")
print(pow(2,3))

print("取最大")
print(max(5, 1, 3))

print("取最小")
print(min(5, 1, 3))


print("四捨五入")
print(round(5.4))
print(round(5.5))

# math 函式庫
print("無條件捨去")
print(floor(5.4))
print(floor(5.5))

print("無條件進位")
print(ceil(5.4))
print(ceil(5.5))

print("開根號")
print(sqrt(4))
print(sqrt(9))