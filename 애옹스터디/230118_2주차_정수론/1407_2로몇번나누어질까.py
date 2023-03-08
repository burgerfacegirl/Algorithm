# boj_1407_2로 몇 번 나누어질까_정수론

def find(N):
    cnt = 0
    while True:
        if N%2 == 0:
            cnt += 1
        elif N%2:
            break
        N = N//2
    return cnt

A, B = map(int, input().split())
for i in range(A, B+1):
    if i%2 == 0:
        minN, minC = i, find(i)
        break
# 5 6 7 8 9
# minN = 6, minC = 1
# 1 +
# 6 ~ 9
# 2 +
# 1
# 8
ans = minN - A
for i in range(minN, B+1):
    if i%2 == 0:
        ans += 2**minC
        minC += 1
    else:
        ans += 1


print(ans)