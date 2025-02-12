# https://youtu.be/aWfeDWEU6tM?si=PyIqA_-gSK3CCRfl
import random

result =  str(random.randrange(1, 100))
guess = ""
limit = 3
guess_count = 0
print("歡迎來到猜數字遊戲 0~99")


while guess != result and guess_count < limit:
    guess = input("猜猜看~ ")
    if guess > result:
        print("偷偷告訴你 要小一點")
    elif guess < result:
        print("欸欸 要大一點啦")
    guess_count += 1

if guess == result:
    print("答對了!! 過關~")
else:
    print("歐歐 猜太多次 失敗惹")