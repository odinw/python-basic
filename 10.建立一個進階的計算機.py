# https://youtu.be/xyeiZqrXMvA?si=wjsZKXZYICoRSY6o

num1 = float(input("輸入第一個數:"))
op = input("輸入 運算符號:")
num2 = float(input("輸入第二個數:"))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("不支援的運算")