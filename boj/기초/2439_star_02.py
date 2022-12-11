# 220916_boj_2439_별찍기2_구현_브론즈4

N = int(input())

for i in range(1 , N + 1):
    print(' '* (N-i) + '*' * i)