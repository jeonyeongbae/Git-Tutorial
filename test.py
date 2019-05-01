import random
import time

w = ["cat", "dog", "fox", "monkey", "mouse",
     "panda", "frog", "snake", "wolf"]

n = 1

print("[타자 게임] 준비되면 엔터!")
input()

start = time.time()

q = random.choice(w)

while n <= 5:
    print("*문제", n)
    print(q)

    x = input()

    if q == x:
        print("통과")
        n = n + 1
        q = random.choice(w)
    else:
        print("오답! 다시도전")

end = time.time()


개인방송장비,개인방송조명,아프리카티비조명,음식촬영,방송조명,방송장비,제품촬영,야외촬영,셀카조명,캠핑랜턴,조명/노출용품,골든멀티미디어,알리딘,알라딘 유튜브조명,행복회로샵