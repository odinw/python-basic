# https://youtu.be/4KkK-8CrEz4?si=omCIUFMpXaGg_tW4

print("string:")
for char in "Audin":
    print(char)

print("list:")
for member in [5, 1, 3]:
    print(member)

print("tuple:")
for member in (5, 1, 3):
    print(member)

print("dictionary:")
for member in {"A":"Audin", "T":"Tom"}:
    print(member)


print("控制迴圈跑幾次:")
for index in range(3):
    print(index) 

print("從1到5:")
for index in range(1, 6):
    print(index) 




def power(base, index):
    result = 1
    for i in range(index):
        result *= base
    return result;

b = int(input("請輸入指數的底數:"))
i = int(input("請輸入指數的次方數:"))
r = power(b, i)
print("答案為 " + str(r))