# 설탕 배달

N = int(input()) # 배달할 설탕의 무게
ans = 0

if N >= 5 :
    i = N//5
    err = 0
    while True:
        if (N - (5 * i)) % 3 == 0:
            ans = err + N//5 + (N - (5 * i))//3
            break
        else:
            i -= 1
            err -= 1

if N == 3:
    ans = 1
elif N == 4 or N == 7 :
    ans = -1

print(ans)
