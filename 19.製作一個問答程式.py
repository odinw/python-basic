# https://youtu.be/q_X4amTktHU?si=u1TUEsxrmt-bHdLd

from lesson_19.question import Question

puzzles = [
    Question("8+9=? (a)17 (b)87 (c)跨啥啦 : ", "b"),
    Question("女生說[沒關係]的意義是? (a)真的沒關係 (b)有關係 (c)快氣鼠ˋ^ˊ : ", "c")
]

def test(questions):
    score = 0
    for p in puzzles:
        answer = input(p.description)
        if (answer == p.answer):
            score += 1
    print("總題數" + str(len(puzzles)) +  " 答對題數: " + str(score))

test(puzzles)