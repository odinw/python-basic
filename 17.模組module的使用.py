#https://youtu.be/SV5OqR46kEM?si=FdFhm8ioGqNPX7ku

# import 相對目錄下的自寫腳本，並改名(簡化名稱)來用
from lesson_17 import import_call_function as call


print("呼叫自寫的模組:")
result = call.Hi("Audin")
print(result)


# terminal 指令安裝第三方WebAP模組，ex: pip install django