# https://youtu.be/uHV4V-z5c8E?si=M3wmgrykKb8uDu0P


file = open("16-test-io/document.txt", mode="r")
print("讀第1行") 
print(file.readline())
print("接續第2行直到讀完全部")
print(file.read())
# 關閉檔案 避免佔用資源
file.close()

print("[迴圈印出]")
file_for_loop = open("16-test-io/document.txt", mode="r")
for line in file_for_loop:
    print(line)
file_for_loop.close()

print("[讀取成列表]")
list = open("16-test-io/document.txt", mode="r")
print(list.readlines())
list.close()


print("[結尾加資料]")
append = open("16-test-io/document.txt", mode="a")
append.write("\nappend new data")
append.close()
check_append = open("16-test-io/document.txt", mode="r")
print(check_append.read())
check_append.close()

print("[寫入中文 要指定編碼]")
tw = open("16-test-io/document.txt", mode="a", encoding="utf-8")
tw.write("\n寫入中文成功")
tw.close()
check_tw = open("16-test-io/document.txt", mode="r", encoding="utf-8")
print(check_tw.read())
check_tw.close()

print("[覆寫]")
data = '''1
2
3'''
overwrite = open("16-test-io/document.txt", mode="w")
overwrite.write(data)
overwrite.close()
check_overwrite = open("16-test-io/document.txt", mode="r")
print(check_overwrite.read())
check_overwrite.close()

print("[無須close的寫法]")
with open("16-test-io/document.txt", mode="r") as auto_close:
    print(auto_close.read())