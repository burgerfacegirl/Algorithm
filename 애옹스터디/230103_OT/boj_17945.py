# 230103_OT_boj_17945_통학의 신

A, B = map(int,input().split())

answer1, answer2 = ((-2*A) + (((2*A)**2) - (4*B))**0.5)//2, ((-2*A) - (((2*A)**2) - (4*B))**0.5)//2

if answer1 != answer2:
    print(int(answer2), int(answer1))
else:
    print(int(answer1))