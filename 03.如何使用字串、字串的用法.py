

# https://youtu.be/dNFI2c007Sw?si=p_J7ctviA5BNbvFk

print("hello")

print("換行")
print("Hi \n Audin")

print("雙引號 \" ")

print("字串連接")
print("字串" + "連接")

name = "Audin"
print("Hi " + name)

#函式
print("小寫 " + name.lower())
print("大寫 " + name.upper())

print("是否為 全大寫")
print(name.isupper())

print("是否為 全小寫")
print(name.islower())

print("流利方法 是否為 全小寫")
print(name.lower().islower())

print("字串索引")
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#print(name[5]) #不存在的索引 會報錯

print("找指定字串的索引")
print(name.index("n"))


print("替換")
print(name.replace("n", "N"))