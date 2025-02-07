
# https://youtu.be/orCsnSHc8Mo?si=YTaeRdSsQGFkrmyy

scores = [50,30,90,80,100]
print("同種資料類別 列表")
print(scores)


member = ["Audin", 18, True]
print("多種資料資料 列表")
print(member)


print("列表索引")
print(scores[0])


print("列表索引 倒數")
print(scores[-1])


print("列表連取多筆 從[起始索引]到[結束索引] 但不包含[結束索引]本身")
print(scores[1:3])


print("列表連取多筆 從[起始索引]取到底")
print(scores[1:])


print("列表連取多筆 從索引0取到[指定的倒數索引] 但不包含[指定的倒數索引]本身")
print(scores[:4])


scores[0] = 55
print("修改指定索引值")
print(scores)


scores.append("a")
print("列表 結尾加值 (不限資料類型 都可加)")
print(scores)


scores.extend(member)
print("把另一個列表 併入結尾")
print(scores)


scores.insert(1, "b")
scores.insert(3, "b")
print("加入值到指定索引")
print(scores)


print("找指定值 符合的第一個索引")
print(scores.index("b"))


print("計算指定值的數量")
print(scores.count("b"))


scores.remove("b")
print("刪除 第一個找到的指定值")
print(scores)


last = scores.pop()
print("取出最後一個值 (該值會從列表中移除)")
print(scores)
print(last)


scores.reverse()
print("倒序")
print(scores)


scores.clear()
print("清空列表")
print(scores)

scores = [5, 9, 1]
scores.sort()
print("排序 小到大")
print(scores)