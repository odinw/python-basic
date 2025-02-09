

def hello():
    print("定義函式 hello")
hello()


def hello_name(name):
    print("hello " + name)

hello_name("函式參數 Audin")


def hello_name_age(name, age):
    print("函式參數多參數 hello " + name + str(age))
hello_name_age("Audin", 18)


def add(num1, num2):
    return num1+num2;
add_result = add(2, 3)
print("回傳:" + str(add_result))

no_return = hello()
print("無回傳:")
print(no_return)


def return_break():
    print("這行會印出")
    return
    print("被return 中斷 無法印出")
return_break()